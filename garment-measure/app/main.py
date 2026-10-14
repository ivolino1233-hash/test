"""Garment Measure web server: phone app, measuring API, history, specs and the AI checks."""
from __future__ import annotations

import asyncio
import contextlib
import hashlib
import hmac
import io
import shutil
import time
import uuid

import cv2
import numpy as np
from fastapi import FastAPI, File, Form, HTTPException, Request, UploadFile
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import FileResponse, JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from PIL import Image, ImageOps

from cv import annotate, board, catalogue, pipeline

from . import export, netinfo, specs
from .config import ROOT, Settings, load
from .db import DB, now
from .qwen import QwenClient

STATIC = ROOT / "static"
VERSION = "1.0.0"
IMAGE_NAMES = {"photo", "rect", "annotated", "thumb"}
DEFAULT_SETTINGS = {"ruler_h_mm": board.RULER_H_MM, "ruler_v_mm": board.RULER_V_MM, "unit": "cm",
                    "auto_capture": True}


def decode_image(data: bytes, exif: bool = True) -> np.ndarray:
    try:
        img = Image.open(io.BytesIO(data))
        if exif:
            img = ImageOps.exif_transpose(img)
        return cv2.cvtColor(np.asarray(img.convert("RGB")), cv2.COLOR_RGB2BGR)
    except Exception as e:  # noqa: BLE001
        raise HTTPException(400, f"Could not read the image ({type(e).__name__}).") from e


def jpeg(img: np.ndarray, quality: int = 90, max_side: int | None = None) -> bytes:
    if max_side and max(img.shape[:2]) > max_side:
        k = max_side / max(img.shape[:2])
        img = cv2.resize(img, None, fx=k, fy=k, interpolation=cv2.INTER_AREA)
    ok, buf = cv2.imencode(".jpg", img, [cv2.IMWRITE_JPEG_QUALITY, quality])
    return buf.tobytes()


def create_app(settings: Settings | None = None, qwen_transport=None) -> FastAPI:
    st = settings or load()
    db = DB(st.data_dir / "app.db")
    scans_dir = st.data_dir / "scans"
    scans_dir.mkdir(parents=True, exist_ok=True)
    qwen = (QwenClient(st.qwen_base_url, st.qwen_api_key, st.qwen_model, st.qwen_timeout, transport=qwen_transport)
            if st.qwen_enabled else None)
    measure_slots = asyncio.Semaphore(2)
    jobs: asyncio.Queue[str] = asyncio.Queue()
    auth_token = hmac.new(st.app_pin.encode(), b"garment-measure", hashlib.sha256).hexdigest() if st.app_pin else ""

    # ---------------------------------------------------------------------------- helpers
    def app_settings() -> dict:
        return {**DEFAULT_SETTINGS, **db.get_settings()}

    def printer_scale() -> tuple[float, float]:
        s = app_settings()
        return float(s["ruler_h_mm"]) / board.RULER_H_MM, float(s["ruler_v_mm"]) / board.RULER_V_MM

    def folder(scan_id: str):
        return scans_dir / scan_id

    def render_images(scan_id: str, scan: dict) -> None:
        rect = cv2.imread(str(folder(scan_id) / "rect.jpg"))
        if rect is None:
            return
        meas = [m for m in scan["measurements"]]
        ann = annotate.draw(rect, scan["landmarks"], meas, scan["results"], scan["confidence"],
                            unit=app_settings()["unit"])
        (folder(scan_id) / "annotated.jpg").write_bytes(jpeg(ann, 88))
        (folder(scan_id) / "thumb.jpg").write_bytes(jpeg(ann, 80, max_side=480))

    def scan_json(s: dict) -> dict:
        style = db.style(s["style_id"]) if s["style_id"] else None
        spec_pts = db.spec(s["style_id"], s["size"]) if style else []
        t = int(time.time())
        return {
            "id": s["id"], "created_at": s["created_at"], "updated_at": s["updated_at"], "status": s["status"],
            "style": {"id": style["id"], "code": style["code"], "name": style["name"], "sizes": style["sizes"]}
            if style else None,
            "size": s["size"], "garment_type": s["garment_type"], "label": s["label"], "notes": s["notes"],
            "px_per_mm": s["px_per_mm"], "landmarks": s["landmarks"], "confidence": s["confidence"],
            "measurements": s["measurements"], "results": s["results"], "warnings": s["warnings"],
            "debug": s["debug"], "params": s["params"], "ai_status": s["ai_status"], "ai": s["ai"],
            "pass_count": s["pass_count"], "fail_count": s["fail_count"],
            "verdict": specs.verdict(s["results"]), "spec": spec_pts,
            "defs": catalogue.defs_for(s["garment_type"]),
            "images": {n: f"/api/scans/{s['id']}/{n}.jpg?v={t}" for n in IMAGE_NAMES},
        }

    def scan_summary(s: dict, styles: dict) -> dict:
        st_ = styles.get(s["style_id"])
        return {"id": s["id"], "created_at": s["created_at"], "status": s["status"],
                "style": {"id": st_["id"], "code": st_["code"], "name": st_["name"]} if st_ else None,
                "size": s["size"], "label": s["label"], "garment_type": s["garment_type"],
                "pass_count": s["pass_count"], "fail_count": s["fail_count"], "verdict": specs.verdict(s["results"]),
                "thumb": f"/api/scans/{s['id']}/thumb.jpg"}

    async def run_ai(scan_id: str) -> None:
        s = db.scan(scan_id)
        if not s or qwen is None:
            return
        ai = dict(s["ai"] or {})
        t0 = time.time()
        style = db.style(s["style_id"]) if s["style_id"] else None
        if "check" not in ai:
            try:
                rect = cv2.imread(str(folder(scan_id) / "rect.jpg"))
                ai["check"] = await qwen.photo_check(jpeg(rect, 85, max_side=1024),
                                                     catalogue.GARMENT_TYPES[s["garment_type"]]["label"])
                ai.pop("check_error", None)
            except Exception as e:  # noqa: BLE001
                ai["check_error"] = f"{type(e).__name__}: {e}"[:300]
        try:
            issues = (ai.get("check") or {}).get("issues", [])
            ai["summary"] = await qwen.summary(style["code"] if style else "", s["size"], s["results"],
                                               specs.verdict(s["results"]), issues)
            ai.pop("summary_error", None)
        except Exception as e:  # noqa: BLE001
            ai["summary_error"] = f"{type(e).__name__}: {e}"[:300]
        ai["model"] = qwen.model
        ai["ms"] = int((time.time() - t0) * 1000)
        ok = "check" in ai or "summary" in ai
        db.update_scan(scan_id, ai_status="done" if ok else "error", ai=ai)

    async def ai_worker():
        while True:
            scan_id = await jobs.get()
            try:
                await run_ai(scan_id)
            except Exception as e:  # noqa: BLE001
                db.update_scan(scan_id, ai_status="error", ai={"error": str(e)[:300]})
            finally:
                jobs.task_done()

    def cleanup_drafts():
        for sid in db.old_drafts(st.draft_days):
            shutil.rmtree(folder(sid), ignore_errors=True)
            db.delete_scan(sid)

    @contextlib.asynccontextmanager
    async def lifespan(app: FastAPI):
        cleanup_drafts()
        task = asyncio.create_task(ai_worker())
        app.state.jobs = jobs
        try:
            yield
        finally:
            task.cancel()
            if qwen:
                await qwen.close()

    app = FastAPI(title="Garment Measure", version=VERSION, lifespan=lifespan)
    app.state.db = db
    app.state.settings = st

    @app.middleware("http")
    async def pin_guard(request: Request, call_next):
        p = request.url.path
        if auth_token and p.startswith("/api/") and p not in ("/api/login", "/api/status", "/api/connect-info") \
                and not p.startswith("/api/qr.svg"):
            if not hmac.compare_digest(request.cookies.get("gm_auth", ""), auth_token):
                return JSONResponse({"detail": "PIN required"}, status_code=401)
        return await call_next(request)

    # ---------------------------------------------------------------------------- pages & files
    app.mount("/static", StaticFiles(directory=STATIC), name="static")

    @app.get("/", include_in_schema=False)
    def index():
        return FileResponse(STATIC / "index.html", headers={"Cache-Control": "no-cache"})

    @app.get("/onboarding", include_in_schema=False)
    def onboarding():
        return FileResponse(STATIC / "onboarding.html", headers={"Cache-Control": "no-cache"})

    @app.get("/manifest.webmanifest", include_in_schema=False)
    def manifest():
        return FileResponse(STATIC / "manifest.webmanifest", media_type="application/manifest+json")

    marker_cache: dict[int, bytes] = {}

    @app.get("/marker.pdf")
    def marker_pdf(sheets: int = 1):
        n = max(1, min(int(sheets), 2))
        if n not in marker_cache:
            buf = io.BytesIO()
            board.write_pdf(buf, sheets=tuple(range(n)))
            marker_cache[n] = buf.getvalue()
        return Response(marker_cache[n], media_type="application/pdf",
                        headers={"Content-Disposition": f'inline; filename="garment-measure-sheets-{n}.pdf"'})

    @app.get("/ca.crt", include_in_schema=False)
    def ca_cert():
        if not st.ca_file.exists():
            raise HTTPException(404, "No local certificate authority yet - run scripts/make_cert.sh")
        return FileResponse(st.ca_file, media_type="application/x-x509-ca-cert", filename="garment-measure-ca.crt")

    @app.get("/api/qr.svg")
    def qr_svg(text: str):
        import qrcode
        import qrcode.image.svg

        img = qrcode.make(text[:500], image_factory=qrcode.image.svg.SvgPathImage, box_size=12, border=2)
        buf = io.BytesIO()
        img.save(buf)
        return Response(buf.getvalue(), media_type="image/svg+xml")

    @app.get("/api/connect-info")
    def connect_info():
        ips = netinfo.lan_ips()
        host = netinfo.hostname()
        return {"ips": ips, "hostname": host, "ca": st.ca_file.exists(), "https": st.cert_file.exists(),
                "https_urls": [f"https://{ip}:{st.https_port}" for ip in ips],
                "http_urls": [f"http://{ip}:{st.http_port}" for ip in ips]}

    # ---------------------------------------------------------------------------- status & settings
    @app.get("/api/status")
    async def status():
        q = {"enabled": False}
        if qwen:
            q = {"enabled": True, "base_url": st.qwen_base_url, **(await qwen.status())}
        return {"version": VERSION, "pin_required": bool(st.app_pin), "qwen": q, "queue": jobs.qsize()}

    @app.post("/api/login")
    async def login(request: Request):
        body = await request.json()
        if not st.app_pin or hmac.compare_digest(str(body.get("pin", "")), st.app_pin):
            r = JSONResponse({"ok": True})
            if auth_token:
                r.set_cookie("gm_auth", auth_token, max_age=3600 * 24 * 365, httponly=True, samesite="lax")
            return r
        raise HTTPException(401, "Wrong PIN")

    @app.get("/api/catalogue")
    def get_catalogue():
        return {"types": catalogue.GARMENT_TYPES, "params": catalogue.DEFAULT_PARAMS,
                "defs": {t: catalogue.defs_for(t) for t in catalogue.GARMENT_TYPES}}

    @app.get("/api/settings")
    def get_settings():
        return app_settings()

    @app.put("/api/settings")
    async def put_settings(request: Request):
        body = await request.json()
        clean = {}
        for k in ("ruler_h_mm", "ruler_v_mm"):
            if k in body:
                v = float(body[k])
                nominal = board.RULER_H_MM if k == "ruler_h_mm" else board.RULER_V_MM
                if not 0.85 * nominal <= v <= 1.15 * nominal:
                    raise HTTPException(400, f"{k} must be within 15 % of {nominal:.0f} mm")
                clean[k] = v
        if "unit" in body:
            if body["unit"] not in ("cm", "in"):
                raise HTTPException(400, "unit must be cm or in")
            clean["unit"] = body["unit"]
        if "auto_capture" in body:
            clean["auto_capture"] = bool(body["auto_capture"])
        db.set_settings(clean)
        return app_settings()

    # ---------------------------------------------------------------------------- styles
    def validate_style(body: dict) -> dict:
        code = str(body.get("code", "")).strip()
        if not code:
            raise HTTPException(400, "Style code is required")
        gt = body.get("garment_type")
        if gt not in catalogue.GARMENT_TYPES:
            raise HTTPException(400, "Unknown garment type")
        keys = {d["key"] for d in catalogue.defs_for(gt)}
        sizes = [str(x).strip() for x in body.get("sizes", []) if str(x).strip()]
        spec = []
        for p in body.get("spec", []):
            if p.get("key") not in keys:
                raise HTTPException(400, f"Unknown measurement point {p.get('key')}")
            if str(p.get("size")) not in sizes:
                raise HTTPException(400, f"Size {p.get('size')} is not in the size list")
            if p.get("target_mm") in (None, ""):
                continue
            spec.append({"size": str(p["size"]), "key": p["key"], "target_mm": float(p["target_mm"]),
                         "tol_minus_mm": abs(float(p.get("tol_minus_mm", 10))),
                         "tol_plus_mm": abs(float(p.get("tol_plus_mm", p.get("tol_minus_mm", 10))))})
        params = {k: float(v) for k, v in (body.get("params") or {}).items() if k in catalogue.DEFAULT_PARAMS}
        return {"code": code, "name": str(body.get("name", "")), "customer": str(body.get("customer", "")),
                "garment_type": gt, "sizes": sizes, "params": params, "notes": str(body.get("notes", "")),
                "spec": spec}

    @app.get("/api/styles")
    def list_styles():
        return db.styles()

    @app.post("/api/styles")
    async def create_style(request: Request):
        data = validate_style(await request.json())
        if db.style_by_code(data["code"]):
            raise HTTPException(409, f"Style {data['code']} already exists")
        return db.style(db.save_style(data))

    @app.get("/api/styles/template.csv")
    def spec_template():
        return Response(specs.template_csv(), media_type="text/csv",
                        headers={"Content-Disposition": 'attachment; filename="spec-template.csv"'})

    @app.get("/api/styles/{style_id}")
    def get_style(style_id: int):
        s = db.style(style_id)
        if not s:
            raise HTTPException(404, "Style not found")
        return s

    @app.put("/api/styles/{style_id}")
    async def update_style(style_id: int, request: Request):
        if not db.style(style_id):
            raise HTTPException(404, "Style not found")
        data = validate_style(await request.json())
        other = db.style_by_code(data["code"])
        if other and other["id"] != style_id:
            raise HTTPException(409, f"Style {data['code']} already exists")
        db.save_style(data, style_id)
        return db.style(style_id)

    @app.delete("/api/styles/{style_id}")
    def delete_style(style_id: int):
        db.delete_style(style_id)
        return {"ok": True}

    @app.post("/api/styles/import")
    async def import_styles(file: UploadFile = File(...)):
        text = (await file.read()).decode("utf-8-sig", errors="replace")
        parsed, errors = specs.parse_spec_csv(text)
        done = []
        for code, data in parsed.items():
            existing = db.style_by_code(code)
            if existing:
                old = db.style(existing["id"])
                merged = {p["size"] + "|" + p["key"]: p for p in old["spec"]}
                merged.update({p["size"] + "|" + p["key"]: p for p in data["spec"]})
                data = {**old, **{k: v for k, v in data.items() if v}, "spec": list(merged.values()),
                        "sizes": list(dict.fromkeys(old["sizes"] + data["sizes"]))}
                db.save_style(data, existing["id"])
            else:
                db.save_style(data)
            done.append(code)
        return {"imported": done, "errors": errors}

    # ---------------------------------------------------------------------------- measuring
    @app.post("/api/preview")
    async def preview(request: Request):
        data = await request.body()
        img = cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_COLOR)
        if img is None:
            raise HTTPException(400, "Send one JPEG frame as the request body")
        return await run_in_threadpool(pipeline.preview, img, pipeline.Options(printer_scale=printer_scale()))

    @app.post("/api/measure")
    async def measure(image: UploadFile = File(...), style_id: str = Form(""), size: str = Form(""),
                      garment_type: str = Form("auto"), label: str = Form("")):
        raw = await image.read()
        img = await run_in_threadpool(decode_image, raw)
        style = db.style(int(style_id)) if style_id else None
        if style_id and not style:
            raise HTTPException(404, "Style not found")
        gtype = style["garment_type"] if style else garment_type
        if gtype != "auto" and gtype not in catalogue.GARMENT_TYPES:
            raise HTTPException(400, "Unknown garment type")
        params = {**catalogue.DEFAULT_PARAMS, **(style["params"] if style else {})}
        opts = pipeline.Options(garment_type=gtype, params=params, printer_scale=printer_scale(),
                                px_per_mm=st.px_per_mm)
        async with measure_slots:
            res = await run_in_threadpool(pipeline.measure, img, opts)
        if not res["ok"]:
            return JSONResponse({"error": res["error"], "warnings": res["warnings"], "debug": res["debug"]},
                                status_code=422)
        scan_id = uuid.uuid4().hex[:12]
        f = folder(scan_id)
        f.mkdir(parents=True)
        (f / "photo.jpg").write_bytes(raw if raw[:2] == b"\xff\xd8" else jpeg(img, 92))
        (f / "rect.jpg").write_bytes(jpeg(res["rectified"], 90))
        spec_pts = db.spec(style["id"], size) if style else []
        results = specs.compare(res["measurements"], spec_pts)
        p, fl = specs.counts(results)
        t = now()
        scan = {"id": scan_id, "created_at": t, "updated_at": t, "status": "draft",
                "style_id": style["id"] if style else None, "size": size, "garment_type": res["garment_type"],
                "label": label, "notes": "", "px_per_mm": res["px_per_mm"], "landmarks": res["landmarks"],
                "confidence": res["confidence"], "measurements": res["measurements"], "results": results,
                "warnings": res["warnings"], "debug": res["debug"], "params": res["params"],
                "ai_status": "pending" if qwen else "off", "ai": {}, "pass_count": p, "fail_count": fl}
        db.insert_scan(scan)
        await run_in_threadpool(render_images, scan_id, scan)
        if qwen:
            jobs.put_nowait(scan_id)
        return scan_json(db.scan(scan_id))

    # ---------------------------------------------------------------------------- scans
    @app.get("/api/scans")
    def list_scans(style_id: int | None = None, status: str = "saved", limit: int = 100, offset: int = 0):
        styles = {s["id"]: s for s in db.styles()}
        return [scan_summary(s, styles) for s in db.scans(style_id, status, min(limit, 500), offset)]

    def get_or_404(scan_id: str) -> dict:
        s = db.scan(scan_id)
        if not s:
            raise HTTPException(404, "Scan not found")
        return s

    @app.get("/api/scans/{scan_id}")
    def get_scan(scan_id: str):
        return scan_json(get_or_404(scan_id))

    @app.get("/api/scans/{scan_id}/ai")
    def get_ai(scan_id: str):
        s = get_or_404(scan_id)
        return {"ai_status": s["ai_status"], "ai": s["ai"], "queue": jobs.qsize()}

    @app.get("/api/scans/{scan_id}/{name}.jpg")
    def scan_image(scan_id: str, name: str):
        if name not in IMAGE_NAMES or not all(c.isalnum() for c in scan_id):
            raise HTTPException(404)
        p = folder(scan_id) / f"{name}.jpg"
        if not p.exists():
            raise HTTPException(404)
        return FileResponse(p, media_type="image/jpeg", headers={"Cache-Control": "private, max-age=600"})

    @app.put("/api/scans/{scan_id}")
    async def update_scan(scan_id: str, request: Request):
        s = get_or_404(scan_id)
        body = await request.json()
        landmarks = dict(s["landmarks"])
        for k, v in (body.get("landmarks") or {}).items():
            if k in landmarks and isinstance(v, (list, tuple)) and len(v) == 2:
                landmarks[k] = [round(float(v[0]), 2), round(float(v[1]), 2)]
        style_id = s["style_id"]
        if "style_id" in body:
            style_id = int(body["style_id"]) if body["style_id"] else None
            if style_id and not db.style(style_id):
                raise HTTPException(404, "Style not found")
        size = str(body.get("size", s["size"]))
        meas = catalogue.evaluate(catalogue.defs_for(s["garment_type"]), landmarks, s["px_per_mm"])
        results = specs.compare(meas, db.spec(style_id, size) if style_id else [])
        p, fl = specs.counts(results)
        conf = dict(s["confidence"])
        for k in (body.get("landmarks") or {}):
            if k in conf:
                conf[k] = 1.0     # checked by a person
        changed = results != s["results"]
        fields = dict(landmarks=landmarks, confidence=conf, measurements=meas, results=results, style_id=style_id,
                      size=size, pass_count=p, fail_count=fl, label=str(body.get("label", s["label"])),
                      notes=str(body.get("notes", s["notes"])))
        if body.get("status") in ("saved", "draft"):
            fields["status"] = body["status"]
        if changed and qwen:
            ai = dict(s["ai"] or {})
            ai.pop("summary", None)
            fields.update(ai_status="pending", ai=ai)
        db.update_scan(scan_id, **fields)
        s = db.scan(scan_id)
        await run_in_threadpool(render_images, scan_id, s)
        if changed and qwen:
            jobs.put_nowait(scan_id)
        return scan_json(s)

    @app.delete("/api/scans/{scan_id}")
    def delete_scan(scan_id: str):
        get_or_404(scan_id)
        db.delete_scan(scan_id)
        shutil.rmtree(folder(scan_id), ignore_errors=True)
        return {"ok": True}

    # ---------------------------------------------------------------------------- export
    def export_scans(style_id: int | None):
        return db.scans(style_id, "saved", limit=100000), {s["id"]: s for s in db.styles()}

    @app.get("/api/export.csv")
    def export_csv(style_id: int | None = None):
        sc, styles = export_scans(style_id)
        return Response(export.to_csv(sc, styles), media_type="text/csv",
                        headers={"Content-Disposition": 'attachment; filename="garment-measurements.csv"'})

    @app.get("/api/export.xlsx")
    def export_xlsx(style_id: int | None = None):
        sc, styles = export_scans(style_id)
        return Response(export.to_xlsx(sc, styles),
                        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        headers={"Content-Disposition": 'attachment; filename="garment-measurements.xlsx"'})

    return app

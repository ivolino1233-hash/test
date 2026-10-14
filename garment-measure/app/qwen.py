"""Client for the local Qwen model served by vLLM (OpenAI-compatible API).

Qwen never decides pass/fail. It looks at the photo for problems (folded sleeve, wrong garment
type, sheet covered...) and writes a short plain-language note on the computed results.
"""
from __future__ import annotations

import base64
import json
import re
import time

import httpx

PHOTO_SCHEMA = {
    "type": "object",
    "properties": {
        "garment_type": {"type": "string", "enum": ["sweater", "cardigan", "tshirt", "trousers", "skirt", "other"]},
        "type_matches": {"type": "boolean"},
        "lying_flat": {"type": "boolean"},
        "sleeves_or_legs_folded": {"type": "boolean"},
        "wrinkles_or_stretching": {"type": "boolean"},
        "sheet_visible_and_flat": {"type": "boolean"},
        "issues": {"type": "array", "items": {"type": "string"}, "maxItems": 4},
        "notes": {"type": "string"},
    },
    "required": ["garment_type", "type_matches", "lying_flat", "sleeves_or_legs_folded",
                 "wrinkles_or_stretching", "sheet_visible_and_flat", "issues", "notes"],
}

SYSTEM = ("You are a quality-control assistant in a knitwear factory. Photos show one garment lying flat "
          "on a table next to a printed black-and-white reference sheet, straightened to a top-down view. "
          "Be concise and practical. Never invent measurements.")


class QwenError(Exception):
    pass


def _strip(text: str) -> str:
    text = re.sub(r"<think>.*?</think>", "", text or "", flags=re.S).strip()
    m = re.search(r"```(?:json)?\s*(.*?)```", text, flags=re.S)
    return m.group(1).strip() if m else text


def _json(text: str) -> dict:
    t = _strip(text)
    try:
        return json.loads(t)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", t, flags=re.S)
        if m:
            return json.loads(m.group(0))
        raise


class QwenClient:
    def __init__(self, base_url: str, api_key: str = "", model: str = "", timeout: float = 90.0,
                 transport: httpx.AsyncBaseTransport | None = None):
        self.base_url = base_url.rstrip("/")
        self.configured_model = model
        self.model = model
        self.timeout = timeout
        headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
        self.http = httpx.AsyncClient(base_url=self.base_url, headers=headers, timeout=timeout, transport=transport)
        self.last_error = ""
        self.supports_schema = True

    async def close(self):
        await self.http.aclose()

    async def status(self) -> dict:
        t = time.time()
        try:
            r = await self.http.get("/models", timeout=5)
            r.raise_for_status()
            ids = [m["id"] for m in r.json().get("data", [])]
            if not self.configured_model:
                qwen = [i for i in ids if "qwen" in i.lower()]
                self.model = (qwen or ids or [""])[0]
            ok = bool(self.model) and (self.model in ids or not ids)
            self.last_error = "" if ok else f"model '{self.model}' not served; available: {', '.join(ids)}"
            return {"reachable": True, "model": self.model, "models": ids, "ok": ok, "error": self.last_error,
                    "ms": int((time.time() - t) * 1000)}
        except Exception as e:  # noqa: BLE001 - report any connection problem to the UI
            self.last_error = f"{type(e).__name__}: {e}"
            return {"reachable": False, "model": self.model, "models": [], "ok": False, "error": self.last_error}

    async def _chat(self, messages, max_tokens=400, schema=None) -> str:
        if not self.model:
            st = await self.status()
            if not st["ok"]:
                raise QwenError(st["error"] or "no model")
        body = {"model": self.model, "messages": messages, "max_tokens": max_tokens, "temperature": 0.2,
                "chat_template_kwargs": {"enable_thinking": False}}
        if schema and self.supports_schema:
            body["response_format"] = {"type": "json_schema", "json_schema": {"name": "result", "schema": schema}}
        r = await self.http.post("/chat/completions", json=body)
        if r.status_code == 400 and "response_format" in body:
            # Older servers: retry once without structured output and parse the JSON from text.
            self.supports_schema = False
            body.pop("response_format")
            r = await self.http.post("/chat/completions", json=body)
        if r.status_code >= 400:
            raise QwenError(f"HTTP {r.status_code}: {r.text[:300]}")
        msg = r.json()["choices"][0]["message"]
        return msg.get("content") or ""

    async def photo_check(self, jpeg: bytes, garment_label: str) -> dict:
        b64 = base64.b64encode(jpeg).decode()
        prompt = (f"The app measured this as: {garment_label}. Check the photo. Reply with JSON only, keys: "
                  "garment_type (sweater|cardigan|tshirt|trousers|skirt|other), type_matches (bool), "
                  "lying_flat (bool), sleeves_or_legs_folded (bool), wrinkles_or_stretching (bool), "
                  "sheet_visible_and_flat (bool), issues (list of up to 4 short strings, empty if fine), "
                  "notes (one short sentence).")
        text = await self._chat([
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": [
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}},
                {"type": "text", "text": prompt},
            ]},
        ], max_tokens=300, schema=PHOTO_SCHEMA)
        data = _json(text)
        data["issues"] = [str(i) for i in (data.get("issues") or [])][:4]
        return data

    async def summary(self, style: str, size: str, results: dict, verdict: str, photo_issues: list[str]) -> str:
        lines = []
        for r in results.values():
            if r["actual_mm"] is None:
                continue
            side = {"l": " left", "r": " right"}.get(r.get("side") or "", "")
            spec = (f"spec {r['target_mm'] / 10:.1f} cm (-{r['tol_minus_mm'] / 10:.1f}/+{r['tol_plus_mm'] / 10:.1f})"
                    if r["target_mm"] is not None else "no spec")
            lines.append(f"- {r['label']}{side}: {r['actual_mm'] / 10:.1f} cm, {spec}, {r['status']}")
        prompt = (f"Style {style or '(none)'}, size {size or '-'}.\nVerdict: {verdict}\n"
                  f"Measurements:\n" + "\n".join(lines) +
                  ("\nPhoto check issues: " + "; ".join(photo_issues) if photo_issues else "") +
                  "\n\nWrite at most 4 short sentences for the QC operator: what failed and by how much, the most "
                  "likely practical causes (e.g. garment stretched or not flat when laid out, sleeve not straight, "
                  "relaxation/shrinkage), and what to re-check. Use only the numbers above. Plain text, no lists.")
        text = await self._chat([{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}],
                                max_tokens=220)
        return _strip(text)

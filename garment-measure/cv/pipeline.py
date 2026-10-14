"""Photo in -> measurements out. Also a fast `preview` for the live camera overlay."""
from __future__ import annotations

import time
from dataclasses import dataclass, field

import cv2
import numpy as np

from . import catalogue
from .geom import apply_h, disk, largest_contour, rot
from .homography import detect_sheets, fit_plane, sheet_outlines_mm
from .landmarks_bottom import skirt_landmarks, trouser_landmarks
from .landmarks_top import top_landmarks
from .orient import decide, symmetry_angle
from .rectify import axis_frame, downscale, photo_extent_mm, rotated_frame, warp
from .segment import coarse_mask, fine_mask

MESSAGES = {
    "NO_MARKER": "Reference sheet not found. Make sure the whole printed sheet is in the picture and in focus.",
    "NO_GARMENT": "No garment found. Lay it on a plain surface that contrasts with its colour.",
    "GARMENT_CUT_OFF": "Part of the garment is outside the picture. Step back or move the phone.",
    "TOUCHES_SHEET": "The garment touches the reference sheet. Leave a gap of a few centimetres.",
    "LOW_CONTRAST": "Garment and table colours are similar. Use a contrasting background for accurate edges.",
    "NO_ARMPITS": "Could not find the armpits. Spread the sleeves away from the body.",
    "NO_NECK": "Could not find the neckline. Lay the garment collar-up.",
    "NECK_UNCLEAR": "Neckline is not clear in the outline; neck width and HPS points are estimates.",
    "SHOULDER_POINT_UNCLEAR": "Shoulder seam point is not visible in the outline (drop shoulder / raglan?). "
                              "Check the shoulder points and drag them if needed.",
    "LEGS_TOUCHING": "The legs are touching. Separate them slightly so the crotch is visible, or drag the crotch point.",
    "CURVED_HEM": "The hem is curved; hem sweep is measured straight corner to corner.",
    "LOW_RESOLUTION": "The photo has few pixels per centimetre, so edges are less precise. For best accuracy use Take photo (full camera resolution) or move a little closer.",
    "STEEP_ANGLE": "The phone is tilted a lot. Hold it more directly above the garment.",
    "MARKER_BLURRY": "The reference sheet is blurry or not flat. Keep it flat and hold the phone still.",
    "TYPE_MISMATCH": "The shape does not look like the selected garment type.",
    "SLEEVE_NOT_FOUND_L": "Left sleeve not found.",
    "SLEEVE_NOT_FOUND_R": "Right sleeve not found.",
    "ONE_SHEET_FAR": "Garment extends far from the sheet. A second sheet on the other side improves accuracy.",
}

BLOCKING = {"NO_MARKER", "NO_GARMENT", "GARMENT_CUT_OFF", "NO_ARMPITS", "NO_NECK"}


@dataclass
class Options:
    garment_type: str = "auto"
    params: dict = field(default_factory=dict)
    printer_scale: tuple = (1.0, 1.0)
    px_per_mm: float = 2.0
    max_side_px: int = 4500


def _warn(code: str) -> dict:
    base = code.split(":")[0]
    return {"code": code, "message": MESSAGES.get(base, MESSAGES.get(code, code))}


def _camera_up_deg(H: np.ndarray, image_size) -> float:
    """Rotation that makes the photo's 'up' direction point up in the plane frame."""
    w, h = image_size
    c = np.array([w / 2, h / 2])
    p = apply_h(H, [c, c - [0, 100]])
    v = p[1] - p[0]
    return float(np.degrees(np.arctan2(-1, 0) - np.arctan2(v[1], v[0]))) % 360


def _exclusion(fit, frame, margin_mm: float = 10.0) -> np.ndarray:
    ex = np.zeros((frame.size[1], frame.size[0]), np.uint8)
    for quad in sheet_outlines_mm(fit, margin_mm):
        cv2.fillPoly(ex, [np.round(frame.to_px(quad)).astype(np.int32)], 1)
    return ex > 0


def _coarse(image, fit, s0: float, max_side: int):
    small, k = downscale(image, max_side)
    h, w = image.shape[:2]
    sheet_c = np.vstack(sheet_outlines_mm(fit)).mean(0)
    lo, hi = photo_extent_mm(fit.H, (w, h), sheet_c, limit_mm=2500)
    frame0 = axis_frame(lo, hi, s0)
    rect0, valid0 = warp(small, fit.H, frame0, k)
    exclude0 = _exclusion(fit, frame0)
    mask0, model, flags = coarse_mask(rect0, valid0, exclude0, s0)
    return frame0, mask0, model, flags


def preview(image: np.ndarray, opts: Options | None = None) -> dict:
    """Fast check for the live overlay: where are the sheet and the garment, is it ready?"""
    opts = opts or Options()
    t0 = time.time()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dets = detect_sheets(gray, opts.printer_scale)
    quads = [q.tolist() for d in dets for q in d.marker_quads]
    fit = fit_plane(dets)
    out = {"status": "NO_MARKER", "markers": quads, "outline": [], "sheets": len(dets),
           "size": [image.shape[1], image.shape[0]]}
    if fit is None:
        out["message"] = MESSAGES["NO_MARKER"]
        return out
    frame0, mask0, model, flags = _coarse(image, fit, 0.35, 900)
    status = "READY"
    for code in ("NO_GARMENT", "GARMENT_CUT_OFF", "TOUCHES_SHEET"):
        if flags.get(code):
            status = code
            break
    if status != "NO_GARMENT":
        c = largest_contour(mask0)
        if c is not None:
            c = cv2.approxPolyDP(c.astype(np.float32).reshape(-1, 1, 2), 2.0, True).reshape(-1, 2)
            out["outline"] = apply_h(fit.H_inv, frame0.to_mm(c)).round(1).tolist()
    out["status"] = status
    out["message"] = "Ready - hold still" if status == "READY" else MESSAGES[status]
    out["low_contrast"] = bool(flags.get("LOW_CONTRAST"))
    out["ms"] = int((time.time() - t0) * 1000)
    return out


def measure(image: np.ndarray, opts: Options | None = None) -> dict:
    opts = opts or Options()
    params = {**catalogue.DEFAULT_PARAMS, **(opts.params or {})}
    t0 = time.time()
    h, w = image.shape[:2]
    res = {"ok": False, "error": None, "warnings": [], "debug": {}}

    def fail(code):
        res["error"] = _warn(code)
        res["debug"]["ms"] = int((time.time() - t0) * 1000)
        return res

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dets = detect_sheets(gray, opts.printer_scale)
    fit = fit_plane(dets)
    if fit is None:
        return fail("NO_MARKER")
    res["debug"].update(sheets=fit.sheets, rms_px=round(fit.rms_px, 3), tilt_deg=round(fit.tilt_deg((w, h)), 1),
                        points=fit.n_points)

    s0 = 0.5
    frame0, mask0, model, flags = _coarse(image, fit, s0, 1600)
    if flags.get("NO_GARMENT"):
        return fail("NO_GARMENT")
    if flags.get("GARMENT_CUT_OFF"):
        return fail("GARMENT_CUT_OFF")
    warns = [c for c in ("TOUCHES_SHEET", "LOW_CONTRAST") if flags.get(c)]

    cam_up = _camera_up_deg(fit.H, (w, h))
    axis, sym, cpx = symmetry_angle(mask0, s0, prefer_deg=cam_up % 180)
    angle, fam, notes = decide(mask0, s0, cpx, axis, opts.garment_type, catalogue.family, cam_up)
    for n in notes:
        if n.startswith("auto_family"):
            continue
        warns.append(n)
    gtype = opts.garment_type if opts.garment_type != "auto" else {"top": "sweater", "trousers": "trousers",
                                                                     "skirt": "skirt"}[fam]

    # Fine, upright frame around the garment.
    c0 = largest_contour(mask0)
    pts_mm = frame0.to_mm(c0)
    centroid_mm = frame0.to_mm([cpx])[0]
    R = rot(angle)
    q = (pts_mm - centroid_mm) @ R.T
    qlo, qhi = q.min(0) - 40, q.max(0) + 40
    center = centroid_mm + R.T @ ((qlo + qhi) / 2)
    half = (qhi - qlo) / 2
    s = opts.px_per_mm
    s = min(s, opts.max_side_px / (2 * half.max()))
    frame = rotated_frame(center, angle, half, s)
    rect, valid = warp(image, fit.H, frame, 1.0)
    exclude = _exclusion(fit, frame)
    M = frame.A @ np.linalg.inv(frame0.A)
    region = cv2.warpPerspective(mask0.astype(np.uint8) * 255, M, frame.size, flags=cv2.INTER_NEAREST) > 0
    region = cv2.dilate(region.astype(np.uint8), disk(12 * s)) > 0
    mask = fine_mask(rect, valid, exclude, s, model, region)

    if fam == "top":
        L, conf, lw = top_landmarks(mask, s, params)
    elif fam == "trousers":
        L, conf, lw = trouser_landmarks(mask, s, params)
    else:
        L, conf, lw = skirt_landmarks(mask, s, params)
    warns += lw

    photo_res = fit.px_per_mm_at(centroid_mm)
    if photo_res < 1.2:
        warns.append("LOW_RESOLUTION")
    if res["debug"]["tilt_deg"] > 35:
        warns.append("STEEP_ANGLE")
    if fit.rms_px > 1.0:
        warns.append("MARKER_BLURRY")
    if len(fit.sheets) == 1:
        sheet_c = sheet_outlines_mm(fit)[0].mean(0)
        if np.max(np.linalg.norm(pts_mm - sheet_c, axis=1)) > 1100:
            warns.append("ONE_SHEET_FAR")

    landmarks = {k: [round(float(v[0]), 2), round(float(v[1]), 2)] for k, v in L.items() if v is not None}
    defs = catalogue.defs_for(gtype)
    meas = catalogue.evaluate(defs, landmarks, s)
    blocking = [x for x in warns if x in BLOCKING]
    if blocking:
        res["error"] = _warn(blocking[0])
    res.update(
        ok=not blocking,
        garment_type=gtype,
        family=fam,
        px_per_mm=s,
        landmarks=landmarks,
        confidence={k: round(float(v), 2) for k, v in conf.items()},
        measurements=meas,
        defs=defs,
        params=params,
        warnings=[_warn(x) for x in dict.fromkeys(warns)],
        rectified=rect,
        mask=mask,
    )
    res["debug"].update(photo_px_per_mm=round(photo_res, 2), symmetry=round(sym, 3), angle_deg=round(angle, 2),
                        contrast=round(model.contrast, 1), threshold=round(model.threshold, 1),
                        ms=int((time.time() - t0) * 1000), rect_size=list(frame.size))
    return res

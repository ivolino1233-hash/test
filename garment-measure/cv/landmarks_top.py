"""Landmarks on an upright flat-lay top (sweater, cardigan, T-shirt).

Input: upright garment mask (collar at the top), s px/mm. Output: landmark name -> (x, y) in
mask px, a confidence per landmark and warning codes.
"""
from __future__ import annotations

import cv2
import numpy as np

from .geom import (bend_deg, fit_polyline, largest_contour, march_to_edge, nearest_index, path_between,
                   push_out, refine_corner, row_runs, unit)


def _corner(contour, i, s, far_mm=40.0):
    x = refine_corner(contour, i, s, far_mm=far_mm)
    return x if x is not None else push_out(contour, i)


def _profiles(mask: np.ndarray):
    h, w = mask.shape
    has = mask.any(axis=0)
    top = np.where(has, np.argmax(mask, axis=0), h).astype(np.float64)
    bot = np.where(has, h - 1 - np.argmax(mask[::-1], axis=0), -1).astype(np.float64)
    return has, top, bot


def _smooth(v: np.ndarray, sigma_px: float) -> np.ndarray:
    k = int(3 * sigma_px) * 2 + 1
    return cv2.GaussianBlur(v.reshape(1, -1).astype(np.float64), (k, 1), sigma_px,
                            borderType=cv2.BORDER_REPLICATE).ravel()


def _armpits(contour, mask, s):
    h_img = mask.shape[0]
    ys = contour[:, 1]
    y0, y1 = ys.min(), ys.max()
    H = y1 - y0
    cx = contour[:, 0].mean()
    ci = contour.astype(np.int32).reshape(-1, 1, 2)
    hull = cv2.convexHull(ci, returnPoints=False)
    try:
        defects = cv2.convexityDefects(ci, hull)
    except cv2.error:
        defects = None
    best = {"l": None, "r": None}
    if defects is None:
        return best, cx
    for s0, e0, f, d in defects.reshape(-1, 4):
        depth = d / 256.0 / s
        x, y = contour[f]
        rel = (y - y0) / H
        if depth < 20 or not (0.08 <= rel <= 0.75) or abs(x - cx) < 20 * s:
            continue
        side = "l" if x < cx else "r"
        if best[side] is None or depth > best[side][0]:
            best[side] = (depth, int(f))
    return best, cx


def top_landmarks(mask: np.ndarray, s: float, params: dict):
    L, conf, warn = {}, {}, []
    contour = largest_contour(mask)
    if contour is None:
        return L, conf, ["NO_GARMENT"]
    n = len(contour)
    arm, cx = _armpits(contour, mask, s)
    if arm["l"] is None or arm["r"] is None:
        return L, conf, ["NO_ARMPITS"]
    for side in ("l", "r"):
        L[f"armpit_{side}"] = _corner(contour, arm[side][1], s)
        conf[f"armpit_{side}"] = 1.0

    has, top, bot = _profiles(mask)
    cols = np.arange(mask.shape[1])
    top_s = _smooth(np.where(has, top, np.nan_to_num(top, nan=mask.shape[0])), 3 * s)
    win = has & (np.abs(cols - cx) <= 60 * s)
    if not win.any():
        return L, conf, ["NO_NECK"]
    x_dip = int(cols[win][np.argmax(top_s[win])])
    left = has & (cols >= x_dip - 150 * s) & (cols <= x_dip - 5 * s)
    right = has & (cols <= x_dip + 150 * s) & (cols >= x_dip + 5 * s)
    if not left.any() or not right.any():
        return L, conf, ["NO_NECK"]
    xl = int(cols[left][np.argmin(top[left])])
    xr = int(cols[right][np.argmin(top[right])])
    hps = {}
    for side, x in (("l", xl), ("r", xr)):
        i = nearest_index(contour, (x, top[x]))
        p = refine_corner(contour, i, s, near_mm=4, far_mm=35, max_move_mm=8)
        hps[side] = p if p is not None else np.array([x, top[x] - 0.5])
    L["hps_l"], L["hps_r"] = hps["l"], hps["r"]
    # Centre back neck: on the garment's axis, i.e. midway between the two HPS points.
    x_dip = int(round((hps["l"][0] + hps["r"][0]) / 2))
    L["cb_neck"] = np.array([(hps["l"][0] + hps["r"][0]) / 2, top[x_dip] - 0.5])
    dip = top_s[x_dip] - (top_s[xl] + top_s[xr]) / 2
    neck_conf = 1.0 if dip >= 5 * s else 0.4
    for k in ("hps_l", "hps_r", "cb_neck"):
        conf[k] = neck_conf
    if neck_conf < 1:
        warn.append("NECK_UNCLEAR")

    # Sleeve: contour path HPS -> armpit that does not pass the back neck, fitted with four straight
    # pieces: shoulder seam, sleeve top edge, cuff, underside.
    i_cb = nearest_index(contour, L["cb_neck"])
    for side in ("l", "r"):
        i_h = nearest_index(contour, L[f"hps_{side}"])
        i_a = arm[side][1]
        fwd = path_between(n, i_h, i_a)
        if i_cb in set(fwd.tolist()):
            fwd = path_between(n, i_a, i_h)[::-1]
        step = max(1, int(round(1.5 * s)))
        idx = fwd[::step]
        if idx[-1] != fwd[-1]:
            idx = np.append(idx, fwd[-1])
        pts = contour[idx]
        if len(pts) < 20:
            warn.append(f"SLEEVE_NOT_FOUND_{side.upper()}")
            continue
        b1, b2, b3 = fit_polyline(pts, 4, min_pts=max(4, int(15 * s / step)))
        sp_i, ct_i, cbt_i = idx[b1], idx[b2], idx[b3]
        cuff_len = np.linalg.norm(pts[b3] - pts[b2]) / s
        cuff_arm = max(8.0, min(40.0, 0.45 * cuff_len))
        L[f"sp_{side}"] = _corner(contour, sp_i, s)
        L[f"cuff_top_{side}"] = _corner(contour, ct_i, s, cuff_arm)
        L[f"cuff_bot_{side}"] = _corner(contour, cbt_i, s, cuff_arm)
        bend = bend_deg(pts[0], pts[b1], pts[b2])
        conf[f"sp_{side}"] = 1.0 if bend >= 10 else 0.5
        if bend < 10:
            warn.append("SHOULDER_POINT_UNCLEAR")
        conf[f"cuff_top_{side}"] = conf[f"cuff_bot_{side}"] = 1.0 if 40 <= cuff_len <= 300 else 0.4

        # Upper arm: across the sleeve axis, a fixed distance down the underside from the armpit.
        sp, ct, cbt, ap = (L[f"sp_{side}"], L[f"cuff_top_{side}"], L[f"cuff_bot_{side}"], L[f"armpit_{side}"])
        axis = unit(unit(ct - sp) + unit(cbt - ap))
        q = ap + params.get("bicep_offset_mm", 25.0) * s * unit(cbt - ap)
        perp = np.array([-axis[1], axis[0]])
        if np.dot(perp, sp - ap) < 0:
            perp = -perp
        q_in = march_to_edge(mask, q + perp * 3 * s, -perp, max_len=20 * s)
        p_out = march_to_edge(mask, q, perp, max_len=400 * s)
        L[f"bicep_in_{side}"] = q_in
        L[f"bicep_out_{side}"] = p_out
        conf[f"bicep_in_{side}"] = conf[f"bicep_out_{side}"] = 1.0

    # Chest and hem: outer extent of the body between the armpits.
    al, ar = L["armpit_l"], L["armpit_r"]
    inner = (al[0] + 5 * s, ar[0] - 5 * s)

    def body_extent(y):
        runs = [r for r in row_runs(mask, int(round(y))) if r[1] >= inner[0] and r[0] <= inner[1]]
        if not runs:
            return None
        return min(r[0] for r in runs) - 0.5, max(r[1] for r in runs) + 0.5

    y_chest = (al[1] + ar[1]) / 2 + params.get("chest_offset_mm", 25.0) * s
    ext = body_extent(y_chest)
    if ext:
        L["chest_l"], L["chest_r"] = np.array([ext[0], y_chest]), np.array([ext[1], y_chest])
        conf["chest_l"] = conf["chest_r"] = 1.0

    body_cols = has & (cols >= al[0]) & (cols <= ar[0])
    bc = cols[body_cols]
    if len(bc):
        lo, hi = np.percentile(bc, [20, 80])
        sel = body_cols & (cols >= lo) & (cols <= hi)
        bottom_y = float(np.median(bot[sel])) + 0.5
        y_hem = bottom_y - params.get("hem_offset_mm", 5.0) * s
        ext = body_extent(y_hem)
        if ext:
            L["hem_l"], L["hem_r"] = np.array([ext[0], y_hem]), np.array([ext[1], y_hem])
            conf["hem_l"] = conf["hem_r"] = 1.0
        xl = int(round(L["hps_l"][0]))
        L["len_bottom"] = np.array([xl, bot[xl] + 0.5])
        L["cb_bottom"] = np.array([x_dip, bot[x_dip] + 0.5])
        conf["len_bottom"] = conf["cb_bottom"] = 1.0
    return L, conf, warn

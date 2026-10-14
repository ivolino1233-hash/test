"""Landmarks on upright flat-lay trousers and skirts (waistband at the top)."""
from __future__ import annotations

import cv2
import numpy as np

from .geom import extreme_point, largest_contour, push_out, refine_corner, row_runs, snap_to_corner


def _corner(contour, direction, s, where=None):
    i = extreme_point(contour, direction, where)
    i = snap_to_corner(contour, i, eps_px=3 * s, max_px=12 * s)
    x = refine_corner(contour, i, s, near_mm=5, far_mm=40)
    return x if x is not None else push_out(contour, i)


def _crotch(mask, c, s, y0, y1):
    """Top of the gap between the legs. Where the legs meet in a narrow V the very tip is lost
    in the outline, so it is reconstructed by intersecting lines fitted to the two inner edges."""
    min_run = int(15 * s)
    gaps = []                       # (y, left inner edge x, right inner edge x)
    for y in range(int(y1), int(y0), -1):
        runs = row_runs(mask, y, min_run)
        if len(runs) == 2:
            gaps.append((y, runs[0][1] + 0.5, runs[1][0] - 0.5))
        elif gaps:
            break
    if len(gaps) < 0.15 * (y1 - y0):
        return None, 0.0
    g = np.array(gaps[::-1], float)            # top of the gap first
    y_top = g[0, 0] - 0.5
    x_top = (g[0, 1] + g[0, 2]) / 2
    near = g[(g[:, 0] >= y_top + 15 * s) & (g[:, 0] <= y_top + 200 * s)]
    narrow = (g[0, 2] - g[0, 1]) < 10 * s
    if len(near) >= 10 and narrow:
        aL, bL = np.polyfit(near[:, 0], near[:, 1], 1)
        aR, bR = np.polyfit(near[:, 0], near[:, 2], 1)
        if abs(aL - aR) > 1e-3:
            yi = (bR - bL) / (aL - aR)
            if y_top - 60 * s <= yi <= y_top + 1:
                return np.array([aL * yi + bL, yi]), 0.7   # reconstructed tip: worth a glance
    return np.array([x_top, y_top]), 1.0


def _outer(mask, y):
    runs = row_runs(mask, int(round(y)))
    if not runs:
        return None
    return min(r[0] for r in runs) - 0.5, max(r[1] for r in runs) + 0.5


def _top_bottom_at(mask, x):
    col = mask[:, int(round(x))]
    ys = np.flatnonzero(col)
    if len(ys) == 0:
        return None
    return ys[0] - 0.5, ys[-1] + 0.5


def trouser_landmarks(mask: np.ndarray, s: float, params: dict):
    L, conf, warn = {}, {}, []
    c = largest_contour(mask)
    if c is None:
        return L, conf, ["NO_GARMENT"]
    h, w = mask.shape
    ys = c[:, 1]
    y0, y1 = ys.min(), ys.max()
    min_run = int(15 * s)

    crotch, crotch_conf = _crotch(mask, c, s, y0, y1)
    if crotch is None:
        warn.append("LEGS_TOUCHING")
        ci = c.astype(np.int32).reshape(-1, 1, 2)
        try:
            d = cv2.convexityDefects(ci, cv2.convexHull(ci, returnPoints=False))
        except cv2.error:
            d = None
        cand = []
        width = c[:, 0].max() - c[:, 0].min()
        if d is not None:
            for s0, e0, f, dd in d.reshape(-1, 4):
                x, y = c[f]
                if (dd / 256 / s >= 15 and abs(x - c[:, 0].mean()) < 0.2 * width
                        and y > y0 + 0.2 * (y1 - y0)):
                    cand.append((dd, f))
        if cand:
            crotch = c[max(cand)[1]]
            conf["crotch"] = 0.5
        else:
            crotch = np.array([c[:, 0].mean(), y0 + 0.3 * (y1 - y0)])
            conf["crotch"] = 0.1
    else:
        conf["crotch"] = crotch_conf
    L["crotch"] = crotch

    upper = c[:, 1] < crotch[1]
    L["waist_l"] = _corner(c, (-1, -1.5), s, upper)
    L["waist_r"] = _corner(c, (1, -1.5), s, upper)
    tb = _top_bottom_at(mask, crotch[0])
    L["waist_c"] = np.array([crotch[0], tb[0]]) if tb else None
    y_hip = (L["waist_l"][1] + L["waist_r"][1]) / 2 + params.get("hip_offset_mm", 180.0) * s
    ext = _outer(mask, y_hip)
    if ext:
        L["hip_l"], L["hip_r"] = np.array([ext[0], y_hip]), np.array([ext[1], y_hip])

    below = c[:, 1] > crotch[1]
    left, right = below & (c[:, 0] < crotch[0]), below & (c[:, 0] > crotch[0])
    if left.any() and right.any():
        L["leg_out_l"] = _corner(c, (-1, 1.5), s, left)
        L["leg_in_l"] = _corner(c, (1, 1.5), s, left)
        L["leg_out_r"] = _corner(c, (1, 1.5), s, right)
        L["leg_in_r"] = _corner(c, (-1, 1.5), s, right)
    y_th = crotch[1] + params.get("thigh_offset_mm", 25.0) * s
    runs = row_runs(mask, int(round(y_th)), min_run)
    lr = [r for r in runs if (r[0] + r[1]) / 2 < crotch[0]]
    rr = [r for r in runs if (r[0] + r[1]) / 2 > crotch[0]]
    if len(runs) == 1:
        # Legs touching: split the single run at the crotch.
        r = runs[0]
        lr, rr = [(r[0], int(crotch[0]))], [(int(crotch[0]), r[1])]
    if lr:
        L["thigh_out_l"], L["thigh_in_l"] = np.array([lr[0][0] - 0.5, y_th]), np.array([lr[-1][1] + 0.5, y_th])
    if rr:
        L["thigh_in_r"], L["thigh_out_r"] = np.array([rr[0][0] - 0.5, y_th]), np.array([rr[-1][1] + 0.5, y_th])
    crotch_conf = conf["crotch"]
    for k in L:
        depends_on_crotch = k.startswith(("thigh", "leg_in", "waist_c"))
        conf.setdefault(k, min(1.0, crotch_conf + 0.3) if depends_on_crotch else 1.0)
    return L, conf, warn


def skirt_landmarks(mask: np.ndarray, s: float, params: dict):
    L, conf, warn = {}, {}, []
    c = largest_contour(mask)
    if c is None:
        return L, conf, ["NO_GARMENT"]
    cy = (c[:, 1].min() + c[:, 1].max()) / 2
    L["waist_l"] = _corner(c, (-1, -1.5), s, c[:, 1] < cy)
    L["waist_r"] = _corner(c, (1, -1.5), s, c[:, 1] < cy)
    L["hem_l"] = _corner(c, (-1, 1.5), s, c[:, 1] > cy)
    L["hem_r"] = _corner(c, (1, 1.5), s, c[:, 1] > cy)
    xc = (L["waist_l"][0] + L["waist_r"][0]) / 2
    tb = _top_bottom_at(mask, xc)
    if tb:
        L["top_c"], L["bottom_c"] = np.array([xc, tb[0]]), np.array([xc, tb[1]])
    y_hip = (L["waist_l"][1] + L["waist_r"][1]) / 2 + params.get("hip_offset_mm", 180.0) * s
    ext = _outer(mask, y_hip)
    if ext:
        L["hip_l"], L["hip_r"] = np.array([ext[0], y_hip]), np.array([ext[1], y_hip])
    for k in L:
        conf[k] = 1.0
    hem_curve = abs(L["bottom_c"][1] - (L["hem_l"][1] + L["hem_r"][1]) / 2) / s if tb else 0
    if hem_curve > 15:
        warn.append("CURVED_HEM")
    return L, conf, warn

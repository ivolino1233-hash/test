"""Straighten the garment (mirror-symmetry axis) and decide which end is up / what it is."""
from __future__ import annotations

import cv2
import numpy as np

from .geom import largest_contour, rot, row_runs


def _rotate_mask(mask: np.ndarray, centroid, angle_deg: float, D: int) -> np.ndarray:
    R = rot(angle_deg)
    t = np.array([D / 2, D / 2]) - R @ np.asarray(centroid)
    M = np.hstack([R, t[:, None]]).astype(np.float32)
    return cv2.warpAffine(mask, M, (D, D), flags=cv2.INTER_NEAREST) > 0


def _sym_score(r: np.ndarray, max_shift: int) -> float:
    m = r[:, ::-1]
    best = 0.0
    for d in range(-max_shift, max_shift + 1):
        mm = np.roll(m, d, axis=1)
        inter = np.count_nonzero(r & mm)
        union = np.count_nonzero(r | mm)
        best = max(best, inter / union if union else 0.0)
    return best


def symmetry_angle(mask: np.ndarray, s: float, prefer_deg: float | None = None):
    """Rotation (deg, applied to plane points about the mask centroid) that makes the garment's
    mirror axis vertical. Returns (angle in [0,180), score, centroid_px)."""
    target_s = 0.2
    k = target_s / s
    small = cv2.resize(mask.astype(np.uint8), None, fx=k, fy=k, interpolation=cv2.INTER_AREA) if k < 1 else \
        mask.astype(np.uint8)
    ys, xs = np.nonzero(small)
    c = np.array([xs.mean(), ys.mean()])
    D = int(2 * np.max(np.hypot(xs - c[0], ys - c[1]))) + 8
    shift = max(2, int(round(20 * target_s)))
    angles = np.arange(0, 180, 3.0)
    scores = np.array([_sym_score(_rotate_mask(small, c, a, D), shift) for a in angles])

    # Candidates: local maxima close to the best; prefer the one closest to the camera's "up".
    n = len(angles)
    peaks = [i for i in range(n) if scores[i] >= scores[(i - 1) % n] and scores[i] >= scores[(i + 1) % n]]
    good = [i for i in peaks if scores[i] >= scores.max() - 0.03]
    if prefer_deg is not None and len(good) > 1:
        def dist(i):
            d = abs((angles[i] - prefer_deg + 90) % 180 - 90)
            return d
        i0 = min(good, key=dist)
    else:
        i0 = int(np.argmax(scores))
    fine = np.arange(angles[i0] - 3, angles[i0] + 3.01, 0.25)
    fs = np.array([_sym_score(_rotate_mask(small, c, a, D), shift) for a in fine])
    a = float(fine[int(np.argmax(fs))]) % 180
    return a, float(fs.max()), c / k


def upright(mask: np.ndarray, centroid, angle_deg: float) -> np.ndarray:
    """Mask rotated by angle about centroid into a square canvas (for feature checks)."""
    ys, xs = np.nonzero(mask)
    D = int(2 * np.max(np.hypot(xs - centroid[0], ys - centroid[1]))) + 8
    m = _rotate_mask(mask.astype(np.uint8), centroid, angle_deg, D).astype(np.uint8)
    ys, xs = np.nonzero(m)
    return m[ys.min():ys.max() + 1, xs.min():xs.max() + 1]


def side_defects(m: np.ndarray, s: float, min_depth_mm: float = 20.0):
    """Deep concavities on both sides of the axis (armpits). Returns (found, mean relative y)."""
    c = largest_contour(m)
    if c is None or len(c) < 10:
        return False, None
    ci = c.astype(np.int32).reshape(-1, 1, 2)
    hull = cv2.convexHull(ci, returnPoints=False)
    try:
        defects = cv2.convexityDefects(ci, hull)
    except cv2.error:
        return False, None
    if defects is None:
        return False, None
    h, w = m.shape
    cx = w / 2
    left, right = [], []
    for s0, e0, f, d in defects.reshape(-1, 4):
        depth = d / 256.0 / s
        x, y = c[f]
        if depth < min_depth_mm or abs(x - cx) < 0.06 * w or not (0.05 * h < y < 0.95 * h):
            continue
        (left if x < cx else right).append((depth, y / h))
    if not left or not right:
        return False, None
    yl = max(left)[1]
    yr = max(right)[1]
    return True, (yl + yr) / 2


def legs_at_bottom(m: np.ndarray, s: float) -> bool:
    """Two leg runs at the bottom that merge into one going up (trousers), not three (top)."""
    h, w = m.shape
    min_run = int(15 * s)
    counts = [len(row_runs(m, y, min_run)) for y in range(h - 1, -1, -1)]
    bottom = counts[: max(3, int(0.12 * h))]
    if np.mean([c == 2 for c in bottom]) < 0.7:
        return False
    for c in counts[len(bottom):]:
        if c == 1:
            return True
        if c >= 3:
            return False
    return False


def width_near(m: np.ndarray, top: bool, frac: float = 0.05) -> float:
    h = m.shape[0]
    ys = range(0, max(1, int(frac * h))) if top else range(h - max(1, int(frac * h)), h)
    return float(np.mean([np.count_nonzero(m[y]) for y in ys]))


def decide(mask: np.ndarray, s: float, centroid, axis_deg: float, requested: str, family_of, cam_up_deg=None):
    """Choose the final rotation (axis_deg or axis_deg+180) and the garment family.
    Returns (angle_deg, family, notes)."""
    notes = []
    up = upright(mask, centroid, axis_deg)
    down = up[::-1, ::-1]

    def cam_choice():
        if cam_up_deg is None:
            return axis_deg
        d0 = abs((axis_deg - cam_up_deg + 180) % 360 - 180)
        return axis_deg if d0 <= 90 else axis_deg + 180

    fam_req = family_of(requested) if requested != "auto" else None
    found, ry = side_defects(up, s)
    legs_up, legs_down = legs_at_bottom(up, s), legs_at_bottom(down, s)

    fam = fam_req
    if fam is None:
        if found:
            fam = "top"
        elif legs_up or legs_down:
            fam = "trousers"
        else:
            fam = "skirt"
        notes.append(f"auto_family:{fam}")

    if fam == "top":
        if found:
            ang = axis_deg if ry < 0.5 else axis_deg + 180
        else:
            ang = cam_choice()
            notes.append("NO_ARMPITS")
    elif fam == "trousers":
        if legs_up != legs_down:
            ang = axis_deg if legs_up else axis_deg + 180
        else:
            ang = cam_choice()
            if not (legs_up or legs_down):
                notes.append("LEGS_TOUCHING")
    else:
        wt, wb = width_near(up, True), width_near(up, False)
        if abs(wt - wb) > 0.05 * max(wt, wb):
            ang = axis_deg if wt < wb else axis_deg + 180
        else:
            ang = cam_choice()
    if fam_req and fam_req != "top" and found:
        notes.append("TYPE_MISMATCH:top")
    if fam_req and fam_req != "trousers" and (legs_up or legs_down) and not found:
        notes.append("TYPE_MISMATCH:trousers")
    return ang % 360, fam, notes

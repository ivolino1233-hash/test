"""Small geometry helpers shared by the vision modules (numpy + OpenCV only)."""
from __future__ import annotations

import cv2
import numpy as np


def apply_h(H: np.ndarray, pts) -> np.ndarray:
    """Apply a 3x3 homography to (N,2) points."""
    p = np.asarray(pts, dtype=np.float64).reshape(-1, 2)
    q = np.hstack([p, np.ones((len(p), 1))]) @ H.T
    return q[:, :2] / q[:, 2:3]


def rigid_fit(src: np.ndarray, dst: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Rotation R (2x2) and translation t minimising |R src + t - dst| (no scale)."""
    cs, cd = src.mean(0), dst.mean(0)
    U, _, Vt = np.linalg.svd((src - cs).T @ (dst - cd))
    R = (U @ Vt).T
    if np.linalg.det(R) < 0:
        Vt[-1] *= -1
        R = (U @ Vt).T
    return R, cd - R @ cs


def rot(deg: float) -> np.ndarray:
    a = np.deg2rad(deg)
    return np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]])


def unit(v) -> np.ndarray:
    v = np.asarray(v, dtype=np.float64)
    n = np.linalg.norm(v)
    return v / n if n > 1e-12 else v


def largest_contour(mask: np.ndarray) -> np.ndarray | None:
    cs, _ = cv2.findContours(mask.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if not cs:
        return None
    c = max(cs, key=cv2.contourArea).reshape(-1, 2).astype(np.float64)
    # Enforce clockwise order on screen (y down): positive shoelace area.
    x, y = c[:, 0], c[:, 1]
    if np.sum(x * np.roll(y, -1) - np.roll(x, -1) * y) < 0:
        c = c[::-1].copy()
    return c


def row_runs(mask: np.ndarray, y: int, min_len: int = 1) -> list[tuple[int, int]]:
    """Inclusive (start, end) column runs of nonzero pixels on row y."""
    if y < 0 or y >= mask.shape[0]:
        return []
    row = np.concatenate([[0], (mask[y] > 0).astype(np.int8), [0]])
    d = np.diff(row)
    starts, ends = np.flatnonzero(d == 1), np.flatnonzero(d == -1) - 1
    return [(int(s), int(e)) for s, e in zip(starts, ends) if e - s + 1 >= min_len]


def fill_holes(mask: np.ndarray) -> np.ndarray:
    m = (mask > 0).astype(np.uint8)
    cs, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    out = np.zeros_like(m)
    cv2.drawContours(out, cs, -1, 1, thickness=cv2.FILLED)
    return out


def largest_component(mask: np.ndarray) -> np.ndarray:
    n, lab, stats, _ = cv2.connectedComponentsWithStats((mask > 0).astype(np.uint8), connectivity=8)
    if n <= 1:
        return np.zeros_like(mask, dtype=np.uint8)
    k = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
    return (lab == k).astype(np.uint8)


def disk(radius_px: float) -> np.ndarray:
    r = max(1, int(round(radius_px)))
    return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * r + 1, 2 * r + 1))


def segment_sse_table(pts: np.ndarray) -> np.ndarray:
    """SSE of the best-fit (orthogonal) line through pts[i..j] for every i<=j, via prefix sums."""
    n = len(pts)
    x, y = pts[:, 0] - pts[:, 0].mean(), pts[:, 1] - pts[:, 1].mean()
    P = lambda v: np.concatenate([[0.0], np.cumsum(v)])  # noqa: E731
    Sx, Sy, Sxx, Syy, Sxy = P(x), P(y), P(x * x), P(y * y), P(x * y)
    i = np.arange(n)[:, None]
    j = np.arange(n)[None, :]
    cnt = (j - i + 1).astype(np.float64)
    valid = cnt >= 1
    cnt = np.where(valid, cnt, 1.0)
    sx, sy = Sx[j + 1] - Sx[i], Sy[j + 1] - Sy[i]
    cxx = (Sxx[j + 1] - Sxx[i]) - sx * sx / cnt
    cyy = (Syy[j + 1] - Syy[i]) - sy * sy / cnt
    cxy = (Sxy[j + 1] - Sxy[i]) - sx * sy / cnt
    tr, det = cxx + cyy, cxx * cyy - cxy * cxy
    lam_min = tr / 2 - np.sqrt(np.maximum(tr * tr / 4 - det, 0))
    return np.where(valid, np.maximum(lam_min, 0), np.inf)


def fit_polyline(pts: np.ndarray, n_seg: int, min_pts: int = 4) -> list[int]:
    """Indices of the n_seg-1 breakpoints of the least-squares n_seg-segment polyline
    through pts (endpoints fixed). Segments share their breakpoints."""
    n = len(pts)
    sse = segment_sse_table(pts)
    i = np.arange(n)[:, None]
    j = np.arange(n)[None, :]
    sse = np.where(j - i + 1 >= min_pts, sse, np.inf)
    cost = sse[0].copy()          # cost of 1 segment ending at j
    back = []
    for _ in range(n_seg - 1):
        total = cost[:, None] + sse      # break at i, segment i..j
        arg = np.argmin(total, axis=0)
        cost = total[arg, np.arange(n)]
        back.append(arg)
    idx = [n - 1]
    for arg in reversed(back):
        idx.append(int(arg[idx[-1]]))
    return list(reversed(idx[1:]))


def bend_deg(a, b, c) -> float:
    """Angle (degrees) by which the direction a->b turns to b->c."""
    u, v = unit(np.subtract(b, a)), unit(np.subtract(c, b))
    return float(np.degrees(np.arccos(np.clip(np.dot(u, v), -1, 1))))


def push_out(contour: np.ndarray, idx: int, amount: float = 0.5, span: int = 4) -> np.ndarray:
    """Contour point idx moved `amount` px outward along the normal (contour is clockwise on screen),
    so landmarks sit on the true edge rather than on the centre of the boundary pixel."""
    n = len(contour)
    t = unit(contour[(idx + span) % n] - contour[(idx - span) % n])
    normal = np.array([t[1], -t[0]])  # clockwise on screen (y down): this normal points outward
    return contour[idx] + amount * normal


def fit_line(pts: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Total-least-squares line: (point on line, unit direction)."""
    c = pts.mean(0)
    _, _, Vt = np.linalg.svd(pts - c)
    return c, Vt[0]


def intersect_lines(p, d, q, e):
    A = np.array([d, -np.asarray(e)]).T
    if abs(np.linalg.det(A)) < 1e-9:
        return None
    t, _ = np.linalg.solve(A, np.asarray(q) - np.asarray(p))
    return np.asarray(p) + t * np.asarray(d)


def refine_corner(contour: np.ndarray, idx: int, s: float, near_mm: float = 6.0, far_mm: float = 40.0,
                  min_angle: float = 12.0, max_move_mm: float = 12.0, far_mm_next: float | None = None):
    """Sharp corner as the intersection of lines fitted to the edges on either side of contour[idx].
    Removes the inward bias of rounded or filled-in corners. Returns None if not a clear corner."""
    n = len(contour)
    seg = np.linalg.norm(np.diff(contour, axis=0, append=contour[:1]), axis=1)
    fwd = np.cumsum(np.roll(seg, -idx))            # arc length from idx going forward
    bwd = np.cumsum(np.roll(seg[::-1], idx))       # going backward
    k_f = np.flatnonzero((fwd >= near_mm * s) & (fwd <= (far_mm_next or far_mm) * s))
    k_b = np.flatnonzero((bwd >= near_mm * s) & (bwd <= far_mm * s))
    if len(k_f) < 4 or len(k_b) < 4:
        return None
    pf = contour[(idx + 1 + k_f) % n]
    pb = contour[(idx - 1 - k_b) % n]
    c1, d1 = fit_line(pf)
    c2, d2 = fit_line(pb)
    ang = np.degrees(np.arccos(min(1.0, abs(float(np.dot(d1, d2))))))
    if ang < min_angle:
        return None
    x = intersect_lines(c1, d1, c2, d2)
    if x is None or np.linalg.norm(x - contour[idx]) > max_move_mm * s:
        return None
    return x


def nearest_index(contour: np.ndarray, p) -> int:
    return int(np.argmin(np.sum((contour - np.asarray(p)) ** 2, axis=1)))


def extreme_point(contour: np.ndarray, direction, where=None) -> int:
    d = unit(direction)
    score = contour @ d
    if where is not None:
        score = np.where(where, score, -np.inf)
    return int(np.argmax(score))


def snap_to_corner(contour: np.ndarray, idx: int, eps_px: float, max_px: float) -> int:
    """Move idx to the nearest polygon-approximation vertex if one is close by."""
    approx = cv2.approxPolyDP(contour.astype(np.float32).reshape(-1, 1, 2), eps_px, True).reshape(-1, 2)
    d = np.linalg.norm(approx - contour[idx], axis=1)
    k = int(np.argmin(d))
    if d[k] <= max_px:
        return nearest_index(contour, approx[k])
    return idx


def path_between(n: int, a: int, b: int) -> np.ndarray:
    """Contour indices from a to b walking forward (wrapping)."""
    if b >= a:
        return np.arange(a, b + 1)
    return np.concatenate([np.arange(a, n), np.arange(0, b + 1)])


def march_to_edge(mask: np.ndarray, start, direction, step: float = 0.5, max_len: float = 1e5) -> np.ndarray:
    """Walk from start along direction while inside the mask; return the last inside point."""
    d = unit(direction)
    p = np.asarray(start, dtype=np.float64)
    h, w = mask.shape
    last = p.copy()
    t = 0.0
    seen_inside = False
    while t < max_len:
        q = p + t * d
        x, y = int(round(q[0])), int(round(q[1]))
        if not (0 <= x < w and 0 <= y < h):
            break
        inside = mask[y, x] > 0
        if inside:
            seen_inside = True
            last = q
        elif seen_inside:
            break
        t += step
    return last + 0.5 * d

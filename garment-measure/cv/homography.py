"""Find the reference sheet(s) in a photo and fit the image -> table-plane homography (mm)."""
from __future__ import annotations

from dataclasses import dataclass, field

import cv2
import numpy as np

from . import board as B
from .geom import apply_h, rigid_fit


@dataclass
class SheetDetection:
    sheet: int
    img_pts: np.ndarray            # (N,2) image px
    obj_pts: np.ndarray            # (N,2) board mm (printer scale applied)
    n_charuco: int
    marker_quads: list = field(default_factory=list)


@dataclass
class PlaneFit:
    H: np.ndarray                  # image px -> plane mm
    H_inv: np.ndarray              # plane mm -> image px
    poses: dict                    # sheet -> (R, t): board mm -> plane mm
    rms_px: float
    n_points: int
    sheets: list
    marker_quads: list

    def px_per_mm_at(self, p_mm) -> float:
        """Photo resolution on the table at plane point p (px per mm)."""
        p = np.asarray(p_mm, dtype=np.float64)
        q = apply_h(self.H_inv, [p, p + [1, 0], p + [0, 1]])
        J = np.column_stack([q[1] - q[0], q[2] - q[0]])
        return float(np.sqrt(abs(np.linalg.det(J))))

    def tilt_deg(self, image_size) -> float:
        """Approximate camera tilt from straight-down, assuming a typical phone main lens."""
        w, h = image_size
        f = 0.75 * max(w, h)
        K = np.array([[f, 0, w / 2], [0, f, h / 2], [0, 0, 1]])
        M = np.linalg.inv(K) @ self.H_inv
        r1, r2 = M[:, 0] / np.linalg.norm(M[:, 0]), M[:, 1] / np.linalg.norm(M[:, 1])
        n = np.cross(r1, r2)
        n /= np.linalg.norm(n)
        return float(np.degrees(np.arccos(min(1.0, abs(n[2])))))


def _detector() -> cv2.aruco.ArucoDetector:
    p = cv2.aruco.DetectorParameters()
    p.cornerRefinementMethod = cv2.aruco.CORNER_REFINE_SUBPIX
    p.cornerRefinementWinSize = 5
    p.minMarkerPerimeterRate = 0.01
    return cv2.aruco.ArucoDetector(B.dictionary(), p)


def detect_sheets(gray: np.ndarray, printer_scale=(1.0, 1.0)) -> list[SheetDetection]:
    corners, ids, _ = _detector().detectMarkers(gray)
    if ids is None or len(ids) == 0:
        return []
    ids = ids.ravel()
    sx, sy = printer_scale
    out = []
    for sheet in sorted({B.sheet_of_marker(i) for i in ids if i < B.MAX_SHEETS * B.MARKERS_PER_SHEET}):
        sel = [k for k, i in enumerate(ids) if B.sheet_of_marker(i) == sheet]
        mc = tuple(corners[k] for k in sel)
        mi = ids[sel].reshape(-1, 1).astype(np.int32)
        brd = B.board(sheet)
        img_pts, obj_pts = [], []
        n_ch = 0
        if len(sel) >= 2:
            cc, ci, _, _ = cv2.aruco.CharucoDetector(brd).detectBoard(gray, markerCorners=mc, markerIds=mi)
            if cc is not None and ci is not None and len(ci) > 0:
                chess = brd.getChessboardCorners()[:, :2]
                img_pts.append(cc.reshape(-1, 2))
                obj_pts.append(chess[ci.ravel()])
                n_ch = len(ci)
        board_ids = list(brd.getIds().ravel())
        obj = brd.getObjPoints()
        quads = []
        # Chessboard corners locate ~10x more precisely than marker corners, so marker corners
        # are only used when too few chessboard corners were found (e.g. small preview frames).
        use_markers = n_ch < 6
        for k in sel:
            quads.append(corners[k].reshape(4, 2))
            if use_markers:
                j = board_ids.index(int(ids[k]))
                img_pts.append(corners[k].reshape(4, 2))
                obj_pts.append(np.asarray(obj[j])[:, :2])
        ip, op = np.vstack(img_pts).astype(np.float64), np.vstack(obj_pts).astype(np.float64)
        op = op * [sx, sy]
        out.append(SheetDetection(sheet, ip, op, n_ch, quads))
    return out


def _fit_h(obj: np.ndarray, img: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """plane->image homography with RANSAC then least-squares refit on inliers."""
    if len(obj) < 4:
        raise ValueError("need at least 4 points")
    if len(obj) > 4:
        H, inl = cv2.findHomography(obj, img, cv2.RANSAC, 3.0)
        inl = inl.ravel().astype(bool) if inl is not None else np.ones(len(obj), bool)
    else:
        inl = np.ones(len(obj), bool)
    H, _ = cv2.findHomography(obj[inl], img[inl], 0)
    return H, inl


def fit_plane(dets: list[SheetDetection]) -> PlaneFit | None:
    dets = [d for d in dets if len(d.img_pts) >= 4]
    if not dets:
        return None
    dets.sort(key=lambda d: -len(d.img_pts))
    base = dets[0]
    poses = {base.sheet: (np.eye(2), np.zeros(2))}
    H_pi, _ = _fit_h(base.obj_pts, base.img_pts)

    # Further sheets sit at unknown positions on the same table: alternate between fitting the
    # homography to all points and re-placing each extra sheet rigidly in the plane frame.
    for _ in range(6 if len(dets) > 1 else 0):
        H_ip = np.linalg.inv(H_pi)
        for d in dets[1:]:
            R, t = rigid_fit(d.obj_pts, apply_h(H_ip, d.img_pts))
            poses[d.sheet] = (R, t)
        obj = np.vstack([d.obj_pts @ poses[d.sheet][0].T + poses[d.sheet][1] for d in dets])
        img = np.vstack([d.img_pts for d in dets])
        H_pi, _ = _fit_h(obj, img)

    if len(dets) > 1:
        H_pi, poses = _refine_joint(H_pi, poses, dets)
    obj = np.vstack([d.obj_pts @ poses[d.sheet][0].T + poses[d.sheet][1] for d in dets])
    img = np.vstack([d.img_pts for d in dets])
    if len(dets) == 1:
        H_pi, inl = _fit_h(obj, img)
    else:
        inl = np.ones(len(obj), bool)
    err = np.linalg.norm(apply_h(H_pi, obj[inl]) - img[inl], axis=1)
    H_pi = H_pi / H_pi[2, 2]
    H = np.linalg.inv(H_pi)
    H /= H[2, 2]
    return PlaneFit(H=H, H_inv=H_pi, poses=poses, rms_px=float(np.sqrt(np.mean(err ** 2))),
                    n_points=int(inl.sum()), sheets=[d.sheet for d in dets],
                    marker_quads=[q for d in dets for q in d.marker_quads])


def _refine_joint(H_pi, poses, dets, iters: int = 30):
    """Levenberg-Marquardt over the homography and the rigid poses of the extra sheets,
    minimising reprojection error in the photo. Works in normalised coordinates."""
    from .geom import rot

    allimg = np.vstack([d.img_pts for d in dets])
    ci, si = allimg.mean(0), allimg.std() + 1e-9
    base_obj = np.vstack([d.obj_pts @ poses[d.sheet][0].T + poses[d.sheet][1] for d in dets])
    cp, sp = base_obj.mean(0), base_obj.std() + 1e-9
    Ni = np.array([[1 / si, 0, -ci[0] / si], [0, 1 / si, -ci[1] / si], [0, 0, 1]])
    Np = np.array([[1 / sp, 0, -cp[0] / sp], [0, 1 / sp, -cp[1] / sp], [0, 0, 1]])
    Hn = Ni @ H_pi @ np.linalg.inv(Np)
    Hn /= Hn[2, 2]
    extra = dets[1:]

    def unpack(x):
        H = np.append(x[:8], 1.0).reshape(3, 3)
        ps = {}
        for k, d in enumerate(extra):
            th, tx, ty = x[8 + 3 * k: 11 + 3 * k]
            ps[d.sheet] = (rot(np.degrees(th)), np.array([tx, ty]))
        return H, ps

    def resid(x):
        H, ps = unpack(x)
        r = []
        for d in dets:
            if d is dets[0]:
                obj = (d.obj_pts - cp) / sp
            else:
                R, t = ps[d.sheet]
                obj = (d.obj_pts @ R.T + t * sp - cp) / sp  # t is stored as t_mm / sp
            r.append(apply_h(H, obj) - (d.img_pts - ci) / si)
        return np.concatenate(r).ravel()

    x0 = list(Hn.ravel()[:8])
    for d in extra:
        R, t = poses[d.sheet]
        x0 += [np.arctan2(R[1, 0], R[0, 0]), *((t) / sp)]
    x = np.array(x0, dtype=np.float64)
    lam = 1e-3
    r = resid(x)
    cost = r @ r
    for _ in range(iters):
        J = np.empty((len(r), len(x)))
        for k in range(len(x)):
            dx = np.zeros_like(x)
            dx[k] = 1e-7
            J[:, k] = (resid(x + dx) - r) / 1e-7
        A = J.T @ J
        g = J.T @ r
        while True:
            step = np.linalg.solve(A + lam * np.diag(np.diag(A) + 1e-12), -g)
            xn = x + step
            rn = resid(xn)
            cn = rn @ rn
            if cn < cost:
                x, r, cost, lam = xn, rn, cn, max(lam / 3, 1e-9)
                break
            lam *= 4
            if lam > 1e6:
                break
        if lam > 1e6 or np.linalg.norm(step) < 1e-12:
            break
    Hn, ps = unpack(x)
    H_pi = np.linalg.inv(Ni) @ Hn @ Np
    poses = {dets[0].sheet: poses[dets[0].sheet]}
    for d in extra:
        R, t = ps[d.sheet]
        poses[d.sheet] = (R, t * sp)
    return H_pi / H_pi[2, 2], poses


def sheet_outlines_mm(fit: PlaneFit, margin_mm: float = 0.0) -> list[np.ndarray]:
    """Paper outlines (with margin) in plane mm, one 4x2 array per detected sheet."""
    x0, y0, x1, y1 = B.page_rect_mm()
    c = np.array([[x0 - margin_mm, y0 - margin_mm], [x1 + margin_mm, y0 - margin_mm],
                  [x1 + margin_mm, y1 + margin_mm], [x0 - margin_mm, y1 + margin_mm]])
    return [c @ R.T + t for R, t in (fit.poses[s] for s in fit.sheets)]

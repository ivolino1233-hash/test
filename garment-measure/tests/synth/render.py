"""Render a synthetic phone photo of a flat-lay garment next to the reference sheet(s).

The scene lives on the table plane (mm). A pinhole camera at a chosen height/tilt/yaw
projects it into the photo, supersampled and then degraded (blur, noise, JPEG).
"""
from __future__ import annotations

from dataclasses import dataclass

import cv2
import numpy as np

from cv import board as B
from cv.geom import rot

from .garments import Garment


@dataclass
class Scene:
    garment: Garment
    garment_angle: float = 0.0          # deg, garment rotation on the table
    garment_pos: tuple = (0.0, 0.0)     # garment frame origin on the table (mm)
    sheets: tuple = ((0, (-700.0, -150.0), 0.0),)  # (sheet, board-origin pos mm, angle deg)
    background: tuple = (200, 205, 210)  # BGR table colour
    printer_scale: tuple = (1.0, 1.0)


@dataclass
class Camera:
    width: int = 3000
    height: int = 2250
    fov_deg: float = 70.0
    height_mm: float = 1500.0
    tilt_deg: float = 0.0
    tilt_dir_deg: float = 0.0
    yaw_deg: float = 0.0
    target: tuple | None = None          # plane point at the image centre


def _rx(a):
    a = np.radians(a)
    return np.array([[1, 0, 0], [0, np.cos(a), -np.sin(a)], [0, np.sin(a), np.cos(a)]])


def _rz(a):
    a = np.radians(a)
    return np.array([[np.cos(a), -np.sin(a), 0], [np.sin(a), np.cos(a), 0], [0, 0, 1]])


def camera_homography(cam: Camera, target, scale: float = 1.0) -> np.ndarray:
    """Plane (mm) -> image px homography. World: x right, y down, z into the table."""
    f = (cam.width / 2) / np.tan(np.radians(cam.fov_deg / 2))
    K = np.array([[f, 0, (cam.width - 1) / 2], [0, f, (cam.height - 1) / 2], [0, 0, 1.0]])
    # Camera looking straight down has the same axes as the world; tilt about an axis in the plane.
    R_cw = _rz(cam.tilt_dir_deg) @ _rx(cam.tilt_deg) @ _rz(-cam.tilt_dir_deg) @ _rz(cam.yaw_deg)
    R = R_cw.T                                    # world -> camera
    axis = R_cw @ np.array([0, 0, 1.0])           # optical axis in world
    tx, ty = target
    d = cam.height_mm / axis[2]
    C = np.array([tx, ty, 0.0]) - d * axis
    t = -R @ C
    H = K @ np.column_stack([R[:, 0], R[:, 1], t])
    if scale != 1.0:
        S = np.array([[scale, 0, (scale - 1) / 2], [0, scale, (scale - 1) / 2], [0, 0, 1]])
        H = S @ H
    return H / H[2, 2]


def _knit_texture(h, w, color, rng):
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    rib = 0.5 + 0.5 * np.sin(xx * (2 * np.pi / 12.0))                 # ~4 mm wales at 3 px/mm
    stitch = 0.5 + 0.5 * np.sin(yy * (2 * np.pi / 9.0) + 1.5 * np.sin(xx * 0.5))
    shade = 0.82 + 0.1 * rib + 0.06 * stitch
    shade += rng.standard_normal((h, w), dtype=np.float32) * 0.03
    img = np.clip(np.stack([shade * c for c in color], axis=-1), 0, 255)
    return img.astype(np.uint8)


def render(scene: Scene, cam: Camera, seed: int = 0, px_per_mm: float = 3.0, supersample: int = 2,
           blur: float = 0.7, noise: float = 2.5, jpeg_quality: int = 88, round_mm: float = 3.0,
           edge_noise_mm: float = 1.0):
    rng = np.random.default_rng(seed)
    g = scene.garment
    R = rot(scene.garment_angle)
    poly = g.polygon @ R.T + np.asarray(scene.garment_pos)

    sheet_quads = []
    for sheet, pos, ang in scene.sheets:
        c = B.page_corners_mm() @ rot(ang).T + np.asarray(pos)
        sheet_quads.append(c)
    allp = np.vstack([poly] + sheet_quads)
    lo, hi = allp.min(0) - 250, allp.max(0) + 250
    s = px_per_mm
    W, Hh = int((hi[0] - lo[0]) * s), int((hi[1] - lo[1]) * s)

    def to_canvas(p):
        return (np.asarray(p) - lo) * s - 0.5

    # Table: colour with a lighting gradient and fine texture.
    yy, xx = np.mgrid[0:64, 0:64].astype(np.float32)
    grad = cv2.resize(0.92 + 0.08 * (xx / 63) - 0.05 * (yy / 63), (W, Hh), interpolation=cv2.INTER_LINEAR)
    canvas = np.empty((Hh, W, 3), np.float32)
    for c in range(3):
        canvas[..., c] = grad * scene.background[c]
    canvas += rng.standard_normal((Hh, W, 3), dtype=np.float32) * 3

    # Garment silhouette with rounded corners and slightly wobbly edges.
    gm = np.zeros((Hh, W), np.uint8)
    pts = to_canvas(poly)
    if edge_noise_mm:
        dense = []
        for i in range(len(pts)):
            a, b = pts[i], pts[(i + 1) % len(pts)]
            n = max(2, int(np.linalg.norm(b - a) / (10 * s)))
            seg = a + (b - a) * np.linspace(0, 1, n, endpoint=False)[:, None]
            dense.append(seg)
        dense = np.vstack(dense)
        tang = np.roll(dense, -1, 0) - np.roll(dense, 1, 0)
        nrm = np.column_stack([tang[:, 1], -tang[:, 0]])
        nrm /= np.linalg.norm(nrm, axis=1, keepdims=True) + 1e-9
        wob = cv2.GaussianBlur(rng.normal(0, 1, (len(dense), 1)).astype(np.float32), (1, 0), 6).ravel()
        wob = wob / (np.abs(wob).max() + 1e-9) * edge_noise_mm * s
        pts = dense + nrm * wob[:, None]
    cv2.fillPoly(gm, [np.round(pts * 16).astype(np.int32)], 1, lineType=cv2.LINE_8, shift=4)
    if round_mm:
        k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (int(2 * round_mm * s) | 1,) * 2)
        gm = cv2.morphologyEx(gm, cv2.MORPH_OPEN, k)

    # Soft shadow (computed at low resolution), then the knit inside the garment's bounding box.
    small = cv2.resize(np.roll(gm, (int(4 * s), int(3 * s)), (0, 1)).astype(np.float32), (W // 4, Hh // 4),
                       interpolation=cv2.INTER_AREA)
    sh = cv2.resize(cv2.GaussianBlur(small, (0, 0), 1.5 * s), (W, Hh), interpolation=cv2.INTER_LINEAR)
    canvas *= (1 - 0.18 * sh)[..., None]
    ys, xs = np.nonzero(gm)
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    tex = _knit_texture(y1 - y0, x1 - x0, g.color, rng).astype(np.float32)
    gmf = cv2.GaussianBlur(gm[y0:y1, x0:x1].astype(np.float32), (0, 0), 0.6)[..., None]
    sub = canvas[y0:y1, x0:x1]
    canvas[y0:y1, x0:x1] = sub * (1 - gmf) + tex * gmf

    # Reference sheets (paper, printed board).
    for (sheet, pos, ang), quad in zip(scene.sheets, sheet_quads):
        page = B.render_page(sheet, 6).astype(np.float32)
        sx, sy = scene.printer_scale
        ph, pw = page.shape
        src = np.array([[0, 0], [pw, 0], [pw, ph], [0, ph]], np.float32) - 0.5
        x0, y0, x1, y1 = B.page_rect_mm()
        corners_board = np.array([[x0, y0], [x1, y0], [x1, y1], [x0, y1]]) * [sx, sy]
        dst = to_canvas(corners_board @ rot(ang).T + np.asarray(pos)).astype(np.float32)
        bx0, by0 = np.floor(dst.min(0)).astype(int) - 2
        bx1, by1 = np.ceil(dst.max(0)).astype(int) + 2
        M = cv2.getPerspectiveTransform(src, (dst - [bx0, by0]).astype(np.float32))
        size = (int(bx1 - bx0), int(by1 - by0))
        warped = cv2.warpPerspective(page, M, size, flags=cv2.INTER_LINEAR, borderValue=0)
        pm = cv2.warpPerspective(np.ones_like(page), M, size, flags=cv2.INTER_LINEAR, borderValue=0)[..., None]
        paper = np.stack([warped * 0.96, warped * 0.97, warped * 0.95], -1)
        sub = canvas[by0:by1, bx0:bx1]
        canvas[by0:by1, bx0:bx1] = sub * (1 - pm) + paper * pm

    canvas = np.clip(canvas, 0, 255).astype(np.uint8)

    target = cam.target if cam.target is not None else tuple((allp.min(0) + allp.max(0)) / 2)
    H_pi = camera_homography(cam, target, scale=supersample)
    A = np.array([[1 / s, 0, lo[0] + 0.5 / s], [0, 1 / s, lo[1] + 0.5 / s], [0, 0, 1]])
    M = H_pi @ A
    big = cv2.warpPerspective(canvas, M, (cam.width * supersample, cam.height * supersample),
                              flags=cv2.INTER_LINEAR, borderValue=(30, 30, 30))
    img = cv2.resize(big, (cam.width, cam.height), interpolation=cv2.INTER_AREA)
    if blur:
        img = cv2.GaussianBlur(img, (0, 0), blur)
    if noise:
        img = np.clip(img.astype(np.float32) + rng.normal(0, noise, img.shape), 0, 255).astype(np.uint8)
    if jpeg_quality:
        ok, buf = cv2.imencode(".jpg", img, [cv2.IMWRITE_JPEG_QUALITY, jpeg_quality])
        img = cv2.imdecode(buf, cv2.IMREAD_COLOR)
    H_true = camera_homography(cam, target)    # plane mm -> photo px
    return img, H_true

"""Warp the photo into a top-down view of the table at a fixed scale (px per mm)."""
from __future__ import annotations

from dataclasses import dataclass

import cv2
import numpy as np

from .geom import apply_h, rot


@dataclass
class Frame:
    """Maps table-plane mm to rectified-image px (pixel centres at integer coordinates)."""
    A: np.ndarray            # 3x3, plane mm -> rect px
    size: tuple              # (w, h)
    s: float                 # px per mm

    def to_px(self, pts_mm) -> np.ndarray:
        return apply_h(self.A, pts_mm)

    def to_mm(self, pts_px) -> np.ndarray:
        return apply_h(np.linalg.inv(self.A), pts_px)


def axis_frame(lo, hi, s: float) -> Frame:
    lo, hi = np.asarray(lo, float), np.asarray(hi, float)
    w, h = int(np.ceil((hi[0] - lo[0]) * s)), int(np.ceil((hi[1] - lo[1]) * s))
    A = np.array([[s, 0, -lo[0] * s - 0.5], [0, s, -lo[1] * s - 0.5], [0, 0, 1.0]])
    return Frame(A, (w, h), s)


def rotated_frame(center_mm, angle_deg: float, half_size_mm, s: float) -> Frame:
    """Frame where plane points are rotated by angle about center, which lands mid-image."""
    hw, hh = half_size_mm
    w, h = int(np.ceil(2 * hw * s)), int(np.ceil(2 * hh * s))
    R = rot(angle_deg) * s
    c = np.asarray(center_mm, float)
    t = np.array([w / 2 - 0.5, h / 2 - 0.5]) - R @ c
    A = np.array([[R[0, 0], R[0, 1], t[0]], [R[1, 0], R[1, 1], t[1]], [0, 0, 1.0]])
    return Frame(A, (w, h), s)


def photo_extent_mm(H: np.ndarray, image_size, around_mm, limit_mm: float = 2000.0):
    """Bounding box (lo, hi) of the photo on the table, clipped to limit around a point."""
    w, h = image_size
    corners = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], float)
    q = np.hstack([corners, np.ones((4, 1))]) @ H.T
    c = np.asarray(around_mm, float)
    if np.any(q[:, 2] <= 1e-9):          # horizon in view: just use the limit box
        return c - limit_mm, c + limit_mm
    p = q[:, :2] / q[:, 2:3]
    lo = np.maximum(p.min(0), c - limit_mm)
    hi = np.minimum(p.max(0), c + limit_mm)
    return lo, hi


def warp(image: np.ndarray, H: np.ndarray, frame: Frame, image_scale: float = 1.0):
    """Rectify. H maps full-resolution photo px -> plane mm; `image` may be a downscaled copy
    (image_scale = image px per full-res px). Returns (rectified, valid_mask)."""
    S = np.array([[image_scale, 0, (image_scale - 1) / 2], [0, image_scale, (image_scale - 1) / 2], [0, 0, 1]])
    M = frame.A @ H @ np.linalg.inv(S)
    rect = cv2.warpPerspective(image, M, frame.size, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT,
                               borderValue=0)
    valid = cv2.warpPerspective(np.full(image.shape[:2], 255, np.uint8), M, frame.size, flags=cv2.INTER_NEAREST,
                                borderValue=0)
    valid[[0, -1], :] = 0          # the frame edge also counts as "outside the photo"
    valid[:, [0, -1]] = 0
    valid = cv2.erode(valid, np.ones((3, 3), np.uint8))
    return rect, valid > 0


def downscale(image: np.ndarray, max_side: int):
    h, w = image.shape[:2]
    k = max_side / max(h, w)
    if k >= 1:
        return image, 1.0
    small = cv2.resize(image, (int(round(w * k)), int(round(h * k))), interpolation=cv2.INTER_AREA)
    return small, small.shape[1] / w

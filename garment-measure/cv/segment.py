"""Separate the garment from the table in a rectified image.

The table colour is learned from a band along the edge of the photo (k-means in Lab), each
pixel is scored by its colour distance to the nearest table colour (lightness down-weighted so
shadows count less), and Otsu picks the threshold.
"""
from __future__ import annotations

from dataclasses import dataclass

import cv2
import numpy as np

from .geom import disk, fill_holes, largest_component

L_WEIGHT = 0.5


@dataclass
class BackgroundModel:
    centers: np.ndarray       # (k,3) Lab
    threshold: float          # score threshold (delta-E units)
    contrast: float           # median garment score


def to_lab(bgr: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(bgr.astype(np.float32) / 255.0, cv2.COLOR_BGR2Lab)


def score(lab: np.ndarray, centers: np.ndarray) -> np.ndarray:
    w = np.array([L_WEIGHT, 1.0, 1.0], np.float32)
    best = None
    for c in centers:
        d = np.sqrt(np.sum(((lab - c.astype(np.float32)) * w) ** 2, axis=-1))
        best = d if best is None else np.minimum(best, d)
    return best


def _otsu(values: np.ndarray, vmax: float = 100.0) -> float:
    v = np.clip(values / vmax * 255, 0, 255).astype(np.uint8).reshape(-1, 1)
    t, _ = cv2.threshold(v, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return float(t) / 255 * vmax


def _kmeans(px: np.ndarray, k: int, seed: int = 0):
    rng = np.random.default_rng(seed)
    if len(px) > 20000:
        px = px[rng.choice(len(px), 20000, replace=False)]
    k = min(k, max(1, len(px) // 10))
    crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1)
    cv2.setRNGSeed(seed)
    _, labels, centers = cv2.kmeans(px.astype(np.float32), k, None, crit, 3, cv2.KMEANS_PP_CENTERS)
    share = np.bincount(labels.ravel(), minlength=k) / len(labels)
    return centers, share


def learn_background(lab: np.ndarray, valid: np.ndarray, exclude: np.ndarray, s: float):
    """Table colours. The reference sheet lies on the table, so a ring around it is table for sure;
    a band along the photo edge adds the same table under different light, but colours there that
    are far from the ring (floor, other objects) are ignored."""
    ex = exclude.astype(np.uint8)
    ring = (cv2.dilate(ex, disk(60 * s)) > 0) & ~(cv2.dilate(ex, disk(4 * s)) > 0) & valid
    band_px = max(3, int(round(60 * s)))
    band = valid & ~(cv2.erode(valid.astype(np.uint8), disk(band_px)) > 0) & ~exclude
    centers = np.zeros((0, 3), np.float32)
    if ring.sum() >= 30:
        c, share = _kmeans(lab[ring], 2)
        centers = c[share >= 0.25]                     # a garment touching the sheet is a minority
    if band.sum() >= 30:
        c, share = _kmeans(lab[band], 3, seed=1)
        c = c[share >= 0.10]
        if len(centers):
            w = np.array([L_WEIGHT, 1, 1], np.float32)
            d = np.array([np.min(np.sqrt((((centers - x) * w) ** 2).sum(1))) for x in c]) if len(c) else []
            c = c[np.asarray(d) < 18] if len(c) else c
            centers = np.vstack([centers, c])
        else:
            centers = c
    if not len(centers):
        c, share = _kmeans(lab[valid & ~exclude], 1)
        centers = c
    return centers


def _pick_garment(m: np.ndarray, valid: np.ndarray, s: float, min_area_px: float) -> np.ndarray:
    """Largest blob that is not mostly made of photo border (floor, table edge, wall)."""
    n, lab, stats, _ = cv2.connectedComponentsWithStats(m, connectivity=8)
    if n <= 1:
        return np.zeros_like(m)
    edge = cv2.dilate((~valid).astype(np.uint8), disk(2)) > 0
    best, best_area, fallback, fb_area = None, 0, None, 0
    for k in range(1, n):
        area = stats[k, cv2.CC_STAT_AREA]
        if area < min_area_px:
            continue
        comp = lab == k
        touch = np.count_nonzero(comp & edge)
        perim = max(1.0, cv2.arcLength(largest_contour_pts(comp), True))
        if area > fb_area:
            fallback, fb_area = k, area
        if touch < 0.15 * perim and area > best_area:
            best, best_area = k, area
    k = best if best is not None else fallback
    return (lab == k).astype(np.uint8) if k is not None else np.zeros_like(m)


def largest_contour_pts(comp: np.ndarray) -> np.ndarray:
    cs, _ = cv2.findContours(comp.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return max(cs, key=cv2.contourArea) if cs else np.zeros((1, 1, 2), np.int32)


def coarse_mask(rect: np.ndarray, valid: np.ndarray, exclude: np.ndarray, s: float):
    """Garment mask at coarse scale. Returns (mask, BackgroundModel, flags)."""
    lab = to_lab(rect)
    centers = learn_background(lab, valid, exclude, s)
    sc = score(lab, centers)
    usable = valid & ~exclude
    t = float(np.clip(_otsu(sc[usable]), 8.0, 30.0))
    m = ((sc > t) & usable).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, disk(3 * s))
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, disk(6 * s))
    m = fill_holes(_pick_garment(m, valid, s, min_area_px=(150 * s) ** 2))
    flags = {}
    if m.sum() < (150 * s) ** 2:
        flags["NO_GARMENT"] = True
        return m, BackgroundModel(centers, t, 0.0), flags
    contrast = float(np.median(sc[m > 0]))
    if contrast < 12:
        flags["LOW_CONTRAST"] = True
    edge = cv2.dilate((~valid).astype(np.uint8), disk(2))
    if np.count_nonzero(edge & m) > 2:
        flags["GARMENT_CUT_OFF"] = True
    near_sheet = cv2.dilate(exclude.astype(np.uint8), disk(2 * s))
    if np.count_nonzero(near_sheet & m) > (20 * s):
        flags["TOUCHES_SHEET"] = True
    return m, BackgroundModel(centers, t, contrast), flags


def fine_mask(rect: np.ndarray, valid: np.ndarray, exclude: np.ndarray, s: float, model: BackgroundModel,
              region: np.ndarray) -> np.ndarray:
    """Full-resolution mask, searched only near the coarse outline (`region`)."""
    lab = to_lab(rect)
    sc = score(lab, model.centers)
    m = ((sc > model.threshold) & valid & ~exclude & region).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, disk(2.0 * s))   # knit texture gaps
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, disk(1.0 * s))    # specks and fibres
    m = fill_holes(largest_component(m))
    return cv2.medianBlur(m * 255, 5) > 127

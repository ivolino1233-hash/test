"""Parametric flat-lay garments with analytic ground truth.

Each builder returns a polygon in the garment's own frame (mm, x right, y down, symmetric about
x=0) plus the true landmark positions. Expected measurements are computed here from those
landmarks with plain geometry, independently of the vision code.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np


@dataclass
class Garment:
    kind: str                       # sweater | cardigan | tshirt | trousers | skirt
    polygon: np.ndarray             # (N,2) mm, clockwise on screen
    landmarks: dict                 # name -> (x, y) mm
    params: dict = field(default_factory=dict)
    color: tuple = (60, 70, 160)    # BGR
    legs_touching: bool = False


def _u(v):
    v = np.asarray(v, float)
    return v / np.linalg.norm(v)


def _line_intersect(p, d, q, e):
    """Intersection of p + t d and q + s e."""
    A = np.array([d, -np.asarray(e)]).T
    t, _ = np.linalg.solve(A, np.asarray(q) - np.asarray(p))
    return np.asarray(p) + t * np.asarray(d)


def row_extent(poly: np.ndarray, y: float, x_range=None):
    """Outer extent (xmin, xmax) of the polygon on the horizontal line y."""
    xs = []
    n = len(poly)
    for i in range(n):
        (x0, y0), (x1, y1) = poly[i], poly[(i + 1) % n]
        if (y0 - y) * (y1 - y) <= 0 and y0 != y1:
            xs.append(x0 + (y - y0) * (x1 - x0) / (y1 - y0))
    if x_range is not None:
        xs = [x for x in xs if x_range[0] <= x <= x_range[1]]
    return (min(xs), max(xs)) if xs else None


def _mirror(points):
    return [(-x, y) for x, y in reversed(points)]


def top(kind="sweater", chest=520, length=660, neck=180, back_neck_drop=18, shoulder=440,
        shoulder_drop=45, sleeve=600, sleeve_angle=50, armhole_width=210, cuff=95,
        rib_h=60, rib_pull=12, drop_bend=0.0, color=(60, 70, 160)):
    """Sweater / cardigan / T-shirt. sleeve_angle: degrees from vertical (90 = horizontal)."""
    hw = chest / 2
    hps = np.array([neck / 2, 0.0])
    sp = np.array([shoulder / 2, shoulder_drop])
    a = np.radians(sleeve_angle)
    u = np.array([np.sin(a), np.cos(a)])                       # along sleeve top edge
    if drop_bend:
        # Drop shoulder: the sleeve continues the shoulder line with only a small bend.
        u = _u(sp - hps)
        b = np.radians(drop_bend)
        u = np.array([u[0] * np.cos(b) - u[1] * np.sin(b), u[0] * np.sin(b) + u[1] * np.cos(b)])
        a = np.arctan2(u[0], u[1])
    n = np.array([-np.cos(a), np.sin(a)])                      # across the sleeve, toward underside
    ct = sp + sleeve * u
    cb = ct + cuff * n
    q0 = sp + armhole_width * n
    armpit = _line_intersect(cb, q0 - cb, np.array([hw, 0.0]), np.array([0.0, 1.0]))
    hem_y = length
    right = [hps, sp, ct, cb, armpit, (hw, hem_y - rib_h), (hw - rib_pull, hem_y - rib_h + 8),
             (hw - rib_pull, hem_y)]
    right = [tuple(map(float, p)) for p in right]
    cb_neck = (0.0, float(back_neck_drop))
    poly = np.array([cb_neck] + right + _mirror(right), dtype=float)

    L = {"cb_neck": cb_neck}
    for side, sgn in (("r", 1), ("l", -1)):
        m = np.array([sgn, 1.0])
        L[f"hps_{side}"] = tuple(hps * m)
        L[f"sp_{side}"] = tuple(sp * m)
        L[f"cuff_top_{side}"] = tuple(ct * m)
        L[f"cuff_bot_{side}"] = tuple(cb * m)
        L[f"armpit_{side}"] = tuple(armpit * m)
        # Upper arm: 25 mm down the underside from the armpit, across the sleeve axis.
        axis = _u(_u(ct - sp) + _u(cb - armpit))
        q = armpit + 25 * _u(cb - armpit)
        perp = np.array([-axis[1], axis[0]])
        if np.dot(perp, sp - armpit) < 0:
            perp = -perp
        p = _line_intersect(q, perp, sp, ct - sp)
        L[f"bicep_in_{side}"] = tuple(q * m)
        L[f"bicep_out_{side}"] = tuple(p * m)
    y_chest = armpit[1] + 25
    x0, x1 = row_extent(poly, y_chest, (-hw - 1, hw + 1))
    L["chest_l"], L["chest_r"] = (x0, y_chest), (x1, y_chest)
    x0, x1 = row_extent(poly, hem_y - 5, (-hw - 1, hw + 1))
    L["hem_l"], L["hem_r"] = (x0, hem_y - 5), (x1, hem_y - 5)
    L["len_bottom"] = (L["hps_l"][0], hem_y)
    L["cb_bottom"] = (0.0, hem_y)
    return Garment(kind, poly, L, params=dict(chest_offset_mm=25), color=color)


def trousers(waist=400, hip=520, hip_y=180, rise=290, length=1000, leg_open=210, gap=90,
             legs_touching=False, color=(110, 80, 40)):
    hw = hip / 2
    xi = 0.0 if legs_touching else gap / 2
    xo = xi + leg_open
    wr = (waist / 2, 0.0)
    right = [wr, (hw, hip_y), (xo, length), (xi, length)]
    crotch = (0.0, float(rise))
    left = [(-x, y) for x, y in reversed(right)]
    poly = np.array(right + [crotch] + left, dtype=float)
    L = {"waist_l": (-waist / 2, 0.0), "waist_r": wr, "crotch": crotch, "waist_c": (0.0, 0.0)}
    x0, x1 = row_extent(poly, hip_y)
    L["hip_l"], L["hip_r"] = (x0, hip_y), (x1, hip_y)
    for side, sgn in (("r", 1), ("l", -1)):
        L[f"leg_out_{side}"] = (sgn * xo, length)
        L[f"leg_in_{side}"] = (sgn * xi, length)
        y = rise + 25
        rng = (0, 1e4) if sgn > 0 else (-1e4, 0)
        ext = row_extent(poly, y, rng)
        L[f"thigh_out_{side}"] = (ext[1] if sgn > 0 else ext[0], y)
        L[f"thigh_in_{side}"] = (ext[0] if sgn > 0 else ext[1], y)
    return Garment("trousers", poly, L, params=dict(hip_offset_mm=hip_y), color=color,
                   legs_touching=legs_touching)


def skirt(waist=360, hip=480, hip_y=180, length=600, hem=640, color=(40, 120, 60)):
    right = [(waist / 2, 0.0), (hip / 2, hip_y), (hem / 2, length)]
    poly = np.array(right + _mirror(right), dtype=float)
    L = {"waist_l": (-waist / 2, 0.0), "waist_r": (waist / 2, 0.0),
         "hip_l": (-hip / 2, hip_y), "hip_r": (hip / 2, hip_y),
         "top_c": (0.0, 0.0), "bottom_c": (0.0, length),
         "hem_l": (-hem / 2, length), "hem_r": (hem / 2, length)}
    return Garment("skirt", poly, L, params=dict(hip_offset_mm=hip_y), color=color)


def expected(g: Garment, catalogue_defs) -> dict:
    """Expected measurement values (mm) keyed like the pipeline output ('key' or 'key.l')."""
    out = {}
    for d in catalogue_defs:
        for side in (("l", "r") if d["sides"] else (None,)):
            names = [p.format(s=side) for p in d["points"]]
            if any(n not in g.landmarks for n in names):
                continue
            pts = np.array([g.landmarks[n] for n in names], float)
            if d["kind"] == "dy":
                v = abs(pts[1, 1] - pts[0, 1])
            elif d["kind"] == "dx":
                v = abs(pts[1, 0] - pts[0, 0])
            else:
                v = float(np.sum(np.linalg.norm(np.diff(pts, axis=0), axis=1)))
            out[d["key"] + (f".{side}" if side else "")] = v
    return out

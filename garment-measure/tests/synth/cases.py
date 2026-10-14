"""Named synthetic photo cases shared by the accuracy tests and the end-to-end test.
Rendered photos are cached in tests/.cache so repeated runs are fast."""
from __future__ import annotations

import os
from pathlib import Path

import cv2

from . import garments as G
from .render import Camera, Scene, render

CACHE = Path(__file__).resolve().parents[1] / ".cache"
CAM = dict(width=4000, height=3000)

CASES = {
    "sweater": dict(
        garment=lambda: G.top(), type="sweater",
        scene=dict(garment_angle=6, sheets=((0, (-120.0, 720.0), 10.0),)),
        camera=dict(tilt_deg=15, tilt_dir_deg=40, yaw_deg=5)),
    "sweater_two_sheets_auto": dict(
        garment=lambda: G.top(), type="auto",
        scene=dict(garment_angle=-80, sheets=((0, (420.0, 700.0), 0.0), (1, (-900.0, -300.0), 20.0))),
        camera=dict(tilt_deg=25, tilt_dir_deg=200, yaw_deg=95, height_mm=2100)),
    "cardigan_black_drop_shoulder": dict(
        garment=lambda: G.top("cardigan", shoulder=560, shoulder_drop=60, sleeve=520, drop_bend=15,
                              armhole_width=230, color=(30, 30, 30)), type="cardigan",
        scene=dict(garment_angle=2, background=(225, 225, 220), sheets=((0, (-100.0, 760.0), 0.0),)),
        camera=dict(tilt_deg=20, tilt_dir_deg=90)),
    "tshirt_white_on_dark": dict(
        garment=lambda: G.top("tshirt", chest=500, length=700, sleeve=210, sleeve_angle=55, armhole_width=190,
                              cuff=150, rib_h=0, rib_pull=0, color=(240, 240, 240)), type="auto",
        scene=dict(garment_angle=8, background=(90, 60, 40), sheets=((0, (780.0, 0.0), 90.0),)),
        camera=dict(tilt_deg=18, tilt_dir_deg=300)),
    "tshirt_flat_shoulder": dict(
        garment=lambda: G.top("tshirt", chest=500, length=700, sleeve=200, sleeve_angle=65, armhole_width=200,
                              cuff=160, rib_h=0, rib_pull=0), type="tshirt",
        scene=dict(garment_angle=-3, sheets=((0, (760.0, 0.0), 90.0),)),
        camera=dict(tilt_deg=10)),
    "trousers": dict(
        garment=lambda: G.trousers(), type="auto",
        scene=dict(garment_angle=4, sheets=((0, (380.0, 300.0), 0.0),)),
        camera=dict(tilt_deg=12)),
    "trousers_legs_touching": dict(
        garment=lambda: G.trousers(legs_touching=True), type="trousers",
        scene=dict(garment_angle=0, sheets=((0, (380.0, 300.0), 0.0),)),
        camera=dict(tilt_deg=5)),
    "skirt": dict(
        garment=lambda: G.skirt(), type="auto",
        scene=dict(garment_angle=-5, sheets=((0, (420.0, 0.0), 0.0),)),
        camera=dict(tilt_deg=10)),
}


def photo(name: str):
    """(image, Garment) for a named case, rendered once and cached."""
    case = CASES[name]
    g = case["garment"]()
    CACHE.mkdir(exist_ok=True)
    path = CACHE / f"{name}.png"
    if path.exists() and not os.environ.get("REGEN_SYNTH"):
        return cv2.imread(str(path)), g
    img, _ = render(Scene(g, **case["scene"]), Camera(**CAM, **case["camera"]), seed=sum(map(ord, name)) % 997)
    cv2.imwrite(str(path), img)
    return img, g

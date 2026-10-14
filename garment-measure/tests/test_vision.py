"""Accuracy of the measuring pipeline on synthetic phone photos with known true sizes."""
import cv2
import numpy as np
import pytest

from cv import board as B
from cv import catalogue, pipeline
from cv.homography import detect_sheets, fit_plane
from tests.synth import garments as G
from tests.synth.cases import CASES, photo
from tests.synth.render import Camera, Scene, camera_homography, render

TOL_MM = 3.0
# The crotch tip sits where the inner leg edges meet at a shallow angle, so it is less certain.
CROTCH_TOL_MM = 8.0
CROTCH_KEYS = {"front_rise", "inseam"}


def _measured(res):
    return {m["key"] + (f".{m['side']}" if m["side"] else ""): m["value_mm"] for m in res["measurements"]}


def test_board_ids_and_page_geometry():
    assert B.MARKERS_PER_SHEET == 12
    assert list(B.board(1).getIds().ravel()) == list(range(12, 24))
    x0, y0, x1, y1 = B.page_rect_mm()
    assert (x1 - x0, y1 - y0) == (210.0, 297.0)
    page = B.render_page(0, 6)
    assert page.shape == (297 * 6, 210 * 6)


def test_marker_pdf_is_written(tmp_path):
    p = tmp_path / "m.pdf"
    B.write_pdf(p, sheets=(0, 1))
    data = p.read_bytes()
    assert data.startswith(b"%PDF") and data.count(b"/Type /Page") >= 2


def test_homography_scale_far_from_sheet():
    g = G.skirt()
    scene = Scene(g, sheets=((0, (420.0, 0.0), 0.0),))
    cam = Camera(width=3000, height=2250, tilt_deg=20, tilt_dir_deg=30, yaw_deg=10)
    img, H_true = render(scene, cam, seed=3)
    fit = fit_plane(detect_sheets(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)))
    assert fit is not None and fit.rms_px < 0.2
    # Two points 600 mm apart, half a metre from the sheet: distance must come out right.
    a, b = np.array([[-300.0, 600.0]]), np.array([[300.0, 600.0]])
    from cv.geom import apply_h
    pa, pb = apply_h(fit.H, apply_h(H_true, a)), apply_h(fit.H, apply_h(H_true, b))
    assert abs(np.linalg.norm(pa - pb) - 600.0) < 2.0
    assert abs(fit.tilt_deg(img.shape[1::-1]) - 20) < 3


def test_printer_scale_correction():
    g = G.skirt()
    scene = Scene(g, sheets=((0, (420.0, 0.0), 0.0),), printer_scale=(0.97, 0.98))
    img, _ = render(scene, Camera(width=3000, height=2250, tilt_deg=8), seed=4)
    off = pipeline.measure(img, pipeline.Options(garment_type="skirt"))
    on = pipeline.measure(img, pipeline.Options(garment_type="skirt", printer_scale=(0.97, 0.98)))
    w_off = _measured(off)["waist"]
    w_on = _measured(on)["waist"]
    assert abs(w_on - 360) < 3
    assert w_off > w_on * 1.015          # uncorrected shrunken print over-reads by ~3 %


@pytest.mark.parametrize("name", [n for n in CASES if n != "trousers_legs_touching"])
def test_accuracy(name):
    img, g = photo(name)
    case = CASES[name]
    res = pipeline.measure(img, pipeline.Options(garment_type=case["type"], params=g.params))
    assert res["ok"], res["error"]
    assert catalogue.family(res["garment_type"]) == catalogue.family(g.kind)
    codes = {w["code"] for w in res["warnings"]}
    exp = G.expected(g, catalogue.defs_for(res["garment_type"]))
    got = _measured(res)
    sp_unclear = "SHOULDER_POINT_UNCLEAR" in codes
    bad = []
    for k, e in exp.items():
        base = k.split(".")[0]
        if sp_unclear and base in {"across_shoulder", "armhole", "sleeve_length", "sleeve_length_cb"}:
            continue
        tol = CROTCH_TOL_MM if base in CROTCH_KEYS else TOL_MM
        v = got.get(k)
        if v is None or abs(v - e) > tol:
            bad.append(f"{k}: expected {e:.1f} got {v if v is None else round(v, 1)}")
    assert not bad, bad


def test_flat_shoulder_is_flagged():
    img, g = photo("tshirt_flat_shoulder")
    res = pipeline.measure(img, pipeline.Options(garment_type="tshirt"))
    assert "SHOULDER_POINT_UNCLEAR" in {w["code"] for w in res["warnings"]}
    assert res["confidence"]["sp_l"] < 1


def test_legs_touching_is_flagged_but_widths_still_measured():
    img, g = photo("trousers_legs_touching")
    res = pipeline.measure(img, pipeline.Options(garment_type="trousers", params=g.params))
    assert "LEGS_TOUCHING" in {w["code"] for w in res["warnings"]}
    got = _measured(res)
    assert abs(got["waist"] - 400) < TOL_MM and abs(got["hip"] - 520) < TOL_MM
    assert res["confidence"]["crotch"] < 1


def test_wrong_type_is_reported():
    img, _ = photo("skirt")
    res = pipeline.measure(img, pipeline.Options(garment_type="sweater"))
    assert not res["ok"] and res["error"]["code"] == "NO_ARMPITS"


def test_no_marker():
    img = np.full((1200, 1600, 3), 200, np.uint8)
    cv2.rectangle(img, (400, 300), (1200, 900), (40, 40, 160), -1)
    res = pipeline.measure(img)
    assert res["error"]["code"] == "NO_MARKER"
    assert pipeline.preview(img)["status"] == "NO_MARKER"


def test_preview_on_small_frame():
    img, _ = photo("sweater")
    small = cv2.resize(img, (1280, 960), interpolation=cv2.INTER_AREA)
    p = pipeline.preview(small)
    assert p["status"] == "READY", p
    assert p["sheets"] == 1 and len(p["outline"]) > 6
    xs = [q[0] for q in p["outline"]]
    assert 0 <= min(xs) and max(xs) <= 1280


def test_cut_off_garment_is_rejected():
    g = G.top()
    scene = Scene(g, sheets=((0, (-120.0, 720.0), 0.0),))
    cam = Camera(width=2000, height=1500, height_mm=1200, target=(400.0, 300.0))
    img, _ = render(scene, cam, seed=5)
    assert pipeline.measure(img)["error"]["code"] == "GARMENT_CUT_OFF"


def test_camera_homography_identity_overhead():
    cam = Camera(width=1000, height=1000, height_mm=1000, fov_deg=90)
    H = camera_homography(cam, (0.0, 0.0))
    from cv.geom import apply_h
    p = apply_h(H, [[0, 0], [100, 0]])
    assert np.allclose(p[0], [499.5, 499.5]) and abs(p[1][0] - p[0][0] - 50) < 1e-6

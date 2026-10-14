"""The phone recomputes measurements while a point is dragged; it must agree with the server."""
import json
import shutil
import subprocess
from pathlib import Path

import pytest

from app import specs
from cv import catalogue

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.skipif(shutil.which("node") is None, reason="node not installed")
def test_measure_js_matches_python():
    defs = catalogue.defs_for("sweater") + catalogue.defs_for("trousers")
    names = {p.format(s=s) for d in defs for p in d["points"] for s in ("l", "r")}
    landmarks = {n: [100 + 37.3 * i, 50 + 91.7 * ((i * 7) % 11)] for i, n in enumerate(sorted(names))}
    spec = [{"key": "chest", "target_mm": 500, "tol_minus_mm": 10, "tol_plus_mm": 15},
            {"key": "sleeve_length", "target_mm": 300, "tol_minus_mm": 5, "tol_plus_mm": 5}]
    py_meas = catalogue.evaluate(defs, landmarks, 2.0)
    py_res = specs.compare(py_meas, spec)
    js = f"""
      import {{ evaluate, compare }} from "{(ROOT / 'static/js/measure.js').as_uri()}";
      const m = evaluate({json.dumps(defs)}, {json.dumps(landmarks)}, 2.0);
      console.log(JSON.stringify({{ m, r: compare(m, {json.dumps(spec)}) }}));
    """
    out = json.loads(subprocess.check_output(["node", "--input-type=module", "-e", js], text=True))
    assert len(out["m"]) == len(py_meas)
    for a, b in zip(out["m"], py_meas):
        assert a["key"] == b["key"] and a["side"] == b["side"]
        assert abs(a["value_mm"] - b["value_mm"]) < 1e-9
    for k, r in py_res.items():
        assert out["r"][k]["status"] == r["status"]

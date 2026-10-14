"""Pass/fail against the style spec, the plain-language verdict, and spec CSV import."""
from __future__ import annotations

import csv
import io

from cv import catalogue


def result_key(m: dict) -> str:
    return m["key"] + (f".{m['side']}" if m.get("side") else "")


def compare(measurements: list[dict], spec_points: list[dict]) -> dict:
    """Result per measurement ('chest', 'sleeve_length.l', ...). Both sides of a two-sided
    measurement are checked against the same spec line."""
    spec = {p["key"]: p for p in spec_points}
    out = {}
    for m in measurements:
        k = result_key(m)
        p = spec.get(m["key"])
        v = m.get("value_mm")
        r = {"key": m["key"], "side": m.get("side"), "label": m["label"], "actual_mm": v,
             "target_mm": None, "tol_minus_mm": None, "tol_plus_mm": None, "diff_mm": None, "status": "no_spec"}
        if p is not None:
            r.update(target_mm=p["target_mm"], tol_minus_mm=p["tol_minus_mm"], tol_plus_mm=p["tol_plus_mm"])
            if v is None:
                r["status"] = "missing"
            else:
                d = v - p["target_mm"]
                r["diff_mm"] = d
                r["status"] = "pass" if -p["tol_minus_mm"] - 1e-6 <= d <= p["tol_plus_mm"] + 1e-6 else "fail"
        out[k] = r
    return out


def counts(results: dict) -> tuple[int, int]:
    st = [r["status"] for r in results.values()]
    return st.count("pass"), st.count("fail")


def _cm(mm):
    return f"{mm / 10:.1f} cm"


def verdict(results: dict) -> str:
    """Deterministic summary; the AI summary is only an extra explanation next to it."""
    checked = [r for r in results.values() if r["status"] in ("pass", "fail")]
    if not checked:
        return "No spec for this style/size - measurements only."
    fails = [r for r in checked if r["status"] == "fail"]
    missing = [r for r in results.values() if r["status"] == "missing"]
    if not fails:
        s = f"PASS - all {len(checked)} checked points are within tolerance."
    else:
        parts = []
        for r in sorted(fails, key=lambda r: -abs(r["diff_mm"])):
            side = {"l": " (left)", "r": " (right)"}.get(r["side"] or "", "")
            over = r["diff_mm"] - r["tol_plus_mm"] if r["diff_mm"] > 0 else r["diff_mm"] + r["tol_minus_mm"]
            parts.append(f"{r['label']}{side} {'+' if r['diff_mm'] > 0 else '-'}{_cm(abs(r['diff_mm']))} "
                         f"({_cm(abs(over))} outside tolerance)")
        s = f"FAIL - {len(fails)} of {len(checked)} points out of tolerance: " + "; ".join(parts) + "."
    if missing:
        s += " Not measured: " + ", ".join(sorted({r["label"] for r in missing})) + "."
    return s


TEMPLATE_HEADER = ["style_code", "style_name", "customer", "garment_type", "size", "point", "target_cm",
                   "tol_minus_cm", "tol_plus_cm"]


def parse_spec_csv(text: str) -> tuple[dict, list[str]]:
    """Read a spec sheet (one row per style/size/point, values in cm). Returns
    ({style_code: style dict with spec}, errors). Point names may be our keys, our labels or
    common spec-sheet names such as '1/2 chest'."""
    rdr = csv.DictReader(io.StringIO(text.lstrip("﻿")))
    if not rdr.fieldnames:
        return {}, ["The file is empty."]
    norm = {f: f.strip().lower().replace(" ", "_") for f in rdr.fieldnames}
    need = {"style_code", "size", "point", "target_cm"}
    if not need <= set(norm.values()):
        return {}, [f"Missing columns: {', '.join(sorted(need - set(norm.values())))}"]
    styles, errors = {}, []
    for n, raw in enumerate(rdr, start=2):
        row = {norm[k]: (v or "").strip() for k, v in raw.items() if k in norm}
        code = row["style_code"]
        if not code:
            continue
        st = styles.setdefault(code, {"code": code, "name": "", "customer": "", "garment_type": "", "sizes": [],
                                      "spec": []})
        for f in ("style_name", "customer", "garment_type"):
            if row.get(f):
                st["name" if f == "style_name" else f] = row[f]
        gt = (st["garment_type"] or "sweater").lower()
        if gt not in catalogue.GARMENT_TYPES:
            errors.append(f"Row {n}: unknown garment type '{gt}'.")
            continue
        st["garment_type"] = gt
        key = catalogue.match_key(gt, row["point"])
        if key is None:
            errors.append(f"Row {n}: unknown point '{row['point']}' for {gt}.")
            continue
        try:
            target = float(row["target_cm"].replace(",", ".")) * 10
            tm = float((row.get("tol_minus_cm") or row.get("tol_cm") or "1").replace(",", ".")) * 10
            tp = float((row.get("tol_plus_cm") or row.get("tol_cm") or str(tm / 10)).replace(",", ".")) * 10
        except ValueError:
            errors.append(f"Row {n}: numbers expected for target/tolerance.")
            continue
        if row["size"] not in st["sizes"]:
            st["sizes"].append(row["size"])
        st["spec"] = [p for p in st["spec"] if not (p["size"] == row["size"] and p["key"] == key)]
        st["spec"].append({"size": row["size"], "key": key, "target_mm": target, "tol_minus_mm": abs(tm),
                           "tol_plus_mm": abs(tp)})
    return styles, errors


def template_csv() -> str:
    out = io.StringIO()
    w = csv.writer(out)
    w.writerow(TEMPLATE_HEADER)
    for size, chest, length in (("M", 52, 66), ("L", 55, 68)):
        for point, val, tol in (("1/2 chest", chest, 1), ("body length", length, 1), ("sleeve length", 60, 1),
                                ("1/2 bottom", chest - 2.5, 1), ("cuff", 9.5, 0.5)):
            w.writerow(["KN-1001", "Crew neck sweater", "Example brand", "sweater", size, point, val, tol, tol])
    return out.getvalue()

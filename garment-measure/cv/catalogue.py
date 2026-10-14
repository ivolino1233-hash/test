"""Garment types and their measurement points (points of measure).

Every measurement is a line between named landmarks, so the phone can recompute it the
moment a landmark is dragged:
  dist - straight distance            dy - vertical distance only
  dx   - horizontal distance only     path - sum of segments through 3+ landmarks
`{s}` in a landmark name expands to l / r for measurements taken on both sides.
"""
from __future__ import annotations

GARMENT_TYPES = {
    "sweater": {"label": "Sweater / pullover", "family": "top"},
    "cardigan": {"label": "Cardigan", "family": "top"},
    "tshirt": {"label": "T-shirt / short sleeve", "family": "top", "short_sleeve": True},
    "trousers": {"label": "Trousers", "family": "trousers"},
    "skirt": {"label": "Skirt", "family": "skirt"},
}

DEFAULT_PARAMS = {
    "chest_offset_mm": 25.0,   # chest measured this far below the armhole
    "bicep_offset_mm": 25.0,   # upper arm measured this far below the armhole
    "hem_offset_mm": 5.0,      # bottom width measured this far above the bottom edge
    "hip_offset_mm": 180.0,    # hip measured this far below the top of the waistband
    "thigh_offset_mm": 25.0,   # thigh measured this far below the crotch
}


def _m(key, label, kind, points, sides=False, aliases=(), note=""):
    return {"key": key, "label": label, "kind": kind, "points": list(points), "sides": sides,
            "aliases": list(aliases), "note": note}


TOP = [
    _m("chest", "Chest width ½", "dist", ["chest_l", "chest_r"],
       aliases=["1/2 chest", "chest width", "chest", "half chest", "bust"], note="below armhole"),
    _m("body_length", "Body length (HPS)", "dy", ["hps_l", "len_bottom"],
       aliases=["body length", "front length", "hps length", "length from hps", "length"]),
    _m("body_length_cb", "Centre back length", "dy", ["cb_neck", "cb_bottom"],
       aliases=["cb length", "back length", "centre back length", "center back length"]),
    _m("across_shoulder", "Across shoulder", "dist", ["sp_l", "sp_r"],
       aliases=["shoulder", "shoulder width", "across shoulders", "x-shoulder"]),
    _m("neck_width", "Neck width", "dist", ["hps_l", "hps_r"],
       aliases=["neck width", "neck opening", "neck"], note="outline estimate"),
    _m("armhole", "Armhole (straight)", "dist", ["sp_{s}", "armpit_{s}"], sides=True,
       aliases=["armhole", "armhole straight", "arm hole"]),
    _m("sleeve_length", "Sleeve length (from shoulder)", "dist", ["sp_{s}", "cuff_top_{s}"], sides=True,
       aliases=["sleeve length", "sleeve", "sleeve length from shoulder"]),
    _m("sleeve_length_cb", "Sleeve length (from CB neck)", "path", ["cb_neck", "sp_{s}", "cuff_top_{s}"],
       sides=True, aliases=["cb sleeve", "sleeve from cb", "cb neck to cuff", "sleeve length cb"]),
    _m("underarm", "Underarm sleeve length", "dist", ["armpit_{s}", "cuff_bot_{s}"], sides=True,
       aliases=["underarm", "underarm length", "inseam sleeve"]),
    _m("bicep", "Upper arm ½", "dist", ["bicep_in_{s}", "bicep_out_{s}"], sides=True,
       aliases=["upper arm", "bicep", "biceps", "1/2 upper arm"], note="below armhole"),
    _m("sleeve_opening", "Cuff / sleeve opening ½", "dist", ["cuff_top_{s}", "cuff_bot_{s}"], sides=True,
       aliases=["cuff", "cuff width", "sleeve opening", "1/2 cuff", "1/2 sleeve opening"]),
    _m("hem", "Bottom width ½", "dist", ["hem_l", "hem_r"],
       aliases=["hem", "bottom width", "1/2 bottom", "hem width", "sweep"]),
]

TROUSERS = [
    _m("waist", "Waist ½ (relaxed)", "dist", ["waist_l", "waist_r"], aliases=["waist", "1/2 waist", "waist relaxed"]),
    _m("hip", "Hip ½", "dist", ["hip_l", "hip_r"], aliases=["hip", "1/2 hip", "seat"], note="below waist"),
    _m("front_rise", "Front rise", "dy", ["waist_c", "crotch"], aliases=["front rise", "rise"]),
    _m("inseam", "Inseam", "dist", ["crotch", "leg_in_{s}"], sides=True, aliases=["inseam", "inside leg"]),
    _m("outseam", "Outseam", "dist", ["waist_{s}", "leg_out_{s}"], sides=True,
       aliases=["outseam", "outside leg", "side length"]),
    _m("thigh", "Thigh ½", "dist", ["thigh_out_{s}", "thigh_in_{s}"], sides=True,
       aliases=["thigh", "1/2 thigh"], note="below crotch"),
    _m("leg_opening", "Leg opening ½", "dist", ["leg_out_{s}", "leg_in_{s}"], sides=True,
       aliases=["leg opening", "1/2 leg opening", "bottom", "hem"]),
]

SKIRT = [
    _m("waist", "Waist ½ (relaxed)", "dist", ["waist_l", "waist_r"], aliases=["waist", "1/2 waist"]),
    _m("hip", "Hip ½", "dist", ["hip_l", "hip_r"], aliases=["hip", "1/2 hip"], note="below waist"),
    _m("length", "Length (centre)", "dy", ["top_c", "bottom_c"], aliases=["length", "skirt length", "cf length"]),
    _m("hem_sweep", "Hem sweep ½", "dist", ["hem_l", "hem_r"], aliases=["hem sweep", "sweep", "hem", "1/2 sweep"]),
]

BY_FAMILY = {"top": TOP, "trousers": TROUSERS, "skirt": SKIRT}


def family(garment_type: str) -> str:
    return GARMENT_TYPES[garment_type]["family"]


def defs_for(garment_type: str) -> list[dict]:
    defs = [dict(d) for d in BY_FAMILY[family(garment_type)]]
    if GARMENT_TYPES[garment_type].get("short_sleeve"):
        for d in defs:
            if d["key"] == "sleeve_opening":
                d["label"] = "Sleeve opening ½"
    return defs


def label_for(garment_type: str, key: str) -> str:
    for d in defs_for(garment_type):
        if d["key"] == key:
            return d["label"]
    return key


def match_key(garment_type: str, name: str) -> str | None:
    """Map a spec-sheet name ('1/2 chest', 'Chest width ½', 'chest') to an internal key."""
    n = " ".join(name.lower().replace("½", "1/2").replace("_", " ").split())
    for d in defs_for(garment_type):
        cands = {d["key"].replace("_", " "), d["label"].lower().replace("½", "1/2").strip(), *d["aliases"]}
        if n in cands:
            return d["key"]
    return None


def evaluate(defs: list[dict], landmarks: dict, px_per_mm: float) -> list[dict]:
    """Measurement values (mm) from landmark positions (rectified px)."""
    out = []
    for d in defs:
        for side in (("l", "r") if d["sides"] else (None,)):
            names = [p.format(s=side) for p in d["points"]]
            if any(n not in landmarks or landmarks[n] is None for n in names):
                out.append({"key": d["key"], "side": side, "label": d["label"], "kind": d["kind"],
                            "value_mm": None, "points": names})
                continue
            pts = [landmarks[n] for n in names]
            if d["kind"] == "dy":
                v = abs(pts[1][1] - pts[0][1])
            elif d["kind"] == "dx":
                v = abs(pts[1][0] - pts[0][0])
            else:
                v = sum(((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5 for a, b in zip(pts, pts[1:]))
            out.append({"key": d["key"], "side": side, "label": d["label"], "kind": d["kind"],
                        "value_mm": v / px_per_mm, "points": names})
    return out

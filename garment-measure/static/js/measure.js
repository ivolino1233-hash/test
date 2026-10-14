// Same rules as cv/catalogue.py evaluate() and app/specs.py compare(), so values update
// instantly while a point is dragged. The server recomputes on save and is authoritative.

export function evaluate(defs, landmarks, pxPerMm) {
  const out = [];
  for (const d of defs) {
    for (const side of d.sides ? ["l", "r"] : [null]) {
      const names = d.points.map((p) => p.replace("{s}", side));
      const pts = names.map((n) => landmarks[n]);
      let v = null;
      if (pts.every(Boolean)) {
        if (d.kind === "dy") v = Math.abs(pts[1][1] - pts[0][1]);
        else if (d.kind === "dx") v = Math.abs(pts[1][0] - pts[0][0]);
        else {
          v = 0;
          for (let i = 1; i < pts.length; i++) v += Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]);
        }
        v /= pxPerMm;
      }
      out.push({ key: d.key, side, label: d.label, kind: d.kind, value_mm: v, points: names });
    }
  }
  return out;
}

export const resultKey = (m) => m.key + (m.side ? "." + m.side : "");

export function compare(measurements, specPoints) {
  const spec = Object.fromEntries((specPoints || []).map((p) => [p.key, p]));
  const out = {};
  for (const m of measurements) {
    const p = spec[m.key];
    const r = { key: m.key, side: m.side, label: m.label, actual_mm: m.value_mm, target_mm: null,
      tol_minus_mm: null, tol_plus_mm: null, diff_mm: null, status: "no_spec" };
    if (p) {
      Object.assign(r, { target_mm: p.target_mm, tol_minus_mm: p.tol_minus_mm, tol_plus_mm: p.tol_plus_mm });
      if (m.value_mm == null) r.status = "missing";
      else {
        r.diff_mm = m.value_mm - p.target_mm;
        r.status = r.diff_mm >= -p.tol_minus_mm - 1e-6 && r.diff_mm <= p.tol_plus_mm + 1e-6 ? "pass" : "fail";
      }
    }
    out[resultKey(m)] = r;
  }
  return out;
}

export function fmt(mm, unit = "cm", signed = false) {
  if (mm == null) return "–";
  const sign = signed ? (mm > 0 ? "+" : mm < 0 ? "−" : "±") : mm < 0 ? "−" : "";
  const a = Math.abs(mm);
  if (unit === "in") {
    let inches = a / 25.4, whole = Math.floor(inches), e = Math.round((inches - whole) * 8);
    if (e === 8) { whole += 1; e = 0; }
    const frac = ["", "⅛", "¼", "⅜", "½", "⅝", "¾", "⅞"][e];
    return `${sign}${whole || (frac ? "" : "0")}${frac}"`;
  }
  return `${sign}${(a / 10).toFixed(1)}`;
}

export const unitLabel = (unit) => (unit === "in" ? "in" : "cm");

// cm/inch text field <-> mm
export function toMm(text, unit = "cm") {
  if (text == null || String(text).trim() === "") return null;
  const v = parseFloat(String(text).replace(",", "."));
  if (!isFinite(v)) return null;
  return unit === "in" ? v * 25.4 : v * 10;
}
export function fromMm(mm, unit = "cm") {
  if (mm == null) return "";
  return unit === "in" ? (mm / 25.4).toFixed(2).replace(/\.?0+$/, "") : (mm / 10).toFixed(1).replace(/\.0$/, "");
}

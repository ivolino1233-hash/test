"""Draw measurement lines and values on the straightened photo (for history and export)."""
from __future__ import annotations

import cv2
import numpy as np

PASS, FAIL, NOSPEC, LOW = (60, 170, 60), (40, 40, 220), (220, 150, 40), (0, 165, 255)


def fmt(mm: float, unit: str = "cm") -> str:
    if unit == "in":
        inches = mm / 25.4
        whole, eighths = int(inches), round((inches - int(inches)) * 8)
        if eighths == 8:
            whole, eighths = whole + 1, 0
        frac = {0: "", 1: " 1/8", 2: " 1/4", 3: " 3/8", 4: " 1/2", 5: " 5/8", 6: " 3/4", 7: " 7/8"}[eighths]
        return f'{whole}{frac}"'
    return f"{mm / 10:.1f}"


def draw(rect: np.ndarray, landmarks: dict, measurements: list, results: dict | None = None,
         confidence: dict | None = None, unit: str = "cm", max_side: int = 2000) -> np.ndarray:
    img = rect.copy()
    k = min(1.0, max_side / max(img.shape[:2]))
    if k < 1:
        img = cv2.resize(img, None, fx=k, fy=k, interpolation=cv2.INTER_AREA)
    img = cv2.addWeighted(img, 0.85, np.full_like(img, 255), 0.15, 0)
    th = max(2, int(round(3 * k * 1.5)))
    fs = max(0.5, 0.9 * k * 1.4)
    results = results or {}
    confidence = confidence or {}
    for m in measurements:
        if m.get("value_mm") is None:
            continue
        pts = [np.array(landmarks[p]) * k for p in m["points"]]
        rk = m["key"] + (f".{m['side']}" if m.get("side") else "")
        status = results.get(rk, {}).get("status")
        col = PASS if status == "pass" else FAIL if status == "fail" else NOSPEC
        if m.get("kind") == "dy":
            a, b = pts[0], pts[1]
            pts = [a, np.array([a[0], b[1]])]
        for a, b in zip(pts, pts[1:]):
            cv2.line(img, tuple(np.round(a).astype(int)), tuple(np.round(b).astype(int)), col, th, cv2.LINE_AA)
        mid = (pts[0] + pts[-1]) / 2 if len(pts) == 2 else pts[len(pts) // 2]
        label = fmt(m["value_mm"], unit)
        (tw, tht), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, fs, 2)
        org = (int(mid[0] - tw / 2), int(mid[1] - 6))
        cv2.rectangle(img, (org[0] - 4, org[1] - tht - 4), (org[0] + tw + 4, org[1] + 6), (255, 255, 255), -1)
        cv2.putText(img, label, org, cv2.FONT_HERSHEY_SIMPLEX, fs, col, 2, cv2.LINE_AA)
    for name, p in landmarks.items():
        q = tuple(np.round(np.array(p) * k).astype(int))
        c = LOW if confidence.get(name, 1.0) < 0.9 else (30, 30, 30)
        cv2.circle(img, q, th * 2 + 1, (255, 255, 255), -1, cv2.LINE_AA)
        cv2.circle(img, q, th * 2 + 1, c, 2, cv2.LINE_AA)
    return img

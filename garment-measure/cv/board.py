"""Printable reference sheet: one A4 page with a ChArUco board plus two check rulers.

The same definition drives the printable PDF, the detector and the synthetic test renderer,
so all three always agree on geometry.

Coordinates are millimetres in the board frame: origin at the board's top-left corner,
x to the right, y down (the page sits at negative offsets around it).
"""
from __future__ import annotations

from functools import lru_cache

import cv2
import numpy as np

SQUARES = (4, 6)               # squares in x, y
SQUARE_MM = 42.0
MARKER_MM = 32.0
BOARD_W_MM = SQUARES[0] * SQUARE_MM   # 168
BOARD_H_MM = SQUARES[1] * SQUARE_MM   # 252
PAGE_W_MM, PAGE_H_MM = 210.0, 297.0
BOARD_ON_PAGE = ((PAGE_W_MM - BOARD_W_MM) / 2, (PAGE_H_MM - BOARD_H_MM) / 2)  # (21, 22.5)
MARKERS_PER_SHEET = (SQUARES[0] * SQUARES[1]) // 2                        # 12
MAX_SHEETS = 4                                                             # DICT_4X4_50 holds 50 ids
RULER_H_MM = 150.0
RULER_V_MM = 250.0
DICTIONARY_ID = cv2.aruco.DICT_4X4_50


@lru_cache(maxsize=1)
def dictionary():
    return cv2.aruco.getPredefinedDictionary(DICTIONARY_ID)


@lru_cache(maxsize=MAX_SHEETS)
def board(sheet: int) -> cv2.aruco.CharucoBoard:
    ids = np.arange(sheet * MARKERS_PER_SHEET, (sheet + 1) * MARKERS_PER_SHEET, dtype=np.int32)
    return cv2.aruco.CharucoBoard(SQUARES, SQUARE_MM, MARKER_MM, dictionary(), ids)


def sheet_of_marker(marker_id: int) -> int:
    return int(marker_id) // MARKERS_PER_SHEET


def page_rect_mm() -> tuple[float, float, float, float]:
    """Paper outline in board coordinates: (x0, y0, x1, y1)."""
    ox, oy = BOARD_ON_PAGE
    return (-ox, -oy, PAGE_W_MM - ox, PAGE_H_MM - oy)


def page_corners_mm() -> np.ndarray:
    x0, y0, x1, y1 = page_rect_mm()
    return np.array([[x0, y0], [x1, y0], [x1, y1], [x0, y1]], dtype=np.float64)


def _mm(v: float, s: float) -> int:
    return int(round(v * s))


def render_page(sheet: int, px_per_mm: int = 12) -> np.ndarray:
    """Full A4 page (grayscale uint8) at an integer px/mm so sizes are exact."""
    s = px_per_mm
    page = np.full((_mm(PAGE_H_MM, s), _mm(PAGE_W_MM, s)), 255, np.uint8)
    img = board(sheet).generateImage((_mm(BOARD_W_MM, s), _mm(BOARD_H_MM, s)), marginSize=0, borderBits=1)
    ox, oy = _mm(BOARD_ON_PAGE[0], s), _mm(BOARD_ON_PAGE[1], s)
    page[oy:oy + img.shape[0], ox:ox + img.shape[1]] = img

    font, black = cv2.FONT_HERSHEY_SIMPLEX, 0
    line = max(1, s // 4)
    fs = s / 22.0
    cv2.putText(page, f"GARMENT MEASURE - reference sheet {sheet + 1}", (_mm(21, s), _mm(10, s)),
                font, fs * 1.15, black, max(1, s // 6), cv2.LINE_AA)
    cv2.putText(page, "Print at 100% / Actual size. Glue to card so it stays flat.", (_mm(21, s), _mm(17, s)),
                font, fs, black, max(1, s // 8), cv2.LINE_AA)

    # Horizontal check ruler (bottom margin).
    x0, y = 30.0, 285.0
    cv2.line(page, (_mm(x0, s), _mm(y, s)), (_mm(x0 + RULER_H_MM, s), _mm(y, s)), black, line)
    for i in range(int(RULER_H_MM / 10) + 1):
        h = 4 if i % 5 == 0 else 2
        xx = _mm(x0 + i * 10, s)
        cv2.line(page, (xx, _mm(y - h, s)), (xx, _mm(y, s)), black, line)
    cv2.putText(page, "0", (_mm(x0 - 1, s), _mm(y + 5, s)), font, fs, black, max(1, s // 8), cv2.LINE_AA)
    cv2.putText(page, "150 mm", (_mm(x0 + RULER_H_MM - 8, s), _mm(y + 5, s)), font, fs, black,
                max(1, s // 8), cv2.LINE_AA)

    # Vertical check ruler (right margin).
    x, y0 = 200.0, BOARD_ON_PAGE[1] + 1
    cv2.line(page, (_mm(x, s), _mm(y0, s)), (_mm(x, s), _mm(y0 + RULER_V_MM, s)), black, line)
    for i in range(int(RULER_V_MM / 10) + 1):
        w = 4 if i % 5 == 0 else 2
        yy = _mm(y0 + i * 10, s)
        cv2.line(page, (_mm(x - w, s), yy), (_mm(x, s), yy), black, line)
    cv2.putText(page, "0", (_mm(x + 1.5, s), _mm(y0 + 1.5, s)), font, fs, black, max(1, s // 8), cv2.LINE_AA)
    cv2.putText(page, "250", (_mm(x + 1.5, s), _mm(y0 + RULER_V_MM + 1.5, s)), font, fs, black,
                max(1, s // 8), cv2.LINE_AA)
    return page


def write_pdf(path_or_file, sheets=(0,), px_per_mm: int = 12) -> None:
    from PIL import Image

    pages = [Image.fromarray(render_page(k, px_per_mm)).convert("L") for k in sheets]
    pages[0].save(path_or_file, format="PDF", resolution=25.4 * px_per_mm, save_all=True,
                  append_images=pages[1:])

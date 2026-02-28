#!/usr/bin/env python3
"""
grid_calc.py — Calculateur de positions EMU pour stfu-slides v2.

Usage:
    python3 grid_calc.py columns N [--margin compact|spacious] [--x-start X] [--x-end X] [--gutter G]
    python3 grid_calc.py rows N [--full-page] [--margin compact|spacious] [--y-start Y] [--y-end Y] [--gutter G]
    python3 grid_calc.py grid NxM [--full-page] [--margin compact|spacious] [--gutter G]
    python3 grid_calc.py body-start CHAR_COUNT [--font-size S]

Output: JSON on stdout.
"""

import argparse
import json
import math
import sys

# === Canvas constants ===
CANVAS_W = 9_144_000
CANVAS_H = 5_143_500

# Dual margin modes
MARGINS = {
    "compact": 152_400,    # 16px — dense layouts (4+ blocks)
    "spacious": 381_000,   # 40px — airy layouts (1-3 blocks)
}
DEFAULT_MARGIN = "compact"

Y_TITLE_BOTTOM = 915_570        # sous le placeholder titre
Y_TOP = 205_740                 # haut de page utile
Y_BOTTOM = 4_738_000            # bas de page utile
DEFAULT_GUTTER = 0.15           # 15% de gouttiere

# Titre Playfair Display Black
TITLE_LINE_HEIGHT = {
    24: 380_000,  # EMU par ligne a 24pt
    20: 320_000,
    18: 290_000,
}
TITLE_CHARS_PER_LINE = {
    24: 45,  # caracteres par ligne a 24pt
    20: 54,
    18: 60,
}
TITLE_Y_DEFAULT = 300_000  # y position du titre sur layout Vide
CLEARANCE = 150_000        # espace entre bas du titre et debut du body


def resolve_margins(margin_mode, x_start_override=None, x_end_override=None):
    """Resolve x_start and x_end from margin mode, with optional overrides."""
    margin = MARGINS[margin_mode]
    x_start = x_start_override if x_start_override is not None else margin
    x_end = x_end_override if x_end_override is not None else (CANVAS_W - margin)
    return x_start, x_end


def calc_columns(n, margin_mode=DEFAULT_MARGIN, x_start=None, x_end=None, gutter_ratio=DEFAULT_GUTTER):
    """Calculate N horizontal columns."""
    x_start, x_end = resolve_margins(margin_mode, x_start, x_end)
    usable = x_end - x_start
    slot = usable / n
    col_w = int(slot * (1 - gutter_ratio))
    gutter = int(slot * gutter_ratio)

    columns = []
    for i in range(n):
        x = int(x_start + i * slot)
        columns.append({"x": x, "w": col_w})

    return {
        "columns": columns,
        "gutter": gutter,
        "usable_width": int(usable),
        "margin_mode": margin_mode,
        "x_start": int(x_start),
        "x_end": int(x_end),
    }


def calc_rows(n, full_page=False, margin_mode=DEFAULT_MARGIN, y_start=None, y_end=None, gutter_ratio=DEFAULT_GUTTER):
    """Calculate N vertical rows."""
    if y_start is None:
        y_start = Y_TOP if full_page else Y_TITLE_BOTTOM
    if y_end is None:
        y_end = Y_BOTTOM

    usable = y_end - y_start
    slot = usable / n
    row_h = int(slot * (1 - gutter_ratio))
    gutter = int(slot * gutter_ratio)

    rows = []
    for i in range(n):
        y = int(y_start + i * slot)
        rows.append({"y": y, "h": row_h})

    return {
        "rows": rows,
        "gutter": gutter,
        "usable_height": int(usable),
        "margin_mode": margin_mode,
    }


def calc_grid(cols, rows, full_page=False, margin_mode=DEFAULT_MARGIN, gutter_ratio=DEFAULT_GUTTER):
    """Calculate NxM grid (cols x rows)."""
    col_data = calc_columns(cols, margin_mode=margin_mode, gutter_ratio=gutter_ratio)
    row_data = calc_rows(rows, full_page=full_page, margin_mode=margin_mode, gutter_ratio=gutter_ratio)

    cells = []
    for r_idx, row in enumerate(row_data["rows"]):
        for c_idx, col in enumerate(col_data["columns"]):
            cells.append({
                "col": c_idx,
                "row": r_idx,
                "x": col["x"],
                "y": row["y"],
                "w": col["w"],
                "h": row["h"],
            })

    return {
        "cells": cells,
        "cols": cols,
        "rows": rows,
        "col_width": col_data["columns"][0]["w"],
        "row_height": row_data["rows"][0]["h"],
        "h_gutter": col_data["gutter"],
        "v_gutter": row_data["gutter"],
        "margin_mode": margin_mode,
    }


def calc_body_start(char_count, font_size=24, title_y=TITLE_Y_DEFAULT):
    """Calculate body start y position based on title length."""
    if font_size not in TITLE_CHARS_PER_LINE:
        return {"error": f"Font size {font_size} not supported. Use 18, 20, or 24."}

    chars_per_line = TITLE_CHARS_PER_LINE[font_size]
    line_height = TITLE_LINE_HEIGHT[font_size]
    title_lines = math.ceil(char_count / chars_per_line)

    if title_lines > 2:
        return {
            "error": "Title exceeds 2 lines — reformulate.",
            "title_lines": title_lines,
            "char_count": char_count,
            "chars_per_line": chars_per_line,
            "suggestion": f"Reduce to {chars_per_line * 2} chars max at {font_size}pt",
        }

    title_text_height = title_lines * line_height
    body_start = title_y + title_text_height + CLEARANCE

    # Ensure body_start is at least at the standard body zone
    body_start = max(body_start, Y_TITLE_BOTTOM)

    return {
        "body_start_y": int(body_start),
        "title_lines": title_lines,
        "title_text_height": int(title_text_height),
        "font_size": font_size,
        "char_count": char_count,
        "note": f"Titre {title_lines} ligne{'s' if title_lines > 1 else ''} a {font_size}pt",
    }


def main():
    parser = argparse.ArgumentParser(description="Grid calculator for stfu-slides v2")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # columns
    p_cols = subparsers.add_parser("columns", help="Calculate N horizontal columns")
    p_cols.add_argument("n", type=int, help="Number of columns")
    p_cols.add_argument("--margin", choices=["compact", "spacious"], default=DEFAULT_MARGIN)
    p_cols.add_argument("--x-start", type=int, default=None)
    p_cols.add_argument("--x-end", type=int, default=None)
    p_cols.add_argument("--gutter", type=float, default=DEFAULT_GUTTER)

    # rows
    p_rows = subparsers.add_parser("rows", help="Calculate N vertical rows")
    p_rows.add_argument("n", type=int, help="Number of rows")
    p_rows.add_argument("--full-page", action="store_true")
    p_rows.add_argument("--margin", choices=["compact", "spacious"], default=DEFAULT_MARGIN)
    p_rows.add_argument("--y-start", type=int, default=None)
    p_rows.add_argument("--y-end", type=int, default=None)
    p_rows.add_argument("--gutter", type=float, default=DEFAULT_GUTTER)

    # grid
    p_grid = subparsers.add_parser("grid", help="Calculate NxM grid")
    p_grid.add_argument("spec", help="Grid spec as NxM (e.g. 3x2)")
    p_grid.add_argument("--full-page", action="store_true")
    p_grid.add_argument("--margin", choices=["compact", "spacious"], default=DEFAULT_MARGIN)
    p_grid.add_argument("--gutter", type=float, default=DEFAULT_GUTTER)

    # body-start
    p_body = subparsers.add_parser("body-start", help="Calculate body start y from title length")
    p_body.add_argument("char_count", type=int, help="Number of characters in title")
    p_body.add_argument("--font-size", type=int, default=24, choices=[18, 20, 24])

    args = parser.parse_args()

    if args.command == "columns":
        result = calc_columns(args.n, args.margin, args.x_start, args.x_end, args.gutter)
    elif args.command == "rows":
        result = calc_rows(args.n, args.full_page, args.margin, args.y_start, args.y_end, args.gutter)
    elif args.command == "grid":
        parts = args.spec.split("x")
        if len(parts) != 2:
            print(json.dumps({"error": "Grid spec must be NxM (e.g. 3x2)"}))
            sys.exit(1)
        cols, rows = int(parts[0]), int(parts[1])
        result = calc_grid(cols, rows, args.full_page, args.margin, args.gutter)
    elif args.command == "body-start":
        result = calc_body_start(args.char_count, args.font_size)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

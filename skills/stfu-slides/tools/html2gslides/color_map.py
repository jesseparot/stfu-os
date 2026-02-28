"""CSS color → Google Slides API {red, green, blue} (0-1 float) converter."""

from __future__ import annotations

import re
from typing import Optional

# Precomputed named colors we actually use
_NAMED_COLORS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "transparent": None,
}


def parse_css_color(value: str) -> Optional[dict]:
    """Parse a CSS color string to API format {red, green, blue} (0-1 floats).

    Supports: rgb(), rgba(), hex (#RGB, #RRGGBB, #RRGGBBAA), named colors.
    Returns None for transparent or unparseable values.
    """
    value = value.strip().lower()

    if not value or value == "transparent" or value == "initial" or value == "inherit":
        return None

    # Named color
    if value in _NAMED_COLORS:
        rgb = _NAMED_COLORS[value]
        if rgb is None:
            return None
        return {"red": rgb[0] / 255, "green": rgb[1] / 255, "blue": rgb[2] / 255}

    # rgb(R, G, B) or rgba(R, G, B, A)
    m = re.match(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)", value)
    if m:
        r, g, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return {"red": r / 255, "green": g / 255, "blue": b / 255}

    # Hex
    m = re.match(r"#([0-9a-f]+)$", value)
    if m:
        h = m.group(1)
        if len(h) == 3:
            r, g, b = int(h[0] * 2, 16), int(h[1] * 2, 16), int(h[2] * 2, 16)
        elif len(h) in (6, 8):
            r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
        else:
            return None
        return {"red": round(r / 255, 3), "green": round(g / 255, 3), "blue": round(b / 255, 3)}

    return None


def colors_equal(a: Optional[dict], b: Optional[dict], tolerance: float = 0.02) -> bool:
    """Check if two API colors are approximately equal."""
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return all(abs(a[k] - b[k]) <= tolerance for k in ("red", "green", "blue"))

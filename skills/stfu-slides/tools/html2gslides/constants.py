"""Constants for HTML → Google Slides conversion."""

# 1px CSS = 9525 EMU (exact)
EMU_PER_PX = 9525

# Canvas dimensions (Google Slides 16:9)
CANVAS_W_PX = 960
CANVAS_H_PX = 540
CANVAS_W_EMU = CANVAS_W_PX * EMU_PER_PX  # 9,144,000
CANVAS_H_EMU = CANVAS_H_PX * EMU_PER_PX  # 5,143,500

# Layout 5 — Vide (all slides use this; we place everything from scratch)
LAYOUT_BLANK_ID = "g386b92f88e9_0_46"

# Colors (API format: 0-1 float)
BLACK = {"red": 0, "green": 0, "blue": 0}
WHITE = {"red": 1, "green": 1, "blue": 1}
DK2 = {"red": 0.263, "green": 0.263, "blue": 0.263}
GRAY = {"red": 0.478, "green": 0.478, "blue": 0.478}
YELLOW_STFU = {"red": 1, "green": 0.886, "blue": 0}
LT2 = {"red": 0.953, "green": 0.953, "blue": 0.953}


def px_to_emu(px: float) -> int:
    """Convert CSS pixels to EMU."""
    return int(round(px * EMU_PER_PX))

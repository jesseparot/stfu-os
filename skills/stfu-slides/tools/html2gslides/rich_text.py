"""Convert extracted inline segments → plain text + FIXED_RANGE style runs.

Input: list of segments from extract.py, each with {text, style}.
Output: (plain_text, style_runs) where each style_run is:
    {startIndex, endIndex, fontFamily, fontSize, bold, italic, foregroundColor}
"""

from __future__ import annotations

from typing import List, Tuple

from .color_map import parse_css_color, colors_equal


def _normalize_font_family(family: str) -> str:
    """Map CSS font family to Google Slides API font family."""
    f = family.strip().strip("'\"")
    # Map weight-specific names
    if f.lower() in ("playfair display", "playfair display black"):
        return "Playfair Display"
    if f.lower() in ("lato", "lato black"):
        return "Lato"
    if f.lower() in ("fira code",):
        return "Fira Code"
    return f


def _font_size_px_to_pt(px: float) -> float:
    """Convert CSS px to pt (1pt = 1.333px at 96dpi)."""
    return round(px * 0.75, 1)


def segments_to_styled_text(
    segments: list[dict],
    separator: str = "",
) -> tuple[str, list[dict]]:
    """Convert extracted segments to plain text + style runs.

    Args:
        segments: List of {text, style} from extract.py.
        separator: String to insert between segments (usually "" for inline,
                   "\\n" for list items).

    Returns:
        (plain_text, style_runs)
    """
    if not segments:
        return "", []

    plain_parts = []
    runs = []
    cursor = 0

    for i, seg in enumerate(segments):
        text = seg["text"]
        style = seg.get("style", {})

        # Apply text-transform
        transform = style.get("textTransform", "none")
        if transform == "uppercase":
            text = text.upper()
        elif transform == "capitalize":
            text = text.title()

        plain_parts.append(text)
        end = cursor + len(text)

        # Build style run
        font_family = _normalize_font_family(style.get("fontFamily", "Lato"))
        font_size_px = style.get("fontSize", 10.67)  # default ~8pt
        font_size_pt = _font_size_px_to_pt(font_size_px)
        font_weight = style.get("fontWeight", 400)
        is_bold = font_weight >= 700
        is_italic = style.get("fontStyle", "normal") == "italic"
        color = parse_css_color(style.get("color", "rgb(0,0,0)"))

        run = {
            "startIndex": cursor,
            "endIndex": end,
            "fontFamily": font_family,
            "fontSize": font_size_pt,
            "bold": is_bold,
            "italic": is_italic,
            "foregroundColor": color,
        }
        runs.append(run)

        cursor = end
        if separator and i < len(segments) - 1:
            plain_parts.append(separator)
            cursor += len(separator)

    plain_text = "".join(plain_parts)

    # Merge adjacent runs with identical styles
    merged = _merge_runs(runs)

    return plain_text, merged


def _merge_runs(runs: list[dict]) -> list[dict]:
    """Merge adjacent runs with identical styles."""
    if not runs:
        return []

    merged = [runs[0].copy()]
    for run in runs[1:]:
        prev = merged[-1]
        if (
            prev["endIndex"] == run["startIndex"]
            and prev["fontFamily"] == run["fontFamily"]
            and prev["fontSize"] == run["fontSize"]
            and prev["bold"] == run["bold"]
            and prev["italic"] == run["italic"]
            and colors_equal(prev["foregroundColor"], run["foregroundColor"])
        ):
            prev["endIndex"] = run["endIndex"]
        else:
            merged.append(run.copy())

    return merged


def list_items_to_styled_text(
    items: list[dict],
) -> tuple[str, list[dict]]:
    """Convert list items (each with segments) to a single text block.

    Each <li> is separated by \\n. Last <li> has no trailing \\n.

    Returns:
        (plain_text, style_runs)
    """
    all_segments = []
    for i, item in enumerate(items):
        segs = item.get("segments", [])
        all_segments.extend(segs)
        if i < len(items) - 1:
            # Add newline separator as a segment with the same style as last segment
            last_style = segs[-1]["style"] if segs else {}
            all_segments.append({"text": "\n", "style": last_style})

    return segments_to_styled_text(all_segments)

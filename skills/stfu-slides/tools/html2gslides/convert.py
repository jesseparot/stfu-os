"""Convert extracted elements → Google Slides batch_update requests.

Each slide uses Layout 5 (Vide) — everything placed from scratch.
HTML bounding rects × 9525 = EMU positions.
"""

from __future__ import annotations

from typing import List, Tuple

from .constants import (
    LAYOUT_BLANK_ID,
    BLACK,
    WHITE,
    px_to_emu,
)
from .color_map import parse_css_color
from .rich_text import segments_to_styled_text, list_items_to_styled_text


def _id_gen(slide_id: str):
    """Generate unique element IDs for a slide."""
    counter = [0]

    def next_id(prefix: str = "el") -> str:
        counter[0] += 1
        return f"{slide_id}_{prefix}{counter[0]:03d}"

    return next_id


def _make_size(w_px: float, h_px: float) -> dict:
    return {
        "width": {"magnitude": px_to_emu(w_px), "unit": "EMU"},
        "height": {"magnitude": px_to_emu(h_px), "unit": "EMU"},
    }


def _make_transform(x_px: float, y_px: float) -> dict:
    return {
        "scaleX": 1,
        "scaleY": 1,
        "translateX": px_to_emu(x_px),
        "translateY": px_to_emu(y_px),
        "unit": "EMU",
    }


def _create_text_box(object_id: str, slide_id: str, el: dict) -> list[dict]:
    """Create a TEXT_BOX with styled text from an extracted text element."""
    requests = []

    # Create shape
    requests.append({
        "createShape": {
            "objectId": object_id,
            "shapeType": "TEXT_BOX",
            "elementProperties": {
                "pageObjectId": slide_id,
                "size": _make_size(el["w"], el["h"]),
                "transform": _make_transform(el["x"], el["y"]),
            },
        }
    })

    # Convert segments to styled text
    segments = el.get("segments", [])
    plain_text, style_runs = segments_to_styled_text(segments)

    if not plain_text.strip():
        return requests

    # Insert text
    requests.append({
        "insertText": {
            "objectId": object_id,
            "text": plain_text,
        }
    })

    # Apply style runs
    for run in style_runs:
        style = {
            "fontFamily": run["fontFamily"],
            "fontSize": {"magnitude": run["fontSize"], "unit": "PT"},
            "bold": run["bold"],
        }
        fields = ["fontFamily", "fontSize", "bold"]

        if run.get("italic"):
            style["italic"] = True
            fields.append("italic")

        if run.get("foregroundColor"):
            style["foregroundColor"] = {"opaqueColor": {"rgbColor": run["foregroundColor"]}}
            fields.append("foregroundColor")

        requests.append({
            "updateTextStyle": {
                "objectId": object_id,
                "textRange": {
                    "type": "FIXED_RANGE",
                    "startIndex": run["startIndex"],
                    "endIndex": run["endIndex"],
                },
                "style": style,
                "fields": ",".join(fields),
            }
        })

    # Paragraph alignment
    text_align = el.get("textAlign", "left")
    if text_align and text_align != "left":
        align_map = {"center": "CENTER", "right": "END", "justify": "JUSTIFIED"}
        api_align = align_map.get(text_align)
        if api_align:
            requests.append({
                "updateParagraphStyle": {
                    "objectId": object_id,
                    "textRange": {"type": "ALL"},
                    "style": {"alignment": api_align},
                    "fields": "alignment",
                }
            })

    # Content alignment: TOP
    requests.append({
        "updateShapeProperties": {
            "objectId": object_id,
            "shapeProperties": {"contentAlignment": "TOP"},
            "fields": "contentAlignment",
        }
    })

    return requests


def _create_list_box(object_id: str, slide_id: str, el: dict) -> list[dict]:
    """Create a TEXT_BOX with bullet list content."""
    requests = []

    # Create shape
    requests.append({
        "createShape": {
            "objectId": object_id,
            "shapeType": "TEXT_BOX",
            "elementProperties": {
                "pageObjectId": slide_id,
                "size": _make_size(el["w"], el["h"]),
                "transform": _make_transform(el["x"], el["y"]),
            },
        }
    })

    # Convert list items to styled text
    items = el.get("items", [])
    plain_text, style_runs = list_items_to_styled_text(items)

    if not plain_text.strip():
        return requests

    # Insert text
    requests.append({
        "insertText": {
            "objectId": object_id,
            "text": plain_text,
        }
    })

    # Apply style runs
    for run in style_runs:
        style = {
            "fontFamily": run["fontFamily"],
            "fontSize": {"magnitude": run["fontSize"], "unit": "PT"},
            "bold": run["bold"],
        }
        fields = ["fontFamily", "fontSize", "bold"]

        if run.get("italic"):
            style["italic"] = True
            fields.append("italic")

        if run.get("foregroundColor"):
            style["foregroundColor"] = {"opaqueColor": {"rgbColor": run["foregroundColor"]}}
            fields.append("foregroundColor")

        requests.append({
            "updateTextStyle": {
                "objectId": object_id,
                "textRange": {
                    "type": "FIXED_RANGE",
                    "startIndex": run["startIndex"],
                    "endIndex": run["endIndex"],
                },
                "style": style,
                "fields": ",".join(fields),
            }
        })

    # Create bullets for all paragraphs
    requests.append({
        "createParagraphBullets": {
            "objectId": object_id,
            "textRange": {"type": "ALL"},
            "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE" if not el.get("ordered") else "NUMBERED_DIGIT_ALPHA_ROMAN",
        }
    })

    # Content alignment: TOP
    requests.append({
        "updateShapeProperties": {
            "objectId": object_id,
            "shapeProperties": {"contentAlignment": "TOP"},
            "fields": "contentAlignment",
        }
    })

    return requests


def _create_table(object_id: str, slide_id: str, el: dict) -> list[dict]:
    """Create a table from extracted table data."""
    requests = []
    rows = el.get("rows", [])
    if not rows:
        return requests

    num_rows = len(rows)
    num_cols = max(len(row) for row in rows)

    # Create table
    requests.append({
        "createTable": {
            "objectId": object_id,
            "elementProperties": {
                "pageObjectId": slide_id,
                "size": _make_size(el["w"], el["h"]),
                "transform": _make_transform(el["x"], el["y"]),
            },
            "rows": num_rows,
            "columns": num_cols,
        }
    })

    # Insert text and style each cell
    for row_idx, row in enumerate(rows):
        for col_idx, cell in enumerate(row):
            cell_id = f"{object_id}.{row_idx}.{col_idx}"
            text = cell.get("text", "")
            if not text:
                continue

            # Insert text into cell
            requests.append({
                "insertText": {
                    "objectId": object_id,
                    "cellLocation": {
                        "rowIndex": row_idx,
                        "columnIndex": col_idx,
                    },
                    "text": text,
                }
            })

            # Style the cell text
            segments = cell.get("segments", [])
            if segments:
                _, style_runs = segments_to_styled_text(segments)
                for run in style_runs:
                    style = {
                        "fontFamily": run["fontFamily"],
                        "fontSize": {"magnitude": run["fontSize"], "unit": "PT"},
                        "bold": run["bold"],
                    }
                    fields = ["fontFamily", "fontSize", "bold"]

                    if run.get("foregroundColor"):
                        style["foregroundColor"] = {"opaqueColor": {"rgbColor": run["foregroundColor"]}}
                        fields.append("foregroundColor")

                    requests.append({
                        "updateTextStyle": {
                            "objectId": object_id,
                            "cellLocation": {
                                "rowIndex": row_idx,
                                "columnIndex": col_idx,
                            },
                            "textRange": {
                                "type": "FIXED_RANGE",
                                "startIndex": run["startIndex"],
                                "endIndex": run["endIndex"],
                            },
                            "style": style,
                            "fields": ",".join(fields),
                        }
                    })

            # Style header cells
            if cell.get("isHeader"):
                bg_color = parse_css_color(cell.get("backgroundColor", "")) or BLACK
                requests.append({
                    "updateTableCellProperties": {
                        "objectId": object_id,
                        "tableRange": {
                            "location": {"rowIndex": row_idx, "columnIndex": col_idx},
                            "rowSpan": 1,
                            "columnSpan": 1,
                        },
                        "tableCellProperties": {
                            "tableCellBackgroundFill": {
                                "solidFill": {"color": {"rgbColor": bg_color}}
                            }
                        },
                        "fields": "tableCellBackgroundFill.solidFill.color",
                    }
                })

    return requests


def _create_shape(object_id: str, slide_id: str, el: dict) -> list[dict]:
    """Create a rectangle shape (background div)."""
    requests = []
    bg_color = parse_css_color(el.get("backgroundColor", ""))
    if not bg_color:
        return requests

    requests.append({
        "createShape": {
            "objectId": object_id,
            "shapeType": "RECTANGLE",
            "elementProperties": {
                "pageObjectId": slide_id,
                "size": _make_size(el["w"], el["h"]),
                "transform": _make_transform(el["x"], el["y"]),
            },
        }
    })

    # Fill color
    requests.append({
        "updateShapeProperties": {
            "objectId": object_id,
            "shapeProperties": {
                "shapeBackgroundFill": {
                    "solidFill": {
                        "color": {"rgbColor": bg_color}
                    }
                },
                "outline": {"outlineFill": {"solidFill": {"color": {"rgbColor": bg_color}}}, "weight": {"magnitude": 0, "unit": "PT"}},
            },
            "fields": "shapeBackgroundFill.solidFill.color,outline",
        }
    })

    return requests


def _create_image(object_id: str, slide_id: str, el: dict) -> list[dict]:
    """Create an image placeholder (flag for manual upload)."""
    # Images need to be publicly accessible URLs for createImage
    # Local file:// URLs won't work — flag them
    src = el.get("src", "")
    if src.startswith("file://") or src.startswith("/") or src.startswith("."):
        return [{
            "_warning": {
                "type": "local_image",
                "src": src,
                "position": {"x": el["x"], "y": el["y"], "w": el["w"], "h": el["h"]},
                "message": "Local image — upload to Drive and use public URL",
            }
        }]

    return [{
        "createImage": {
            "objectId": object_id,
            "url": src,
            "elementProperties": {
                "pageObjectId": slide_id,
                "size": _make_size(el["w"], el["h"]),
                "transform": _make_transform(el["x"], el["y"]),
            },
        }
    }]


def convert_slide(
    extraction: dict,
    slide_id: str,
    slide_index: int = 0,
) -> list[dict]:
    """Convert extraction data for one slide into batch_update requests.

    Args:
        extraction: Output from extract.extract_slide().
        slide_id: Object ID for the new slide (min 5 chars).
        slide_index: Optional insertion index.

    Returns:
        List of batch_update request dicts.
    """
    gen_id = _id_gen(slide_id)
    requests = []
    warnings = []

    # Create the slide (Layout 5 — Vide)
    requests.append({
        "createSlide": {
            "objectId": slide_id,
            "slideLayoutReference": {"layoutId": LAYOUT_BLANK_ID},
        }
    })

    # Set background color if not white
    bg_color = parse_css_color(extraction.get("background", ""))
    if bg_color and not (
        abs(bg_color["red"] - 1) < 0.02
        and abs(bg_color["green"] - 1) < 0.02
        and abs(bg_color["blue"] - 1) < 0.02
    ):
        # Handle gradient backgrounds: extract dominant color
        bg_image = extraction.get("backgroundImage", "")
        if bg_image and bg_image != "none":
            # Gradient — use the solid background color as fallback
            warnings.append({
                "type": "gradient_background",
                "value": bg_image,
                "fallback": bg_color,
            })

        requests.append({
            "updatePageProperties": {
                "objectId": slide_id,
                "pageProperties": {
                    "pageBackgroundFill": {
                        "solidFill": {
                            "color": {"rgbColor": bg_color}
                        }
                    }
                },
                "fields": "pageBackgroundFill.solidFill.color",
            }
        })

    # Process elements in order (z-order from DOM)
    for el in extraction.get("elements", []):
        el_type = el.get("type")

        if el_type == "text":
            obj_id = gen_id("txt")
            requests.extend(_create_text_box(obj_id, slide_id, el))

        elif el_type == "list":
            obj_id = gen_id("lst")
            requests.extend(_create_list_box(obj_id, slide_id, el))

        elif el_type == "table":
            obj_id = gen_id("tbl")
            requests.extend(_create_table(obj_id, slide_id, el))

        elif el_type == "shape":
            obj_id = gen_id("shp")
            requests.extend(_create_shape(obj_id, slide_id, el))

        elif el_type == "image":
            obj_id = gen_id("img")
            result = _create_image(obj_id, slide_id, el)
            for r in result:
                if "_warning" in r:
                    warnings.append(r["_warning"])
                else:
                    requests.append(r)

    # Collect extraction warnings
    for w in extraction.get("warnings", []):
        warnings.append(w)

    return requests, warnings


def convert_deck(
    extractions: list[dict],
    id_prefix: str = "sl",
) -> dict:
    """Convert a full deck of extractions into batch_update JSON.

    Returns:
        {
            "requests": [...],
            "warnings": [...],
            "slides": [{slide_id, source_file, num_requests, num_warnings}]
        }
    """
    all_requests = []
    all_warnings = []
    slide_info = []

    for i, extraction in enumerate(extractions):
        slide_id = f"{id_prefix}{i + 1:03d}"
        requests, warnings = convert_slide(extraction, slide_id, slide_index=i)

        # Tag warnings with slide info
        source = extraction.get("source_file", f"slide_{i + 1}")
        for w in warnings:
            w["slide"] = slide_id
            w["source"] = source

        all_requests.extend(requests)
        all_warnings.extend(warnings)
        slide_info.append({
            "slide_id": slide_id,
            "source_file": source,
            "num_requests": len(requests),
            "num_warnings": len(warnings),
        })

    return {
        "requests": all_requests,
        "warnings": all_warnings,
        "slides": slide_info,
    }

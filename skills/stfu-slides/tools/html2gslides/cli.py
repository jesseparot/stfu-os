"""CLI for html2gslides compiler.

Usage:
    # Single slide
    python3 -m html2gslides slide.html --slide-id sl001

    # Full deck (from deck.json manifest or slides/ glob)
    python3 -m html2gslides deck/ --output requests.json

    # Dry run (summary without JSON)
    python3 -m html2gslides deck/ --dry-run
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        prog="html2gslides",
        description="Compile HTML slides to Google Slides batch_update JSON",
    )
    parser.add_argument(
        "input",
        help="Path to a single .html slide or a deck directory",
    )
    parser.add_argument(
        "--slide-id",
        default="sl001",
        help="Slide object ID (single slide mode, default: sl001)",
    )
    parser.add_argument(
        "--id-prefix",
        default="sl",
        help="Slide ID prefix (deck mode, default: sl)",
    )
    parser.add_argument(
        "--output", "-o",
        help="Output JSON file (default: stdout)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print summary without JSON output",
    )

    args = parser.parse_args()
    input_path = Path(args.input).resolve()

    if input_path.is_file() and input_path.suffix == ".html":
        result = asyncio.run(_compile_single(input_path, args.slide_id))
    elif input_path.is_dir():
        result = asyncio.run(_compile_deck(input_path, args.id_prefix))
    else:
        print(f"Error: {args.input} is not an HTML file or directory", file=sys.stderr)
        sys.exit(1)

    if args.dry_run:
        _print_summary(result)
        return

    output_json = json.dumps({"requests": result["requests"]}, ensure_ascii=False, indent=2)

    if args.output:
        Path(args.output).write_text(output_json)
        print(f"Written {len(result['requests'])} requests to {args.output}", file=sys.stderr)
    else:
        print(output_json)

    # Print warnings to stderr
    if result.get("warnings"):
        print(f"\n⚠ {len(result['warnings'])} warnings:", file=sys.stderr)
        for w in result["warnings"]:
            print(f"  [{w.get('slide', '?')}] {w.get('type', '?')}: {w.get('message', w)}", file=sys.stderr)


async def _compile_single(html_path: Path, slide_id: str) -> dict:
    """Compile a single HTML slide."""
    from playwright.async_api import async_playwright
    from .extract import extract_slide
    from .convert import convert_slide

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 960, "height": 540})
        extraction = await extract_slide(page, html_path)
        await browser.close()

    requests, warnings = convert_slide(extraction, slide_id)
    return {"requests": requests, "warnings": warnings}


async def _compile_deck(deck_dir: Path, id_prefix: str) -> dict:
    """Compile a full deck."""
    from .extract import extract_deck
    from .convert import convert_deck

    extractions = await extract_deck(deck_dir)
    return convert_deck(extractions, id_prefix)


def _print_summary(result: dict):
    """Print a human-readable summary."""
    total_requests = len(result.get("requests", []))
    slides = result.get("slides", [])
    warnings = result.get("warnings", [])

    print(f"Compilation summary")
    print(f"{'='*50}")

    if slides:
        for s in slides:
            print(f"  {s['slide_id']} ({s['source_file']}): {s['num_requests']} requests, {s['num_warnings']} warnings")
    else:
        print(f"  Single slide: {total_requests} requests")

    print(f"\nTotal: {total_requests} requests")

    if warnings:
        print(f"\nWarnings ({len(warnings)}):")
        for w in warnings:
            slide = w.get("slide", "")
            wtype = w.get("type", "unknown")
            msg = w.get("message", str(w))
            print(f"  [{slide}] {wtype}: {msg}")
    else:
        print("\nNo warnings.")

"""Extract visual elements from HTML slides using Playwright.

Renders each slide HTML in a headless browser, walks the DOM,
and extracts bounding rects + computed styles + inline text segments.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Union

# JS injected into the page to extract element data
_EXTRACT_JS = """
() => {
    const slide = document.querySelector('.slide');
    if (!slide) return {error: 'No .slide element found'};

    const rect = slide.getBoundingClientRect();
    const slideW = rect.width;
    const slideH = rect.height;
    const cs = getComputedStyle(slide);

    const result = {
        width: slideW,
        height: slideH,
        background: cs.backgroundColor,
        backgroundImage: cs.backgroundImage,
        elements: [],
        warnings: []
    };

    // Walk visible elements
    function shouldSkip(el) {
        const tag = el.tagName.toLowerCase();
        if (tag === 'style' || tag === 'script' || tag === 'link') return true;
        const s = getComputedStyle(el);
        if (s.display === 'none' || s.visibility === 'hidden') return true;
        return false;
    }

    function getTextSegments(el) {
        // Walk childNodes to extract inline text segments with their styles
        const segments = [];
        function walkInline(node, inheritedStyle) {
            if (node.nodeType === 3) {
                // Text node
                const text = node.textContent;
                if (text.trim().length > 0) {
                    segments.push({text: text, style: {...inheritedStyle}});
                }
                return;
            }
            if (node.nodeType !== 1) return;

            const el = node;
            const tag = el.tagName.toLowerCase();
            const cs = getComputedStyle(el);

            // Build style for this element
            const style = {...inheritedStyle};
            style.fontFamily = cs.fontFamily.split(',')[0].replace(/['"]/g, '').trim();
            style.fontSize = parseFloat(cs.fontSize);
            style.fontWeight = parseInt(cs.fontWeight);
            style.fontStyle = cs.fontStyle;
            style.color = cs.color;
            style.textTransform = cs.textTransform;
            style.textDecoration = cs.textDecoration;

            // Handle <br> as newline
            if (tag === 'br') {
                segments.push({text: '\\n', style: {...inheritedStyle}});
                return;
            }

            if (tag === 'strong' || tag === 'b') style.fontWeight = Math.max(style.fontWeight, 700);
            if (tag === 'em' || tag === 'i') style.fontStyle = 'italic';
            if (tag === 'code') style.fontFamily = cs.fontFamily.split(',')[0].replace(/['"]/g, '').trim();

            for (const child of el.childNodes) {
                walkInline(child, style);
            }
        }

        const baseStyle = {
            fontFamily: getComputedStyle(el).fontFamily.split(',')[0].replace(/['"]/g, '').trim(),
            fontSize: parseFloat(getComputedStyle(el).fontSize),
            fontWeight: parseInt(getComputedStyle(el).fontWeight),
            fontStyle: getComputedStyle(el).fontStyle,
            color: getComputedStyle(el).color,
            textTransform: getComputedStyle(el).textTransform,
            textDecoration: getComputedStyle(el).textDecoration
        };

        for (const child of el.childNodes) {
            walkInline(child, baseStyle);
        }
        return segments;
    }

    function extractElement(el) {
        const tag = el.tagName.toLowerCase();
        const cs = getComputedStyle(el);
        const r = el.getBoundingClientRect();

        // Skip zero-size elements
        if (r.width < 1 && r.height < 1) return null;

        // Position relative to slide
        const x = r.left - rect.left;
        const y = r.top - rect.top;
        const w = r.width;
        const h = r.height;

        // Check for pseudo-elements
        const beforeContent = getComputedStyle(el, '::before').content;
        const afterContent = getComputedStyle(el, '::after').content;
        if (beforeContent && beforeContent !== 'none' && beforeContent !== '""' && beforeContent !== "''") {
            result.warnings.push({type: 'pseudo_element', element: tag, pseudo: '::before', classes: el.className});
        }
        if (afterContent && afterContent !== 'none' && afterContent !== '""' && afterContent !== "''") {
            result.warnings.push({type: 'pseudo_element', element: tag, pseudo: '::after', classes: el.className});
        }

        const base = {x, y, w, h, tag, classes: el.className || ''};

        // Images
        if (tag === 'img') {
            return {...base, type: 'image', src: el.src};
        }

        // Tables
        if (tag === 'table') {
            const rows = [];
            for (const tr of el.querySelectorAll('tr')) {
                const cells = [];
                for (const cell of tr.querySelectorAll('th, td')) {
                    const cellCs = getComputedStyle(cell);
                    cells.push({
                        text: cell.textContent.trim(),
                        segments: getTextSegments(cell),
                        isHeader: cell.tagName.toLowerCase() === 'th',
                        backgroundColor: cellCs.backgroundColor,
                        textAlign: cellCs.textAlign
                    });
                }
                rows.push(cells);
            }
            return {...base, type: 'table', rows};
        }

        // Lists (ul/ol) — extract as list type
        if (tag === 'ul' || tag === 'ol') {
            const items = [];
            for (const li of el.querySelectorAll(':scope > li')) {
                items.push({
                    segments: getTextSegments(li)
                });
            }
            return {...base, type: 'list', ordered: tag === 'ol', items};
        }

        // Text elements
        if (['h1', 'h2', 'h3', 'h4', 'p', 'span', 'div', 'blockquote', 'cite'].includes(tag)) {
            // Check if it's a text container or just a layout div
            const hasDirectText = Array.from(el.childNodes).some(
                n => n.nodeType === 3 && n.textContent.trim().length > 0
            );
            const hasInlineChildren = Array.from(el.children).some(c => {
                const d = getComputedStyle(c).display;
                return d === 'inline' || d === 'inline-block';
            });

            if (hasDirectText || hasInlineChildren || ['h1','h2','h3','h4','p'].includes(tag)) {
                const segments = getTextSegments(el);
                if (segments.length === 0) return null;

                const textAlign = cs.textAlign;

                return {
                    ...base,
                    type: 'text',
                    segments,
                    textAlign: textAlign === 'start' ? 'left' : textAlign
                };
            }

            // Layout div with background — treat as shape
            if (cs.backgroundColor && cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && cs.backgroundColor !== 'transparent') {
                return {...base, type: 'shape', backgroundColor: cs.backgroundColor};
            }

            return null;
        }

        return null;
    }

    // Walk the slide's descendants
    function walk(parent) {
        for (const child of parent.children) {
            if (shouldSkip(child)) continue;

            const tag = child.tagName.toLowerCase();

            // Extract this element
            const data = extractElement(child);
            if (data) {
                result.elements.push(data);
                // Don't recurse into text/list/table elements (already extracted inline)
                if (['text', 'list', 'table', 'image'].includes(data.type)) continue;
            }

            // Recurse for layout containers
            walk(child);
        }
    }

    walk(slide);
    return result;
}
"""


async def extract_slide(page, html_path: Union[str, Path]) -> dict:
    """Extract elements from a single slide HTML file.

    Args:
        page: Playwright page object (already created).
        html_path: Path to the HTML file.

    Returns:
        Dict with keys: width, height, background, elements[], warnings[].
    """
    html_path = Path(html_path).resolve()
    await page.goto(f"file://{html_path}")

    # Wait for fonts to load
    await page.wait_for_function("document.fonts.ready.then(() => true)")
    # Small extra wait for layout to settle
    await page.wait_for_timeout(200)

    result = await page.evaluate(_EXTRACT_JS)

    if isinstance(result, dict) and "error" in result:
        raise RuntimeError(f"Extraction failed: {result['error']}")

    return result


async def extract_deck(deck_dir: Union[str, Path]) -> List[dict]:
    """Extract all slides from a deck directory.

    Expects a deck.json manifest with a 'slides' array of relative paths.

    Returns:
        List of extraction results, one per slide.
    """
    from playwright.async_api import async_playwright

    deck_dir = Path(deck_dir).resolve()
    manifest_path = deck_dir / "deck.json"

    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        slide_paths = [deck_dir / s for s in manifest["slides"]]
    else:
        # Fallback: glob for slides/*.html sorted by name
        slide_paths = sorted((deck_dir / "slides").glob("*.html"))

    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 960, "height": 540})

        for path in slide_paths:
            data = await extract_slide(page, path)
            data["source_file"] = str(path.relative_to(deck_dir))
            results.append(data)

        await browser.close()

    return results

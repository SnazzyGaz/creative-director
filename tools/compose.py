#!/usr/bin/env python3
"""compose.py: deterministic art-plate + locked-copy + official-mark + chart compositor.

Why this exists:
  Asking an image generator to spell locked copy (CD-7), draw accurate data bars (LAY-19),
  or reproduce an official logo unaltered (BRAND-4) is fragile. Generate clean art plates,
  then composite exact symbolic elements in code.

Outputs:
  1. Rendered PNG at --out
  2. Exact text manifest at <stem>-boxes.json (automatically read by cd.py check for CD-7 copy,
     LAY-5 safe area, and UI-6 / LAY-15 worst-pixel contrast!)
  3. Optional standalone HTML/SVG file at --html (for Playwright/browser rendering)

Usage:
  python3 tools/compose.py spec.json --out final.png [--html final.html] [--allow-unsafe]
"""
import argparse
import html as html_lib
import json
import math
from pathlib import Path
import sys
from PIL import Image, ImageColor, ImageDraw, ImageFont

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]


def parse_color(value, default=(17, 24, 39)):
    if value is None:
        return default
    if isinstance(value, (list, tuple)) and len(value) in (3, 4):
        return tuple(int(v) for v in value[:3])
    if isinstance(value, str):
        rgb = ImageColor.getrgb(value)
        return rgb[:3]
    raise ValueError(f'unsupported color: {value!r}')


def find_font(font_spec=None, size=24):
    """Resolve a TrueType font from explicit path, repo fonts/, or common OS font directories."""
    candidates = []
    if font_spec:
        p = Path(font_spec)
        if p.is_file():
            candidates.append(p)
        elif (ROOT / font_spec).is_file():
            candidates.append(ROOT / font_spec)
        else:
            needle = font_spec.lower()
            if (ROOT / 'fonts').is_dir():
                for ttf in sorted((ROOT / 'fonts').rglob('*.ttf')):
                    if needle in ttf.stem.lower():
                        candidates.append(ttf)
                        break

    # Bundled clean fallback sans font in docs/assets or fonts/
    bundled = [
        ROOT / 'docs/assets/src/fonts/InstrumentSans-VariableFont_wdth,wght.ttf',
    ]
    if (ROOT / 'fonts').is_dir():
        bundled.extend(sorted((ROOT / 'fonts').rglob('*.ttf'))[:10])

    system_fonts = [
        Path('C:/Windows/Fonts/arialbd.ttf') if str(font_spec).lower() == 'bold' else Path('C:/Windows/Fonts/arial.ttf'),
        Path('C:/Windows/Fonts/segoeui.ttf'),
        Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if str(font_spec).lower() == 'bold' else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'),
        Path('/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'),
        Path('/System/Library/Fonts/Helvetica.ttc'),
    ]

    for path in [*candidates, *bundled, *system_fonts]:
        if path and path.is_file():
            try:
                return ImageFont.truetype(str(path), size=int(size)), str(path)
            except OSError:
                continue
    return ImageFont.load_default(size=int(size)), 'pillow-default'


def fit_cover(im, width, height):
    src_ratio = im.width / im.height
    dst_ratio = width / height
    if src_ratio > dst_ratio:
        new_h = height
        new_w = max(width, round(height * src_ratio))
    else:
        new_w = width
        new_h = max(height, round(width / src_ratio))
    resized = im.resize((new_w, new_h), Image.LANCZOS)
    x0 = (new_w - width) // 2
    y0 = (new_h - height) // 2
    return resized.crop((x0, y0, x0 + width, y0 + height))


def wrap_text(draw, text, font, max_width):
    if not max_width:
        return text.splitlines() or ['']
    lines = []
    for para in text.splitlines():
        words = para.split()
        if not words:
            lines.append('')
            continue
        cur = words[0]
        for w in words[1:]:
            test = cur + ' ' + w
            bbox = draw.textbbox((0, 0), test, font=font)
            if (bbox[2] - bbox[0]) <= max_width:
                cur = test
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    return lines


def draw_panel(canvas, panel):
    x0, y0, x1, y1 = [int(round(v)) for v in panel['box']]
    rgb = parse_color(panel.get('fill', '#FFFFFF'))
    opacity = float(panel.get('opacity', 1.0))
    radius = int(panel.get('radius', 0))
    alpha = max(0, min(255, round(opacity * 255)))
    overlay = Image.new('RGBA', canvas.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    if radius > 0:
        od.rounded_rectangle([x0, y0, x1, y1], radius=radius, fill=(*rgb, alpha))
    else:
        od.rectangle([x0, y0, x1, y1], fill=(*rgb, alpha))
    if panel.get('stroke'):
        sc = parse_color(panel['stroke'])
        sw = int(panel.get('stroke_width', 2))
        if radius > 0:
            od.rounded_rectangle([x0, y0, x1, y1], radius=radius, outline=(*sc, 255), width=sw)
        else:
            od.rectangle([x0, y0, x1, y1], outline=(*sc, 255), width=sw)
    return Image.alpha_composite(canvas, overlay)


def place_mark(canvas, mark, base_dir):
    """Place an official mark unaltered (aspect-ratio locked, never stretched; BRAND-4)."""
    p = Path(mark['path'])
    if not p.is_absolute():
        cand = base_dir / p
        p = cand if cand.is_file() else (ROOT / p)
    if not p.is_file():
        raise FileNotFoundError(f'mark file not found: {mark["path"]}')
    im = Image.open(p).convert('RGBA')
    mw = mark.get('max_width', im.width)
    mh = mark.get('max_height', im.height)
    scale = min(mw / im.width, mh / im.height)
    nw, nh = max(1, round(im.width * scale)), max(1, round(im.height * scale))
    if (nw, nh) != im.size:
        im = im.resize((nw, nh), Image.LANCZOS)
    x, y = int(round(mark['x'])), int(round(mark['y']))
    canvas.alpha_composite(im, (x, y))
    return dict(path=str(p), box=[x, y, x + nw, y + nh])


def draw_chart(canvas, draw, chart, manifest_rows):
    """Draw a data-accurate horizontal bar chart in code (LAY-19)."""
    ctype = chart.get('type', 'bars')
    if ctype != 'bars':
        raise ValueError(f'unsupported chart type in compose.py: {ctype} (use datagraphic.py for donut/route)')
    x0, y0, x1, y1 = [int(round(v)) for v in chart['box']]
    data = chart.get('data', [])
    if not data:
        return None
    bar_rgb = parse_color(chart.get('bar_color', '#0F766E'))
    track_rgb = parse_color(chart.get('track_color', '#E5E7EB'))
    text_rgb = parse_color(chart.get('text_color', '#111827'))
    max_val = float(chart.get('max_value') or max(float(d['value']) for d in data) or 1.0)
    font_size = int(chart.get('font_size', 18))
    font, _ = find_font(chart.get('font'), size=font_size)
    n = len(data)
    row_h = max(28, (y1 - y0) // n)
    label_w = int(chart.get('label_width', min(180, (x1 - x0) * 0.35)))
    val_w = int(chart.get('value_width', 72))
    track_x0 = x0 + label_w
    track_x1 = max(track_x0 + 20, x1 - val_w)
    bar_h = max(10, min(28, int(row_h * 0.48)))

    for i, item in enumerate(data):
        ry = y0 + i * row_h
        cy = ry + (row_h - bar_h) // 2
        label = str(item['label'])
        val = float(item['value'])
        val_txt = str(item.get('display', f'{val:g}'))
        frac = max(0.0, min(1.0, val / max_val))
        # Label text
        lb = draw.textbbox((x0, ry + (row_h - font_size) // 2), label, font=font)
        draw.text((x0, ry + (row_h - font_size) // 2), label, fill=(*text_rgb, 255), font=font)
        if chart.get('include_in_manifest', False):
            manifest_rows.append([label, [int(lb[0]), int(lb[1]), int(lb[2]), int(lb[3])], list(text_rgb)])
        # Track + accurate data bar
        draw.rectangle([track_x0, cy, track_x1, cy + bar_h], fill=(*track_rgb, 255))
        bw = round((track_x1 - track_x0) * frac)
        if bw > 0:
            draw.rectangle([track_x0, cy, track_x0 + bw, cy + bar_h], fill=(*bar_rgb, 255))
        # Value label
        vx = track_x1 + 10
        vb = draw.textbbox((vx, ry + (row_h - font_size) // 2), val_txt, font=font)
        draw.text((vx, ry + (row_h - font_size) // 2), val_txt, fill=(*text_rgb, 255), font=font)
        if chart.get('include_in_manifest', False):
            manifest_rows.append([val_txt, [int(vb[0]), int(vb[1]), int(vb[2]), int(vb[3])], list(text_rgb)])
    return dict(type=ctype, rows=n, max_value=max_val, box=[x0, y0, x1, y1])


def export_html(spec, out_html):
    w, h = int(spec['width']), int(spec['height'])
    bg = spec.get('background', '#FFFFFF')
    bg_css = f"background:{bg};" if isinstance(bg, str) else f"background:url('{html_lib.escape(bg['image'])}') center/cover no-repeat;"
    parts = [
        '<!doctype html><html lang="en"><head><meta charset="utf-8">',
        f'<style>*{{box-sizing:border-box;margin:0;padding:0}}body{{width:{w}px;height:{h}px;position:relative;overflow:hidden;{bg_css}font-family:system-ui,-apple-system,sans-serif}}</style>',
        '</head><body>',
    ]
    for p in spec.get('panels', []):
        x0, y0, x1, y1 = p['box']
        fill = p.get('fill', '#FFFFFF')
        op = p.get('opacity', 1.0)
        rad = p.get('radius', 0)
        parts.append(
            f'<div style="position:absolute;left:{x0}px;top:{y0}px;width:{x1 - x0}px;height:{y1 - y0}px;'
            f'background:{html_lib.escape(str(fill))};opacity:{op};border-radius:{rad}px;"></div>'
        )
    for t in spec.get('text', []):
        col = t.get('color', '#111827')
        align = t.get('align', 'left')
        mw = f"max-width:{t['max_width']}px;" if t.get('max_width') else ''
        fw = '700' if str(t.get('font', '')).lower() == 'bold' else '400'
        parts.append(
            f'<div style="position:absolute;left:{t["x"]}px;top:{t["y"]}px;font-size:{t.get("size", 24)}px;'
            f'font-weight:{fw};color:{html_lib.escape(str(col))};text-align:{align};{mw}line-height:{t.get("line_height", 1.25)};">'
            f'{html_lib.escape(t["text"])}</div>'
        )
    parts.append('</body></html>')
    Path(out_html).write_text('\n'.join(parts) + '\n', encoding='utf-8')


def compose_spec(spec, out_path, base_dir=None, html_out=None, allow_unsafe=False):
    base_dir = Path(base_dir) if base_dir else Path.cwd()
    w, h = int(spec['width']), int(spec['height'])
    safe = float(spec.get('safe_area_px', 0))
    bg = spec.get('background', '#FFFFFF')

    if isinstance(bg, dict) and bg.get('image'):
        img_path = Path(bg['image'])
        if not img_path.is_absolute():
            cand = base_dir / img_path
            img_path = cand if cand.is_file() else (ROOT / img_path)
        canvas = fit_cover(Image.open(img_path).convert('RGBA'), w, h)
    else:
        rgb = parse_color(bg, (255, 255, 255))
        canvas = Image.new('RGBA', (w, h), (*rgb, 255))

    for panel in spec.get('panels', []):
        canvas = draw_panel(canvas, panel)

    marks_placed = []
    for mark in spec.get('marks', []):
        marks_placed.append(place_mark(canvas, mark, base_dir))

    draw = ImageDraw.Draw(canvas)
    manifest_rows = []
    charts_drawn = []
    for chart in spec.get('charts', []):
        info = draw_chart(canvas, draw, chart, manifest_rows)
        if info:
            charts_drawn.append(info)

    unsafe_boxes = []
    for item in spec.get('text', []):
        txt = str(item['text'])
        size = int(item.get('size', 24))
        rgb = parse_color(item.get('color', '#111827'))
        align = item.get('align', 'left')
        lh = float(item.get('line_height', 1.25))
        font, _ = find_font(item.get('font'), size=size)
        lines = wrap_text(draw, txt, font, item.get('max_width'))
        y = float(item['y'])
        step = max(size, round(size * lh))
        for line in lines:
            if not line:
                y += step
                continue
            raw = draw.textbbox((0, 0), line, font=font)
            lw = raw[2] - raw[0]
            x = float(item['x'])
            if align == 'center':
                x -= lw / 2
            elif align == 'right':
                x -= lw
            # Compute actual rendered bounding box with small padding for clean contrast sampling
            bb = draw.textbbox((x, y), line, font=font)
            box = [max(0, math.floor(bb[0]) - 2), max(0, math.floor(bb[1]) - 2),
                   min(w, math.ceil(bb[2]) + 2), min(h, math.ceil(bb[3]) + 2)]
            draw.text((x, y), line, fill=(*rgb, 255), font=font)
            manifest_rows.append([line, box, list(rgb)])
            if safe > 0 and min(box[0], box[1], w - box[2], h - box[3]) < safe:
                unsafe_boxes.append(dict(text=line, box=box))
            y += step

    if unsafe_boxes and not allow_unsafe:
        raise ValueError(f'safe area violation (safe_area_px={safe}): {unsafe_boxes}')

    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert('RGB').save(out_path)

    manifest_path = out_path.with_name(out_path.stem + '-boxes.json')
    manifest_path.write_text(json.dumps(manifest_rows, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

    if html_out:
        export_html(spec, html_out)

    return dict(
        schema_version=2,
        status='OK',
        output=str(out_path),
        manifest=str(manifest_path),
        html=str(html_out) if html_out else None,
        size=[w, h],
        lines_rendered=len(manifest_rows),
        marks_placed=len(marks_placed),
        charts_drawn=len(charts_drawn),
        safe_area_px=safe,
        safe_area_ok=len(unsafe_boxes) == 0,
    )


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('spec', help='Path to composition spec JSON')
    ap.add_argument('--out', required=True, help='Output PNG path (also writes <stem>-boxes.json)')
    ap.add_argument('--html', help='Optional standalone HTML export path')
    ap.add_argument('--allow-unsafe', action='store_true', help='Permit text outside safe_area_px (still reported)')
    a = ap.parse_args(argv)
    spec_path = Path(a.spec)
    spec = json.loads(spec_path.read_text(encoding='utf-8'))
    res = compose_spec(spec, a.out, base_dir=spec_path.parent, html_out=a.html, allow_unsafe=a.allow_unsafe)
    print(json.dumps(res, indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())

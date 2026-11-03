#!/usr/bin/env python3
"""Zoomed crops for the anatomy pass (modules/character/, CHAR-9).

Usage:
  python3 tools/anatomy_crops.py IMG OUTDIR "label:x0,y0,x1,y1" ["label:..." ...] [--zoom 3]

Coordinates are pixels in IMG. Writes OUTDIR/<label>.png for each region (enlarged
--zoom times, Lanczos), OUTDIR/sheet.png (all crops labelled, plus a small overview
with the boxes drawn), and OUTDIR/anatomy-pass.md: one blank line per crop and check
(A1-A11) to fill with PASS/FAIL and what was seen. The tool does not judge anatomy;
it makes sure every region is looked at up close and recorded.
"""
import os, sys
from PIL import Image, ImageDraw

CHECKS = {
    "hand": ["A2 finger count", "A3 trace to shoulder (side?)", "A4 thumb side", "A5 grip", "A6 joints", "A7 merges/extras"],
    "face": ["A8 eyes match / gaze / teeth"],
    "animal": ["A9 eye, limb or fin count and joins"],
}

def kind(label):
    l = label.lower()
    for k in CHECKS:
        if k in l:
            return k
    return "hand" if any(w in l for w in ("arm", "limb", "wrist", "finger")) else None

def main(a):
    zoom = 3
    if "--zoom" in a:
        i = a.index("--zoom"); zoom = int(a[i + 1]); del a[i:i + 2]
    if len(a) < 3:
        sys.exit(__doc__)
    img, out, regions = a[0], a[1], a[2:]
    os.makedirs(out, exist_ok=True)
    im = Image.open(img).convert("RGB")
    crops, boxes = [], []
    for r in regions:
        label, xy = r.split(":", 1)
        box = tuple(int(float(v)) for v in xy.split(","))
        c = im.crop(box)
        c = c.resize((c.width * zoom, c.height * zoom), Image.LANCZOS)
        c.save(os.path.join(out, f"{label}.png"))
        crops.append((label, c)); boxes.append((label, box))
    ov = im.copy(); d = ImageDraw.Draw(ov)
    for label, b in boxes:
        d.rectangle(b, outline=(255, 0, 255), width=max(2, im.width // 300)); d.text((b[0] + 4, b[1] + 4), label, fill=(255, 0, 255))
    ov.thumbnail((480, 480))
    h = max([c.height for _, c in crops] + [ov.height]) + 24
    sheet = Image.new("RGB", (ov.width + sum(c.width for _, c in crops) + 10 * (len(crops) + 1), h), "white")
    sd = ImageDraw.Draw(sheet); x = 0
    sheet.paste(ov, (x, 24)); sd.text((x + 4, 4), "overview", fill="black"); x += ov.width + 10
    for label, c in crops:
        sheet.paste(c, (x, 24)); sd.text((x + 4, 4), f"{label} x{zoom}", fill="black"); x += c.width + 10
    sheet.save(os.path.join(out, "sheet.png"))
    lines = [f"# Anatomy pass: {os.path.basename(img)}", "", "A1 hand count per person: ___ (PASS/FAIL)", ""]
    for label, b in boxes:
        k = kind(label)
        for chk in CHECKS.get(k, ["A1-A11 (name the checks that apply)"]):
            lines.append(f"- {label}.png {b} | {chk} | PASS/FAIL | ")
    lines += ["", "A10 clothing symmetry: ___", "A11 ground and shadow: ___", "", "Any FAIL = blocker. Re-run every line after each image edit."]
    open(os.path.join(out, "anatomy-pass.md"), "w").write("\n".join(lines) + "\n")
    print(f"{len(crops)} crops -> {out}/ (sheet.png, anatomy-pass.md)")

if __name__ == "__main__":
    main(sys.argv[1:])

"""Labelled overview of every side-by-side in this folder. python3 src/make_overview.py -> overview.jpg"""
import os, sys
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.common import font
HERE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ITEMS = [("illustration", "Illustration", "Picture-book spread: one light, the pair lead, nothing added"),
         ("technical-drawing", "Technical drawing", "Exploded view: true isometric, 4:2:1 lines, balloons"),
         ("web-landing", "Web landing page", "Pottery studio: real facts in the first screen, invented reviews out"),
         ("app-flow", "App UX flow", "Bus ticket: 48 px targets, readable by the driver"),
         ("poster", "Poster", "Seed swap: what and when from across the path"),
         ("product-3d", "3D product shot", "Perfume: glass drawn by rim light, model-qa clean"),
         ("data-chart", "Data chart", "Mauna Loa CO\u2082: one line, a title that says the finding")]
CW, PAD, TOP, HEAD = 900, 40, 150, 80
cols = 2
thumbs = []
for folder, label, sub in ITEMS:
    t = Image.open(os.path.join(HERE, folder, "side-by-side.jpg")).convert("RGB")
    thumbs.append(t.resize((CW, round(t.height * CW / t.width)), Image.LANCZOS))
rows = [list(range(i, min(i + cols, len(ITEMS)))) for i in range(0, len(ITEMS), cols)]
row_h = [max(thumbs[i].height for i in r) for r in rows]
W = PAD + cols * (CW + PAD); H = TOP + sum(h + HEAD + PAD for h in row_h)
INK, SOFT, BG = (29, 27, 24), (91, 85, 76), (246, 244, 239)
im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
d.text((PAD, 40), "Same rules, seven kinds of work: before and after", font=font("humanist-sans/sourcesans3/SourceSans3[wght].ttf", 46, 600), fill=INK)
d.text((PAD, 98), "Each pair: a plausible first try, a rule-cited critique, every fix applied. Self-judged by the agent that made them.", font=font("humanist-sans/sourcesans3/SourceSans3[wght].ttf", 24, 400), fill=SOFT)
fl = font("humanist-sans/sourcesans3/SourceSans3[wght].ttf", 30, 600); fs = font("humanist-sans/sourcesans3/SourceSans3[wght].ttf", 21, 400)
y = TOP
for r, h in zip(rows, row_h):
    for c, n in enumerate(r):
        folder, label, sub = ITEMS[n]; x = PAD + c * (CW + PAD)
        d.text((x, y), f"{n + 1}. {label}", font=fl, fill=INK)
        d.text((x, y + 40), sub, font=fs, fill=SOFT)
        im.paste(thumbs[n], (x, y + HEAD))
        d.rectangle((x, y + HEAD, x + CW - 1, y + HEAD + thumbs[n].height - 1), outline=(217, 210, 197))
    y += h + HEAD + PAD
im.save(os.path.join(HERE, "overview.jpg"), quality=88); print(im.size)

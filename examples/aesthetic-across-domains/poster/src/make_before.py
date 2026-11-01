"""Before: the type-only poster a bot typically makes in code: centred Bebas Neue, gradient, drop shadows."""
import sys, textwrap
sys.path.insert(0, "../../src")
from common import font
from PIL import Image, ImageDraw, ImageFilter
W, H = 1754, 2480  # A3 portrait at 150 dpi
img = Image.new("RGB", (W, H))
top, bot = (46, 125, 50), (249, 212, 35)
for y in range(H):
    t = y / H
    ImageDraw.Draw(img).line([(0, y), (W, y)], fill=tuple(round(a + (b - a) * t) for a, b in zip(top, bot)))
B = "condensed-poster/bebasneue/BebasNeue-Regular.ttf"
lines = [("JOIN US FOR OUR ANNUAL", 96), ("SEED SWAP!", 330), ("HOLLIN LANE ALLOTMENTS", 120),
         ("SATURDAY 14TH MARCH 2027", 120), ("10AM - 1PM", 120)]
body = ("BRING YOUR SPARE SEEDS AND SWAP WITH FELLOW GARDENERS! ENVELOPES PROVIDED. "
        "TEA & CAKE IN THE HUT. FREE ENTRY. ALL WELCOME! DON'T MISS OUT!")
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0)); txt = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ds, dt = ImageDraw.Draw(shadow), ImageDraw.Draw(txt)
y = 330
boxes = []
for s, size in lines:
    f = font(B, size); w = dt.textlength(s, font=f)
    ds.text(((W - w) / 2 + 8, y + 8), s, font=f, fill=(0, 0, 0, 150))
    dt.text(((W - w) / 2, y), s, font=f, fill=(255, 255, 255, 255))
    boxes.append((s, ((W - w) / 2, y, (W + w) / 2, y + size)))
    y += size * 1.25 + (60 if size > 200 else 10)
f = font(B, 52)
y += 60
for s in textwrap.wrap(body, 44):
    w = dt.textlength(s, font=f)
    ds.text(((W - w) / 2 + 4, y + 4), s, font=f, fill=(0, 0, 0, 150))
    dt.text(((W - w) / 2, y), s, font=f, fill=(255, 255, 255, 255))
    boxes.append((s, ((W - w) / 2, y, (W + w) / 2, y + 52)))
    y += 70
img.save("before-ground.png")  # ground without text, for the contrast check (deleted after measuring)
img = img.convert("RGBA"); img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(6))); img.alpha_composite(txt)
img.convert("RGB").save("../before.png")
import json; json.dump(boxes, open("before-boxes.json", "w"))

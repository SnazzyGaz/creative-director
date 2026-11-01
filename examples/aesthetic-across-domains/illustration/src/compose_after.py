"""After: text set in code in Fredoka, flush left in the plain sky on the left page, clear of the fold."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))
from common import font, text_contrast
from PIL import Image, ImageDraw
here = os.path.dirname(__file__)
art = Image.open(os.path.join(here, "after-art-r4.jpg")).convert("RGB").resize((2560, 1440), Image.LANCZOS)
lines = ["Every evening,", "Nell and Biscuit walked", "the long way home,", "past the harbour wall."]
f = font("childrens-playful/fredoka/Fredoka[wdth,wght].ttf", 66, 500)
ink = (14, 22, 40)          # deep slate navy, from the sky's own hue family
x0, y0, lead = 190, 330, 92  # left margin 7.4% of width; leading 1.39
d = ImageDraw.Draw(art)
boxes = []
for i, t in enumerate(lines):
    w = d.textlength(t, font=f); boxes.append((x0, y0 + i * lead, int(x0 + w), y0 + i * lead + 80))
res = [text_contrast(art, b, ink) for b in boxes]
for b, r in zip(boxes, res):
    print("box", b, "mean %.2f:1  harsh %.2f:1" % r)
print("rightmost text x:", max(b[2] for b in boxes), "fold zone starts at", int(2560 * 0.44))
for i, t in enumerate(lines):
    d.text((x0, y0 + i * lead), t, font=f, fill=ink)
art.save(os.path.join(here, "..", "after.jpg"), quality=90)

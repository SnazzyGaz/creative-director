"""Set the type over the two renders. python3 compose.py -> ../before.jpg, ../after.jpg, ../src/*-boxes.json
before: Great Vibes title + Playfair Display, centred, pale grey and gold over a light ground.
after:  Bodoni Moda (high-contrast didone, catalogued for luxury and perfume) for the name,
        Josefin Sans (thin geometric caps, catalogued for art-deco and fashion labels) for the small lines,
        set in the empty dark top third, warm off-white and one amber accent taken from the liquid."""
import json, os, sys
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from src.common import font, text_contrast
HERE = os.path.dirname(os.path.abspath(__file__)); UP = os.path.join(HERE, "..")

def centred(d, y, txt, f, fill, W, tracking=0, boxes=None, name=None, ground=None):
    if tracking:
        widths = [d.textlength(c, font=f) for c in txt]; w = sum(widths) + tracking * (len(txt) - 1)
    else:
        w = d.textlength(txt, font=f)
    x = (W - w) / 2
    bb = d.textbbox((x, y), txt, font=f)
    if tracking:
        box = (int(x), bb[1], int(x + w), bb[3])
    else:
        box = bb
    if boxes is not None:
        boxes[name] = {"box": list(map(int, box)), "rgb": fill, "contrast_mean_worst": [round(v, 2) for v in text_contrast(ground, box, fill)]}
    if tracking:
        cx = x
        for c, cw in zip(txt, widths):
            d.text((cx, y), c, font=f, fill=fill); cx += cw + tracking
    else:
        d.text((x, y), txt, font=f, fill=fill)
    return box

def before():
    im = Image.open(os.path.join(UP, "render-before.png")).convert("RGB"); g = im.copy(); W = im.width
    d = ImageDraw.Draw(im); b = {}
    centred(d, 70, "Saltmarsh No. 2", font("romance-script/greatvibes/GreatVibes-Regular.ttf", 92), (255, 255, 255), W, boxes=b, name="title", ground=g)
    centred(d, 205, "LUXURY EAU DE PARFUM", font("luxury-didone/playfairdisplay/PlayfairDisplay[wght].ttf", 26, 400), (201, 170, 98), W, tracking=6, boxes=b, name="kicker", ground=g)
    centred(d, 1130, "The scent of the sea, captured forever.", font("luxury-didone/playfairdisplay/PlayfairDisplay-Italic[wght].ttf", 34, 400), (235, 235, 235), W, boxes=b, name="tagline", ground=g)
    centred(d, 1190, "Sea air  |  Vetiver  |  Smoked cedar  |  50ml", font("luxury-didone/playfairdisplay/PlayfairDisplay[wght].ttf", 24, 400), (201, 170, 98), W, boxes=b, name="notes", ground=g)
    im.save(os.path.join(UP, "before.jpg"), quality=92); json.dump(b, open(os.path.join(HERE, "before-boxes.json"), "w"), indent=1)

def after():
    im = Image.open(os.path.join(UP, "render-after.png")).convert("RGB"); g = im.copy(); W = im.width
    d = ImageDraw.Draw(im); b = {}
    ink, amber = (239, 230, 216), (222, 165, 98)
    centred(d, 92, "EAU DE PARFUM  ·  50 ML", font("art-deco-display/josefinsans/JosefinSans[wght].ttf", 22, 500), amber, W, tracking=7, boxes=b, name="kicker", ground=g)
    centred(d, 140, "Saltmarsh", font("luxury-didone/bodonimoda/BodoniModa[opsz,wght].ttf", 128, 500), ink, W, boxes=b, name="title", ground=g)
    centred(d, 300, "No. 2", font("luxury-didone/bodonimoda/BodoniModa-Italic[opsz,wght].ttf", 54, 400), ink, W, boxes=b, name="number", ground=g)
    centred(d, 412, "SEA AIR   ·   VETIVER   ·   SMOKED CEDAR", font("art-deco-display/josefinsans/JosefinSans[wght].ttf", 21, 500), (200, 190, 176), W, tracking=5, boxes=b, name="notes", ground=g)
    im.save(os.path.join(UP, "after.jpg"), quality=92); json.dump(b, open(os.path.join(HERE, "after-boxes.json"), "w"), indent=1)

before(); after()

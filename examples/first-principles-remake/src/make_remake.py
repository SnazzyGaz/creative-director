"""The chosen concept (B, Bring / Take) built at A3. Type only; two inks on paper; flush left on the 22 mm margin.
The date and weekday agree: Saturday 13 March 2027 (checked, FP-3)."""
import json
from PIL import Image, ImageDraw
from fp import *

PAPER, INK, ACC = (238, 228, 206), (33, 43, 30), (163, 60, 33)
MEAS = W - 2 * M
SPLIT = 1470
im = Image.new("RGB", (W, H), PAPER); d = ImageDraw.Draw(im)
d.rectangle((0, SPLIT, W, H), fill=INK)
ground = im.copy()                     # for the contrast check, before any text
boxes = []

def fit(text, max_w, **ax):
    s = 200
    while d.textlength(text, font=vfont(BRIC, s + 4, **ax)) <= max_w: s += 4
    return vfont(BRIC, s, **ax)

def put(xy, s, f, fill, anchor="ls"):
    d.text(xy, s, font=f, fill=fill, anchor=anchor)
    b = d.textbbox(xy, s, font=f, anchor=anchor); boxes.append((s, b, fill)); return b

HEAD = dict(wght=800, wdth=75, opsz=96)
SUB = dict(wght=600, wdth=82, opsz=96)
# top: what and who
put((M, M + 118), "Seed swap", vfont(BRIC, 150, wght=700, wdth=90, opsz=96), INK)
put((W - M, M + 118), "Hollin Lane Allotments", vfont(HANK, 56, wght=600), INK, anchor="rs")
d.line((M, M + 160, W - M, M + 160), fill=INK, width=5)
# far read, top half: the first half of the swap. Bring and Take share one size (the swap is symmetrical).
fb = fit("Bring", MEAS * 0.86, **HEAD)
put((M - 10, 880), "Bring", fb, INK)
put((M, 1060), "spare seeds", vfont(BRIC, 172, **SUB), INK)
# second level: when
put((M, 1290), "Sat 13 March 2027", vfont(BRIC, 172, wght=700, wdth=75, opsz=96), ACC)
put((M, 1376), "10:00 to 13:00, in the hut", vfont(HANK, 60, wght=500), INK)
# far read, bottom half: the other half, inverted
put((M - 10, SPLIT + 560), "Take", fb, PAPER)
put((M, SPLIT + 740), "some home", vfont(BRIC, 172, **SUB), PAPER)
# near read
fn = vfont(HANK, 52, wght=400)
put((M, H - M), "Envelopes provided. Free. Tea in the hut.", fn, PAPER)
im.save("../remake.png")
ground.save("/tmp/fp-remake-ground.png")
json.dump(boxes, open("remake-boxes.json", "w"))
for s, b, f in boxes: print(f"{s!r:45} {b}")

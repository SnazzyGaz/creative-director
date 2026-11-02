"""After: Antonio for the far read, Cabin for the near read, flush left on a 12-column grid, two inks."""
import sys, json
sys.path.insert(0, "../../src")
from common import font
from PIL import Image, ImageDraw
W, H = 1754, 2480
PAPER, INK, RED = (241, 236, 223), (28, 56, 41), (176, 58, 38)
img = Image.new("RGB", (W, H), PAPER); d = ImageDraw.Draw(img)
M = 132                     # outer margin: 22 mm at A3
col = (W - 2 * M) / 12
A = "condensed-poster/antonio/Antonio[wght].ttf"; C = "humanist-sans/cabin/Cabin[wdth,wght].ttf"
boxes = []
def put(xy, s, f, fill, anchor="ls"):
    d.text(xy, s, font=f, fill=fill, anchor=anchor); boxes.append((s, d.textbbox(xy, s, font=f, anchor=anchor), fill))
# top line: who
put((M, M + 52), "Hollin Lane Allotments", font(C, 54, 600), INK)
d.line([(M, M + 92), (W - M, M + 92)], fill=INK, width=4)
# far read: SEED / SWAP, caps set to fill the measure
fh = font(A, 760, 700)
put((M - 14, 1010), "SEED", fh, INK)
put((M - 14, 1700), "SWAP", fh, INK)
# date block on columns 1-12, accent for the when
fd = font(A, 210, 700)
put((M - 4, 1990), "Sat 13 March 2027", fd, RED)
put((M, 2090), "10:00 to 13:00, in the hut", font(C, 72, 500), INK)
# near read: one block, columns 1-8
fb = font(C, 50, 400)
y = 2215
for s in ["Bring spare seeds and take some home.", "Envelopes provided. Free. Tea in the hut."]:
    put((M, y), s, fb, INK); y += 70
img.save("../after.png")
json.dump([(s, b, f) for s, b, f in boxes], open("after-boxes.json", "w"))
print(boxes)

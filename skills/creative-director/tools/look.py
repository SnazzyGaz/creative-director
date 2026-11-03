"""Five look tests from core/critique-loop.md as one contact sheet, plus value stats.
Usage: python3 look.py IMAGE OUT_SHEET.png"""
import sys
import numpy as np
from PIL import Image, ImageFilter, ImageOps, ImageDraw
src = Image.open(sys.argv[1]).convert('RGB')
W = 512
im = src.resize((W, int(src.height * W / src.width)))
H = im.height
def lum(img):  # Rec.709 luminance on linearised sRGB, returned as perceptual-ish 8-bit
    a = np.asarray(img).astype(float) / 255
    lin = np.where(a <= 0.04045, a / 12.92, ((a + 0.055) / 1.055) ** 2.4)
    Y = lin @ [0.2126, 0.7152, 0.0722]
    L = np.where(Y > 0.008856, 116 * np.cbrt(Y) - 16, 903.3 * Y)  # CIE L*
    return Image.fromarray((L * 2.55).clip(0, 255).astype('uint8')), L
grey, L = lum(im)
blur = im.filter(ImageFilter.GaussianBlur(8))
thumb = im.resize((180, int(H * 180 / W))).resize((W, H), Image.NEAREST)
flip = ImageOps.mirror(im)
post = grey.quantize(4).convert('RGB')
# edges: 4 strips (top, bottom, left, right) at 12%
e = int(0.12 * H)
edges = Image.new('RGB', (W, H), 'white')
edges.paste(im.crop((0, 0, W, e)), (0, 0)); edges.paste(im.crop((0, H - e, W, H)), (0, e + 4))
ew = int(0.12 * W)
edges.paste(im.crop((0, 0, ew, H)).resize((ew, H - 2 * e - 8)), (0, 2 * e + 8))
edges.paste(im.crop((W - ew, 0, W, H)).resize((ew, H - 2 * e - 8)), (ew + 4, 2 * e + 8))
tiles = [('original', im), ('blur 8px', blur), ('thumbnail 180px', thumb), ('flip', flip),
         ('greyscale (L*)', grey.convert('RGB')), ('posterised 4 values', post), ('edges/crops', edges)]
cols = 4; rows = 2
sheet = Image.new('RGB', (cols * (W + 10), rows * (H + 30)), 'white')
d = ImageDraw.Draw(sheet)
for i, (name, t) in enumerate(tiles):
    x, y = (i % cols) * (W + 10), (i // cols) * (H + 30)
    sheet.paste(t, (x, y + 22)); d.text((x + 4, y + 4), name, fill='black')
# stats tile
x, y = 3 * (W + 10), H + 30
hist = np.histogram(L, bins=10, range=(0, 100))[0] / L.size
d.text((x + 4, y + 4), 'L* histogram (0-100, 10 bins)', fill='black')
for i, h in enumerate(hist):
    d.rectangle([x + 10 + i * 48, y + 22 + H - int(h * H * 2.5), x + 50 + i * 48, y + 22 + H], fill='grey')
sheet.save(sys.argv[2])
# blur "what leads": local contrast of blurred luminance, 4x4 grid
bl = np.asarray(lum(blur)[0]).astype(float)
gy, gx = np.gradient(bl)
mag = np.hypot(gx, gy)
g = 4
cells = [[mag[r*H//g:(r+1)*H//g, c*W//g:(c+1)*W//g].mean() for c in range(g)] for r in range(g)]
print('L* mean %.1f  p5 %.1f  p50 %.1f  p95 %.1f' % (L.mean(), *np.percentile(L, [5, 50, 95])))
print('L* hist %:', ' '.join('%d' % round(100 * h) for h in hist))
print('blurred-contrast grid (rows top->bottom):')
for r in cells: print('  ' + ' '.join('%5.1f' % v for v in r))

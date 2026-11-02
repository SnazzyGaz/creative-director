"""COMP-2 / CORE-11 balance check: where is the picture's centre of visual "mass"?

Method (paraphrased): each pixel gets a weight from how far it stands out from the
background (lightness difference plus a smaller share of chroma). The weighted centroid
is compared with the geometric centre of the frame. This is the "deviation of the centre
of mass" (DCM) idea that Hübner & Fillinger (2016) found tracked people's balance ratings
of simple pictures, after Arnheim and Poore's steelyard. It is a crude model: faces, text,
gaze and meaning add weight that pixels cannot see (COMP-3), so read it as a prompt.

Usage: python3 balance.py IMAGE [--bg R,G,B] [--sheet OUT.png]
Prints: centroid offset from centre (dx, dy as % of the half-width and half-height;
+dx = right, +dy = down), DCM (0 = centred, 100 = at an edge), left/right and top/bottom
weight ratios, and a reading. Always exits 0: there is no PASS or FAIL, because a
strongly off-centre picture can be right (tension on purpose, COMP-12).
Reading bands (self-chosen, not from a study): DCM < 10 centred, 10-25 off-centre,
> 25 strongly off-centre - say whether that is intended.
"""
import sys, argparse
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

def srgb_to_lab(a):
    a = a / 255.0
    lin = np.where(a <= 0.04045, a / 12.92, ((a + 0.055) / 1.055) ** 2.4)
    M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
    xyz = lin @ M.T / np.array([0.95047, 1.0, 1.08883])
    f = np.where(xyz > 216 / 24389, np.cbrt(xyz), (24389 / 27 * xyz + 16) / 116)
    L = 116 * f[..., 1] - 16
    A = 500 * (f[..., 0] - f[..., 1]); B = 200 * (f[..., 1] - f[..., 2])
    return L, A, B

def analyse(path, bg=None, sheet=None):
    im = Image.open(path).convert('RGB')
    W0 = 400; im = im.resize((W0, max(1, round(im.height * W0 / im.width))), Image.LANCZOS)
    im = im.filter(ImageFilter.GaussianBlur(2))  # squint: weigh masses, not specks
    a = np.asarray(im).astype(float); H, W = a.shape[:2]
    L, A, B = srgb_to_lab(a); C = np.hypot(A, B)
    if bg is None:  # modal colour of the outer 2% frame
        e = max(2, int(0.02 * min(H, W)))
        border = np.concatenate([a[:e].reshape(-1, 3), a[-e:].reshape(-1, 3), a[:, :e].reshape(-1, 3), a[:, -e:].reshape(-1, 3)])
        q = (border // 16).astype(int); keys, cnt = np.unique(q, axis=0, return_counts=True)
        bg = keys[cnt.argmax()] * 16 + 8
    bL, bA, bB = srgb_to_lab(np.array(bg, float).reshape(1, 1, 3))
    w = np.abs(L - bL[0, 0]) + 0.5 * np.hypot(A - bA[0, 0], B - bB[0, 0])
    w = np.where(w < 6, 0, w)  # ignore near-background noise
    tot = w.sum()
    if tot == 0:
        print('No content found against the background.'); return None
    ys, xs = np.mgrid[0:H, 0:W]
    cx = (w * (xs + 0.5)).sum() / tot; cy = (w * (ys + 0.5)).sum() / tot
    dx = (cx - W / 2) / (W / 2) * 100; dy = (cy - H / 2) / (H / 2) * 100
    dcm = float(np.hypot(dx, dy))
    left = w[:, :W // 2].sum(); right = w[:, W - W // 2:].sum()
    top = w[:H // 2].sum(); bot = w[H - H // 2:].sum()
    lr = right / left if left else float('inf'); tb = bot / top if top else float('inf')
    reading = 'centred' if dcm < 10 else ('off-centre' if dcm <= 25 else 'strongly off-centre - say whether that is intended')
    print(f'centroid offset: dx {dx:+.1f}% (+ = right), dy {dy:+.1f}% (+ = down) of the half-frame')
    print(f'DCM: {dcm:.1f}  ->  {reading}')
    print(f'weight right/left: {lr:.2f}   bottom/top: {tb:.2f}')
    print('Next: mirror-flip the image (look.py) and ask if it still feels settled; then weigh faces, text and gaze by eye (COMP-3).')
    if sheet:
        hm = (w / w.max() * 255).astype('uint8')
        out = Image.merge('RGB', [Image.fromarray(hm)] * 3).convert('RGB')
        out = Image.blend(im, out, 0.6); d = ImageDraw.Draw(out)
        d.line([(W / 2, 0), (W / 2, H)], fill=(0, 160, 255), width=1)
        d.line([(0, H / 2), (W, H / 2)], fill=(0, 160, 255), width=1)
        r = 6; d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 40, 40), width=3)
        d.line([(W / 2, H / 2), (cx, cy)], fill=(255, 40, 40), width=2)
        out.save(sheet)
    return dict(dx=dx, dy=dy, dcm=dcm, lr=lr, tb=tb)

if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('image'); p.add_argument('--bg'); p.add_argument('--sheet')
    o = p.parse_args()
    bg = tuple(int(v) for v in o.bg.split(',')) if o.bg else None
    analyse(o.image, bg, o.sheet)

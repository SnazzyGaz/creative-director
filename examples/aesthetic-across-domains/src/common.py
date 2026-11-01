"""Shared helpers for examples/aesthetic-across-domains/ (Pillow + numpy).

font(rel, size, wght=None)    load a font from the repo's fonts/ library, optionally setting the weight axis
text_contrast(img, box, rgb)  WCAG ratio of a text colour against the mean and the most similar pixel in a box
chroma_stats(img)             mean and spread of LCh chroma, and the share of pixels above C*=40
side_by_side(a, b, out, ...)  labelled before/after sheet
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
F = lambda *p: os.path.join(REPO, "fonts", *p)

def font(rel, size, wght=None):
    f = ImageFont.truetype(F(rel) if not rel.startswith("/") else rel, size)
    if wght is not None:
        try:
            axes = f.get_variation_axes()
            vals = []
            for a in axes:
                name = a.get("name", b"")
                name = name.decode() if isinstance(name, bytes) else name
                vals.append(wght if name.lower().startswith("weight") else a.get("default", a["minimum"]))
            f.set_variation_by_axes(vals)
        except Exception:
            pass
    return f

def _lin(c):
    c = c / 255.0
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)

def rel_lum(rgb):
    a = _lin(np.asarray(rgb, dtype=float))
    return a[..., 0] * 0.2126 + a[..., 1] * 0.7152 + a[..., 2] * 0.0722

def ratio(l1, l2):
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)

def text_contrast(img, box, rgb):
    """Contrast of text colour rgb against the ground inside box (x0,y0,x1,y1) of img (before the text is drawn).
    Returns (ratio on the mean ground, ratio against the closest-luminance pixel: a harsh check)."""
    a = np.asarray(img.convert("RGB").crop(box), dtype=float).reshape(-1, 3)
    L = rel_lum(a)
    lt = float(rel_lum(np.array(rgb, dtype=float)))
    mean = float(rel_lum(a.mean(0)))
    worst = L[np.argmin(np.abs(L - lt))]
    return ratio(lt, mean), ratio(lt, float(worst))

def chroma_stats(img):
    a = np.asarray(img.convert("RGB").resize((320, int(320 * img.height / img.width))), dtype=float).reshape(-1, 3)
    lin = _lin(a)
    M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
    xyz = lin @ M.T / np.array([0.9505, 1.0, 1.089])
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    A = 500 * (f[:, 0] - f[:, 1]); B = 200 * (f[:, 1] - f[:, 2])
    C = np.hypot(A, B)
    return {"mean_C": round(float(C.mean()), 1), "p90_C": round(float(np.percentile(C, 90)), 1), "share_C_over_40": round(float((C > 40).mean()), 3)}

def side_by_side(a, b, out, la="Before", lb="After", sub_a="", sub_b="", width=900, bg=(246, 244, 239)):
    ims = []
    for p in (a, b):
        im = Image.open(p).convert("RGB") if isinstance(p, str) else p.convert("RGB")
        ims.append(im.resize((width, round(im.height * width / im.width)), Image.LANCZOS))
    h = max(i.height for i in ims)
    top, gap, pad = 86, 36, 36
    s = Image.new("RGB", (pad * 2 + width * 2 + gap, top + h + pad), bg)
    d = ImageDraw.Draw(s)
    fh = font("grotesk-neutral/publicsans/PublicSans[wght].ttf", 30, 700)
    fs = font("grotesk-neutral/publicsans/PublicSans[wght].ttf", 19, 400)
    for k, (im, l, sb) in enumerate(zip(ims, (la, lb), (sub_a, sub_b))):
        x = pad + k * (width + gap)
        d.text((x, 16), l, fill=(28, 27, 25), font=fh)
        d.text((x, 54), sb, fill=(88, 84, 77), font=fs)
        s.paste(im, (x, top))
        d.rectangle((x - 1, top - 1, x + width, top + im.height), outline=(200, 195, 186))
    s.save(out, quality=90)
    return out

def static_font(rel, wght, out_dir="/tmp/aad-static-fonts", **axes):
    """Instance a variable font from fonts/ at a weight (and other axes) into a static TTF, for tools
    such as matplotlib that only read a variable font's default instance. Returns the file path."""
    from fontTools.ttLib import TTFont
    from fontTools.varLib import instancer
    os.makedirs(out_dir, exist_ok=True)
    tag = "-".join(f"{k}{v}" for k, v in sorted(dict(wght=wght, **axes).items()))
    out = os.path.join(out_dir, os.path.basename(rel).split("[")[0].replace(".ttf", "") + f"-{tag}.ttf")
    if not os.path.exists(out):
        f = TTFont(F(rel))
        have = {a.axisTag for a in f["fvar"].axes}
        loc = {k: v for k, v in dict(wght=wght, **axes).items() if k in have}
        inst = instancer.instantiateVariableFont(f, loc, updateFontNames=False)
        # give each instance a unique family name so matplotlib keeps them apart
        name = inst["name"]
        fam = name.getDebugName(1) + f" {tag}"
        for rec in name.names:
            if rec.nameID in (1, 4, 16):
                rec.string = fam
            if rec.nameID in (2, 17):
                rec.string = "Regular"
        inst.save(out)
    return out

def stacked(a, b, out, la="Before", lb="After", sub_a="", sub_b="", width=1500, captions=None, bg=(246, 244, 239)):
    """Before above after, for wide strips (e.g. three phone screens). captions: labels placed above
    equal-width columns of each strip."""
    ims = []
    for p in (a, b):
        im = Image.open(p).convert("RGB") if isinstance(p, str) else p.convert("RGB")
        ims.append(im.resize((width, round(im.height * width / im.width)), Image.LANCZOS))
    pad, head, cap = 36, 84, (34 if captions else 0)
    H = pad + sum(head + cap + i.height + pad for i in ims)
    s = Image.new("RGB", (width + 2 * pad, H), bg)
    d = ImageDraw.Draw(s)
    fh = font("grotesk-neutral/publicsans/PublicSans[wght].ttf", 30, 700)
    fs = font("grotesk-neutral/publicsans/PublicSans[wght].ttf", 19, 400)
    fc = font("grotesk-neutral/publicsans/PublicSans[wght].ttf", 18, 600)
    y = pad - 16
    for im, l, sb in zip(ims, (la, lb), (sub_a, sub_b)):
        d.text((pad, y + 16), l, fill=(28, 27, 25), font=fh)
        d.text((pad, y + 54), sb, fill=(88, 84, 77), font=fs)
        y += head
        if captions:
            n = len(captions)
            for k, c in enumerate(captions):
                d.text((pad + k * width / n + 4, y + 4), c, fill=(60, 57, 52), font=fc)
            y += cap
        s.paste(im, (pad, y))
        d.rectangle((pad - 1, y - 1, pad + width, y + im.height), outline=(200, 195, 186))
        y += im.height + pad
    s.save(out, quality=90)
    return out

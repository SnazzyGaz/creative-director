"""Shared helpers for the first-principles remake example (Pillow). Fonts come from the repo's fonts/ library."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "aesthetic-across-domains", "src"))
from common import font as _font, F, text_contrast, side_by_side  # noqa: F401
from PIL import ImageFont

def vfont(rel, size, **axes):
    """Variable font with named axes, e.g. vfont(BRIC, 400, wght=800, wdth=75, opsz=96)."""
    f = ImageFont.truetype(F(rel), size)
    vals = []
    for a in f.get_variation_axes():
        n = a.get("name", b""); n = (n.decode() if isinstance(n, bytes) else n).lower()
        key = {"weight": "wght", "width": "wdth", "optical size": "opsz"}.get(n, n)
        vals.append(axes.get(key, a.get("default", a["minimum"])))
    f.set_variation_by_axes(vals)
    return f

font = _font
BRIC = "grotesk-neutral/bricolagegrotesque/BricolageGrotesque[opsz,wdth,wght].ttf"
HANK = "grotesk-neutral/hankengrotesk/HankenGrotesk[wght].ttf"
ALFA = "nautical-vintage/alfaslabone/AlfaSlabOne-Regular.ttf"
ZILLA = "western-slab/zillaslab/ZillaSlab-Regular.ttf"
ZILLA_B = "western-slab/zillaslab/ZillaSlab-SemiBold.ttf"
JOST = "geometric-sans/jost/Jost[wght].ttf"
LIT = "editorial-serif/literata/Literata[opsz,wght].ttf"
W, H = 1754, 2480          # A3 portrait at 150 dpi
M = 132                    # 22 mm margin

"""Before: typical bot layout. Text in a display face, centred over the sky, white with a drop shadow."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))
from common import font, text_contrast
from PIL import Image, ImageDraw, ImageFilter
here = os.path.dirname(__file__)
art = Image.open(os.path.join(here, "before-art.jpg")).convert("RGB").resize((2560, 1440), Image.LANCZOS)
line1 = "Every evening, Nell and Biscuit walked the long way home,"
line2 = "past the harbour wall."
f = font("childrens-playful/chewy/Chewy-Regular.ttf", 64)
d = ImageDraw.Draw(art)
W = art.width
boxes = []
for i, t in enumerate((line1, line2)):
    w = d.textlength(t, font=f); x = (W - w) / 2; y = 70 + i * 84
    boxes.append((int(x), int(y), int(x + w), int(y + 80)))
print("contrast white on ground (mean, harsh):", [tuple(round(v, 2) for v in text_contrast(art, b, (255, 255, 255))) for b in boxes])
sh = Image.new("RGBA", art.size, (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
for i, t in enumerate((line1, line2)):
    w = d.textlength(t, font=f); sd.text(((W - w) / 2 + 4, 70 + i * 84 + 4), t, font=f, fill=(0, 0, 0, 150))
art = Image.alpha_composite(art.convert("RGBA"), sh.filter(ImageFilter.GaussianBlur(3)))
d = ImageDraw.Draw(art)
for i, t in enumerate((line1, line2)):
    w = d.textlength(t, font=f); d.text(((W - w) / 2, 70 + i * 84), t, font=f, fill="white")
art.convert("RGB").save(os.path.join(here, "..", "before.jpg"), quality=90)

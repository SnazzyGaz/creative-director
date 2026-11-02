"""Side-by-side (light-touch fix vs remake), a three-up with the original, and the far read at 10%."""
from PIL import Image, ImageDraw
from fp import *

side_by_side("../light-touch.png", "../remake.png", "../side-by-side.jpg",
             la="Light-touch fix (keeps the old idea)", lb="First-principles remake (concept B)",
             sub_a="Same stacked layout, repaired: contrast, grid, three levels. Antonio + Cabin.",
             sub_b="Leads with what to do: bring seeds, take seeds. Bricolage Grotesque + Hanken Grotesk.")

def three_up(paths, labels, out, width, title_size=26, sub=None, bg=(246, 244, 239)):
    ims = [Image.open(p).convert("RGB") for p in paths]
    ims = [i.resize((width, round(i.height * width / i.width)), Image.LANCZOS) for i in ims]
    pad, gap, top = 30, 30, 70 if sub else 52
    s = Image.new("RGB", (2 * pad + 3 * width + 2 * gap, top + ims[0].height + pad), bg); d = ImageDraw.Draw(s)
    for k, (im, l) in enumerate(zip(ims, labels)):
        x = pad + k * (width + gap)
        d.text((x, 14), l, font=vfont(HANK, title_size, wght=700), fill=(28, 27, 25))
        if sub: d.text((x, 14 + title_size + 6), sub[k], font=vfont(HANK, 16, wght=400), fill=(88, 84, 77))
        s.paste(im, (x, top)); d.rectangle((x - 1, top - 1, x + width, top + im.height), outline=(200, 195, 186))
    s.save(out, quality=90)

P = ["../original.png", "../light-touch.png", "../remake.png"]
three_up(P, ["1  Original", "2  Light-touch fix", "3  Remake"], "../overview.jpg", 560,
         sub=["Bebas Neue on a gradient; invented copy", "same idea, repaired (AES-10, UI-6, LAY-7)", "rebuilt from the brief: bring / take"])
# far read: each sheet at 10% (A3 seen from a few metres), shown at that size without upscaling
small = [Image.open(p).convert("RGB").resize((175, 248), Image.LANCZOS) for p in P]
fv = Image.new("RGB", (3 * 175 + 4 * 24, 248 + 70), (246, 244, 239)); d = ImageDraw.Draw(fv)
for k, (im, l) in enumerate(zip(small, ["Original", "Light-touch", "Remake"])):
    x = 24 + k * (175 + 24); d.text((x, 16), l, font=vfont(HANK, 20, wght=700), fill=(28, 27, 25)); fv.paste(im, (x, 50))
fv.save("../far-view.png")

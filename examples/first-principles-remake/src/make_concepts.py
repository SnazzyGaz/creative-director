"""Three concept roughs from the brief (FP-5). Type and rules only, as the brief says "no pictures".
A: the seed packet. B: bring / take. C: the date on a calendar. Rendered at A3, shown as thumbnails."""
import calendar
from PIL import Image, ImageDraw
from fp import *

def concept_a():
    PAPER, INK, RED = (226, 208, 172), (46, 36, 26), (150, 52, 32)
    im = Image.new("RGB", (W, H), PAPER); d = ImageDraw.Draw(im)
    d.rectangle((M - 40, M - 40, W - M + 40, H - M + 40), outline=INK, width=14)       # packet edge
    d.line((M - 40, M + 260, W - M + 40, M + 260), fill=INK, width=6)                   # flap fold
    d.text((W / 2, M + 120), "HOLLIN LANE ALLOTMENTS", font=font(ZILLA_B, 64), fill=INK, anchor="mm")
    d.text((W / 2, M + 620), "Seed", font=font(ALFA, 400), fill=RED, anchor="mm")
    d.text((W / 2, M + 1000), "Swap", font=font(ALFA, 400), fill=RED, anchor="mm")
    rows = [("Sow", "14 March 2027, 10:00 to 13:00"), ("Where", "In the hut"), ("Bring", "Spare seeds"),
            ("Take", "Some home"), ("Packets", "Envelopes provided"), ("Price", "Free"), ("Also", "Tea in the hut")]
    y = M + 1330
    for k, v in rows:
        d.line((M + 20, y - 70, W - M - 20, y - 70), fill=INK, width=3)
        d.text((M + 40, y), k, font=font(ZILLA_B, 64), fill=INK, anchor="ls")
        d.text((M + 420, y), v, font=font(ZILLA, 64), fill=INK, anchor="ls")
        y += 128
    return im

def concept_b():
    PAPER, INK, ACC = (238, 228, 206), (33, 43, 30), (168, 64, 36)
    im = Image.new("RGB", (W, H), PAPER); d = ImageDraw.Draw(im)
    split = 1430
    d.rectangle((0, split, W, H), fill=INK)
    d.text((M, M + 50), "Seed swap  ·  Hollin Lane Allotments", font=vfont(HANK, 58, wght=600), fill=INK, anchor="ls")
    d.text((M - 20, 860), "Bring", font=vfont(BRIC, 640, wght=800, wdth=75, opsz=96), fill=INK, anchor="ls")
    d.text((M, 1060), "spare seeds", font=vfont(BRIC, 190, wght=600, wdth=80, opsz=96), fill=INK, anchor="ls")
    d.text((M, 1320), "14 March 2027 · 10:00 to 13:00", font=vfont(BRIC, 120, wght=700, wdth=75, opsz=96), fill=ACC, anchor="ls")
    d.text((M - 20, split + 640), "Take", font=vfont(BRIC, 640, wght=800, wdth=75, opsz=96), fill=PAPER, anchor="ls")
    d.text((M, split + 840), "some home", font=vfont(BRIC, 190, wght=600, wdth=80, opsz=96), fill=PAPER, anchor="ls")
    return im

def concept_c():
    PAPER, INK, ACC = (244, 241, 233), (30, 34, 48), (190, 70, 40)
    im = Image.new("RGB", (W, H), PAPER); d = ImageDraw.Draw(im)
    d.text((M, M + 200), "Seed swap", font=vfont(JOST, 260, wght=700), fill=INK, anchor="ls")
    d.text((M, M + 330), "Hollin Lane Allotments, in the hut", font=vfont(LIT, 64, wght=400, opsz=24), fill=INK, anchor="ls")
    d.text((M, 760), "March 2027", font=vfont(JOST, 110, wght=500), fill=INK, anchor="ls")
    cw = (W - 2 * M) / 7; y0 = 880
    for i, n in enumerate("MTWTFSS"):
        d.text((M + cw * i + cw / 2, y0), n, font=vfont(JOST, 60, wght=600), fill=INK, anchor="mm")
    for r, week in enumerate(calendar.Calendar(0).monthdayscalendar(2027, 3)):
        for c, day in enumerate(week):
            if not day: continue
            cx, cy = M + cw * c + cw / 2, y0 + 150 + r * 170
            if day == 14:
                d.ellipse((cx - 74, cy - 74, cx + 74, cy + 74), fill=ACC)
            d.text((cx, cy), str(day), font=vfont(JOST, 84, wght=700 if day == 14 else 400), fill=PAPER if day == 14 else INK, anchor="mm")
    y = 2050
    for s in ["10:00 to 13:00. Bring spare seeds and take some home.", "Envelopes provided. Free. Tea in the hut."]:
        d.text((M, y), s, font=vfont(LIT, 58, wght=400, opsz=24), fill=INK, anchor="ls"); y += 84
    return im

if __name__ == "__main__":
    ims = {"a-packet": concept_a(), "b-bring-take": concept_b(), "c-calendar": concept_c()}
    labels = {"a-packet": ("A  The seed packet", "the poster is the back of a packet; the label leads", "Alfa Slab One + Zilla Slab"),
              "b-bring-take": ("B  Bring / Take", "the two halves of the swap lead; recommended", "Bricolage Grotesque + Hanken Grotesk"),
              "c-calendar": ("C  The date", "a March calendar with the day marked leads", "Jost + Literata")}
    tw = 460; th = round(H * tw / W)
    sheet = Image.new("RGB", (36 + 3 * (tw + 36), 150 + th + 36), (246, 244, 239)); sd = ImageDraw.Draw(sheet)
    for k, (name, im) in enumerate(ims.items()):
        im.save(f"../concepts/{name}.png")
        x = 36 + k * (tw + 36)
        t = im.resize((tw, th), Image.LANCZOS)
        l1, l2, l3 = labels[name]
        sd.text((x, 22), l1, font=vfont(HANK, 30, wght=700), fill=(28, 27, 25))
        sd.text((x, 64), l2, font=vfont(HANK, 19, wght=400), fill=(70, 66, 60))
        sd.text((x, 92), l3, font=vfont(HANK, 19, wght=400), fill=(110, 104, 96))
        sheet.paste(t, (x, 150)); sd.rectangle((x - 1, 149, x + tw, 150 + th), outline=(200, 195, 186))
    sheet.save("../concepts/concepts.jpg", quality=90)

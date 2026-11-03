"""blind.py: shuffle the blind-test images into judging sheets and write the hidden key.

Run from the repo root once the 16 images exist (they are not in git):
  python3 examples/blind-test/blind.py --repeat --images DIR --sheets OUT_DIR --key KEY.json   (batch 1)

DIR holds B1-with.jpg, B1-without.jpg ... B8-without.jpg (made from briefs.json, one GenerateImage call each).
With --repeat (batch 1) each brief gives two sheets: the pair side by side, then the same pair with sides
swapped, so position bias shows up. Without it (batch 2) each brief gives one sheet, sides picked at random:
a human judge recognises the repeat, so it adds nothing for them; it still helps with model judges. Every image gets a random 4-letter ID; judges record the ID they prefer, never "left" or "right".
Sheets are shuffled and numbered S01.. (or from --start) so that a brief's two sheets are not next to each other.
The key (which ID is which condition, plus a random salt) goes to KEY.json, outside the repo. Its SHA-256 is
printed: commit that hash (KEY-SHA256.txt) before anyone judges, and publish the key only after.

A later batch gets its own key and continues the sheet numbers, without touching earlier sheets or keys:
  python3 blind.py --batch 2 --start 17 --avoid-key KEY.json --images DIR --sheets OUT_DIR --key KEY-2.json
"""
import argparse, hashlib, json, os, secrets, string, textwrap
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
FONT_PATHS = [os.path.join(ROOT, "fonts/grotesk-neutral/publicsans/PublicSans[wght].ttf"),
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
RNG = secrets.SystemRandom()

def font(size):
    for p in FONT_PATHS:
        if os.path.exists(p): return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def new_id(used):
    while True:
        i = "".join(RNG.choice(string.ascii_uppercase.replace("O", "").replace("I", "")) for _ in range(4))
        if i not in used: used.add(i); return i

def sheet(num, brief, left, right, out, H=1000, pad=40):
    ims = [Image.open(p).convert("RGB") for p, _ in (left, right)]
    ims = [im.resize((round(im.width * H / im.height), H), Image.LANCZOS) for im in ims]
    W = sum(im.width for im in ims) + pad * 3
    f_b, f_t, f_id = font(40), font(34), font(60)
    lines = textwrap.wrap("Brief: " + brief["brief"], width=int(W / 18))
    top = pad + 60 + len(lines) * 44 + 24
    canvas = Image.new("RGB", (W, top + H + 130), (245, 244, 240)); d = ImageDraw.Draw(canvas)
    d.text((pad, pad), f"Sheet S{num:02d}  ({brief['medium']})", font=f_b, fill=(20, 20, 20))
    for k, l in enumerate(lines): d.text((pad, pad + 60 + k * 44), l, font=f_t, fill=(40, 40, 40))
    x = pad
    for im, (_, iid) in zip(ims, (left, right)):
        canvas.paste(im, (x, top)); d.text((x, top + H + 24), iid, font=f_id, fill=(20, 20, 20)); x += im.width + pad
    canvas.save(out, quality=88)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--images", required=True); ap.add_argument("--sheets", required=True)
    ap.add_argument("--key", required=True)
    ap.add_argument("--batch", type=int, default=1, help="which batch of briefs.json to build (briefs with no 'batch' are batch 1)")
    ap.add_argument("--start", type=int, default=1, help="number of the first sheet, e.g. 17 for batch 2")
    ap.add_argument("--repeat", action="store_true", help="two sheets per brief, sides swapped (batch 1 used this; useful for model judges)")
    ap.add_argument("--avoid-key", action="append", default=[], help="earlier key file(s) whose IDs must not be reused")
    a = ap.parse_args()
    briefs = [b for b in json.load(open(os.path.join(HERE, "briefs.json"), encoding="utf-8")) if b.get("batch", 1) == a.batch]
    used = set()
    for k in a.avoid_key:
        used |= set(json.load(open(k))["images"])
    per = 2 if a.repeat else 1
    if os.path.exists(a.key) or any(os.path.exists(os.path.join(a.sheets, f"S{a.start + i:02d}.jpg")) for i in range(per * len(briefs))):
        raise SystemExit("refusing to overwrite an existing key or sheet")
    os.makedirs(a.sheets, exist_ok=True); pairs = []
    for b in briefs:
        ids = {c: new_id(used) for c in ("with", "without")}
        paths = {c: os.path.join(a.images, f"{b['id']}-{c}.jpg") for c in ids}
        first = RNG.choice([("with", "without"), ("without", "with")])
        for order in ((first, first[::-1]) if a.repeat else (first,)):
            pairs.append((b, order, ids, paths))
    # shuffle until no brief has its two sheets next to each other
    while True:
        RNG.shuffle(pairs)
        if all(pairs[i][0]["id"] != pairs[i + 1][0]["id"] for i in range(len(pairs) - 1)): break
    key = {"salt": secrets.token_hex(16), "note": "Hidden key for examples/blind-test. Do not commit or show to judges before judging ends.",
           "images": {}, "sheets": []}
    for n, (b, order, ids, paths) in enumerate(pairs, a.start):
        l, r = order
        sheet(n, b, (paths[l], ids[l]), (paths[r], ids[r]), os.path.join(a.sheets, f"S{n:02d}.jpg"))
        key["sheets"].append({"sheet": f"S{n:02d}", "brief": b["id"], "left": {"id": ids[l], "condition": l}, "right": {"id": ids[r], "condition": r}})
        for c in ids:
            key["images"][ids[c]] = {"brief": b["id"], "condition": c, "file": os.path.basename(paths[c]),
                                     "sha256": hashlib.sha256(open(paths[c], "rb").read()).hexdigest()}
    data = json.dumps(key, indent=1, sort_keys=True).encode()
    open(a.key, "wb").write(data)
    print(f"{len(pairs)} sheets in {a.sheets}; key {a.key}\nkey sha256 {hashlib.sha256(data).hexdigest()}")

if __name__ == "__main__":
    main()

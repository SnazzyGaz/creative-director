"""datagraphic.py: draw charts and routes from the data in code, composite them into generated art, and check
that bar lengths match the data (LAY-19). Never trust an image model for numbers or geometry.

  python3 tools/datagraphic.py bars SPEC.json OUT.png        # bar chart from data (transparent unless "bg" is set)
  python3 tools/datagraphic.py route SPEC.json OUT.png       # closed loop route; a bridge wherever it crosses the river
  python3 tools/datagraphic.py donut SPEC.json OUT.png       # part-of-whole donut (at most 6 slices), angles exactly from the data
  python3 tools/datagraphic.py composite ART LAYER --box x0,y0,x1,y1 OUT.png   # fit LAYER into a reserved box
  python3 tools/datagraphic.py check-donut IMG --centre cx,cy --radius R --values 38,22 --colour R,G,B [--colour ...]
  python3 tools/datagraphic.py check-panel IMG --box x0,y0,x1,y1   # FLAG a flat panel pasted behind the chart (INF-1)
  python3 tools/datagraphic.py check-bars IMG --box x0,y0,x1,y1 --values 42,58,71 --colour R,G,B [--colour ...]
                                          [--orientation vertical|horizontal] [--scale-max V] [--tol 0.02]

bars spec: {"values": [42, 58], "labels": ["2021", "2022"], "value_labels": ["42,000", "58,000"],
  "orientation": "vertical", "width": 1200, "height": 600, "colours": ["#2E7D32"], "track": "#E6E6E6",
  "scale_max": null, "text": "#1F2A24", "font": "path.ttf", "bold_font": "path.ttf", "text_size": 30, "gap": 0.35}
  Lengths are exactly value / scale_max of the plot length (scale_max defaults to the largest value). A track is
  drawn the full plot length when "track" is set, which makes the scale visible (0 to scale_max).
route spec: {"width": 1600, "height": 900, "points": [[0.1, 0.6], ...] (0-1, in order, start first),
  "river": [[x, y], ...] (optional), "colour": "#D81B60", "line": 14, "labels": [{"text": "Old Mill", "at": [x, y]}],
  "start_label": "Start / Finish", "arrows": 6, "font": ..., "text_size": 28, "river_colour": "#64B5F6" (draws the river)}
  The route is drawn as one smooth closed loop through the points, so start = finish by construction, with a
  chequered start/finish marker and direction arrows. Every place the loop crosses the river gets a bridge.
donut spec: {"values": [38, 22, 40], "colours": [...], "labels": [...], "value_labels": [...], "size": 900,
  "inner": 0.55, "gap_colour": null, "start": 0 (degrees clockwise from 12 o'clock), "font": ..., "text_size": 34}
  Slices run clockwise from "start"; each spans exactly value / total of 360 degrees. Labels sit outside the ring.
check-donut: samples a circle of --radius round --centre and measures each colour's share of the ring. PASS when
  every share is within --tol (default 0.02) of value / total.
check-panel: compares a thin band just inside the box with one just outside. A flat, near-uniform inner band that
  differs from its surroundings is a panel or white box pasted behind the chart: FLAG (exit 0; it is a design check).
route: labels that would cross the line are moved off it (reported as "labels clear of the route").
bars spec also takes "corner" (px, rounds the bar ends) to match the piece's corner style.
check-bars: in the box, finds bars of the given colour(s) and measures each one's length from its base. PASS when
  every bar's length relative to the longest matches value / largest value within --tol (default 0.02, i.e. 2% of
  the longest bar); with --scale-max, the lengths are also checked against the box length (the box spans 0 to V).
  Exit 1 on FAIL. Measures pixels only: put the box tight round the plot area (base line to the far end).
Needs Pillow and numpy.
"""
import sys, json, math, argparse
import numpy as np
from PIL import Image, ImageDraw, ImageFont

FALLBACK = ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/Library/Fonts/Arial.ttf", "C:/Windows/Fonts/arial.ttf"]
FALLBACK_BOLD = ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/Library/Fonts/Arial Bold.ttf", "C:/Windows/Fonts/arialbd.ttf"]

def font(path, size, bold=False):
    for p in ([path] if path else []) + (FALLBACK_BOLD if bold else FALLBACK):
        try: return ImageFont.truetype(p, size)
        except (OSError, TypeError): pass
    try: return ImageFont.load_default(size)
    except TypeError: return ImageFont.load_default()

def rgb(c):
    if isinstance(c, (list, tuple)): return tuple(int(v) for v in c[:3])
    c = c.lstrip("#"); return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))

def text_c(d, xy, s, f, fill, anchor):
    d.text(xy, s, font=f, fill=fill, anchor=anchor)

def bar(d, xy, fill, r):
    r = min(int(r), int((xy[2] - xy[0]) // 2), int((xy[3] - xy[1]) // 2))
    d.rounded_rectangle(xy, radius=r, fill=fill) if r > 0 else d.rectangle(xy, fill=fill)

def bars(spec, out):
    v = [float(x) for x in spec["values"]]; n = len(v)
    W, H = spec.get("width", 1200), spec.get("height", 600)
    vert = spec.get("orientation", "vertical") == "vertical"
    top = spec.get("scale_max") or max(v)
    cols = [rgb(c) for c in spec.get("colours", ["#2E7D32"])]; tc = rgb(spec.get("text", "#222222"))
    ts = spec.get("text_size", max(14, H // 20))
    f = font(spec.get("font"), ts); fb = font(spec.get("bold_font"), ts, bold=True)
    labels = spec.get("labels", [""] * n); vl = spec.get("value_labels", [""] * n)
    im = Image.new("RGBA", (W, H), rgb(spec["bg"]) + (255,) if spec.get("bg") else (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    gap = spec.get("gap", 0.35); boxes = []
    if vert:
        x0, x1, y_base, y_top = int(W * .02), int(W * .98), int(H - ts * 1.9), int(ts * 1.8)
        L = y_base - y_top; slot = (x1 - x0) / n; bw = slot * (1 - gap)
        for i, val in enumerate(v):
            cx = x0 + slot * (i + .5); a, b = int(round(cx - bw / 2)), int(round(cx + bw / 2))
            if spec.get("track"): d.rectangle([a, y_top, b, y_base], fill=rgb(spec["track"]))
            h = int(round(L * val / top)); bar(d, [a, y_base - h, b, y_base], cols[i % len(cols)], spec.get("corner", 0))
            boxes.append([a, y_base - h, b, y_base])
            text_c(d, (cx, y_base - h - ts * .4), vl[i], fb, tc, "ms")
            text_c(d, (cx, y_base + ts * .5), labels[i], f, tc, "mt")
        plot = [x0, y_top, x1, y_base]
    else:
        lab_w = max([d.textlength(s, font=f) for s in labels] + [0]) + ts * .8
        val_w = max([d.textlength(s, font=fb) for s in vl] + [0]) + ts * .8
        x_base, x_end, y0, y1 = int(lab_w), int(W - val_w), 0, H
        L = x_end - x_base; slot = (y1 - y0) / n; bh = slot * (1 - gap)
        for i, val in enumerate(v):
            cy = y0 + slot * (i + .5); a, b = int(round(cy - bh / 2)), int(round(cy + bh / 2))
            if spec.get("track"): d.rectangle([x_base, a, x_end, b], fill=rgb(spec["track"]))
            w = int(round(L * val / top)); bar(d, [x_base, a, x_base + w, b], cols[i % len(cols)], spec.get("corner", 0))
            boxes.append([x_base, a, x_base + w, b])
            text_c(d, (0, cy), labels[i], f, tc, "lm")
            text_c(d, (W, cy), vl[i], fb, tc, "rm")
        plot = [x_base, y0, x_end, y1]
    im.save(out)
    rep = {"plot": plot, "bars": boxes, "values": v, "scale_max": top, "orientation": "vertical" if vert else "horizontal"}
    json.dump(rep, open(out + ".json", "w"), indent=1)
    print(f"bars: {n} drawn, lengths exactly value / {top:g} of {L} px; boxes in {out}.json")
    return rep

def catmull(pts, k=24):
    n = len(pts); out = []
    for i in range(n):
        p0, p1, p2, p3 = (np.array(pts[(i + j) % n], float) for j in (-1, 0, 1, 2))
        for t in np.linspace(0, 1, k, endpoint=False):
            out.append(.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t * t + (-p0 + 3 * p1 - 3 * p2 + p3) * t ** 3))
    out.append(out[0]); return out

def seg_x(p, q, r, s):
    d = (q[0] - p[0]) * (s[1] - r[1]) - (q[1] - p[1]) * (s[0] - r[0])
    if abs(d) < 1e-12: return None
    t = ((r[0] - p[0]) * (s[1] - r[1]) - (r[1] - p[1]) * (s[0] - r[0])) / d
    u = ((r[0] - p[0]) * (q[1] - p[1]) - (r[1] - p[1]) * (q[0] - p[0])) / d
    return (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]), math.atan2(q[1] - p[1], q[0] - p[0])) if 0 <= t <= 1 and 0 <= u <= 1 else None

def route(spec, out):
    W, H = spec.get("width", 1600), spec.get("height", 900); S = lambda p: (p[0] * W, p[1] * H)
    col = rgb(spec.get("colour", "#D81B60")); lw = spec.get("line", 14); ts = spec.get("text_size", 28)
    im = Image.new("RGBA", (W, H), rgb(spec["bg"]) + (255,) if spec.get("bg") else (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    path = [S(p) for p in catmull(spec["points"])]
    if spec.get("river") and spec.get("river_colour"):   # draw the river too, when the art doesn't already show it
        d.line([S(p) for p in spec["river"]], fill=rgb(spec["river_colour"]), width=spec.get("river_width", lw * 3), joint="curve")
    d.line(path, fill=col, width=lw, joint="curve")
    crossings = []
    if spec.get("river"):
        rv = [S(p) for p in spec["river"]]
        for i in range(len(path) - 1):
            for j in range(len(rv) - 1):
                x = seg_x(path[i], path[i + 1], rv[j], rv[j + 1])
                if x and all(math.hypot(x[0] - c[0], x[1] - c[1]) > lw * 3 for c in crossings): crossings.append(x)
        for (x, y, ang) in crossings:   # bridge: deck along the route, rails either side
            ca, sa = math.cos(ang), math.sin(ang); hl, hw = lw * 3.2, lw * 1.25
            corners = [(x + ca * a - sa * b, y + sa * a + ca * b) for a, b in ((-hl, -hw), (hl, -hw), (hl, hw), (-hl, hw))]
            d.polygon(corners, fill=rgb(spec.get("bridge", "#8D6E63")))
            for b in (-hw, hw):
                d.line([(x - ca * hl - sa * b, y - sa * hl + ca * b), (x + ca * hl - sa * b, y + sa * hl + ca * b)], fill=rgb(spec.get("rail", "#4E342E")), width=max(3, lw // 4))
            d.line([(x - ca * hl, y - sa * hl), (x + ca * hl, y + sa * hl)], fill=col, width=max(4, lw // 2))
    na = spec.get("arrows", 6); step = max(1, (len(path) - 1) // (na + 1))
    for i in range(step, len(path) - 2, step):   # chevrons showing the direction of travel
        (x, y), (x2, y2) = path[i], path[i + 1]; a = math.atan2(y2 - y, x2 - x); r = lw * 1.1
        tip = (x + math.cos(a) * r, y + math.sin(a) * r)
        d.polygon([tip, (x + math.cos(a + 2.5) * r, y + math.sin(a + 2.5) * r), (x + math.cos(a - 2.5) * r, y + math.sin(a - 2.5) * r)], fill=(255, 255, 255))
    sx, sy = path[0]; q = lw * 1.3   # chequered start/finish block on the loop's first point
    for i in range(4):
        for j in range(2):
            d.rectangle([sx - 2 * q + i * q, sy - q + j * q, sx - q + i * q, sy + j * q], fill=(20, 20, 20) if (i + j) % 2 else (255, 255, 255))
    f = font(spec.get("font"), ts, bold=True); tc = rgb(spec.get("text", "#1F2A33"))
    labs = list(spec.get("labels", []))
    if spec.get("start_label"): labs.append({"text": spec["start_label"], "at": [spec["points"][0][0], spec["points"][0][1] - 3.2 * lw / H]})
    moved = 0
    def hits(x, y, w):   # does the label box (with padding) come within half a line of the route?
        return any(x - w / 2 - lw <= px <= x + w / 2 + lw and y - ts / 2 - lw <= py <= y + ts / 2 + lw for px, py in path)
    for lab in labs:
        x, y = S(lab["at"]); w = d.textlength(lab["text"], font=f); p = ts * .35
        if hits(x, y, w):
            for k in range(1, 12):
                cand = [(x, y - k * ts * .5), (x, y + k * ts * .5), (x - k * ts * .5, y), (x + k * ts * .5, y)]
                cand = [c for c in cand if w / 2 + p <= c[0] <= W - w / 2 - p and ts <= c[1] <= H - ts and not hits(c[0], c[1], w)]
                if cand: x, y = cand[0]; moved += 1; break
        x = min(max(x, w / 2 + p), W - w / 2 - p)   # keep the whole label inside the layer
        d.rounded_rectangle([x - w / 2 - p, y - ts / 2 - p, x + w / 2 + p, y + ts / 2 + p], radius=int(p), fill=(255, 255, 255))
        text_c(d, (x, y), lab["text"], f, tc, "mm")
    im.save(out)
    closed = math.hypot(path[0][0] - path[-1][0], path[0][1] - path[-1][1]) < 1
    clear = sum(not hits(*S(l["at"]), d.textlength(l["text"], font=f)) for l in labs)
    print(f"route: closed loop {'yes' if closed else 'NO'} (start = finish), {len(crossings)} river crossing(s), {len(crossings)} bridge(s) drawn, "
          f"{moved} label(s) moved off the line")
    return {"closed": closed, "crossings": len(crossings), "bridges": len(crossings), "labels_moved": moved}

def donut(spec, out):
    v = [float(x) for x in spec["values"]]; tot = sum(v); n = len(v)
    if n > 6: print("donut: more than 6 slices; use bars (INF-4)")
    S_ = spec.get("size", 900); ts = spec.get("text_size", max(14, S_ // 26)); pad = spec.get("pad", ts * 5)
    W = H = S_ + 2 * pad; cx = cy = W / 2; R_ = S_ / 2; ri = R_ * spec.get("inner", 0.55)
    cols = [rgb(c) for c in spec.get("colours", ["#2E7D32"])]; tc = rgb(spec.get("text", "#222222"))
    im = Image.new("RGBA", (int(W), int(H)), rgb(spec["bg"]) + (255,) if spec.get("bg") else (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    f = font(spec.get("font"), ts); fb = font(spec.get("bold_font"), ts, bold=True)
    labels = spec.get("labels", [""] * n); vl = spec.get("value_labels", [""] * n)
    a0 = spec.get("start", 0); slices = []
    for i, val in enumerate(v):
        a1 = a0 + 360 * val / tot
        d.pieslice([cx - R_, cy - R_, cx + R_, cy + R_], a0 - 90, a1 - 90, fill=cols[i % len(cols)])
        mid = math.radians((a0 + a1) / 2); lx, ly = cx + (R_ + ts * 1.6) * math.sin(mid), cy - (R_ + ts * 1.6) * math.cos(mid)
        anc = "lm" if math.sin(mid) > 0.25 else "rm" if math.sin(mid) < -0.25 else "mm"
        text_c(d, (lx, ly - ts * .55), vl[i], fb, tc, anc); text_c(d, (lx, ly + ts * .6), labels[i], f, tc, anc)
        slices.append([a0, a1]); a0 = a1
    hole = spec.get("hole")   # the ground colour shows through the hole; transparent by default
    d.ellipse([cx - ri, cy - ri, cx + ri, cy + ri], fill=rgb(hole) + (255,) if hole else (0, 0, 0, 0))
    if spec.get("gap_colour"):
        for a, _ in slices:
            r_ = math.radians(a); d.line([(cx + ri * math.sin(r_), cy - ri * math.cos(r_)), (cx + R_ * math.sin(r_), cy - R_ * math.cos(r_))], fill=rgb(spec["gap_colour"]), width=max(3, ts // 6))
    im.save(out)
    rep = {"centre": [cx, cy], "radius": R_, "inner": ri, "slices": slices, "values": v}
    json.dump(rep, open(out + ".json", "w"), indent=1)
    print(f"donut: {n} slices, each exactly value / {tot:g} of 360 degrees; geometry in {out}.json"); return rep

def check_donut(img, centre, radius, values, colours, tol=0.02, ctol=60):
    a = np.asarray(Image.open(img).convert("RGB")).astype(int); cx, cy = centre; cnt = [0] * len(colours); N = 3600
    for k in range(N):
        t_ = 2 * math.pi * k / N; x, y = int(round(cx + radius * math.sin(t_))), int(round(cy - radius * math.cos(t_)))
        if not (0 <= x < a.shape[1] and 0 <= y < a.shape[0]): continue
        dist = [np.abs(a[y, x] - np.array(c)).sum() for c in colours]; j = int(np.argmin(dist))
        if dist[j] < ctol: cnt[j] += 1
    tot, vt = sum(cnt), sum(values)
    if not tot: print("FAIL  LAY-19  no slice colours found on that circle: check --centre, --radius and --colour"); return 1
    worst = 0; rows = []
    for v, c in zip(values, cnt):
        got, exp = c / tot, v / vt; worst = max(worst, abs(got - exp))
        rows.append(f"    {v:g}: {got * 100:.1f}% of the ring (data {exp * 100:.1f}%, {(got - exp) * 100:+.1f} pts)")
    st = "PASS" if worst <= tol else "FAIL"
    print(f"{st}  LAY-19  slice shares against the data: worst error {worst * 100:.1f} pts (tolerance {tol * 100:g})"); print("\n".join(rows))
    return 0 if st == "PASS" else 1

def check_panel(img, box, band=8):
    a = np.asarray(Image.open(img).convert("RGB")).astype(float); x0, y0, x1, y1 = box; H, W = a.shape[:2]
    def ring(o):   # pixels on a band of width `band` at offset o (negative = inside the box)
        X0, Y0, X1, Y1 = max(0, x0 + o), max(0, y0 + o), min(W, x1 - o), min(H, y1 - o)
        m = np.zeros((H, W), bool); m[Y0:Y1, X0:X1] = True
        X0b, Y0b, X1b, Y1b = X0 + band, Y0 + band, X1 - band, Y1 - band
        if X1b > X0b and Y1b > Y0b: m[Y0b:Y1b, X0b:X1b] = False
        return a[m]
    inner, outer = ring(band // 2), ring(-band * 2)
    if not len(inner) or not len(outer): print("SKIP  INF-1  box at the image edge"); return 0
    sd = float(inner.std(0).mean()); diff = float(np.abs(np.median(inner, 0) - np.median(outer, 0)).sum())
    flat = sd < 6 and diff > 30
    print(f"{'FLAG' if flat else 'PASS'}  INF-1  chart ground against its surroundings: inner band spread {sd:.1f}, colour step {diff:.0f} "
          f"({'a flat panel pasted behind the chart: style the chart into the piece' if flat else 'no pasted panel edge'})")
    return "FLAG" if flat else "PASS"

def composite(art, layer, box, out):
    A = Image.open(art).convert("RGBA"); Lr = Image.open(layer).convert("RGBA"); x0, y0, x1, y1 = box
    s = min((x1 - x0) / Lr.width, (y1 - y0) / Lr.height); Lr = Lr.resize((round(Lr.width * s), round(Lr.height * s)), Image.LANCZOS)
    A.alpha_composite(Lr, (x0 + (x1 - x0 - Lr.width) // 2, y0 + (y1 - y0 - Lr.height) // 2))
    A.convert("RGB").save(out); print(f"composite: {layer} fitted into {box} of {art} -> {out} (scale {s:.3f}, aspect kept)")

def check_bars(img, box, values, colours, orientation="vertical", scale_max=None, tol=0.02, ctol=60):
    a = np.asarray(Image.open(img).convert("RGB")).astype(int); x0, y0, x1, y1 = box; a = a[y0:y1, x0:x1]
    m = np.zeros(a.shape[:2], bool)
    for c in colours: m |= np.abs(a - np.array(c)).sum(2) < ctol
    m = m.T if orientation == "horizontal" else m[::-1]   # row 0 is the base: the left edge, or the bottom
    cols = m.sum(0) > 0; runs = []; i = 0
    while i < len(cols):
        if cols[i]:
            j = i
            while j < len(cols) and cols[j]: j += 1
            if j - i >= 3: runs.append((i, j))
            i = j
        else: i += 1
    lens = []
    for i, j in runs:   # length = contiguous run from the base, median over the bar's middle half
        L = []
        for c in range((3 * i + j) // 4, (i + 3 * j) // 4 + 1):
            col = m[:, c]; nz = np.nonzero(col)[0]
            if not len(nz): continue
            b = nz[0]; e = b
            while e < len(col) and col[e]: e += 1
            L.append(e)
        lens.append(float(np.median(L)) if L else 0.0)
    rule = "LAY-19"
    if len(lens) != len(values):
        print(f"FAIL  {rule}  found {len(lens)} bar(s) of the given colour(s), expected {len(values)}: tighten --box or add --colour"); return 1
    vmax = max(values); lmax = max(lens); worst = 0; rows = []
    for v, L in zip(values, lens):
        exp, got = v / vmax, L / lmax; err = got - exp; worst = max(worst, abs(err))
        rows.append(f"    {v:g}: {L:.0f} px, {got * 100:.1f}% of the longest (data {exp * 100:.1f}%, {err * 100:+.1f} pts)")
    st = "PASS" if worst <= tol else "FAIL"
    print(f"{st}  {rule}  bar lengths against the data: worst error {worst * 100:.1f}% of the longest bar (tolerance {tol * 100:g}%)"); print("\n".join(rows))
    bad = worst > tol
    if scale_max:
        full = (y1 - y0) if orientation == "vertical" else (x1 - x0)
        w2 = max(abs(L / full - v / scale_max) for v, L in zip(values, lens))
        st2 = "PASS" if w2 <= tol else "FAIL"; bad |= w2 > tol
        print(f"{st2}  {rule}  against the scale (box = 0 to {scale_max:g}): worst error {w2 * 100:.1f}% of full scale")
    return 1 if bad else 0

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0]); sp = ap.add_subparsers(dest="cmd", required=True)
    for c in ("bars", "route", "donut"):
        p = sp.add_parser(c); p.add_argument("spec"); p.add_argument("out")
    p = sp.add_parser("composite"); p.add_argument("art"); p.add_argument("layer"); p.add_argument("--box", required=True); p.add_argument("out")
    p = sp.add_parser("check-bars"); p.add_argument("img"); p.add_argument("--box", required=True); p.add_argument("--values", required=True)
    p.add_argument("--colour", action="append", required=True); p.add_argument("--orientation", default="vertical", choices=["vertical", "horizontal"])
    p.add_argument("--scale-max", type=float); p.add_argument("--tol", type=float, default=0.02); p.add_argument("--colour-tol", type=int, default=60)
    p = sp.add_parser("check-donut"); p.add_argument("img"); p.add_argument("--centre", required=True); p.add_argument("--radius", type=float, required=True)
    p.add_argument("--values", required=True); p.add_argument("--colour", action="append", required=True); p.add_argument("--tol", type=float, default=0.02)
    p = sp.add_parser("check-panel"); p.add_argument("img"); p.add_argument("--box", required=True)
    a = ap.parse_args(argv); box = lambda s: [int(float(x)) for x in s.split(",")]
    if a.cmd == "bars": bars(json.load(open(a.spec)), a.out); return 0
    if a.cmd == "route": r = route(json.load(open(a.spec)), a.out); return 0 if r["closed"] else 1
    if a.cmd == "composite": composite(a.art, a.layer, box(a.box), a.out); return 0
    if a.cmd == "donut": donut(json.load(open(a.spec)), a.out); return 0
    if a.cmd == "check-panel": check_panel(a.img, box(a.box)); return 0
    cols = [rgb(c) if c.startswith("#") else tuple(int(v) for v in c.split(",")) for c in a.colour]
    if a.cmd == "check-donut":
        return check_donut(a.img, [float(v) for v in a.centre.split(",")], a.radius, [float(v) for v in a.values.split(",")], cols, a.tol)
    return check_bars(a.img, box(a.box), [float(v) for v in a.values.split(",")], cols, a.orientation, a.scale_max, a.tol, a.colour_tol)

if __name__ == "__main__":
    sys.exit(main())

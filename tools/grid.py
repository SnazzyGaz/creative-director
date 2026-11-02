"""grid.py: layout-grid check from a screenshot (CORE-5 alignment, UI-4 grid, CORE-4 spacing scale).

python3 tools/grid.py SHOT.png [--out overlay.png] [--near 6] [--merge 9] [--min 8] [--scale 4] [--dpr 1]

Finds element boxes from edges (text joined into blocks by a --merge px dilation;
nested boxes such as text inside a card are kept). A box is "solid" when it has a
hard frame (border, background, image): its edges are straight lines of pixels.
Reports:
  STRAY   a solid box whose left edge misses an alignment line (3+ boxes within 1 px)
          by 2..--near px. Text ink a few px off a line is listed as "check" only:
          letter side bearings move ink by 1-5 px at large sizes.
  ROW     a row of 2+ similar-width solid boxes (cards, tiles) whose tops differ, or
          whose column steps or gaps differ.
  (in ROW) boxes in a row whose content sits at different left/top insets (padding).
  SCALE   gaps between solid boxes (in rows and in stacks) that are not multiples of --scale (default 4; the share on 8 is shown too), or near-duplicates 2..--near px apart.
Vertical gaps between text blocks are printed for information only: ink tops and
bottoms depend on the letters, so they can't be held to a px scale.
Sizes are screenshot px; --dpr converts to CSS px (2 for a retina capture).
Limits: sees ink, not the DOM; boxes with no frame end at their text; shadows and
gradients can merge neighbours; centred layouts have few left-edge lines. Confirm
on the overlay (--out): blue = boxes, green = alignment lines, red = findings.
"""
import argparse
import numpy as np, cv2

def find_boxes(img, merge, mn):
    g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    e = cv2.Canny(g, 20, 60)
    m = cv2.dilate(e, cv2.getStructuringElement(cv2.MORPH_RECT, (merge, max(3, merge // 2))))
    cs, _ = cv2.findContours(m, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    out = []
    for c in cs:
        x, y, w, h = cv2.boundingRect(c)
        if w < mn or h < mn or (w > 0.97 * img.shape[1] and h > 0.97 * img.shape[0]): continue
        ys, xs = np.nonzero(e[y:y + h, x:x + w])           # undo the dilation
        if len(xs) == 0: continue
        b = (int(x + xs.min()), int(y + ys.min()), int(x + xs.max() + 1), int(y + ys.max() + 1))
        if any(b == o['b'] for o in out): continue
        x0, y0, x1, y1 = b; W, H = x1 - x0, y1 - y0
        def run(sl): return float((sl.max(axis=0) > 0).mean()) if sl.size else 0
        # frame: edge pixels along most of the left side and the top side (+-2 px; rounded corners ok)
        left = run(e[y0:y1, max(0, x0 - 1):x0 + 3].T); top = run(e[max(0, y0 - 1):y0 + 3, x0:x1])
        solid = W >= 16 and H >= 16 and left > 0.7 and top > 0.7
        if solid: b = refine(g, b)
        out.append(dict(b=b, solid=solid))
    return out

def refine(g, b):
    """Canny marks the pixel just outside a thin border; step each side in while the
    line still matches the background beyond it."""
    x0, y0, x1, y1 = b; g = g.astype(int); H, W = g.shape
    def same(a, c): return np.median(np.abs(a - c)) < 6
    for _ in range(2):
        if x0 >= 1 and same(g[y0:y1, x0], g[y0:y1, x0 - 1]): x0 += 1
        if x1 < W and same(g[y0:y1, x1 - 1], g[y0:y1, x1]): x1 -= 1
        if y0 >= 1 and same(g[y0, x0:x1], g[y0 - 1, x0:x1]): y0 += 1
        if y1 < H and same(g[y1 - 1, x0:x1], g[y1, x0:x1]): y1 -= 1
    return (x0, y0, x1, y1)

def inside(a, b, s=2):
    return a != b and a[0] >= b[0] - s and a[1] >= b[1] - s and a[2] <= b[2] + s and a[3] <= b[3] + s

def nested(a, b): return inside(a, b) or inside(b, a)

def groups(vals, tol=1):
    vs = sorted(vals); cl = [[vs[0]]] if vs else []
    for v in vs[1:]:
        if v - cl[-1][-1] <= tol: cl[-1].append(v)
        else: cl.append([v])
    return cl

def main():
    p = argparse.ArgumentParser(); p.add_argument('img'); p.add_argument('--out')
    p.add_argument('--near', type=int, default=6); p.add_argument('--merge', type=int, default=9)
    p.add_argument('--min', type=int, default=8); p.add_argument('--scale', type=int, default=4)
    p.add_argument('--dpr', type=float, default=1)
    a = p.parse_args(); k = a.dpr
    img = cv2.imread(a.img); BX = find_boxes(img, a.merge, a.min); B = [o['b'] for o in BX]
    S = [o['b'] for o in BX if o['solid']]
    # drop a solid box that just frames another solid box 1-4 px inside it (double border, shadow)
    S = [s for s in S if not any(inside(t, s) and max(abs(t[i] - s[i]) for i in range(4)) <= 4 for t in S)]
    print(f'{a.img}: {img.shape[1]}x{img.shape[0]} px, {len(B)} boxes, {len(S)} solid')
    issues = 0; red = []; spacing = []
    px = lambda v: f'{v / k:.0f}' if k != 1 else f'{v}'
    # 1. alignment lines and strays
    lines = [c for c in groups([b[0] for b in B]) if len(c) >= 3]
    print('left-edge lines (x: boxes): ' + (', '.join(f'{px(round(np.median(c)))}: {len(c)}' for c in sorted(lines, key=len, reverse=True)[:12]) or 'none with 3+'))
    for o in BX:
        b = o['b']; x = b[0]
        best = None
        for c in lines:
            lx = np.median(c); d = x - lx
            members = [m for m in B if m[0] in c and not nested(m, b)]
            if 1 < abs(d) <= a.near and len(members) >= 3 and (best is None or abs(d) < abs(best[0])): best = (d, lx, len(members))
        if best and not any(abs(x - np.median(c)) <= 1 for c in lines):
            d, lx, n = best
            if o['solid']:
                issues += 1; red.append(b)
                print(f'  STRAY solid box at ({px(b[0])}, {px(b[1])}) {px(b[2]-b[0])}x{px(b[3]-b[1])}: left edge {d/k:+.0f} px off the line at x={px(round(lx))} ({n} boxes) -> CORE-5, UI-4')
            else:
                print(f'  check: text at ({px(b[0])}, {px(b[1])}) is {d/k:+.0f} px off the line at x={px(round(lx))}; side bearing or a real miss? Look at 2x')
    # 2. rows of same-size solid boxes
    tops = [s for s in S if not any(inside(s, t) for t in S)]
    rows, used = [], set()
    for i, s in enumerate(sorted(tops, key=lambda b: (b[1], b[0]))):
        if s in used: continue
        r = [t for t in tops if t not in used and abs((t[2] - t[0]) - (s[2] - s[0])) <= 0.3 * (s[2] - s[0])
             and min(s[3], t[3]) - max(s[1], t[1]) > 0.5 * min(s[3] - s[1], t[3] - t[1])]
        if len(r) >= 2: rows.append(sorted(r, key=lambda b: b[0])); used |= set(r)
    for r in rows:
        ts = [b[1] for b in r]; steps = np.diff([b[0] for b in r]); gaps = [int(v[0] - u[2]) for u, v in zip(r, r[1:])]
        bad = []
        if max(ts) - min(ts) > 1: bad.append(f'tops differ by {px(max(ts) - min(ts))} px')
        ws = [b[2] - b[0] for b in r]
        if len(steps) >= 2 and steps.max() - steps.min() > 2 and max(ws) - min(ws) <= 2: bad.append(f'column steps differ ({", ".join(px(int(s)) for s in steps)})')
        if len(gaps) >= 2 and max(gaps) - min(gaps) > 2: bad.append(f'gaps differ ({", ".join(px(g) for g in gaps)})')
        spacing += [('row gap', g) for g in gaps if g > 0]
        # insets: where the content starts inside each box
        ins = []
        for b in r:
            kids = [c for c in B if inside(c, b) and c != b and (c[2] - c[0]) < (b[2] - b[0]) - 4]
            ins.append((min(c[0] for c in kids) - b[0], min(c[1] for c in kids) - b[1]) if kids else None)
        msg = f'row of {len(r)} boxes {px(r[0][2]-r[0][0])} px wide at y={px(min(ts))}: tops {[px(t) for t in ts]}, gaps {[px(g) for g in gaps]}'
        if all(ins):
            msg += f', content insets (left, top) {[(px(i[0]), px(i[1])) for i in ins]}'
            li = [i[0] for i in ins]; ti = [i[1] for i in ins]
            if max(li) - min(li) > 2 or max(ti) - min(ti) > 3: bad.append('content insets differ (padding)')
        if bad: issues += 1; red += r
        print(('  ROW ' if bad else 'row ') + msg + (' -> ' + '; '.join(bad) + ' -> CORE-5, UI-4' + (', CORE-4' if any('inset' in x or 'gaps' in x for x in bad) else '') if bad else ' OK'))
    # 3. vertical gaps between stacked solid boxes in one column
    for c in groups([s[0] for s in S]):
        col = sorted([s for s in S if s[0] in c], key=lambda b: b[1])
        for u, v in zip(col, col[1:]):
            g = v[1] - u[3]
            if 0 < g < 300 and not nested(u, v): spacing.append(('stack gap', int(g)))
    if spacing:
        vals = [v for _, v in spacing]
        off = [(n, v) for n, v in spacing if round(v / k) % a.scale]
        on8 = sum(1 for v in vals if round(v / k) % 8 == 0)
        cl = [round(float(np.median(c))) for c in groups(vals, 1)]
        dup = [(x, y) for x, y in zip(cl, cl[1:]) if 1 < y - x <= a.near * k]
        print(f'spacing between solid boxes: {sorted(px(v) for v in vals)}; on a {a.scale} px scale: {len(vals) - len(off)}/{len(vals)}, on 8 px: {on8}/{len(vals)}')
        if off: print('  SCALE off-scale: ' + ', '.join(f'{n} {px(v)}' for n, v in off) + ' -> CORE-4')
        if dup: print('  SCALE near-duplicate values: ' + ', '.join(f'{px(x)} vs {px(y)}' for x, y in dup) + ' -> CORE-4 (pick one)')
        issues += bool(off) + bool(dup)
    tg = []
    for c in lines:
        col = sorted([b for b in B if b[0] in c], key=lambda b: b[1])
        tg += [int(v[1] - u[3]) for u, v in zip(col, col[1:]) if 0 < v[1] - u[3] < 120 and not nested(u, v)]
    if tg: print(f'info: ink gaps between stacked text blocks {sorted(set(px(g) for g in tg), key=float)} (not checked)')
    print('OK: no alignment or spacing issues found' if not issues else f'{issues} issue(s)')
    if a.out:
        o = img.copy()
        for b in B: cv2.rectangle(o, b[:2], (b[2] - 1, b[3] - 1), (200, 140, 0), 1)
        for c in lines: x = int(np.median(c)); cv2.line(o, (x, 0), (x, o.shape[0]), (0, 170, 0), 1)
        for b in red: cv2.rectangle(o, b[:2], (b[2] - 1, b[3] - 1), (0, 0, 230), 2)
        cv2.imwrite(a.out, o)
    return issues

if __name__ == '__main__':
    raise SystemExit(1 if main() else 0)

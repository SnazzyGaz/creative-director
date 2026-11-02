"""LAY-10 whitespace-distribution check: measures the empty bands between element groups
and flags unintended dead zones. Paraphrased method: proximity grouping (Gestalt) means the
gaps *between* groups should be larger than gaps *within* them, and no single empty band
should dwarf the others unless it is a deliberate focal space.

Usage: python3 whitespace.py IMAGE [--bg R,G,B] [--intended Y0-Y1,...] [--axis left|right] [--ratio 1.5] [--sheet OUT.png]
  --intended  y ranges (in source pixels) that hold deliberate space, e.g. a shared header device
  --axis      the layout is flush-left/right; a zone on the open side, touching the far edge, is reviewed, not failed
  A dead zone mirrored by an equally empty zone on the other side (the flanks of a centred group) is reviewed, not failed.
Prints: margins, interior empty bands (height px and % of H), the ratio of each band to the
largest *other* interior band, sparse-row bands (coverage < 12%), and the largest empty
2-D cell region after a squint blur. Exit code 1 if any band or the dead zone fails.
A PASS means "review by eye", not approval.
"""
import sys, argparse
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

def analyse(path, bg=None, intended=(), ratio=1.5, min_frac=0.03, sparse=0.12, sheet=None, axis=None):
    im = Image.open(path).convert('RGB')
    W0 = 600; im = im.resize((W0, round(im.height * W0 / im.width)), Image.LANCZOS)
    s = W0 / Image.open(path).width
    a = np.asarray(im).astype(float); H, W = a.shape[:2]
    if bg is None:  # modal colour of the outer 2% frame
        e = max(2, int(0.02 * min(H, W)))
        border = np.concatenate([a[:e].reshape(-1, 3), a[-e:].reshape(-1, 3), a[:, :e].reshape(-1, 3), a[:, -e:].reshape(-1, 3)])
        q = (border // 16).astype(int); keys, cnt = np.unique(q, axis=0, return_counts=True)
        bg = keys[cnt.argmax()] * 16 + 8
    bg = np.array(bg, float)
    dist = np.sqrt(((a - bg) ** 2).sum(2))
    # texture counts as content too (photos with dark areas), via local gradient
    g = np.asarray(im.convert('L').filter(ImageFilter.FIND_EDGES)).astype(float)
    g[:2] = 0; g[-2:] = 0; g[:, :2] = 0; g[:, -2:] = 0   # the filter marks the image border itself as an edge
    content = (dist > 38) | (g > 40)
    # squint: blur then threshold so specks don't count and near things merge
    sq = np.asarray(Image.fromarray((content * 255).astype('uint8')).filter(ImageFilter.GaussianBlur(3))) > 60
    cov = sq.mean(1)
    rows = cov > 0.004
    bands = []; y = 0
    while y < H:
        if not rows[y]:
            y0 = y
            while y < H and not rows[y]: y += 1
            bands.append((y0, y - 1))
        else: y += 1
    margins = [b for b in bands if b[0] == 0 or b[1] == H - 1]
    inner = [b for b in bands if b not in margins and (b[1] - b[0] + 1) >= 4]
    sc = lambda v: round(v / s)
    out = {'H': sc(H), 'margins': [(sc(b0), sc(b1)) for b0, b1 in margins], 'bands': [], 'fail': False}
    hs = [b1 - b0 + 1 for b0, b1 in inner]
    for i, (b0, b1) in enumerate(inner):
        h = b1 - b0 + 1; others = [x for j, x in enumerate(hs) if j != i]
        ref = max(others) if others else 0
        r = h / ref if ref else float('inf')
        isint = any(lo <= sc(b0) and sc(b1) <= hi for lo, hi in intended)
        bad = (r > ratio and h / H > min_frac and not isint)
        out['bands'].append(dict(y0=sc(b0), y1=sc(b1), h=sc(h), pct=round(100 * h / H, 1), ratio=round(r, 2), intended=isint, fail=bad))
        out['fail'] |= bad
    # sparse rows: coverage under `sparse` across a run of at least 6% of H (a band that is "mostly empty")
    sp = cov < sparse; runs = []; y = 0
    while y < H:
        if sp[y]:
            y0 = y
            while y < H and sp[y]: y += 1
            if (y - y0) / H >= 0.06 and y0 > 0 and y < H: runs.append((sc(y0), sc(y - 1), round(100 * (y - y0) / H, 1), round(float(cov[y0:y].mean()), 3)))
        else: y += 1
    out['sparse'] = runs
    # 2-D dead zone: 24-px cells (at 600 wide) with < 2% content; largest empty rectangle
    c = 24; gh, gw = H // c, W // c
    cell = np.array([[sq[i*c:(i+1)*c, j*c:(j+1)*c].mean() < 0.02 for j in range(gw)] for i in range(gh)])
    best = (0, None); hist = np.zeros(gw, int)
    for i in range(gh):
        hist = np.where(cell[i], hist + 1, 0); st = []
        for j in range(gw + 1):
            hh = hist[j] if j < gw else 0; start = j
            while st and st[-1][1] >= hh:
                start, h0 = st.pop(); area = h0 * (j - start)
                if area > best[0]: best = (area, (start, i - h0 + 1, j - 1, i))
            st.append((start, hh))
    if best[1]:
        x0, y0, x1, y1 = best[1]
        out['dead_zone'] = dict(box=(sc(x0*c), sc(y0*c), sc((x1+1)*c), sc((y1+1)*c)), pct_area=round(100 * best[0] / (gh * gw), 1),
                                touches_edge=(y0 == 0 or y1 == gh - 1 or x0 == 0 or x1 == gw - 1))
        bx = out['dead_zone']['box']; side = min(bx[2] - bx[0], bx[3] - bx[1])
        gaps = [b['h'] for b in out['bands']] + [m[1] - m[0] + 1 for m in out['margins']]
        # with no interior bands (a full-bleed layout) fall back to a typical inter-group gap: 8% of the short side
        ref = max(gaps + [round(0.08 * min(out['H'], out['H'] * W / H))])
        full_width = (bx[2] - bx[0]) > 0.9 * out['H'] * W / H
        isint = any(lo <= bx[1] and bx[3] <= hi for lo, hi in intended)
        # a side zone mirrored by an equally empty zone on the other side is the flank of a centred group:
        # report it for review, do not fail it (a one-sided void beside off-centre content still fails)
        side_edge = x0 <= 2 or x1 >= gw - 3
        mirror = cell[y0:y1 + 1, gw - 1 - x1:gw - x0]
        symmetric = bool(side_edge and mirror.size and mirror.mean() >= 0.9)
        # with --axis left|right (a declared flush-left or flush-right layout), a zone on the open side,
        # touching the far edge, is the ragged counter-space of the axis: review it, don't fail it
        open_side = (axis == 'left' and x1 >= gw - 3) or (axis == 'right' and x0 <= 2)
        dz_bad = ref > 0 and side > ratio * ref and out['dead_zone']['pct_area'] > 3 and not full_width and not isint and not symmetric and not open_side
        out['dead_zone'].update(short_side=side, ref_gap=ref, ratio=round(side / ref, 2) if ref else None, symmetric_flank=symmetric, open_side=bool(open_side), fail=bool(dz_bad))
        out['fail'] |= bool(dz_bad)
    if sheet:
        v = Image.fromarray((sq * 255).astype('uint8')).convert('RGB'); vis = Image.blend(im, v, 0.35); d = ImageDraw.Draw(vis)
        for b in out['bands']:
            d.rectangle((0, b['y0'] * s, W - 1, b['y1'] * s), outline=(255, 0, 0) if b['fail'] else (0, 200, 0), width=2)
        if best[1]: d.rectangle(tuple(v * c for v in (x0, y0, x1 + 1, y1 + 1)), outline=(255, 160, 0), width=3)
        vis.save(sheet)
    return out

if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('image'); p.add_argument('--bg'); p.add_argument('--intended', default='')
    p.add_argument('--ratio', type=float, default=1.5); p.add_argument('--sheet'); p.add_argument('--axis', choices=['left', 'right'])
    A = p.parse_args()
    bg = tuple(int(v) for v in A.bg.split(',')) if A.bg else None
    intended = [tuple(int(v) for v in r.split('-')) for r in A.intended.split(',') if r]
    o = analyse(A.image, bg, intended, A.ratio, sheet=A.sheet, axis=A.axis)
    print(f"H={o['H']} margins={o['margins']}")
    for b in o['bands']:
        print(f"  band y{b['y0']}-{b['y1']} h={b['h']} ({b['pct']}%) ratio_to_largest_other={b['ratio']}{' intended' if b['intended'] else ''}{'  FAIL' if b['fail'] else ''}")
    for r in o['sparse']: print(f"  sparse rows y{r[0]}-{r[1]} ({r[2]}% of H, mean coverage {r[3]})  REVIEW")
    if 'dead_zone' in o: print(f"  largest empty region {o['dead_zone']}")
    print('RESULT', 'FAIL' if o['fail'] else 'PASS (review sparse rows and dead zone by eye)')
    sys.exit(1 if o['fail'] else 0)

"""ellipse.py: fit an ellipse in a region and check it (TD-ELL-1, -2, -3).

python3 ellipse.py IMG x0,y0,x1,y1 [--axis x1,y1,x2,y2] [--out overlay.png]
  ROI = a box around ONE ellipse (or the visible arc of it), full-size pixels.
  --axis = the form's centre line (cylinder axis, axle); the minor axis should lie along it.

Reports: degree (minor/major ratio), minor-axis angle and tilt of the major axis
(TD-ELL-1), angle to the axis line, fit residual, and an end check (TD-ELL-3): how
thick the shape is at 75% and 85% of the way to each end, against a true ellipse.
Pointed ("lemon") ends read thin, flattened (boxy) ends read thick.

Fit: RANSAC over every edge pixel in the box, keeping only ellipses that span
50-130% of the box width and lie inside the box (15% margin), so side lines,
hatching and a second ellipse in the box don't pull the fit. Test:
python3 tools/tests/ellipse_cases.py

Limits: the box still matters. Keep it tight around one ellipse; a loose box
round concentric rims can lock onto a different rim. Thick rims give two outlines;
it fits one of them. Half-visible ellipses (a cylinder's base) fit
less reliably: treat degree as approximate there. Generated images
are noisy: confirm the overlay by eye.
"""
import sys, math
import numpy as np, cv2

PT, FL = 0.93, 1.25
NEAR = 0.15           # end check looks at edge pixels within this share of the radius of the fit
MARGIN = 0.15         # a fitted ellipse may overrun the box by this share of its size   # end-check thresholds, set on the synthetic tests in tests/ellipse_cases.py

def _r(c, el):
    (cx, cy), (w, h), ang = el
    t = math.radians(ang); p = c - (cx, cy)
    u = p[:, 0] * math.cos(t) + p[:, 1] * math.sin(t); v = -p[:, 0] * math.sin(t) + p[:, 1] * math.cos(t)
    return np.sqrt((u / (w / 2)) ** 2 + (v / (h / 2)) ** 2) - 1

def end_check(u, v, deg):
    """TD-ELL-3. Thickness of the shape near each major-axis end, as a share of its full
    thickness, against a true ellipse: sqrt(1 - f^2) at f = 0.75, 0.85 of the half-length.
    A pointed ("lemon") end is thinner there; a flattened (boxy) end is thicker."""
    mid = np.abs(u) < 0.1 * np.abs(u).max()                 # full thickness at the middle
    if (mid & (v > 0)).sum() < 2 or (mid & (v < 0)).sum() < 2:
        print('end check: not enough points at the middle of the ellipse'); return
    T = v[mid].max() - v[mid].min()
    out = []
    for sgn in (1, -1):
        U = np.percentile(sgn * u, 99.5)
        rs = []
        for f in (0.75, 0.85):
            m = np.abs(sgn * u - f * U) < 0.03 * U
            if (m & (v > 0)).sum() < 2 or (m & (v < 0)).sum() < 2: break
            rs.append((v[m].max() - v[m].min()) / T / math.sqrt(1 - f * f))
        if len(rs) == 2: out.append(float(np.mean(rs)))
    if not out:
        print('end check: not enough points near the major-axis ends (arc only?)'); return
    lo, hi = min(out), max(out)
    verdict = 'pointed ends (lemon) -> TD-ELL-3 fail' if lo < PT else ('flattened ends -> TD-ELL-3 fail' if hi > FL else 'ends OK')
    print('end check: thickness near ends vs a true ellipse ' + ', '.join(f'{x:.2f}' for x in out)
          + f' (true ellipse ~1.0-1.15 with stroke width; < {PT} pointed, > {FL} flat) -> {verdict}')
    return out

def main(a):
    img, roi = a[0], [int(v) for v in a[1].split(',')]
    axis = [float(v) for v in a[a.index('--axis') + 1].split(',')] if '--axis' in a else None
    out = a[a.index('--out') + 1] if '--out' in a else None
    x0, y0, x1, y1 = roi
    g = cv2.imread(img, cv2.IMREAD_GRAYSCALE)[y0:y1, x0:x1]
    g = cv2.GaussianBlur(g, (5, 5), 0)
    e = cv2.Canny(g, 30, 90)
    W, H = x1 - x0, y1 - y0
    ys, xs = np.nonzero(e)
    P = np.stack([xs, ys], 1).astype(np.float32)          # every edge pixel in the box
    if len(P) < 20: print('no edges found; adjust the ROI'); return
    rng = np.random.default_rng(0)
    def ok(el):
        (ex, ey), (ew, eh), t = el       # size sane, and the whole ellipse inside the box
        t = math.radians(t); hx = math.hypot(ew / 2 * math.cos(t), eh / 2 * math.sin(t))
        hy = math.hypot(ew / 2 * math.sin(t), eh / 2 * math.cos(t)); mx, my = MARGIN * W, MARGIN * H
        return (0.5 * W <= max(ew, eh) <= 1.3 * W and min(ew, eh) > 4 and ex - hx > -mx and ex + hx < W + mx
                and ey - hy > -my and ey + hy < H + my)
    best = None                       # RANSAC: the ellipse most edge pixels sit on, so side
    for _ in range(400):              # lines, rims and hatching in the box don't pull the fit
        s = P[rng.choice(len(P), 6, replace=False)]
        try: el = cv2.fitEllipse(s)
        except cv2.error: continue
        if not ok(el): continue
        n = int((np.abs(_r(P, el)) < 0.04).sum())
        if best is None or n > best[0]: best = (n, el)
    if best is None: print('no elliptical edge found; adjust the ROI'); return
    el = best[1]
    for tol in (0.08, 0.05, 0.05):     # refit on the inliers
        c = P[np.abs(_r(P, el)) < tol]
        if len(c) < 20: break
        el = cv2.fitEllipse(c)
    c = P[np.abs(_r(P, el)) < 0.05]
    near = P[np.abs(_r(P, el)) < NEAR]  # end check uses everything near the fit, incl. points that stray
    (cx, cy), (w, h), ang = el
    a_, b_ = max(w, h) / 2, min(w, h) / 2
    maj = math.radians(ang if w >= h else ang + 90)   # major-axis direction, image coords
    mino = maj + math.pi / 2
    pts = c - (cx, cy)
    q = near - (cx, cy)
    uq = q[:, 0] * math.cos(maj) + q[:, 1] * math.sin(maj)
    vq = -q[:, 0] * math.sin(maj) + q[:, 1] * math.cos(maj)
    u = pts[:, 0] * math.cos(maj) + pts[:, 1] * math.sin(maj)
    v = -pts[:, 0] * math.sin(maj) + pts[:, 1] * math.cos(maj)
    r = np.sqrt((u / a_) ** 2 + (v / b_) ** 2) - 1          # 0 on the fit
    tilt = abs((math.degrees(maj) + 90) % 180 - 90)
    print(f'centre ({cx + x0:.0f}, {cy + y0:.0f})  axes {2*a_:.0f} x {2*b_:.0f} px  degree (minor/major) {b_/a_:.3f}')
    print(f'minor axis angle {math.degrees(mino) % 180:.1f} deg (90 = vertical); major axis tilted {tilt:.1f} deg from horizontal'
          + ('' if tilt < 3 or axis else ' -> TD-ELL-1: tilted ellipse; fine only if the form\'s axis is tilted the same way (pass --axis)'))
    print(f'fit residual: mean |r| {np.abs(r).mean():.3f} (fraction of radius), edge pixels on the fit {len(c)} of {len(P)}')
    end_check(uq, vq, b_ / a_)
    if axis:
        ax = math.atan2(axis[3] - axis[1], axis[2] - axis[0])
        d = abs((math.degrees(mino - ax) + 90) % 180 - 90)
        print(f'minor axis vs given axis: {d:.1f} deg off ' + ('(TD-ELL-1 ok, < 3 deg)' if d < 3 else '(TD-ELL-1: check)'))
    if out:
        im = cv2.imread(img)             # grey box = ROI, blue = edge pixels on the fit, red = fit
        cv2.rectangle(im, (x0, y0), (x1, y1), (200, 200, 200), 1)
        for px_, py_ in c.astype(int): im[py_ + y0, px_ + x0] = (255, 0, 0)
        cv2.ellipse(im, ((cx + x0, cy + y0), (w, h), ang), (0, 0, 255), 1)
        cv2.imwrite(out, im)

if __name__ == '__main__':
    if len(sys.argv) < 3: print(__doc__); sys.exit(1)
    main(sys.argv[1:])

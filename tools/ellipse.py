"""ellipse.py: fit an ellipse in a region and check it (TD-ELL-1, -2, -3).

python3 ellipse.py IMG x0,y0,x1,y1 [--axis x1,y1,x2,y2] [--out overlay.png]
  ROI = a box around ONE ellipse (or the visible arc of it), full-size pixels.
  --axis = the form's centre line (cylinder axis, axle); the minor axis should lie along it.

Reports: degree (minor/major ratio), minor-axis angle, angle to the axis line,
fit residual, and an end check: are the points at the major-axis ends further
out than the fit (pointed, "lemon") or further in (flat)?

Limits: picks the edge contour (spanning 60-130% of the ROI width) that an
ellipse fits best, so keep the ROI tight and
free of other strong edges (rims, rings, hatching). Thick rims give two
outlines; it fits one of them. Half-visible ellipses (a cylinder's base) fit
less reliably: treat degree as approximate there. Generated images
are noisy: confirm the overlay by eye.
"""
import sys, math
import numpy as np, cv2

def _resid(c, el):
    (cx, cy), (w, h), ang = el
    t = math.radians(ang); p = c.reshape(-1, 2).astype(float) - (cx, cy)
    u = p[:, 0] * math.cos(t) + p[:, 1] * math.sin(t); v = -p[:, 0] * math.sin(t) + p[:, 1] * math.cos(t)
    return float(np.abs(np.sqrt((u / (w / 2)) ** 2 + (v / (h / 2)) ** 2) - 1).mean())

def main(a):
    img, roi = a[0], [int(v) for v in a[1].split(',')]
    axis = [float(v) for v in a[a.index('--axis') + 1].split(',')] if '--axis' in a else None
    out = a[a.index('--out') + 1] if '--out' in a else None
    x0, y0, x1, y1 = roi
    g = cv2.imread(img, cv2.IMREAD_GRAYSCALE)[y0:y1, x0:x1]
    g = cv2.GaussianBlur(g, (5, 5), 0)
    e = cv2.Canny(g, 30, 90)
    cs, _ = cv2.findContours(e, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    W, H = x1 - x0, y1 - y0
    best = None
    for c in cs:                      # pick the contour an ellipse fits best,
        if len(c) < 40: continue      # among those spanning most of the ROI width
        el = cv2.fitEllipse(c)
        (ex, ey), (ew, eh), _ = el
        if max(ew, eh) < 0.6 * W or max(ew, eh) > 1.3 * W or not (0 <= ex <= W and 0 <= ey <= H): continue
        res = _resid(c, el)
        if best is None or res < best[0]: best = (res, c)
    if best is None: print('no elliptical contour found; adjust the ROI'); return
    c = best[1]
    (cx, cy), (w, h), ang = cv2.fitEllipse(c)
    a_, b_ = max(w, h) / 2, min(w, h) / 2
    # direction of the major axis in image coords
    maj = math.radians(ang if w >= h else ang + 90)
    mino = maj + math.pi / 2
    pts = c.reshape(-1, 2).astype(float) - (cx, cy)
    u = pts[:, 0] * math.cos(maj) + pts[:, 1] * math.sin(maj)
    v = -pts[:, 0] * math.sin(maj) + pts[:, 1] * math.cos(maj)
    r = np.sqrt((u / a_) ** 2 + (v / b_) ** 2) - 1          # 0 on the fit
    t = np.degrees(np.arctan2(v / b_, u / a_))
    ends = (np.abs(t) < 20) | (np.abs(t) > 160)
    print(f'centre ({cx + x0:.0f}, {cy + y0:.0f})  axes {2*a_:.0f} x {2*b_:.0f} px  degree (minor/major) {b_/a_:.3f}')
    print(f'minor axis angle {math.degrees(mino) % 180:.1f} deg (90 = vertical)')
    print(f'fit residual: mean |r| {np.abs(r).mean():.3f} (fraction of radius), points used {len(c)}')
    if ends.sum() >= 5:
        de = r[ends].mean() - r[~ends].mean()
        verdict = 'pointed ends?' if de > 0.03 else ('flat ends?' if de < -0.03 else 'ends OK')
        print(f'end check: ends sit {de:+.3f} vs the rest -> {verdict}')
    else:
        print('end check: not enough points near the major-axis ends (arc only?)')
    if axis:
        ax = math.atan2(axis[3] - axis[1], axis[2] - axis[0])
        d = abs((math.degrees(mino - ax) + 90) % 180 - 90)
        print(f'minor axis vs given axis: {d:.1f} deg off ' + ('(TD-ELL-1 ok, < 3 deg)' if d < 3 else '(TD-ELL-1: check)'))
    if out:
        im = cv2.imread(img)
        cv2.rectangle(im, (x0, y0), (x1, y1), (200, 200, 200), 1)
        cv2.drawContours(im, [c + (x0, y0)], -1, (255, 0, 0), 1)
        cv2.ellipse(im, ((cx + x0, cy + y0), (w, h), ang), (0, 0, 255), 2)
        cv2.imwrite(out, im)

if __name__ == '__main__':
    if len(sys.argv) < 3: print(__doc__); sys.exit(1)
    main(sys.argv[1:])

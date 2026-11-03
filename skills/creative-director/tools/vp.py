"""vp.py: least-squares vanishing points and horizon check (TD-PER-1, TD-PER-3).

Fit:    python3 vp.py fit SEGMENTS.csv [--image IMG --out overlay.png]
        CSV rows: group,x1,y1,x2,y2  (pixel coords of the full-size image)
        group = any name for one family of parallel edges (e.g. L, R);
        group "v" = edges meant to be vertical (reports their tilt, no VP).
Detect: python3 vp.py detect IMG OUT.png [--min-len 60]
        Finds long straight segments (OpenCV LSD or Hough) and draws them numbered,
        printing a CSV you can sort into groups. Detection does NOT group edges
        into families; a person or bot does that by eye.

Limits: 2+ segments per group (3+ gives a residual). Hand-drawn and generated
edges wobble, so endpoints matter; take them at zoom. Near-parallel edges put
the VP far away and make its position unstable: read the "spread" figure.
"""
import sys, csv, math
import numpy as np

def line_eq(x1, y1, x2, y2):
    a, b = y2 - y1, x1 - x2
    n = math.hypot(a, b)
    return a / n, b / n, (a * x1 + b * y1) / n

def fit_vp(segs):
    A = np.array([line_eq(*s)[:2] for s in segs]); c = np.array([line_eq(*s)[2] for s in segs])
    vp, *_ = np.linalg.lstsq(A, c, rcond=None)
    res = A @ vp - c                      # perpendicular distance of each line from the VP
    return vp, res

def fit(path, image=None, out=None):
    groups = {}
    for row in csv.reader(open(path)):
        if not row or row[0].startswith('#'): continue
        groups.setdefault(row[0].strip(), []).append(tuple(map(float, row[1:5])))
    vps = {}
    for g, segs in groups.items():
        if g == 'v':
            for s in segs:
                ang = math.degrees(math.atan2(s[2] - s[0], s[3] - s[1]))
                ang = (ang + 90) % 180 - 90
                print(f'vertical {s}: tilt {ang:+.2f} deg from vertical')
            continue
        if len(segs) < 2: print(f'{g}: need 2+ segments'); continue
        vp, res = fit_vp(segs)
        # spread: how far the VP moves if each line is dropped in turn (stability)
        spread = 0.0
        if len(segs) >= 3:
            alt = [fit_vp(segs[:i] + segs[i+1:])[0] for i in range(len(segs))]
            spread = max(np.hypot(*(a - vp)) for a in alt)
        vps[g] = vp
        print(f'{g}: VP ({vp[0]:.0f}, {vp[1]:.0f})  max line miss {np.abs(res).max():.1f}px  spread {spread:.0f}px  n={len(segs)}')
    names = list(vps)
    if len(names) >= 2:
        (x1, y1), (x2, y2) = vps[names[0]], vps[names[1]]
        tilt = math.degrees(math.atan2(y2 - y1, x2 - x1))
        tilt = (tilt + 90) % 180 - 90
        print(f'horizon {names[0]}-{names[1]}: tilt {tilt:+.2f} deg, VP height mismatch {abs(y2 - y1):.0f}px over {abs(x2 - x1):.0f}px')
        print('TD-PER-1:', 'consistent (tilt < 1.5 deg)' if abs(tilt) < 1.5 else 'NOT consistent (tilt >= 1.5 deg) - confirm by eye')
    if image and out:
        import cv2
        im = cv2.imread(image)
        for g, segs in groups.items():
            for s in segs:
                p, q = (int(s[0]), int(s[1])), (int(s[2]), int(s[3]))
                cv2.line(im, p, q, (0, 0, 255), 2)
                if g in vps:  # extend toward the VP
                    cv2.line(im, q, tuple(int(v) for v in np.clip(vps[g], -1e5, 1e5)), (0, 160, 255), 1)
        cv2.imwrite(out, im)

def detect(image, out, min_len=60):
    import cv2
    g = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    g = cv2.GaussianBlur(g, (5, 5), 0)
    segs = []
    try:
        lsd = cv2.createLineSegmentDetector()
        segs = [np.ravel(l)[:4] for l in lsd.detect(g)[0]]
    except Exception:
        e = cv2.Canny(g, 40, 120)
        h = cv2.HoughLinesP(e, 1, np.pi / 360, 60, minLineLength=min_len, maxLineGap=6)
        segs = [np.ravel(l)[:4] for l in (h if h is not None else [])]
    segs = [s for s in segs if math.hypot(s[2] - s[0], s[3] - s[1]) >= min_len]
    segs.sort(key=lambda s: -math.hypot(s[2] - s[0], s[3] - s[1]))
    im = cv2.cvtColor(g, cv2.COLOR_GRAY2BGR)
    print('# id: group,x1,y1,x2,y2  (replace "?" with a group name; delete rows you don\'t want)')
    for i, s in enumerate(segs[:40]):
        x1, y1, x2, y2 = map(int, s)
        cv2.line(im, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(im, str(i), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        print(f'?,{x1},{y1},{x2},{y2}  # {i}')
    cv2.imwrite(out, im)

if __name__ == '__main__':
    a = sys.argv[1:]
    if not a or a[0] not in ('fit', 'detect'): print(__doc__); sys.exit(1)
    if a[0] == 'fit':
        img = a[a.index('--image') + 1] if '--image' in a else None
        out = a[a.index('--out') + 1] if '--out' in a else None
        fit(a[1], img, out)
    else:
        ml = int(a[a.index('--min-len') + 1]) if '--min-len' in a else 60
        detect(a[1], a[2], ml)

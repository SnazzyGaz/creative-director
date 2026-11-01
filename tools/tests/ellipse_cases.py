"""ellipse_cases.py: synthetic good and bad ellipses for tools/ellipse.py.
python3 tools/tests/ellipse_cases.py   (writes images to a temp folder, prints pass/fail)

Good: true ellipses, degrees 0.15-0.9, stroke 2-6 px, some with a cylinder's side
lines and a second ellipse touching the box. Bad: pointed ("lemon") ends, flattened
(superellipse) ends, and a tilted ellipse on an upright axis."""
import sys, os, math, io, tempfile, contextlib, subprocess
import numpy as np, cv2
HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, '..', 'ellipse.py')

def shape(a, b, kind='ellipse', p=2.0, rot=0, n=720):
    t = np.linspace(0, 2 * np.pi, n, endpoint=False)
    x = a * np.cos(t)
    if kind == 'ellipse': y = b * np.sin(t)
    elif kind == 'lemon': y = b * np.sign(np.sin(t)) * np.abs(np.sin(t)) ** p            # pointed tips
    elif kind == 'super':                                                                 # boxy ends
        x = a * np.sign(np.cos(t)) * np.abs(np.cos(t)) ** (2 / p); y = b * np.sign(np.sin(t)) * np.abs(np.sin(t)) ** (2 / p)
    r = math.radians(rot)
    return np.stack([x * math.cos(r) - y * math.sin(r), x * math.sin(r) + y * math.cos(r)], 1)

def draw(path, pts, stroke=4, sides=0, extra=False):
    im = np.full((400, 500), 255, np.uint8); c = np.array([250, 160])
    q = (pts + c).astype(np.int32)
    cv2.polylines(im, [q], True, 20, stroke, cv2.LINE_AA)
    if sides:                         # cylinder sides from the ellipse's left/right ends
        l, r = q[q[:, 0].argmin()], q[q[:, 0].argmax()]
        cv2.line(im, tuple(map(int, l)), (int(l[0]), int(l[1]) + sides), 20, stroke, cv2.LINE_AA)
        cv2.line(im, tuple(map(int, r)), (int(r[0]), int(r[1]) + sides), 20, stroke, cv2.LINE_AA)
    if extra: cv2.ellipse(im, (250, 330), (120, 30), 0, 0, 180, 20, stroke, cv2.LINE_AA)
    cv2.imwrite(path, im)
    x0, y0 = q.min(0) - 12; x1, y1 = q.max(0) + 12
    return f'{x0},{y0},{x1},{y1}'

def run(img, roi, axis=None):
    a = [sys.executable, TOOL, img, roi] + (['--axis', axis] if axis else [])
    return subprocess.run(a, capture_output=True, text=True).stdout

CASES = []  # (name, points, draw kwargs, expected: 'ok' | 'pointed' | 'flat' | 'tilt')
for d in (0.15, 0.3, 0.5, 0.7, 0.9):
    for s in (2, 4, 6):
        CASES.append((f'good deg {d} stroke {s}', shape(150, 150 * d), dict(stroke=s), 'ok'))
CASES += [('good deg 0.3 + side lines', shape(150, 45), dict(sides=150), 'ok'),
          ('good deg 0.5 + side lines', shape(150, 75), dict(sides=120), 'ok'),
          ('good rotated 25 deg, axis given', shape(150, 50, rot=25), dict(), 'ok-axis'),
          ('good deg 0.3, base arc below box', shape(150, 45), dict(sides=150, extra=True), 'ok')]
for d in (0.25, 0.4, 0.6):
    for p in (1.5, 2.0):
        CASES.append((f'lemon deg {d} p {p}', shape(150, 150 * d, 'lemon', p), dict(), 'pointed'))
CASES += [('lemon deg 0.35 + side lines, rot 12', shape(95 * 1.5, 34 * 1.5, 'lemon', 2.0, rot=12), dict(sides=150), 'pointed')]
for d in (0.3, 0.6):
    for p in (3.0, 4.0):
        CASES.append((f'flattened deg {d} n {p}', shape(150, 150 * d, 'super', p), dict(), 'flat'))
CASES += [('tilted 10 deg on upright axis', shape(150, 45, rot=10), dict(), 'tilt'),
          ('tilted 5 deg on upright axis', shape(150, 45, rot=5), dict(), 'tilt')]

REAL = [  # (name, image under examples/, ROI, expected)
    ('takeover r01 tin top (planted lemon)', 'technical-drawing-takeover/round-01.png', '455,170,672,280', 'pointed'),
    ('takeover r02 tin top (constructed)', 'technical-drawing-takeover/round-02.png', '455,170,672,280', 'ok'),
    ('still-life r01 can top (generated)', 'technical-drawing-still-life/round-01.png', '680,230,1020,370', 'ok'),
    ('still-life r02 can top (generated)', 'technical-drawing-still-life/round-02.png', '700,240,980,340', 'ok')]

def verdict(out, want):
    end = 'pointed' if 'pointed ends' in out else 'flat' if 'flattened ends' in out else 'ok' if 'ends OK' in out else '?'
    if want == 'tilt': return 'TD-ELL-1: check' in out
    if want == 'ok-axis': return end == 'ok' and 'TD-ELL-1 ok' in out
    return end == want

if __name__ == '__main__':
    tmp = tempfile.mkdtemp(); npass = 0
    for i, (name, pts, kw, want) in enumerate(CASES):
        p = os.path.join(tmp, f'case{i:02d}.png'); roi = draw(p, pts, **kw)
        axis = None
        if want == 'ok-axis': axis = f'{250 - 100 * math.sin(math.radians(25)):.0f},{160 + 100 * math.cos(math.radians(25)):.0f},250,160'
        if want == 'tilt': axis = '250,100,250,300'
        out = run(p, roi, axis); ok = verdict(out, want); npass += ok
        endl = [l for l in out.splitlines() if l.startswith('end check') or 'given axis' in l]
        print(f"{'PASS' if ok else 'FAIL'}  {name:40s} want {want:8s} | {' | '.join(endl)}")
    print(f'\nsynthetic: {npass}/{len(CASES)} passed')
    ex = os.path.join(HERE, '..', '..', 'examples'); rpass = 0
    for name, img, roi, want in REAL:
        out = run(os.path.join(ex, img), roi); ok = verdict(out, want); rpass += ok
        endl = [l.split(' (true')[0] for l in out.splitlines() if l.startswith('end check')]
        print(f"{'PASS' if ok else 'FAIL'}  {name:40s} want {want:8s} | {' | '.join(endl)}")
    print(f'examples: {rpass}/{len(REAL)} passed')
    sys.exit(0 if npass == len(CASES) and rpass == len(REAL) else 1)

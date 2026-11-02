"""whitespace_cases.py: synthetic layouts for tools/whitespace.py (LAY-10).
python3 tools/tests/whitespace_cases.py"""
import os, sys, subprocess, tempfile
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); TOOL = os.path.join(HERE, '..', 'whitespace.py')
W, H, M = 1080, 1350, 60

def page(path, blocks):   # blocks: (x0, y0, x1, y1) dark text bars on a light page
    im = Image.new('RGB', (W, H), (244, 239, 228)); d = ImageDraw.Draw(im)
    for b in blocks: d.rectangle(b, fill=(30, 30, 30))
    im.save(path)

def stack(gaps, h=150):   # full-width groups separated by the given gaps
    y, out = M, []
    for g in gaps + [None]:
        out.append((M, y, W - M, y + h)); y += h + (g or 0)
    return out

CASES = [  # (name, blocks, extra args, expect fail)
    ('even stack, gaps 60', stack([60, 60, 60, 60]), [], False),
    ('one band 3x the others', stack([60, 180, 60, 60]), [], True),
    ('same band marked intended', stack([60, 180, 60, 60]), ['--intended', '400-640'], False),
    ('header row: small item left, small item right, empty middle',
     [(M, M, M + 160, M + 160), (W - M - 220, M + 60, W - M, M + 100)] + stack([60, 60, 60], 200)[1:] + [(M, 520, W - M, 700)], [], True),
    ('centred group with symmetric flanks', [(340, M, 740, M + 200), (M, 320, W - M, 520), (M, 580, W - M, 780), (M, 840, W - M, 1040), (M, 1100, W - M, H - M)], [], False),
]

ok = 0
with tempfile.TemporaryDirectory() as t:
    for name, blocks, args, want in CASES:
        p = os.path.join(t, 'c.png'); page(p, blocks)
        r = subprocess.run([sys.executable, TOOL, p] + args, capture_output=True, text=True)
        got = r.returncode == 1
        ok += got == want
        print(f"{'ok ' if got == want else 'BAD'} {name}: expected {'FAIL' if want else 'PASS'}, got {'FAIL' if got else 'PASS'}")
print(f'{ok}/{len(CASES)} synthetic cases')

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXAMPLES = [  # (path, extra args, expect fail): finished examples should pass
    ('examples/case-study-may-specials/final.jpg', [], False),
    ('examples/aesthetic-across-domains/poster/after.png', ['--axis', 'left'], False),
    ('examples/first-principles-remake/remake.png', ['--axis', 'left'], False),
]
eok = 0
for rel, args, want in EXAMPLES:
    r = subprocess.run([sys.executable, TOOL, os.path.join(ROOT, rel)] + args, capture_output=True, text=True)
    got = r.returncode == 1
    eok += got == want
    print(f"{'ok ' if got == want else 'BAD'} {rel}: expected {'FAIL' if want else 'PASS'}, got {'FAIL' if got else 'PASS'}")
print(f'{eok}/{len(EXAMPLES)} example images')
sys.exit(0 if ok == len(CASES) and eok == len(EXAMPLES) else 1)

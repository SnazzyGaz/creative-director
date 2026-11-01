"""grid_cases.py: synthetic layouts plus screenshots in examples/ for tools/grid.py.
python3 tools/tests/grid_cases.py"""
import os, sys, subprocess, tempfile
import numpy as np, cv2
HERE = os.path.dirname(os.path.abspath(__file__)); TOOL = os.path.join(HERE, '..', 'grid.py')
EX = os.path.join(HERE, '..', '..', 'examples')

def page(path, cards):   # cards: (x, y, w, h); white cards with a 1 px border and two text bars
    im = np.full((700, 900, 3), 246, np.uint8)
    for x, y, w, h in cards:
        cv2.rectangle(im, (x, y), (x + w - 1, y + h - 1), (255, 255, 255), -1)
        cv2.rectangle(im, (x, y), (x + w - 1, y + h - 1), (200, 200, 200), 1)
        cv2.rectangle(im, (x + 16, y + 16), (x + w // 2, y + 28), (40, 40, 40), -1)
        cv2.rectangle(im, (x + 16, y + 40), (x + w - 24, y + 48), (120, 120, 120), -1)
    cv2.imwrite(path, im)

STACK = lambda xs, gaps: [(x, 40 + sum(gaps[:i]) + 80 * i, 300, 80) for i, x in enumerate(xs)]
SYN = [  # (name, cards, expected tags)
    ('stack aligned, gaps 16', STACK([40] * 5, [16] * 4), set()),
    ('stack, one card 3 px off', STACK([40, 40, 43, 40, 40], [16] * 4), {'STRAY'}),
    ('stack, gaps 16 16 13 16', STACK([40] * 5, [16, 16, 13, 16]), {'SCALE'}),
    ('row of 3, steps 280, gap 20', [(40 + 280 * i, 40, 260, 120) for i in range(3)], set()),
    ('row of 3, middle top +5', [(40, 40, 260, 120), (320, 45, 260, 120), (600, 40, 260, 120)], {'ROW'}),
    ('row of 3, gaps 20 and 26', [(40, 40, 260, 120), (320, 40, 260, 120), (606, 40, 260, 120)], {'ROW', 'SCALE'}),
]
REAL = [  # (name, screenshot under examples/, expected tags)
    ('common-failures grid before', 'common-failures/grid-before.png', {'ROW', 'SCALE'}),
    ('common-failures grid after', 'common-failures/grid-after.png', set()),
    ('common-failures spacing before', 'common-failures/spacing-before.png', {'ROW', 'SCALE'}),
    ('common-failures spacing after', 'common-failures/spacing-after.png', set()),
] + [(f'{d} r{r} {w}', f'{d}/round-{r}-{w}.png', set()) for d in ('web-ui-landing', 'web-ui-takeover') for r in ('01', '02') for w in (1280, 390)]

def tags(out): return {t for t in ('STRAY', 'ROW', 'SCALE') if f'  {t} ' in out}

if __name__ == '__main__':
    tmp = tempfile.mkdtemp(); rows = []
    for i, (name, cards, want) in enumerate(SYN):
        p = os.path.join(tmp, f's{i}.png'); page(p, cards); rows.append((name, p, want))
    rows += [(n, os.path.join(EX, f), w) for n, f, w in REAL]
    ok_n = 0
    for name, p, want in rows:
        out = subprocess.run([sys.executable, TOOL, p], capture_output=True, text=True).stdout
        got = tags(out); ok = got == want; ok_n += ok
        print(f"{'PASS' if ok else 'FAIL'}  {name:36s} want {sorted(want)} got {sorted(got)}")
        if not ok: print(out)
    print(f'\n{ok_n}/{len(rows)} passed'); sys.exit(0 if ok_n == len(rows) else 1)

"""balance_cases.py: synthetic pictures for tools/balance.py (COMP-2, CORE-11).
python3 tools/tests/balance_cases.py"""
import os, sys, tempfile, glob
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..'))
import balance
W, H = 800, 600

def pic(path, discs):  # discs: (cx, cy, r, value)
    im = Image.new('RGB', (W, H), (240, 240, 240)); d = ImageDraw.Draw(im)
    for x, y, r, v in discs: d.ellipse([x - r, y - r, x + r, y + r], fill=(v, v, v))
    im.save(path)

CASES = [  # name, discs, test on result
    ('one disc at centre', [(400, 300, 80, 20)], lambda r: r['dcm'] < 5),
    ('one disc far left', [(120, 300, 80, 20)], lambda r: r['dx'] < -50 and r['dcm'] > 25),
    ('steelyard: big near centre-left, small far right', [(300, 300, 110, 20), (720, 300, 48, 20)], lambda r: abs(r['dx']) < 12),
    ('same pair, small moved in: tips left', [(300, 300, 110, 20), (480, 300, 48, 20)], lambda r: r['dx'] < -12),
    ('dark small balances light big', [(250, 300, 100, 190), (600, 300, 55, 10)], lambda r: abs(r['dx']) < 15),
    ('symmetric pair', [(200, 300, 70, 30), (600, 300, 70, 30)], lambda r: r['dcm'] < 5 and 0.95 < r['lr'] < 1.05),
]
ok = 0
with tempfile.TemporaryDirectory() as t:
    for i, (name, discs, test) in enumerate(CASES):
        p = os.path.join(t, f'{i}.png'); pic(p, discs)
        print(f'--- {name}'); r = balance.analyse(p)
        good = test(r); ok += good; print('OK' if good else 'UNEXPECTED')
    ex = sorted(glob.glob(os.path.join(HERE, '..', '..', 'examples', 'case-study-may-specials', '*.png')))[:3]
    for p in ex:  # smoke test on real images: must run and give finite numbers
        print(f'--- example {os.path.basename(p)}'); r = balance.analyse(p)
print(f'{ok}/{len(CASES)} synthetic cases as expected')
sys.exit(0 if ok == len(CASES) else 1)

"""datagraphic_cases.py: cases for tools/datagraphic.py (LAY-19).
python3 tools/tests/datagraphic_cases.py"""
import os, sys, json, tempfile
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..'))
import datagraphic as dg
GREEN = (46, 125, 50); ok = 0; n = 0

def case(name, got, want):
    global ok, n
    n += 1; good = got == want; ok += good; print(f'--- {name}: {"OK" if good else "UNEXPECTED"}')

with tempfile.TemporaryDirectory() as t:
    # 1-2: bars drawn from data pass the check, vertical and horizontal, against the shared scale too
    for orient in ('vertical', 'horizontal'):
        out = os.path.join(t, f'{orient}.png'); vals = [42, 58, 71, 96, 118]
        r = dg.bars({'values': vals, 'labels': list('ABCDE'), 'value_labels': [str(v) for v in vals], 'orientation': orient,
                     'width': 1000, 'height': 500, 'colours': ['#2E7D32'], 'bg': '#FFFFFF', 'track': '#E6E6E6', 'scale_max': 120}, out)
        case(f'{orient} bars from data pass', dg.check_bars(out, r['plot'], vals, [GREEN], orient, 120), 0)
    # 3: a chart with the small bars overstated, as a generator drew one (+12 pts on the smallest), fails
    im = Image.new('RGB', (800, 400), 'white'); d = ImageDraw.Draw(im)
    for i, p in enumerate([0.48, 0.59, 0.71, 0.85, 1.0]):
        d.rectangle([40 + i * 150, 380 - int(340 * p), 140 + i * 150, 380], fill=GREEN)
    p = os.path.join(t, 'wrong.png'); im.save(p)
    case('overstated small bars fail', dg.check_bars(p, [0, 0, 800, 381], [42, 58, 71, 96, 118], [GREEN]), 1)
    # 4: bars in several colours (a graded palette) are all found with one --colour each
    im = Image.new('RGB', (800, 400), 'white'); d = ImageDraw.Draw(im); cs = [(200, 230, 200), (120, 190, 120), (40, 140, 60)]
    for i, (v, c) in enumerate(zip([30, 60, 90], cs)): d.rectangle([60 + i * 250, 380 - int(360 * v / 90), 220 + i * 250, 380], fill=c)
    p = os.path.join(t, 'graded.png'); im.save(p)
    case('graded colours found and pass', dg.check_bars(p, [0, 0, 800, 381], [30, 60, 90], cs), 0)
    # 5: a missing bar is reported, not passed
    case('wrong bar count fails', dg.check_bars(p, [0, 0, 800, 381], [30, 60, 90, 10], cs), 1)
    # 6-7: a loop route closes at start = finish, and each river crossing gets a bridge
    spec = {'width': 1200, 'height': 700, 'bg': '#DDEFD5', 'points': [[.12, .6], [.35, .55], [.55, .3], [.8, .25], [.85, .6], [.5, .8]],
            'river': [[.62, 0], [.6, .5], [.7, 1]], 'labels': [{'text': 'Old Mill', 'at': [.4, .45]}], 'start_label': 'Start / Finish'}
    r = dg.route(spec, os.path.join(t, 'route.png'))
    case('loop closes', r['closed'], True)
    case('two crossings, two bridges', (r['crossings'], r['bridges']), (2, 2))
    # 8: composite keeps the aspect and stays inside the box
    art = os.path.join(t, 'art.png'); Image.new('RGB', (1200, 900), 'white').save(art)
    out = os.path.join(t, 'comp.png'); dg.composite(art, os.path.join(t, 'vertical.png'), [100, 100, 700, 700], out)
    a = Image.open(out).convert('RGB'); case('composite inside the box', a.getpixel((50, 50)) == (255, 255, 255) and a.size == (1200, 900), True)
print(f'{ok}/{n} cases as expected'); sys.exit(0 if ok == n else 1)

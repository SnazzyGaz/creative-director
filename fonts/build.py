"""Render the font library's specimen sheets and catalogue table from catalogue.json.
Run from the repo root: python3 fonts/build.py   (needs Pillow with libraqm or basic layout; no network)
Writes fonts/specimens/<theme>.png, fonts/specimens/overview.png and the table in fonts/CATALOGUE.md."""
import json, os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAT = json.load(open(os.path.join(ROOT, 'fonts', 'catalogue.json'), encoding='utf-8'))
OUT = os.path.join(ROOT, 'fonts', 'specimens')
INK, PAPER, MUTED, RULE = (28, 27, 31), (247, 244, 238), (110, 106, 100), (214, 208, 198)
# Labels use one neutral face so the samples are the only thing that varies.
LABEL = os.path.join(ROOT, 'fonts/grotesk-neutral/publicsans/PublicSans[wght].ttf')
SAMPLE = {
    'editorial-serif': 'The Quiet Season', 'pulp-retro-comic': 'Attack of the Giant Tuna!',
    'noir-thriller': 'Nobody Leaves the Docks', 'horror': 'Something in the Cellar',
    'scifi-tech': 'Orbit Station Nine', 'fantasy-medieval': 'The Crown of Ash',
    'childrens-playful': 'Pip and the Big Jump', 'romance-script': 'Forever in Lisbon',
    'western-slab': 'Dust Creek Saloon', 'art-deco-display': 'The Starlight Ballroom',
    'grotesk-neutral': 'Settings and Billing', 'geometric-sans': 'Form Follows Function',
    'humanist-sans': 'Clear Paths for Everyone', 'monospace-code': 'git commit -m "fix"',
    'condensed-poster': 'LIVE AT THE ARENA', 'handwritten-marker': 'Back in five minutes',
    'nautical-vintage': 'The Salt Road Voyage', 'luxury-didone': 'Maison Lumière',
}
PANGRAM = 'The quick brown fox jumps over the lazy dog 0123456789'

def path_of(f):
    files = [x for x in f['files'] if 'Italic' not in x] or f['files']
    pref = [x for x in files if '[' in x or 'Variable' in x] or [x for x in files if 'Regular' in x] or files
    return os.path.join(ROOT, f['path'], pref[0])

def font(f, size, wght=None):
    ft = ImageFont.truetype(path_of(f), size)
    if 'wght' in f['axes']:
        try:
            axes = ft.get_variation_axes()
            vals = [a['default'] for a in axes]
            names = [a['name'].decode() if isinstance(a['name'], bytes) else str(a['name']) for a in axes]
            for i, a in enumerate(axes):
                if names[i].lower().startswith('weight') and wght is not None:
                    vals[i] = max(a['minimum'], min(a['maximum'], wght))
                elif names[i].lower().startswith('weight'):
                    vals[i] = max(a['minimum'], min(a['maximum'], 400))
                elif names[i].lower().startswith('optical'):
                    vals[i] = max(a['minimum'], min(a['maximum'], size * 0.75))
            ft.set_variation_by_axes(vals)
        except Exception:
            pass
    return ft

def label(size, w=500):
    ft = ImageFont.truetype(LABEL, size)
    try: ft.set_variation_by_axes([w])
    except Exception: pass
    return ft

def fit(f, text, size, maxw, wght=None):
    while size > 14:
        ft = font(f, size, wght)
        if ft.getlength(text) <= maxw: return ft
        size -= 2
    return font(f, size, wght)

def axes_text(f):
    if f['axes']: return 'Variable: ' + ', '.join(f"{k} {v[0]:g}-{v[1]:g}" for k, v in f['axes'].items())
    return 'Static weights: ' + ', '.join(str(w) for w in f['static_weights'])

def theme_sheet(theme, fams):
    W, pad, row = 1600, 56, 236
    H = 150 + row * len(fams) + 40
    im = Image.new('RGB', (W, H), PAPER); d = ImageDraw.Draw(im)
    d.text((pad, 44), theme['name'], font=label(44, 700), fill=INK)
    d.text((pad, 100), theme['use'], font=label(22), fill=MUTED)
    y = 150
    for f in fams:
        d.line([(pad, y), (W - pad, y)], fill=RULE, width=2)
        d.text((pad, y + 16), f['family'], font=label(22, 700), fill=INK)
        meta = f"{f['licence']}  ·  {f['designer']}  ·  {axes_text(f)}"
        d.text((pad + 330, y + 18), meta, font=label(18), fill=MUTED)
        d.text((pad, y + 58), SAMPLE[theme['id']], font=fit(f, SAMPLE[theme['id']], 84, W - 2 * pad), fill=INK)
        if 'wght' in f['axes']:
            lo, hi = f['axes']['wght']; x = pad
            for wv in (lo, (lo + hi) / 2, hi):
                ft = font(f, 26, wv); t = f'{wv:g} Weight'
                d.text((x, y + 172), t, font=ft, fill=INK); x += ft.getlength(t) + 36
            d.text((x, y + 178), PANGRAM[:44], font=fit(f, PANGRAM[:44], 22, W - pad - x), fill=MUTED)
        else:
            d.text((pad, y + 172), PANGRAM, font=fit(f, PANGRAM, 26, W - 2 * pad), fill=MUTED)
        y += row
    return im

def overview(themes, by_theme):
    cols, cw, ch, pad = 4, 420, 92, 40
    rows = sum(-(-len(by_theme[t['id']]) // cols) for t in themes)
    H = 120 + rows * ch + len(themes) * 46 + 40
    W = pad * 2 + cols * cw
    im = Image.new('RGB', (W, H), PAPER); d = ImageDraw.Draw(im)
    d.text((pad, 36), 'creative-director font library: every family, in its own face', font=label(34, 700), fill=INK)
    y = 110
    for t in themes:
        d.text((pad, y), t['name'].upper(), font=label(18, 700), fill=MUTED); y += 34
        for i, f in enumerate(by_theme[t['id']]):
            c, r = i % cols, i // cols
            x = pad + c * cw; yy = y + r * ch
            d.text((x, yy), f['family'], font=fit(f, f['family'], 46, cw - 24), fill=INK)
            d.text((x, yy + 60), f['licence'], font=label(14), fill=MUTED)
        y += -(-len(by_theme[t['id']]) // cols) * ch + 12
    return im

def table(themes, by_theme):
    lines = []
    for t in themes:
        lines.append(f"\n### {t['name']}\n\n{t['use']} Specimen: [`specimens/{t['id']}.png`](specimens/{t['id']}.png)\n")
        lines.append('| Family | Licence | Axes / weights | Good for | Avoid | Pairs with |')
        lines.append('|---|---|---|---|---|---|')
        for f in by_theme[t['id']]:
            also = [x for x in f['themes'] if x != t['id']]
            fam = f"[{f['family']}]({f['source']})" + (f"<br><sub>also: {', '.join(also)}</sub>" if also else '')
            lic = f"[{f['licence']}](../{f['licence_file']})"
            lines.append(f"| {fam} | {lic} | {axes_text(f)} | {f['good_for']} | {f['avoid']} | {', '.join(f['pairs_with'])} |")
        also = [f['family'] for f in CAT['families'] if t['id'] in f['themes'][1:]]
        if also:
            lines.append(f"\nAlso suits this theme (listed under another): {', '.join(also)}.")
    return '\n'.join(lines) + '\n'

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    themes = CAT['themes']
    by_theme = {t['id']: [f for f in CAT['families'] if f['themes'][0] == t['id']] for t in themes}
    for t in themes:
        theme_sheet(t, by_theme[t['id']]).save(os.path.join(OUT, t['id'] + '.png'), optimize=True)
    overview(themes, by_theme).save(os.path.join(OUT, 'overview.png'), optimize=True)
    md = os.path.join(ROOT, 'fonts', 'CATALOGUE.md')
    head = open(md, encoding='utf-8').read().split('<!-- table -->')[0] if os.path.exists(md) else '# Font catalogue\n\n'
    open(md, 'w', encoding='utf-8').write(head + '<!-- table -->\n' + table(themes, by_theme))
    print('families:', len(CAT['families']), {t['id']: len(by_theme[t['id']]) for t in themes})

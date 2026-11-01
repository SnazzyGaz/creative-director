#!/usr/bin/env python3
"""Build the README images: banner, before/after strip, loop diagram (light + dark).
Run from the repo root: python3 docs/assets/src/build.py   (needs google-chrome and Pillow; banner fonts are in src/fonts/)"""
import os, subprocess, pathlib
from PIL import Image
ROOT = pathlib.Path(__file__).resolve().parents[3]
OUT = ROOT / "docs/assets"; SRC = OUT / "src"
THEMES = {
  "light": dict(bg="#F4F1EA", ink="#1D1B18", mute="#6A645B", faint="#CFC8BB", accent="#A3472B"),
  "dark":  dict(bg="#161514", ink="#EEE9DF", mute="#A39C91", faint="#3E3A35", accent="#D9825F"),
}
FONTS = "font-family:'Inter',sans-serif;"
# Banner type: Fraunces (display, opsz 144, soft) over Instrument Sans. Both OFL 1.1, vendored in src/fonts/
# and loaded from file so the variable axes (opsz, SOFT) apply.
FACES = ("@font-face{font-family:'CD Fraunces';src:url('fonts/Fraunces-VariableFont_SOFT,WONK,opsz,wght.ttf');font-weight:100 900}"
         "@font-face{font-family:'CD Instrument Sans';src:url('fonts/InstrumentSans-VariableFont_wdth,wght.ttf');font-weight:400 700}")
def shot(html, name, w, h):
    p = SRC / f"_{name}.html"; p.write_text(html)
    out = OUT / f"{name}.png"
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
        f"--window-size={w},{h}", "--force-device-scale-factor=2", f"--screenshot={out}", f"file://{p}"],
        check=True, capture_output=True)
    p.unlink(); return out

def banner(t):
    c = THEMES[t]
    # two-point box under a horizon (we look down on it), plus a cylinder: a quiet nod to the rules
    hy, vl, vr = 112, (560, 112), (1640, 112)
    fx, ft, fb = 905, 196, 318          # front vertical edge
    def on(p, v, x):                     # point on line p->v at given x
        return (x, p[1] + (v[1]-p[1]) * (x-p[0]) / (v[0]-p[0]))
    lt, lb = on((fx,ft), vl, 800), on((fx,fb), vl, 800)
    rt, rb = on((fx,ft), vr, 1035), on((fx,fb), vr, 1035)
    def inter(a, va, b, vb):
        (x1,y1),(x2,y2),(x3,y3),(x4,y4) = a, va, b, vb
        d = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
        px = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/d
        py = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/d
        return (px, py)
    bk = inter(lt, vr, rt, vl)
    P = lambda *ps: " ".join(f"{x:.1f},{y:.1f}" for x, y in ps)
    cx, cw, ctop, cbot = 1135, 46, 214, 318
    svg = f'''<svg width="1280" height="400" style="position:absolute;left:0;top:0">
 <g stroke="{c['faint']}" stroke-width="1" fill="none">
  <line x1="700" y1="{hy}" x2="1250" y2="{hy}"/>
  <line x1="{lt[0]}" y1="{lt[1]}" x2="{vl[0]+160}" y2="{hy+ (lt[1]-hy)*(160)/(lt[0]-vl[0]):.1f}" stroke-dasharray="2 4"/>
  <line x1="{lb[0]}" y1="{lb[1]}" x2="{vl[0]+160}" y2="{hy+ (lb[1]-hy)*(160)/(lb[0]-vl[0]):.1f}" stroke-dasharray="2 4"/>
  <line x1="{rt[0]}" y1="{rt[1]}" x2="1250" y2="{rt[1]+(hy-rt[1])*(1250-rt[0])/(vr[0]-rt[0]):.1f}" stroke-dasharray="2 4"/>
  <line x1="{rb[0]}" y1="{rb[1]}" x2="1250" y2="{rb[1]+(hy-rb[1])*(1250-rb[0])/(vr[0]-rb[0]):.1f}" stroke-dasharray="2 4"/>
 </g>
 <g stroke="{c['mute']}" stroke-width="1.4" fill="none" stroke-linejoin="round">
  <polygon points="{P((fx,ft),lt,bk,rt)}"/>
  <polyline points="{P(lt,lb,(fx,fb),rb,rt)}"/><line x1="{fx}" y1="{ft}" x2="{fx}" y2="{fb}"/>
  <ellipse cx="{cx}" cy="{ctop}" rx="{cw}" ry="{cw*0.30:.1f}"/>
  <path d="M{cx-cw},{ctop} L{cx-cw},{cbot} A{cw},{cw*0.42:.1f} 0 0 0 {cx+cw},{cbot} L{cx+cw},{ctop}"/>
 </g>
 <g stroke="{c['accent']}" stroke-width="1.2"><line x1="{cx}" y1="{ctop-30}" x2="{cx}" y2="{cbot+34}" stroke-dasharray="5 4"/></g>
 <g fill="{c['mute']}" font-family="DM Mono" font-size="12" letter-spacing="1">
  <text x="1182" y="{hy-8}">HL</text><text x="{cx-150}" y="{cbot+50}" fill="{c['accent']}">minor axis = cylinder axis</text>
 </g></svg>'''
    html = f'''<html><head><style>{FACES}</style></head><body style="margin:0;background:{c['bg']};width:1280px;height:400px;position:relative;overflow:hidden">{svg}
 <div style="position:absolute;left:84px;top:128px;color:{c['ink']}">
  <div style="font:380 104px/1 'CD Fraunces',serif;font-variation-settings:'opsz' 144,'SOFT' 50,'WONK' 0;letter-spacing:-2px">creative director</div>
  <div style="margin-top:24px;font:400 38px/1.2 'CD Instrument Sans',sans-serif;color:{c['mute']}">Design judgement for AI agents</div>
 </div></body></html>'''
    return shot(html, f"banner-{t}", 1280, 400)

PAIRS = [  # (title, note, before, after, crop box as fractions l,t,r,b)
 ("Technical drawing", "Horizon levelled, verticals plumb · TD-PER-1, TD-PER-3",
  "examples/technical-drawing-still-life/round-01.png", "examples/technical-drawing-still-life/round-02.png", (0, .12, 1, .89)),
 ("Illustration", "Sky quieted, figure separated · CORE-3, ILL-2, ILL-11",
  "examples/illustration-knight/round-01.png", "examples/illustration-knight/round-02.png", (.03, 0, .87, 1)),
 ("Web UI", "Contrast fixed (1.84 → 5.17:1), decoration cut · UI-6, UI-7",
  "examples/web-ui-landing/round-01-1280.png", "examples/web-ui-landing/round-02-1280.png", (0, 0, 1, .6)),
]
def crops():
    out = []
    for i, (_, _, b, a, (l, tp, r, bt)) in enumerate(PAIRS):
        for k, f in (("b", b), ("a", a)):
            im = Image.open(ROOT / f).convert("RGB"); W, H = im.size
            box = [l*W, tp*H, r*W, bt*H]; cw, ch = box[2]-box[0], box[3]-box[1]
            want = 3/2                                  # force 3:2, trimming the long side around the centre
            if cw/ch > want: d = (cw - ch*want)/2; box[0] += d; box[2] -= d
            else: d = (ch - cw/want)/2; box[1] += d; box[3] -= d
            p = SRC / f"_c{i}{k}.jpg"; im.crop([int(v) for v in box]).resize((780, 520), Image.LANCZOS).save(p, quality=92)
            out.append(p)
    return out

def strip(t):
    c = THEMES[t]; crops()
    cols = ""
    for i, (title, note, *_ ) in enumerate(PAIRS):
        img = lambda k, lab: f'''<div style="position:relative;margin-top:10px"><img src="_c{i}{k}.jpg" style="width:390px;height:260px;display:block;border-radius:3px">
          <span style="position:absolute;left:8px;top:8px;background:{c['bg']};color:{c['ink']};font:600 12px/1 Inter;letter-spacing:.8px;padding:5px 7px;border-radius:2px">{lab}</span></div>'''
        cols += f'''<div style="width:390px"><div style="font:600 19px/1.2 Inter;color:{c['ink']}">{title}</div>
          <div style="font:400 14px/1.35 Inter;color:{c['mute']};margin-top:4px;height:20px">{note}</div>
          {img("b","BEFORE")}{img("a","AFTER")}</div>'''
    html = f'''<html><body style="margin:0;background:{c['bg']}"><div style="display:flex;gap:28px;padding:28px 33px 30px">{cols}</div></body></html>'''
    return shot(html, f"before-after-{t}", 1280, 650)

def loop(t):
    c = THEMES[t]
    steps = [("0","Brief","what, who, where, must-keeps"),("1","Render","real output, real size"),("2","Look","blur, thumbnail, flip,<br>greyscale, crop"),
             ("3","Critique","every point cites a rule"),("4","Fix","up to 3, biggest first"),("5","Stop","clearly better? hand off")]
    x0, w, gap = 40, 168, 36
    boxes = ""; arrows = ""
    for i, (n, name, sub) in enumerate(steps):
        x = x0 + i*(w+gap)
        strong = name in ("Critique",)
        boxes += f'''<div style="position:absolute;left:{x}px;top:70px;width:{w}px;height:104px;box-sizing:border-box;border:1.5px solid {c['accent'] if strong else c['faint']};border-radius:6px;padding:14px 14px">
          <div style="font:500 16px/1 'DM Mono';color:{c['mute']};letter-spacing:1px">{n}</div>
          <div style="font:600 30px/1.2 Inter;color:{c['ink']};margin-top:10px">{name}</div></div>'''
        if i: arrows += f'<line x1="{x-gap+6}" y1="122" x2="{x-8}" y2="122"/><polyline points="{x-13},117 {x-8},122 {x-13},127" fill="none"/>'
    xr, xf = x0+1*(w+gap)+w/2, x0+4*(w+gap)+w/2
    xc = x0+3*(w+gap)+w/2
    svg = f'''<svg width="1280" height="300" style="position:absolute;left:0;top:0"><g stroke="{c['mute']}" stroke-width="1.5">{arrows}
      <path d="M{xf},174 V214 H{xr} V182" fill="none" stroke-dasharray="4 4"/><polyline points="{xr-5},187 {xr},181 {xr+5},187" fill="none"/></g>
      <g stroke="{c['accent']}" stroke-width="1.5" fill="none"><path d="M{xc},48 V22 H{xc+60}" stroke-dasharray="4 4"/></g></svg>'''
    labels = f'''<div style="position:absolute;left:{(xr+xf)/2-200}px;top:220px;width:400px;text-align:center;font:400 18px/1.3 Inter;color:{c['mute']}">re-render and compare · max 5 rounds</div>
      <div style="position:absolute;left:{xc+70}px;top:10px;font:400 18px/1.3 Inter;color:{c['accent']}">fundamentally broken? take over and rework (4b)</div>'''
    html = f'''<html><body style="margin:0;background:{c['bg']};width:1280px;height:260px;position:relative;overflow:hidden">{svg}{boxes}{labels}</body></html>'''
    return shot(html, f"loop-{t}", 1280, 260)

if __name__ == "__main__":
    for t in THEMES:
        print(banner(t), strip(t), loop(t))
    for p in SRC.glob("_c*.jpg"): p.unlink()
    for p in OUT.glob("before-after-*.png"):     # photos compress better as JPEG
        Image.open(p).convert("RGB").save(p.with_suffix(".jpg"), quality=86, optimize=True); p.unlink()

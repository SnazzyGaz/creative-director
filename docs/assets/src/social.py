#!/usr/bin/env python3
"""Build the social cards: X/Twitter (1600x900 + 1200x675) and the GitHub social preview (1280x640).
Run from repo root: python3 docs/assets/src/social.py [x|github|all]  (default all)"""
import subprocess, pathlib, sys
from PIL import Image
ROOT = pathlib.Path(__file__).resolve().parents[3]
SRC = ROOT / "docs/assets/src"; OUT = ROOT / "docs/assets/social"
c = dict(bg="#161514", ink="#EEE9DF", mute="#A39C91", faint="#3E3A35", accent="#D9825F")
FACES = ("@font-face{font-family:'CD Newsreader';src:url('../../../fonts/editorial-serif/newsreader/Newsreader%5Bopsz,wght%5D.ttf');font-weight:200 800}"
         "@font-face{font-family:'CD Instrument Sans';src:url('fonts/InstrumentSans-VariableFont_wdth,wght.ttf');font-weight:400 700}")
W, H = 1600, 900
def on(p, v, x): return (x, p[1] + (v[1]-p[1]) * (x-p[0]) / (v[0]-p[0]))
def inter(a, va, b, vb):
    (x1,y1),(x2,y2),(x3,y3),(x4,y4) = a, va, b, vb
    d = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    return (((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/d, ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/d)
P = lambda *ps: " ".join(f"{x:.1f},{y:.1f}" for x, y in ps)

def card(kind="x"):
    hy = 300; vl, vr = (520, hy), (2050, hy)        # two vanishing points on one horizon, both outside the cone
    fx, ft, fb = 1130, 410, 590                      # front vertical edge of the box (below eye level)
    lt, lb = on((fx,ft), vl, 975), on((fx,fb), vl, 975)
    rt, rb = on((fx,ft), vr, 1300), on((fx,fb), vr, 1300)
    bk = inter(lt, vr, rt, vl)
    cx, cw, ctop, cbot = 1415, 62, 440, 590          # cylinder: ellipse degree matches the box station point and opens further below the horizon (TD-ELL-2)
    ext = lambda p, v, x: on(p, v, x)
    gh = kind == "github"
    CW, CH = (1280, 640) if gh else (W, H)
    # GitHub preview: the same sketch at 0.72, right edge of its labels on the 80 px margin (12.5% of the short side, LAY-5)
    tf = f'translate({1200 - (W - 112) * 0.72:.1f},0) scale(0.72)' if gh else ''
    svg = f'''<svg width="{CW}" height="{CH}" style="position:absolute;left:0;top:0"><g transform="{tf}">
 <g stroke="{c['faint']}" stroke-width="1.2" fill="none">
  <line x1="860" y1="{hy}" x2="{W}" y2="{hy}"/>
  {''.join(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{ext(p,vl,880)[0]:.1f}" y2="{ext(p,vl,880)[1]:.1f}" stroke-dasharray="2 5"/>' for p in (lt, lb))}
  {''.join(f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{W}" y2="{ext(p,vr,W)[1]:.1f}" stroke-dasharray="2 5"/>' for p in (rt, rb))}
 </g>
 <g stroke="{c['mute']}" stroke-width="2.4" fill="none" stroke-linejoin="round">
  <polygon points="{P((fx,ft),lt,bk,rt)}"/>
  <polyline points="{P(lt,lb,(fx,fb),rb,rt)}"/><line x1="{fx}" y1="{ft}" x2="{fx}" y2="{fb}"/>
  <ellipse cx="{cx}" cy="{ctop}" rx="{cw}" ry="{cw*0.20:.1f}"/>
  <path d="M{cx-cw},{ctop} L{cx-cw},{cbot} A{cw},{cw*0.34:.1f} 0 0 0 {cx+cw},{cbot} L{cx+cw},{ctop}"/>
 </g>
 <g stroke="{c['accent']}" stroke-width="2" fill="none">
  <line x1="{cx}" y1="{ctop-46}" x2="{cx}" y2="{cbot+52}" stroke-dasharray="6 5"/>
  <line x1="{cx-cw-14}" y1="{ctop}" x2="{cx+cw+14}" y2="{ctop}" stroke-dasharray="2 4"/>
 </g>
 <g font-family="DM Mono" font-size="17" letter-spacing="1.2">
  <text x="{W-112}" y="{hy-14}" text-anchor="end" fill="{c['mute']}">HL · eye level</text>
  <text x="{W-112}" y="{cbot+90}" text-anchor="end" fill="{c['accent']}">TD-ELL-1</text>
  <text x="{W-112}" y="{cbot+114}" text-anchor="end" fill="{c['accent']}">minor axis = cylinder axis</text>
 </g></g></svg>'''
    if gh:
        m = 80
        txt = f'''<div style="position:absolute;left:{m}px;top:118px;color:{c['ink']}">
  <div style="font:380 128px/0.94 'CD Newsreader',serif;font-variation-settings:'opsz' 72;letter-spacing:-2.6px">creative<br>director</div>
  <div style="margin-top:32px;font:400 38px/1.2 'CD Instrument Sans',sans-serif;color:{c['ink']}">Design judgement for AI agents</div>
 </div>
 <div style="position:absolute;left:{m}px;right:{m}px;bottom:{m}px;display:flex;justify-content:space-between;font:400 20px/1 'DM Mono';letter-spacing:.5px">
  <span style="color:{c['ink']}">github.com/SnazzyGaz/creative-director</span>
  <span style="color:{c['mute']}">MIT · Claude, Cursor, GPT, Grok</span>
 </div>'''
    html = f'''<html><head><style>{FACES}</style></head><body style="margin:0;background:{c['bg']};width:{CW}px;height:{CH}px;position:relative;overflow:hidden">{svg}
 {txt if gh else ''}<div style="position:absolute;left:112px;top:196px;color:{c['ink']};display:{'none' if gh else 'block'}">
  <div style="font:380 172px/0.94 'CD Newsreader',serif;font-variation-settings:'opsz' 72;letter-spacing:-3.5px">creative<br>director</div>
  <div style="margin-top:44px;font:400 50px/1.2 'CD Instrument Sans',sans-serif;color:{c['ink']}">Design judgement for AI agents</div>
 </div>
 <div style="position:absolute;left:112px;right:112px;bottom:64px;display:{'none' if gh else 'flex'};justify-content:space-between;font:400 24px/1 'DM Mono';letter-spacing:.5px">
  <span style="color:{c['ink']}">github.com/SnazzyGaz/creative-director</span>
  <span style="color:{c['mute']}">MIT · works with Claude, Cursor, GPT, Grok</span>
 </div></body></html>'''
    p = SRC / "_social.html"; p.write_text(html); big = OUT / "_card@2x.png"
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
        f"--window-size={CW},{CH}", "--force-device-scale-factor=2", f"--screenshot={big}", f"file://{p}"], check=True, capture_output=True)
    p.unlink()
    im = Image.open(big).convert("RGB"); big.unlink()
    if gh:
        im.resize((1280, 640), Image.LANCZOS).save(OUT / "card-1280x640.png", optimize=True); return
    im.resize((1600, 900), Image.LANCZOS).save(OUT / "card-1600x900.png", optimize=True)
    im.resize((1200, 675), Image.LANCZOS).save(OUT / "card-1200x675.png", optimize=True)
    im.resize((500, 281), Image.LANCZOS).save("/tmp/card-feed-500.png")
if __name__ == "__main__":
    k = sys.argv[1] if len(sys.argv) > 1 else "all"
    if k in ("x", "all"): card("x")
    if k in ("github", "all"): card("github")
    print("ok")

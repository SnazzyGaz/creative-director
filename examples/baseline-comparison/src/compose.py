#!/usr/bin/env python3
"""Set the type for the with-skill fox cover and jazz poster over the generated art (art has no text).
Fonts: Fraunces and Instrument Sans (OFL 1.1, vendored in docs/assets/src/fonts). Output 864x1152, same as the
without-skill images. Usage: python3 compose.py ROUND   (writes ../fox-with-rROUND.png and ../poster-with-rROUND.png)"""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
FONTS = (HERE / "../../../docs/assets/src/fonts").resolve()
FACES = (f"@font-face{{font-family:F;src:url('file://{FONTS}/Fraunces-VariableFont_SOFT,WONK,opsz,wght.ttf');font-weight:100 900}}"
         f"@font-face{{font-family:S;src:url('file://{FONTS}/InstrumentSans-VariableFont_wdth,wght.ttf');font-weight:400 700;font-stretch:75% 100%}}")
R = sys.argv[1] if len(sys.argv) > 1 else "1"
from params import FOX, POSTER   # per-round values live in params.py so each round's change is a small diff

def page(art, body, extra=""):
    return (f"<html><head><style>{FACES} body{{margin:0;width:864px;height:1152px;position:relative;overflow:hidden;"
            f"background:url('file://{HERE/art}') center/cover}} {extra}</style></head><body>{body}</body></html>")

def fox(p):
    return page("fox-art.jpg", f'''
 <div style="position:absolute;left:{p['x']}px;top:{p['y']}px;color:{p['ink']}">
  <div style="font:{p['w']} {p['size']}px/0.92 F,serif;font-variation-settings:'opsz' 144,'SOFT' 100,'WONK' 1;letter-spacing:-1px">{p['title']}</div>
  <div style="margin-top:{p['gap']}px;font:600 {p['asize']}px/1 S,sans-serif;letter-spacing:{p['atrack']}px;color:{p['aink']}">{p['author']}</div>
 </div>''')

def poster(p):
    return page("poster-art.jpg", f'''
 <div style="position:absolute;left:{p['x']}px;top:{p['y']}px;right:{p['x']}px;color:{p['ink']}">
  <div style="font:600 {p['kicker']}px/1 S,sans-serif;letter-spacing:{p['ktrack']}px;text-transform:uppercase;color:{p['kink']}">Neighbourhood</div>
  <div style="margin-top:10px;font:{p['w']} {p['size']}px/0.86 F,serif;font-variation-settings:'opsz' 144,'SOFT' 0,'WONK' 1;letter-spacing:-3px">Jazz<br>Night</div>
  <div style="margin-top:{p['gap']}px;width:{p['rule']}px;height:5px;background:{p['accent']}"></div>
  <div style="margin-top:{p['gap2']}px;font:600 {p['fsize']}px/1.25 S,sans-serif;font-stretch:{p['stretch']}">Friday 14 March, 8pm<br>The Lantern</div>
  <div style="margin-top:14px;font:400 {p['fsize2']}px/1.2 S,sans-serif">Free entry</div>
 </div>''')

for name, fn, p in (("fox", fox, FOX), ("poster", poster, POSTER)):
    h = HERE / f"_{name}.html"; h.write_text(fn(p)); out = HERE.parent / f"{name}-with-r{R}.png"
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--window-size=864,1152", f"--screenshot={out}", f"file://{h}"], check=True, capture_output=True)
    h.unlink(); print(out)

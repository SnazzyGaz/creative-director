#!/usr/bin/env python3
"""Aesthetic demo: set the jazz poster type over the night artwork (art has no text).
Same facts, fonts and size as examples/baseline-comparison (864x1152). Usage: python3 compose.py ROUND"""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
FONTS = (HERE / "../../../docs/assets/src/fonts").resolve()
FACES = (f"@font-face{{font-family:F;src:url('file://{FONTS}/Fraunces-VariableFont_SOFT,WONK,opsz,wght.ttf');font-weight:100 900}}"
         f"@font-face{{font-family:S;src:url('file://{FONTS}/InstrumentSans-VariableFont_wdth,wght.ttf');font-weight:400 700;font-stretch:75% 100%}}")
R = sys.argv[1] if len(sys.argv) > 1 else "1"
P = dict(x=64, y=56, ink="#F3E6C8", kink="#E9B566", kicker=30, ktrack=6, size=136, w=800, accent="#E9A23B",
         rule=120, gap=22, gap2=20, fsize=40, fsize2=34, stretch="85%")
body = f'''
 <div style="position:absolute;left:{P['x']}px;top:{P['y']}px;right:{P['x']}px;color:{P['ink']}">
  <div style="font:600 {P['kicker']}px/1 S,sans-serif;letter-spacing:{P['ktrack']}px;text-transform:uppercase;color:{P['kink']}">Neighbourhood</div>
  <div style="margin-top:10px;font:{P['w']} {P['size']}px/0.86 F,serif;font-variation-settings:'opsz' 144,'SOFT' 0,'WONK' 1;letter-spacing:-3px">Jazz<br>Night</div>
  <div style="margin-top:{P['gap']}px;width:{P['rule']}px;height:5px;background:{P['accent']}"></div>
  <div style="margin-top:{P['gap2']}px;font:600 {P['fsize']}px/1.25 S,sans-serif;font-stretch:{P['stretch']}">Friday 14 March, 8pm<br>The Lantern</div>
  <div style="margin-top:14px;font:400 {P['fsize2']}px/1.2 S,sans-serif">Free entry</div>
 </div>'''
html = (f"<html><head><style>{FACES} body{{margin:0;width:864px;height:1152px;position:relative;overflow:hidden;"
        f"background:url('file://{HERE}/poster-art-night.jpg') center/cover}}</style></head><body>{body}</body></html>")
h = HERE / "_poster.html"; h.write_text(html); out = HERE.parent / f"poster-aes-r{R}.png"
subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                "--window-size=864,1152", f"--screenshot={out}", f"file://{h}"], check=True, capture_output=True)
h.unlink(); print(out)

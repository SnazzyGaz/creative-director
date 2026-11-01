#!/usr/bin/env python3
"""Aesthetic demo 2: set the fox cover type over the golden-hour artwork (art has no text).
Same title wording, placeholder author, fonts and size as examples/baseline-comparison (864x1152). Usage: python3 compose_fox.py ROUND"""
import pathlib, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
FONTS = (HERE / "../../../docs/assets/src/fonts").resolve()
FACES = (f"@font-face{{font-family:F;src:url('file://{FONTS}/Fraunces-VariableFont_SOFT,WONK,opsz,wght.ttf');font-weight:100 900}}"
         f"@font-face{{font-family:S;src:url('file://{FONTS}/InstrumentSans-VariableFont_wdth,wght.ttf');font-weight:400 700;font-stretch:75% 100%}}")
R = sys.argv[1] if len(sys.argv) > 1 else "1"
# Warmer type to match the golden-hour art: deep cocoa ink instead of forest green, softer rounder Fraunces (SOFT 100, WONK 1, heavier).
P = dict(x=64, y=72, size=96, w=640, ink="#3A1F12", gap=26, asize=26, atrack=3, aink="#6B3A20")
body = f'''
 <div style="position:absolute;left:{P['x']}px;top:{P['y']}px;color:{P['ink']}">
  <div style="font:{P['w']} {P['size']}px/0.92 F,serif;font-variation-settings:'opsz' 144,'SOFT' 100,'WONK' 1;letter-spacing:-1px">A Fox<br>Who Loves<br><i style="font-style:italic;font-weight:{P['w']}">Reading</i></div>
  <div style="margin-top:{P['gap']}px;font:600 {P['asize']}px/1 S,sans-serif;letter-spacing:{P['atrack']}px;color:{P['aink']}">AUTHOR NAME</div>
 </div>'''
html = (f"<html><head><style>{FACES} body{{margin:0;width:864px;height:1152px;position:relative;overflow:hidden;"
        f"background:url('file://{HERE}/fox-art-golden.jpg') center/cover}}</style></head><body>{body}</body></html>")
h = HERE / "_fox.html"; h.write_text(html); out = HERE.parent / f"fox-aes-r{R}.png"
subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                "--window-size=864,1152", f"--screenshot={out}", f"file://{h}"], check=True, capture_output=True)
h.unlink(); print(out)

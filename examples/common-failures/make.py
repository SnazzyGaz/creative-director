"""make.py: builds the small single-round UI cases as HTML (before/after) and screenshots them
with headless Chrome at 640x400. Each before is built with one planted failure."""
import subprocess, os
BASE="<!doctype html><html><head><meta charset=utf-8><style>body{margin:0;font-family:'Source Sans 3',sans-serif;color:#1f2328;background:#f6f7f9}*{box-sizing:border-box}%s</style></head><body>%s</body></html>"
ICON_OUT='<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#1f2328" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">%s</svg>'
ICON_FILL='<svg width="30" height="30" viewBox="0 0 24 24" fill="#d1242f">%s</svg>'
home='<path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>'
search='<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>'
bell='<path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4z"/><path d="M10 21h4"/>'
user='<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>'
cards=lambda st: "".join(f'<div class="c" style="{s}"><h3>{t}</h3><p>Short description of the plan.</p></div>' for t,s in zip(["Basic","Plus","Pro"],st))
CASES={
 "spacing":(
  ".c{background:#fff;border:1px solid #d0d7de;border-radius:8px}.row{display:flex;gap:%s;padding:24px}h3{margin:0 0 4px}p{margin:0}",
  lambda b: '<div class="row">'+(cards(["padding:7px 22px","padding:18px 9px","padding:30px 14px"]) if b else cards(["padding:16px"]*3))+'</div>',
  ["5px 31px","16px"]),
 "grid":(
  ".c{background:#fff;border:1px solid #d0d7de;border-radius:8px;padding:16px;width:180px}h3{margin:0 0 4px}p{margin:0}.row{position:relative;height:240px;padding:24px}",
  lambda b: '<div class="row">'+("".join(f'<div class="c" style="position:absolute;left:{x}px;top:{y}px"><h3>{t}</h3><p>Short description of the plan.</p></div>' for t,(x,y) in zip(["Basic","Plus","Pro"],[(24,24),(219,37),(421,19)])) if b else "".join(f'<div class="c" style="position:absolute;left:{x}px;top:24px"><h3>{t}</h3><p>Short description of the plan.</p></div>' for t,x in zip(["Basic","Plus","Pro"],[24,224,424])))+'</div>',
  None),
 "type-scale":(
  ".w{padding:24px;background:#fff;height:240px}",
  lambda b: '<div class="w">'+('<h1 style="font:700 31px Lobster,cursive;margin:0">Plans for teams</h1><h2 style="font:600 29px Oswald,sans-serif;margin:4px 0">Choose a plan</h2><p style="font:15px \'Courier Prime\',monospace">Every plan includes unlimited projects.</p><p style="font:13.5px \'Source Sans 3\';font-weight:700">Billed yearly. Cancel any time.</p><p style="font:italic 17px Georgia,serif">Questions? Talk to us.</p>' if b else '<h1 style="font:700 36px Fraunces,serif;margin:0">Plans for teams</h1><h2 style="font:600 24px \'Source Sans 3\';margin:12px 0 8px">Choose a plan</h2><p style="font:17px \'Source Sans 3\';margin:0 0 8px">Every plan includes unlimited projects.</p><p style="font:14px \'Source Sans 3\';color:#57606a;margin:0 0 8px">Billed yearly. Cancel any time.</p><p style="font:17px \'Source Sans 3\';margin:0">Questions? Talk to us.</p>')+'</div>',
  None),
 "icons":(
  ".bar{display:flex;gap:40px;align-items:center;padding:40px;background:#fff}.bar span{display:flex;flex-direction:column;align-items:center;gap:6px;font-size:14px}",
  lambda b: '<div class="bar">'+("".join(f'<span>{i}{t}</span>' for i,t in [(ICON_OUT%home,"Home"),(ICON_FILL%'<circle cx="11" cy="11" r="8"/>',"Search"),('<span style="font-size:30px">🔔</span>',"Alerts"),('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0969da" stroke-width="1"><rect x="3" y="3" width="18" height="18"/><circle cx="12" cy="10" r="3"/></svg>',"Account")]) if b else "".join(f'<span>{ICON_OUT%i}{t}</span>' for i,t in [(home,"Home"),(search,"Search"),(bell,"Alerts"),(user,"Account")]))+'</div>',
  None),
}
for name,(css,body,gaps) in CASES.items():
    for b,tag in ((1,"before"),(0,"after")):
        c=css%(gaps[0] if b else gaps[1]) if gaps else css
        f=f"{name}-{tag}.html"; open(f,"w").write(BASE%(c,body(b)))
        subprocess.run(["google-chrome","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--window-size=640,240",f"--screenshot={name}-{tag}.png","file://"+os.path.abspath(f)],capture_output=True)
    subprocess.run(["python3","../../tools/beforeafter.py",f"{name}-before.png",f"{name}-after.png",f"{name}-before-after.png","Before","After"])

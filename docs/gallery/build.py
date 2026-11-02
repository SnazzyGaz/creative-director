"""Builds index.html. Run from the repo root: python3 docs/gallery/build.py"""
import html
R = "https://raw.githubusercontent.com/SnazzyGaz/creative-director/main/examples/"
G = "https://github.com/SnazzyGaz/creative-director/blob/main/examples/"
# (module, title, kind, made with, image path, log path, one line)
E = [
 ("web-ui","Bakery page","Take-over","Hand-built bad HTML","web-ui-takeover/before-after.png","web-ui-takeover/log.md","11 of 11 text pairs failed contrast (worst 1.13:1); rebuilt, all pass (min 6.31:1)."),
 ("illustration","The keeper's cat","Take-over","GenerateImage (AI)","illustration-takeover/before-after.png","illustration-takeover/log.md","Light from four directions and the generic AI look; regenerated with one light and a value plan. Round 3 made it worse; round 2 delivered."),
 ("technical-drawing","Box and tin","Take-over","Code, errors planted","technical-drawing-takeover/before-after.png","technical-drawing-takeover/log.md","VPs 200 px apart, verticals leaning, ellipses 19 deg off; redrawn by construction. ellipse.py missed the lemon shape until v0.3.0."),
 ("technical-drawing","Lemon-shaped ellipse, caught","Tool check","Code, error planted","technical-drawing-takeover/ell-r01-top-v03.png","technical-drawing-takeover/log.md","v0.3.0 ellipse.py on the planted top: ends 0.71/0.68 of a true ellipse, pointed; tilted 12 deg. v0.2.0 said OK."),
 ("technical-drawing","Box and can","Take-over","GenerateImage (AI)","technical-drawing-still-life/before-after.png","technical-drawing-still-life/log.md","Perspective rebuilt; the rework dropped the open box from the brief."),
 ("ux","Library sign-up","Nudge","Hand-built HTML","ux-signup-nudge/before-after.png","ux-signup-nudge/log.md","Placeholder labels at 1.92:1 and 'Error 422'; real labels, inline errors that keep the input."),
 ("3d","White mug","Nudge","Blender 4.2 Cycles","3d-mug-nudge/before-after.png","3d-mug-nudge/log.md","24.2% clipped to flat white; AgX, plausible materials, three lights. 0% clipped."),
 ("illustration","Knight and castle","Nudge","GenerateImage (AI)","illustration-knight/before-after.png","illustration-knight/log.md","Sky out-shouted the knight; quieter sky and mist. The rim light edit did not apply."),
 ("web-ui","AI landing page","Nudge","Generated HTML","web-ui-landing/before-after.png","web-ui-landing/log.md","Six pairs failed contrast; fixed. Still generic: needs a brand brief."),
 ("web-ui","Inconsistent spacing","Common failure","Code","common-failures/spacing-before-after.png","common-failures/README.md","Three different paddings; one 16 px scale."),
 ("web-ui","Misaligned grid","Common failure","Code","common-failures/grid-before-after.png","common-failures/README.md","Card tops at 24, 37 and 19 px; shared top and column step. v0.3.0 grid.py measures the same numbers from the screenshot."),
 ("web-ui","Clashing type scale","Common failure","Code","common-failures/type-scale-before-after.png","common-failures/README.md","Five typefaces; two faces, four steps."),
 ("web-ui","Mixed icon set","Common failure","Code","common-failures/icons-before-after.png","common-failures/README.md","Four icon styles; one outline set."),
 ("technical-drawing","SVG perspective","Common failure","Code (SVG)","common-failures/svg-box-before-after.png","common-failures/README.md","Horizon tilt 8.26 deg (vp.py); 0.02 deg after."),
 ("3d","Floating and intersecting parts","Common failure","Blender 4.2, model-qa","common-failures/stool-before-after.png","common-failures/README.md","Seat floating 12 mm, a leg through the seat; model-qa PASS after. v0.3.0 intersect.py names the leg through the seat directly."),
 ("layout","X launch card","Critique","Code (Pillow)","layout-social-card/feed-400.png","layout-social-card/README.md","Passes the blockers; the proof-point caption is about 2 px tall in the feed, and the footer margin is half the side margins."),
 ("typography","Plan card type scale","Critique","Code","common-failures/type-scale-before-after.png","typography-scale/README.md","Five families and ratios of 1.07 between sizes; two families and a 1.2-1.5 scale."),
 ("brand","Brand intake: AI landing page","Intake","Generated HTML","web-ui-landing/before-after.png","brand-intake/README.md","Five generic-look tells left after round 2; seven questions and an assumed token sheet. Three tells need the owner's facts."),
 ("character","Barista hands and face","Zoom audit","AI image generator","character-hands/generated.jpg","character-hands/README.md","Five digits, joints that bend right, eyes that match: no blockers. One hand reads about 10% large."),
 ("illustration","Fox cover: with and without the skill","Baseline","GenerateImage (AI), both; type set in code","baseline-comparison/fox-side-by-side.jpg","baseline-comparison/README.md","Without: invented subtitle, signs and slogans, cluttered. With: art plus type set in code, working title and author placeholder only, 3 rounds (round 3 removed a second light glowing from the book). Calmer; loses on energy at a glance."),
 ("illustration","Jazz poster: with and without the skill","Baseline","GenerateImage (AI), both; type set in code","baseline-comparison/poster-side-by-side.jpg","baseline-comparison/README.md","Without: invented address and slogans. With: exactly the four facts, two typefaces, 3 rounds. More legible and correct; loses on atmosphere."),
 ("aesthetic-critique","Jazz poster: atmosphere won back","Aesthetic demo","GenerateImage (AI) art; type set in code","aesthetic-benchmark/side-by-side.jpg","aesthetic-benchmark/README.md","One sample, self-judged. Intent model, two aesthetic changes (night street, lamp at true scale), side-by-side verdict: stronger on atmosphere; cost: busier, title second at blur. All contrast checks pass. Round 3 moved the bass into the lamp's light (it had been lit from nowhere)."),
 ("aesthetic-critique","Picture-book spread: one light","Across domains","GenerateImage (AI); type in code","aesthetic-across-domains/illustration/side-by-side.jpg","aesthetic-across-domains/illustration/critique.md","Two lights and text across the fold at 1.4:1; regenerated with one light, the pair against plain sky, nothing added. Anatomy pass after every edit."),
 ("aesthetic-critique","Nest box exploded view","Across domains","Code (matplotlib)","aesthetic-across-domains/technical-drawing/side-by-side.jpg","aesthetic-across-domains/technical-drawing/critique.md","Height drawn at 0.675 of width, screws as dots, labels on parts; true isometric, 4:2:1 lines, balloons and a parts list."),
 ("aesthetic-critique","Pottery studio landing page","Across domains","HTML/CSS; generated photo","aesthetic-across-domains/web-landing/side-by-side.jpg","aesthetic-across-domains/web-landing/critique.md","Invented reviews and no date or price; the course facts and Book in the first screen, all text 4.5:1 or better."),
 ("aesthetic-critique","Bus ticket app flow","Across domains","HTML/CSS","aesthetic-across-domains/app-flow/side-by-side.jpg","aesthetic-across-domains/app-flow/critique.md","Text 1.5-2.7:1 and 18-25 px targets; 48 px targets, prices on the buttons, a ticket a driver can read."),
 ("aesthetic-critique","Seed swap poster","Across domains","Code (Pillow)","aesthetic-across-domains/poster/side-by-side.jpg","aesthetic-across-domains/poster/critique.md","Date at 2.8:1 on a gradient and five invented phrases; what and when now read at 10% size."),
 ("aesthetic-critique","Perfume product shot","Across domains","Blender 4.2 Cycles; type in code","aesthetic-across-domains/product-3d/side-by-side.jpg","aesthetic-across-domains/product-3d/critique.md","Glass invisible on grey, 29.3% clipped, base through the glass floor; rim-lit on black, AgX, model-qa 0 high."),
 ("aesthetic-critique","Mauna Loa CO2 chart","Across domains","Code (matplotlib), NOAA data","aesthetic-across-domains/data-chart/side-by-side.jpg","aesthetic-across-domains/data-chart/critique.md","No source, an added 'Alarming increase!', rainbow bars; one line, a title that states the finding, source line."),
 ("web-ui","Claude Opus 5.5 smoke test (contaminated)","Outside run","Claude Opus 5.5, claude.ai","cross-model/runs/claude-opus-5.5-2026-11-01/crumb-1280.png","cross-model/runs/README.md","Not a score: the model had read the answer keys and ran no baseline. Shows the tools and rule IDs work outside Grok Bot; its rework passes contrast (min 6.11:1) and 390 px."),
 ("web-ui","GPT-6 pilot (contaminated)","Outside run","ChatGPT GPT-6","cross-model/runs/gpt-6-2026-11-01-pilot/outputs/task-a/shot-1280.png","cross-model/runs/README.md","Not a score: rubric read, with and without written in one chat, no tools run. Its rework, checked here, passes contrast, 390 px and 200% text."),
 ("first-principles","Seed swap poster: remade from scratch","Remake","Code (Pillow)","first-principles-remake/side-by-side.jpg","first-principles-remake/README.md","Stepped back to the poster's one job (bring seeds), caught a Saturday that is a Sunday, compared three concepts, built Bring / Take. Self-judged."),
]
mods = ["all","web-ui","ux","illustration","technical-drawing","3d","layout","typography","brand","character","aesthetic-critique","first-principles"]
cards = "\n".join(f'''<article data-m="{m}"><a href="{G}{l}"><img loading="lazy" src="{R}{i}" alt="Before and after: {html.escape(t)}"></a>
<div class="b"><p class="k">{m} · {k} · {html.escape(w)}</p><h2>{html.escape(t)}</h2><p>{html.escape(d)}</p><a href="{G}{l}">Critique and log</a></div></article>''' for m,t,k,w,i,l,d in E)
btns = "".join(f'<button data-f="{m}"{" aria-pressed=\"true\"" if m=="all" else " aria-pressed=\"false\""}>{m}</button>' for m in mods)
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>creative-director: before and after gallery</title>
<style>
:root{{--bg:#f7f4ee;--fg:#1d1b18;--mut:#5b554c;--line:#d9d2c5;--acc:#1f3a5f}}
@media(prefers-color-scheme:dark){{:root{{--bg:#161513;--fg:#ece7de;--mut:#b3ab9e;--line:#3a3631;--acc:#9cc0ec}}}}
*{{box-sizing:border-box}}body{{margin:0;font:16px/1.5 system-ui,sans-serif;background:var(--bg);color:var(--fg)}}
header,main{{max-width:1200px;margin:0 auto;padding:24px 16px}}h1{{font:600 2rem/1.2 Georgia,serif;margin:0 0 8px}}
header p{{color:var(--mut);margin:0 0 16px;max-width:65ch}}a{{color:var(--acc)}}
nav{{display:flex;flex-wrap:wrap;gap:8px}}button{{font:inherit;padding:8px 14px;border:1px solid var(--line);border-radius:999px;background:transparent;color:var(--fg);cursor:pointer;min-height:44px}}
button[aria-pressed=true]{{background:var(--fg);color:var(--bg);border-color:var(--fg)}}
main{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:24px}}
article{{border:1px solid var(--line);border-radius:8px;overflow:hidden;display:flex;flex-direction:column}}
article img{{width:100%;height:220px;object-fit:contain;display:block;background:#fff;border-bottom:1px solid var(--line)}}.b{{padding:12px 16px 16px}}.b h2{{font-size:1.1rem;margin:0 0 4px}}.b p{{margin:0 0 8px}}
.k{{font-size:.85rem;color:var(--mut)}}[hidden]{{display:none}}
</style></head><body>
<header><h1>Before and after</h1>
<p>Every example from <a href="https://github.com/SnazzyGaz/creative-director">creative-director</a>, run through its critique loop. Each card says how the work was made; AI-generated and deliberately bad starting points are labelled. Click a card for the rule-cited critique and log, including what didn't work.</p>
<nav aria-label="Filter by module">{btns}</nav></header>
<main>
{cards}
</main>
<script>
document.querySelectorAll('nav button').forEach(b=>b.onclick=()=>{{const f=b.dataset.f;
document.querySelectorAll('nav button').forEach(x=>x.setAttribute('aria-pressed',x===b));
document.querySelectorAll('article').forEach(a=>a.hidden=!(f==='all'||a.dataset.m===f));}});
</script></body></html>
'''
open("docs/gallery/index.html","w").write(page)

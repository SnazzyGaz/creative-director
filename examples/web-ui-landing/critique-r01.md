## Critique: "Nimbus AI" landing page, round 1

**Brief:** typical AI-generated SaaS landing page (hero, one call to action, three feature cards). Seen on phone (390 px) and desktop (1280 px).
**Criteria judged against:** UI-2, UI-6, UI-7, UI-9, UI-10, UX-1, UX-6, CORE-1, CORE-8.
**Evidence looked at:** round-01-390.png, round-01-1280.png, round-01-zoom200.png (headless Chrome, tools/shot.sh); WCAG ratios from tools/contrast.py.

### Test results (evidence)
- Squint/blur: headline and white button lead; cards read as one grey band.
- Thumbnail: headline readable; subtitle and card text are not.
- Greyscale: subtitle and badge fall into the gradient's value; card body text is close to the card ground.
- Contrast (automatic): subtitle 2.86:1 on purple, 1.84:1 on blue; badge 3.14 / 2.15; gradient headline end 1.99 on blue (large text, needs 3); card body 3.53; footer 2.52. Button 5.70 and card headings 15.5 pass.
- 200% zoom (automatic screenshot, judged): nothing clipped, but the three cards stay side by side at 640 CSS px: 1-3 words per line.

### Meets criteria
- UX-1: one clear action ("Get started"), reachable on both widths.
- UI-10: text grows to 200% without clipping or overlap.
- CORE-1: headline then button is a clear order.

### Needs improvement (ranked)
1. [BLOCKER] UI-6 not met. Six text pairs below 4.5:1 (3:1 for the headline): hero subtitle, badge, headline gradient end, card body, footer. Fix: darken the gradient's blue end to #2563eb; white subtitle and badge on a dark scrim; card body and footer to #9ca3af.
2. [IMPROVEMENT] UI-7 / UI-9 / CORE-8 not met. 8 generic tells (purple-blue gradient, Inter, centred hero with one button, three identical icon cards, glass glow, gradient text, one radius everywhere, vague copy). Fix this round: remove the gradient text, glow shadows and backdrop blur.
3. [IMPROVEMENT] UI-2 not met at 200% zoom. Card text 1-3 words per line. Fix: stack the cards below 900 px.
4. [IMPROVEMENT] UX-6 / UI-7. Copy says nothing specific ("seamlessly elevates", "next-generation"). Needs real claims from the brief (see Questions).

### Take-over check (4b)
- One MUST-BE-RIGHT rule fails (UI-6, many instances). The flow works and the page is usable. Nudge.

### Questions for the owner
- The remaining UI-7 tells (gradient, centred hero, three cards, Inter) are choices, not errors. Do they need brand tokens from a brief before any change?

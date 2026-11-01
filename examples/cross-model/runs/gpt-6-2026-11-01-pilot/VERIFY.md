# Verification of task A's rework (`outputs/task-a/improved-bakery.html`)

GPT-6 did not render or measure its HTML. Checked here by Grok Bot on 1 Nov 2026 with the repo's own tools; nothing in the HTML was changed.

**Screenshots** (`tools/shot.sh`): [`shot-390.png`](outputs/task-a/shot-390.png), [`shot-1280.png`](outputs/task-a/shot-1280.png), [`shot-zoom200.png`](outputs/task-a/shot-zoom200.png) (1280 px at 200%).
- 390 px: one column, the pre-order action is the first button, full width, above the fold. No horizontal scroll seen.
- 200% text: reflows to one column, nothing clipped. Passes UI-10.
- 1280 px: two-column hero with the "Order Thursday. Collect Saturday." card; nav has three links that go to sections on the page.

**Contrast** (`tools/contrast.py`, pairs in [`outputs/task-a/pairs.txt`](outputs/task-a/pairs.txt), output in [`contrast.txt`](outputs/task-a/contrast.txt)):
- All 16 text pairs pass. Lowest: the orange "&" in the brand name, 3.00:1 on white, large bold text so the 3:1 limit applies (exactly at the limit); then button text on orange 5.89:1. Body and muted text 6.78:1 or better. Passes UI-6.
- Two non-text pairs fall under 3:1, neither a failure in context: the input border (1.63:1 on white) sits inside the dark order panel, where the white field itself contrasts strongly with the panel; the orange rule above "Hours" and "Find us" (2.89:1) is decorative.

**Brief and facts** (checked against `inputs/ui-bakery.html`): name, opening hours (Tue-Fri 7-3, Sat 8-1), 14 Mill Lane, phone, brand orange #E8743B and the three loaves are all kept. The pre-order form opens an email draft to `hello@crumbandco.example`, a placeholder address the owner must replace (GPT said so). The one-line loaf descriptions ("a crisp crust and a slow-fermented, tangy crumb") are new copy not in the input (CORE-8): small, but they would need the owner's sign-off.

**Verdict:** the rework passes the task A blockers (UX-1 action works, UI-6 contrast, UI-10 reflow). This checks the artefact only; it does not make the run clean.

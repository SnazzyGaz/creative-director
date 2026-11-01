# Log: web-ui-takeover

Take-over case (section 4b). Round 1 was built badly on purpose, by hand in HTML, to stand in for the worst bot output. Code, so fixes apply exactly.

- r01: 3 MUST-BE-RIGHT failures at once: UX-1 (pre-order buttons go nowhere and are off-screen on a phone), UI-6 (11 of 11 text pairs fail, worst 1.13:1), UI-10 (fixed 1250 px absolute layout). Also six typefaces (UI-1), no hierarchy (CORE-1), filler copy (UX-6). Take over.
- r02: rebuilt from the brief, keeping all must-keeps (CD-5). Tokens first (colours, two typefaces, spacing scale), then a single-column flow. All 6 text pairs pass (min 6.31:1); nothing clips at 390 px or 200% zoom; blur test now leads with headline then button. Stopped: no blockers, clearly better.
- Honest notes: Creepster (one of r01's six fonts) is not installed and fell back to a serif; the six counted are the ones that rendered. The rework added placeholder copy (loaf descriptions, the Friday bake step) and an example.com email; first draft also invented prices and a 6 pm cut-off, which were removed before the screenshots because the brief did not give them.
- Brand orange as text fails on cream (2.79:1), so it moved to decoration and a darker shade carries text. A brand question, listed for the owner.

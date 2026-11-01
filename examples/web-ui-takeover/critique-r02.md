## Critique: Crumb & Co landing page, round 2 (the rework)

**Brief:** as round 1 (`brief.md`).
**Criteria judged against:** as round 1.
**Evidence looked at:** round-02-390.png, round-02-1280.png, round-02-zoom200.png; look-r02.png; contrast-r02.txt.

### Brief check (CD-1, CD-5)
- Answers the brief: yes. The one idea is the lede and is repeated as three steps; the action sits directly under it.
- Must-keeps intact: name, pre-order action, hours, address, the three loaves: yes. Brand orange #E8743B: kept for the loaf rules; a darker shade (#9a3f12) carries text and the button, because #E8743B on the cream ground is 2.79:1 and would fail UI-6 as text.
- Not from the brief, added as placeholder copy: the short loaf descriptions and "Friday night: we bake them". Flagged under Questions.

### Test results (evidence)
- Squint/blur: headline, then the dark button, then the steps card. Matches the brief's order.
- Thumbnail: name, headline and button readable at 200 px.
- Flip/mirror: one left edge for all text on the phone; nothing tilted.
- Greyscale: three value groups (dark text and button, white card, cream ground). Button stays the darkest large shape.
- Crop/edges: no clipping at 390 px or at 200% zoom.

### Meets criteria
- UX-1: one real pre-order link, visible without scrolling at 390 px.
- UI-6: 6 of 6 text pairs pass (min 6.31:1 large headline accent; body 14.66:1).
- UI-10 / CORE-10: single-column flow; nothing clipped at 200% zoom.
- UI-1 / CORE-7: two typefaces (Fraunces display, Source Sans 3 text); five sizes.
- CORE-1 / UI-4: name > headline > action > steps > loaves > hours.
- UI-8 / CORE-6: one accent with one job (action and key times).

### Needs improvement (ranked, max 5)
1. [IMPROVEMENT] UX-9 not met. Phone number and address are plain text; on a phone they could be tap targets. Fix: `tel:` and a map link.
2. [IMPROVEMENT] CORE-8. The lede and step 1/3 say the same thing on a phone, one above the other. Fix (optional): shorten the lede to one clause.
- Note: the orange rules are 2.79:1 against the ground. They are decorative (the loaf names carry the meaning), so WCAG's 3:1 non-text rule does not apply. Recorded, not a failure.

### Stop check
- No MUST-BE-RIGHT failures remain; clearly better than round 1 on every test. The remaining points are small. Stop and hand off.

### Questions for the owner
- Real order route: email (placeholder used), phone, or an ordering system?
- Placeholder copy: loaf descriptions and "Friday night: we bake them". Replace with real details, and add prices if wanted.
- Typeface: Fraunces + Source Sans 3 are stand-ins; is there a brand face?

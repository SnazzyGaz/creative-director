## Critique: parcel box and tin, round 1

**Brief:** see `brief.md`. Two-point perspective, eye level above the box.
**Criteria judged against:** CD-1, TD-PER-1, TD-PER-3, TD-PER-5, TD-ELL-1, TD-ELL-2, TD-ELL-3, TD-CON-1.
**Evidence looked at:** round-01.png (1200x800); look-r01.png; `tools/vp.py fit segments-r01.csv` (vp-r01.png); `tools/ellipse.py` on the tin's top and base (ell-r01-top.png); top ellipse at 2x zoom by eye.

### Brief check (CD-1, CD-5)
- Answers the brief: no. The box does not read as a solid with a flat lid; the tin looks tilted off the lid. Must-keeps present: corner toward viewer, tin on lid, line only: yes.

### Test results (evidence)
- Flip/mirror: the box leans; the tin tilts the other way. Both obvious when flipped.
- Thumbnail / blur / greyscale / edges: single-weight line drawing; these tests add little here. Nothing touches the frame.
- vp.py: left VP (-351, 60), right VP (1500, 260). Horizon tilt +6.18 deg; VP heights differ by 200 px.
- vp.py verticals: -3.73, -7.60 and +2.25 deg from vertical (three different leans).
- ellipse.py top: minor axis 19.4 deg off the tin's axis (14.3 with a box around the upper arc only). Base: 18.8 deg off. The tool's top degree (0.58) is wrong because the side lines pull the fit (see item 5). Construction values from `draw.py`: top degree 0.36, base 0.23.

### Meets criteria
- TD-PER-5: both VPs are well outside the object (1851 px apart for a 600 px box): no wide-angle distortion.
- TD-CON-1: built from two simple forms (box, cylinder).

### Needs improvement (ranked, max 5)
1. [BLOCKER] TD-PER-1 not met. Left and right VPs at different heights (200 px apart; horizon tilt 6.2 deg). Fix: one horizon; both VPs on it.
2. [BLOCKER] TD-PER-3 not met. Verticals lean -7.6 to +2.3 deg in different directions, with no third VP intended. Fix: all verticals truly vertical.
3. [BLOCKER] TD-ELL-1 not met. Both ellipses' minor axes are about 19 deg off the tin's centre line. Fix: minor axis along the axis (vertical here).
4. [BLOCKER] TD-ELL-2 not met. The base (further below eye level) is flatter (0.23) than the top (0.36); it should be fuller. Fix: base degree greater than top.
5. [BLOCKER] TD-ELL-3 not met, judged by eye at 2x zoom: the top ellipse comes to points at both ends (a "lemon"). **ellipse.py did not catch this** (end check "OK" in three box sizes): the tin's side lines fall inside any box that holds the whole top, and they pull the fit. See log.

### Take-over check (4b)
- Five MUST-BE-RIGHT failures at once, and no consistent horizon. **Take over: redraw by construction** (horizon first, then VPs, then box, then tin centred on the lid's diagonals).
- Keep (CD-5): corner toward viewer, tin on lid, line only.

### Questions for the owner
- Eye level: the redraw keeps "above the box" as briefed. Higher (more lid) or lower (more side)?

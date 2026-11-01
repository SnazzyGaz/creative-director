## Critique: mug render, round 3

**Evidence looked at:** round-03.png; measure.py; L* samples.

### Did the fixes apply?
1. Key, fill, rim: applied as placed, but **too strong**. Mug L* 96 / 97 / 91: the fall-off is barely visible; the near table is L* 92. The ratio is there but the overall level drowns it.
2. Dark backdrop: applied (far table and wall L* 35 and below).
3. Camera raised: applied; the opening and inner wall now read.

### Comparison
- Clipping 15.4% -> 1.8%. Opening visible. Better on 3D-5 (camera) and CORE-2 at the top of frame; still flat on the body.

### Needs improvement
1. [IMPROVEMENT] 3D-7 / 3D-5. Lights are too bright, so the key-to-fill modelling cannot show. Fix: scale all three lights down together (to 0.2x), keeping their ratio. 3D-7 says re-balance exposure after switching view transform.

### Round count
- Round 3 is the stop point for routine work. Going to round 4 (5 is the maximum) because the round-3 lighting fix was only half applied: right layout, wrong level. One change.

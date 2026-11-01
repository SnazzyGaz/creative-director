## Critique: mug render, round 2

**Evidence looked at:** round-02.png; measure.py; mug-r02 model-qa (same 2 intended mediums).

### Did the fixes apply?
1. AgX: applied. Clipped pixels 24.2% -> 15.4%.
2. Materials in range: applied (values in scene.py).
3. 48 segments, smooth, bevel: applied; the handle now reads round.

### Needs improvement (ranked)
1. [IMPROVEMENT] 3D-5 / TD-LIT-1 not met. Still one frontal light: mug L* 99 / 100 / 98 left to right. No modelling, so the body still reads flat. Fix: key light upper left, fill about 4:1, rim behind.
2. [IMPROVEMENT] CORE-2 not met. Mug (99) against a light grey wall (73): separation comes only from the edge. Fix: dark backdrop.
3. [IMPROVEMENT] 3D-5 (camera). Camera at mug mid-height: the top opening is not visible, which is what says "mug" rather than "cylinder". Fix: raise the camera to look slightly down.

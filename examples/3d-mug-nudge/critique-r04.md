## Critique: mug render, round 4

**Evidence looked at:** round-04.png; look-r04.png; measure.py; qa-r04.txt.

### Did the fix apply?
- Lights scaled to 0.2x: applied. Clipped pixels 0.0%. L* p95 85.

### Meets criteria
- 3D-1, 3D-2: unchanged (model-qa: 0 high; same 2 intended mediums).
- 3D-4: round body and handle; rim bevel catches a line of light.
- 3D-6: materials in range (ceramic ~226 sRGB, metalness 0; table ~92,70,54).
- 3D-7: AgX, nothing clipped.
- 3D-5 (camera): looks down into the opening; mug off the horizon line.

### Needs improvement (not done, ranked)
1. [IMPROVEMENT] 3D-5 / CORE-2 partly met. Mug L* 84 / 85 / 74: the right side turns, but the left-to-centre body is still nearly even, and the near table (75) sits close to the mug's value. The rim light does not register.
- Fix, if continued: lower the fill further (toward 8:1) or move the key more to the side; darken the table one step.

### Stop check
- Clearly better than round 1 on every measured criterion. The remaining point is a lighting-mood choice (soft vs dramatic) more than a failure. Stop and hand off.

### Questions for the owner
- Soft, even product look (current, about 2:1 to 4:1) or more dramatic modelling (8:1)? 3D-5 allows either; it depends on the shop's style.
- Will the mug be textured? (UV warning, see round 1.)

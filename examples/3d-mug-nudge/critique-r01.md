## Critique: mug render, round 1

**Brief:** see `brief.md`.
**Criteria judged against:** 3D-1, 3D-2, 3D-4, 3D-5, 3D-6, 3D-7, CORE-2, CORE-10, TD-LIT-1.
**Evidence looked at:** round-01.png (960x720); look-r01.png; qa-r01.txt (`model-qa check --no-render --brief --profile render`); measure.py (clipped pixels, L* samples); material values from scene.py.

### Brief check (CD-1, CD-5)
- Answers the brief: partly. A mug is recognisable, but it reads as a flat white cut-out. Must-keeps: white mug, 95 mm, on a table: yes.

### Test results (evidence)
- Squint/blur: the mug and the hot spot on the table below it merge into one white shape.
- Thumbnail: silhouette reads; no form inside it.
- Greyscale: mug L* 100 at left, centre and right (no shading at all); wall 82; table 51.
- Crop/edges: centred, camera at mug mid-height, the table edge crosses behind the mug at about two-thirds of its height.
- measure.py: 24.2% of pixels clipped (a channel at 250 or more).

### Meets criteria
- 3D-1: model-qa reports 0 high; 2 medium, both judged intended for this render: NEAR_GROUND on the handle (it is attached to the body, not meant to touch the table) and UV_ZERO_AREA on the body (the mug is untextured; listed as a question).
- 3D-2: 95 mm tall, Z up, resting on the table.

### Needs improvement (ranked, max 5)
1. [IMPROVEMENT] 3D-7 not met. "Standard" view transform; mug clipped to flat white (L* 100 across the body; 24.2% of the frame clipped). Fix: AgX.
2. [IMPROVEMENT] 3D-6 not met. Ceramic base colour pure white (255) with metalness 0.5; table pure black (0). Fix: ceramic ~226,222,214 sRGB, metalness 0; table ~92,70,54 sRGB.
3. [IMPROVEMENT] 3D-4 not met. 8-sided body and handle, flat shaded, no bevel: facets visible on the handle. Fix: 48 segments, smooth shading, small rim bevel.
4. [IMPROVEMENT] 3D-5 / TD-LIT-1 / CORE-2 not met. One light from the camera position: no modelling; light wall behind a white mug. Next round.

### Take-over check (4b)
- No MUST-BE-RIGHT failures (3D-1 and 3D-2 pass). Readable at thumbnail. **Nudge**: fixes 1-3 this round.

### Questions for the owner
- Will the mug be textured later? If so, the UV_ZERO_AREA warning becomes a real problem to fix.

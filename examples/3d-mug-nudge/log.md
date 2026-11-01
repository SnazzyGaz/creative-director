# Log: 3d-mug-nudge

Nudge case. Real Blender 4.2 Cycles renders from `scene.py` (the .blend files are not committed; rebuild with `blender -b -P scene.py -- N`).

- r01: built correctly (model-qa: 0 high; 2 medium judged intended). Looks: 3D-7 (Standard view, mug clipped to L* 100, 24.2% of frame clipped), 3D-6 (albedo 255 white with metalness 0.5; table pure black), 3D-4 (8-sided, flat shaded), 3D-5 (one frontal light). Nudge.
- r02: AgX, plausible materials, 48 segments with smooth shading and bevel. All applied. Clipping 15.4%; still flat (one frontal light).
- r03: key/fill/rim, dark backdrop, raised camera. All placed, but the lights were too strong: clipping 1.8%, body still near-white.
- r04: one change, lights to 0.2x. Clipping 0%; form starts to read. Went one round past the routine stop because r03's fix was half applied. Stopped with the key-to-fill ratio as a question for the owner.
- Honest notes: the first round-1 render also had exposure +1 and came out almost entirely white; that was dialled back to exposure 0 before critique so round 1 shows typical defaults rather than an extreme. The light energies in r03 were a guess and were wrong by about 5x. Rim light never became visible.

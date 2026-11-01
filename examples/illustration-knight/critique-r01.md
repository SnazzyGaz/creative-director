## Critique: knight and castle, round 1

**Brief:** generic one-line prompt: a lone knight on a hill looking at a distant castle at sunset. Focal point: the knight; story target: the castle. 1280x720, seen in a feed at ~300 px.
**Criteria judged against:** CORE-1, CORE-2, CORE-3, CORE-8, CORE-10, ILL-1, ILL-2, ILL-3, ILL-5, ILL-6, TD-LIT-1.
**Evidence looked at:** round-01.png (1280x720); look-r01.png (tools/look.py).

### Test results (evidence)
- Squint/blur: highest blurred contrast is in the sky and sun band (grid rows 1-2, up to 2.2); knight region (rows 3-4, left) is 0.4-0.9. The sky leads, not the knight.
- Thumbnail: helmet and shoulders read against the sky; lower body and legs merge with the forest.
- Flip/mirror: no tilt or lopsided weight found.
- Greyscale: L* mean 26; histogram skewed dark (31% in the darkest bin), no clear light group except the sun.
- Crop/edges: no tangents at the frame; clouds are hard-edged across the whole top third.

### Meets criteria
- ILL-3: helmet and shoulders form a clear silhouette against the sky.
- TD-LIT-1: one light source (low sun behind), shadows consistent.
- ILL-1: horizon and knight placement divide the frame unequally.
- ILL-6: the castle gives the knight's gaze a target; keep it.

### Needs improvement (ranked)
1. [IMPROVEMENT] CORE-3 / ILL-2 not met. Peak contrast and detail are at the sun and clouds, not the knight. Fix: simplify the sky (fewer, softer clouds; softer sun).
2. [IMPROVEMENT] ILL-3 / CORE-2 not met. Knight's lower body and cape sit in the same dark value as the forest. Fix: add light warm mist behind the legs and lower cape.
3. [IMPROVEMENT] ILL-3 not met. Knight's back edge has no separation from the hill. Fix: warm rim light on the back edge, helmet and shoulder.
4. [IMPROVEMENT] CORE-8 / ILL-5 not met. Detail is spread evenly (clouds, trees, grass). Covered by fix 1 for now.

### Next round
- Apply fixes 1-3 as an image edit with round-01 as reference. Compare with round 1.

### Questions for the owner
- Sunset orange-teal is the generic AI default here. Keep it, or ask for a different light family?

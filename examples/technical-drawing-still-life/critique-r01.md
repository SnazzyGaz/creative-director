## Critique: box and can still life, round 1

**Brief:** generic prompt: pencil drawing of an open cardboard box and a tin can on a table, two-point perspective. Teaching-style still life.
**Criteria judged against:** TD-PER-1, TD-PER-3, TD-ELL-1, TD-ELL-2, TD-LIT-1, TD-LIT-3, CORE-2, CORE-10.
**Evidence looked at:** round-01.png (1152x864); look-r01.png; grid overlay with box edges picked by eye and extended in Python.

### Test results (evidence)
- Squint/blur: box and can both read; nothing competes.
- Thumbnail: both objects read at ~200 px.
- Flip/mirror: the box leans when flipped (see TD-PER-3).
- Greyscale: very high key (L* p50 94; 67% in the lightest bin).
- Crop/edges: no tangents.
- Perspective (judged endpoints, computed intersections): left-face edges meet about 140 px above the frame top; right-face edges meet about 830 px above. The two VPs sit at very different heights: implied horizon tilted ~13 degrees.
- Verticals (judged): all three box verticals shear the same way (x drifts ~6-16 px over the edge).
- Ellipses (judged at 2x zoom): can top ratio ~0.32, base ~0.49. Base is more open.

### Meets criteria
- TD-ELL-2: base ellipse is more open than the top (measured at zoom; first read at normal size said otherwise).
- TD-LIT-1, TD-LIT-3: one light from upper left, cast shadows to lower right touching the bases.

### Needs improvement (ranked)
1. [BLOCKER] TD-PER-1 not met. Box: the two vanishing points are at different heights, so there is no consistent horizon.
2. [BLOCKER] TD-PER-3 not met. Box verticals are not vertical; they all shear the same way.
3. [IMPROVEMENT] CORE-2 unclear. Very light overall; may be fine for a pencil sketch (see Questions).

### Take-over check (critique-loop 4b)
- No consistent horizon "breaks the whole piece". Take over: regenerate with the construction spelled out, rather than three small edits.

### Next round
- Rework prompt: one level horizon slightly above the objects; both VPs on it, far outside the frame; verticals perfectly vertical; base ellipse more open than the top; light upper left, shadows touching the bases.

### Questions for Gaz
- Is a high-key, light pencil sketch a deliberate exception to CORE-2, or should it carry a darker value group?

## Critique: "The keeper's cat", round 1

**Brief:** see `brief.md`. Focal point: the cat, waiting for the boat. Needs a quiet area for text.
**Criteria judged against:** CD-1, CD-5, CORE-1, CORE-2, CORE-3, CORE-6, CORE-8, CORE-10, ILL-1, ILL-2, ILL-4, ILL-5, ILL-6, ILL-11, TD-LIT-1.
**Evidence looked at:** round-01.png (1024x768, GenerateImage); look-r01.png (tools/look.py).

### Brief check (CD-1, CD-5)
- Answers the brief: no. The lighthouse is the subject; the cat is a small dark shape at lower centre-right, seen from behind. Two sailing ships appear; neither reads as "the keeper coming home". No quiet area for text: every region is filled.
- Must-keeps present: cat, lighthouse, storm, night: yes. The keeper's small boat: no (two tall ships instead).

### Test results (evidence)
- Squint/blur: the lamp and the light burst behind the tower lead. The cat merges with the dark rocks.
- Thumbnail: tower and rainbow sky read; the cat does not.
- Flip/mirror: the tower is on the exact vertical centre line; the picture is near-symmetrical.
- Greyscale: L* spread evenly across the full range (histogram ~13% in each of the lower bins); no planned value groups. Sparkles add bright points across the whole lower half.
- Crop/edges: lightning and saturated colour run into every edge and corner. The blurred-contrast grid is 1.5-2.7 in all 16 cells: no quiet region anywhere.

### Meets criteria
- CORE-2 (partly): the cat's silhouette is darker than the sky behind the tower. That is the only value separation the subject has.

### Needs improvement (ranked, max 5)
1. [BLOCKER] TD-LIT-1 not met. At least four light directions: the lamp, a burst from behind the tower, lightning both sides, and point-light sparkles on the rocks lighting nothing consistently.
2. [IMPROVEMENT] ILL-2 / CORE-3 not met. Highest contrast is the lamp and the sky, not the cat (blur and thumbnail tests).
3. [IMPROVEMENT] ILL-11 / CORE-8 not met. Generic AI look: rainbow nebula sky, sparkles, god rays, lens glow, everything equally sharp (ILL-5), symmetrical centred subject (ILL-1).
4. [IMPROVEMENT] ILL-6 not met. No readable moment: the cat faces away and no boat reads as the keeper's.
5. [IMPROVEMENT] ILL-4 / CORE-6 not met. Full spectrum of saturated hues, none with a job.

### Take-over check (4b)
- Fails the brief's focal point at blur and thumbnail; one MUST-BE-RIGHT failure that runs through the whole picture (light); unusable for its purpose (no space for text, wrong boat); fixing it in three-change rounds would take well over three rounds. **Take over: regenerate with the composition, values and light written into the prompt.**
- Keep (CD-5): cat, lighthouse, stormy night sea; restore the small boat.

### Questions for the owner
- Painted (gouache) or digital look for the book? The rework uses gouache as a stand-in.

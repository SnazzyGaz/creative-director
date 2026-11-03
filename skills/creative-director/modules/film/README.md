# Module: film

Cinematography and the moving image: live-action footage, generated video clips, animation, storyboards, animatics, shot lists, edits, trailers and social video. Load with `core/`. Story comes first: read `story.md` before these craft rules, because every rule here is a tool for a story beat, not a goal of its own.

| File | What it holds | Load when |
|---|---|---|
| `README.md` (this file) | Craft rules: shots, continuity, camera, light, flashing and captions | any moving-image work |
| `edit.md` | Colour and grading, editing and pacing, composition in motion, sound, on-screen text | grading, cutting, titles, subtitles or sound; any full review |
| `notes.md` | Look vocabulary (film looks by technique) and film myths | optional: a brief asks for "a film look", or a myth is offered as a reason |
| `story.md` | Story first: the beat check (FILM-STORY-0), framing, colour, light, movement, music, editing and motifs as storytelling | always with this module; it is the core of it |
| `generated.md` | Generated video: failures (identity drift, morphing, physics, flicker, invented text) and the frame-sampling QC checklist | AI or generated clips, or any clip a model touched |
| `review.md` | How to review moving work (in motion, hands-on, then frames) and the film critique template | every critique of a clip, sequence, edit or storyboard |
| `crossover.md` | Which repo rules apply to film as they are, which change in motion, and which are film-only | when unsure whether a still-image rule applies |
| `diagrams/axis-180-30.svg` | Overhead diagram of the 180° line and 30° rule (not in the skill folder; the text stands alone) | if a picture helps |

Format: **What / Why / Check / Fix / Auto / Grade / Source**, as in the other modules. Grades follow `core/evidence.md`. "Craft wisdom" here means long agreement among teachers and working crews; where a claim rests on one practitioner it says so. Sources are `[SRC-267]` to `[SRC-331]` in `SOURCES.md`.

**Conventions, not laws.** Continuity rules (180°, 30°, eyelines, screen direction) are conventions that keep space readable. Break one when the beat wants disorientation or a jolt, and write the reason down as a deliberate exception. An accidental break is a fault; a chosen one is a choice.

**Blockers (MUST-BE-RIGHT):** FILM-ACC-1 (flashing), FILM-LIT-1 within one continuous scene, and the generated-video checks marked so in `generated.md` (identity, anatomy, invented text). Everything else is a default with a reason.

**Review in motion.** A clip is judged by watching it at full speed, at its delivered size, with sound, more than once. Stills and contact sheets find faults; they cannot judge rhythm, movement or performance (FILM-REV-1 in `review.md`).

---

## Shot grammar

### FILM-SHOT-1. Shot size matches what the viewer must read
- **What:** Choose the size (extreme wide, wide, full, medium, medium close-up, close-up, extreme close-up) for the information and feeling the beat needs: geography and scale in wides, behaviour in mediums, thought and feeling in close-ups.
- **Why:** Faces are read faster and more surely when larger; cluttered or wide frames need more screen time to read. Closer shots also raise viewers' tendency to think about a character's mind.
- **Check:** At the delivered screen size, can the viewer read the expression, prop or action the beat depends on, within the shot's duration? Does the scene vary size on purpose, or sit in one size by default?
- **Fix:** Go tighter for the read, or hold the wide longer (FILM-EDIT-3). Save the closest size for the beat that needs it most (FILM-STORY-2).
- **Auto:** no.
- **Grade:** Partly supported (face size and clutter [SRC-287]; close-ups and mental-state talk, a tendency, not ability [SRC-289]). Size vocabulary: craft wisdom [SRC-267, SRC-268, SRC-327].
- **Source:** [SRC-287, SRC-289, SRC-267, SRC-268, SRC-327].

### FILM-SHOT-2. Camera height and angle are chosen, not left at eye level by habit
- **What:** Eye level is neutral. High angles can diminish or reveal layout; low angles can enlarge or threaten; a tilted (Dutch) horizon adds unease. Pick each for a reason in the beat.
- **Why:** Angle shifts how people judge a subject, but the effect is small and depends on context and attention, so it is a lever, not a guarantee.
- **Check:** Name the reason for each non-eye-level angle. Is any tilt or extreme angle unexplained, or used so often it stops meaning anything?
- **Fix:** Return unmotivated angles to eye level; keep the strong angle for the beat that needs it. Also see ILL-16.
- **Auto:** partly (horizon tilt per frame with `tools/vp.py`, then judge).
- **Grade:** Partly supported, conditional (angle changed trait judgements [SRC-290]; in ads the effect appeared only under low motivation [SRC-291]). Meanings of angles: craft wisdom [SRC-267, SRC-270].
- **Source:** [SRC-290, SRC-291, SRC-267, SRC-270].

### FILM-SHOT-3. Perspective comes from camera distance; the lens chooses the crop
- **What:** How much a face bulges or a background looms depends on where the camera stands. Focal length only decides how much of that view fills the frame. "Wide-angle distortion" is being close; "telephoto compression" is being far.
- **Why:** Treating zoom as perspective gives faces with swollen noses from too close, or flat, airless space chosen by accident.
- **Check:** For each face close-up, how far was the camera? Very close (roughly under a metre) exaggerates near features. Does the depth feel (stretched or stacked) suit the beat?
- **Fix:** Move the camera, then pick the lens for the crop. For flattering faces, step back and use a longer lens. In generated video, ask for the distance in words ("shot from across the room") rather than only a focal length.
- **Auto:** no.
- **Grade:** Standard (optics). Which look suits which beat: craft wisdom.
- **Source:** [SRC-313, SRC-268].

### FILM-SHOT-4. Focus and depth of field point at the beat
- **What:** What is sharp is what the viewer is told to look at. Shallow focus isolates; deep focus lets the viewer choose within a staged frame. A focus pull moves attention and should land on time.
- **Why:** Blur is a strong depth and attention cue; misplaced focus sends the eye to the wrong thing, and shallow focus everywhere flattens every beat into the same isolation.
- **Check:** In each shot, is the sharp plane on the subject of the beat (eyes, for faces)? Is any pull late, early, or hunting? Is shallow focus used even where the staging needs both planes?
- **Fix:** Re-focus or re-stage; stop down for deep staging (FILM-COMP-3). Keep shallow focus for isolation the story wants.
- **Auto:** partly (sharpness maps per sampled frame flag a soft subject; judge by eye).
- **Grade:** Well supported that blur affects perceived depth and size [SRC-248]; use for story: craft wisdom [SRC-268, SRC-270].
- **Source:** [SRC-248, SRC-268, SRC-270].

### FILM-SHOT-5. Aspect ratio and safe areas suit every delivery
- **What:** Pick the aspect ratio for the delivery and the content, and protect the action for every crop it will get (16:9, 9:16, 1:1). Keep vital action inside action-safe (93% of width and height) and graphics inside graphics-safe (90%).
- **Why:** Edges get cropped by displays, players and reframes; a 9:16 cut of a 16:9 master loses most of the frame.
- **Check:** Overlay the safe areas and every target crop on sampled frames. Does the subject, eyeline and any text survive each?
- **Fix:** Re-frame, shoot or generate wider with the crop in mind, or make a separate vertical version. See LAY-4 for social safe zones.
- **Auto:** yes for text against safe areas; partly for subjects.
- **Grade:** Standard for safe areas [SRC-318]; ratio choice: craft wisdom.
- **Source:** [SRC-318, SRC-268].

### FILM-SHOT-6. Headroom and looking room
- **What:** Leave space in front of a face or moving subject in the direction it looks or travels, and keep headroom consistent between matched shots. In close-ups the top of the head may be cropped; the eyes usually sit in the upper part of the frame.
- **Why:** Faces facing into the frame are preferred, and cramped looking room reads as blocked or tense. Mismatched headroom in a shot/reverse-shot pair makes the cut bump.
- **Check:** Is the open side in front of each look? Do matched singles share headroom and eye height?
- **Fix:** Re-frame; keep the cramped version only when the beat wants confinement. Same rule as COMP-5.
- **Auto:** partly (face detection gives eye height and facing side per frame).
- **Grade:** Partly supported (inward bias in stills [SRC-218]); headroom conventions: craft wisdom [SRC-275].
- **Source:** [SRC-218, SRC-275, SRC-267].

## Continuity (conventions that keep space readable)

Event-segmentation work shows breaks in *action* move viewers' sense of a new event most, while spatial and time jumps cost less [SRC-282]. So guard action continuity hardest. Overhead plan of the 180° line and the 30° rule: [`diagrams/axis-180-30.svg`](diagrams/axis-180-30.svg) (the rules below don't depend on it).

### FILM-CON-1. Keep the cameras on one side of the 180° line
- **What:** Draw the line through two characters (or along a direction of travel). Shots from one side keep each person on their own side of the screen and keep looks and movement consistent. Picture it from above: two people face each other across a table; every camera sits on the near side of the line between them; a camera on the far side flips who is on the left.
- **Why:** Crossing the line flips screen positions and directions, so viewers briefly lose who is where. Continuity cues help attention move smoothly across cuts.
- **Check:** Sketch the overhead plan of the scene with the line and each camera position. Any camera across the line without a bridge?
- **Fix:** Cross on screen with a camera move, cut to a shot on the line (neutral), let a character's movement move the line, or use a cutaway. If the crossing is meant to unsettle, record it as a deliberate exception.
- **Auto:** partly (face positions across a shot/reverse-shot pair flag a flip).
- **Grade:** Craft wisdom, with a perceptual account (Partly supported) [SRC-277].
- **Source:** [SRC-277, SRC-272, SRC-267, SRC-270, SRC-326, SRC-330].

### FILM-CON-2. Cut to the same subject with a real change (the 30° rule)
- **What:** When cutting between two shots of the same subject, move the camera at least about 30° around it, or change shot size clearly (for example wide to medium close-up), or both.
- **Why:** A small change looks like a skip in time (a jump cut), not a new view.
- **Check:** For each cut between shots of the same subject, estimate the angle and size change. Small both? It reads as a jump.
- **Fix:** Change angle or size more, cut away in between, or embrace the jump cut as a chosen style and use it consistently.
- **Auto:** partly (high similarity between the last and first frames of a cut flags it).
- **Grade:** Craft wisdom [SRC-270, SRC-330]; that continuity-style cuts go unnoticed more often is Partly supported [SRC-278].
- **Source:** [SRC-270, SRC-330, SRC-278].

### FILM-CON-3. Eyelines meet
- **What:** In shot/reverse-shot, the person on screen left looks right of lens and the other looks left of lens, at matching heights for their relative heights, and at matching distance from the lens in matched singles.
- **Why:** Mismatched eyelines make people seem to look past each other, which breaks the conversation.
- **Check:** Mark where each looks in the pair. Do the looks point to where the other person sits in the master?
- **Fix:** Re-angle or re-frame; in generated work, regenerate with the look direction stated.
- **Auto:** partly (gaze direction estimates per frame).
- **Grade:** Craft wisdom [SRC-270, SRC-272, SRC-326].
- **Source:** [SRC-270, SRC-272, SRC-326].

### FILM-CON-4. Screen direction carries across cuts
- **What:** Something travelling right keeps travelling right after the cut, unless a turn is shown. A character exiting frame right enters the next shot from the left.
- **Why:** Reversed direction reads as turning back.
- **Check:** Arrow every movement across a sequence. Any reversal without a shown turn or a neutral shot?
- **Fix:** Flop only if nothing in frame betrays it (text, asymmetric faces and costumes, traffic side); otherwise re-shoot, re-generate or insert a neutral (head-on) shot.
- **Auto:** partly (dominant motion direction per shot from optical flow).
- **Grade:** Craft wisdom [SRC-267, SRC-272].
- **Source:** [SRC-267, SRC-272, SRC-270].

### FILM-CON-5. Match on action
- **What:** Cut during a movement and let it continue in the next shot: the hand reaching in the wide finishes the reach in the close-up.
- **Why:** Cuts made during motion go unnoticed far more often, because attention is on the movement.
- **Check:** Is the cut inside the movement, with the action neither repeated nor missing frames?
- **Fix:** Trim so the action overlaps by a frame or two at most.
- **Auto:** no.
- **Grade:** Partly supported (cuts during motion missed most often [SRC-278]; attentional account [SRC-277]).
- **Source:** [SRC-278, SRC-277, SRC-269].

### FILM-CON-6. Physical continuity holds inside a scene
- **What:** Props, costume, hair, make-up, wounds, liquid levels, weather and time of day stay the same from shot to shot unless the story changes them.
- **Why:** Viewers miss many changes, but the ones on the focus (a drink in a hand, a face) are caught and pull them out.
- **Check:** Contact sheet of the first and last frame of every shot in the scene; compare the things on the focus first.
- **Fix:** Re-shoot, re-generate, or cut around it. For generated clips, see FILM-GEN-2 to FILM-GEN-4.
- **Auto:** partly.
- **Grade:** Craft wisdom; that changes off the focus are often missed is Partly supported [SRC-278].
- **Source:** [SRC-278, SRC-268].

## Camera movement

### FILM-CAM-1. Every move has a motivation
- **What:** A move follows a subject, reveals something, approaches (intensifies), withdraws (releases or isolates), or takes a character's point of view. If it does none of these, lock off.
- **Why:** Unmotivated drift is the commonest weakness of generated clips and new crews; it tells the viewer to expect something that never comes.
- **Check:** Name the motivation of every move in one word. Any blank?
- **Fix:** Lock off, or make the move do one of those jobs (FILM-STORY-6).
- **Auto:** no.
- **Grade:** Craft wisdom [SRC-268, SRC-271]. Narrow evidence that smooth approaching camera movement engages viewers' motor responses more than a static or zoomed view: Partly supported [SRC-292].
- **Source:** [SRC-268, SRC-271, SRC-292].

### FILM-CAM-2. Moves start and land on composed frames, at a steady intent
- **What:** A move starts from a good frame, ends on a good frame, and changes speed smoothly (ease in and out) unless a snap is the point. Speed matches the scene's energy.
- **Why:** Moves that stop arbitrarily or wobble in speed read as accidents.
- **Check:** Freeze the first and last frames of each move; do both compose? Watch for speed jumps and drifting horizons.
- **Fix:** Trim to the composed part; stabilise or redo; re-time.
- **Auto:** partly (motion speed from optical flow over time).
- **Grade:** Craft wisdom [SRC-268, SRC-275].
- **Source:** [SRC-268, SRC-275].

### FILM-CAM-3. Shake is chosen, not suffered
- **What:** Handheld energy is a choice for subjectivity, urgency or closeness to a performer; tripod-calm is the default for observation. Accidental jitter, rolling-shutter wobble and stabiliser warping are faults.
- **Why:** Shake draws attention to the camera; when it doesn't serve the beat it reads as amateur.
- **Check:** Is the operating style the same across the scene unless the story shifts it? Any jelly, warp or bobbing horizon?
- **Fix:** Stabilise lightly (watch for warp), redo, or make the handheld consistent and responsive to the action.
- **Auto:** partly (camera motion spectrum from tracking).
- **Grade:** Craft wisdom; handheld as a response to the actor is one practitioner's account [SRC-325].
- **Source:** [SRC-325, SRC-268].

### FILM-CAM-4. Frame rate and shutter set the motion on purpose
- **What:** Motion blur follows the shutter angle: 180° (an exposure of 1/(2 × frame rate), so 1/48 s at 24 fps) is the usual default. Narrow shutters give crisp, staccato motion; wide ones smear. Slow motion is shot (or rendered) at a higher frame rate, not invented between frames where avoidable. Pick the frame rate for the delivery and the feel.
- **Why:** Mismatched blur (crisp backgrounds, smeared hands) or interpolated slow motion with warping edges look broken.
- **Check:** Step through fast action frame by frame. Is the blur consistent with one shutter? Any ghosting or warped edges from frame interpolation?
- **Fix:** Re-render with a set shutter; replace interpolated slow motion; conform frame rates before editing.
- **Auto:** partly (frame-difference spikes and duplicated frames show judder and pulldown).
- **Grade:** Standard (the shutter arithmetic); 180° as default: craft wisdom [SRC-268]. Viewers preferred higher frame rates in stereoscopic tests, so 24 fps is a convention, not a law [SRC-311, SRC-312].
- **Source:** [SRC-268, SRC-311, SRC-312].

## Light

### FILM-LIT-1. One key direction per setup, held across the cuts of a scene (MUST-BE-RIGHT within one continuous scene)
- **What:** Within one moment in one place, the main light comes from one consistent side relative to the world source (window, lamp, sun), in every angle of coverage. The key may be cheated a little per angle, but not flipped.
- **Why:** If the light jumps sides between shot and reverse shot, the cut reads as a different time or place. This is TD-LIT-1 extended across time.
- **Check:** For each shot in the scene, note which side of the face is lit and where cast shadows fall. Do they agree with the master and the source?
- **Fix:** Relight, regrade (shapes of shadow can't be graded away), or regenerate. A change of light is fine when the story motivates it (a door opens, a cloud passes) and the change is shown.
- **Auto:** partly (bright side of detected faces per frame).
- **Grade:** Standard within the scene (light physics; see TD-LIT-1). Cheating per angle: craft wisdom [SRC-268, SRC-324].
- **Source:** [SRC-268, SRC-324, SRC-274]; TD-LIT-1, CV-7.

### FILM-LIT-2. Light is motivated by the world
- **What:** Every source can be explained by something seen or implied: a window, a practical lamp, a screen, fire, sky. Rim and back light have a believable source too.
- **Why:** Unmotivated glow (a rim on every edge, light from nowhere) is the generic look (ILL-11) and flattens mood.
- **Check:** Name the source of key, fill and back light in each setup. Any "from nowhere"?
- **Fix:** Add or reveal the source, or remove the light.
- **Auto:** no.
- **Grade:** Craft wisdom [SRC-268, SRC-274, SRC-322, SRC-323].
- **Source:** [SRC-268, SRC-274, SRC-322, SRC-323].

### FILM-LIT-3. The key-to-fill ratio is set for the mood and held within the scene
- **What:** Ratio is the difference between the lit and shadow side, counted in stops (each stop doubles the light): about 1 stop (2:1) is soft and even, 2 stops (4:1) is shaped, 3 stops or more (8:1+) is low key. Negative fill deepens the shadow side.
- **Why:** The ratio sets high key or low key; drifting ratios between shots of one scene make the cut bump.
- **Check:** Measure lit-cheek against shadow-cheek luminance on faces in sampled frames (or read them on a waveform or false-colour view). Same ratio across the scene?
- **Fix:** Relight; grade to match where the shapes allow it.
- **Auto:** yes (luminance sampling on face regions).
- **Grade:** Standard (the arithmetic of stops); which ratio suits which mood: craft wisdom [SRC-268, SRC-273, SRC-329].
- **Source:** [SRC-268, SRC-273, SRC-329].

### FILM-LIT-4. The subject separates from the background
- **What:** Value, edge light, colour or depth separates the subject from what is behind it, at the beat's focus.
- **Why:** In motion, viewers have little time; weak separation loses the subject behind clutter.
- **Check:** Greyscale and blur a frame from each beat (CORE-2, CV-3). Does the subject read as its own shape?
- **Fix:** Darken or lighten the background, add a motivated edge light, or move the subject.
- **Auto:** partly (`tools/look.py` on sampled frames).
- **Grade:** Craft wisdom, consistent with figure-ground evidence [SRC-37].
- **Source:** [SRC-268, SRC-37]; CV-1, CV-3.

### FILM-LIT-5. Practicals read as sources and protect the latitude
- **What:** Lamps, screens and windows in frame are exposed so they read as light sources (some detail or a gentle bloom), not as dead grey or a clipped hole. Skin never clips by accident; shadows are crushed only when chosen.
- **Why:** The image's latitude (the range from black to white that holds detail) is finite; clipping on faces and dead practicals look like mistakes.
- **Check:** Waveform or histogram per shot; zoom on highlights on faces and practicals; check the delivered SDR and HDR versions.
- **Fix:** Dim the practical, lift or lower exposure, or protect highlights in the grade. See 3D-7 for view transforms in renders.
- **Auto:** yes (clipped pixels in face and practical regions).
- **Grade:** Standard (sensor and display range); exposure for practicals: craft wisdom [SRC-323, SRC-268].
- **Source:** [SRC-323, SRC-268].

## Accessibility

### FILM-ACC-1. No flashing above the threshold (MUST-BE-RIGHT)
- **What:** No more than three general flashes or three red flashes in any one-second period, unless the flashing area is small (under about a quarter of a 10° field of view; 341 × 256 px at 1024 × 768). A general flash is a pair of opposing changes in relative luminance of 10% or more where the darker state is below 0.80; red flashes have their own definition. Broadcast has its own (stricter) guidance, and stripes and regular patterns can be a hazard too.
- **Why:** Flashing can trigger seizures in people with photosensitive epilepsy.
- **Check:** Look for strobes, lightning, muzzle flashes, rapid cuts between light and dark, and flickering generated textures. Analyse at full-screen size; loop short clips. For broadcast, run a photosensitive-epilepsy analyser.
- **Fix:** Slow the flashes, shrink the flashing area, or cut its contrast.
- **Auto:** yes (frame-luminance analysis; a pass is a strong signal, not a guarantee).
- **Grade:** Standard [SRC-314, SRC-315].
- **Source:** [SRC-314, SRC-315].

### FILM-ACC-2. Captions for speech and sound, description where only the picture tells
- **What:** Prerecorded video with speech has captions that include plot-relevant sounds; where the picture carries information no one says aloud, provide audio description or a text alternative.
- **Why:** Deaf, hard-of-hearing and blind viewers otherwise miss the story.
- **Check:** Are captions present, accurate and synced? Is any key story point purely visual?
- **Fix:** Add captions (FILM-TXT-2) and description.
- **Auto:** partly.
- **Grade:** Standard [SRC-314].
- **Source:** [SRC-314].

---

## Colour, editing, motion, sound, text and myths

In [`edit.md`](edit.md): grading FILM-COL-1 to 4, editing FILM-EDIT-1 to 6, composition in motion FILM-COMP-1 to 4, sound FILM-SND-1 and 2, on-screen text FILM-TXT-1 to 3. Look vocabulary and film myths: [`notes.md`](notes.md).

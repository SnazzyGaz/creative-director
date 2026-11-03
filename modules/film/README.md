# Module: film

Cinematography and the moving image: live-action footage, generated video clips, animation, storyboards, animatics, shot lists, edits, trailers and social video. Load with `core/`. Story comes first: read `story.md` before these craft rules, because every rule here is a tool for a story beat, not a goal of its own.

| File | What it holds | Load when |
|---|---|---|
| `README.md` (this file) | Craft rules: shots, continuity, camera, light, colour, editing, composition in motion, sound, on-screen text, flashing; film myths | any moving-image work |
| `story.md` | Story first: the beat check (FILM-STORY-0), framing, colour, light, movement, music, editing and motifs as storytelling | always with this module; it is the core of it |
| `generated.md` | Generated video: failures (identity drift, morphing, physics, flicker, invented text) and the frame-sampling QC checklist | AI or generated clips, or any clip a model touched |
| `review.md` | How to review moving work (in motion, hands-on, then frames) and the film critique template | every critique of a clip, sequence, edit or storyboard |
| `crossover.md` | Which repo rules apply to film as they are, which change in motion, and which are film-only | when unsure whether a still-image rule applies |
| `diagrams/axis-180-30.svg` | One small overhead diagram of the 180° line and the 30° rule (not in the skill folder; the text below stands alone) | if a picture helps |

Format: **What / Why / Check / Fix / Auto / Grade / Source**, as in the other modules. Grades follow `core/evidence.md`. "Craft wisdom" here means long agreement among teachers and working crews; where a claim rests on one practitioner it says so. Sources are `[S267]` to `[S331]` in `SOURCES.md`.

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
- **Grade:** Partly supported (face size and clutter [S287]; close-ups and mental-state talk, a tendency, not ability [S289]). Size vocabulary: craft wisdom [S267, S268, S327].
- **Source:** [S287, S289, S267, S268, S327].

### FILM-SHOT-2. Camera height and angle are chosen, not left at eye level by habit
- **What:** Eye level is neutral. High angles can diminish or reveal layout; low angles can enlarge or threaten; a tilted (Dutch) horizon adds unease. Pick each for a reason in the beat.
- **Why:** Angle shifts how people judge a subject, but the effect is small and depends on context and attention, so it is a lever, not a guarantee.
- **Check:** Name the reason for each non-eye-level angle. Is any tilt or extreme angle unexplained, or used so often it stops meaning anything?
- **Fix:** Return unmotivated angles to eye level; keep the strong angle for the beat that needs it. Also see ILL-16.
- **Auto:** partly (horizon tilt per frame with `tools/vp.py`, then judge).
- **Grade:** Partly supported, conditional (angle changed trait judgements [S290]; in ads the effect appeared only under low motivation [S291]). Meanings of angles: craft wisdom [S267, S270].
- **Source:** [S290, S291, S267, S270].

### FILM-SHOT-3. Perspective comes from camera distance; the lens chooses the crop
- **What:** How much a face bulges or a background looms depends on where the camera stands. Focal length only decides how much of that view fills the frame. "Wide-angle distortion" is being close; "telephoto compression" is being far.
- **Why:** Treating zoom as perspective gives faces with swollen noses from too close, or flat, airless space chosen by accident.
- **Check:** For each face close-up, how far was the camera? Very close (roughly under a metre) exaggerates near features. Does the depth feel (stretched or stacked) suit the beat?
- **Fix:** Move the camera, then pick the lens for the crop. For flattering faces, step back and use a longer lens. In generated video, ask for the distance in words ("shot from across the room") rather than only a focal length.
- **Auto:** no.
- **Grade:** Standard (optics). Which look suits which beat: craft wisdom.
- **Source:** [S313, S268].

### FILM-SHOT-4. Focus and depth of field point at the beat
- **What:** What is sharp is what the viewer is told to look at. Shallow focus isolates; deep focus lets the viewer choose within a staged frame. A focus pull moves attention and should land on time.
- **Why:** Blur is a strong depth and attention cue; misplaced focus sends the eye to the wrong thing, and shallow focus everywhere flattens every beat into the same isolation.
- **Check:** In each shot, is the sharp plane on the subject of the beat (eyes, for faces)? Is any pull late, early, or hunting? Is shallow focus used even where the staging needs both planes?
- **Fix:** Re-focus or re-stage; stop down for deep staging (FILM-COMP-3). Keep shallow focus for isolation the story wants.
- **Auto:** partly (sharpness maps per sampled frame flag a soft subject; judge by eye).
- **Grade:** Well supported that blur affects perceived depth and size [S248]; use for story: craft wisdom [S268, S270].
- **Source:** [S248, S268, S270].

### FILM-SHOT-5. Aspect ratio and safe areas suit every delivery
- **What:** Pick the aspect ratio for the delivery and the content, and protect the action for every crop it will get (16:9, 9:16, 1:1). Keep vital action inside action-safe (93% of width and height) and graphics inside graphics-safe (90%).
- **Why:** Edges get cropped by displays, players and reframes; a 9:16 cut of a 16:9 master loses most of the frame.
- **Check:** Overlay the safe areas and every target crop on sampled frames. Does the subject, eyeline and any text survive each?
- **Fix:** Re-frame, shoot or generate wider with the crop in mind, or make a separate vertical version. See LAY-4 for social safe zones.
- **Auto:** yes for text against safe areas; partly for subjects.
- **Grade:** Standard for safe areas [S318]; ratio choice: craft wisdom.
- **Source:** [S318, S268].

### FILM-SHOT-6. Headroom and looking room
- **What:** Leave space in front of a face or moving subject in the direction it looks or travels, and keep headroom consistent between matched shots. In close-ups the top of the head may be cropped; the eyes usually sit in the upper part of the frame.
- **Why:** Faces facing into the frame are preferred, and cramped looking room reads as blocked or tense. Mismatched headroom in a shot/reverse-shot pair makes the cut bump.
- **Check:** Is the open side in front of each look? Do matched singles share headroom and eye height?
- **Fix:** Re-frame; keep the cramped version only when the beat wants confinement. Same rule as COMP-5.
- **Auto:** partly (face detection gives eye height and facing side per frame).
- **Grade:** Partly supported (inward bias in stills [S218]); headroom conventions: craft wisdom [S275].
- **Source:** [S218, S275, S267].

## Continuity (conventions that keep space readable)

Event-segmentation work shows breaks in *action* move viewers' sense of a new event most, while spatial and time jumps cost less [S282]. So guard action continuity hardest. Overhead plan of the 180° line and the 30° rule: [`diagrams/axis-180-30.svg`](diagrams/axis-180-30.svg) (the rules below don't depend on it).

### FILM-CON-1. Keep the cameras on one side of the 180° line
- **What:** Draw the line through two characters (or along a direction of travel). Shots from one side keep each person on their own side of the screen and keep looks and movement consistent. Picture it from above: two people face each other across a table; every camera sits on the near side of the line between them; a camera on the far side flips who is on the left.
- **Why:** Crossing the line flips screen positions and directions, so viewers briefly lose who is where. Continuity cues help attention move smoothly across cuts.
- **Check:** Sketch the overhead plan of the scene with the line and each camera position. Any camera across the line without a bridge?
- **Fix:** Cross on screen with a camera move, cut to a shot on the line (neutral), let a character's movement move the line, or use a cutaway. If the crossing is meant to unsettle, record it as a deliberate exception.
- **Auto:** partly (face positions across a shot/reverse-shot pair flag a flip).
- **Grade:** Craft wisdom, with a perceptual account (Partly supported) [S277].
- **Source:** [S277, S272, S267, S270, S326, S330].

### FILM-CON-2. Cut to the same subject with a real change (the 30° rule)
- **What:** When cutting between two shots of the same subject, move the camera at least about 30° around it, or change shot size clearly (for example wide to medium close-up), or both.
- **Why:** A small change looks like a skip in time (a jump cut), not a new view.
- **Check:** For each cut between shots of the same subject, estimate the angle and size change. Small both? It reads as a jump.
- **Fix:** Change angle or size more, cut away in between, or embrace the jump cut as a chosen style and use it consistently.
- **Auto:** partly (high similarity between the last and first frames of a cut flags it).
- **Grade:** Craft wisdom [S270, S330]; that continuity-style cuts go unnoticed more often is Partly supported [S278].
- **Source:** [S270, S330, S278].

### FILM-CON-3. Eyelines meet
- **What:** In shot/reverse-shot, the person on screen left looks right of lens and the other looks left of lens, at matching heights for their relative heights, and at matching distance from the lens in matched singles.
- **Why:** Mismatched eyelines make people seem to look past each other, which breaks the conversation.
- **Check:** Mark where each looks in the pair. Do the looks point to where the other person sits in the master?
- **Fix:** Re-angle or re-frame; in generated work, regenerate with the look direction stated.
- **Auto:** partly (gaze direction estimates per frame).
- **Grade:** Craft wisdom [S270, S272, S326].
- **Source:** [S270, S272, S326].

### FILM-CON-4. Screen direction carries across cuts
- **What:** Something travelling right keeps travelling right after the cut, unless a turn is shown. A character exiting frame right enters the next shot from the left.
- **Why:** Reversed direction reads as turning back.
- **Check:** Arrow every movement across a sequence. Any reversal without a shown turn or a neutral shot?
- **Fix:** Flop only if nothing in frame betrays it (text, asymmetric faces and costumes, traffic side); otherwise re-shoot, re-generate or insert a neutral (head-on) shot.
- **Auto:** partly (dominant motion direction per shot from optical flow).
- **Grade:** Craft wisdom [S267, S272].
- **Source:** [S267, S272, S270].

### FILM-CON-5. Match on action
- **What:** Cut during a movement and let it continue in the next shot: the hand reaching in the wide finishes the reach in the close-up.
- **Why:** Cuts made during motion go unnoticed far more often, because attention is on the movement.
- **Check:** Is the cut inside the movement, with the action neither repeated nor missing frames?
- **Fix:** Trim so the action overlaps by a frame or two at most.
- **Auto:** no.
- **Grade:** Partly supported (cuts during motion missed most often [S278]; attentional account [S277]).
- **Source:** [S278, S277, S269].

### FILM-CON-6. Physical continuity holds inside a scene
- **What:** Props, costume, hair, make-up, wounds, liquid levels, weather and time of day stay the same from shot to shot unless the story changes them.
- **Why:** Viewers miss many changes, but the ones on the focus (a drink in a hand, a face) are caught and pull them out.
- **Check:** Contact sheet of the first and last frame of every shot in the scene; compare the things on the focus first.
- **Fix:** Re-shoot, re-generate, or cut around it. For generated clips, see FILM-GEN-2 to FILM-GEN-4.
- **Auto:** partly.
- **Grade:** Craft wisdom; that changes off the focus are often missed is Partly supported [S278].
- **Source:** [S278, S268].

## Camera movement

### FILM-CAM-1. Every move has a motivation
- **What:** A move follows a subject, reveals something, approaches (intensifies), withdraws (releases or isolates), or takes a character's point of view. If it does none of these, lock off.
- **Why:** Unmotivated drift is the commonest weakness of generated clips and new crews; it tells the viewer to expect something that never comes.
- **Check:** Name the motivation of every move in one word. Any blank?
- **Fix:** Lock off, or make the move do one of those jobs (FILM-STORY-6).
- **Auto:** no.
- **Grade:** Craft wisdom [S268, S271]. Narrow evidence that smooth approaching camera movement engages viewers' motor responses more than a static or zoomed view: Partly supported [S292].
- **Source:** [S268, S271, S292].

### FILM-CAM-2. Moves start and land on composed frames, at a steady intent
- **What:** A move starts from a good frame, ends on a good frame, and changes speed smoothly (ease in and out) unless a snap is the point. Speed matches the scene's energy.
- **Why:** Moves that stop arbitrarily or wobble in speed read as accidents.
- **Check:** Freeze the first and last frames of each move; do both compose? Watch for speed jumps and drifting horizons.
- **Fix:** Trim to the composed part; stabilise or redo; re-time.
- **Auto:** partly (motion speed from optical flow over time).
- **Grade:** Craft wisdom [S268, S275].
- **Source:** [S268, S275].

### FILM-CAM-3. Shake is chosen, not suffered
- **What:** Handheld energy is a choice for subjectivity, urgency or closeness to a performer; tripod-calm is the default for observation. Accidental jitter, rolling-shutter wobble and stabiliser warping are faults.
- **Why:** Shake draws attention to the camera; when it doesn't serve the beat it reads as amateur.
- **Check:** Is the operating style the same across the scene unless the story shifts it? Any jelly, warp or bobbing horizon?
- **Fix:** Stabilise lightly (watch for warp), redo, or make the handheld consistent and responsive to the action.
- **Auto:** partly (camera motion spectrum from tracking).
- **Grade:** Craft wisdom; handheld as a response to the actor is one practitioner's account [S325].
- **Source:** [S325, S268].

### FILM-CAM-4. Frame rate and shutter set the motion on purpose
- **What:** Motion blur follows the shutter angle: 180° (an exposure of 1/(2 × frame rate), so 1/48 s at 24 fps) is the usual default. Narrow shutters give crisp, staccato motion; wide ones smear. Slow motion is shot (or rendered) at a higher frame rate, not invented between frames where avoidable. Pick the frame rate for the delivery and the feel.
- **Why:** Mismatched blur (crisp backgrounds, smeared hands) or interpolated slow motion with warping edges look broken.
- **Check:** Step through fast action frame by frame. Is the blur consistent with one shutter? Any ghosting or warped edges from frame interpolation?
- **Fix:** Re-render with a set shutter; replace interpolated slow motion; conform frame rates before editing.
- **Auto:** partly (frame-difference spikes and duplicated frames show judder and pulldown).
- **Grade:** Standard (the shutter arithmetic); 180° as default: craft wisdom [S268]. Viewers preferred higher frame rates in stereoscopic tests, so 24 fps is a convention, not a law [S311, S312].
- **Source:** [S268, S311, S312].

## Light

### FILM-LIT-1. One key direction per setup, held across the cuts of a scene (MUST-BE-RIGHT within one continuous scene)
- **What:** Within one moment in one place, the main light comes from one consistent side relative to the world source (window, lamp, sun), in every angle of coverage. The key may be cheated a little per angle, but not flipped.
- **Why:** If the light jumps sides between shot and reverse shot, the cut reads as a different time or place. This is TD-LIT-1 extended across time.
- **Check:** For each shot in the scene, note which side of the face is lit and where cast shadows fall. Do they agree with the master and the source?
- **Fix:** Relight, regrade (shapes of shadow can't be graded away), or regenerate. A change of light is fine when the story motivates it (a door opens, a cloud passes) and the change is shown.
- **Auto:** partly (bright side of detected faces per frame).
- **Grade:** Standard within the scene (light physics; see TD-LIT-1). Cheating per angle: craft wisdom [S268, S324].
- **Source:** [S268, S324, S274]; TD-LIT-1, CV-7.

### FILM-LIT-2. Light is motivated by the world
- **What:** Every source can be explained by something seen or implied: a window, a practical lamp, a screen, fire, sky. Rim and back light have a believable source too.
- **Why:** Unmotivated glow (a rim on every edge, light from nowhere) is the generic look (ILL-11) and flattens mood.
- **Check:** Name the source of key, fill and back light in each setup. Any "from nowhere"?
- **Fix:** Add or reveal the source, or remove the light.
- **Auto:** no.
- **Grade:** Craft wisdom [S268, S274, S322, S323].
- **Source:** [S268, S274, S322, S323].

### FILM-LIT-3. The key-to-fill ratio is set for the mood and held within the scene
- **What:** Ratio is the difference between the lit and shadow side, counted in stops (each stop doubles the light): about 1 stop (2:1) is soft and even, 2 stops (4:1) is shaped, 3 stops or more (8:1+) is low key. Negative fill deepens the shadow side.
- **Why:** The ratio sets high key or low key; drifting ratios between shots of one scene make the cut bump.
- **Check:** Measure lit-cheek against shadow-cheek luminance on faces in sampled frames (or read them on a waveform or false-colour view). Same ratio across the scene?
- **Fix:** Relight; grade to match where the shapes allow it.
- **Auto:** yes (luminance sampling on face regions).
- **Grade:** Standard (the arithmetic of stops); which ratio suits which mood: craft wisdom [S268, S273, S329].
- **Source:** [S268, S273, S329].

### FILM-LIT-4. The subject separates from the background
- **What:** Value, edge light, colour or depth separates the subject from what is behind it, at the beat's focus.
- **Why:** In motion, viewers have little time; weak separation loses the subject behind clutter.
- **Check:** Greyscale and blur a frame from each beat (CORE-2, CV-3). Does the subject read as its own shape?
- **Fix:** Darken or lighten the background, add a motivated edge light, or move the subject.
- **Auto:** partly (`tools/look.py` on sampled frames).
- **Grade:** Craft wisdom, consistent with figure-ground evidence [S37].
- **Source:** [S268, S37]; CV-1, CV-3.

### FILM-LIT-5. Practicals read as sources and protect the latitude
- **What:** Lamps, screens and windows in frame are exposed so they read as light sources (some detail or a gentle bloom), not as dead grey or a clipped hole. Skin never clips by accident; shadows are crushed only when chosen.
- **Why:** The image's latitude (the range from black to white that holds detail) is finite; clipping on faces and dead practicals look like mistakes.
- **Check:** Waveform or histogram per shot; zoom on highlights on faces and practicals; check the delivered SDR and HDR versions.
- **Fix:** Dim the practical, lift or lower exposure, or protect highlights in the grade. See 3D-7 for view transforms in renders.
- **Auto:** yes (clipped pixels in face and practical regions).
- **Grade:** Standard (sensor and display range); exposure for practicals: craft wisdom [S323, S268].
- **Source:** [S323, S268].

## Colour and grading

### FILM-COL-1. One look per scene, and shots matched to it
- **What:** Build the look first (overall contrast, colour of light and shadow, saturation), then balance every shot of the scene to it: black and white points first, then skin, then neutrals.
- **Why:** Shots that differ in colour or contrast make the cut visible and break the scene into pieces.
- **Check:** Contact sheet of all shots in the scene side by side, plus the waveform and vectorscope. Do skin, blacks and neutrals match? Match to the widest representative shot first.
- **Fix:** Regrade with few shot-level fixes; regenerate the outlier.
- **Auto:** partly (mean and spread of L*, a*, b* per shot, and on face regions).
- **Grade:** Procedure; the look-first order is one practitioner's method, widely used [S309]; matching order: craft wisdom [S307].
- **Source:** [S307, S309].

### FILM-COL-2. Skin reads as healthy and as itself
- **What:** Under neutral light, skin sits near one narrow hue band (the "skin line" on a vectorscope), whatever the person's complexion; lightness and saturation differ by person. Keep each person's own tone; push it only when the light or story asks.
- **Why:** Viewers remember skin, sky and foliage as more saturated than they are and judge them against memory, so off skin is caught before anything else.
- **Check:** Vectorscope on a face region per shot; compare faces across shots and with each other.
- **Fix:** Isolate and correct skin; don't drag every complexion to one hue.
- **Auto:** yes (hue angle of face regions).
- **Grade:** Partly supported (memory colours [S308]); the skin line as a guide, not a rule: craft wisdom [S307].
- **Source:** [S308, S307].

### FILM-COL-3. One colour pipeline from source to delivery
- **What:** Know the colour space each source is in (camera log, generated sRGB, renders), transform it once into the working space, apply the look there, and output for each delivery (SDR, HDR). A LUT made for one input is used only on that input.
- **Why:** A LUT on the wrong input gives crunchy, clipped or muddy pictures that no later tweak fixes cleanly.
- **Check:** Write down the chain: input space, transform, look, output. Is any step guessed?
- **Fix:** Rebuild the chain with a colour-managed pipeline (for example ACES) and exchange grades as CDLs or the project's LUTs.
- **Auto:** no.
- **Grade:** Standard (colour-management specs) [S331]; pipeline practice: craft wisdom [S324].
- **Source:** [S331, S324].

### FILM-COL-4. Colour guides the eye and the arc
- **What:** The strongest chroma sits at the focus of the beat, the palette plans change over time (`story.md`, FILM-STORY-3), and the meaning survives colour-vision deficiency.
- **Why:** The CV rules apply to every frame, and a whole film needs a plan, not one grade dragged everywhere.
- **Check:** CV-6 and CV-9 on sampled frames; a one-frame-per-scene strip for the arc.
- **Fix:** See CV-6, CV-9 and FILM-STORY-3.
- **Auto:** partly.
- **Grade:** See CV-6, CV-9.
- **Source:** CV-6, CV-9; [S306].

## Editing and pacing

### FILM-EDIT-1. Cut for emotion first (the rule of six)
- **What:** Judge a cut in this order: emotion, story, rhythm, eye-trace, the flat picture plane, then 3D space continuity. When a cut can't satisfy all, give up from the bottom of the list.
- **Why:** A cut that keeps the feeling and the story right is forgiven a small spatial slip; the reverse isn't true.
- **Check:** For each doubtful cut, which of the six does it serve and which does it break?
- **Fix:** Prefer the take or cut point that keeps the higher priorities.
- **Auto:** no.
- **Grade:** Craft wisdom (one editor's framework, widely taught; the percentages he gives are deliberately playful, not measured) [S269].
- **Source:** [S269].

### FILM-EDIT-2. Cut where the eye already is, or lead it
- **What:** After a cut, the next thing to look at appears near where the viewer was looking, or a strong cue (motion, a face, contrast, sound) leads the eye to it fast.
- **Why:** Viewers' gaze clusters on the same few places at the same time, led by motion and faces; a cut that puts the subject far away makes them search and miss the start of the shot.
- **Check:** Scrub across each cut: where is the focus in the last frame of A and the first frame of B? If it jumps across the frame with no cue, flag it.
- **Fix:** Re-frame, flop (FILM-CON-4 permitting), move the cut point, or add a cue.
- **Auto:** partly (saliency or face position at both sides of each cut).
- **Grade:** Partly supported [S279, S280, S281, S277].
- **Source:** [S279, S280, S281, S277, S269].

### FILM-EDIT-3. Shot length follows information and intensity
- **What:** Hold each shot until its information is read, no longer than its interest lasts. Wide, cluttered or emotional shots need more time; close, simple ones less. Shots usually shorten toward a climax and lengthen as it resolves.
- **Why:** In popular films, shot length tracks how hard a shot is to read, and shots get shorter around climaxes; uniform lengths feel mechanical.
- **Check:** List shots with durations per scene. Does pace rise toward the peaks? Is any shot cut before its information can be read (try a fresh viewer)? Are lengths all the same?
- **Fix:** Extend shots that are too short to read; trim lingering ones; vary lengths in a pattern that follows intensity.
- **Auto:** yes for durations (shot-boundary detection); judgement for readability.
- **Grade:** Partly supported. The corpus studies describe what popular films do, not what is best [S283, S285, S286, S287]; average shot length has fallen over decades [S284, S288].
- **Source:** [S283, S284, S285, S286, S287, S288].

### FILM-EDIT-4. Let sound lead or trail the picture (J and L cuts)
- **What:** In dialogue and scene changes, let the next shot's sound start early (J cut) or the last shot's sound run on (L cut), instead of switching picture and sound together every time.
- **Why:** Overlapping sound smooths cuts, keeps listeners on the listener, and pulls the viewer into the next scene.
- **Check:** Are most dialogue cuts straight cuts on both tracks at once? Any scene change that jolts without reason?
- **Fix:** Offset sound edits; use a sound bridge into a new scene (FILM-STORY-8).
- **Auto:** no.
- **Grade:** Craft wisdom [S270, S330].
- **Source:** [S270, S330].

### FILM-EDIT-5. Juxtaposition shifts meaning, but only so far (the Kuleshov effect)
- **What:** A neutral face can read slightly differently depending on what is cut next to it, and music can do the same. Use it to steer a reaction shot; don't rely on it to rescue a performance or picture that says something else.
- **Why:** Modern replications find a real but modest and uneven effect (some emotions more than others, for experienced viewers more than first-time viewers). The legend of a dramatic, universal effect goes beyond the evidence; the original footage is lost.
- **Check:** Does the meaning of a reaction shot depend wholly on context? Does it still hold if the context shot were removed?
- **Fix:** Get a performance that supports the beat; use context to sharpen it, not invent it.
- **Auto:** no.
- **Grade:** Partly supported [S293, S294, S295, S296, S297].
- **Source:** [S293, S294, S295, S296, S297, S330].

### FILM-EDIT-6. Few kinds of transition, each with a meaning
- **What:** The cut is neutral. A dissolve suggests passing time or a link; a fade suggests an ending; wipes, whips and match cuts are stylised. Use one small set consistently.
- **Why:** A different transition at every change reads as decoration and blurs what each one means.
- **Check:** List the transitions used. Does each kind mean one thing in this piece?
- **Fix:** Replace decorative transitions with cuts.
- **Auto:** partly (transition detection).
- **Grade:** Craft wisdom [S270, S267].
- **Source:** [S270, S267].

## Composition in motion

### FILM-COMP-1. Compose the key frames, not every frame
- **What:** A moving shot is composed at its moments: where it starts, where it rests, the frame on the beat, and where it ends. Run the composition rules (COMP-1 to COMP-18, ILL-2) on those frames.
- **Why:** Frames in passing don't need to compose; the ones the viewer rests on do.
- **Check:** Pull the rest frames and the beat frame of each shot; run the five look tests on them.
- **Fix:** Re-block, re-frame, or re-time the move so it rests on a composed frame.
- **Auto:** partly (`tools/look.py` on extracted frames).
- **Grade:** Craft wisdom [S275, S271].
- **Source:** [S275, S271].

### FILM-COMP-2. Motion beats everything for attention, so control stray motion
- **What:** In moving images, motion and flicker predict where people look better than anything else, then faces. A moving or flickering background element steals the eye from the subject.
- **Why:** Attention clusters tightly on motion; stray motion drags it there.
- **Check:** Watch the shot with eyes soft: what moves besides the subject (extras, leaves, screens, blinking lights, generated texture "boiling")?
- **Fix:** Still it, blur it, darken it, or let the subject move more.
- **Auto:** partly (motion energy maps outside the subject).
- **Grade:** Well supported for gaze [S279, S280]; the fix is craft.
- **Source:** [S279, S280].

### FILM-COMP-3. Stage in depth and move people, not only the camera
- **What:** Use foreground, middle ground and background; let actors move to new positions to change the composition and power within a shot (blocking), instead of cutting each time.
- **Why:** Depth staging gives the viewer a readable space and lets one shot do the work of several.
- **Check:** Does the scene use more than one plane? Do the actors' moves change the frame meaningfully?
- **Fix:** Re-block; separate planes by value and edge (ILL-14).
- **Auto:** no.
- **Grade:** Craft wisdom [S270, S271, S275].
- **Source:** [S270, S271, S275]; ILL-14.

### FILM-COMP-4. Balance in motion is a flag, never a push to centre
- **What:** Balance is judged across time. An off-centre single is answered by its reverse shot; empty space may wait for an entrance; a frame may be lopsided on purpose to unsettle. Run Sitting right (COMP-19 to COMP-25) on key frames, flag only what looks accidental, and ask "intended?".
- **Why:** Centring every subject kills looking room, eyeline geometry and tension.
- **Check:** Flags from key frames, each answered "intended: keep (why)" or "fix".
- **Fix:** A counterweight, a firmer asymmetry, or the matching reverse; never centre or symmetrise by default.
- **Auto:** partly (`tools/balance.py` on key frames: FLAG only).
- **Grade:** Craft wisdom; balance and liking are only loosely linked [S235, S237].
- **Source:** COMP-19 to COMP-25; [S235, S237, S275].

## Sound (short; story uses are in `story.md`)

### FILM-SND-1. Dialogue is intelligible, and loudness meets the delivery spec
- **What:** Speech sits clearly above music and effects, on small speakers as well as good ones. The mix is normalised to the delivery's loudness target (for broadcast in Europe, EBU R 128: −23 LUFS integrated, true peak no higher than −1 dBTP; streaming platforms publish their own).
- **Why:** Lost dialogue is the commonest audience complaint about sound; wrong loudness gets rejected or turned down by the platform.
- **Check:** Listen on a phone speaker and on headphones; measure integrated loudness and true peak.
- **Fix:** Duck music under speech; re-mix; normalise.
- **Auto:** yes for loudness; no for intelligibility.
- **Grade:** Standard for loudness [S319]; intelligibility: craft wisdom.
- **Source:** [S319].

### FILM-SND-2. Sound and picture are in sync, and visible events have sound
- **What:** Lips, footsteps and impacts land on the frame. Visible actions that would make a sound have one (or their silence is a choice).
- **Why:** Viewers fuse a sound with whatever moves at the same moment, so a well-timed sound sells an image, and a late one breaks it.
- **Check:** Step through impacts and plosives frame by frame; list silent actions in generated clips.
- **Fix:** Slip sync; add effects; or make silence a clear choice (FILM-STORY-8).
- **Auto:** partly (audio-onset against motion-onset).
- **Grade:** Craft wisdom with a perceptual account (synchresis) [S302].
- **Source:** [S302].

## On-screen text

### FILM-TXT-1. Titles and lower thirds read at size, on the worst frame behind them
- **What:** On-screen text stays inside graphics-safe, meets the size floor at the delivered size (TYPE-3), and keeps contrast against the brightest or busiest frame it passes over (LAY-15, UI-6), not the frame it was designed on. It doesn't cover mouths, faces or the action.
- **Why:** Footage changes under fixed text; a title legible on frame one can vanish on frame forty.
- **Check:** Sample every frame the text is on; measure contrast against the worst background pixels; overlay safe areas.
- **Fix:** Add a soft shadow, a box or a darker grade under the text, or move it.
- **Auto:** yes (contrast per frame within the text box, `tools/contrast.py` on samples).
- **Grade:** Standard (WCAG contrast, safe areas) [S3, S318]; placement: craft wisdom [S317].
- **Source:** [S3, S318, S317]; TYPE-3, LAY-15.

### FILM-TXT-2. Subtitles and titles stay up long enough to read
- **What:** Follow the delivery's subtitle spec. Typical published values: at most 2 lines in landscape; about 37 to 42 characters a line; reading speed up to about 160 to 180 words a minute (BBC) or 17 to 20 characters a second (Netflix, children and adults); each subtitle up between about 5/6 s and 7 s; line breaks at natural phrase boundaries; avoid hanging a subtitle across a shot change. Titles need at least time to read twice.
- **Why:** Text that leaves before it is read is worse than none; text across cuts flashes.
- **Check:** Characters per line and per second for every event; minimum and maximum durations; events crossing shot changes.
- **Fix:** Condense, split or re-time.
- **Auto:** yes (parse the subtitle file).
- **Grade:** Standard within each spec [S316, S317].
- **Source:** [S316, S317].

### FILM-TXT-3. One title system
- **What:** One or two type families, fixed positions, sizes and in/out timing for each kind of text (titles, lower thirds, captions).
- **Why:** Consistent text recedes so the picture leads.
- **Check:** Compare every instance of each kind.
- **Fix:** Rebuild from one template. See TYPE-1, TYPE-2, TYPE-10.
- **Auto:** partly.
- **Grade:** Craft wisdom; see CORE-9.
- **Source:** CORE-9, TYPE-1, TYPE-2.

## Accessibility

### FILM-ACC-1. No flashing above the threshold (MUST-BE-RIGHT)
- **What:** No more than three general flashes or three red flashes in any one-second period, unless the flashing area is small (under about a quarter of a 10° field of view; 341 × 256 px at 1024 × 768). A general flash is a pair of opposing changes in relative luminance of 10% or more where the darker state is below 0.80; red flashes have their own definition. Broadcast has its own (stricter) guidance, and stripes and regular patterns can be a hazard too.
- **Why:** Flashing can trigger seizures in people with photosensitive epilepsy.
- **Check:** Look for strobes, lightning, muzzle flashes, rapid cuts between light and dark, and flickering generated textures. Analyse at full-screen size; loop short clips. For broadcast, run a photosensitive-epilepsy analyser.
- **Fix:** Slow the flashes, shrink the flashing area, or cut its contrast.
- **Auto:** yes (frame-luminance analysis; a pass is a strong signal, not a guarantee).
- **Grade:** Standard [S314, S315].
- **Source:** [S314, S315].

### FILM-ACC-2. Captions for speech and sound, description where only the picture tells
- **What:** Prerecorded video with speech has captions that include plot-relevant sounds; where the picture carries information no one says aloud, provide audio description or a text alternative.
- **Why:** Deaf, hard-of-hearing and blind viewers otherwise miss the story.
- **Check:** Are captions present, accurate and synced? Is any key story point purely visual?
- **Fix:** Add captions (FILM-TXT-2) and description.
- **Auto:** partly.
- **Grade:** Standard [S314].
- **Source:** [S314].

---

## Look vocabulary (by technique, not by title)

When a brief asks for "a film look", name the technique, not a title: high-key studio light; low-key chiaroscuro; available-light naturalism; day-for-night; bleach-bypass (silver retained: low saturation, high contrast); saturated dye-transfer primaries; cross-processed colour shifts; push-processed grain; black-and-white with filters; halation and bloom around highlights; diffusion filtering; anamorphic flares and oval bokeh. The `lookbook` module has no film entries yet; adding them would need example plates, which this version does not include.

## Myths and weak claims

- **The rule of thirds is the law of framing.** It is a rough guide for some shots. Eyelines, looking room and the matching reverse shot decide placement (FILM-SHOT-6, FILM-COMP-4). See `core/evidence.md`.
- **The golden ratio or spiral is how great shots are framed.** Overlays fitted after the fact prove nothing; preference studies don't support it [S220, S38].
- **24 fps is sacred.** It became the standard in the sound era as a compromise of cost and sound quality [S312]; viewers preferred higher rates in stereoscopic tests [S311]. It is a strong convention with a familiar feel, not a property of "cinema".
- **Shallow depth of field makes it cinematic.** It is one tool. Deep staging is as old and as cinematic, and shallow focus on every shot flattens the beats (FILM-SHOT-4).
- **Teal and orange always looks good.** It separates warm skin from cool shadows, but applied by default it is a cliché and fights many stories [S310]. The palette comes from the story (FILM-STORY-3).
- **"Film look" means grain, letterbox bars and a LUT.** The look comes from light, lens, staging, movement and grade working together; bars on a 16:9 frame just crop it.
- **The Kuleshov effect proves editing can make any face mean anything.** The effect is real but modest and uneven, and the original experiment can't be checked [S293 to S296].
- **Wide lenses distort and long lenses compress.** Camera distance does; the lens only crops (FILM-SHOT-3) [S313].
- **Colours carry fixed meanings (red is danger, blue is sad).** Shared associations exist across cultures but vary with language and place, and context and the film's own pairings decide meaning [S304, S46].
- **Never cross the line.** It is a convention for readable space, broken well when the beat wants it (FILM-CON-1).
- **Faster cutting is more exciting.** Corpus studies show pace has risen, not that faster is better; shots cut before they are read lose the viewer (FILM-EDIT-3) [S284, S286].
- **Murch's percentages are measured.** They are a deliberately playful ranking (FILM-EDIT-1) [S269].
- **Handheld means realism; low angle means power.** Each can, depending on context and use [S290, S291, S325].

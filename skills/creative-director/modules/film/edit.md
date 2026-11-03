# Film: colour, editing, composition in motion, sound and on-screen text

On-demand part of `modules/film/`; load it with the module README and `story.md` for grading, cutting, titles, subtitles or sound, and for any full review. Format, grades and sources as in the module README.

## Colour and grading

### FILM-COL-1. One look per scene, and shots matched to it
- **What:** Build the look first (overall contrast, colour of light and shadow, saturation), then balance every shot of the scene to it: black and white points first, then skin, then neutrals.
- **Why:** Shots that differ in colour or contrast make the cut visible and break the scene into pieces.
- **Check:** Contact sheet of all shots in the scene side by side, plus the waveform and vectorscope. Do skin, blacks and neutrals match? Match to the widest representative shot first.
- **Fix:** Regrade with few shot-level fixes; regenerate the outlier.
- **Auto:** partly (mean and spread of L*, a*, b* per shot, and on face regions).
- **Grade:** Procedure; the look-first order is one practitioner's method, widely used [SRC-309]; matching order: craft wisdom [SRC-307].
- **Source:** [SRC-307, SRC-309].

### FILM-COL-2. Skin reads as healthy and as itself
- **What:** Under neutral light, skin sits near one narrow hue band (the "skin line" on a vectorscope), whatever the person's complexion; lightness and saturation differ by person. Keep each person's own tone; push it only when the light or story asks.
- **Why:** Viewers remember skin, sky and foliage as more saturated than they are and judge them against memory, so off skin is caught before anything else.
- **Check:** Vectorscope on a face region per shot; compare faces across shots and with each other.
- **Fix:** Isolate and correct skin; don't drag every complexion to one hue.
- **Auto:** yes (hue angle of face regions).
- **Grade:** Partly supported (memory colours [SRC-308]); the skin line as a guide, not a rule: craft wisdom [SRC-307].
- **Source:** [SRC-308, SRC-307].

### FILM-COL-3. One colour pipeline from source to delivery
- **What:** Know the colour space each source is in (camera log, generated sRGB, renders), transform it once into the working space, apply the look there, and output for each delivery (SDR, HDR). A LUT made for one input is used only on that input.
- **Why:** A LUT on the wrong input gives crunchy, clipped or muddy pictures that no later tweak fixes cleanly.
- **Check:** Write down the chain: input space, transform, look, output. Is any step guessed?
- **Fix:** Rebuild the chain with a colour-managed pipeline (for example ACES) and exchange grades as CDLs or the project's LUTs.
- **Auto:** no.
- **Grade:** Standard (colour-management specs) [SRC-331]; pipeline practice: craft wisdom [SRC-324].
- **Source:** [SRC-331, SRC-324].

### FILM-COL-4. Colour guides the eye and the arc
- **What:** The strongest chroma sits at the focus of the beat, the palette plans change over time (`story.md`, FILM-STORY-3), and the meaning survives colour-vision deficiency.
- **Why:** The CV rules apply to every frame, and a whole film needs a plan, not one grade dragged everywhere.
- **Check:** CV-6 and CV-9 on sampled frames; a one-frame-per-scene strip for the arc.
- **Fix:** See CV-6, CV-9 and FILM-STORY-3.
- **Auto:** partly.
- **Grade:** See CV-6, CV-9.
- **Source:** CV-6, CV-9; [SRC-306].

## Editing and pacing

### FILM-EDIT-1. Cut for emotion first (the rule of six)
- **What:** Judge a cut in this order: emotion, story, rhythm, eye-trace, the flat picture plane, then 3D space continuity. When a cut can't satisfy all, give up from the bottom of the list.
- **Why:** A cut that keeps the feeling and the story right is forgiven a small spatial slip; the reverse isn't true.
- **Check:** For each doubtful cut, which of the six does it serve and which does it break?
- **Fix:** Prefer the take or cut point that keeps the higher priorities.
- **Auto:** no.
- **Grade:** Craft wisdom (one editor's framework, widely taught; the percentages he gives are deliberately playful, not measured) [SRC-269].
- **Source:** [SRC-269].

### FILM-EDIT-2. Cut where the eye already is, or lead it
- **What:** After a cut, the next thing to look at appears near where the viewer was looking, or a strong cue (motion, a face, contrast, sound) leads the eye to it fast.
- **Why:** Viewers' gaze clusters on the same few places at the same time, led by motion and faces; a cut that puts the subject far away makes them search and miss the start of the shot.
- **Check:** Scrub across each cut: where is the focus in the last frame of A and the first frame of B? If it jumps across the frame with no cue, flag it.
- **Fix:** Re-frame, flop (FILM-CON-4 permitting), move the cut point, or add a cue.
- **Auto:** partly (saliency or face position at both sides of each cut).
- **Grade:** Partly supported [SRC-279, SRC-280, SRC-281, SRC-277].
- **Source:** [SRC-279, SRC-280, SRC-281, SRC-277, SRC-269].

### FILM-EDIT-3. Shot length follows information and intensity
- **What:** Hold each shot until its information is read, no longer than its interest lasts. Wide, cluttered or emotional shots need more time; close, simple ones less. Shots usually shorten toward a climax and lengthen as it resolves.
- **Why:** In popular films, shot length tracks how hard a shot is to read, and shots get shorter around climaxes; uniform lengths feel mechanical.
- **Check:** List shots with durations per scene. Does pace rise toward the peaks? Is any shot cut before its information can be read (try a fresh viewer)? Are lengths all the same?
- **Fix:** Extend shots that are too short to read; trim lingering ones; vary lengths in a pattern that follows intensity.
- **Auto:** yes for durations (shot-boundary detection); judgement for readability.
- **Grade:** Partly supported. The corpus studies describe what popular films do, not what is best [SRC-283, SRC-285, SRC-286, SRC-287]; average shot length has fallen over decades [SRC-284, SRC-288].
- **Source:** [SRC-283, SRC-284, SRC-285, SRC-286, SRC-287, SRC-288].

### FILM-EDIT-4. Let sound lead or trail the picture (J and L cuts)
- **What:** In dialogue and scene changes, let the next shot's sound start early (J cut) or the last shot's sound run on (L cut), instead of switching picture and sound together every time.
- **Why:** Overlapping sound smooths cuts, keeps listeners on the listener, and pulls the viewer into the next scene.
- **Check:** Are most dialogue cuts straight cuts on both tracks at once? Any scene change that jolts without reason?
- **Fix:** Offset sound edits; use a sound bridge into a new scene (FILM-STORY-8).
- **Auto:** no.
- **Grade:** Craft wisdom [SRC-270, SRC-330].
- **Source:** [SRC-270, SRC-330].

### FILM-EDIT-5. Juxtaposition shifts meaning, but only so far (the Kuleshov effect)
- **What:** A neutral face can read slightly differently depending on what is cut next to it, and music can do the same. Use it to steer a reaction shot; don't rely on it to rescue a performance or picture that says something else.
- **Why:** Modern replications find a real but modest and uneven effect (some emotions more than others, for experienced viewers more than first-time viewers). The legend of a dramatic, universal effect goes beyond the evidence; the original footage is lost.
- **Check:** Does the meaning of a reaction shot depend wholly on context? Does it still hold if the context shot were removed?
- **Fix:** Get a performance that supports the beat; use context to sharpen it, not invent it.
- **Auto:** no.
- **Grade:** Partly supported [SRC-293, SRC-294, SRC-295, SRC-296, SRC-297].
- **Source:** [SRC-293, SRC-294, SRC-295, SRC-296, SRC-297, SRC-330].

### FILM-EDIT-6. Few kinds of transition, each with a meaning
- **What:** The cut is neutral. A dissolve suggests passing time or a link; a fade suggests an ending; wipes, whips and match cuts are stylised. Use one small set consistently.
- **Why:** A different transition at every change reads as decoration and blurs what each one means.
- **Check:** List the transitions used. Does each kind mean one thing in this piece?
- **Fix:** Replace decorative transitions with cuts.
- **Auto:** partly (transition detection).
- **Grade:** Craft wisdom [SRC-270, SRC-267].
- **Source:** [SRC-270, SRC-267].

## Composition in motion

### FILM-COMP-1. Compose the key frames, not every frame
- **What:** A moving shot is composed at its moments: where it starts, where it rests, the frame on the beat, and where it ends. Run the composition rules (COMP-1 to COMP-18, ILL-2) on those frames.
- **Why:** Frames in passing don't need to compose; the ones the viewer rests on do.
- **Check:** Pull the rest frames and the beat frame of each shot; run the five look tests on them.
- **Fix:** Re-block, re-frame, or re-time the move so it rests on a composed frame.
- **Auto:** partly (`tools/look.py` on extracted frames).
- **Grade:** Craft wisdom [SRC-275, SRC-271].
- **Source:** [SRC-275, SRC-271].

### FILM-COMP-2. Motion beats everything for attention, so control stray motion
- **What:** In moving images, motion and flicker predict where people look better than anything else, then faces. A moving or flickering background element steals the eye from the subject.
- **Why:** Attention clusters tightly on motion; stray motion drags it there.
- **Check:** Watch the shot with eyes soft: what moves besides the subject (extras, leaves, screens, blinking lights, generated texture "boiling")?
- **Fix:** Still it, blur it, darken it, or let the subject move more.
- **Auto:** partly (motion energy maps outside the subject).
- **Grade:** Well supported for gaze [SRC-279, SRC-280]; the fix is craft.
- **Source:** [SRC-279, SRC-280].

### FILM-COMP-3. Stage in depth and move people, not only the camera
- **What:** Use foreground, middle ground and background; let actors move to new positions to change the composition and power within a shot (blocking), instead of cutting each time.
- **Why:** Depth staging gives the viewer a readable space and lets one shot do the work of several.
- **Check:** Does the scene use more than one plane? Do the actors' moves change the frame meaningfully?
- **Fix:** Re-block; separate planes by value and edge (ILL-14).
- **Auto:** no.
- **Grade:** Craft wisdom [SRC-270, SRC-271, SRC-275].
- **Source:** [SRC-270, SRC-271, SRC-275]; ILL-14.

### FILM-COMP-4. Balance in motion is a flag, never a push to centre
- **What:** Balance is judged across time. An off-centre single is answered by its reverse shot; empty space may wait for an entrance; a frame may be lopsided on purpose to unsettle. Run Sitting right (COMP-19 to COMP-25) on key frames, flag only what looks accidental, and ask "intended?".
- **Why:** Centring every subject kills looking room, eyeline geometry and tension.
- **Check:** Flags from key frames, each answered "intended: keep (why)" or "fix".
- **Fix:** A counterweight, a firmer asymmetry, or the matching reverse; never centre or symmetrise by default.
- **Auto:** partly (`tools/balance.py` on key frames: FLAG only).
- **Grade:** Craft wisdom; balance and liking are only loosely linked [SRC-235, SRC-237].
- **Source:** COMP-19 to COMP-25; [SRC-235, SRC-237, SRC-275].

## Sound (short; story uses are in `story.md`)

### FILM-SND-1. Dialogue is intelligible, and loudness meets the delivery spec
- **What:** Speech sits clearly above music and effects, on small speakers as well as good ones. The mix is normalised to the delivery's loudness target (for broadcast in Europe, EBU R 128: −23 LUFS integrated, true peak no higher than −1 dBTP; streaming platforms publish their own).
- **Why:** Lost dialogue is the commonest audience complaint about sound; wrong loudness gets rejected or turned down by the platform.
- **Check:** Listen on a phone speaker and on headphones; measure integrated loudness and true peak.
- **Fix:** Duck music under speech; re-mix; normalise.
- **Auto:** yes for loudness; no for intelligibility.
- **Grade:** Standard for loudness [SRC-319]; intelligibility: craft wisdom.
- **Source:** [SRC-319].

### FILM-SND-2. Sound and picture are in sync, and visible events have sound
- **What:** Lips, footsteps and impacts land on the frame. Visible actions that would make a sound have one (or their silence is a choice).
- **Why:** Viewers fuse a sound with whatever moves at the same moment, so a well-timed sound sells an image, and a late one breaks it.
- **Check:** Step through impacts and plosives frame by frame; list silent actions in generated clips.
- **Fix:** Slip sync; add effects; or make silence a clear choice (FILM-STORY-8).
- **Auto:** partly (audio-onset against motion-onset).
- **Grade:** Craft wisdom with a perceptual account (synchresis) [SRC-302].
- **Source:** [SRC-302].

## On-screen text

### FILM-TXT-1. Titles and lower thirds read at size, on the worst frame behind them
- **What:** On-screen text stays inside graphics-safe, meets the size floor at the delivered size (TYPE-3), and keeps contrast against the brightest or busiest frame it passes over (LAY-15, UI-6), not the frame it was designed on. It doesn't cover mouths, faces or the action.
- **Why:** Footage changes under fixed text; a title legible on frame one can vanish on frame forty.
- **Check:** Sample every frame the text is on; measure contrast against the worst background pixels; overlay safe areas.
- **Fix:** Add a soft shadow, a box or a darker grade under the text, or move it.
- **Auto:** yes (contrast per frame within the text box, `tools/contrast.py` on samples).
- **Grade:** Standard (WCAG contrast, safe areas) [SRC-3, SRC-318]; placement: craft wisdom [SRC-317].
- **Source:** [SRC-3, SRC-318, SRC-317]; TYPE-3, LAY-15.

### FILM-TXT-2. Subtitles and titles stay up long enough to read
- **What:** Follow the delivery's subtitle spec. Typical published values: at most 2 lines in landscape; about 37 to 42 characters a line; reading speed up to about 160 to 180 words a minute (BBC) or 17 to 20 characters a second (Netflix, children and adults); each subtitle up between about 5/6 s and 7 s; line breaks at natural phrase boundaries; avoid hanging a subtitle across a shot change. Titles need at least time to read twice.
- **Why:** Text that leaves before it is read is worse than none; text across cuts flashes.
- **Check:** Characters per line and per second for every event; minimum and maximum durations; events crossing shot changes.
- **Fix:** Condense, split or re-time.
- **Auto:** yes (parse the subtitle file).
- **Grade:** Standard within each spec [SRC-316, SRC-317].
- **Source:** [SRC-316, SRC-317].

### FILM-TXT-3. One title system
- **What:** One or two type families, fixed positions, sizes and in/out timing for each kind of text (titles, lower thirds, captions).
- **Why:** Consistent text recedes so the picture leads.
- **Check:** Compare every instance of each kind.
- **Fix:** Rebuild from one template. See TYPE-1, TYPE-2, TYPE-10.
- **Auto:** partly.
- **Grade:** Craft wisdom; see CORE-9.
- **Source:** CORE-9, TYPE-1, TYPE-2.

Look vocabulary (film looks named by technique) and film myths: [`notes.md`](notes.md), optional.

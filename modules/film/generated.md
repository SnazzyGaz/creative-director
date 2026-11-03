# Film: generated video

For clips made or altered by a video model (text-to-video, image-to-video, extensions, inpainting, frame interpolation). The rules in `README.md`, `edit.md` and `story.md` still apply; these are the faults models add. Judge in motion first (FILM-REV-1), then sample frames. Benchmarks confirm these failure families: subject and background consistency, temporal flicker and motion smoothness are separate measured dimensions [SRC-320], and on a physics benchmark the best models scored low, with visual realism not predicting physical understanding [SRC-321].

Format: **What / Why / Check / Fix / Grade / Source**. MUST-BE-RIGHT rules block delivery.

---

### FILM-GEN-1. Sample frames on a schedule, and look at them (the QC sheet)
- **What:** Extract frames at a fixed interval (every 0.5 s for clips under 10 s, every 1 s for longer ones), plus the first and last frame of every shot and the frames either side of every cut, into contact sheets. Review the sheet and crops at 2× of faces, hands, text and contacts.
- **Why:** Generated faults come and go within a second; watching at speed misses many, and a single still misses the rest.
- **Check:** Example with ffmpeg (no special tool): `ffmpeg -i clip.mp4 -vf "fps=2,scale=480:-1,tile=6x4" sheet_%02d.png` for the sheet; `ffmpeg -i clip.mp4 -vf "select='gt(scene,0.3)'" -fps_mode vfr cut_%03d.png` for the first frame after each cut (tested with ffmpeg 7; older builds use `-vsync vfr`). Write one line per sampled frame with anything found.
- **Fix:** Regenerate, trim or repair the shots that fail; re-sample after every fix.
- **Grade:** Procedure.
- **Source:** [SRC-320]; CHAR-9 for the written-line method.

### FILM-GEN-2. Identity holds across frames and shots (MUST-BE-RIGHT for any recurring character)
- **What:** Face shape, features, age, hair, skin, build, costume and distinguishing marks stay the same through a shot and across shots.
- **Why:** Identity drift is the failure viewers notice fastest; a character who changes face is a different person.
- **Check:** Crop the face from the first, middle and last frame of each shot and from each shot of the character; lay the crops side by side; compare features one by one (eye shape, nose, jaw, hairline, marks).
- **Fix:** Regenerate with a reference image or identity conditioning; shorten the shot; cut before the drift.
- **Grade:** Procedure; drift as a measured failure [SRC-320].
- **Source:** [SRC-320].

### FILM-GEN-3. Anatomy holds in every sampled frame (MUST-BE-RIGHT where people or animals appear)
- **What:** Run the anatomy pass (CHAR-9) on sampled frames, weighted to frames mid-gesture: hands opening and closing, legs crossing, turning heads, people passing in front of each other.
- **Why:** Bodies that look right at rest often break in motion (fingers merging, limbs swapping, a third arm in a crowd).
- **Check:** One written line per region per sampled frame, as CHAR-9.
- **Fix:** Regenerate, trim the frames, or re-frame to hide the hands only if the beat allows.
- **Grade:** Procedure (CHAR-9).
- **Source:** CHAR-9, CHAR-10.

### FILM-GEN-4. Objects persist and keep their shape
- **What:** Objects don't morph, merge, multiply, vanish or appear between frames; things held stay held; things behind others reappear the same.
- **Why:** Morphing reads as a dream at best and a fault at worst.
- **Check:** Count and name objects on the focus in the first and last frame of each shot; scrub through occlusions.
- **Fix:** Regenerate shorter, simplify the scene, or composite a stable plate.
- **Grade:** Procedure; consistency failures measured [SRC-320].
- **Source:** [SRC-320].

### FILM-GEN-5. Physics is plausible
- **What:** Gravity, weight, momentum, contact and materials behave: feet plant and don't slide, things fall at a believable rate, liquids pour and splash, collisions push back, nothing passes through anything solid, scale stays constant.
- **Why:** Models produce photoreal frames with impossible motion; viewers feel wrong weight even when they can't say why.
- **Check:** Watch contacts and impacts frame by frame; for anything falling or thrown, check the arc and speed; watch feet against the ground.
- **Fix:** Regenerate with simpler action, cut away before the impossible part, or use practical or simulated elements.
- **Grade:** Partly supported (benchmark results) [SRC-321].
- **Source:** [SRC-321]; 3D-1, 3D-2 for related rules.

### FILM-GEN-6. No flicker, boiling or pumping
- **What:** Textures (skin, foliage, water, fabric, backgrounds) don't crawl or boil; exposure and colour don't pump from frame to frame; fine patterns don't shimmer.
- **Why:** Temporal flicker draws the eye (FILM-COMP-2) and can approach flash thresholds (FILM-ACC-1).
- **Check:** Scrub at 1 frame a time; difference consecutive frames (for example `ffmpeg -i clip.mp4 -vf "tblend=all_mode=difference" diff.mp4`) and look for bright noise outside real motion; plot mean luminance per frame.
- **Fix:** Regenerate, deflicker, or replace the background with a stable plate.
- **Grade:** Procedure; temporal flicker measured [SRC-320].
- **Source:** [SRC-320]; FILM-ACC-1.

### FILM-GEN-7. Light and look are consistent across the sequence
- **What:** Each generated shot invents its own sun and grade. Across a scene, the key side, the ratio, the colour of light and the look must agree (FILM-LIT-1, FILM-COL-1).
- **Why:** Shots generated separately rarely match; the cut then reads as a new place or time.
- **Check:** Contact sheet with one frame from every shot of the scene; check key side on faces and shadow direction, then colour.
- **Fix:** State light direction and time of day in every prompt, use the same reference frame, grade to match, or regenerate the outlier.
- **Grade:** Standard within a scene (see FILM-LIT-1).
- **Source:** FILM-LIT-1, TD-LIT-1, CV-7.

### FILM-GEN-8. No invented text or marks (MUST-BE-RIGHT)
- **What:** Signs, screens, labels, shirts and documents in generated video contain no gibberish, morphing letters or invented logos. Real marks follow BRAND-4 and BRAND-8.
- **Why:** Invented text is an instant tell and can mislead; it often also changes from frame to frame.
- **Check:** List every frame region with lettering across the samples; read each.
- **Fix:** Generate without text and composite real text in post, blur or remove, or regenerate.
- **Grade:** Procedure; rule as BRAND-8.
- **Source:** BRAND-4, BRAND-8; [SRC-108].

### FILM-GEN-9. Camera and geometry behave
- **What:** The camera moves with a believable path (FILM-CAM-2); parallax is consistent (near things move faster than far ones); horizons and verticals don't bend or drift (TD-PER-1, TD-PER-3, per frame); rooms keep their layout when the camera returns.
- **Why:** Warped parallax and shifting rooms make space unreadable and feel uncanny.
- **Check:** Track a few points through the move; check horizons on sampled frames; compare the room in the first and last frame of a move that returns.
- **Fix:** Regenerate with a simpler move or lock off; stabilise only if it doesn't warp.
- **Grade:** Standard (projective geometry), per frame.
- **Source:** TD-PER-1, TD-PER-3.

### FILM-GEN-10. Avoid the generic generated-video look
- **What:** The defaults to question: a slow push-in on every shot, golden-hour light everywhere, lens flares and haze, shallow focus on everything, slow motion by default, every subject centred, music bed under all of it.
- **Why:** These are what make a clip read as generated and generic (ILL-11 for stills).
- **Check:** Run FILM-STORY-0: which of these choices serves the beat?
- **Fix:** Replace each default with a choice from the beat.
- **Grade:** Craft wisdom (practitioner write-ups) [SRC-108, SRC-109].
- **Source:** [SRC-108, SRC-109]; ILL-11.

---

## QC checklist for a generated clip

1. Watch the whole clip at full speed, at delivered size, with sound, twice (FILM-REV-1). Note what jumped out.
2. Make the contact sheets and cut frames (FILM-GEN-1).
3. Flashing (FILM-ACC-1): any strobe or flicker above threshold? Blocker.
4. Identity (FILM-GEN-2): face crops first, middle, last, per shot. Blocker.
5. Anatomy (FILM-GEN-3, CHAR-9): one line per region per sampled frame with people. Blocker.
6. Text and marks (FILM-GEN-8). Blocker.
7. Objects (FILM-GEN-4) and physics (FILM-GEN-5).
8. Flicker and boiling (FILM-GEN-6): scrub and difference.
9. Light and look across shots (FILM-GEN-7, FILM-LIT-1, FILM-COL-1).
10. Camera and geometry (FILM-GEN-9).
11. Continuity (FILM-CON-1 to FILM-CON-6) and the beat check (FILM-STORY-0).
12. Re-run 1 to 11 on the final render after every fix.

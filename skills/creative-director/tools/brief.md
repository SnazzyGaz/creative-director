# Structured brief and the in-repo front door (v0.11.4)

Run from the repo or the installed skill folder; no service, account or packaged CLI is needed.

```sh
python tools/cd.py brief init 'A quiet exhibition invitation' --out brief.json
python tools/cd.py load --brief brief.json
python tools/cd.py rule CD-7
python tools/cd.py check final.png --brief brief.json
python tools/cd.py select r1.png r2.png r3.png r4.png --brief brief.json > selection.json
```

## Brief contract

For a writing job, name audience, purpose, channel, next action, tone/genre and English variety; record locked versus draftable copy in existing fields/constraints, then load `modules/writing/README.md`. Use `medium: "writing"` for a writing job.

`brief init` copies `brief-template.json` and records the description, without inventing intent or a medium. The new fields are `medium: ""` and `has_people_or_animals: false`; fill `medium` with a nonempty string and set the boolean explicitly, even for a small figure or animal. `load` and `check` reject a missing/empty medium or a non-boolean anatomy flag; schema_version remains 1. It refuses to overwrite a file. Fill the idea, feeling (name the tone and kind of piece: a thriller, a comedy, a children's book, a play, a fete, a concert and what kind of music — this shapes type, colour, energy and adornment), audience, purpose and success before making roughs. Then run `python tools/cd.py load --brief brief.json` and read every file it lists before making or fixing; quote the matched media and rule IDs. Routes come from the first Task/Load table in `core/which-modules.md`, not a parallel keyword list: boundary-matched medium/task phrases, the explicit people/animals gate, screen format and writing-task phrases. Energy uses only feeling/purpose/idea and the live genre examples in that table; it is never inferred from medium alone. Rule references resolve to canonical files; the sitting-right delivery checks remain always listed. Record assumptions explicitly in constraints; must_be_right holds the owner's non-negotiables. The template's empty lists mean **no fixed copy or counts**, not a completed brief. The check reports incomplete intent as unverified.

## Intake when the world is not locked

Follow `core/creative-direction.md` (CD-1 and *When the world is not locked*). A locked brief is enough to load and work. An open ask without "invent" needs a short intake first: what it is for, who it is for, the facts that must appear, and the tone or genre. Propose theme, mood and colour from those answers unless they were already named. An ask to invent needs the finished brief shown to the owner of the work before roughs. Do not default invented worlds to salt, marshes, lighthouses, harbours or coastal weather.

Format width/height and safe_area_px are final rendered pixels, not print points or OCR glyph height. Set kind to fixed or screen. The template uses a 6% short-side text margin (LAY-5); update it when the format changes. Screens use their declared viewport, and a longer rendered document is reported as a format mismatch, not silently cropped.

Copy is a list of complete rendered lines (DOM: visible text runs), for example `[{"text":"OPEN 10–6", "count":1}]`. Comparisons preserve case, punctuation, units and spaces. OCR normalises spaces within a line, so check spacing visually; split or wrapped DOM nodes may need a render transcript. `exact_copy: true` rejects extra lines as well as missing ones. False permits other copy but still checks each required line's count. Counts are physical items, e.g. `[{"item":"cups", "count":10}]`, never OCR word matches.

## Check JSON and exit codes

`check` invokes `autocheck.py` (which reuses contrast, whitespace and balance); its original results remain under `autocheck`. Pages also expose their visible text runs and geometry from the same measurement. For images with code-set type, pass `--boxes PATH` for the pipeline manifest, or put `{stem}-boxes.json` beside the image for automatic discovery. Each row is `[text, [x0,y0,x1,y1], [r,g,b]]`. The manifest strings are compared to brief.copy with the same Counter/exact-copy rules, and its boxes are used for the safe-area check. Provenance names the manifest path. A real manifest mismatch is FAIL. Manifest evidence takes precedence over OCR and supplied transcripts. Only generated lettering without a manifest uses optional system `tesseract` TSV: word tokens below confidence 50 (including -1) are dropped, then retained words are grouped into lines and line boxes. No OCR dependency is installed automatically. `--no-ocr` disables OCR, not manifests. `--ocr-text render.txt` supplies a transcription with explicit provenance, not a claim that OCR ran. It cannot supply geometry. Supplied transcripts and visible DOM text are not fallible OCR: real copy mismatches remain FAIL. An automatic OCR mismatch is FLAG, not FAIL; `crop_boxes` identifies suspect extra lines and `crops` names small PNGs written beside the target in `{stem}-copy-crops/`. Missing lines cannot be localised from OCR, so a whole-frame overview is included for visual reading. Read these images before clearing the flag. `--text-box x0,y0,x1,y1[:large]` forwards image contrast regions and adds their safe-area bounds. Pixel-based type size stays SKIP: no invented font sizes from OCR glyphs. Page type size uses the existing DOM checks (TYPE-3).

Each required check has id, status, passed and provenance. Missing evidence is SKIP, never PASS. `passed` is true only when required checks PASS and autocheck has no FAIL. A required FLAG is not a certified pass, but does not fail the run: if there is no FAIL or required SKIP, the top-level status is FLAG and exit is 0. Ancillary FLAGs remain review questions, not reasons to centre. Exit 0: no mechanical blocker or incomplete required evidence (review any FLAGs); 1: failed or incomplete; 2: invalid input or measurement error (still JSON on stdout). No mechanical pass certifies anatomy, official marks, every must-be-right condition, or aesthetic success. OCR is fallible; CD-7 still requires a read of the render. DOM copy does not detect lettering in canvas or images.

For physical counts, pass `--observations counts.json`, containing the current local image's SHA-256 and a labelled count per item:

```json
{"target_sha256":"<sha256 of final.png>", "counts":{"cups":{"count":10,"provenance":"2x crop final-cups.png, one tick per cup; visual count"}}}
```

This is supplied evidence, not automated object recognition. Wrong-image evidence is rejected; page counts require visual review and remain SKIP here.

## Selection without a second checker

`select` makes a portable comparison packet for 4–8 existing roughs, IDs R1 onward. Open that packet and the images in a **fresh context of the same model**, without the maker's rationale. No model call happens in the script. Compare every pair; write a review JSON with `same_model: true`, `fresh_context: true`, `comparisons` and `shortlist`. Each comparison has a, b, stronger (either ID or null for a tie), reason, trade_off, confidence (high/medium/low). Shortlist 2–3 IDs against the brief, not an averaged taste score. The packet includes a starter shape, not a completed review.

```sh
python tools/cd.py select r1.png r2.png r3.png r4.png --brief brief.json --review review.json
# Only after the owner of the work has picked R2:
python tools/cd.py select r1.png r2.png r3.png r4.png --brief brief.json --review review.json --owner-choice R2
```

The script validates comparisons and records the supplied choice; it does not authenticate context freshness or owner approval. Show the shortlist, wait for that choice, then fix only the winner. On an existing-work edit or consult, do not manufacture four new directions: preserve its intent and record selection as not applicable. “The original is better” can end a comparison; unresolved delivery blockers must still be reported.

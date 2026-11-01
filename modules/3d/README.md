# Module: 3D

How to check 3D work with two companion repos, and how design judgement applies on top. Load with `core/`; add `illustration/` for a composed final render.

- **model-qa** (github.com/SnazzyGaz/model-qa): a "spell-checker" for 3D models. Measures defects a render hides (floating parts, inside-out normals, duplicates, holes, wrong units, asymmetry, UV problems) and reports what, where and how to fix. `--look` adds measurable looks advice and a lit `beauty.png`. MIT. [S29]
- **bot-creative-toolkit** (`bct`, github.com/SnazzyGaz/bot-creative-toolkit): headless Blender/Inkscape/GIMP/potrace for bots. `bct look` renders a labelled multi-view contact sheet and can run model-qa via `--qa`. Also layered images (`bct layers`) and vectors (`bct vector`). MIT. [S30]

Follow each repo's own `AGENTS.md` for commands; this module only says where they fit in the critique loop and what they don't cover.

## Where they sit in the loop

1. **Build** the model (script or `.blend`).
2. **Measure first:** `model-qa check FILE --no-render --brief` with the right `--profile` (`render`/`game` for assembled objects, `print` for printing) and `--category`. Fix high/med issues. These are the 3D equivalent of MUST-BE-RIGHT.
3. **Look:** `bct look FILE -o sheet.png --qa` for one contact sheet plus the model-qa verdict.
4. **Judge appearance** on model-qa's `beauty.png` (lit), not flat clay, using the rules below and `core/`.
5. Fix, re-check (fixes often cause new issues, e.g. UV damage), re-render. Stop per `core/critique-loop.md`.

## Rules

Format: **What / Why / Check / Fix / Source**.

### 3D-1. Built correctly before judged for looks (MUST-BE-RIGHT)
- **What:** No high or medium model-qa issues, or each remaining one is intended and stated.
- **Why:** In model-qa's tests an agent caught 4 of 8 planted defects by eye; the tool caught 7 of 8. Renders hide gaps, flipped normals and duplicates.
- **Check:** `model-qa check FILE --no-render --brief`; exit code 0.
- **Fix:** Use each issue's `fix` hint; ignore intended items in a spec file rather than "fixing" them.
- **Source:** model-qa README and AGENTS.md [S29].

### 3D-2. Right size and right way up (MUST-BE-RIGHT)
- **What:** Real-world scale in metres; Z up; resting on the ground.
- **Why:** Wrong units and lying-on-its-side models break every scene they go into.
- **Check:** `--category` (IMPLAUSIBLE_SIZE, LOOK_PROPORTION, NEAR_GROUND); the `bct look` header shows size in metres.
- **Fix:** Scale, rotate, apply transforms.
- **Source:** [S29, S30].

### 3D-3. Silhouette reads from the main view
- **What:** From the hero camera angle, the object's outline is distinctive and readable.
- **Why:** Same reason as ILL-3: silhouette is what survives at small size.
- **Check:** model-qa `--look` writes `silhouettes.png`; also read its boxy-silhouette advice. Fill the render's alpha black: is the object recognisable?
- **Fix:** Turn the object or camera; exaggerate the defining forms. For characters and props in a set, each should be identifiable from its silhouette alone, as Valve did for *Team Fortress 2*.
- **Source:** model-qa `--look` [S29]; Mitchell et al., *Illustrative Rendering in Team Fortress 2* [S83]; ILL-3.

### 3D-4. Surfaces catch light believably
- **What:** Curves look round (enough segments, smooth shading); hard edges have a small bevel so they catch a highlight; no black shading artefacts.
- **Why:** Faceted curves and razor edges are the clearest "made by a bot" tells in 3D.
- **Check:** model-qa `--look` flags (LOOK_FACETED, LOOK_NO_BEVEL, LOOK_FLAT_SHADED_CURVE, LOOK_BAD_NORMALS). Judge on `beauty.png`.
- **Fix:** Go to the suggested segment count once (don't keep adding); bevel modifier; shade smooth by angle. Don't bevel deliberately low-poly or stylised work.
- **Source:** model-qa AGENTS.md [S29].

### 3D-5. Presentation renders follow the picture rules
- **What:** A final render is an illustration: one key light (TD-LIT-1), clear value separation from the background (CORE-2), deliberate camera height (TD-PER-1) and an unequal composition (ILL-1).
- **Why:** A good model in flat, frontal, centred light looks worse than it is.
- **Check:** Run the core five tests on the beauty render.
- **Fix:** Three-point light: key, fill, and a rim or back light for separation from the background. Set the key-to-fill ratio for the mood: about 2:1 is soft and even, 4:1 is more modelled, 8:1 is dramatic and low-key. Use a darker or lighter backdrop than the object, and put the camera at a deliberate height.
- **Source:** Gurney, *Light and Form* [S20, S21]; lighting ratios [S84]; rim light instead of outlines in TF2 [S83]; core principles.

### 3D-6. Materials stay in physically plausible ranges
- **What:** Non-metal base colours sit between about 30-50 and 240 in sRGB (no pure black or pure white). Raw metals use bright base colours (about 180-255 sRGB). Metalness is mostly 0 or 1.
- **Why:** Values outside these ranges don't occur in real materials. They render too dark, glowing or plastic-looking under good lighting.
- **Check:** Sample the base colour and metallic maps (or material values): min, max, and the share of in-between metalness. **Auto: yes.**
- **Fix:** Clamp the albedo into range; set metalness to 0 or 1 and use in-between values only for transitions such as dust or rust edges.
- **Source:** Adobe, *The PBR Guide* parts 1-2 [S82].

### 3D-7. The view transform doesn't clip the light
- **What:** Lit renders use a filmic tone mapping (AgX in current Blender), not "Standard". Bright areas roll off toward white instead of clipping into flat, oversaturated patches.
- **Why:** Clipped highlights lose form at the brightest point, which is often the focal point.
- **Check:** Inspect the brightest areas: are there flat blobs of pure colour or white? Which view transform was used? **Auto: partly** (count clipped pixels).
- **Fix:** Switch to AgX, then re-balance exposure. Don't fix clipping by dimming the whole scene.
- **Source:** Blender manual, *Displays and Views* [S85].

## Myths and weak claims
- **"More polygons look better":** only up to the point where curves read as round (3D-4). Beyond that, extra density costs performance and adds nothing [S29].
- **"Filmic is the realistic option":** in current Blender, Filmic is superseded by AgX [S85].
- **"You need black outlines for characters to read":** Valve got its separation from distinct silhouettes and rim light rather than dark outlines [S83]. Outlines are a style choice, not a requirement.

## What these tools don't do

model-qa checks whether a model is **built** correctly, not whether it **looks good** or is the right object; `--look` covers only measurable looks problems [S29]. Style, colour and appeal still go through `core/` and, finally, the owner of the work.

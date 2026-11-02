# Module: web and app UI (how it looks)

Layout, components, accessible contrast, colour roles and avoiding the generic AI look. Type numbers live in `typography/` and the spacing scale in CORE-4. Load with `core/`; add `ux/` when people have to complete a task, `typography/` for text-heavy pages.

Format: **What / Why / Check / Fix / Grade / Source**. Rules marked **MUST-BE-RIGHT** are blockers (accessibility minimums); the rest are defaults.

---

### UI-1. Moved to TYPE-2 (one type scale), v0.6.0.

### UI-2. Moved to TYPE-3 (size), TYPE-4 (measure), TYPE-5 (leading) and TYPE-13 (flush left, ragged right), v0.6.0.

### UI-3. Moved to CORE-4 (spacing scale), v0.6.0.

### UI-4. Layout on a grid, primary action obvious
- **What:** Content sits on a clear column grid; each screen has one primary action that is visually strongest.
- **Why:** Users scan for structure and for "what do I do here".
- **Check:** Overlay a grid; look for near-miss alignments. Blur the screen: is the primary action the strongest element after the headline?
- **Fix:** Align to columns; keep a small set of image and block sizes that fit the grid. Give only the primary action a solid fill; make secondary actions outline buttons and tertiary actions text links.
- **Grade:** Craft wisdom.
- **Source:** NN/g, *Visual Hierarchy* [S1]; Müller-Brockmann, *Grid Systems* [S60]; Refactoring UI (button hierarchy) [S57]; CORE-1, CORE-5.

### UI-5. Components are consistent and say their state
- **What:** One style per component type; hover, focus, pressed, disabled, error and loading states all exist and look distinct. Touch targets at least 48 dp (Material), 44 × 44 pt (Apple), or about 1 cm (NN/g).
- **Why:** Inconsistent components make users wonder if they behave differently; missing states hide what the system is doing.
- **Check:** Inventory buttons, inputs, cards. Count variants. Tab through the page: is focus always visible?
- **Fix:** Consolidate into tokens; design every state.
- **Grade:** Partly supported (usability heuristics); target sizes are Standard (platform guidance).
- **Source:** NN/g heuristics #1, #4 [S4]; Material 3 spacing/targets [S9]; Apple HIG [S58]; NN/g touch targets [S67].

### UI-6. Accessible contrast (MUST-BE-RIGHT)
- **What:** Text contrast at least 4.5:1 against its background (3:1 for large text, about 24 px or 18.5 px bold). UI component boundaries and meaningful graphics at least 3:1. Never use colour as the only signal.
- **Why:** Below this, people with low vision or older eyes can't read it; colour-only signals fail for colour-blind users.
- **Check:** Compute the WCAG contrast ratio for each text/background pair, including text over images and placeholder text. **Auto: yes** (`tools/contrast.py`).
- **Fix:** Darken text or lighten ground (or add a scrim behind text on images); add an icon or label beside colour cues.
- **Grade:** Standard (WCAG).
- **Source:** WCAG 2.1 SC 1.4.3 and 1.4.11 [S3, S32]; NN/g, *Visual Hierarchy* (don't rely on colour alone) [S1].

### UI-7. Avoid the generic AI look
- **What:** Don't let defaults make the decisions. Common tells of AI-generated UI: purple-to-blue gradient hero, Inter/Roboto everywhere, centred hero with one button, a row of three identical icon cards, glassmorphism glow, gradient text on a big number, the same radius and shadow on everything, cards nested in cards, vague copy ("seamless", "elevate").
- **Why:** None is wrong alone; several together signal "no one decided this" and make the product indistinguishable. Unrequested decoration also raises visual complexity, the main predictor of low first-impression appeal [S35].
- **Check:** Count the tells above. Two or more: flag. Ask: which colour, type and layout choices come from the brief or brand, and which are defaults?
- **Fix:** Write down tokens (colour roles, type pair, spacing, radius) from the brand or subject before styling; take the accent colour from the subject itself; give shape a role (e.g. pill buttons, square images, small-radius cards); vary section layouts to fit content.
- **Grade:** Craft wisdom (practitioner write-ups).
- **Source:** Anticode, *Why so many AI websites look the same* [S27]; Superdesign, *Why AI design looks generic* [S28]. These are practitioner write-ups, not research; treat the list as a checklist, not a law.
- **Needs a brief:** the fix comes from brand and brief input (CD-1, CD-2), not from more rounds. If there is no direction to draw tokens from, list the tells under Questions for the owner and stop; don't invent a brand.
- **Ask the owner:** whether any of these tells are acceptable for a given project (e.g. Inter is a perfectly good typeface).

### UI-8. Colour as a system of roles and ramps
- **What:** Colours are defined once as roles (primary, surface, error...), each with a paired "on" colour for text and icons. Each hue has a ramp of about 5-10 shades, and the greys have about 8-10.
- **Why:** Picking colours ad hoc gives near-duplicates and pairs that fail contrast. HSL "lightness" is not perceptual, so ramps built in HSL have uneven steps between hues.
- **Check:** Collect every colour in use. Are there near-duplicates? Is every text/background pair a defined role pair? Convert the ramps to OKLCH: does L step evenly, and is it the same across hues at the same step?
- **Fix:** Build ramps in OKLCH (fixed L steps, chroma per hue) and map every use to a role. Re-check the pairs with WCAG ratios (UI-6). OKLCH lightness is a guide, not a contrast test.
- **Grade:** Craft wisdom.
- **Source:** Material 3 colour roles [S59]; Refactoring UI, *Building your color palette* [S57]; Evil Martians / Ottosson on OKLCH [S50]; Munsell (hue, value, chroma) [S49].

### UI-9. Hierarchy by turning things down
- **What:** Secondary content is made quieter with weight and colour (lighter grey, normal weight), not only with smaller size. Separation comes from space and background shade before borders.
- **Why:** Making everything bigger and bolder flattens hierarchy, and borders everywhere add noise.
- **Check:** Count the border lines, the bold weights and the font sizes. On coloured backgrounds, look for grey text, which looks dirty and loses contrast.
- **Fix:** De-emphasise labels and metadata. Swap some borders for spacing or a subtle background shift. On a coloured ground, use a tint or shade of that colour (or white at reduced opacity) instead of grey, then check UI-6.
- **Grade:** Craft wisdom.
- **Source:** Wathan & Schoger, Refactoring UI and *7 Practical Tips for Cheating at Design* [S57]; CORE-3.

### UI-10. Text can grow without breaking (MUST-BE-RIGHT, every project)
- **What:** On every project, without exception, text scales to 200% (browser zoom, iOS Dynamic Type) without being clipped, overlapping or hiding content or controls.
- **Why:** Many people read at large sizes. Fixed-height boxes and truncation hide content from them.
- **Check:** Zoom to 200%, or set the largest Dynamic Type size. Is anything clipped, overlapped, or truncated in a way that loses meaning? **Auto: partly** (screenshot diff at two zoom levels; `tools/shot.sh`).
- **Fix:** Use relative units, min-height not fixed height, and layouts that wrap or stack.
- **Grade:** Standard (WCAG).
- **Source:** WCAG 2.1 SC 1.4.4 [S86]; Apple HIG typography and larger-text criteria [S58].

## Myths and weak claims
- **Golden-ratio type scales are "more harmonious":** no evidence for a special ratio [S38]. Pick the ratio for density (TYPE-2).
- **"HSL lightness 50% means equal brightness":** false. Yellow and blue at the same HSL L differ a lot. Use OKLCH L or luminance [S50].
- **"An OKLCH lightness gap guarantees contrast":** it doesn't. Compute WCAG ratios [S3, S50].
- **Generic-AI tells (UI-7) as proof of bad design:** they are practitioner heuristics, not research [S27, S28].

More depth (grid construction, Refactoring UI habits, platform specifics): `notes.md`.

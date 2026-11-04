# Module: web and app UI (how it looks)

Layout, components, accessible contrast, colour roles, avoiding the generic AI look, and screens with a mood of their own (UI-12). Type numbers live in `typography/` and the spacing scale in CORE-4. Load with `core/`; add `ux/` when people have to complete a task, `typography/` for text-heavy pages.

Format: **What / Why / Check / Fix / Grade / Source**. Rules marked **MUST-BE-RIGHT** are blockers (accessibility minimums); the rest are defaults.

---

### UI-4. Layout on a grid, primary action obvious
- **What:** Content sits on a clear column grid; each screen has one primary action that is visually strongest.
- **Why:** Users scan for structure and for "what do I do here".
- **Check:** Overlay a grid; look for near-miss alignments. Blur the screen: is the primary action the strongest element after the headline?
- **Fix:** Align to columns; keep a small set of image and block sizes that fit the grid. Give only the primary action a solid fill; make secondary actions outline buttons and tertiary actions text links.
- **Grade:** Craft wisdom.
- **Source:** NN/g, *Visual Hierarchy* [SRC-1]; Müller-Brockmann, *Grid Systems* [SRC-60]; Refactoring UI (button hierarchy) [SRC-57]; CORE-1, CORE-5.

### UI-5. Components are consistent and say their state
- **What:** One style per component type; hover, focus, pressed, disabled, error and loading states all exist and look distinct. Touch targets at least 48 dp (Material), 44 × 44 pt (Apple), or about 1 cm (NN/g).
- **Why:** Inconsistent components make users wonder if they behave differently; missing states hide what the system is doing.
- **Check:** Inventory buttons, inputs, cards. Count variants. Tab through the page: is focus always visible?
- **Fix:** Consolidate into tokens; design every state.
- **Grade:** Partly supported (usability heuristics); target sizes are Standard (platform guidance).
- **Source:** NN/g heuristics #1, #4 [SRC-4]; Material 3 spacing/targets [SRC-9]; Apple HIG [SRC-58]; NN/g touch targets [SRC-67].

### UI-6. Accessible contrast (MUST-BE-RIGHT)
- **What:** Text contrast at least 4.5:1 against its background (3:1 for large text, about 24 px or 18.5 px bold). UI component boundaries and meaningful graphics at least 3:1. Never use colour as the only signal.
- **Why:** Below this, people with low vision or older eyes can't read it; colour-only signals fail for colour-blind users.
- **Check:** Compute the WCAG contrast ratio for each text/background pair, including text over images and placeholder text. **Auto: yes** (`tools/contrast.py`).
- **Fix:** Darken text or lighten ground (or add a scrim behind text on images); add an icon or label beside colour cues.
- **Grade:** Standard (WCAG).
- **Source:** WCAG 2.1 SC 1.4.3 and 1.4.11 [SRC-3, SRC-32]; NN/g, *Visual Hierarchy* (don't rely on colour alone) [SRC-1].

### UI-7. Avoid the generic AI look
- **What:** Don't let defaults make the decisions. Common tells of AI-generated UI: purple-to-blue gradient hero, Inter/Roboto everywhere, centred hero with one button, a row of three identical icon cards, glassmorphism glow, gradient text on a big number, the same radius and shadow on everything, cards nested in cards, vague copy ("seamless", "elevate").
- **Why:** None is wrong alone; several together signal "no one decided this" and make the product indistinguishable. Unrequested decoration also raises visual complexity, the main predictor of low first-impression appeal [SRC-35].
- **Check:** Count the tells above. Two or more: flag. Ask: which colour, type and layout choices come from the brief or brand, and which are defaults?
- **Fix:** Write down tokens (colour roles, type pair, spacing, radius) from the brand or subject before styling; take the accent colour from the subject itself; give shape a role (e.g. pill buttons, square images, small-radius cards); vary section layouts to fit content.
- **Grade:** Craft wisdom (practitioner write-ups).
- **Source:** Anticode, *Why so many AI websites look the same* [SRC-27]; Superdesign, *Why AI design looks generic* [SRC-28]. These are practitioner write-ups, not research; treat the list as a checklist, not a law.
- **Needs a brief:** the fix comes from brand and brief input (CD-1, CD-2), not from more rounds. If there is no direction to draw tokens from, list the tells under Questions for the owner and stop; don't invent a brand.
- **Ask the owner:** whether any of these tells are acceptable for a given project (e.g. Inter is a perfectly good typeface).

### UI-8. Colour as a system of roles and ramps
- **What:** Colours are defined once as roles (primary, surface, error...), each with a paired "on" colour for text and icons. Each hue has a ramp of about 5-10 shades, and the greys have about 8-10.
- **Why:** Picking colours ad hoc gives near-duplicates and pairs that fail contrast. HSL "lightness" is not perceptual, so ramps built in HSL have uneven steps between hues.
- **Check:** Collect every colour in use. Are there near-duplicates? Is every text/background pair a defined role pair? Convert the ramps to OKLCH: does L step evenly, and is it the same across hues at the same step?
- **Fix:** Build ramps in OKLCH (fixed L steps, chroma per hue) and map every use to a role. Re-check the pairs with WCAG ratios (UI-6). OKLCH lightness is a guide, not a contrast test.
- **Grade:** Craft wisdom.
- **Source:** Material 3 colour roles [SRC-59]; Refactoring UI, *Building your color palette* [SRC-57]; Evil Martians / Ottosson on OKLCH [SRC-50]; Munsell (hue, value, chroma) [SRC-49].

### UI-9. Hierarchy by turning things down
- **What:** Secondary content is made quieter with weight and colour (lighter grey, normal weight), not only with smaller size. Separation comes from space and background shade before borders.
- **Why:** Making everything bigger and bolder flattens hierarchy, and borders everywhere add noise.
- **Check:** Count the border lines, the bold weights and the font sizes. On coloured backgrounds, look for grey text, which looks dirty and loses contrast.
- **Fix:** De-emphasise labels and metadata. Swap some borders for spacing or a subtle background shift. On a coloured ground, use a tint or shade of that colour (or white at reduced opacity) instead of grey, then check UI-6.
- **Grade:** Craft wisdom.
- **Source:** Wathan & Schoger, Refactoring UI and *7 Practical Tips for Cheating at Design* [SRC-57]; CORE-3.

### UI-10. Text can grow without breaking (MUST-BE-RIGHT, every project)
- **What:** On every project, without exception, text scales to 200% (browser zoom, iOS Dynamic Type) without being clipped, overlapping or hiding content or controls.
- **Why:** Many people read at large sizes. Fixed-height boxes and truncation hide content from them.
- **Check:** Zoom to 200%, or set the largest Dynamic Type size. Is anything clipped, overlapped, or truncated in a way that loses meaning? **Auto: partly** (screenshot diff at two zoom levels; `tools/shot.sh`).
- **Fix:** Use relative units, min-height not fixed height, and layouts that wrap or stack.
- **Grade:** Standard (WCAG).
- **Source:** WCAG 2.1 SC 1.4.4 [SRC-86]; Apple HIG typography and larger-text criteria [SRC-58].

### UI-11. No invented product screens in finished work
- **What:** A hero, ad or poster for an app shows only screens, features and UI the owner supplied. Don't generate phone screens, dashboards or app UI with made-up content for finished work: they promise features nobody agreed and fill with garbled text. Invented UI belongs only in a mock-up the brief asks for, labelled as a mock.
- **Why:** Invented screens are additions (AES-10) and invented facts (FP-3), and generators garble small UI text (BRAND-8). In batch 4 the owner of the work preferred a hero with a big generated phone screen on looks, but noted that the with-skill version, which followed the brief, would win if the brief meant finished work (S39). Internal evidence, one judge.
- **Check:** List every screen or UI element in the piece. Is each one supplied, or a labelled mock?
- **Fix:** Use the supplied screenshot; or show the product's effect (the person, the outcome) instead of its screen; or label the mock and ask the owner.
- **Grade:** Procedure, from AES-10 and FP-3.
- **Source:** AES-10; FP-3; BRAND-8; `examples/blind-test/RESULTS.md`.

### UI-12. Screens need soul: a named mood and one expressive move
- **What:** Before styling a screen, write one line naming its mood and atmosphere (e.g. "a quiet harbour at dawn: calm, salt-washed, early light"), and let the palette, imagery, type and spacing follow it (CD-2). Each screen that greets or sells (a hero, landing page, pricing section, app home or summary) gets one focal image or expressive move: a photograph or illustration with atmosphere, a confident display headline, a colour field, a bold crop. Pricing and summary screens count: a plan card or a stats row can carry the brand's character without losing its order. Task clarity, contrast and real content still win (UI-4, UI-6, UI-11); forms, settings and checkout stay calm (EN-1).
- **Why:** In batch 8, screens were the skill's weakest theme (2 to 3): tidy, correct screens lost to ones that "have soul" (S88) or as "too bland and basic" (S100); even a with-skill win had the weaker atmosphere (S107), and a liked personality was noted as perhaps too striking (S79). Judgements of a web page's visual appeal form in about 50 ms [SRC-36], and attractive interfaces earn more tolerance for minor problems [SRC-34]; those studies support that looks matter, not this rule's exact moves.
- **Check:** Is the mood line written, and does the thumbnail show it? Name the one expressive move: if there is none, the screen is sterile (EN-3 table). Then the task check: is the primary action still found first or second (UI-4)? Is anything invented (UI-11)?
- **Fix:** Add one move from the brief's own material (its photo, its colour, its name set large); warm or deepen the ground; give the key number or plan a display setting. If it got too loud, keep the move and quieten everything else.
- **Grade:** Craft wisdom. Internal evidence, one judge, one batch; untested as a rule. The cited studies only partly support it.
- **Source:** Lindgaard et al. [SRC-36]; NN/g, aesthetic-usability effect [SRC-34]; CD-2; EN-1; `examples/blind-test/RESULTS.md`.

### UI-13. Design every screen state, not only the full one
- **What:** Each screen has its empty, loading, error, partial and success states designed, not left to defaults. Empty says what will appear and offers the first action; loading for a whole page shows the page's shape (a skeleton), for a single part a spinner, and over about 10 s a progress bar; errors say what happened and how to recover (UX-3); a status change that appears without moving focus is announced to screen readers.
- **Why:** A totally empty area leaves people unsure whether it is loading, broken or genuinely empty; a designed empty state reports the status, teaches what goes there and links to the first step, and a "no records" message shown while still loading is worse than none [SRC-423]. Skeletons suit full-page loads under about 10 seconds, spinners suit one module, and longer waits need a progress bar; under a second, no indicator is needed [SRC-424, SRC-65]. WCAG asks for status messages to reach assistive technology without taking focus [SRC-425].
- **Check:** List the states for each screen and render each one (empty account, slow network, failed request, one item, a thousand items). Is any state a blank area or a raw error code?
- **Fix:** Write and design the missing states; reuse the page's layout for its skeleton; add a live region for status text.
- **Grade:** Partly supported (usability guidance); status messages are Standard (WCAG 4.1.3).
- **Source:** NN/g, empty states [SRC-423]; NN/g, skeleton screens [SRC-424]; Nielsen, response times [SRC-65]; WCAG 2.2 SC 4.1.3 [SRC-425]; UX-2; UX-3.

### UI-14. Dark mode is designed, not inverted
- **What:** When there is a dark theme, build it from the colour roles (UI-8): dark grey surfaces rather than pure black for large areas, lighter surfaces for raised layers, accent colours re-tuned so they don't glow, and every text and control pair re-checked for contrast (UI-6). Images and illustrations get dark-ready versions where white boxes would flash. Offer the theme where people read for long or at night, and follow the system setting; light stays the default unless the brief says otherwise.
- **Why:** Platform guidance builds dark themes from separate colour roles and asks for contrast in both [SRC-426, SRC-59]. For people with normal vision, reading tends to be better in light mode, especially for small text, while some people with low vision do better in dark mode, which is why it should be a choice [SRC-427].
- **Check:** Switch the theme: does every pair still pass UI-6? Any pure-white image box, invisible divider, or saturated colour that vibrates on the dark ground? Does it follow the system setting?
- **Fix:** Map each role to a dark value; desaturate and lighten accents; give images transparent or dark-ready versions.
- **Grade:** Standard for contrast (WCAG) and platform guidance; partly supported for which mode reads better.
- **Source:** Apple HIG, Dark Mode [SRC-426]; Material 3 colour roles [SRC-59]; NN/g, *Dark Mode vs. Light Mode* [SRC-427]; WCAG [SRC-3].

### UI-15. Responsive: reflows at 320 px wide, designed at every width
- **What:** Content reflows into one column at 320 CSS px wide (or 400% zoom) without sideways scrolling, except for things that need two dimensions (maps, data tables, wide charts). Breakpoints come from where the content breaks, not from device names. Check at least phone, tablet and desktop widths, and the in-between width where things first collide.
- **Why:** WCAG requires reflow at 320 CSS px so that people who zoom don't scroll in two directions [SRC-428]; intrinsic layouts let the content decide the breakpoints [SRC-56].
- **Check:** Screenshot at 320, 768, 1024 and 1440 px, then drag slowly between them (`tools/shot.sh`): any overlap, horizontal scroll, orphaned single word in a heading, or primary action pushed below a wall of content on the phone?
- **Fix:** Use wrapping and stacking layouts; set breakpoints where it breaks; reorder so the primary action stays near the top on narrow screens.
- **Grade:** Standard (WCAG 1.4.10); the breakpoint advice is craft.
- **Source:** WCAG 2.2 SC 1.4.10 [SRC-428]; *Every Layout* [SRC-56]; UI-10.

### UI-16. Motion has a job, and respects reduced motion
- **What:** Every animation explains something: where an element came from or went, what changed, what is loading. Keep it short (most interface transitions are well under half a second) and never block the task. Anything that moves for more than 5 seconds on its own can be paused. When the system asks for reduced motion, swap movement and zooms for fades or no animation, and turn off parallax and auto-play.
- **Why:** WCAG asks that motion started by interaction can be turned off and that moving content lasting over 5 seconds can be paused, stopped or hidden [SRC-429]; movement can make people with vestibular disorders unwell. Browsers expose the setting as `prefers-reduced-motion` [SRC-430], and platform guidance says motion should be purposeful and optional [SRC-431]. Flashing is a separate blocker (FILM-ACC-1).
- **Check:** For each animation, name its job. Turn on reduced motion in the system: does large movement, parallax or auto-play stop? Can a carousel or background video be paused?
- **Fix:** Cut decorative motion; add a `prefers-reduced-motion` branch; add a pause control.
- **Grade:** Standard (WCAG 2.2.2; 2.3.3 is AAA, applied here as the default); purposeful motion is craft.
- **Source:** WCAG 2.2 SC 2.2.2 and 2.3.3 [SRC-429]; MDN, `prefers-reduced-motion` [SRC-430]; Apple HIG, Motion [SRC-431].

## Myths and weak claims
- **Golden-ratio type scales are "more harmonious":** no evidence for a special ratio [SRC-38]. Pick the ratio for density (TYPE-2).
- **"HSL lightness 50% means equal brightness":** false. Yellow and blue at the same HSL L differ a lot. Use OKLCH L or luminance [SRC-50].
- **"An OKLCH lightness gap guarantees contrast":** it doesn't. Compute WCAG ratios [SRC-3, SRC-50].
- **Generic-AI tells (UI-7) as proof of bad design:** they are practitioner heuristics, not research [SRC-27, SRC-28].

More depth (grid construction, Refactoring UI habits, platform specifics): `notes.md`.

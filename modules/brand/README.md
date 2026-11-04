# Module: brand

Reading a brand guide and applying it, or working without one. Load with `core/` whenever work carries a name, logo or product, and add the module for the medium (web-ui, layout, illustration). If the brief has no brand input at all, run `core/brand-intake.md` first.

Format: **What / Why / Check / Fix / Grade / Source**. Rules marked **MUST-BE-RIGHT** are blockers; the rest are defaults.

What a brand is for, on evidence: brands are remembered through **distinctive assets** (colours, shapes, characters, type, sounds) that people link to the brand name. Assets only work if they are used consistently, over time, and are actually unique to the brand [SRC-120]. So the critique question is not "is it pretty" but "would someone know whose this is".

The known failure this module addresses: critique rounds remove errors but cannot remove the generic look. That needs brand input ([examples/web-ui-landing](../../examples/web-ui-landing/log.md), [example](../../examples/brand-intake/)).

---

### BRAND-1. Read the guide before making anything
- **What:** If a guide exists, extract its rules into a token sheet first: colour roles and values, type families and roles, logo files and rules, voice, imagery style, and any do-nots.
- **Why:** Guides are long; agents skim them and then fall back to defaults. A token sheet makes the rules checkable.
- **Check:** Is there a written sheet with values (hex, font names, sizes, clear space) and the page each came from? Is anything marked "don't" in the guide present in the work?
- **Fix:** Write the sheet (format in `core/brand-intake.md`) and check the work against it line by line. If the guide contradicts itself, note it and ask the owner.
- **Grade:** Procedure.
- **Source:** Wheeler [SRC-119]; CD-1.

### BRAND-2. Colours: exact values, right roles, right proportions
- **What:** Use the brand's own values, in the colour space given (hex/RGB for screen, CMYK or spot for print). Respect the role each colour has (primary, accent, background) and the rough proportions the guide shows. Accessible contrast still applies (UI-6).
- **Why:** Distinctive colour is one of the strongest brand assets, and near-misses weaken it [SRC-120]. A brand accent used as body-text colour often fails contrast.
- **Check:** Sample the colours in the render and compare to the sheet (ΔE under about 3 is a match by eye). Is any off-brand colour present? Does any brand colour pair fail 4.5:1 for text?
- **Fix:** Replace near-misses with exact values. Where a brand pair fails contrast, use the brand's darker or lighter step, or move the colour to a non-text role. Never ship a contrast failure to match a guide; flag the conflict to the owner.
- **Grade:** Partly supported (distinctive brand assets [SRC-120]).
- **Source:** Romaniuk [SRC-120]; Wheeler [SRC-119]; UI-6.

### BRAND-3. Type follows the guide, set well
- **What:** Use the brand's families for their stated roles. If a family isn't available (web licence, platform), use the guide's named fallback, or the closest match by category, x-height and width, and say so.
- **Why:** Type is a distinctive asset like colour. A silent substitution looks off-brand to anyone who knows it.
- **Check:** Compare computed font families to the sheet. Any substitution not listed as a fallback?
- **Fix:** Load the brand fonts, or document the fallback in the hand-off. Then apply the typography module (TYPE-2 to TYPE-6).
- **Grade:** Procedure.
- **Source:** Wheeler [SRC-119]; TYPE-1.

### BRAND-4. Official marks: the real file, unaltered, at good quality (MUST-BE-RIGHT)
- **What:** This covers any official mark in the work: the client's own logo, and also sports teams, sponsors, crests, partner and product logos. The default is to **include the official mark**, at better quality rather than worse, from an official file. Use the first of these that exists:
  1. the file the owner supplies;
  2. the brand's own site, press kit or brand centre;
  3. Wikimedia Commons, checked against the official source for shape and colour.

  Prefer a vector or the largest raster. Use it unaltered: official proportions and colours, the version the guide gives for the background, its clear space (often a unit of the logo, such as the cap height or a symbol width) and its minimum size. Never redraw, retype, restyle, recolour, stretch, rotate, add effects to, or AI-generate a mark, not even to "clean it up" or to match the piece's style. The only cleaning allowed:
  - knocking out the background behind the mark;
  - a faithful trace of a low-quality file into a vector, verified by the overlay check below;
  - a one-colour silhouette (all of the mark in one ink) where the guide gives no version for the background. The shapes never change.

  If no file exists, set the trademark name in plain text in the piece's own type; don't draw a mark. A labelled placeholder (a plain box reading "[Team] crest: official file needed") is for symbols with no name to set. Say which you used in the hand-off.

  **Official pieces** (a notice, sign, leaflet or public-information sheet from a council, service, school or venue): the issuer's mark is part of the message, so the default is the real mark, with the name, at the top, where it reads as the official say-so rather than as advertising. If no file was supplied, ask for it before delivery; if the piece must go out first, leave a labelled slot at the mark's size ("[Issuer] logo: official file needed") and flag it in the critique as open. Never invent a crest or emblem (BRAND-8), and don't settle for a bare, characterless text header in its place: in the repo's blind test, the owner of the work called official pieces without their real marks amateurish, like a children's project (`examples/blind-test/RESULTS.md`; one judge, internal evidence).
- **Why:** A logo is a trademark. It identifies who the goods or services come from [SRC-170]. In UK law, using a sign identical with or similar to a registered mark, in the course of trade and in a way likely to confuse, infringes it [SRC-171]. Brand guides are explicit. Spotify says its logo is not to be modified or added to, and its orientation, colour and composition are not to change [SRC-172]. Mastercard says its artwork is to be downloaded and not altered, and its Symbol is used only in full colour [SRC-173]. A file on Commons carries no permission to use the trademark; that stays with the owner of the mark [SRC-174]. Image generators routinely garble marks. A near-miss mark is worse than none, because it looks like a fake.
- **Check:**
  - The logo's width-to-height ratio matches the source file within 1%.
  - Colours are sampled against the guide (ΔE under about 3).
  - The gap to the nearest element is at least the clear-space unit.
  - Its width at display size is at or above the minimum.
  - Compared side by side with the source at 200%, it has the same letters and the same shapes.
  - **Overlay check:** lay the placed mark over the source at the same size (50% opacity or a difference blend). The outlines coincide; nothing is added, dropped or moved. Re-run after every trace, knockout or recolour.
  - The hand-off names the source of each mark (owner, brand site, or Commons with its file page).
  - For third-party marks, a line notes that permission to use them is the owner's call.
  - On an official piece: the issuer's real mark sits with its name at the top, or a labelled slot does and the critique lists it as open.
- **Fix:**
  - Place the original file.
  - Restore clear space by moving other elements, not by shrinking the logo below its minimum.
  - On dark or busy grounds, use the guide's one-colour or reversed version.
  - If you can't find a faithful source, set the name in plain text (or, for a nameless symbol, use the labelled placeholder) and ask the owner for the file. On an official piece, use the labelled slot as well as the name, and list it as open in the critique.
- **Grade:** Standard (trade-mark law and brand guidelines).
- **Source:** Wheeler [SRC-119]; USPTO [SRC-170]; Trade Marks Act 1994 s.10 [SRC-171]; Spotify [SRC-172]; Mastercard [SRC-173]; Wikimedia Commons [SRC-174].

### BRAND-5. Voice matches, in words and in pictures
- **What:** Headlines, labels and microcopy follow the brand's voice (the guide's words, or the three from intake). Tone may shift with context (error message vs launch post); voice stays the same.
- **Why:** Tone of voice measurably changes how people judge a brand's friendliness, trustworthiness and desirability [SRC-121]. Generic AI copy ("seamless", "elevate", "unlock") has no voice.
- **Check:** Place each piece of copy on NN/g's four scales: funny-serious, formal-casual, respectful-irreverent, enthusiastic-matter-of-fact. Does it land where the guide says? Count generic filler words.
- **Fix:** Rewrite to the voice; cut filler; never invent facts, claims or quotes (CD-1). Copy changes beyond fixing errors are suggestions for the owner.
- **Grade:** Partly supported (tone-of-voice testing [SRC-121]).
- **Source:** Moran, NN/g [SRC-121]; Mailchimp Content Style Guide, voice and tone [SRC-122].

### BRAND-6. Consistent across pieces
- **What:** Pieces in one set (a site and its social cards, a deck, a campaign) share the same tokens: colours, type, logo placement, image treatment, corner radius.
- **Why:** Distinctive assets only build memory when repeated consistently [SRC-120]. Each piece "being a bit different" erodes them.
- **Check:** Put the pieces side by side as thumbnails. Same palette, type, logo position and image style? List any token that differs and why. **Set-level pass for a series:** after each piece passes on its own, check the set together:
  - the logo is the same size and in the same position;
  - the margins and the header/footer device are the same;
  - the palette logic is shared, e.g. one shared neutral plus one accent per piece;
  - the type logic is shared, i.e. the same roles map to the same faces.

  Each piece still keeps its own theme and image.
- **Fix:** Pull every piece from one token sheet; vary layout and content, not the assets. Write the set's shared tokens down once and build every piece from them.
- **Grade:** Partly supported (distinctive brand assets [SRC-120]).
- **Source:** Romaniuk [SRC-120]; Wheeler [SRC-119].

### BRAND-7. No brand? Make the defaults visible and owned
- **What:** When intake gets no answers, use the assumed token sheet from `core/brand-intake.md`, build from the subject (its materials, place, audience), and label every assumed choice.
- **Why:** Hidden defaults produce the generic look (UI-7, ILL-11, TYPE-9). Labelled assumptions turn it into a question the owner can answer.
- **Check:** Does the hand-off list the assumed colours, type and voice? Can each be traced to the subject rather than to a tool's default?
- **Fix:** Add the "assumed" sheet and a question for the owner. Don't run extra rounds to fix "generic"; ask.
- **Grade:** Procedure.
- **Source:** CD-1, CD-2; web-ui-landing log.

### BRAND-8. No invented marks in generated imagery (MUST-BE-RIGHT)
- **What:** Generated or edited images often put pseudo-logos, fake wordmarks and garbled lettering on things that would carry a brand in real life. Look at jerseys and kits, bottles and cans, packaging, signage and shopfronts, vehicles, screens, pitch boards and caps. Each mark must be one of two things: the official one, placed from the file per BRAND-4, or none at all.
- **Why:** An invented mark reads as a fake, or as an existing brand the owner did not choose. A mark similar to a real one can raise the same confusion problem as copying it [SRC-171]. Generators don't know which brands the brief allows.
- **Check:**
  - Crop every surface where a mark could appear at 2x-4x, and write one line per crop: none, official (with its source) or invented.
  - Read any lettering. Gibberish text that looks like a logo counts as invented.
  - Re-check after every regenerate or edit.
- **Fix:**
  - Regenerate with the surfaces described as plain ("plain white jersey, no logos or text; unlabelled bottle").
  - Or paint the mark out to the plain surface.
  - Then, if the brief calls for a real mark, composite the official file in afterwards (BRAND-4), following the surface's perspective without distorting the mark's proportions beyond what the surface's own perspective causes.
  - Never ask a generator to draw a real logo.
- **Grade:** Standard (trade-mark law).
- **Source:** BRAND-4; Trade Marks Act 1994 s.10 [SRC-171]; ILL-11.

### BRAND-9. Logos and mascots: one step past the literal
- **What:** Name the literal subject (a path, a kangaroo, a book), then take one step of metaphor: a second reading, a related action or a shape that carries the brand's promise (a path that is also a rising line; a kangaroo whose pouch holds a book). Stop there. Zero steps is a clip-art label; two steps is an abstraction that loses the subject. The mark also suits the audience and where it will live (a children's library, a charity letterhead).
- **Why:** In batch 8 a with-skill logo was called "way literal, not creative" against one too abstract that the owner still preferred visually (S93); a mascot lost to one better suited to its brief and context (S97); a simple logo that "sells it" beat a busy one (S87). Internal evidence, one judge; the middle path is this rule's reading of those notes.
- **Check:** Write the literal subject and the one extra reading in a line each. Can a stranger name the subject at thumbnail? Can they get the second reading once told? If either fails, it is one step short or one too far.
- **Fix:** Too literal: find the brand's promise in a verb (rise, shelter, carry) and fold it into the subject's shape. Too abstract: bring back one recognisable feature of the subject.
- **Grade:** Craft wisdom. Internal evidence, one judge, one batch; untested as a rule.
- **Source:** BRAND-7; ILL-17; `examples/blind-test/RESULTS.md`.

### BRAND-10. Packaging: the brand name has character, and decoration reads as brand
- **What:** On a pack, the brand name is a designed mark (drawn or chosen lettering, a lock-up, a shape it sits in) with the brand's character, not a basic typed line. Decoration and pattern read as the brand's world, not as ingredients or contents (florals on a chocolate wrapper read as flavour). Then the layout still has balance, one eye pull and a clear flow from brand to product to the facts (COMP-19, LAY-3).
- **Why:** Brands are recognised by distinctive assets used consistently [SRC-120], and pack imagery sets expectations of the contents [SRC-334]. In batch 8 a coffee bag won though its branding was basic (S102), a wrapper's florals read as ingredients (S89), and a label with good brand type lost on balance, eye pull and flow (S91). The cases are internal evidence, one judge.
- **Check:** At thumbnail, cover the product name: does the brand still read as a mark with a personality? Point at each decorative element and say what a shopper would think it is: brand or contents? Blur test: one eye pull, then brand, product, facts?
- **Fix:** Draw or set the brand name as a lock-up with one distinctive move; move ingredient imagery to where it means contents, and give the brand its own motif; rebalance with a counterweight (COMP-2, COMP-19).
- **Grade:** Partly supported for distinctive assets and expectations [SRC-120, SRC-334]; the rest is craft wisdom with internal cases.
- **Source:** Romaniuk [SRC-120]; Piqueras-Fiszman & Spence [SRC-334]; BRAND-5; EN-2 item 8; `examples/blind-test/RESULTS.md`.

---

## Making a logo (LOGO-1 to LOGO-16)

To make or change a mark, also load `logo.md` (the rules, about 3,800 tokens) and, when choosing a type, mood or clever move, `logo-notes.md`; for what to show and how to reduce and build it, `mark-making.md`; for double readings, `clever-marks.md`. The idea comes first; the rules are the edit pass. One line each:

- **LOGO-1** Idea first: brief, word map, 20+ thumbnails over four routes, then pick.
- **LOGO-2** Simple enough to remember, distinctive enough to own.
- **LOGO-3** Works at 16 px and on a 1 cm stamp, with a small version if needed.
- **LOGO-4** One colour first, reversed second, full colour last.
- **LOGO-5** A system: lockups, clear space, minimum size, matched weights.
- **LOGO-6** Grid to start, eye to finish (optical corrections).
- **LOGO-7** Name the quality, then choose the shapes that carry it.
- **LOGO-8** Clever reads second, never instead; check unintended readings.
- **LOGO-9** Pick the logo type for the name, the budget and the life.
- **LOGO-10** Trends are seasoning; the mark stands without them.
- **LOGO-11** Not confusable, and registrable (MUST-BE-RIGHT).
- **LOGO-12** Redesigns keep the equity.
- **LOGO-13** Test in the world: size ladder, blur, one colour, five mockups.
- **LOGO-14** Dynamic identities keep one constant.
- **LOGO-15** Choose the abstraction level on purpose; reduce from the real thing.
- **LOGO-16** A second reading must be identifiable and meaningful once seen.

**Further reading:** Airey, *Logo Design Love* [SRC-339]; Wheeler [SRC-119]; Chermayeff, Geismar & Haviv, *Identify* [SRC-340]; Mollerup, *Marks of Excellence* [SRC-343]; Hyland & Bateman, *Symbol* [SRC-344]; Evamy, *Logo* [SRC-345]; Müller, *Logo Modernism* [SRC-346]; Brand New [SRC-375]. More in `logo-notes.md`.

---

## Myths

- **"A brand is its logo."** Logos are one asset among several. Colour, type, shapes and characters can be more distinctive than the mark itself [SRC-120].
- **"Consistency is boring; refresh it often."** People who aren't the brand team notice assets far less than the team does. Frequent changes waste the memory they've built [SRC-120].
- **"Colour X means trust / energy."** See `core/evidence.md`: colour-emotion claims are weak. Choose brand colours for distinctiveness and contrast, not psychology.
- **"A great logo has a hidden trick."** Most lasting marks are plain; a trick helps only when the mark already works without it and the hidden part is seen (LOGO-8, LOGO-16).
- **"The golden ratio makes a logo work."** Golden overlays are mostly drawn after the fact; use geometry to decide, not to justify (`mark-making.md`).
- **"A simple mark is always better."** Very simple marks are harder to own and, in one study, less memorable than moderately elaborate ones [SRC-359]; aim for one distinctive feature (LOGO-2).

# Module: brand

Reading a brand guide and applying it, or working without one. Load with `core/` whenever work carries a name, logo or product, and add the module for the medium (web-ui, layout, illustration). If the brief has no brand input at all, run `core/brand-intake.md` first.

Format: **What / Why / Check / Fix / Source**. Rules marked **MUST-BE-RIGHT** are blockers; the rest are defaults.

What a brand is for, on evidence: brands are remembered through **distinctive assets** (colours, shapes, characters, type, sounds) that people link to the brand name. Assets only work if they are used consistently, over time, and are actually unique to the brand [S120]. So the critique question is not "is it pretty" but "would someone know whose this is".

The known failure this module addresses: critique rounds remove errors but cannot remove the generic look. That needs brand input ([examples/web-ui-landing](../../examples/web-ui-landing/log.md), [example](../../examples/brand-intake/)).

---

### BRAND-1. Read the guide before making anything
- **What:** If a guide exists, extract its rules into a token sheet first: colour roles and values, type families and roles, logo files and rules, voice, imagery style, and any do-nots.
- **Why:** Guides are long; agents skim them and then fall back to defaults. A token sheet makes the rules checkable.
- **Check:** Is there a written sheet with values (hex, font names, sizes, clear space) and the page each came from? Is anything marked "don't" in the guide present in the work?
- **Fix:** Write the sheet (format in `core/brand-intake.md`) and check the work against it line by line. If the guide contradicts itself, note it and ask the owner.
- **Source:** Wheeler [S119]; CD-1.

### BRAND-2. Colours: exact values, right roles, right proportions
- **What:** Use the brand's own values, in the colour space given (hex/RGB for screen, CMYK or spot for print). Respect the role each colour has (primary, accent, background) and the rough proportions the guide shows. Accessible contrast still applies (UI-6).
- **Why:** Distinctive colour is one of the strongest brand assets, and near-misses weaken it [S120]. A brand accent used as body-text colour often fails contrast.
- **Check:** Sample the colours in the render and compare to the sheet (ΔE under about 3 is a match by eye). Is any off-brand colour present? Does any brand colour pair fail 4.5:1 for text?
- **Fix:** Replace near-misses with exact values. Where a brand pair fails contrast, use the brand's darker or lighter step, or move the colour to a non-text role. Never ship a contrast failure to match a guide; flag the conflict to the owner.
- **Source:** Romaniuk [S120]; Wheeler [S119]; UI-6.

### BRAND-3. Type follows the guide, set well
- **What:** Use the brand's families for their stated roles. If a family isn't available (web licence, platform), use the guide's named fallback, or the closest match by category, x-height and width, and say so.
- **Why:** Type is a distinctive asset like colour. A silent substitution looks off-brand to anyone who knows it.
- **Check:** Compare computed font families to the sheet. Any substitution not listed as a fallback?
- **Fix:** Load the brand fonts, or document the fallback in the hand-off. Then apply the typography module (TYPE-2 to TYPE-6).
- **Source:** Wheeler [S119]; TYPE-1.

### BRAND-4. Official marks: the real file, unaltered, at good quality (MUST-BE-RIGHT)
- **What:** This covers any official mark in the work: the client's own logo, and also sports teams, sponsors, crests, partner and product logos. The default is to **include the official mark**, at better quality rather than worse, from an official file. Use the first of these that exists:
  1. the file the owner supplies;
  2. the brand's own site, press kit or brand centre;
  3. Wikimedia Commons, checked against the official source for shape and colour.

  Prefer a vector or the largest raster. Use it unaltered: official proportions and colours, the version the guide gives for the background, its clear space (often a unit of the logo, such as the cap height or a symbol width) and its minimum size. Never redraw, trace, retype, restyle, recolour, stretch, rotate, add effects to, or AI-generate a mark, not even to "clean it up" or to match the piece's style. A labelled placeholder (a plain box reading "[Team] crest: official file needed") is the last resort, used only when no faithful source exists. Say so in the hand-off.
- **Why:** A logo is a trademark. It identifies who the goods or services come from [S170]. In UK law, using a sign identical with or similar to a registered mark, in the course of trade and in a way likely to confuse, infringes it [S171]. Brand guides are explicit. Spotify says its logo is not to be modified or added to, and its orientation, colour and composition are not to change [S172]. Mastercard says its artwork is to be downloaded and not altered, and its Symbol is used only in full colour [S173]. A file on Commons carries no permission to use the trademark; that stays with the owner of the mark [S174]. Image generators routinely garble marks. A near-miss mark is worse than none, because it looks like a fake.
- **Check:**
  - The logo's width-to-height ratio matches the source file within 1%.
  - Colours are sampled against the guide (ΔE under about 3).
  - The gap to the nearest element is at least the clear-space unit.
  - Its width at display size is at or above the minimum.
  - Compared side by side with the source at 200%, it has the same letters and the same shapes.
  - The hand-off names the source of each mark (owner, brand site, or Commons with its file page).
  - For third-party marks, a line notes that permission to use them is the owner's call.
- **Fix:**
  - Place the original file.
  - Restore clear space by moving other elements, not by shrinking the logo below its minimum.
  - On dark or busy grounds, use the guide's one-colour or reversed version.
  - If you can't find a faithful source, use the labelled placeholder and ask the owner for the file.
- **Source:** Wheeler [S119]; USPTO [S170]; Trade Marks Act 1994 s.10 [S171]; Spotify [S172]; Mastercard [S173]; Wikimedia Commons [S174].

### BRAND-5. Voice matches, in words and in pictures
- **What:** Headlines, labels and microcopy follow the brand's voice (the guide's words, or the three from intake). Tone may shift with context (error message vs launch post); voice stays the same.
- **Why:** Tone of voice measurably changes how people judge a brand's friendliness, trustworthiness and desirability [S121]. Generic AI copy ("seamless", "elevate", "unlock") has no voice.
- **Check:** Place each piece of copy on NN/g's four scales: funny-serious, formal-casual, respectful-irreverent, enthusiastic-matter-of-fact. Does it land where the guide says? Count generic filler words.
- **Fix:** Rewrite to the voice; cut filler; never invent facts, claims or quotes (CD-1). Copy changes beyond fixing errors are suggestions for the owner.
- **Source:** Moran, NN/g [S121]; Mailchimp Content Style Guide, voice and tone [S122].

### BRAND-6. Consistent across pieces
- **What:** Pieces in one set (a site and its social cards, a deck, a campaign) share the same tokens: colours, type, logo placement, image treatment, corner radius.
- **Why:** Distinctive assets only build memory when repeated consistently [S120]. Each piece "being a bit different" erodes them.
- **Check:** Put the pieces side by side as thumbnails. Same palette, type, logo position and image style? List any token that differs and why.
- **Fix:** Pull every piece from one token sheet; vary layout and content, not the assets.
- **Source:** Romaniuk [S120]; Wheeler [S119].

### BRAND-7. No brand? Make the defaults visible and owned
- **What:** When intake gets no answers, use the assumed token sheet from `core/brand-intake.md`, build from the subject (its materials, place, audience), and label every assumed choice.
- **Why:** Hidden defaults produce the generic look (UI-7, ILL-11, TYPE-9). Labelled assumptions turn it into a question the owner can answer.
- **Check:** Does the hand-off list the assumed colours, type and voice? Can each be traced to the subject rather than to a tool's default?
- **Fix:** Add the "assumed" sheet and a question for the owner. Don't run extra rounds to fix "generic"; ask.
- **Source:** CD-1, CD-2; web-ui-landing log.

### BRAND-8. No invented marks in generated imagery (MUST-BE-RIGHT)
- **What:** Generated or edited images often put pseudo-logos, fake wordmarks and garbled lettering on things that would carry a brand in real life. Look at jerseys and kits, bottles and cans, packaging, signage and shopfronts, vehicles, screens, pitch boards and caps. Each mark must be one of two things: the official one, placed from the file per BRAND-4, or none at all.
- **Why:** An invented mark reads as a fake, or as an existing brand the owner did not choose. A mark similar to a real one can raise the same confusion problem as copying it [S171]. Generators don't know which brands the brief allows.
- **Check:**
  - Crop every surface where a mark could appear at 2x-4x, and write one line per crop: none, official (with its source) or invented.
  - Read any lettering. Gibberish text that looks like a logo counts as invented.
  - Re-check after every regenerate or edit.
- **Fix:**
  - Regenerate with the surfaces described as plain ("plain white jersey, no logos or text; unlabelled bottle").
  - Or paint the mark out to the plain surface.
  - Then, if the brief calls for a real mark, composite the official file in afterwards (BRAND-4), following the surface's perspective without distorting the mark's proportions beyond what the surface's own perspective causes.
  - Never ask a generator to draw a real logo.
- **Source:** BRAND-4; Trade Marks Act 1994 s.10 [S171]; ILL-11.

---

## Myths

- **"A brand is its logo."** Logos are one asset among several. Colour, type, shapes and characters can be more distinctive than the mark itself [S120].
- **"Consistency is boring; refresh it often."** People who aren't the brand team notice assets far less than the team does. Frequent changes waste the memory they've built [S120].
- **"Colour X means trust / energy."** See `core/evidence.md`: colour-emotion claims are weak. Choose brand colours for distinctiveness and contrast, not psychology.

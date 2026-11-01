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

### BRAND-4. Logo: clear space, minimum size, unaltered (MUST-BE-RIGHT)
- **What:** Use the supplied logo file, never redrawn or regenerated. Keep its clear space (often defined as a unit of the logo, such as the cap height or a symbol width) and its minimum size. Don't stretch, recolour, rotate, add effects or set it on a busy background unless the guide allows that version.
- **Why:** The logo is the brand's legal and visual signature; altered logos are the most visible brand error, and image generators routinely garble them.
- **Check:** Measure the logo's width-to-height ratio against the file (within 1%). Measure the gap to the nearest element against the clear-space unit. Measure its width at display size against the minimum. Compare it side by side with the source file at 200%: same letters, same shapes?
- **Fix:** Place the original vector file; restore clear space by moving other elements, not by shrinking the logo below minimum; use the guide's one-colour or reversed version on dark or busy grounds.
- **Source:** Wheeler [S119].

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

---

## Myths

- **"A brand is its logo."** Logos are one asset among several. Colour, type, shapes and characters can be more distinctive than the mark itself [S120].
- **"Consistency is boring; refresh it often."** People who aren't the brand team notice assets far less than the team does. Frequent changes waste the memory they've built [S120].
- **"Colour X means trust / energy."** See `core/evidence.md`: colour-emotion claims are weak. Choose brand colours for distinctiveness and contrast, not psychology.

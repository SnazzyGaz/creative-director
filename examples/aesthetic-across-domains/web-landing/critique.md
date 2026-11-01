## Critique: Marrow Street Pottery landing page, round 1 (the before)

**Brief:** a one-page site for a small pottery studio in Sheffield (Marrow Street Pottery is a made-up name for this example). Goal: fill a six-week beginners' wheel course. Facts given: starts 12 January; Tuesday or Thursday, 18:30 to 21:00; £195 including clay and firing; six places a class, one wheel each; course covers wedging and centring, throwing cylinders and bowls, trimming and handles, glazing; pots ready two weeks after; aprons provided; address 14 Marrow Street, Sheffield; pots on sale Saturdays 10:00 to 16:00. Done when a visitor can decide and book from the first screen on a phone and on a laptop.
**Intent (AES-0):** purpose: sell six places a class [brief] / audience: adults who have never thrown a pot [brief] / mood: calm, hands-on, small and real [inferred from "small studio"] / style: crafted, photographic, not a tech start-up [inferred] / focal experience: "I could do that, on a Tuesday, for £195" [inferred] / polish: live site [brief] / must-keeps: the facts above and a booking button [brief].
**Criteria judged against:** CORE-1, CORE-3, CD-1, CD-6, UI-1, UI-4, UI-6, UI-7, UI-10, UX-1, TYPE-9, TYPE-10, AES-2, AES-6, AES-7, AES-10.
**Evidence looked at:** `before-1280.png`, `before-390.png`, `before-zoom200.png` (headless Chrome), `look-before.jpg`, colours from `src/before.html`.

### Brief check (CD-1, CD-5)
- Answers the brief: no. Not one of the course facts (date, days, time, price, class size, what is covered) appears anywhere on the page; only the address does, in the footer.
- Content not in the brief: three testimonials with names and five stars, "Join 10,000+ Happy Potters", "Expert Instructors", "glazes and tools included", "Spaces fill up fast". None of it was supplied.

### Test results
- Blur: the gradient band leads (grid 1.4 top-centre); after that the eye has nothing to land on; the button is a small white pill.
- Thumbnail: purple block, three cards, three cards. Could be any product.
- 5-second test: "it's some kind of creative class"; what, when, and how much are unknown.
- 200% zoom (UI-10): the first screen is headline and intro only; the button is the last thing visible.

### Anatomy pass (CHAR-9, CHAR-10)
- No figures in either version (the 👩‍🎨 emoji in the before is a font glyph). Not applicable.

### Meets criteria
- UI-10: text reflows at 390 px and at 200% without clipping.
- Nav links and button are real links with a visible focus ring from the browser.

### Findings: MEASURED
- CD-1, AES-10 (MUST-BE-RIGHT): invented reviews, names, ratings and a "10,000+" customer figure on a real business's page. **Blocker**: these are claims the studio did not make. (UK consumer law bans fake consumer reviews outright under the Digital Markets, Competition and Consumers Act 2024 [S161]; reason enough not to ship invented ones.)
- UX-1, CD-6: 0 of 6 booking facts on the page. **Blocker** for a page whose job is booking.
- UI-6 (MUST-BE-RIGHT): section subtitles, card text, nav links and footer in #9ca3af on white = **2.54:1** (needs 4.5:1). The hero paragraph (white at 85% on the pink end, #ec4899) = **2.75:1**. White button label on the pink end of the last button = 3.53:1, under 4.5:1 for 16 px text. **Blocker.**
- TYPE-9: Inter for everything, all centred; listed as a generic tell.
- UI-7, AES-6 generic tells counted: purple-to-pink gradient, sparkle emoji, emoji feature cards, "Unleash your inner…", "Why Choose Us?", five-star review row. Six of the common set.

### Findings: INTERPRETED
- AES-6: feature: the stock SaaS layout. Effect: swap "clay" for "coding" and the page still works; nothing says pottery, Sheffield or small. Trade-off: the template is familiar and quick to scan. Confidence: high.
- AES-2: feature: equal-weight sections of cards. Effect: no section is more important than another, so the booking decision has no home. Confidence: high.
- AES-7: feature: "Cosy Vibes", "magic of clay". Effect: tells a mood instead of showing the room and the pots. Trade-off: a photo needs the studio to supply or approve one. Confidence: medium.

### Needs improvement (ranked)
1. [BLOCKER] CD-1, AES-10. Remove the invented reviews, the 10,000+ figure, "Expert Instructors", "glazes and tools" and "Spaces fill up fast". Use only the brief's words.
2. [BLOCKER] UX-1, CD-6, UI-4. Put the four deciding facts (start date, days and time, price, class size) and the Book button together in the first screen at 1280 and 390, and at 200%.
3. [BLOCKER] UI-6. All text at 4.5:1 or better (large text 3:1), including text over any image, checked against the worst pixel behind it.
4. [IMPROVEMENT] UI-7, AES-6, AES-7, CORE-3. Replace the gradient and emoji with a photograph of pots on a studio shelf (plain wall left for the headline); one accent colour taken from the photo for the button.
5. [IMPROVEMENT] TYPE-9, TYPE-10, UI-1. Bricolage Grotesque for headings and facts (characterful grotesk, catalogued for modern brands), Literata for reading text (catalogued pairing); left-aligned, one column of reading width.

### Comparison (AES-9), after the fixes
- Stronger for this brief: after. Strongest difference: what, when, how much and "Book" are readable in the first screen. Caused by: the course strip and real copy. Cost: no social proof at all until the studio supplies real reviews; the page is shorter and plainer; it now depends on one photograph (generated here, so the studio must swap in its own). Preference: strong; held with sides swapped.
- Additions: the hero photograph (stands in for the studio's own photo; labelled as generated in the README). Headline "Learn to throw pots in six evenings" restates the brief's course; course content list, aprons and collection time are from the brief. Nothing else.

### Questions for the owner
- Can the studio send a photo of its own shelf and wheels? The generated one is a placeholder.
- Are there real reviews (with permission) to add later?

### Sign-off blurb (as sent before any change)
Imperative changes (sign off and I'll apply all of them):
1. [edit] CD-1, AES-10: reviews, names and "10,000+" are invented. Remove them and every other claim not in the brief.
2. [rebuild] UX-1: none of date, time, price or class size appear. Put all four next to the Book button in the first screen.
3. [edit] UI-6: grey text at 2.54:1, hero text at 2.75:1. Bring all text to 4.5:1 or better.
4. [rebuild] UI-7, AES-6: gradient, emoji and "Unleash" read as a template. Use a photo of pots on a shelf and one accent from it.
5. [edit] TYPE-9: Inter, centred. Bricolage Grotesque headings, Literata text, left-aligned.
Also possible (not needed): a short gallery of student pots. OK to go ahead with 1-5?

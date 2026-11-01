## Critique: Riverside Buses ticket flow, round 1 (the before)

**Brief:** three phone screens (390 x 844) for buying a bus ticket in the app of a city bus company (Riverside Buses is made up for this example): choose, pay, show the ticket. Facts: Adult or Child; Single £2.00 (one journey), Day £4.50 (any bus until 23:59 today), Week £18.00 (any bus for 7 days); child fares are half; saved card Visa ending 4242; tickets start when paid and cannot be refunded once started; the live ticket has a moving band so drivers can spot screenshots, plus a code for the reader. Done when a rider can buy in under 30 seconds at a bus stop, in daylight, one-handed, and a driver can read the ticket type and expiry at arm's length.
**Intent (AES-0):** purpose: buy fast and board [brief] / audience: everyone who rides a bus, including older and low-vision riders [inferred: public service] / mood: calm, certain [inferred] / style: plain public-service UI [inferred] / focal experience: "that's my ticket, it's valid, get on" [inferred] / polish: production screens [brief] / must-keeps: the facts above [brief].
**Criteria judged against:** CORE-1, CD-1, UI-2, UI-5, UI-6, UI-7, UI-9, UX-1, UX-2, UX-5, UX-7, UX-9, TYPE-3, TYPE-10, AES-2, AES-3, AES-6.
**Evidence looked at:** `before.png` (three screens, headless Chrome at 2x), `look-before.jpg`, CSS in `src/before.html`.

### Brief check (CD-1, CD-5)
- Answers the brief: partly. All three steps exist and the fares are right.
- Content not in the brief: a promo-code field, a "Service fee £0.00" line, "Add new card" and Apple Pay options, "Terms of Service and Privacy Policy" text. The service-fee line invents a cost category.
- Missing: the date on the ticket (a Day ticket from yesterday looks identical), the moving band, "show this to the driver".

### Test results
- Blur: on screens 1 and 2 only the gradient buttons survive; the fares and the selected option vanish. Screen 3: the QR code leads, not the ticket type or expiry.
- Squint (daylight stand-in): grey-on-white descriptions and the violet prices disappear first.
- Arm's length: "Adult Day" is 22 px Light and "Valid until 23:59" is 12 px Light white on teal; the driver has to lean in.

### Anatomy pass (CHAR-9, CHAR-10)
- No figures. Not applicable.

### Meets criteria
- UX-1: three steps, no account wall; the flow can be completed.
- UI-9: one primary action per screen.

### Findings: MEASURED
- UI-6 (MUST-BE-RIGHT): descriptions #c4c4cc on white **1.73:1**; prices #a78bfa **2.72:1**; status bar and labels #a1a1aa 2.56:1; terms #d4d4d8 1.48:1 at 10 px; button label white on the teal end **1.86:1**; on the ticket, "Valid until" (white at 80% on teal) **1.62:1**. **Blocker.**
- UX-9, UI-5, WCAG 2.5.8: Adult/Child toggle about 25 px tall; back chevron an 18 px glyph with no padding; payment radios 14 px on 36 px rows. All are under the UI-5 target of 44-48 px, and the chevron and radios also fail the WCAG 2.5.8 minimum of 24 x 24 px [S160]. **Blocker** for one-handed use at a stop.
- CD-1 (MUST-BE-RIGHT): "Service fee £0.00" and a promo-code field are not in the brief; the fee line suggests charges that do not exist. **Blocker.**
- UX-1, CD-1: the ticket shows no date; the brief's moving band is missing. A driver cannot tell today's Day ticket from a screenshot of an old one. **Blocker.**
- UX-2, UX-7: the price is not on either button ("Continue", "Pay now"); the rider confirms an amount they cannot see at the moment of tapping.
- TYPE-3: smallest text 10 px (terms) and 11-12 px (descriptions, ticket meta), all at weight 300.

### Findings: INTERPRETED
- UI-7, AES-6: feature: teal-to-violet gradients, Outfit Light, pill shapes. Effect: reads as a lifestyle app, not a bus company; looks unofficial at the moment a driver judges it. Trade-off: the softer look is friendlier at first glance. Confidence: medium.
- AES-2: feature: everything is light and grey, so the selected ticket, the price and the button are all the same weight. Effect: the eye cannot find "what am I buying for how much". Confidence: high.
- AES-3: feature: a two-colour gradient that also marks selection. Effect: colour carries both brand and state, so state is weak. Confidence: medium.

### Needs improvement (ranked)
1. [BLOCKER] UI-6, TYPE-3. All text 4.5:1 or better, nothing under 15 px, reading weights 400-700; button labels on a solid colour.
2. [BLOCKER] UX-9, UI-5. Every tap target at least 48 x 48 px: toggle, ticket rows (whole row), back, change card, done.
3. [BLOCKER] CD-1. Remove the service-fee line, promo field and extra payment options; show the saved card with "Change".
4. [BLOCKER] UX-1, CORE-1. Ticket screen built for the driver: ticket type at 44 px, "Valid until 23:59 today, Sun 1 Nov" at 30 px, the moving band, "Show this screen to the driver"; the code smaller but kept for the reader.
5. [IMPROVEMENT] UX-2, UX-7, AES-2, AES-3. Price on both buttons ("Next: pay £4.50", "Pay £4.50"), "Step 1 of 2" labels; one solid green for action and selection, ink for everything else.
Text type: [edit] TYPE-10, Atkinson Hyperlegible Next (catalogued as accessibility-first: letter shapes that cannot be confused; its slashed zero keeps 0 and O apart on fares and ticket numbers).

### Comparison (AES-9), after the fixes
- Stronger for this brief: after. Strongest difference: the ticket screen can be read by a driver from arm's length, and every price is visible at the moment of tapping. Caused by: contrast, type size and the driver-first ticket layout. Cost: plainer and more "official"; the QR code is smaller (150 px against 210 px) so the reader needs it held closer; the screens hold less at once. Preference: strong; held with sides swapped.
- Additions: "Step 1 of 2", "Who is travelling?", "Which ticket?", "Show this screen to the driver" and the band caption are labels for existing content and the brief's band, not new content. Nothing else added.

### Questions for the owner
- Does the reader at the door need the larger code? If so, a "Scan" button can enlarge it on tap.
- Are Apple Pay and adding a card in scope? They were removed as not in the brief.

### Sign-off blurb (as sent before any change)
Imperative changes (sign off and I'll apply all of them):
1. [edit] UI-6, TYPE-3: pale text at 1.5-2.7:1 and 10-12 px. All text 4.5:1 or better, 15 px minimum, solid button colour.
2. [edit] UX-9: toggle 25 px, back 18 px. Every target 48 px or more.
3. [edit] CD-1: a fee line and promo field not in the brief. Remove them.
4. [rebuild] UX-1: ticket has no date or moving band. Type 44 px, expiry and date 30 px, band, "show the driver".
5. [edit] UX-2, AES-2: price missing from buttons, no visual lead. Put the price on both buttons; one green for action and selection.
Also possible (not needed): tap-to-enlarge code. OK to go ahead with 1-5?

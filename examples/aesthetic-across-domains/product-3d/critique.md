## Critique: perfume product shot, round 1 (the before)

**Brief:** a 4:5 (1080 x 1350) advert image for a perfume. Saltmarsh No. 2 is made up for this example. The bottle is a rectangular glass flacon, 60 x 32 x 85 mm, with a cap and a small front label. The copy given is "Saltmarsh No. 2", "Eau de parfum, 50 ml" and the notes "Sea air, vetiver, smoked cedar". It is done when the bottle reads as glass holding amber liquid, and the name, size and notes read on a phone screen.
**Intent (AES-0):** purpose: make the bottle look worth picking up [brief] / audience: people browsing on a phone [inferred] / mood: quiet, coastal, a little smoky [inferred from the notes] / style: studio product render [brief] / focal experience: the lit liquid inside clear glass [inferred] / polish: finished advert [brief] / must-keeps: the bottle model and the copy [brief].
**Criteria judged against:** CD-1, CORE-1, CORE-2, LAY-2, TYPE-1, TYPE-3, TYPE-9, TYPE-10, UI-6 (contrast maths applied to an image), 3D-1, 3D-3, 3D-4, 3D-5, 3D-6, 3D-7, AES-1, AES-2, AES-3, AES-10.
**Evidence looked at:** `render-before.png`, `before.jpg`, `look-before.jpg`, text boxes in `src/before-boxes.json`, the material and light values in `src/scene.py`, and a `model-qa check --no-render --brief` run on the saved round-1 scene.

### Brief check (CD-1, CD-5)
- Answers the brief: partly. The name and notes are there, but the bottle reads as an empty box with a yellow block in it.
- Content not in the brief: "LUXURY" and "The scent of the sea, captured forever." Both are claims the maker did not make.

### Test results
- Blur: the grid peaks at 1.0 on the bottle row and is 0.1 everywhere else; the type disappears.
- Greyscale: L* p50 74.5; 32% of pixels are in the top L* bin. Glass, ground and type are all light grey or white.
- Squint: a pale rectangle on a pale ground. The gold cap is the only shape that holds.

### Anatomy pass (CHAR-9, CHAR-10)
- Product only; no figures. Not applicable.

### Meets criteria
- 3D-2: real-world size in metres, Z up, standing on the floor.
- 3D-4: bevelled edges and a smoothed cap.

### Findings: MEASURED
- 3D-1 (MUST-BE-RIGHT): model-qa reports high issues on the bottle itself. The glass base block goes 2.0 mm through the glass floor. The label plate floats 0.1 mm off the glass and the text floats 0.3 mm off the label. The text mesh has 2 zero-area faces and a loose vertex. **Blocker**: overlapping glass volumes refract wrongly, and the label is not attached.
- 3D-7: Standard view transform; **29.3%** of pixels are clipped to pure white (all three channels 254 or above). The whole floor and the lower glass are one flat white patch.
- UI-6 maths on an image (TYPE-3): text against the render behind each line, mean: title 2.05:1, "LUXURY EAU DE PARFUM" **1.13:1**, tagline **1.19:1**, notes 2.23:1. The small lines need 4.5:1. **Blocker.**
- 3D-5, CORE-2: one 9 W area light from the camera side and a grey world at 0.35. The cap is brightest in the middle third (L 228, against 135 and 133 at the sides), so the light comes from straight in front and gives no form. The background (sRGB about 180-200) is the same value as the glass.
- CD-1, AES-10 (MUST-BE-RIGHT): two lines not in the brief ("LUXURY", the "captured forever" tagline). **Blocker.**
- LAY-2: 50 mm lens at eye level with the bottle dead centre. It fills 27% of the frame height, and the type sits in the two places where the ground is lightest.

### Findings: INTERPRETED
- AES-3, 3D-4: feature: clear glass in front of a light grey ground. Effect: glass only shows where it reflects or bends something with a different value; here there is nothing to bend, so the bottle has no edges. Confidence: high.
- TYPE-9, AES-1: feature: a Great Vibes script title, a gold Playfair kicker and a gold cap. Effect: the common "luxury" template; nothing in it says salt marsh or smoke. Confidence: medium.
- AES-2: feature: no dark anywhere. Effect: "smoked cedar" has no visual counterpart; the mood reads as a clean bathroom shelf. Confidence: medium.

### Needs improvement (ranked)
1. [BLOCKER] 3D-1. Seat the base block on the inside of the glass floor (z 4-14 mm); start the liquid on top of it; put the label flush on the glass and the text flush on the label; weld the text mesh and remove its loose vertex.
2. [BLOCKER] CD-1, AES-10. Use only the brief's words. Remove "LUXURY" and the tagline.
3. [BLOCKER] UI-6, TYPE-3. Put all type on a dark, even part of the frame, in warm off-white, 4.5:1 or better.
4. [IMPROVEMENT] 3D-5, 3D-7, CORE-2, AES-3. A black ground and world. Two narrow strip lights behind and to each side, so the glass edges draw as bright lines. A small key from the upper left and a little fill. A hidden warm card behind the bottle that lights the liquid through the glass. Switch to AgX.
5. [IMPROVEMENT] LAY-2, 3D-5. An 85 mm lens slightly above the label. Shift the bottle into the lower half and leave the dark top for the type. Use a glossy black floor for a reflection.
6. [IMPROVEMENT] TYPE-9, AES-1. One accent, amber taken from the liquid, and a black cap, so the gold is gone.
Text type: [edit] TYPE-10. Bodoni Moda for the name: a high-contrast didone with an optical-size axis, catalogued for luxury and fragrance; its hairlines match the rim lines on the glass. Josefin Sans 500 in tracked capitals for the small lines: a geometric face catalogued for art deco and fashion labels, and it is already the face on the bottle's own label.

### Comparison (AES-9), after the fixes
- Stronger for this brief: after. Strongest difference: the bottle now reads as glass holding amber liquid. Caused by the dark ground plus the rim strips, which draw its edges, and the hidden glow card, which lights the liquid. Costs:
  - The image is much darker, so it may sit heavily in a feed.
  - The black coated cap reflects the strips and reads closer to polished steel than black.
  - The liquid is a fairly even amber block rather than glowing at the base.
  - The layout is centred; that is deliberate here because the bottle is symmetrical, but it is the safe choice.
  Preference: strong; held with sides swapped.
- Additions: none. "50 ML" and the notes are the brief's words set in capitals; the glow card is lighting, not content.

### Questions for the owner
- Should the cap be black (as briefed here), brushed steel, or matched to a real cap sample?

### Sign-off blurb (as sent before any change)
Imperative changes (sign off and I'll apply all of them):
1. [edit] 3D-1: base block 2 mm through the glass floor; label and text floating. Seat them and weld the text.
2. [edit] CD-1, AES-10: "LUXURY" and the tagline are not in the brief. Remove them.
3. [relayout] UI-6, TYPE-3: small type at 1.1-2.2:1 on white. Move all type onto a dark area at 4.5:1 or better.
4. [relight] 3D-5, 3D-7, CORE-2: flat front light, 29% clipped white. Black ground, two rim strips, small upper-left key, hidden warm card, AgX.
5. [reframe] LAY-2: 50 mm at eye level, centred. 85 mm, bottle in the lower half, glossy floor.
6. [edit] TYPE-9, AES-1: script and gold. Bodoni Moda + Josefin Sans, one amber accent, black cap.
Also possible (not needed): a lighter variant for feeds where a dark tile would jump out. OK to go ahead with 1-6?

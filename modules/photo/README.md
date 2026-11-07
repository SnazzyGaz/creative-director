# Module: photo (photographs and photoreal images)

Direction for anything that should look like a photograph, shot with a camera or made by an image model: where the camera stands, what the light is, who is in it, what surrounds them, how far retouching may go, and the tells that give a generated photo away. Load with `core/`; add `character/` for any person, hand or animal (the CHAR-9 anatomy pass still gates delivery) and `illustration/` for focus, staging and camera story (ILL-14 to ILL-16). For food, ILL-12 applies.

Write the photo brief before the prompt or the shoot: one line each for distance and lens, camera height, light (source, size, direction, colour), casting, wardrobe and props, set, and the finish (how much retouching). A prompt that names these gets a photograph; one that names only the subject gets the model's default.

Format: **What / Why / Check / Fix / Grade / Source**. No rule here is a blocker on its own; the blockers that apply stay in `critique-loop.md`.

---

### PHOTO-1. Choose the camera distance first; the lens follows
- **What:** Decide how far the camera is from the subject, then pick the focal length that frames it from there. Perspective comes from distance, not from the lens. For faces, keep the camera outside arm's length (about 1.5 m or more) unless the warping is the point; a close, wide view swells the nose and shrinks the ears.
- **Why:** A model of short-distance photographs found that at about 30 cm the nose reads roughly 30% wider than in a true-proportion view, while at about 1.5 m the difference all but disappears [SRC-413]. In experiments, faces photographed from inside personal space were rated less trustworthy, competent and attractive than the same faces photographed from further away, with size, lighting and expression controlled [SRC-414].
- **Check:** Look at the face: is the nose large against the ears and face width, and does the background look stretched and far away? Then the camera was close. Does that suit the brief (intimate, comic, urgent) or is it an accident?
- **Fix:** Step back and frame tighter: in a prompt, name the distance and the lens ("from about 2 m, 85 mm, head and shoulders"). For a wide, close look, say so on purpose.
- **Grade:** Well supported for the geometry; partly supported for the effect on judgements (one lab group, replicated across its own studies).
- **Source:** Ward et al. [SRC-413]; Bryan, Perona and Adolphs [SRC-414].

### PHOTO-2. Camera height has a job
- **What:** Eye level is the neutral default. Go low only when the subject should loom (strength, scale, triumph) and high only when it should look small, mapped or seen from above. Product and food shots pick the height where the product's identifying face reads (a can from the side, a pizza from above, a burger at its own height).
- **Why:** In a study of ads, low-angle shots made products look better to viewers who were paying little attention, while eye level did best for viewers paying more; with close attention the angle mattered little [SRC-415]. So angle shifts impressions, but not by a fixed rule.
- **Check:** Where is the horizon or eye line? Can you name why the camera is at that height? Does the product show the side that identifies it?
- **Fix:** Name the height in the brief ("camera at chest height looking slightly up"). If no reason comes, go back to eye level.
- **Grade:** Partly supported (the effect depends on the viewer); the product-face point is craft.
- **Source:** Meyers-Levy and Peracchio [SRC-415]; ILL-16.

### PHOTO-3. Name the light: source, size, direction, colour
- **What:** Every photo brief names its key light: what it is (window, sun, softbox, street lamp), how big it looks from the subject, where it comes from, and its colour; then the fill and the background. A large source close to the subject makes soft light with gradual shadow edges; a small or distant one makes hard light with crisp shadows. Brightness falls off fast with distance, so a light close to the subject darkens the background more.
- **Why:** Source size and distance set the softness of shadows and highlights, and falloff sets how the background separates [SRC-416]. A generated photo with no named light tends to get the model's even, glowing default (ILL-11).
- **Check:** Find the key: which way do the shadows point, are their edges hard or soft, and does every shadow, highlight and reflection agree (TD-LIT-1, CV-7)? Is there a rim or glow with no source in the scene?
- **Fix:** Write the light as a setup ("a large window to camera left, overcast, no fill, dark room behind"). Remove sourceless rims. Match the background brightness to the falloff.
- **Grade:** Well supported (optics of source size and falloff); the choice of setup is craft.
- **Source:** Hunter, Biver, Fuqua and Reid, *Light: Science and Magic* [SRC-416]; TD-LIT-1; CV-7.

### PHOTO-4. Cast specific people, not average ones
- **What:** Write who each person is: age, build, skin, hair, how their clothes are worn, what they do and how they stand. Cast for the role and the audience. Avoid the model's default face (young, symmetrical, smooth-skinned, posed) unless the brief asks for it. Where real people can be shown (the team, the customers), prefer them to stand-ins.
- **Why:** Eye-tracking found that people study photos of real people and products that carry information, but skip generic stock people used as decoration [SRC-418]. Generated faces drift towards the average, which is part of why they are rated as trustworthy and hard to tell from real ones [SRC-417]; average is also what makes a picture forgettable.
- **Check:** Could you describe each person in a line that isn't "a smiling young professional"? Do the people fit the place, the job and the audience? Do two people share one face?
- **Fix:** Rewrite the casting line with concrete traits and wear (creased linen, a chipped nail, reading glasses pushed up). Give each person a different age or build where the brief allows.
- **Grade:** Partly supported (eye-tracking for real versus generic people); casting detail itself is craft.
- **Source:** NN/g, *Photos as Web Content* [SRC-418]; Nightingale and Farid [SRC-417].

### PHOTO-5. Styling, props and set belong to one story
- **What:** Every object in frame belongs to this person, place and time, and shows signs of use: a mug with a ring under it, a worn handle, a crumpled receipt. Nothing is added that the brief didn't give (AES-10), and nothing that couldn't work (a strap that goes nowhere, a chair with three legs at the back, a lamp with no cable).
- **Why:** Objects that couldn't function are one of the main families of tells in generated photos [SRC-419]; in a real shoot, props that don't belong make the picture read as staged.
- **Check:** List every prop. For each: who owns it, and could it work as drawn? Is any text on it real and from the brief (CD-7, BRAND-8)?
- **Fix:** Cut props that tell no story; give the kept ones wear; regenerate or edit any object that couldn't work.
- **Grade:** Craft wisdom, consistent with the generated-image research.
- **Source:** Kamali et al. [SRC-419]; AES-10; CD-7; BRAND-8.

### PHOTO-6. Retouch within the limits of the context
- **What:** Match the retouching to the context. News and documentary: tone and colour only, minimal, nothing added or removed [SRC-420]. Advertising: never change what the product is claimed to do (skin smoothed for a skin cream, lashes lengthened for a mascara) [SRC-421]. Everywhere: keep skin texture, pores and the shape of bodies unless the brief says otherwise. A photoreal generated image of a real person, place or event is labelled as generated, and provenance data (C2PA content credentials) is kept where the tools support it [SRC-422].
- **Why:** Press codes forbid adding or removing content from news photos [SRC-420]; UK advertising guidance treats retouching that exaggerates a product's effect as misleading [SRC-421]. Over-smoothed skin is also a tell of a generated or heavily edited image [SRC-419].
- **Check:** What is the context? List each edit and whether it changes content or a claim. Zoom on skin: is there texture? Is a generated photoreal image of something real labelled?
- **Fix:** Undo edits that change content or claims; bring back texture; add the label or credential. If the limit is unclear (a law, a platform rule), flag it to the owner rather than decide.
- **Grade:** Standard within news and UK advertising (published codes); craft elsewhere.
- **Source:** AP, *News Values and Principles* [SRC-420]; ASA and CAP, cosmetics production techniques [SRC-421]; C2PA [SRC-422]; Kamali et al. [SRC-419].

### PHOTO-7. Generated-photo pass: crop and look for the five kinds of tell
- **What:** Before delivering a generated photo, crop at 2-4x and check the five families of tell: anatomy (hands, teeth, ears, joints: CHAR-9), style (waxy or airbrushed skin, too-perfect light, everything equally sharp, a polished cinematic finish that still reads as generated rather than candid), function (objects, clothing and text that couldn't work), physics (shadows, reflections and perspective that disagree), and context (the wrong uniform, sign, season or custom for the place). Judge by those checks, not by whether the face "feels real".
- **Why:** A guide built from 138 generated and 42 real images sorts the usual tells into those five families, and notes that busy scenes with several people show more of them than a simple portrait [SRC-419]. People can't reliably spot generated faces by feel: in one study they did no better than chance, and training only helped a little [SRC-417].
- **Check:** One line per family, pass or fail, with the crop. Is the background sharp enough to check, or does blur hide it? Any fail in anatomy or food is already a blocker (CHAR-9, ILL-12).
- **Fix:** Inpaint the failing region with the detail spelled out; regenerate if more than one family fails. Simplify the scene (fewer people, fewer objects) if the tells keep coming.
- **Grade:** Partly supported (a descriptive guide and a detection study, not a test of this pass).
- **Source:** Kamali et al. [SRC-419]; Nightingale and Farid [SRC-417]; CHAR-9; ILL-12.

## Myths and weak claims
- **"85 mm is the portrait lens":** the flattering part is the distance it makes you stand at, not the lens itself [SRC-413]. Name the distance.
- **"A low angle always means power":** the effect depends on how closely the viewer is looking [SRC-415].
- **"If it looks real, it's fine":** generated faces pass the eye test while hands, objects and shadows fail it [SRC-417, SRC-419]. Run PHOTO-7.

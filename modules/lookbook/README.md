# Module: lookbook (optional)

A visual reference of looks: 246 established looks (historic, fine-art, technique-based, digital and contemporary figure styles: LB-001 to LB-234 and LB-SD01 to LB-SD17, in 10 families) and 74 wildcards (LB-R…), 320 in all, each with use, mood, energy, what to avoid it for, hallmarks by layer and a one-line hint. It is a source of directions, not rules. Every core rule and module still applies, and wins over a look whenever they disagree.

- `looks.json` (and `looks.csv`): the tag file, one row per live look, plus the `retired` IDs. Search it; don't load it whole.
- `sheets/`: 81 sheets, named by family, six looks to a sheet, each with its caption. `index.png`: every ID and name on one page. The sheets in git are 1,000 px wide; full-size ones are in `creative-director-lookbook-full.zip` on the [assets-v1 release](https://github.com/SnazzyGaz/creative-director/releases/tag/assets-v1) (`python3 tools/fetch_assets.py --lookbook`). Each look's full text is also in `looks.json`.
- Every example image is our own render from that look's written rules (captions say "our render from LB-xxx rules"). No look is tied to a real artist, studio, community or specific work, and none should be when you cite it: name looks by technique, structure or broad historic era only.

## When to reach for it
1. **From-scratch briefs** (`core/creative-direction.md`, `core/first-principles.md`). Offer two or three directions as thumbnails, each with its LB ID, before building. At most one in three concepts comes from the lookbook; the rest start from the brief alone.
2. **Rescue.** The work passes every check but feels generic (AES-1 to AES-8). Borrow **one layer** of one look at hint strength: a palette, a mark style, a type habit. It is a way out of the default, not a new style.
3. **Shared words.** Someone describes a vibe ("rough, protest-y"). Point to the nearest look so both sides picture the same thing, then confirm.

**Never on fixes or edits to existing work.** That work keeps its own look.

## Strength dial
Five layers: palette, type, mark-making, composition, subject (the `hallmarks` fields). Strength is how many layers you take and how literally.

| Strength | Take |
|---|---|
| Hint, ~20% | the look's `hint` line only; everything else comes from the brief |
| Leaning, ~50% | two or three layers |
| Strong, ~80% | all layers, adapted to the brief's subject and type |
| Full, 100% | the look as shown; only on request |

Default range: hint to leaning (LOOK-1). Strong only on purpose (LOOK-2); full only on request.

### LOOK-1. Default to 20-50%, random pulls included
- **What:** Use a look at hint to leaning (~20-50%). Pick hint for a rescue (one layer) and leaning when the look is the direction. This holds for looks drawn at random too: no random pull goes past leaning without a LOOK-2 reason.
- **Why:** Showcase 3, 21 briefs, each a base render beside one look at 20, 50 and 80%: 20-50% was best on 15 (50% on 14, 20% on 1), 80% on 5, the base on 1. The owner of the work also judged 20-50% the sweet spot (`examples/lookbook-strength/`).
- **Whites:** a look whose palette names cream, ivory or off-white keeps it only when the medium needs it (paper stock, newsprint, an aged print, a printed card in frame). Otherwise the whites stay neutral, as elsewhere in the rules; the look's character comes from its hallmarks, not a warm cast.
- **Grade:** Craft wisdom. Internal evidence: owner-judged, small sample (one render per level), not blind.

### LOOK-2. Strong (~80%) only on purpose, after a creep check
- **What:** Go to strong only when the look's own structure carries the brief's idea (a poster's red block used as a redaction bar on a true-crime cover; a game-box lid for a reading challenge), or when the owner asks.
- **Check:** Put it beside the 50% render. Subject creep: has the look's own subject replaced the brief's (a shuttle for the skater, a marble head for the eye, icon figures on a choir ticket)? It did in 9 of 15 random pulls. Prop stripping: have the brief's props and twists gone (the suitcase, the quill, the lightning)? Either one: go back to leaning.
- **Grade:** Craft wisdom. Same internal evidence as LOOK-1.

### LOOK-3. Keep an invented person's skin tone and identity
- **What:** With any portrait or figure look, the person keeps the skin tone, age, features and identity the brief gives or the base render set. The look's palette goes on clothes, ground, shadow and hair; never flatten skin into the look's paper or tint tones.
- **Why:** SD15 at 80% lightened an invented older woman's skin and features into its paper tone (showcase 3).
- **Check:** Beside the base: same person, same apparent skin tone and age? If not, recolour or step down.
- **Grade:** Procedure (care rule); one observed case.

## Keep it from becoming a crutch
- **Rotation.** Keep a short log of looks used per owner or project (ID, date, strength). Skip any of the last few unless the brief demands that look.
- **Fit before novelty.** A look goes forward only if its `use` and `mood` match the brief and nothing in `avoid_for` applies. Being striking is not a reason.
- **Read status.** Don't lead with a look marked `read_status: partial`; its render misses some layers.
- **Out-there scale** (`out_there`, 1 to 5): 1 default, 2 familiar revival, 3 specialist, 4 deep cut, 5 far out. Match it to the client's appetite; 4 and 5 need the owner's yes.
- **Care flags.** Follow the `care` note where there is one (for example, borrow the form, not a political creed; keep a living observance's imagery out of merchandise), and LOOK-3 for every portrait or figure look.

## How to search
Filter, then open only the matching sheets:

```
python3 tools/lookbook_find.py --use poster --mood bold --avoid children --skip LB-014,LB-040 --max-out 3
```

It matches `use`/`theme`, `mood` and `energy`, drops looks whose `avoid_for` matches a subject, mood or use word, skips IDs from your log, and prints each look's sheet and panel. `--full` adds hallmarks, avoid-for, care, colours, neighbours and the Getty era term. Without Python, filter `looks.csv` the same way.

- **More like this:** `--like LB-010` lists that look's `nearest_looks` (the three most similar renders) and the looks that list it back.
- **By colour:** `--colour "#c5040f,#ed6322"` ranks looks by how close their dominant `colours` (3-5 hex values from the render) come to the given ones; combine with `--use`/`--mood`.
- **Era term:** established looks with a clear movement or period carry `getty_aat` (Getty AAT Styles and Periods ID and preferred term, [SRC-266](../../SOURCES.md), ODC-By). It is a pointer for further reading, not a claim that the look copies any work. Technique-named and generic looks are left blank on purpose.
- **Search quality:** `python3 modules/lookbook/tests/score_find.py` scores the search on 26 generic briefs (`tests/briefs.json`): recall@8 and avoid-for violations.

## Cite
`LB-014 Suprematism at ~20%`: ID, name, strength. Add the layers taken above hint (`LB-005 Russian Constructivism at ~50%: palette, composition`).

New batches are folded in with `tools/lookbook_sync.py` (see `UPDATING.md`). IDs are stable and retired IDs are never reused.

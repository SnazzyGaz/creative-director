# Module: lookbook (optional)

A visual reference of looks: 122 established looks (historic, technique-based and contemporary figure styles: LB-001 to LB-114 and LB-SD01 to LB-SD09) and 74 wildcards (LB-R…), each with use, mood, energy, what to avoid it for, hallmarks by layer and a one-line hint. It is a source of directions, not rules. Every core rule and module still applies, and wins over a look whenever they disagree.

- `looks.json` (and `looks.csv`): the tag file, one row per live look, plus the `retired` IDs. Search it; don't load it whole.
- `sheets/`: one image per family, six looks to a sheet, each with its caption. `index.png`: every ID and name on one page. The sheets in git are 1,000 px wide; full-size ones are in `creative-director-lookbook-full.zip` on the [assets-v1 release](https://github.com/SnazzyGaz/creative-director/releases/tag/assets-v1) (`python3 tools/fetch_assets.py --lookbook`). Each look's full text is also in `looks.json`.
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
| Hint, ~20% (default) | the look's `hint` line only; everything else comes from the brief |
| Leaning, ~50% | two or three layers |
| Strong, ~80% | all layers, adapted to the brief's subject and type |
| Full, 100% | the look as shown; only on request |

Start at hint and go stronger only when the owner asks.

## Keep it from becoming a crutch
- **Rotation.** Keep a short log of looks used per owner or project (ID, date, strength). Skip any of the last few unless the brief demands that look.
- **Fit before novelty.** A look goes forward only if its `use` and `mood` match the brief and nothing in `avoid_for` applies. Being striking is not a reason.
- **Read status.** Don't lead with a look marked `read_status: partial`; its render misses some layers.
- **Out-there scale** (`out_there`, 1 to 5): 1 default, 2 familiar revival, 3 specialist, 4 deep cut, 5 far out. Match it to the client's appetite; 4 and 5 need the owner's yes.
- **Care flags.** Follow the `care` note where there is one (for example, borrow the form, not a political creed; keep a living observance's imagery out of merchandise).

## How to search
Filter, then open only the matching sheets:

```
python3 tools/lookbook_find.py --use poster --mood bold --avoid children --skip LB-014,LB-040 --max-out 3
```

It matches `use`/`theme`, `mood` and `energy`, drops looks whose `avoid_for` matches a subject, mood or use word, skips IDs from your log, and prints each look's sheet and panel. `--full` adds hallmarks, avoid-for, care, colours, neighbours and the Getty era term. Without Python, filter `looks.csv` the same way.

- **More like this:** `--like LB-010` lists that look's `nearest_looks` (the three most similar renders) and the looks that list it back.
- **By colour:** `--colour "#c5040f,#ed6322"` ranks looks by how close their dominant `colours` (3-5 hex values from the render) come to the given ones; combine with `--use`/`--mood`.
- **Era term:** established looks with a clear movement or period carry `getty_aat` (Getty AAT Styles and Periods ID and preferred term, [S266](../../SOURCES.md), ODC-By). It is a pointer for further reading, not a claim that the look copies any work. Technique-named and generic looks are left blank on purpose.
- **Search quality:** `python3 modules/lookbook/tests/score_find.py` scores the search on 26 generic briefs (`tests/briefs.json`): recall@8 and avoid-for violations.

## Cite
`LB-014 Suprematism at ~20%`: ID, name, strength. Add the layers taken above hint (`LB-005 Russian Constructivism at ~50%: palette, composition`).

New batches are folded in with `tools/lookbook_sync.py` (see `UPDATING.md`). IDs are stable and retired IDs are never reused.

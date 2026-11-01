# Blind A/B run 01: rules only vs rules plus aesthetic module (12 pairs)

**Judging? Stop here and open [`JUDGING.md`](JUDGING.md) instead.** This page describes how the pairs were made, which could bias you.

Status: **made and blinded, not yet judged** (1 November 2026). Everything here was generated or coded by Grok Bot. The same agent made both conditions and wrote the aesthetic module, so it must not judge the pairs; it hasn't.

## Conditions

- **rules:** `core/` plus the medium's modules, as of v0.3.1 (no AES rules).
- **rules+aes:** the same, plus `modules/aesthetic-critique/` (AES-0 to AES-10).

## How the pairs were made

- **Briefs.** Twelve, written and frozen before anything was made: two posters (one calm, one loud), an ink illustration, a character, a web page, an app screen, a social card, a 3D product render, a technical drawing, a logo lockup, an editorial spread and a game environment concept. Full text in [`JUDGING.md`](JUDGING.md).
- **Same start.** For each brief the rules version was made first. The rules+aes version started from the same generation or the same code file: an AES-0 intent model, a diagnosis against AES-1 to AES-8, at most two aesthetic changes (AES-10), then the measured checks again. Generated pieces were changed with one image edit of the shared first generation; the web page and editorial spread share one generated photo each.
- **Type in code.** Every piece with text has its type set in HTML/SVG and rendered with headless Chrome (as in `../src/compose.py`), so no generated lettering.
- **Checks on both versions.** The five look tests (`tools/look.py`) and contrast (`tools/contrast.py`, plus a worst-pixel check for type over images). Every text and needed-graphic pair passes WCAG minimums in both versions after fixes. Fixes and regressions are logged per version in the withheld making log.
- **Image budget.** 12 image generations: 7 first generations (5 pieces plus 2 shared photos) and 5 edits.

## Known confounds (read before trusting any result)

1. **Unequal effort.** The rules+aes version always had one extra round of work on top of the rules version. A win for it may come from more work, not from the module. A fair follow-up gives the rules condition an equal extra round.
2. **Maker knew the conditions** and wrote the module. The rules versions were made to pass the rules properly, not deliberately weakened, but this can't be ruled out from inside.
3. **Edits drift.** In some pairs an image edit applied only partly; those notes are in the making log and will be published with the key.
4. **One sample per brief**, one generator, one agent.

## Blinding

- `blind.py` assigns left/right per pair from a random seed and writes `images/pair-NN-A.jpg` and `-B.jpg` (no metadata), the contact sheets in `pairs/` (A left) and `pairs-swapped/` (same letters, sides swapped). Image sizes match within each pair.
- The answer key (`key.json`: seed, a random salt, the condition for each side and the SHA-256 of every image) and the sources and making log (`sources.tar.gz`) are **not in the repository**. Their SHA-256 hashes are committed now in [`KEY-SHA256.txt`](KEY-SHA256.txt). When judging is finished both files will be published, so anyone can check that they match the hashes and haven't been changed after seeing the votes. The salt stops anyone working out the key by trying all 4,096 left/right combinations against the hash.

## Judging

- People: [`JUDGING.md`](JUDGING.md) (inline images and a printable form) or [`judging-form.csv`](judging-form.csv). At least 5 judges who didn't make the work; do pass 2 (swapped) on another day if possible.
- Models: [`OUTSIDE-JUDGE-PROMPT.md`](OUTSIDE-JUDGE-PROMPT.md). Fresh session, images only, no repository access; reported separately from people.
- Analysis plan, fixed now: win rate for rules+aes with a 95% interval over all pair votes, the "neither" rate, flips between pass 1 and pass 2 (counted as marginal), Krippendorff's alpha across judges, and every pair reported, including losses.

# Taste profiles: separating personal preference from design rules

Shared agreement in art and design taste is low (about 8% for artworks, 11–12% for architecture; `AES-12`, [SRC-251]). Mixing an owner's personal house style into universal design rules creates contradictions and forces constant patching.

In v2, **universal hard gates** live in `core/kernel.md` and `manifest.json`, while **owner or brand preferences** live in a project-local `taste.json` (initialised from `taste.default.json`).

## Creating a taste profile

```sh
python3 tools/cd.py taste init --out taste.json
```

Pass `--taste taste.json` to `cd.py load` and `cd.py check`, or place `taste.json` beside `brief.json` for automatic discovery.

## What belongs in `taste.json` (not in universal rules)

- **`english_variety`**: `"en-GB"` or `"en-US"`.
- **`whites`**: `{"default": "neutral" | "warm", "warm_reason": "..."}`. When `"warm"`, `cd.py check` automatically forwards `--warm` to `autocheck.py` so intentional warm paper passes `CV-11`.
- **`finish_ceiling`**: `"restrained"` (stop two clicks before hyper-polished AI finish), `"lean"` (minimal typographic), or `"expressive"` (richer ornament/texture).
- **`preferred_typefaces`** / **`avoid_typefaces`**: brand or personal font allow/deny lists (e.g., excluding a font you dislike without hardcoding it into the shared library).
- **`avoid_tropes`**: recurring clichés to avoid on this project (e.g., coastal/lighthouse defaults, purple gradients, cracked grunge lettering, pack-shot staging).
- **`brand_tokens`** and **`owner_notes`**: specific palette hex roles, recurring house rules, or tone anchors.

## Precedence

1. **Explicit brief requirements** (`brief.json`) always win for a single job.
2. **Hard gates** (`manifest.json` `hard_gates`) never get waived by taste.
3. **Taste profile** (`taste.json`) governs defaults whenever the brief is silent.

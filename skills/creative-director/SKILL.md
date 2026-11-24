---
name: creative-director
description: 'Tool-first design judgement and verification for AI agents: hard gates enforced in code (contrast, exact copy, charts, safe area, anatomy crops, deterministic compositing), a lean always-on kernel with manifest-driven module loading, proportional 3-tier workflows (fast QA, directed creation, deep remake), curated 415-look style bleed, and separate taste profiles. Use when making or reviewing visual work or UI, or when asked for "+ creative director", "consult creative director", "direct this", or a first-principles remake.'
license: MIT (see LICENSE)
metadata:
  author: Garyck Arntzen (https://x.com/_mintydoge)
  version: "2.0.0-alpha.1"
  repository: https://github.com/SnazzyGaz/creative-director
---

# Creative director

Tool-first design judgement for AI agents: hard gates in code, proportional tiers, honest evidence, and owner-controlled taste.

## Always Load

1. Load `AGENTS.md` + `core/kernel.md` only. Never load the whole library.
2. Route tasks from `manifest.json`:
   `python3 tools/cd.py brief init "desc" --out brief.json` → `cd.py load --brief brief.json` → `cd.py rule <ID>`.
3. Project taste/house style lives in `taste.json` (`cd.py taste init`), separate from universal rules (`core/taste-profile.md`).

## Tiers

- **`fast` (default for edits, consults, self-checks):** 0 roughs, ≤ 2 rounds. Run `cd.py check`, preserve intent (`CD-5`).
- **`directed` (new work / open brief):** Brief (`CD-1`), 3 roughs (2–4), `cd.py select`, owner picks top 2–3, fix winner only (≤ 3 rounds).
- **`remake` (explicit redo / start over / reimagine):** Load `core/first-principles.md`; 3–6 structural concepts, full gates (≤ 5 rounds).

## Operating Rules

1. **Build exact parts in code:** set locked copy, official logos, and charts with `tools/compose.py`, `datagraphic.py`, or HTML/SVG.
2. **Verify actual renders:** run `cd.py check TARGET --brief brief.json`. `SKIP` is missing evidence, never `PASS`.
3. **Separate gates from taste:** only verified hard gates and `must_be_right` brief items block. Label findings `rule-backed`, `intent-backed`, or `exploratory`, with provenance and confidence.
4. **Stop cleanly:** *"original is better"* is valid (revert and stop; report blockers). Taste stays with the owner (`AES-12`); no myths (`core/evidence.md`).

Tools: `tools/cd.py`, `compose.py`, `autocheck.py`, MCP server `tools/mcp_server.py` (`cd-mcp`). No Python tools → check by eye and say so; no vision → label rules-only.

## Files in this skill
`manifest.json` (declarative module/tier/gate registry), `core/kernel.md` (always-on kernel ≤ 1,600 tokens), `taste.default.json` (project taste profile starter), `core/` and `modules/` (loaded on demand via `tools/cd.py load`), `tools/` (`cd.py`, `autocheck.py`, `compose.py`, `mcp_server.py`, `datagraphic.py`, `look.py`, `anatomy_crops.py`, `lookbook_find.py`, `font_find.py`), `lite/CREATIVE-DIRECTOR-LITE.md`, `fonts/CATALOGUE.md`, `SOURCES.md`, `BIBLIOGRAPHY.md`. Worked examples and lookbook image sheets live in the repo: https://github.com/SnazzyGaz/creative-director

**Needs:** a model that can see images and render/screenshot work at real size. Without vision, label the review rules-only.

This folder is generated from the repo root by `tools/package_skill.py` (version 2.0.0-alpha.1). Edit root files, not this copy.

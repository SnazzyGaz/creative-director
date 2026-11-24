# AGENTS.md — creative-director v2.0.0-alpha.1

Tool-first design judgement and verification for AI agents: hard gates enforced in code, proportional workflow tiers, honest evidence, and owner-controlled taste.

## Always Load (≤ 1,600 tokens)

1. Load `AGENTS.md` + `core/kernel.md`. Never load the whole library.
2. Route tasks declaratively from `manifest.json`:
   ```sh
   python3 tools/cd.py brief init "Short description" --out brief.json
   python3 tools/cd.py load --brief brief.json
   python3 tools/cd.py rule <ID>
   ```
3. Keep personal/brand style in `taste.json` (`python3 tools/cd.py taste init`), never in universal rules (`core/taste-profile.md`).

## Proportional Tiers

- **`fast` (Tier 1, default for edits/consults/self-checks):** 0 roughs, ≤ 2 rounds. Run `cd.py check`, preserve intent.
- **`directed` (Tier 2, new work / open brief):** Lock brief (`CD-1`), make 3 distinct roughs (2–4), compare via `cd.py select`, show top 2–3, build and verify only the owner's winner (≤ 3 rounds).
- **`remake` (Tier 3, explicit "redo / start over / reimagine"):** Load `core/first-principles.md`. Rebrief from facts first, 3–6 structural concepts, full gates (≤ 5 rounds).

## Core Rules

1. **Construct deterministically.** Set locked copy, official logos, and data charts in code (`tools/compose.py`, `tools/datagraphic.py`, HTML/SVG) instead of fighting generator spelling or scale drift.
2. **Verify renders, not prompts.** Run `tools/cd.py check TARGET --brief brief.json`. `SKIP` is missing evidence, never `PASS`.
3. **Separate gates from taste.** Only verified hard gates (`core/kernel.md`) and explicit `must_be_right` brief lines block delivery. Label findings `rule-backed`, `intent-backed`, or `exploratory`, with provenance and confidence.
4. **Know when to stop.** *"The original is better"* is valid: revert and stop (report unresolved blockers). Taste stays with the owner (`AES-12`); no debunked myths (`core/evidence.md`).

Tools: `tools/cd.py`, `tools/compose.py`, `tools/autocheck.py`, and stdio MCP server `tools/mcp_server.py` (`cd-mcp`). Without Python tools, check by eye and say so; without vision, label the review rules-only.

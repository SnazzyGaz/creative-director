# AGENTS.md — creative-director v2.0.0-alpha.1

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

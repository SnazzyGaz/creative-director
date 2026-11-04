# Contributing

Issues and pull requests are welcome. A few house rules keep the repo small and honest:

- **Rules:** use the `### ID. Title` format with What / Why / Check / Fix / Grade / Source. Grade honestly (`core/evidence.md`); a craft habit is *Craft wisdom*, not *Well supported*. Paraphrase sources in plain words, never paste them, and add each one to `SOURCES.md` with the next free `SRC-` number. Retired IDs stay retired (`docs/RETIRED-IDS.md`).
- **No names in the rules:** no client, brand or living-artist names as rules or styles; cited examples in a source note are fine.
- **Example images:** JPG or WebP, 1280 px or less on the long side (PNG only for line art or a screenshot that needs it, and still 1280 px or less). Keep each under about 300 KB where you can; big images make every clone slower.
- **Don't hand-edit `skills/creative-director/`:** it is generated. Run `python3 tools/package_skill.py` and `python3 tools/build_bundle.py`, then `python3 tools/check_budgets.py --loads`; CI runs the same checks with `--check`.
- **Keep the always-on files lean:** a new rule belongs in a module unless it must apply to every job.

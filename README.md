<p><picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/banner-dark.png">
  <img alt="creative director: design judgement for AI agents. A construction drawing of a box and a cylinder in perspective." src="docs/assets/banner-light.png" width="100%">
</picture></p>

A set of design rules and a critique loop that any AI agent can read. It helps an agent judge and improve its own visual work (drawings, illustrations, 3D renders, web and app UI, UX flows): render it, look at it the way a designer would, cite a rule for every problem, make up to three small fixes, and stop when the work is clearly better. Rules are grounded in perception research where it exists and in craft practice where it doesn't, and taste calls stay with the person who owns the work.

<p><picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/before-after-dark.jpg">
  <img alt="Three before/after pairs: a box and can drawing with its perspective rebuilt, a knight illustration with a quieter sky, and a landing page with readable contrast." src="docs/assets/before-after-light.jpg" width="100%">
</picture></p>

The three pairs above are generated, one or two rounds each. Nine stress tests across every domain, including three take-overs of deliberately bad work, with critiques, logs and honest misses: [examples/](examples/).

## How it works

<p><picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/loop-dark.png">
  <img alt="The loop: 0 Brief, 1 Render, 2 Look, 3 Critique, 4 Fix, 5 Stop. Fix loops back to Render. If the work is fundamentally broken, take over and rework." src="docs/assets/loop-light.png" width="100%">
</picture></p>

Each rule has an ID (`CORE-2`, `TD-PER-1`, `UI-6`) and the same parts: what, why, a check you can run, the usual fix, and a source. Only **MUST-BE-RIGHT** errors (perspective, anatomy, light, contrast and accessibility, broken flows, 3D build defects) block; everything else is a default. Full loop: [`core/critique-loop.md`](core/critique-loop.md).

## Usage

| Mode | What happens |
|---|---|
| **Self-check**<br>`+ creative director` | The agent runs the loop on its own output. Cheapest. |
| **Consult**<br>`consult creative director` | Send the brief and the real output; get back a neutral critique with ranked fixes ([template](core/critique-template.md)). |
| **Direct**<br>`creative director: direct this` | Joins at the start: writes the brief, sets direction, picks from rough options, reviews at checkpoints ([CD-1..6](core/creative-direction.md)). |

Always send the actual output (image, screenshot at real size, URL or renders), never a description.

## Works with

| Tool | Entry point |
|---|---|
| Cursor | [`.cursor/rules/creative-director.mdc`](.cursor/rules/creative-director.mdc), [`AGENTS.md`](AGENTS.md) |
| Claude Code, Claude Skills | [`CLAUDE.md`](CLAUDE.md), [`SKILL.md`](SKILL.md) |
| Codex, Gemini CLI, Jules | [`AGENTS.md`](AGENTS.md) |
| GitHub Copilot | [`.github/copilot-instructions.md`](.github/copilot-instructions.md) |
| ChatGPT, Gemini Gems, Claude Projects | Upload `AGENTS.md`, `core/` and the modules you need as knowledge |
| Grok Bot | [`AGENTS.md`](AGENTS.md), or point it at this repo |

Every entry point leads back to `AGENTS.md`, and [`llms.txt`](llms.txt) is there for tools that read it.

## What's inside

```
core/       principles, creative direction, evidence, the loop, critique template, module picker
modules/    technical-drawing · illustration · web-ui · ux · 3d
tools/      look tests, WCAG contrast, screenshots, vanishing points, ellipses, before/after
examples/   stress tests, round by round, including this README's own critique
```

## Principles of the critique

- **Neutral.** Factual, like a thesis supervisor. No praise padding, no harshness.
- **Rule-cited.** Every point names a rule ID and the evidence. No rule, no point; it becomes a question for the owner.
- **Light touch.** Keep the intent and what already works. At most three fixes a round, then stop when clearly better.
- **Take over when broken.** If the construction is fundamentally wrong, rework it, then re-check it still answers the brief.

This README went through the loop too: [examples/readme-self-critique](examples/readme-self-critique/).

## Sources and evidence

Every rule cites its sources in [SOURCES.md](SOURCES.md); what the research supports, and the myths to stop repeating, are in [core/evidence.md](core/evidence.md).

## Licence

MIT, see [LICENSE](LICENSE). Cited works stay with their authors; this repo paraphrases and links to them.

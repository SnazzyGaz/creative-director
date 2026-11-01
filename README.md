<p><picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/banner-dark.png">
  <img alt="creative director: design judgement for AI agents. A construction drawing of a box and a cylinder in perspective." src="docs/assets/banner-light.png" width="100%">
</picture></p>

**What it gives an agent is restraint and accuracy, not flair.** It stops agents inventing details nobody asked for (addresses, slogans, facts), breaking contrast and accessibility, and drifting from the brief, and it makes them render and measure their own work before calling it done. It won't make work more exciting by itself: in the test below, the versions made without it are more vivid at a glance. They are also the ones with invented facts.

**[Gallery](https://snazzygaz.github.io/creative-director/gallery/)** · **[Install as Grok Bot](https://x.ai/bot/XWBKgRnDOw7uR5SpKx3Af)** · **[Claude Skill zip](https://github.com/SnazzyGaz/creative-director/releases/latest/download/creative-director-skill.zip)** · **[Lite version](lite/CREATIVE-DIRECTOR-LITE.md)**

<p><picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/baseline-dark.jpg">
  <img alt="Same prompts without the skill, with the skill, and with the skill plus the aesthetic layer. Book cover: without, a busy rainbow cover with an invented subtitle, signs and slogans; with, a calm painted fox under a tree with the title set in type; plus aesthetic layer, the same cover in warm golden-hour light with a robin beside the fox. Event poster: without, a rich street scene with an invented address and slogans; with, a plain cream poster with a navy double bass and only the given facts; plus aesthetic layer, a navy night street with lit windows and a lamp, same facts in cream type." src="docs/assets/baseline-light.jpg" width="100%">
</picture></p>

Same prompt, same image model (Grok Bot's built-in GenerateImage), one sample each, so an illustration, not a benchmark. *Without:* the prompt as is; the model lettered its own text and invented a subtitle, signs, slogans and an address. *With:* the skill's loop; art generated without text, then every word set in code from the brief's facts only (the cover's author is a marked placeholder), two to three rounds. The with-skill versions win on accuracy, hierarchy and legibility, and lose on first-impression energy and atmosphere. *+ aesthetic layer:* one more pass with the [aesthetic module](modules/aesthetic-critique/) (one new text-free image each, same facts and type in code, contrast re-checked); it wins back warmth and atmosphere, though that's Grok Bot's own judgement on one sample each. [Full write-up](examples/baseline-comparison/) · [aesthetic notes](examples/aesthetic-benchmark/).

A set of design rules and a critique loop that any AI agent can read. It helps an agent judge and improve its own visual work (drawings, illustrations, 3D renders, web and app UI, UX flows): render it, look at it the way a designer would, cite a rule for every problem, make up to three small fixes, and stop when the work is clearly better. Rules are grounded in perception research where it exists and in craft practice where it doesn't, and taste calls stay with the person who owns the work.

<details><summary>Three more before/after pairs</summary>

<p><picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/before-after-dark.jpg">
  <img alt="Three before/after pairs: a box and can drawing with its perspective rebuilt, a knight illustration with a quieter sky, and a landing page with readable contrast." src="docs/assets/before-after-light.jpg" width="100%">
</picture></p>

Generated, one or two rounds each.
</details>

Example sets across every domain: four take-overs of deliberately bad work, nudges, one small case per common agent failure, the baseline above and an aesthetic demo, all with critiques, logs and honest misses: [examples/](examples/), or filter them in the [gallery](https://snazzygaz.github.io/creative-director/gallery/). To test it on another model, the [cross-model kit](examples/cross-model/) has the inputs, prompts and scoring. There are two outside pilot runs so far, [Claude Opus 5.5 and ChatGPT GPT-6](examples/cross-model/runs/), both contaminated (the models had read the answer keys), so they score nothing. What they suggest: without the skill the models already found most faults; with it, the critiques were better structured (blockers first, rule IDs, brief kept), and where the tools were run they gave measurements instead of guesses. A clean, blind run is still wanted.

## How it works

<p><picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/loop-dark.png">
  <img alt="The loop: 0 Brief, 1 Render, 2 Look, 3 Critique, 4 Fix, 5 Stop. Fix loops back to Render. If the work is fundamentally broken, take over and rework." src="docs/assets/loop-light.png" width="100%">
</picture></p>

Each rule has an ID (`CORE-2`, `TD-PER-1`, `UI-6`) and the same parts: what, why, a check you can run, the usual fix, and a source. Only **MUST-BE-RIGHT** errors (perspective, anatomy, light, contrast and accessibility, broken flows, 3D build defects) block; everything else is a default. Full loop: [`core/critique-loop.md`](core/critique-loop.md).

### Correctness and quality

Passing the rules makes work correct, not necessarily good: in the [baseline](examples/baseline-comparison/) the with-skill poster won on accuracy and legibility but lost on atmosphere. The [aesthetic layer](modules/aesthetic-critique/) addresses that in three ways. It starts from an intent model (purpose, audience, mood, style, polish), with each line marked as stated or guessed. It judges versions side by side for the brief ("which is stronger, why, at what cost"), not by adding up scores. And it changes one or two aesthetic things at a time, re-running the measured checks so a mood gain can't hide a regression. Critiques keep **measured** findings (checked with a tool; only these block) apart from **interpreted** ones (aesthetic readings, labelled as such). A [reference library](docs/references.md) of 27 public works and a [blind test protocol](examples/aesthetic-benchmark/) come with it. See it in the [reference set](examples/aesthetic-benchmark/reference-set/): 12 briefs across posters, web, app, 3D, technical drawing, branding, editorial and game art, each shown rules-only next to rules plus the aesthetic layer (four also with the plain no-skill output). It's made and judged by Grok Bot, so it's a showcase, not evidence.

## Usage

| Mode | What happens |
|---|---|
| **Self-check**<br>`+ creative director` | The agent runs the loop on its own output. Cheapest. |
| **Consult**<br>`consult creative director` | Send the brief and the real output; get back a neutral critique with ranked fixes ([template](core/critique-template.md)). |
| **Direct**<br>`creative director: direct this` | Joins at the start: writes the brief, sets direction, picks from rough options, reviews at checkpoints ([CD-1..6](core/creative-direction.md)). |

Always send the actual output (image, screenshot at real size, URL or renders), never a description.

## Install in Claude

Download [`creative-director-skill.zip`](https://github.com/SnazzyGaz/creative-director/releases/latest/download/creative-director-skill.zip) (about 100 KB: `SKILL.md` with the full instructions, `core/`, `modules/`, `lite/`, `tools/`; no images or examples). Built by [`tools/package_skill.py`](tools/package_skill.py).

- **claude.ai:** Customize > Skills > **+** > Upload a skill, and pick the zip. Needs code execution on (Settings > Capabilities).
- **Claude Code:** `unzip creative-director-skill.zip -d ~/.claude/skills/` (or `.claude/skills/` inside a project).
- **Claude Projects:** unzip, then add `creative-director/SKILL.md`, `core/` and the modules you need as project knowledge.

## Requirements

- **Vision.** The agent has to *see* its output: a model that accepts images.
- **A way to render or screenshot** the work at real size: a browser for UI, a renderer for 3D, the image file for pictures.
- **Recommended setup:** Playwright or headless Chrome for UI (`tools/shot.sh` uses Chrome), Blender for 3D (plus [model-qa](https://github.com/SnazzyGaz/model-qa) for build checks), and Python 3 with Pillow and NumPy for the `tools/` scripts (look tests, contrast, vanishing points, ellipses, layout grid, 3D intersections; `pip install -r tools/requirements.txt`).
- **Without vision** you only get a rules-only review of code or a description. It can still catch contrast, spacing and flow problems in code, but it can't judge how the work looks, and it is much weaker.

Context cost: about 9,100 tokens for `core/` plus 1,700-3,000 per module ([table](core/which-modules.md#token-cost-per-module)). For small context windows, [`lite/CREATIVE-DIRECTOR-LITE.md`](lite/CREATIVE-DIRECTOR-LITE.md) has the loop, core rules and blockers in about 1,600 tokens.

## Works with

| Tool | Entry point |
|---|---|
| Cursor | [`.cursor/rules/creative-director.mdc`](.cursor/rules/creative-director.mdc), [`AGENTS.md`](AGENTS.md) |
| Claude Code, Claude Skills | [Skill zip](https://github.com/SnazzyGaz/creative-director/releases/latest/download/creative-director-skill.zip) ([install](#install-in-claude)), [`CLAUDE.md`](CLAUDE.md), [`SKILL.md`](SKILL.md) |
| Codex, Gemini CLI, Jules | [`AGENTS.md`](AGENTS.md) |
| GitHub Copilot | [`.github/copilot-instructions.md`](.github/copilot-instructions.md) |
| ChatGPT, Gemini Gems, Claude Projects | Upload `AGENTS.md`, `core/` and the modules you need as knowledge |
| Grok Bot | One-click install: [Creative Director bot](https://x.ai/bot/XWBKgRnDOw7uR5SpKx3Af), or point any bot at [`AGENTS.md`](AGENTS.md) |

Every entry point leads back to `AGENTS.md`, and [`llms.txt`](llms.txt) is there for tools that read it.

## What's inside

```
core/       principles, creative direction, brand intake, evidence, the loop, critique template, module picker
modules/    technical-drawing · illustration · character · web-ui · ux · 3d
            typography · layout (social, posters, slides, print) · brand · aesthetic-critique
tools/      look tests, WCAG contrast, screenshots, vanishing points, ellipses, layout grid, 3D intersections, before/after
examples/   stress tests, round by round, including this README's own critique
lite/       the loop, core rules and blockers in one short file
docs/       gallery, README images, reference library, design notes (DECISIONS.md, PROPOSED-REPO.md)
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

# Brand intake (step 0 add-on)

Run this at step 0 (CD-1) when the brief has no brand input: no colours, no typefaces, no voice, no logo rules, no examples. It takes about two minutes and saves rounds.

Why it exists: in the web-ui-landing stress test, two rounds fixed every contrast failure but the page still looked generic, because nothing in the brief said what it should look like instead ([examples/web-ui-landing/log.md](../examples/web-ui-landing/log.md)). The generic look (UI-7, ILL-11, TYPE-9) is a missing-input problem. More critique rounds can't supply the input.

## When to run it

- The brief names no brand, or names one but gives no guide or assets.
- Or the critique finds two or more generic-look tells and none of the choices trace back to the brief.

If there is a brand guide, skip the questions and read the guide with `modules/brand/` (BRAND-1).

## The questions

Ask the owner of the work. Ask all at once, keep each answer short, and accept "don't know".

1. **Who is it from?** Name, and one line on what they do.
2. **Who is it for, and what should they feel or do after seeing it?**
3. **Existing assets?** Logo files, colours (hex), typefaces, a site or past work to match. Links are fine.
4. **Three words for the voice.** E.g. "plain, warm, exact". Also one word it must *not* sound like.
5. **Something you like, and something you don't.** One example each (a site, a poster, a brand), and what about it.
6. **Fixed points.** Anything that must appear or must not (legal lines, a mascot, a colour a competitor owns).
7. **Where will it be seen?** Platforms and sizes (LAY-4), print or screen, light or dark context.

## If there are no answers

Don't stall and don't invent a brand. Write down the assumptions as a mini token sheet and label it **assumed**:

- **Colour:** one neutral ramp, one accent taken from the subject (not purple-to-blue by default), roles for text, surface, accent and error.
- **Type:** one family or one pair, with a reason (TYPE-1, TYPE-9).
- **Voice:** three words, inferred from the audience.
- **Shape:** one radius and one shadow, with a role.

Hand the sheet back with the work under "Questions for the owner", so the next round has real input.

## Output

A short block in the brief:

```
Brand: <name> | voice: <3 words> (not: <1 word>)
Colours: <hex roles>  | Type: <display> / <text>
Logo: <file, clear space, min size> | Must / must not: <...>
Status: given | partly assumed | assumed
```

Sources: Wheeler, *Designing Brand Identity* (brand standards and assets) [S119]; Moran, NN/g, *The Four Dimensions of Tone of Voice* [S121]; BetterBriefs/IPA briefing guide [S88]; CD-1.

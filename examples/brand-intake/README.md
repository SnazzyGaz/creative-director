# Brand intake on the web-ui-landing case

The [web-ui-landing](../web-ui-landing/log.md) stress test stopped at round 2 with every blocker fixed and five generic-look tells left (UI-7): gradient hero, Inter, centred hero, three identical icon cards, vague copy ("Supercharge your workflow with AI"). The log's lesson: that needs brand input, not more rounds. This is what `core/brand-intake.md` does with the same case.

## Trigger

Brief named a product ("Nimbus AI") but gave no guide, colours, type or voice; critique found 5 tells with no choice traceable to the brief. Both triggers met, so intake runs at step 0.

## Questions sent to the owner

1. Who is it from, and what does it do?
2. Who is it for, and what should they do after seeing the page?
3. Logo, colours (hex), typefaces, or a site to match?
4. Three words for the voice, and one word it must not sound like.
5. One example you like and one you don't, and why.
6. Anything that must or must not appear?
7. Where will it be seen (desktop, phone, ads, social cards)?

## No-answer mode

The test page has no real owner, so intake ran with no answers (BRAND-7). The assumed sheet, built from the subject (a nimbus is a rain cloud; the product is a workflow tool) rather than from defaults:

```
Brand: Nimbus AI | voice: plain, calm, exact (not: hype)   Status: ASSUMED
Colours: ink #1E2A33 (slate) on paper #F4F1EA; muted text #5A6670;
         accent #F2C230 (signal yellow) as fill only, with ink text; error #B3261E
Type: one family, a humanist sans with a reason (calm, legible at 16 px), not Inter by default
Shape: 6 px radius on cards and inputs; buttons the same; one soft shadow for raised items only
Logo: none supplied; wordmark set in the text face, nothing generated
```

Contrast check of the assumed roles (WCAG): ink on paper 12.98:1, muted on paper 5.22:1, ink on accent 8.74:1, error on paper 5.79:1. All pass UI-6, so the sheet can't introduce a blocker.

## What it changes

| UI-7 tell left after round 2 | Resolved by |
|---|---|
| Purple-to-blue gradient hero | Colour roles from the subject (slate, paper, yellow) |
| Inter everywhere | Type with a stated reason (TYPE-9), owner to confirm |
| Centred hero, one button | Layout follows content once real copy exists (UX-6), not the template |
| Three identical icon cards | Needs real features from the owner (question 1) |
| "Supercharge your workflow" | Voice words "plain, calm, exact" (BRAND-5); real claims only from the owner |

Two of five tells can be answered from the assumed sheet; three need the owner's facts. That is the honest limit: intake turns "looks generic" into specific questions, and the answers do the rest. Not re-rendered here, because rendering the assumed sheet would present guesses as the brand.

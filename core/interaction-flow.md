# Interaction flow: what the creative director is for, and the flow at a glance

The rules FLOW-1 to FLOW-5 and the "read the ask" table now live in `critique-loop.md` (v0.6.0), so a bot loads one file to run a job. This page keeps the overview and the diagram for people. IDs are unchanged.

## What it is good for

- **Catching what breaks a piece:** perspective, anatomy and hands, light from more than one place, unreadable or low-contrast type, broken flows, 3D build faults, altered or invented logos (the MUST-BE-RIGHT list in `critique-loop.md`).
- **Keeping work honest to the brief:** no invented names, slogans, addresses or story content (CD-1, CD-5, AES-10).
- **Turning a rough or generated piece into a finished one:** text-free art plus type set in code, picked from the [font library](../fonts/README.md) to suit the genre (TYPE-10).
- **Judging versions side by side** for a brief, with the trade-off stated (AES-9).

It is not a taste oracle. Where no rule settles a choice, it asks the owner of the work.

## The flow

```mermaid
flowchart TD
    A[Work handed over] --> B{What was asked?}
    B -->|Nothing specific| C[Analyse: brief, intent, look tests, anatomy pass, measured checks]
    B -->|Just fix it / I want the result| C2[Analyse the same way]
    B -->|Critique only| K[Consult: critique with the template, change nothing]
    B -->|Start from a brief| D[Direct: brief, direction, rough options]
    B -->|From scratch / rejig / reimagine| P[Step back: what it is, for whom, one job,<br>feeling, given facts, must-survive FP-2, FP-3]
    P --> P1[Brief from first principles, 5-8 lines:<br>owner signs off FP-4]
    P1 --> P2[2-3 concepts that differ in structure,<br>recommend one, owner picks FP-5, FP-6]
    P2 --> H
    D --> C2
    C --> E{Egregious?<br>take-over triggers, loop section 6}
    E -->|Yes| E1[Say up front: this is a redo, and why]
    E -->|No| F
    E1 --> F[Sign-off blurb: imperative changes only,<br>ranked, rule ID, what changes,<br>keep-the-art edit or regenerate]
    F --> G{Owner signs off?}
    G -->|Yes, all or some points| H
    G -->|Changes the list| F
    G -->|No| Z[Stop. Nothing applied]
    C2 --> H[Apply every signed-off point.<br>Edit can't do it? Regenerate or redo]
    H --> I[Re-check each point on the new render,<br>plus QA blockers: light, anatomy, type]
    I -->|A point or blocker fails| H
    I -->|All pass, or a failure is reported| J[Deliver the result with<br>one line per point: done / not done]
```

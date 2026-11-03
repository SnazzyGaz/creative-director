# Web and app UI notes (optional depth)

## Grids (Müller-Brockmann) [SRC-60]
- Divide the page into columns and rows of fields, separated by consistent gutters. Text, images and captions fill whole fields.
- Fewer image sizes give a calmer, more legible page. Choose the grid to suit the content, not the other way round.
- On the web, a column grid plus a spacing scale (CORE-4) does the same job. Intrinsic layouts (*Every Layout*) let content set breakpoints [SRC-56].

## Modular scale [SRC-55, SRC-56]
Start at the body size and multiply or divide by one ratio for headings, and for spacing too if you like. Round the results. Treat the scale as suggestions, not law.

## Refactoring UI habits [SRC-57]
Practitioner advice, not research, but concrete:
- Start with too much white space, then remove it.
- Design in greyscale first, then add colour (this matches CORE-2).
- Use fewer borders. Separate with space, shadow or a background shift.
- Shadows are offset vertically, as if lit from above.
- Don't enlarge small icons to fill space. Put them in a shape instead.
- Reserve a solid button for the primary action.

## Platform specifics
- **Apple HIG:** hit targets (sizes in UI-5); system text styles so Dynamic Type works; default body 17 pt; minimum 11 pt [SRC-58].
- **Material 3:** targets (UI-5); type scale tokens; colour roles in pairs (primary / on-primary, container / on-container, surface / on-surface). Don't mix pairs from different roles [SRC-13, SRC-59].

## Colour spaces in one paragraph
OKLCH (Ottosson's Oklab in polar form) has perceptual lightness, so palettes and hover states built by changing L behave predictably across hues. It also fixes LCH's blue-to-purple shift. Some L/C/H values fall outside sRGB, so check gamut. It is not a contrast metric [SRC-50].

# Web and app UI notes (optional depth)

## Grids (Müller-Brockmann) [S60]
- Divide the page into columns and rows of fields, separated by consistent gutters. Text, images and captions fill whole fields.
- Fewer image sizes give a calmer, more legible page. Choose the grid to suit the content, not the other way round.
- On the web, a column grid plus a spacing scale (UI-3) does the same job. Intrinsic layouts (*Every Layout*) let content set breakpoints [S56].

## Modular scale [S55, S56]
Start at the body size and multiply or divide by one ratio for headings, and for spacing too if you like. Round the results. Treat the scale as suggestions, not law.

## Refactoring UI habits [S57]
Practitioner advice, not research, but concrete:
- Start with too much white space, then remove it.
- Design in greyscale first, then add colour (this matches CORE-2).
- Use fewer borders. Separate with space, shadow or a background shift.
- Shadows are offset vertically, as if lit from above.
- Don't enlarge small icons to fill space. Put them in a shape instead.
- Reserve a solid button for the primary action.

## Platform specifics
- **Apple HIG:** 44 × 44 pt hit targets; system text styles so Dynamic Type works; default body 17 pt; minimum 11 pt [S58].
- **Material 3:** 48 dp targets; type scale tokens; colour roles in pairs (primary / on-primary, container / on-container, surface / on-surface). Don't mix pairs from different roles [S13, S59].

## Colour spaces in one paragraph
OKLCH (Ottosson's Oklab in polar form) has perceptual lightness, so palettes and hover states built by changing L behave predictably across hues. It also fixes LCH's blue-to-purple shift. Some L/C/H values fall outside sRGB, so check gamut. It is not a contrast metric [S50].

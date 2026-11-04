# Font library

107 free font families in 29 themes, so type can match a brief's genre instead of the same face turning up in every piece (TYPE-10 in [`modules/typography/`](../modules/typography/README.md#type-10-pick-type-from-the-theme-catalogue-to-suit-the-genre-dont-reuse-one-face-everywhere)).

<p><img alt="Every family in the library, set in its own face, grouped by theme from editorial serif to luxury didone." src="specimens/overview.png" width="100%"></p>

- **Search, don't read:** `python3 tools/font_find.py --mood warmth,craft --genre heritage` shortlists families by mood, genre and use (about 15,000 tokens saved against reading the catalogue).
- **[CATALOGUE.md](CATALOGUE.md):** per family, its themes, licence, axes or weights, mood tags, what it's good for, what to avoid and what it pairs with, plus a "By mood" index (trust, calm, warmth, play, speed, power, precision, luxury, elegance, heritage, craft, rebellion, menace, nostalgia, tech, romance, authority). Same data as [`catalogue.json`](catalogue.json) for scripts.
- **Specimens:** one sheet per theme in [`specimens/`](specimens/) (sample line, weight range, pangram), plus the overview above.
- **Files:** `fonts/<theme>/<family>/`, each folder with its licence in git. The font files themselves (variable versions where they exist) are in `creative-director-fonts.zip` on the [assets-v1 release](https://github.com/SnazzyGaz/creative-director/releases/tag/assets-v1) to keep clones small; `python3 tools/fetch_assets.py` unpacks them into these folders. Every family is also on Google Fonts under the same name. Instrument Sans, used for the README images, stays in `docs/assets/src/fonts/` and is listed in the catalogue too.

## How to pick

1. Name the brief's genre and tone in a few words ("comic pulp romance", "quiet literary memoir", "cyberpunk game UI"), and the one or two moods it must carry. The "By mood" index in the catalogue gives a shortlist; the theme narrows it.
2. Open the matching theme's specimen sheet and catalogue rows. Families also listed under other themes are marked "also".
3. Pick one display face whose "good for" fits and whose "avoid" line your use doesn't break. Pair it with a text face from its "pairs with" list (TYPE-1: two families, each with a job).
4. Set it properly: one scale, real sizes, tracking, contrast (TYPE-2 to TYPE-6, UI-6).
5. Check you haven't used the same family in your last few unrelated pieces. Vary it.

A brand guide always wins over the catalogue (BRAND-3), and the face is a taste call for the owner of the work. The catalogue's notes are craft guidance written for this repo, not research findings; the research only says that readers do read personality into type (SRC-156, SRC-157 in [SOURCES.md](../SOURCES.md)).

## Themes

| Theme | For | Families (primary) |
|---|---|---|
| [Editorial / literary serif](specimens/editorial-serif.png) | Novels, essays, magazines, serious non-fiction. | EB Garamond, Libre Caslon Text, Literata, Newsreader |
| [Pulp / retro / comic](specimens/pulp-retro-comic.png) | Comic books, pulp paperbacks, comedy, loud retro. | Bangers, Luckiest Guy, Shrikhand |
| [Noir / thriller](specimens/noir-thriller.png) | Crime, spy, hard-boiled, case files. | Big Shoulders, Courier Prime, Special Elite |
| [Horror](specimens/horror.png) | B-movie, gothic, slasher, folk horror. | Butcherman, Creepster, Jim Nightshade |
| [Sci-fi / tech](specimens/scifi-tech.png) | Space, cyberpunk, games, tech products. | Exo 2, Orbitron, Oxanium |
| [Fantasy / medieval](specimens/fantasy-medieval.png) | Epic fantasy, myth, pirates, blackletter. | Cinzel, Pirata One, UnifrakturMaguntia |
| [Children's / playful](specimens/childrens-playful.png) | Picture books, kids' apps, friendly brands. | Baloo 2, Chewy, Fredoka |
| [Romance / script](specimens/romance-script.png) | Romance, weddings, formal invitations. | Dancing Script, Great Vibes, Pinyon Script |
| [Western / slab](specimens/western-slab.png) | Wild West, Americana, wanted posters. | Rye, Ultra, Zilla Slab |
| [Art Deco / display](specimens/art-deco-display.png) | 1920s-30s, jazz age, cinema marquees. | Italiana, Josefin Sans, Limelight, Poiret One, Righteous |
| [Grotesk / neutral UI](specimens/grotesk-neutral.png) | Interfaces, docs, quiet subtitles. | Bricolage Grotesque, Hanken Grotesk, Instrument Sans, Inter, Manrope, Public Sans |
| [Geometric sans](specimens/geometric-sans.png) | Modernist, Bauhaus, brand headings. | Jost, League Spartan, Outfit, Sora |
| [Humanist sans](specimens/humanist-sans.png) | Warm, readable text and UI; accessibility. | Atkinson Hyperlegible Next, Cabin, Source Sans 3 |
| [Monospace / code](specimens/monospace-code.png) | Code, terminals, data labels, typewriter. | JetBrains Mono, Martian Mono, Space Mono |
| [Condensed poster](specimens/condensed-poster.png) | Film and gig posters, impact headlines. | Anton, Antonio, Bebas Neue, Oswald |
| [Handwritten / marker](specimens/handwritten-marker.png) | Notes, DIY, street, personal tone. | Caveat, Patrick Hand, Permanent Marker, Rock Salt |
| [Nautical / vintage](specimens/nautical-vintage.png) | Seafaring tales, old print, harbour signs, labels. | Alfa Slab One, IM Fell English, Sail, Vast Shadow |
| [Luxury / high-contrast didone](specimens/luxury-didone.png) | Fashion, perfume, classical, premium. | Abril Fatface, Bodoni Moda, DM Serif Display, Playfair Display |
| [Heritage / badge slab](specimens/heritage-badge.png) | Pubs, saloons, breweries, barbers, crests and badges: Clarendon and slab with a stamped, established feel. | Arvo, Besley, Bevan, Bowlby One, Holtwood One SC, Rokkitt |
| [Blackletter](specimens/blackletter.png) | Tattoo, metal, brewing, old newspapers, Gothic and German-flavoured heritage. | Grenze Gotisch, Texturina, UnifrakturCook |
| [Brutalist / grotesk display](specimens/grotesk-display.png) | Raw, confident headlines: studios, galleries, tech launches, zines, statement posters. | Archivo, Schibsted Grotesk, Space Grotesk |
| [Variable expressive display](specimens/expressive-variable.png) | Festivals, music, motion titles and identities that stretch, squash and change weight. | Anybody, Syne |
| [Rounded friendly sans](specimens/rounded-friendly.png) | Friendly apps, health, food, family and community brands; soft, approachable UI. | Comfortaa, Nunito, Quicksand, Varela Round |
| [Stencil / industrial](specimens/stencil-industrial.png) | Crates, military, logistics, workshops, streetwear and spray-painted signs. | Allerta Stencil, Big Shoulders Stencil, Saira Stencil One, Stardos Stencil |
| [Signage / DIN-like](specimens/signage-din.png) | Wayfinding, transport, dashboards, instruments, labels read at a glance. | B612, Bungee, Overpass, Saira |
| [Wide / extended display](specimens/wide-extended.png) | Short, wide statements: motorsport, fashion, tech and luxury logotypes. | Krona One, Michroma, Unbounded |
| [High-contrast modern serif](specimens/modern-serif.png) | Contemporary editorial, fashion, culture and premium brand headlines. | Gloock, Instrument Serif, Libre Bodoni, Young Serif |
| [Warm old-style text serif](specimens/oldstyle-text.png) | Long reading with a human warmth: books, essays, menus, craft brands. | Alegreya, Cormorant, Crimson Pro, Lora, Source Serif 4 |
| [Script / brush signage](specimens/script-signage.png) | Shopfronts, diners, cafés, surf, retro sports and hand-painted signs. | Damion, Kaushan Script, Pacifico, Yellowtail |

## Licences

Every family is under the [SIL Open Font License 1.1](https://openfontlicense.org) or the Apache License 2.0. Both allow use in commercial work, embedding, and redistribution with the licence included; OFL fonts may not be sold on their own, and modified versions may not use a reserved font name [SRC-154]. Each family's licence file sits next to its fonts. The files come unmodified from [github.com/google/fonts](https://github.com/google/fonts) (fetched 1 November 2026; the 46 families added in v0.9.9 on 4 November 2026) [SRC-155]. Skipped on purpose: large CJK families, and static weight sets where a variable font exists. Zilla Slab has no variable version, so only Regular, Italic, SemiBold and Bold are kept. Inter and Exo 2 are upright only. Of the v0.9.9 additions, italics are kept only for text and workhorse families; display faces are upright only. The mood tags, like the other notes, are this repo's craft judgement.

## Rebuild

`python3 fonts/build.py` re-renders the specimen sheets and the tables in `CATALOGUE.md` from `catalogue.json` (Pillow only, no network). To add a family: put its folder (fonts and licence) under its theme, add an entry to `catalogue.json`, and re-run.

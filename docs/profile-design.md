# Profile design

The profile uses a sketchbook layout with a short introduction, four illustrated project cards, and direct contact links.

The header balances loose handwritten lettering with dimensional pen drawings. The laptop, headphones, racket, drink, dumbbell, F1 car, and mountain-and-coast study reflect Arnav's work and interests. Small handwritten arrows connect “usually here” to the laptop, “always on” to the headphones, “or here” to the outdoor study, and NMIMS / Mumbai to the Computer Engineering line. The badminton racket has an open string grid inside a double oval frame. There are no written drink or hobby labels.

## Current header assets

- `assets/sketchbook/header-animated-dark.svg`
- `assets/sketchbook/header-animated-light.svg`

The static illustrations (`header-edited-dark.png` and `header-edited-light.png`) were edited with the built-in image tool. `scripts/build_name_animation.py` embeds them unchanged in self-contained SVGs. The name-and-marker region reveals from left to right, holds, then fades and repeats over seven seconds. All other artwork stays still; reduced-motion preferences show the full static header. The exact edit prompts are in [illustration-prompts.md](illustration-prompts.md). GitHub's picture sources select the matching theme. The original pen-drawing source and earlier header files remain available; running `scripts/build_sketchbook.py` does not overwrite the current illustrated header.

## References

- [Liz Steel: Placement and White Space](https://www.lizsteel.com/sketchbookdesigntoptips/): grouped sketches, open space, and interlocking forms.
- [Sandy Allnock: Composition in Doodling](https://sandyallnock.com/composition-in-doodling-with-custom-brush-pen/): using light and dark space and directional marks to unify a page.
- [GitHub's profile guidance](https://docs.github.com/en/account-and-profile/tutorials/using-your-github-profile-to-enhance-your-resume): personal context and a small selection of projects.

Reference artwork is not incorporated into the header. The project drawings are the original notebook assets rendered by `scripts/build_sketchbook.py`. The profile is updated locally; publishing and profile-pin settings are separate.

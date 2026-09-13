# Behind the cabinet

**[Play BUG//CHASE →](room-1-1-0.md)** · [Profile](../README.md)

This is a link-driven maze built for GitHub's Markdown renderer. A room's filename
encodes its position and whether the player has the patch. Direction links lead to
the next state. Bugs end the run; the exit only wins after collecting the patch.
There is no server, tracking, shared save, or scheduled workflow.

The profile banner uses self-contained SVG animation, with a static fallback for
reduced-motion preferences. The playable rooms use static SVGs and ordinary links.
Text maps are available in every room. The full board deliberately stays visible:
this is a short navigation puzzle, not a reflex game.

To customize the maze, colors, copy, or artwork, edit
[`scripts/build_arcade.py`](../scripts/build_arcade.py), then run:

```sh
python3 scripts/build_arcade.py
python3 scripts/check_arcade.py
```

The profile prose lives in the root `README.md`. All room Markdown and SVG files
are generated. If changing the maze layout, remove obsolete generated
`room-*.md` and `maps/room-*.svg` files before regenerating.

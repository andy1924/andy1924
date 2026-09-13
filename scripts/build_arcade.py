"""Generate original SVG artwork and a link-driven maze. Python 3, no dependencies.

Game state is (x, y, has_patch); every room filename stores its own state.
Edit this source rather than the generated room Markdown and SVG files.
"""
from collections import deque
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAZE = ("#######", "#S..#E#", "#.#.#.#", "#G#...#", "#...#.#", "##K.G.#", "#######")
START = (1, 1, False)
DIRECTIONS = {"↑ UP": (0, -1), "← LEFT": (-1, 0), "RIGHT →": (1, 0), "↓ DOWN": (0, 1)}
BG, INK, MUTED, LIME, MINT, PINK, PURPLE = "#0c0d16", "#f1f0e7", "#a4a7bd", "#dcff70", "#77f5c1", "#ff729c", "#b4a0ff"


def filename(state):
    x, y, patch = state
    return f"room-{x}-{y}-{int(patch)}.md"


def move(state, direction):
    x, y, patch = state
    dx, dy = direction
    nx, ny = x + dx, y + dy
    if not (0 <= ny < len(MAZE) and 0 <= nx < len(MAZE[ny])):
        return None
    tile = MAZE[ny][nx]
    if tile == "#":
        return None
    if tile == "G":
        return "game-over.md"
    if tile == "E" and patch:
        return "win.md"
    return (nx, ny, patch or tile == "K")


def reachable():
    seen, queue = {START}, deque([START])
    while queue:
        state = queue.popleft()
        for direction in DIRECTIONS.values():
            target = move(state, direction)
            if isinstance(target, tuple) and target not in seen:
                seen.add(target)
                queue.append(target)
    return sorted(seen)


def text(x, y, value, size=14, color=INK, extra=""):
    return (f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" '
            f'font-family="ui-monospace, SFMono-Regular, Consolas, monospace" {extra}>'
            f'{escape(value)}</text>')


def svg(body, width, height, title, description=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
            f'width="{width}" height="{height}" role="img" aria-labelledby="title desc">'
            f'<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>'
            f'{body}</svg>\n')


def player(x, y, animated=False):
    mouth = ('<animate attributeName="d" dur="0.36s" repeatCount="indefinite" '
             'values="M0 0 L11 -9 A14 14 0 1 0 11 9 Z;M0 0 L14 -2 A14 14 0 1 0 14 2 Z;M0 0 L11 -9 A14 14 0 1 0 11 9 Z"/>'
             if animated else "")
    return f'<g transform="translate({x} {y})"><path fill="{LIME}" d="M0 0 L11 -9 A14 14 0 1 0 11 9 Z">{mouth}</path><circle cx="1" cy="-7" r="2" fill="{BG}"/></g>'


def bug(x, y):
    return (f'<g transform="translate({x} {y})" fill="{PINK}">'
            '<path d="M-11 11 V-3 Q-11-13 0-13 Q11-13 11-3 V11 L6 7 L0 11 L-6 7 Z"/>'
            f'<path d="M-6-5 h4 v6 h-4z M2-5 h4 v6 h-4z" fill="{BG}"/></g>')


def board(state=None, tile=42, animated=False):
    parts = []
    for y, row in enumerate(MAZE):
        for x, cell in enumerate(row):
            px, py = x * tile, y * tile
            cx, cy = px + tile / 2, py + tile / 2
            if cell == "#":
                parts.append(f'<rect x="{px+3}" y="{py+3}" width="{tile-6}" height="{tile-6}" rx="6" fill="#171a30" stroke="#424b7d"/>')
            elif cell == "G":
                parts.append(bug(cx, cy))
            elif cell == "K" and not (state and state[2]):
                parts.append(f'<path d="M{cx-4} {cy-12}h8v8h8v8h-8v8h-8v-8h-8v-8h8z" fill="{MINT}"/>')
            elif cell == "E":
                parts.append(f'<rect x="{px+9}" y="{py+7}" width="{tile-18}" height="{tile-14}" rx="3" fill="{PURPLE}"/>')
                parts.append(text(cx, cy+5, "↗", 19, BG, 'text-anchor="middle"'))
            else:
                parts.append(f'<circle cx="{cx}" cy="{cy}" r="2.3" fill="#74798f"/>')
    if animated:
        # Attract-mode runner follows real corridors, avoiding both traps.
        route = [(1,1),(3,1),(3,3),(3,5),(2,5),(3,5),(3,3),(5,3),(5,1),(5,3),(3,3),(3,1),(1,1)]
        path = "M" + " L".join(f"{x*tile+tile/2} {y*tile+tile/2}" for x,y in route)
        parts.append(f'<g class="runner"><animateMotion dur="14s" repeatCount="indefinite" path="{path}" rotate="auto"/>{player(0,0,True)}</g>')
        parts.append(f'<g class="still-runner">{player(tile*1.5,tile*1.5)}</g>')
    elif state:
        parts.append(player(state[0]*tile+tile/2, state[1]*tile+tile/2))
    return "".join(parts)


def hero():
    body = f'''<defs>
      <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#ffffff" stroke-opacity=".035"/></pattern>
      <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse"><path d="M0 0H4" stroke="#000" stroke-opacity=".13"/></pattern>
    </defs>
    <style>.still-runner{{display:none}}.led{{animation:blink 2s steps(2,end) infinite}}@keyframes blink{{50%{{opacity:.35}}}}@media(prefers-reduced-motion:reduce){{.runner{{display:none}}.still-runner{{display:inline}}.led{{animation:none}}}}</style>
    <rect width="960" height="492" rx="20" fill="{BG}"/>
    <rect x="1" y="1" width="958" height="490" rx="19" fill="url(#grid)" stroke="#34364c"/>
    <path d="M32 61H928 M32 427H928" stroke="#34364c"/>
    <circle class="led" cx="43" cy="33" r="5" fill="{LIME}"/>'''
    body += text(59,38,"PLAYER 01 / ANDY1924",13,INK,'letter-spacing="1.5"')
    body += text(920,38,"EST. IN THE TERMINAL",11,MUTED,'text-anchor="end" letter-spacing="1.2"')
    body += text(44,105,"A SMALL PROFILE. A PLAYABLE DETOUR.",11,MUTED,'letter-spacing="1.1"')
    body += text(40,194,"ONE MORE",76,INK,'font-weight="900" letter-spacing="-5"')
    body += text(40,278,"COMMIT.",88,LIME,'font-weight="900" letter-spacing="-6"')
    body += text(45,323,"Chasing ideas. Occasionally chased by bugs.",13,MUTED)
    body += f'<rect x="44" y="355" width="233" height="44" rx="5" fill="{LIME}"/>'
    body += text(62,383,"▶ INSERT COIN",16,BG,'font-weight="bold" letter-spacing="1.5"')
    body += text(293,382,"FREE PLAY / ALWAYS",10,MUTED)
    body += text(743,94,"BUG//CHASE",18,PURPLE,'text-anchor="middle" font-weight="bold" letter-spacing="3"')
    body += f'<g transform="translate(595 111)">{board(animated=True)}</g>'
    body += text(44,462,"FIND THE PATCH",11,MINT,'letter-spacing="1.1"')
    body += text(246,462,"→",15,MUTED)
    body += text(302,462,"DODGE THE BUGS",11,PINK,'letter-spacing="1.1"')
    body += text(505,462,"→",15,MUTED)
    body += text(561,462,"SHIP IT",11,PURPLE,'letter-spacing="1.1"')
    body += text(914,462,"[ CLICK TO START ]",11,LIME,'text-anchor="end"')
    body += '<rect x="1" y="1" width="958" height="490" rx="19" fill="url(#scan)" pointer-events="none"/>'
    return svg(body,960,492,"andy1924 — One more commit","An animated arcade maze. Follow the image link to play BUG//CHASE.")


def room_map(state):
    body = f'<rect width="560" height="426" rx="16" fill="{BG}"/>'
    body += text(24,33,"BUG//CHASE",17,INK,'font-weight="bold" letter-spacing="2"')
    body += text(536,32,"PATCH: " + ("EQUIPPED" if state[2] else "MISSING"),12,MINT if state[2] else MUTED,'text-anchor="end"')
    body += f'<g transform="translate(126 55)">{board(state,44)}</g>'
    for x,label,color in [(28,"● YOU",LIME),(134,"+ PATCH",MINT),(274,"▣ BUG",PINK),(416,"↗ EXIT",PURPLE)]:
        body += text(x,395,label,12,color)
    return svg(body,560,426,"BUG//CHASE maze",f"You are at column {state[0]}, row {state[1]}. Patch {'equipped' if state[2] else 'missing'}.")


def text_map(state):
    return "\n".join(" ".join("@" if (x,y)==state[:2] else {"S":".","K":"." if state[2] else "+","G":"!"}.get(cell,cell) for x,cell in enumerate(row)) for y,row in enumerate(MAZE))


def render_room(state):
    x,y,patch = state
    stem = filename(state).removesuffix(".md")
    labels = {}
    for label,direction in DIRECTIONS.items():
        target = move(state,direction)
        labels[label] = f"[**{label}**]({filename(target) if isinstance(target,tuple) else target})" if target else "· wall ·"
    if MAZE[y][x] == "E":
        message = "**Exit locked.** You brought enthusiasm. The door requires a patch. Find the mint `+`."
    elif MAZE[y][x] == "K":
        message = "**Patch acquired!** Now make it to the purple exit in the top-right corner."
    elif state == START:
        message = "**Your mission:** collect the mint `+` patch, then reach the purple exit. Pink bugs end your run."
    else:
        message = "**Patch equipped.** Reach the purple exit. Watch your next step." if patch else "**Patch missing.** Find the mint `+`. Pink bugs are stationary traps."
    return f'''<!-- Generated by scripts/build_arcade.py. -->
[← Back to profile](../README.md) · **BUG//CHASE** · [Restart](room-1-1-0.md)

{message}

<img src="maps/{stem}.svg" width="400" alt="Maze: you are at column {x}, row {y}; patch {'equipped' if patch else 'missing'}." />

| | {labels['↑ UP']} | |
| :---: | :---: | :---: |
| {labels['← LEFT']} | **● YOU** | {labels['RIGHT →']} |
| | {labels['↓ DOWN']} | |

<details>
<summary>Text map / how to play</summary>

Coordinates count from the top left, starting at 0. You are at **({x}, {y})**.

```text
{text_map(state)}
```

`@` you · `#` wall · `+` patch · `!` bug · `E` exit · `.` corridor

Choose an arrow link to move. Collect the patch before entering the exit.
Every room link stores your position and inventory; moves reload the page.

</details>
'''


def ending(won):
    color = MINT if won else PINK
    headline = "PATCH SHIPPED." if won else "BUG WON THIS ROUND."
    body = f'<rect width="720" height="220" rx="16" fill="{BG}"/>'
    body += text(34,47,"BUG//CHASE / " + ("RUN COMPLETE" if won else "GAME OVER"),13,color,'letter-spacing="2"')
    body += text(30,119,headline,46,color,'font-weight="bold" letter-spacing="-2"')
    body += text(34,170,"You found the fix. You made it out. Nice commit." if won else "A tiny bug. A very dramatic crash. Happens to the best of us.",15,MUTED)
    return svg(body,720,220,headline)


def write(path, content):
    target = ROOT / path
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(content,encoding="utf-8")


def main():
    write("assets/arcade.svg",hero())
    footer = f'<rect width="960" height="76" rx="10" fill="{BG}"/>'
    footer += text(28,44,"END OF PROFILE ≠ END OF GAME",14,MUTED,'letter-spacing="1"')
    footer += text(930,44,"CONTINUE?  ALWAYS.",14,LIME,'text-anchor="end" letter-spacing="1"')
    write("assets/footer.svg",svg(footer,960,76,"End of profile. Not end of game. Continue? Always."))
    for state in reachable():
        write(f"arcade/{filename(state)}",render_room(state))
        write(f"arcade/maps/{filename(state).removesuffix('.md')}.svg",room_map(state))
    for won,name in [(True,"win"),(False,"game-over")]:
        write(f"assets/{name}.svg",ending(won))
        write(f"arcade/{name}.md",f'''<!-- Generated by scripts/build_arcade.py. -->
![{'Patch shipped. You win!' if won else 'Game over. You stepped on a bug.'}](../assets/{name}.svg)

{'**Achievement unlocked: shipped without touching production.** You collected the patch and reached the exit.' if won else '**That pink thing was not a power-up.** Your run is over. Take another route and keep an eye on the map.'}

[**↻ {'Play again' if won else 'Try again'}**](room-1-1-0.md) · [**Explore my repositories ↗**](https://github.com/andy1924?tab=repositories) · [Back to profile](../README.md)
''')
    print(f"Built profile artwork and {len(reachable())} reachable arcade rooms.")


if __name__ == "__main__":
    main()

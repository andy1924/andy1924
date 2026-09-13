"""Validate links/assets and game rules across every reachable room."""
import re
import xml.etree.ElementTree as ET
from collections import deque
from pathlib import Path

from build_arcade import ROOT, START, DIRECTIONS, MAZE, filename, move, reachable


def main():
    documents = [ROOT / 'README.md', *sorted((ROOT / 'arcade').glob('*.md'))]
    links = 0
    for document in documents:
        content = document.read_text()
        targets = re.findall(r'\]\(([^)]+)\)|(?:href|src)="([^"]+)"', content)
        for markdown, html in targets:
            target = markdown or html
            if target.startswith(('https://', '#')):
                continue
            assert (document.parent / target).is_file(), (document, target)
            links += 1
    for asset in [*(ROOT / 'assets').glob('*.svg'), *(ROOT / 'arcade/maps').glob('*.svg')]:
        root = ET.parse(asset).getroot()
        assert root.tag.endswith('svg'), asset
        assert not any(element.tag.endswith(('script', 'foreignObject')) for element in root.iter()), asset

    states = set(reachable())
    assert len(list((ROOT / 'arcade').glob('room-*.md'))) == len(states), 'Stale generated rooms'
    # Explicit regression examples for inventory, trap collision, and the locked exit.
    assert move((3, 5, False), (-1, 0)) == (2, 5, True)
    assert move((2, 5, True), (1, 0)) == (3, 5, True)
    assert move((1, 2, False), (0, 1)) == 'game-over.md'
    assert move((5, 5, True), (-1, 0)) == 'game-over.md'
    assert move((5, 2, False), (0, -1)) == (5, 1, False)
    assert move((5, 2, True), (0, -1)) == 'win.md'
    assert move(START, (-1, 0)) is None

    for state in states:
        document = (ROOT / 'arcade' / filename(state)).read_text()
        for label, direction in DIRECTIONS.items():
            target = move(state, direction)
            if target is None:
                assert f'[**{label}**]' not in document
            else:
                href = filename(target) if isinstance(target, tuple) else target
                assert f'[**{label}**]({href})' in document
                if isinstance(target, tuple):
                    assert target in states
                    assert not state[2] or target[2], 'Patch was lost'
                    assert MAZE[target[1]][target[0]] not in '#G'
                elif target == 'win.md':
                    assert state[2], 'Won without a patch'
        # Any living room must still have a route to victory; no softlocks.
        queue, seen, can_win = deque([state]), {state}, False
        while queue:
            current = queue.popleft()
            for direction in DIRECTIONS.values():
                target = move(current, direction)
                if target == 'win.md':
                    can_win = True
                elif isinstance(target, tuple) and target not in seen:
                    seen.add(target)
                    queue.append(target)
        assert can_win, f'Softlock at {state}'

    # Traverse actual generated Markdown links through a complete run.
    current = ROOT / 'arcade' / filename(START)
    route = ['RIGHT →'] * 2 + ['↓ DOWN'] * 4 + ['← LEFT', 'RIGHT →'] + ['↑ UP'] * 2 + ['RIGHT →'] * 2 + ['↑ UP'] * 2
    for label in route:
        match = re.search(r'\[\*\*' + re.escape(label) + r'\*\*\]\(([^)]+)\)', current.read_text())
        assert match, (current, label)
        current = current.parent / match.group(1)
    assert current.name == 'win.md', current
    print(f'PASS: {len(states)} rooms, {links} local links, valid SVGs, all rooms winnable, {len(route)}-move winning run.')


if __name__ == '__main__':
    main()

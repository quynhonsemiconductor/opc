"""v4.1 — mark everything behind an open modal as `inert` so keyboard focus stays in the dialog.

The mock-ups are static; the build traps focus in the dialog (Radix Dialog does it). In the mock-up, every
sibling of the dialog and of each of its ancestors gets `inert` (probe.mjs --keys: escapesDialog = 0).
Idempotent. Run after any generator that writes a screen with role="dialog" aria-modal="true":
    python3 inert.py            (all screens)   ·   python3 inert.py a.html b.html
"""
import sys, glob, os
from html.parser import HTMLParser

ROOT = os.path.join(os.path.dirname(__file__), '../../apps/app/screens')
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'source', 'track', 'wbr',
        'path', 'circle', 'rect', 'line', 'polyline', 'polygon', 'use', 'ellipse'}
SKIP = {'svg', 'script', 'style', 'template'}


class Tree(HTMLParser):
    def __init__(self, src):
        super().__init__(convert_charrefs=False)
        self.lines = [0]
        for ln in src.splitlines(keepends=True):
            self.lines.append(self.lines[-1] + len(ln))
        self.nodes, self.stack = [], []

    def handle_starttag(self, tag, attrs):
        line, col = self.getpos()
        n = {'tag': tag, 'attrs': dict(attrs), 'pos': self.lines[line - 1] + col,
             'parent': self.stack[-1] if self.stack else None}
        self.nodes.append(n)
        if tag not in VOID:
            self.stack.append(len(self.nodes) - 1)

    def handle_startendtag(self, tag, attrs):
        line, col = self.getpos()
        self.nodes.append({'tag': tag, 'attrs': dict(attrs), 'pos': self.lines[line - 1] + col,
                           'parent': self.stack[-1] if self.stack else None})

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.nodes[self.stack[i]]['tag'] == tag:
                del self.stack[i:]
                break


def fix(path):
    src = open(path, encoding='utf-8').read()
    t = Tree(src); t.feed(src)
    dlg = [i for i, n in enumerate(t.nodes) if n['attrs'].get('role') == 'dialog' and n['attrs'].get('aria-modal') == 'true']
    if not dlg:
        return 0
    body = next(i for i, n in enumerate(t.nodes) if n['tag'] == 'body')
    keep, levels = set(dlg), set()
    for d in dlg:                                   # the dialog and its ancestors (up to <body>) stay live
        i = t.nodes[d]['parent']
        while i is not None:
            keep.add(i); levels.add(i)
            if i == body: break
            i = t.nodes[i]['parent']
    targets = []
    for a in levels:                                 # siblings at each level of the chain go inert
        for i, n in enumerate(t.nodes):
            if n['parent'] == a and i not in keep and n['tag'] not in SKIP and 'inert' not in n['attrs']:
                targets.append(n['pos'] + 1 + len(n['tag']))
    for p in sorted(targets, reverse=True):
        src = src[:p] + ' inert' + src[p:]
    open(path, 'w', encoding='utf-8').write(src)
    return len(targets)


if __name__ == '__main__':
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(ROOT, '*.html')))
    for f in files:
        n = fix(f)
        if n:
            print(f'{os.path.basename(f)}: {n} region(s) inert')

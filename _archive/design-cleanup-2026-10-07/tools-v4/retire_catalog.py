"""v4.1 clean-up: remove retired components from catalog.html (elements, then empty demo wrappers, then empty
sections) and their names from section titles. Usage: python3 retire_catalog.py"""
import re, pathlib
CAT = pathlib.Path(__file__).resolve().parents[2] / 'system' / 'components' / 'catalog.html'
RETIRED = ['c-lane', 'c-lanes', 'c-msign', 'c-msigns', 'c-route', 'c-prod', 'c-prods', 'c-truthbar', 'c-daybars', 'c-spark',
           'c-stamp', 'c-term', 'c-trend', 'c-later', 'c-sheet', 'r-money-hero', 'r-ticket', 'c-coach-anchor', 'r-cart-bar']
VOID = {'img', 'input', 'br', 'hr', 'use', 'path', 'circle', 'rect', 'line', 'polyline', 'polygon', 'meta', 'link', 'source'}
ROOT = re.compile(r'class="(?:[^"]*\s)?(' + '|'.join(map(re.escape, RETIRED)) + r')(?:\s|"|__|--)')


def end_of(s, start, tag):
    depth, i = 0, start
    pat = re.compile(rf'<(/?){tag}\b[^>]*?(/?)>', re.S)
    for m in pat.finditer(s, start):
        if m.group(2):
            continue
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return m.end()
    raise ValueError('unbalanced ' + tag)


def strip_retired(s):
    out, i = [], 0
    for m in re.finditer(r'<([a-z0-9]+)\b[^>]*>', s):
        if m.start() < i:
            continue
        if ROOT.search(m.group(0)):
            tag = m.group(1)
            out.append(s[i:m.start()])
            i = m.end() if tag in VOID or m.group(0).endswith('/>') else end_of(s, m.start(), tag)
    out.append(s[i:])
    return ''.join(out)


s = CAT.read_text()
head, body = s.split('<main', 1)
body = strip_retired(body)
# remove wrappers left empty (only labels / whitespace), repeat until stable
for _ in range(4):
    body = re.sub(r'<div class="(?:surface[^"]*|demo[^"]*|grid\d[^"]*)"[^>]*>\s*(?:<span class="lbl">[^<]*</span>\s*|<p class="lbl">[^<]*</p>\s*)*</div>', '', body)
# titles: drop retired names from "a · b · c" lists
def fix_title(m):
    parts = [p.strip() for p in re.split(r'\s*·\s*', m.group(2))]
    keep = [p for p in parts if not any(re.match(rf'{re.escape(r)}\b', p) for r in RETIRED)]
    return m.group(1) + ' · '.join(keep) + m.group(3)
body = re.sub(r'(<h2 id="s-[^"]+">)(.*?)(</h2>)', fix_title, body)
# sections with no demo left (balanced: sections may contain sections)
out, i = [], 0
for m in re.finditer(r'<section class="sec"[^>]*>', body):
    if m.start() < i:
        continue
    e = end_of(body, m.start(), 'section')
    blk = body[m.start():e]
    inner = re.sub(r'<h2.*?</h2>|<p>.*?</p>|\s', '', blk[len(m.group(0)):-len('</section>')], flags=re.S)
    out.append(body[i:m.start()]); out.append(blk if inner else ''); i = e
out.append(body[i:]); body = ''.join(out)
CAT.write_text(head + '<main' + body)
left = sorted(set(m.group(1) for m in ROOT.finditer(body)))
print('retired left in catalog:', left or 'none')

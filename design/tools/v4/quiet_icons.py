"""v4.5.5 · Icon rule (DESIGN.md §Icons, budgets.md §2): a labelled button carries no verb icon — the verb is written.
Kept, because they carry information the label does not: i-chev (opens a menu), i-lock (blocked until …), and every
icon on an icon-only button. Runs over all screens after the generators, before inert.py. Idempotent.
    python3 quiet_icons.py
"""
import glob, os, re

ROOT = os.path.join(os.path.dirname(__file__), '../../apps/app/screens')
KEEP = {'i-chev', 'i-lock', 'i-arrow-l', 'i-x'}
BTN = re.compile(r'<(a|button)( class="c-btn[^"]*"[^>]*)>(.*?)</\1>', re.S)
SVG = re.compile(r'<svg class="c-ic"[^>]*><use href="#([a-z0-9-]+)"\s*/></svg>')


def quiet(m):
    tag, attrs, inner = m.group(1), m.group(2), m.group(3)
    text = re.sub(r'<[^>]+>', '', SVG.sub('', inner)).strip()
    if not text:                       # icon-only button: the icon is the label
        return m.group(0)
    inner = SVG.sub(lambda s: s.group(0) if s.group(1) in KEEP else '', inner)
    return f'<{tag}{attrs}>{inner}</{tag}>'


n = 0
for f in sorted(glob.glob(os.path.join(ROOT, '*.html'))):
    s = open(f, encoding='utf-8').read()
    out = BTN.sub(quiet, s)
    if out != s:
        n += 1
        open(f, 'w', encoding='utf-8').write(out)
print(f'quiet_icons: {n} screens')

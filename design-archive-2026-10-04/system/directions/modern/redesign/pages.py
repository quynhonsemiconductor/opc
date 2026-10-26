# v4.1 page builder: every restructured screen = the Calm shell of home.html (nav rail, top bar, tab bar) +
# its own <main> + optional overlay + layout-only <style>. Group modules (pages_money.py, …) call build().
import json, re, pathlib

HERE = pathlib.Path(__file__).parent
SCREENS = HERE.parents[3] / 'apps/app/screens'
SYS = HERE.parents[2]
ICONS = {**json.load(open(SYS / 'assets/icons/lucide-map.json')), **json.load(open(SYS / 'assets/icons/lucide-extra.json'))}

def ic(i, cls='c-ic'): return f'<svg class="{cls}" aria-hidden="true"><use href="#{i}"/></svg>'
def sign(k, i, t): return f'<span class="c-sign c-sign--{k}"><span class="c-sign__pic">{ic(i)}</span>{t}</span>'
CUR = '<span class="u-cur">₫</span>'

NAV = {'home': 'home.html', 'orders': 'orders.html', 'money': 'money.html', 'books': 'invoices.html',
       'approvals': 'approvals.html', 'settings': 'settings-users.html'}
TAB = {'home': 'home.html', 'orders': 'orders.html', 'money': 'money.html', 'more': 'home--more.html'}

def shell():
    return (SCREENS / 'home.html').read_text()

def build(name, title, main, current, tab=None, overlay='', style='', body_attrs='', html_attrs=''):
    s = shell()
    # nav current
    s = s.replace(' aria-current="page"', '')
    href = NAV[current]
    s = s.replace(f'<a class="c-nav__item" href="{href}">', f'<a class="c-nav__item" href="{href}" aria-current="page">', 1)
    tab = tab or (current if current in TAB else 'more')
    s = s.replace(f'<a class="c-tabbar__item" href="{TAB[tab]}">', f'<a class="c-tabbar__item" href="{TAB[tab]}" aria-current="page">', 1)
    # main
    a = s.index('<main class="r-shell__content">'); b = s.index('</main>') + len('</main>')
    s = s[:a] + '<main class="r-shell__content">\n' + main.strip('\n') + '\n    </main>' + s[b:]
    if overlay: s = s.replace('</body>', overlay.strip() + '\n</body>')
    if style: s = s.replace('</head>', f'<style>\n/* layout only */\n{style.strip()}\n</style>\n</head>', 1)
    if body_attrs: s = s.replace('<body>', f'<body {body_attrs}>', 1)
    if html_attrs: s = s.replace('<html lang="vi">', f'<html lang="vi" {html_attrs}>', 1)
    s = re.sub(r'<title>[^<]*</title>', f'<title>{title} — OPC</title>', s)
    used = list(dict.fromkeys(re.findall(r'href="#(i-[\w-]+)"', s)))
    missing = [u for u in used if u not in ICONS]
    sprite = '<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">\n' + \
        '\n'.join(f'  <symbol id="{u}" viewBox="0 0 24 24">{ICONS[u]}</symbol>' for u in used if u in ICONS) + '\n</svg>'
    s = re.sub(r'<svg width="0" height="0" style="position:absolute"[^>]*>[\s\S]*?</svg>', lambda m: sprite, s, count=1)
    (SCREENS / f'{name}.html').write_text(s)
    print(name, 'MISSING ' + ','.join(missing) if missing else 'ok')

def subnav(label, items, current):
    return f'<nav class="c-subnav" aria-label="{label}">' + ''.join(
        f'<a class="c-subnav__item" href="{h}"' + (' aria-current="page"' if t == current else '') + f'>{t}</a>' for t, h in items) + '</nav>'

def old_overlay(name):
    """Overlay markup (dialog/drawer) of a v3.1 screen, from the backup."""
    old = (HERE.parents[4] / 'design-backup-v3.1-2026-10-02/apps/app/screens' / f'{name}.html').read_text()
    e = old.index('</nav>', old.index('<nav class="c-tabbar"')) + len('</nav>')
    return old[e:old.index('</body>')].strip()

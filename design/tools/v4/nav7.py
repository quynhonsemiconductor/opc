"""v7.0.0 · apply the ERP menu to every household screen after all generators ran: re-render the rail (navtree) and the phone tab bar
(Tổng quan · Mua · Bán · Kho · Thêm, BA Screen Plan §3). Skips onboarding, the programme and platform consoles. Run before brand.py.  Usage: python3 nav7.py"""
import re, pathlib
import navtree
from pages import ICONS
SCREENS = pathlib.Path(__file__).resolve().parents[2] / 'apps' / 'app' / 'screens'
ic = lambda i: f'<svg class="c-ic" aria-hidden="true"><use href="#{i}"/></svg>'
TABS = [('home', 'Tổng quan', 'home.html', 'i-home', '<span class="c-tabbar__count" aria-label="3 việc cần làm">3</span>'),
        ('buy', 'Mua', 'purchases.html', 'i-download', ''),
        ('orders', 'Bán', 'orders.html', 'i-bag', '<span class="c-tabbar__count" aria-label="3 cần xem">3</span>'),
        ('goods', 'Kho', 'stock.html', 'i-box', ''),
        ('more', 'Thêm', 'home--more.html', 'i-menu', '')]
ROLE = {'shift-close': 'cashier', 'invoices--accountant': 'accountant', 'tax--accountant': 'accountant', 'quick-sale--staff': 'cashier'}


ROLE_TABS = {'cashier': ('home', 'orders', 'more'),   # v7.7: a role sees only the tabs it may use
             'accountant': ('books', 'money', 'more')}
EXTRA_TABS = {'books': ('books', 'Sổ', 'period.html', 'i-book', ''), 'money': ('money', 'Tiền', 'receivables.html', 'i-money', '')}


def tabbar(sec, role=None):
    tabs = TABS
    if role in ROLE_TABS:
        by = {t[0]: t for t in TABS}; by.update(EXTRA_TABS)
        tabs = [by[k] for k in ROLE_TABS[role]]
    keys = [t[0] for t in tabs]
    cur = sec if sec in keys and sec != 'more' else 'more'
    return ('<nav class="c-tabbar" aria-label="Điều hướng nhanh">\n' + ''.join(
        f'  <a class="c-tabbar__item" href="{h}"{" aria-current=" + chr(34) + "page" + chr(34) if k == cur else ""}>{ic(i)}{t}{c}</a>\n' for k, t, h, i, c in tabs) + '</nav>')


def subnav(sec, name):
    """the in-page sub-nav (phone) shows the same children as the rail"""
    kids = next((k for key, _, _, _, k in navtree.SECTIONS + navtree.FOOT if key == sec), [])
    if not kids:
        return ''
    cur = f'{name}.html' if any(h == f'{name}.html' for _, h, _ in kids) else None
    if not cur:
        best = [h for _, h, _ in kids if name.split('--')[0].startswith(h[:-5].split('--')[0].rstrip('s'))]
        cur = max(best, key=len) if best else kids[0][1]
    label = next(l for key, l, _, _, _ in navtree.SECTIONS + navtree.FOOT if key == sec)
    return (f'<nav class="c-subnav" aria-label="{label}">' + ''.join(f'<a class="c-subnav__item" href="{h}"' + (' aria-current="page"' if h == cur else '') + f'>{t}</a>' for t, h, _ in kids) + '</nav>')


def sprite(s):
    used = sorted(set(re.findall(r'href="#(i-[a-z0-9-]+)"', s)))
    sp = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">\n' + '\n'.join(f'  <symbol id="{u}" viewBox="0 0 24 24">{ICONS[u]}</symbol>' for u in used if u in ICONS) + '\n</svg>')
    return re.sub(r'<svg width="0" height="0" style="position:absolute"[^>]*>[\s\S]*?</svg>', lambda m: sp, s, count=1)


n = 0
for p in sorted(SCREENS.glob('*.html')):
    name = p.stem
    if name.startswith(('onboard', 'program', 'platform', '_')):
        continue
    s = o = p.read_text()
    if 'r-shell--program' in s or '<ul class="c-nav__list">' not in s:
        continue
    sec = navtree.section_for(name, None)
    role = next((r for k, r in ROLE.items() if name.startswith(k)), None)
    s = navtree.apply(s, sec, name, role=role)
    s = re.sub(r'<nav class="c-subnav"[^>]*>.*?</nav>', lambda m: subnav(sec, name), s, count=1, flags=re.S)
    if '<nav class="c-tabbar"' in s and 'home--more.html' in s:
        s = re.sub(r'<nav class="c-tabbar"[\s\S]*?</nav>', lambda m: tabbar(sec, role), s, count=1)
    s = sprite(s)
    if s != o:
        p.write_text(s); n += 1
print('nav7: menu applied to', n, 'screens')

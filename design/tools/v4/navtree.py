"""v7.0.0 menu (was v4.4) · The OPC rail as data + renderer (phương án A: current section open with its children; others collapsed with
a peek chevron and the summed count). Shaped by role. Used by pages.build(), home43.py (shell + "Thêm" sheet) and
pages that switch the user (cashier, accountant)."""
import re

ic = lambda i, c='c-ic': f'<svg class="{c}" aria-hidden="true"><use href="#{i}"/></svg>'
#            key          label               landing              icon        children (label, href, count)
# v7.0.0 · menu follows the ERP chain (BA Screen Plan §3, research T16): Tổng quan · Mua hàng · Bán hàng · Hàng hoá và kho · Tiền và chứng từ ·
# Sổ sách và kê khai · Thiết lập. Kết nối lives in Thiết lập; a failing connection is also raised on Tổng quan / Cần xử lý.
# children: (label, href, count) — count may be an int (needs the owner) or ('err', n) (a failure)
SECTIONS = [('home',     'Tổng quan',            'home.html',      'i-home',  [('Hôm nay', 'home.html', None), ('Cần xử lý', 'approvals.html', 3)]),
            ('buy',      'Mua hàng',             'purchases.html', 'i-download',   [('Đơn mua', 'purchases.html', None), ('Nhà cung cấp', 'suppliers.html', None), ('Chi phí', 'purchases--expense.html', None)]),
            ('orders',   'Bán hàng',             'orders.html',    'i-bag',   [('Yêu cầu', 'sales-inbox.html', 3), ('Đơn bán', 'orders.html', None), ('Giao hàng', 'delivery.html', None), ('Khách hàng', 'customers.html', None)]),
            ('goods',    'Kho hàng',             'products.html',  'i-box', [('Hàng và giá', 'products.html', None), ('Tồn kho', 'stock.html', None), ('Kiểm kho', 'stock-count.html', None)]),
            ('money',    'Tiền',                 'money.html',     'i-money', [('Thu chi và đối chiếu', 'money.html', 4), ('Công nợ', 'receivables.html', None), ('Hoá đơn', 'invoices.html', None)]),
            ('books',    'Sổ và kê khai',        'period.html',    'i-book',  [('Kỳ và đối soát', 'period.html', None), ('Kê khai', 'tax.html', None), ('Sổ sách', 'books.html', None), ('Nhật ký', 'audit.html', None)])]
FOOT = [('settings', 'Thiết lập', 'readiness.html', 'i-gear', [('Sẵn sàng', 'readiness.html', None), ('Hộ kinh doanh', 'setup-business.html', None), ('Dữ liệu nền', 'setup-data.html', None),
                                                               ('Người dùng và quyền', 'setup-policy.html', None), ('Kết nối', 'connections.html', ('err', 1)),
                                                               ('Tính năng', 'settings-features.html', None), ('Hiển thị', 'settings-display.html', None)]),
        ('help', 'Trợ giúp và hỗ trợ', 'help.html', 'i-chat', [])]
ROLES = {  # what each role sees (section → allowed child hrefs; None = all)
    'cashier': {'home': ['home.html'], 'orders': ['orders.html'], 'help': None},
    'accountant': {'books': None, 'money': ['receivables.html', 'invoices.html'], 'help': None},
}
ERR_LABEL = lambda n: f'<span class="c-nav__count c-nav__count--err" aria-label="{n} kết nối lỗi">{n}</span>'
COUNT_LABEL = lambda n, what: f'<span class="c-nav__count" aria-label="{n} {what}">{n}</span>'


def _group(key, label, href, icon, kids, cur_sec, cur_child, open_all, peek):
    is_cur = key == cur_sec
    opened = open_all or (is_cur and kids)
    total = sum(n for _, _, n in kids if isinstance(n, int) and n)
    errs = sum(n[1] for _, _, n in kids if isinstance(n, tuple))
    cnt = (ERR_LABEL(errs) if errs else COUNT_LABEL(total, 'việc cần xem') if total else '') if not opened else ''
    if key == 'counter':
        cur = ' aria-current="page"' if is_cur else ''
        return f'<li><a class="c-nav__item c-nav__item--counter" href="{href}"{cur}>{ic(icon)}{label}{ic("i-arrow")}</a></li>'
    if not kids:
        cur = ' aria-current="page"' if is_cur else ''
        own = {'approvals': COUNT_LABEL(3, 'việc: 2 cần chị quyết, 1 lỗi'),
               'connections': '<span class="c-nav__count c-nav__count--err" aria-label="1 kết nối lỗi">1</span>'}.get(key, '')
        return f'<li><a class="c-nav__item" href="{href}"{cur}>{ic(icon)}{label}{own}</a></li>'
    head_cls = 'c-nav__item c-nav__item--here' if is_cur else 'c-nav__item'
    sid = f'nav-{key}' + ('-all' if open_all else '')
    pk = ('' if (open_all or not peek) else
          f'<button class="c-nav__peek" type="button" aria-expanded="{"true" if opened else "false"}" aria-controls="{sid}" aria-label="{"Thu gọn" if opened else "Xem mục con của"} {label}">{ic("i-chev")}</button>')
    items = []
    for t, h, n in kids:
        c = ' aria-current="page"' if (is_cur and h == cur_child) else ''
        badge = ERR_LABEL(n[1]) if isinstance(n, tuple) else COUNT_LABEL(n, 'việc cần xem') if n else ''
        items.append(f'<li><a class="c-nav__subitem" href="{h}"{c}>{t}{badge}</a></li>')
    sub = f'<ul class="c-nav__sub" id="{sid}"{"" if opened else " hidden"}>{"".join(items)}</ul>'
    return (f'<li class="c-nav__grp{" c-nav__grp--open" if opened else ""}"><div class="c-nav__row"><a class="{head_cls}" href="{href}">{ic(icon)}{label}{cnt}</a>{pk}</div>{sub}</li>')


def lists(cur_sec, cur_child=None, role=None, open_all=False, peek=True):
    allow = ROLES.get(role)

    def keep(sec):
        out = []
        for key, label, href, icon, kids in sec:
            if allow is not None:
                if key not in allow:
                    continue
                if allow[key] is not None:
                    kids = [k for k in kids if k[1] in allow[key]]
                    href = kids[0][1] if kids else href
                    if len(kids) == 1:   # v4.4.1: a lone child is shown flat, under its own name
                        label, kids = kids[0][0], []
                        if cur_child != href:
                            key = key + ':other'
            out.append(_group(key, label, href, icon, kids, cur_sec, cur_child, open_all, peek))
        return ''.join(out)
    return f'<ul class="c-nav__list">{keep(SECTIONS)}</ul>\n    <ul class="c-nav__list c-nav__list--foot">{keep(FOOT)}</ul>'


# v7.0.0 · which section a page belongs to (prefix of the page name → section), so detail pages light the right group
PREFIX = [('quick-sale', 'orders'), ('customer-statement', 'money'), ('purchase', 'buy'), ('supplier', 'buy'), ('sales-inbox', 'orders'), ('order', 'orders'), ('deliver', 'orders'), ('customer', 'orders'), ('counter', 'orders'),
          ('product', 'goods'), ('pricelist', 'goods'), ('stock', 'goods'), ('money', 'money'), ('receivable', 'money'), ('receipt', 'money'), ('invoice', 'money'),
          ('shift', 'money'), ('period', 'books'), ('tax', 'books'), ('books', 'books'), ('audit', 'books'), ('readiness', 'settings'), ('setup', 'settings'),
          ('settings', 'settings'), ('connections', 'settings'), ('approvals', 'home'), ('home', 'home'), ('help', 'help')]
ALIAS = {'connections': 'settings', 'approvals': 'home', 'counter': 'orders'}


def section_for(page_name, fallback=None):
    for p, sec in PREFIX:
        if page_name and page_name.startswith(p):
            return sec
    return ALIAS.get(fallback, fallback)


def section_of(href):
    for key, label, landing, icon, kids in SECTIONS + FOOT:
        if href == landing or any(h == href for _, h, _ in kids):
            return key
    return None


def apply(s, cur_sec, page_name=None, role=None):
    """Re-render the rail inside a full page (keeps brand + household switcher)."""
    cur_sec = section_for(page_name, cur_sec)
    m = re.search(r'<nav class="c-subnav[^"]*"[^>]*>.*?</nav>', s, re.S)
    child = None
    if m:
        c = re.search(r'href="([^"]+)" aria-current="page"', m.group(0))
        child = c.group(1) if c else None
    if not child and page_name:
        for key, _, _, _, kids in SECTIONS + FOOT:
            for _, h, _ in kids:
                if h == f'{page_name}.html':
                    child, cur_sec = h, key
    if cur_sec and page_name and (child is None or not any(h == child for k, _, _, _, kids in SECTIONS + FOOT if k == cur_sec for _, h, _ in kids)):
        child = None
        for key, _, _, _, kids in SECTIONS + FOOT:   # v7: a detail page lights the child it belongs to (order-detail → Đơn bán)
            if key == cur_sec:
                best = [h for _, h, _ in kids if page_name.split('--')[0].startswith(h[:-5].split('--')[0].rstrip('s'))]
                child = max(best, key=lambda h: (len(h[:-5].split('--')[0]), '--' not in h)) if best else None   # a base list beats its '--' variant
    if cur_sec and child is None:
        for key, _, landing, _, kids in SECTIONS + FOOT:
            if key == cur_sec and kids:
                child = landing
    new = lists(cur_sec, child, role)
    return re.sub(r'<ul class="c-nav__list">[\s\S]*?</ul>\s*<ul class="c-nav__list(?: c-nav__list--foot)?">[\s\S]*?</ul>(?=\s*</nav>)', lambda _: new, s, count=1)

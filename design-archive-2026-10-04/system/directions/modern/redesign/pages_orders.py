# v4.1 · Đơn hàng group: orders + 9 states. Usage: python3 pages_orders.py
# Keeps the data-table pattern (scan, filter, bulk select are the jobs) but: Calm shell; a first-read money head
# (đã thu figure + truth bar + chưa thu link); 9 columns → 5 (who · payment · status · invoice · total), the
# customer first with code/time/channel/items as one sub-line, the total as the dominant right figure.
import re, pathlib
from pages import build, ic, CUR, SCREENS

HEAD = f'''<section class="r-listhead" aria-label="Tiền của đơn hôm nay">
          <div class="r-listhead__fig"><span class="c-stat__label">Đã thu hôm nay</span><b class="c-figure">8.460.000{CUR}</b></div>
          <div class="r-listhead__bar"><div class="c-split__bar" role="img" aria-label="Đã xác minh 4.560.000 ₫, chờ xác minh 1.380.000 ₫, tiền mặt 2.520.000 ₫"><i class="c-split__ok" style="flex:4560"></i><i class="c-split__pend" style="flex:1380"></i><i class="c-split__cash" style="flex:2520"></i></div>
            <p class="c-sub">đã xác minh 4.560.000 ₫ · chờ 1.380.000 ₫ · tiền mặt 2.520.000 ₫</p></div>
          <a class="r-listhead__due" href="#due"><span class="c-stat__label">Chưa thu · 2 đơn <span class="r-listhead__late">1 quá hạn</span></span><span class="r-listhead__duev">5.570.000{CUR}</span>{ic('i-chev-r')}</a>
        </section>'''

def cells(tr):
    return re.findall(r'<td([^>]*)>(.*?)</td>', tr, re.S)

def row(tr):
    attrs = re.match(r'<tr([^>]*)>', tr).group(1)
    c = cells(tr)
    check = ''
    if c and 'c-check' in c[0][1]:
        check = f'<td class="c-table__cell--hide c-table__cell--check">{c[0][1]}</td>'; c = c[1:]
    if len(c) < 9: return tr
    code, time, who, chan, items, total, pay, status, inv = [x[1].strip() for x in c[:9]]
    if 'c-skel' in code:   # loading skeleton
        sk = lambda w: f'<span class="c-skel c-skel--line {w}"></span>'
        return (f'<tr{attrs}>{check}<td class="c-table__cell--main c-table__who">{sk("u-skw5")}{sk("u-skw4")}</td><td class="c-table__cell--hide">{sk("u-skw3")}</td>'
                f'<td class="c-table__cell--wide">{sk("u-skw5")}</td><td class="c-table__cell--hide c-table__cell--opt">{sk("u-skw4")}</td><td class="c-table__num c-table__cell--end">{sk("u-skw4")}</td></tr>')
    name = re.split(r'<span', who, maxsplit=1)[0].strip()
    sr = re.search(r'<span class="u-sr">.*?</span>', who)
    sub = f'{code} · {time} · {chan} · {items} món'
    return (f'<tr{attrs}>{check}<td class="c-table__cell--main c-table__who"><b>{name}</b><small>{sub}</small>{sr.group(0) if sr else ""}</td>'
            f'<td class="c-table__cell--hide">{pay}</td><td class="c-table__cell--wide">{status}</td>'
            f'<td class="c-table__cell--hide c-table__cell--opt">{inv}</td><td class="c-table__num c-table__cell--end">{total}</td></tr>')

def thead(old):
    check = re.search(r'<th><label class="c-check">.*?</label></th>', old, re.S)
    return ('<thead><tr>' + (check.group(0) if check else '') + '<th>Khách · đơn</th><th>Thanh toán</th><th>Trạng thái</th>'
            '<th class="c-table__cell--opt">Hoá đơn</th><th class="c-table__num">Tổng</th></tr></thead>')

def transform(name):
    s = (pathlib.Path(__file__).parent / 'src_v40' / f'{name}.html').read_text()   # pristine v4.0 copy
    style = re.search(r'<style>([\s\S]*?)</style>', s); style = style.group(1).replace('/* layout only */', '') if style else ''
    mo = re.search(r'<main class="r-shell__content"[^>]*>', s); main = s[mo.end():s.index('</main>')]
    after = s[s.index('</nav>', s.index('<nav class="c-tabbar"')) + len('</nav>'):s.index('</body>')].strip()
    if 'class="r-listhead"' not in main:
        main = re.sub(r'<p class="c-say">Đã thu <b>8\.460\.000 ₫</b>[^<]*<b>5\.570\.000 ₫</b>[^<]*</p>', HEAD, main, count=1)
    main = main.replace('<p class="r-page-head__sub u-meta">', '<p class="c-sub">')
    if '<table' in main:
        main = re.sub(r'<thead>.*?</thead>', lambda m: thead(m.group(0)), main, count=1, flags=re.S)
        tb = re.search(r'<tbody>(.*?)</tbody>', main, re.S)
        rows = re.sub(r'<tr[^>]*>.*?</tr>', lambda m: row(m.group(0)), tb.group(1), flags=re.S)
        main = main[:tb.start(1)] + rows + main[tb.end(1):]
        main = main.replace('id="due"', '')
        main = re.sub(r'(<tr class="c-table__row--you[^"]*")(>.*?DH-1040)', r'\1 id="due"\2', main, count=1, flags=re.S)
    main = main.replace('<section class="c-card" aria-label="Danh sách đơn hàng">', '<section class="c-card r-listcard" aria-label="Danh sách đơn hàng">')
    title = re.search(r'<title>(.*?) — OPC</title>', s).group(1)
    build(name, title, main, 'orders', overlay=after, style=style)

for n in ['orders', 'orders--search', 'orders--filters', 'orders--daterange', 'orders--filtered', 'orders--noresult',
          'orders--loading', 'orders--peek', 'orders--bulk', 'orders--bulk--preview']:
    transform(n)

# the loading state keeps aria-busy on <main>
p = SCREENS / 'orders--loading.html'
p.write_text(p.read_text().replace('<main class="r-shell__content">', '<main class="r-shell__content" aria-busy="true">', 1))

# v4.1 r2: the table already shows status as a labelled pill — drop the unlabelled 3-bar money line from rows
import re as _re
for n in ['orders', 'orders--search', 'orders--filters', 'orders--daterange', 'orders--filtered', 'orders--noresult',
          'orders--bulk', 'orders--bulk--preview', 'orders--peek', 'orders--loading', 'orders--empty', 'orders--error']:
    p = SCREENS / f'{n}.html'
    if p.exists():
        p.write_text(_re.sub(r'<span class="c-moneyline"[^>]*><s></s><s></s><s></s></span>', '', p.read_text()))

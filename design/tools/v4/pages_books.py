# v4.1 · Sổ & thuế group: invoices, invoices--accountant (+ invoice-detail, receipt via pages_detail.detail).
# Usage: python3 pages_books.py
import re, pathlib
from pages import build, ic, CUR
from pages_detail import detail

SRC = pathlib.Path(__file__).parent / 'src_v40'

def head(fig_k, fig, parts, aria, due_k, due_v, due_href):
    bar = ''.join(f'<i class="c-split__{k}" style="flex:{n}"></i>' for k, n, _ in parts)
    sub = ' · '.join(t for _, _, t in parts)
    return f'''<section class="r-listhead" aria-label="Hoá đơn trong kỳ">
          <div class="r-listhead__fig"><span class="c-stat__label">{fig_k}</span><b class="c-figure">{fig}</b></div>
          <div class="r-listhead__bar"><div class="c-split__bar" role="img" aria-label="{aria}">{bar}</div><p class="c-sub">{sub}</p></div>
          <a class="r-listhead__due" href="{due_href}"><span class="c-stat__label">{due_k}</span><span class="r-listhead__duev">{due_v}</span></a>
        </section>'''

def row(tr):
    attrs = re.match(r'<tr([^>]*)>', tr).group(1)
    c = [x.strip() for x in re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)]
    if len(c) < 8: return tr
    num, order, time, buyer, total, kind, cqt, view = c[:8]
    name = re.split(r'<span', buyer, maxsplit=1)[0].strip()
    return (f'<tr{attrs}><td class="c-table__cell--main c-table__who"><b>{num}</b><small>{order} · {time} · {kind}</small></td>'
            f'<td class="c-table__cell--wide">{name}</td><td class="c-table__cell--wide">{cqt}</td>'
            f'<td class="c-table__num c-table__cell--end">{total}</td><td class="c-table__cell--hide">{view}</td></tr>')

THEAD = '<thead><tr><th>Hoá đơn</th><th>Người mua</th><th>Mã CQT</th><th class="c-table__num">Tổng</th><th><span class="u-sr">Xem</span></th></tr></thead>'

def list_page(name, listhead, drop_say=True):
    s = (SRC / f'{name}.html').read_text()
    style = re.search(r'<style>([\s\S]*?)</style>', s); style = style.group(1).replace('/* layout only */', '') if style else ''
    mo = re.search(r'<main class="r-shell__content"[^>]*>', s); main = s[mo.end():s.index('</main>')]
    after = s[s.index('</nav>', s.index('<nav class="c-tabbar"')) + len('</nav>'):s.index('</body>')].strip()
    main = re.sub(r'\s*<p class="u-meta">Ký hiệu <b>2C26MCH</b>.*?</p>', '', main, count=1, flags=re.S)
    main = main.replace('<p class="r-page-head__sub c-conn">', '<p class="c-sub">')
    main = main.replace('<div class="page">', '<div class="page">\n        ' + listhead, 1)
    if drop_say:  # say it once: the reassurance moves into the banner
        say = re.search(r'\s*<p class="c-say">(Hoá đơn chờ mã vẫn đưa khách được[^<]*)</p>', main)
        if say:
            main = main.replace(say.group(0), '')
            main = main.replace('OPC đã gửi lại lúc 10:20.</span>', 'OPC đã gửi lại lúc 10:20. Hoá đơn vẫn đưa khách được.</span>', 1)
    main = re.sub(r'<thead>.*?</thead>', THEAD, main, count=1, flags=re.S)
    tb = re.search(r'<tbody>(.*?)</tbody>', main, re.S)
    main = main[:tb.start(1)] + re.sub(r'<tr[^>]*>.*?</tr>', lambda m: row(m.group(0)), tb.group(1), flags=re.S) + main[tb.end(1):]
    main = main.replace('<section class="c-card" aria-label="Danh sách hoá đơn">', '<section class="c-card r-listcard" aria-label="Danh sách hoá đơn">')
    main = re.sub(r'(<tr class="c-table__row--you")', r'\1 id="due"', main, count=1)
    title = re.search(r'<title>(.*?) — OPC</title>', s).group(1)
    build(name, title, main, 'books', overlay=after, style=style)

list_page('invoices', head('Tháng 10/2026 · 19 hoá đơn', f'7.080.000{CUR}',
          [('ok', 18, 'có mã CQT 18'), ('pend', 1, 'chờ mã 1')], 'Có mã CQT 18 hoá đơn, chờ mã 1 hoá đơn',
          'Chờ mã CQT · 25 phút', 'HĐ 00000418 · 640.000' + CUR, '#due'))
list_page('invoices--accountant', head('Tháng 9/2026 · ký hiệu 2C26MCH', '212 hoá đơn',
          [('ok', 211, 'có mã CQT 211'), ('err', 1, 'bị từ chối 1')], 'Có mã CQT 211 hoá đơn, bị từ chối 1 hoá đơn',
          'Bị từ chối · cần xác nhận', 'HĐ 00000163', '#'))
detail('invoice-detail', 'books', f'<p class="r-detail__fig"><b class="c-figure">640.000{CUR}</b><span class="c-sub">DH-1036 · Anh Tuấn · 02/10/2026 08:34 · ký hiệu 2C26MCH</span></p>')
detail('receipt', 'orders', f'<p class="r-detail__fig"><b class="c-figure">1.020.000{CUR}</b><span class="c-sub"><span class="c-sign c-sign--ok"><span class="c-sign__pic">'+ic('i-check')+'</span>Đã xác minh · QR</span> hoá đơn 00000422 · 02/10/2026 10:47</span></p>')

# v4.1 polish: long CQT codes show only the significant tail ("…0421"); full code for screen readers and on hover
def _short(m):
    code = m.group(1)
    return (f'<span class="c-table__desk" title="{code}"><span class="u-sr">{code[:-4]}</span>'
            f'<span aria-hidden="true">…</span>{code[-4:]}</span>')
for _n in ['invoices', 'invoices--accountant']:
    _p = SCREENS / f'{_n}.html' if 'SCREENS' in globals() else pathlib.Path(__file__).resolve().parents[2] / 'apps/app/screens' / f'{_n}.html'
    _s = _p.read_text()
    _p.write_text(re.sub(r'<span class="c-table__desk">(M1-[A-Z0-9-]+)</span>', _short, _s))

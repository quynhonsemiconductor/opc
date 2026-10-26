"""v4.2 · Sổ & thuế → Đối chiếu kỳ + Sổ sách (BA UI-14, FLOWS.md ⑤ steps 1–4; CEO report B09/B24). An Nhiên data.
Writes period.html (Q III/2026: three sources + 5 to-dos, lock gate locked), period--item.html (drawer: one
exception handled in place), period--ready.html (07/10: all clean, decisions with who), books.html (sổ doanh thu,
built from orders/invoices/bank). Usage: python3 pages_period.py"""
import re
from pages import build, ic, sign, subnav, annhien, SCREENS

CUR = '<span class="u-cur">₫</span>'


def sub(cur):
    return subnav('Sổ & thuế', [('Kỳ thuế', 'period.html'), ('Sổ sách', 'books.html'), ('Hoá đơn', 'invoices.html'), ('Nhật ký', 'audit.html')], cur)


def finish(name, clock=None):
    p = SCREENS / f'{name}.html'
    annhien(p)
    s = p.read_text().replace('class="c-nav__item" href="invoices.html"', 'class="c-nav__item" href="period.html"')
    if clock:
        s = s.replace('Đã lưu 10:45', f'Đã lưu {clock}').replace('Đã lưu · <b>10:45</b>', f'Đã lưu · <b>{clock}</b>')
    p.write_text(s)


def recon(rows):
    out = ''.join(f'<li class="r-recon__r{" r-recon__r--base" if base else ""}"><span class="r-recon__k"><b>{k}</b><small>{m}</small></span>'
                  f'<span class="r-recon__v">{v}</span><span class="r-recon__d">{d}</span></li>' for k, m, v, d, base in rows)
    return f'<ul class="r-recon" aria-label="Ba nguồn">{out}</ul>'


def gate_item(tone, icon, st, t, m, amt, act, href='#', who='', gid=''):
    w = f'<small class="r-gate__who">{who}</small>' if who else ''
    a = f'<a class="c-btn" href="{href}">{act}</a>' if act else ''
    idattr = f' id="{gid}"' if gid else ''
    return (f'<li class="r-gate__i r-gate__i--{tone}"{idattr}><span class="r-gate__b"><b>{t}</b>'
            f'<small><span class="r-gate__st">{st}</span> · {m}</small>{w}</span>'
            f'<span class="r-gate__amt">{amt}</span><span class="r-gate__act">{a}</span></li>')


def tl(items):
    return '<ol class="c-timeline c-timeline--quiet" aria-label="Diễn biến kỳ">' + ''.join(
        f'<li class="c-timeline__item c-timeline__item--{k}"><span class="c-timeline__time">{t}</span><span class="c-timeline__dot" aria-hidden="true"></span>'
        f'<span class="c-timeline__body"><span class="c-timeline__src">{s}</span><span class="c-timeline__what">{w}</span>'
        + (f'<span class="c-timeline__who">{d}</span>' if d else '') + '</span></li>' for k, t, s, w, d in items) + '</ol>'


def tabs(sel):
    return ('<div class="c-tabs" role="tablist" aria-label="Kỳ thuế">' + ''.join(
        f'<a class="c-tabs__tab" role="tab" aria-selected="{"true" if n == sel else "false"}" href="{h}">{n}' + (f' <span class="c-tabs__count">{c}</span>' if c else '') + '</a>'
        for n, h, c in [('Quý III/2026', 'period.html', ''), ('Quý IV/2026', '#', 'đang thu'), ('Quý II/2026', '#', 'đã đóng')]) + '</div>')


def page(name, state, subline, recon_rows, gate_title, items, done, gate, timeline, overlay=None, clock=None, primary=''):
    m = (f'\n      {sub("Kỳ thuế")}\n      <div class="page">{tabs("Quý III/2026")}'
         '<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">Quý III/2026 · đối chiếu ' + state + '</h1>'
         f'<p class="r-detail__fig"><span class="c-sub">{subline}</span></p></div>'
         f'<div class="r-detail__acts">{primary}</div></div>'
         '<div class="r-detail__grid r-detail--calm"><div class="stack">'
         f'<section class="c-card" aria-labelledby="gt"><div class="c-card__head"><h2 class="c-card__title" id="gt">{gate_title}</h2></div>'
         f'<ul class="r-gate">{items}</ul>'
         f'<details class="r-gate__done"><summary>{done[0]}</summary><ul class="r-gate">{done[1]}</ul></details>'
         f'<div class="r-gate__foot">{gate}</div></section></div>'
         '<aside class="r-tower__detail" aria-labelledby="src"><h2 class="r-tower__t" id="src">Ba nguồn có khớp không</h2>' + recon(recon_rows)
         + '<h2 class="r-tower__t r-rail__h2" id="who">Diễn biến kỳ</h2>' + timeline + '</aside></div></div>')
    build(name, 'Sổ & thuế · Đối chiếu Quý III/2026', m, 'books', overlay=overlay)
    finish(name, clock)


OK = lambda t='Khớp': sign('ok', 'i-check', t)
SRC_OPEN = [
    ('Doanh thu đã giao', '01/07–30/09', f'338.400.000{CUR}', '', True),
    ('Hoá đơn bán ra', 'hoá đơn điện tử + máy tính tiền', f'337.100.000{CUR}', sign('err', 'i-x', 'Thiếu 1.300.000 ₫') + ' <a class="r-recon__go" href="#g1">việc 1</a>', False),
    ('Trên cổng thuế', 'bảng kê tải tay 05/10', f'337.760.000{CUR}', sign('err', 'i-x', 'Thiếu 640.000 ₫') + ' <a class="r-recon__go" href="#g2">việc 2</a>', False),
    ('Tiền', 'đã thu + phải thu', f'338.400.000{CUR}', OK('Khớp') + ' <a class="r-recon__go" href="#g3">việc 3</a>', False),
]
GATE_OPEN = ''.join([
    gate_item('you', 'i-invoice', 'Thiếu hoá đơn', 'DH-2036 · Homestay Mây Ngàn', 'giao 28/09 · đã thu', '1.300.000 ₫', 'Tìm hoá đơn', 'order-detail--invoice.html', gid='g1'),
    gate_item('unk', 'i-clock', 'Chưa rõ kết quả', 'HĐ bán lẻ 00001172 · khách lẻ', 'bên hoá đơn máy tính tiền chưa trả kết quả từ 30/09', '640.000 ₫', 'Hỏi lại bên hoá đơn', gid='g2'),
    gate_item('you', 'i-transfer', 'Chưa gán', '2 khoản tiền về', '25/09, 29/09 · không mã đơn', '2.150.000 ₫', 'Gán', 'money--assign.html', gid='g3'),
    gate_item('you', 'i-file', 'Chưa có trong sổ', 'Hoá đơn mua vào · Điện lực Gia Lai', 'tiền điện tháng 8', '1.180.000 ₫', 'Xử lý', 'period--item.html'),
    gate_item('wait', 'i-banknote', 'Chờ chị Lan', 'Xăng xe tháng 9 · không hoá đơn', '4 biên lai · từ 05/10', '3.200.000 ₫', ''),
])
DONE = ('4 mục đã khớp', ''.join([
    gate_item('ok', 'i-box', 'Khớp', 'Kiểm kê cuối kỳ', '30/09 · anh Khoa · khớp sổ', '', ''),
    gate_item('ok', 'i-file', 'Khớp', 'Hoá đơn mua vào HTX Cao Nguyên', '6 hoá đơn · khớp đơn mua và tiền đã trả', '', ''),
    gate_item('ok', 'i-people', 'Khớp', 'Công nợ khách', 'Sunrise 8.400.000 ₫ khớp bảng kê', '', ''),
    gate_item('ok', 'i-bag', 'Khớp', 'Doanh thu qua sàn', 'không có trong kỳ', '', ''),
]))
TL_OPEN = tl([('ai', '05/10', 'Chị Lan', 'Tải bảng kê từ cổng thuế', ''),
              ('ok', '01/10', 'OPC kiểm tra', 'Mở đối chiếu Quý III', ''),
              ('ok', '30/09', 'Anh Khoa', 'Kiểm kê cuối kỳ · khớp', '')])
RESULT = ('<p class="c-decide__result">Khoá kỳ: số liệu đứng yên, mở lại cần duyệt</p>')
GATE_LOCKED = (RESULT + '<div class="c-decide__acts"><button class="c-btn" type="button">Nhắn chị Lan</button><a class="c-btn c-btn--quiet" href="books.html">Xem sổ</a></div>')
P_LOCKED = f'<button class="c-btn c-btn--act" type="button" aria-disabled="true">{ic("i-lock")}Gửi chị An khoá kỳ</button>'
SUBLINE = '<b>Hạn khai 31/10 · còn 25 ngày</b>'
page('period', sign('you', 'i-alert', 'Cần xem'), SUBLINE, SRC_OPEN, 'Trước khi khoá kỳ · 5 việc', GATE_OPEN, DONE, GATE_LOCKED, TL_OPEN, primary=P_LOCKED)

# ---------------- drawer: one exception handled in place ----------------
DRW = ('<div class="c-drawer c-drawer--wide"><div class="c-drawer__panel" role="dialog" aria-modal="true" aria-labelledby="it-t">'
       f'<div class="c-drawer__head"><div><span class="c-drawer__k">Có trên cổng thuế, chưa có trong sổ</span><h2 class="c-drawer__title" id="it-t" tabindex="-1">Hoá đơn mua vào · Điện lực Gia Lai</h2></div>'
       f'<a class="c-icon-btn" href="period.html" aria-label="Đóng, chưa lưu">{ic("i-x")}</a></div>'
       '<div class="c-drawer__body"><p class="r-drawer__fig"><b class="c-figure">1.180.000' + CUR + '</b><span class="c-sub">tiền điện kỳ 08/2026</span></p><dl class="c-kv"><dt>Hoá đơn</dt><dd>0045821 · ngày 08/09/2026</dd><dt>Người bán</dt><dd>Điện lực Gia Lai · MST 0300942001-012</dd>'
       '<dt>Mã khách hàng</dt><dd>PC12GL0034567</dd><dt>Nguồn</dt><dd>bảng kê cổng thuế chị Lan tải 05/10</dd></dl>'
       '<p class="c-decide__q" id="q-it">Ghi khoản này thế nào?</p>'
       '<div class="c-options" role="radiogroup" aria-labelledby="q-it">'
       '<button class="c-option c-option--best" type="button" role="radio" aria-checked="true"><span class="c-option__radio" aria-hidden="true"></span><span class="c-option__body">'
       '<span class="c-option__tag c-option__tag--best">Trợ lý gợi ý</span><strong class="c-option__title">Ghi chi phí điện, tháng 9</strong>'
       '<span class="c-option__meta">Cùng mã khách hàng với tiền điện tháng 9 (1.250.000 ₫) · đã trả 10/09 từ tài khoản MB</span></span></button>'
       '<button class="c-option" type="button" role="radio" aria-checked="false"><span class="c-option__radio" aria-hidden="true"></span><span class="c-option__body">'
       '<strong class="c-option__title">Đã ghi ở khoản khác</strong><span class="c-option__meta">Chọn khoản chi đã có để gắn hoá đơn vào</span></span></button>'
       '<button class="c-option" type="button" role="radio" aria-checked="false"><span class="c-option__radio" aria-hidden="true"></span><span class="c-option__body">'
       '<strong class="c-option__title">Không phải của hộ</strong><span class="c-option__meta">Báo chị Lan · hoá đơn lập nhầm MST</span></span></button></div></div>'
       '<div class="c-drawer__foot"><p class="c-decide__result">Lưu = ghi chi phí điện tháng 9, gắn hoá đơn · OPC chạy lại kiểm tra → <b>còn 4 việc</b></p>'
       '<button class="c-btn c-btn--act" type="button">Lưu quyết định</button></div></div></div>')
page('period--item', sign('you', 'i-alert', 'Cần xem'), SUBLINE, SRC_OPEN, 'Trước khi khoá kỳ · 5 việc', GATE_OPEN, DONE, GATE_LOCKED, TL_OPEN, overlay=DRW, primary=P_LOCKED)

# ---------------- ready (07/10) ----------------
SRC_READY = [
    ('Doanh thu đã giao', '01/07–30/09', f'338.400.000{CUR}', '', True),
    ('Hoá đơn bán ra', 'hoá đơn điện tử + máy tính tiền', f'338.400.000{CUR}', OK(), False),
    ('Trên cổng thuế', 'tải lại 07/10', f'338.400.000{CUR}', OK(), False),
    ('Tiền', 'đã thu + phải thu', f'338.400.000{CUR}', OK(), False),
]
GATE_READY = ''.join([
    gate_item('ok', 'i-invoice', 'Đã xử lý', 'DH-2036 · gắn HĐ 00000201', 'lập 28/09 · hoá đơn điện tử', '1.300.000 ₫', '', who='Anh Khoa · 07/10 08:10'),
    gate_item('ok', 'i-clock', 'Đã xử lý', 'HĐ bán lẻ 00001172 · đã có mã', 'đã có mã từ 30/09', '640.000 ₫', '', who='OPC kiểm tra · 06/10 11:20'),
    gate_item('ok', 'i-transfer', 'Đã xử lý', '2 khoản tiền → DH-2029, DH-2033', 'gán theo số tiền, người chuyển', '2.150.000 ₫', '', who='Anh Khoa · 06/10 11:32'),
    gate_item('ok', 'i-file', 'Đã xử lý', 'Điện tháng 8 → chi phí tháng 9', 'anh Khoa chọn', '1.180.000 ₫', '', who='Anh Khoa · 06/10 11:35'),
    gate_item('ok', 'i-banknote', 'Đã xử lý', 'Xăng xe tháng 9 → chi phí, kèm bảng kê', '4 biên lai đính kèm', '3.200.000 ₫', '', who='Chị Lan · 07/10 08:40'),
])
GATE_OK = (RESULT + '<p class="c-decide__who">Chị An hoặc chị Lan bấm khoá · anh Khoa gửi đề nghị</p>'
           '<div class="c-decide__acts"><a class="c-btn c-btn--quiet" href="books.html">Xem sổ</a></div>')
P_OK = '<button class="c-btn c-btn--act" type="button">Gửi chị An khoá kỳ</button>'
TL_READY = tl([('now', '07/10', 'OPC kiểm tra', 'Chạy lại: ba nguồn khớp · 0 việc', 'kỳ Sẵn sàng khoá'),
               ('ok', '07/10', 'Chị Lan', 'Ghi xăng xe kèm bảng kê · tải lại bảng kê cổng thuế', ''),
               ('ok', '06/10', 'Anh Khoa', 'Xử lý 3 việc', ''),
               ('ok', '01/10', 'OPC kiểm tra', 'Mở đối chiếu Quý III', '')])
page('period--ready', OK('Sẵn sàng khoá'), 'Hạn khai 31/10 · còn 24 ngày · 07/10 08:45', SRC_READY, 'Đã xử lý 5 việc', GATE_READY, DONE, GATE_OK, TL_READY, clock='08:45', primary=P_OK)


# ---------------- books: sổ doanh thu ----------------
who = lambda n, m: f'<td class="c-table__cell--main c-table__who"><b>{n}</b><small>{m}</small></td>'
ROWS = ''.join([
    '<tr>' + '<td>30/09</td>' + who('Bán nhanh · 23 hoá đơn máy tính tiền', 'HĐ 00001149–00001171') + '<td class="c-table__num">5.120.000 ₫</td>' + '<td class="r-book__ok">' + ic('i-check') + 'có mã</td></tr>',
    '<tr class="c-table__row--you">' + '<td>30/09</td>' + who('HĐ bán lẻ 00001172 · khách lẻ', '2 gói bò, 2 hũ muối') + '<td class="c-table__num">640.000 ₫</td>' + f'<td>{sign("unk", "i-clock", "Chưa rõ kết quả")}</td></tr>',
    '<tr class="c-table__row--you">' + '<td>28/09</td>' + who('DH-2036 · Homestay Mây Ngàn', 'đã giao · đã thu chuyển khoản') + '<td class="c-table__num">1.300.000 ₫</td>' + f'<td>{sign("you", "i-alert", "Thiếu hoá đơn")}</td></tr>',
    '<tr>' + '<td>25/09</td>' + who('HĐ 00000199 · Nhà hàng Phố Núi', 'DH-2031 · 3 gói bò một nắng') + '<td class="c-table__num">690.000 ₫</td>' + '<td class="r-book__ok">' + ic('i-check') + 'có mã</td></tr>',
    '<tr>' + '<td>15/09</td>' + who('HĐ 00000193 · Sunrise Hotel', 'giá khách sạn · trả 15 ngày') + '<td class="c-table__num">3.200.000 ₫</td>' + '<td class="r-book__ok">' + ic('i-check') + 'có mã</td></tr>',
    '<tr>' + '<td>09/09</td>' + who('HĐ 00000187 · Sunrise Hotel', 'giá khách sạn · trả 15 ngày') + '<td class="c-table__num">5.200.000 ₫</td>' + '<td class="r-book__ok">' + ic('i-check') + 'có mã</td></tr>',
])
BT = ('<div class="c-tabs" role="tablist" aria-label="Sổ">' + ''.join(
    f'<a class="c-tabs__tab" role="tab" aria-selected="{"true" if n == "Doanh thu" else "false"}" href="{dict(zip(['Doanh thu', 'Chi phí', 'Tiền', 'Kho'], ['books.html', 'books--cost.html', 'money.html', 'books--stock.html']))[n]}">{n}</a>' for n in ['Doanh thu', 'Chi phí', 'Tiền', 'Kho']) + '</div>')
BOOKS = (f'\n      {sub("Sổ sách")}\n      <div class="r-page-head"><div><h1 class="r-page-head__title">Sổ doanh thu</h1>'
         '<p class="c-sub">Dựng tự động từ đơn, hoá đơn và giao dịch — không nhập tay</p>'
         f'<p class="r-book__tpl">{ic("i-alert")}Theo mẫu sổ của TT 152/2025 · ký hiệu mẫu chờ kế toán xác nhận; file xuất ghi rõ điều này.</p></div>'
         f'<div class="r-page-head__acts"><a class="c-btn c-btn--act" href="#">{ic("i-download")}Xuất sổ</a></div></div>'
         '<div class="page">' + BT
         + '<section class="r-listhead" aria-label="Doanh thu"><div class="r-listhead__fig"><span class="c-stat__label">Tháng 9/2026</span>'
         f'<b class="c-figure">118.200.000{CUR}</b></div><div class="r-listhead__bar"><p class="r-book__q"><a href="period.html">2 dòng cần xem trước khi khoá Quý III</a><span class="c-sub">Quý III cộng 338.400.000 ₫</span></p></div></section>'
         '<div class="c-table__scroll" tabindex="0" role="region" aria-label="Sổ doanh thu tháng 9"><table class="c-table c-table--stack r-book">'
         '<thead><tr><th scope="col">Ngày</th><th scope="col">Chứng từ · diễn giải</th><th scope="col" class="c-table__num">Doanh thu</th><th scope="col">Hoá đơn</th></tr></thead>'
         f'<tbody>{ROWS}</tbody></table></div>'
         '<p class="c-sub r-book__more">Hiện 6 / 214 dòng tháng 9 · <a href="#">Xem tất cả</a> · Muốn sửa một dòng: sửa ở chứng từ gốc hoặc ghi điều chỉnh có lý do.</p></div>')
build('books', 'Sổ & thuế · Sổ doanh thu', BOOKS, 'books')
finish('books')
print('period: 4 screens')

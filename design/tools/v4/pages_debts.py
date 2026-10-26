"""v4.2 · Tiền → Công nợ (FLOWS.md ②b steps 16–19, ③ steps 8–10; SCOPE §7 #11, #15, #16). BA demo data (An Nhiên).
Writes receivables.html (Phải thu — datatable), receivables--payables.html (Phải trả — owner sends via bank app),
receivable-detail.html (Sunrise statement + reminder), receivable-detail--assign.html (one transfer → many invoices).
Usage: python3 pages_debts.py"""
from pages import build, ic, sign, subnav, annhien, SCREENS

CUR = '<span class="u-cur">₫</span>'


def sub():
    return subnav('Tiền', [('Thu chi & đối chiếu', 'money.html'), ('Công nợ', 'receivables.html'), ('Đóng ca', 'shift-close.html')], 'Công nợ')


def tabs(sel):
    t = [('Phải thu', 'receivables.html', ''), ('Phải trả', 'receivables--payables.html', '')]
    return ('<div class="c-tabs" role="tablist" aria-label="Công nợ">' + ''.join(
        f'<a class="c-tabs__tab" role="tab" aria-selected="{"true" if n == sel else "false"}" href="{h}">{n}</a>'
        for n, h, v in t) + '</div>')


def listhead(k, fig, parts, aria, due_k, due_v, href, late_t=''):
    bar = ''.join(f'<i class="c-split__{c}" style="flex:{w}"></i>' for c, w, _ in parts)
    lab = ' · '.join(t for _, _, t in parts if t)
    return (f'<section class="r-listhead" aria-label="{aria}"><div class="r-listhead__fig"><span class="c-stat__label">{k}</span>'
            f'<b class="c-figure">{fig}{CUR}</b></div><div class="r-listhead__bar"><div class="c-split__bar" role="img" aria-label="{aria}">{bar}</div>'
            f'<p class="c-sub">{lab}</p></div><a class="r-listhead__due" href="{href}"><span class="c-stat__label">{due_k} '
            f'<span class="r-listhead__late">{late_t}</span></span><span class="r-listhead__duev">{due_v}</span>{ic("i-chev-r")}</a></section>')


def table(head, rows, label):
    th = ''.join(f'<th scope="col"{" class=\"c-table__num\"" if n == 1 else " class=\"c-table__cell--hide\"" if n == 2 else ""}>{h}</th>' for h, n in head)
    return (f'<div class="c-table__scroll" tabindex="0" role="region" aria-label="{label}"><table class="c-table c-table--stack">'
            f'<thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></div>')


def who(name, meta):
    return f'<td class="c-table__cell--main c-table__who"><b>{name}</b><small>{meta}</small></td>'


num = lambda v: f'<td class="c-table__num">{v}</td>'
late = lambda t: f'<td>{sign("err", "i-alert", t)}</td>'
ok = lambda t: f'<td>{sign("ok", "i-check", t)}</td>'
wait = lambda t: f'<td>{sign("wait", "i-clock", t)}</td>'

# ---------------- Phải thu ----------------
AR_ROWS = ''.join([
    '<tr class="c-table__row--you">' + who('Sunrise Hotel', 'Khách sạn · 15 ngày') + num('8.400.000 ₫') + late('Quá hạn 12 ngày')
    + '<td class="c-table__cell--hide">Nhắc lần 2 · 08:00</td><td class="c-table__cell--end"><a class="c-btn" href="receivable-detail.html">Xem & nhắc</a></td></tr>',
    '<tr>' + who('Nhà hàng Phố Núi', 'Nhà hàng · 7 ngày') + num('3.900.000 ₫') + wait('Hạn 12/10') + '<td class="c-table__cell--hide">—</td><td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
    '<tr>' + who('Homestay Mây Ngàn', 'Homestay · 15 ngày') + num('2.400.000 ₫') + wait('Hạn 18/10') + '<td class="c-table__cell--hide">—</td><td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
    '<tr>' + who('GHTK <span class="c-tag">thu hộ</span>', '3 đơn online · đối soát thứ Sáu') + num('1.700.000 ₫') + wait('Trả 09/10') + '<td class="c-table__cell--hide">—</td><td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
    '<tr>' + who('Nhà xe Đức Long <span class="c-tag">thu hộ</span>', 'DH-2043 · chị Thảo (Quy Nhơn)') + num('1.300.000 ₫') + wait('Khi khách nhận') + '<td class="c-table__cell--hide">—</td><td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
])
AR = (tabs('Phải thu') + listhead('Phải thu · 5 khách', '17.700.000', [('cash', 9300, 'trong hạn 9.300.000 ₫'), ('err', 8400, 'quá hạn 8.400.000 ₫')],
               'Phải thu 17.700.000 ₫: trong hạn 9.300.000 ₫, quá hạn 8.400.000 ₫', 'Sunrise Hotel', 'Xem bảng kê, nhắc nợ', 'receivable-detail.html', 'quá hạn 12 ngày')
      + table([('Khách', 0), ('Đang nợ', 1), ('Tình trạng', 0), ('Nhắc gần nhất', 2), ('', 0)], AR_ROWS, 'Khách đang nợ')
      + '<p class="r-upcoming">' + sign('wait', 'i-clock', 'Chưa tính: DH-2052 · Sunrise · 6.250.000 ₫') + ' <span class="c-sub">đơn đã giao, vào công nợ khi chị phát hành hoá đơn</span></p>')
HEAD = lambda t, s: (f'<div class="r-page-head"><div><h1 class="r-page-head__title">{t}</h1><p class="c-sub">{s}</p></div></div>')
main = f'\n      {sub()}\n      {HEAD("Công nợ", "Thứ Ba 06/10/2026 · cập nhật 14:05")}\n      <div class="page">{AR}</div>'
build('receivables', 'Tiền · Công nợ phải thu', main, 'money')
annhien(SCREENS / 'receivables.html')

# ---------------- Phải trả ----------------
AP_ROWS = ''.join([
    '<tr class="c-table__row--you">' + who('HTX Cao Nguyên', 'Đơn mua MH-0109 · 30 ngày') + num('4.800.000 ₫') + wait('Hạn 08/10 · còn 2 ngày')
    + f'<td class="c-table__cell--end"><a class="c-btn c-btn--act" href="#">{ic("i-bank")}Trả 4.800.000 ₫</a><small class="r-pay__help">mở app ngân hàng, chị tự xác nhận</small></td></tr>',
    '<tr>' + who('Điện lực Gia Lai', 'Chi phí · tiền điện tháng 9') + num('1.250.000 ₫') + wait('Hạn 10/10 · còn 4 ngày')
    + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="#">Trả</a></td></tr>',
    '<tr class="c-table__row--muted">' + who('HTX Cao Nguyên · MH-0118', 'chờ chị xác nhận nhận hàng (thiếu 5 kg)') + num('11.200.000 ₫') + wait('Chưa tính')
    + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="purchase-detail--receive.html">Xem</a></td></tr>',
])
AP = (tabs('Phải trả') + listhead('Phải trả · 2 nơi', '6.050.000', [('you', 4800, '2 khoản, đều đến hạn trong tuần này'), ('cash', 1250, '')], 'Phải trả 6.050.000 ₫: HTX 4.800.000 ₫ hạn 08/10, tiền điện 1.250.000 ₫ hạn 10/10',
               'HTX Cao Nguyên', 'Trả trước 08/10', '#', 'còn 2 ngày')
      + table([('Trả cho', 0), ('Số tiền', 1), ('Hạn', 0), ('', 0)], AP_ROWS, 'Khoản phải trả')
      + '<p class="c-decide__who">Ngân hàng báo tiền ra → OPC tự đóng khoản phải trả. Chưa thấy báo sau 1 ngày → khoản này hiện “Chờ xác nhận” để chị đánh dấu kèm biên lai.</p>')
main = f'\n      {sub()}\n      {HEAD("Công nợ", "Thứ Ba 06/10/2026 · cập nhật 14:05")}\n      <div class="page">{AP}</div>'
build('receivables--payables', 'Tiền · Công nợ phải trả', main, 'money')
annhien(SCREENS / 'receivables--payables.html')


# ---------------- Sunrise statement ----------------
def step(kind, src, time, what, detail=''):
    d = f'<span class="c-timeline__who">{detail}</span>' if detail else ''
    return (f'<li class="c-timeline__item c-timeline__item--{kind}"><span class="c-timeline__time">{time}</span>'
            f'<span class="c-timeline__dot" aria-hidden="true"></span><span class="c-timeline__body">'
            f'<span class="c-timeline__src">{src}</span><span class="c-timeline__what">{what}</span>{d}</span></li>')


INV_ROWS = ('<tr class="c-table__row--you">' + who('HĐ 00000187', 'DH-2019 · lập 09/09') + num('5.200.000 ₫') + late('Hạn 24/09 · quá 12 ngày') + '</tr>'
            '<tr class="c-table__row--you">' + who('HĐ 00000193', 'DH-2026 · lập 15/09') + num('3.200.000 ₫') + late('Hạn 30/09 · quá 6 ngày') + '</tr>')
PAID_ROWS = ('<tr>' + who('HĐ 00000231', 'DH-2049 · đơn định kỳ thứ Hai') + num('4.550.000 ₫') + ok('Đã trả QR 06/10 08:41') + '</tr>'
             '<tr>' + who('HĐ 00000176', 'DH-2011') + num('6.900.000 ₫') + ok('Đã trả 18/09') + '</tr>')
DRAFT = ('<figure class="c-quote" style="margin:0"><figcaption class="c-quote__from"><b>Trợ lý soạn</b> · gửi qua Zalo OA cho chị Mai, kèm bảng kê PDF</figcaption>'
         '<p class="c-quote__text">Dạ chào chị Mai, Đặc sản An Nhiên gửi bảng kê công nợ đến 06/10: 2 hoá đơn, tổng 8.400.000 ₫ '
         '(đã quá hạn). Chị chuyển giúp vào STK MB 0901 2345 678 – Đặc sản An Nhiên, nội dung "SUNRISE T9", hoặc quét QR trong bảng kê ạ. Cảm ơn chị!</p></figure>')
STMT = (f'\n      {sub()}\n      <div class="page"><nav class="c-crumbs" aria-label="Đường dẫn"><a href="receivables.html">Công nợ</a><span aria-current="page">Sunrise Hotel</span></nav>'
        '<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">Sunrise Hotel · công nợ '
        + sign('err', 'i-alert', 'Quá hạn 12 ngày') + '</h1>'
        f'<p class="r-detail__fig"><b class="c-figure">8.400.000{CUR}</b><span class="c-sub">2 hoá đơn quá hạn · điều khoản 15 ngày</span></p></div>'
        '<div class="r-detail__acts"><a class="c-btn" href="receivable-detail--assign.html">Ghi nhận tiền</a></div></div>'
        '<div class="r-detail__grid r-detail--calm"><div class="stack">'
        '<section class="c-card" aria-labelledby="s-open"><div class="c-card__head"><h2 class="c-card__title" id="s-open">Hoá đơn còn nợ</h2></div>'
        + table([('Hoá đơn', 0), ('Số tiền', 1), ('Tình trạng', 0)], INV_ROWS, 'Hoá đơn còn nợ')
        + '<p class="r-upcoming">' + sign('wait', 'i-clock', 'Chưa tính: DH-2052 · 6.250.000 ₫') + ' <span class="c-sub">vào công nợ khi chị phát hành hoá đơn</span></p></section>'
        '<details class="r-paid"><summary>Đã trả gần đây · 2 hoá đơn</summary>'
        + table([('Hoá đơn', 0), ('Số tiền', 1), ('Tình trạng', 0)], PAID_ROWS, 'Đã trả gần đây').replace(' tabindex="0" role="region"', '') + '</details>'
        '</div><aside class="r-tower__detail" aria-labelledby="s-rem"><h2 class="r-tower__t" id="s-rem">Nhắc nợ</h2>'
        '<ol class="c-timeline">'
        + step('ai', 'Trợ lý nhắc · Zalo OA', '30/09', 'Lần 1: gửi bảng kê', 'Chị Mai đã xem, chưa trả lời')
        + step('ai', 'Trợ lý nhắc · Zalo OA', '08:00', 'Lần 2: nhắc 8.400.000 ₫', 'Chưa trả lời')
        + step('ok', 'Chị An', '09:15', 'Hẹn khách trả khi nhận DH-2052', 'chị ghi khi xác nhận đơn')
        + step('now', 'Lần nhắc tiếp theo', 'Bây giờ', 'Chờ chị bấm gửi', '', )
        + '</ol>' + DRAFT + f'<div class="c-decide__acts" style="margin-top:var(--space-3)"><button class="c-btn c-btn--act" type="button">{ic("i-send")}Gửi bảng kê & nhắc nợ</button><a class="c-btn" href="customer-statement.html">Xem bảng kê</a><button class="c-btn c-btn--quiet" type="button">Sửa tin</button></div></aside></div></div>')
build('receivable-detail', 'Công nợ · Sunrise Hotel', STMT, 'money')
annhien(SCREENS / 'receivable-detail.html')

# ---------------- one transfer → many invoices ----------------
def opt(code, meta, amt, checked, why):
    return (f'<label class="r-alloc__row"><span class="c-check"><input type="checkbox"{" checked" if checked else ""} aria-describedby="w-{code}"></span>'
            f'<span class="r-alloc__body"><b>{code}</b><small>{meta}</small><small class="r-alloc__why" id="w-{code}">{why}</small></span>'
            f'<span class="r-alloc__amt">{amt}</span></label>')


DLG = ('<div class="c-dialog" role="dialog" aria-modal="true" aria-labelledby="dlg-title"><div class="c-dialog__panel">'
       '<div class="c-dialog__head"><div><span class="c-dialog__k">Tiền về · chưa có mã đơn</span><h2 class="c-dialog__title" id="dlg-title" tabindex="-1">8.400.000 ₫ · 14:05</h2></div>'
       f'<a class="c-icon-btn" href="receivable-detail.html" aria-label="Đóng, không thay đổi gì">{ic("i-x")}</a></div>'
       '<div class="c-dialog__body"><dl class="c-kv"><dt>Người chuyển</dt><dd class="c-kv__raw">CONG TY TNHH SUNRISE PLEIKU</dd>'
       '<dt>Nội dung</dt><dd class="c-kv__raw">SUNRISE TT T9</dd><dt>Ngân hàng</dt><dd>MB · ' + sign('pend', 'i-clock', 'Đã nhận · chờ xác minh') + '</dd></dl>'
       '<p class="c-decide__q">Trả cho hoá đơn nào?</p>'
       '<div class="r-alloc" role="group" aria-label="Chọn hoá đơn">'
       + opt('HĐ 00000187', 'Sunrise Hotel · quá 12 ngày', '5.200.000 ₫', True, 'Đúng tên khách · hoá đơn cũ nhất')
       + opt('HĐ 00000193', 'Sunrise Hotel · quá 6 ngày', '3.200.000 ₫', True, 'Đúng tên khách · tổng 2 hoá đơn = đúng số tiền')
       + '</div><p class="r-alloc__sum">Cộng 2 hoá đơn: <b>8.400.000 ₫</b> = số tiền về <span class="c-sign c-sign--ok"><span class="c-sign__pic">'
       + ic('i-check') + '</span>đủ</span></p><p class="c-decide__who">Đủ là phép cộng. Còn tiền có thật hay chưa: “chờ xác minh” tới khi khớp sao kê MB.</p>'
       '<details class="c-options__off"><summary>Cách khác</summary><p class="c-sub">Trả trước cho DH-2052 (chưa có hoá đơn) · Giữ làm tiền trả trước của khách · Không phải tiền của Sunrise</p></details>'
       '</div><div class="c-dialog__foot"><p class="c-dialog__note">Gán xong: 2 hoá đơn đóng · Sunrise còn nợ 0 ₫.</p>'
       '<button class="c-btn c-btn--act" type="button">Gán vào 2 hoá đơn</button></div></div></div>')
build('receivable-detail--assign', 'Công nợ · gán tiền vào nhiều hoá đơn', STMT, 'money', overlay=DLG)
annhien(SCREENS / 'receivable-detail--assign.html')
print('debts: 4 screens')

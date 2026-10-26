"""v4.2 · Sổ & thuế → Thuế (BA UI-15/16, FLOWS.md ⑤ steps 5–11; SCOPE Q1 option B). Owner's view (chị An).
Writes tax.html (calc + approve), tax--return.html (draft return document), tax-file.html (file: eTax by hand or
sign & send via OPC — Mô phỏng), tax-file--signed.html (accepted → pay outside OPC, enter the receipt),
tax-evidence.html (period closed, evidence pack). Every tax figure is labelled Mô phỏng. Usage: python3 pages_tax.py"""
from pages import build, ic, sign, subnav, annhien, SCREENS

CUR = '<span class="u-cur">₫</span>'
SIM = '<span class="c-sim">Mô phỏng</span>'


def sub():
    return subnav('Sổ & thuế', [('Kỳ thuế', 'period.html'), ('Sổ sách', 'books.html'), ('Hoá đơn', 'invoices.html'), ('Nhật ký', 'audit.html')], 'Kỳ thuế')


def finish(name, clock):
    p = SCREENS / f'{name}.html'
    annhien(p)
    s = p.read_text()
    for a, b in [('class="c-nav__item" href="invoices.html"', 'class="c-nav__item" href="period.html"'),
                 ('Nguyễn Minh Khoa · Người vận hành', 'Phạm Thị An · Chủ hộ'),
                 ('<span class="c-avatar__face" aria-hidden="true">K', '<span class="c-avatar__face" aria-hidden="true">A'),
                 ('Đã lưu 10:45', f'Đã lưu {clock}'), ('Đã lưu · <b>10:45</b>', f'Đã lưu · <b>{clock}</b>')]:
        s = s.replace(a, b)
    p.write_text(s)


STAGES = ['Tính thuế', 'Kế toán xem', 'Chị duyệt', 'Gửi tờ khai', 'Nộp tiền', 'Đóng kỳ']


def journey(now):
    out = []
    for i, s in enumerate(STAGES):
        cls = 'c-journey__s' + (' c-journey__s--done' if i < now else ' c-journey__s--now' if i == now else '')
        cur = ' aria-current="step"' if i == now else ''
        st = ' — xong' if i < now else ' — đang ở đây' if i == now else ''
        out.append(f'<li class="{cls}"{cur}>{s}<span class="u-sr">{st}</span></li>')
    return '<ol class="c-journey" aria-label="Kỳ thuế đang ở đâu">' + ''.join(out) + '</ol>'


def step(kind, src, time, what, detail=''):
    d = f'<span class="c-timeline__who">{detail}</span>' if detail else ''
    return (f'<li class="c-timeline__item c-timeline__item--{kind}"><span class="c-timeline__time">{time}</span>'
            f'<span class="c-timeline__dot" aria-hidden="true"></span><span class="c-timeline__body">'
            f'<span class="c-timeline__src">{src}</span><span class="c-timeline__what">{what}</span>{d}</span></li>')


def head(title, state, fig, figsub, primary, crumbs=''):
    cr = f'<nav class="c-crumbs" aria-label="Đường dẫn">{crumbs}</nav>' if crumbs else ''
    return (f'\n      {sub()}\n      <div class="page">{cr}'
            f'<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">{title} {state}</h1>'
            f'<p class="r-detail__fig"><b class="c-figure">{fig}</b>{SIM}<span class="c-sub">{figsub}</span></p></div>'
            f'<div class="r-detail__acts">{primary}</div></div>')


def gate_item(tone, icon, st, t, m, amt='', act=''):
    return (f'<li class="r-gate__i r-gate__i--{tone}"><span class="r-gate__b"><b>{t}</b>'
            f'<small><span class="r-gate__st">{st}</span> · {m}</small></span><span class="r-gate__amt">{amt}</span><span class="r-gate__act">{act}</span></li>')


who = lambda n, m: f'<td class="c-table__cell--main c-table__who"><b>{n}</b><small>{m}</small></td>'
num = lambda v, c='': f'<td class="c-table__num{c}">{v}</td>'
lab = lambda k, v: f'<td class="c-table__num"><span class="c-table__phone">{k} </span>{v}</td>'

CALC = ('<div class="c-table__scroll" tabindex="0" role="region" aria-label="Cách tính thuế"><table class="c-table c-table--stack r-taxcalc">'
        '<thead><tr><th scope="col">Nhóm ngành · món</th><th scope="col" class="c-table__num">Doanh thu</th><th scope="col" class="c-table__num">GTGT</th>'
        '<th scope="col" class="c-table__num">TNCN</th><th scope="col" class="c-table__num">Cộng</th></tr></thead><tbody>'
        '<tr>' + who('Sản xuất, chế biến', 'bò một nắng — tự chế biến · 3% + 1,5%') + num('266.400.000') + lab('GTGT', '7.992.000') + lab('TNCN', '3.996.000') + lab('Cộng', '<b>11.988.000</b>') + '</tr>'
        '<tr>' + who('Phân phối hàng hoá', 'muối kiến vàng — mua về bán lại · 1% + 0,5%') + num('72.000.000') + lab('GTGT', '720.000') + lab('TNCN', '360.000') + lab('Cộng', '<b>1.080.000</b>') + '</tr>'
        '<tr class="c-table__row--muted">' + who('Doanh thu qua sàn đã bị khấu trừ', 'không có trong kỳ') + num('0') + num('—', ' c-table__cell--hide') + num('—', ' c-table__cell--hide') + num('0', ' c-table__cell--hide') + '</tr>'
        '</tbody><tfoot><tr><th scope="row">Cộng Quý III</th><td class="c-table__num c-table__cell--hide">338.400.000</td><td class="c-table__num c-table__cell--hide">8.712.000</td>'
        '<td class="c-table__num c-table__cell--hide">4.356.000</td><td class="c-table__num"><b>13.068.000 ₫</b></td></tr></tfoot></table></div>'
        '<p class="c-sub">Doanh thu từ kỳ đã khoá 07/10 · <a href="books.html">xem sổ doanh thu</a></p>')
RULES = ('<h2 class="r-tower__t" id="rs">Bộ quy tắc</h2><dl class="c-kv"><dt>Phiên bản</dt><dd>demo-2026.3</dd>'
         '<dt>Cách tính</dt><dd>tỷ lệ % trên doanh thu theo nhóm ngành</dd><dt>Nguồn</dt><dd>giả lập cho demo</dd>'
         '<dt>Hiệu lực</dt><dd>01/01/2026</dd></dl><p class="r-trust">' + ic('i-alert') + '<span><b>Bộ quy tắc demo</b> · chị Lan đối chiếu trước khi dùng thật</span></p>'
         '<p class="r-tax__prev"><span class="c-sub">So với Quý II: 12.009.000 ₫</span><b>+1.059.000 ₫</b><span class="c-sub">vì doanh thu tăng 25.800.000 ₫</span></p>')

# ---------------- tax: calc + approve (owner) ----------------
TAX = (head('Thuế Quý III/2026', sign('you', 'i-alert', 'Chờ chị duyệt'), f'13.068.000{CUR}', 'phải nộp · hạn khai và nộp 31/10',
            f'<button class="c-btn c-btn--act" type="button">{ic("i-check")}Duyệt số thuế</button>')
       + journey(2)
       + '<p class="c-decide__result r-tax__warn">Duyệt = chị xác nhận số thuế · OPC không gửi, không nộp thay · <b>không phải tư vấn thuế</b></p>'
       '<div class="r-detail__grid r-detail--calm"><div class="stack">'
       '<section class="c-card" aria-labelledby="ct"><div class="c-card__head"><h2 class="c-card__title" id="ct">Cách tính, từng dòng</h2></div>' + CALC + '</section>'
       '<section class="c-card" aria-labelledby="rt"><div class="c-card__head"><h2 class="c-card__title" id="rt">Tờ khai nháp</h2></div>'
       '<p class="c-sub">Mẫu 01/CNKD (demo) · chờ đối chiếu mẫu mới · điền sẵn từ bảng trên</p>'
       f'<div class="c-decide__acts"><a class="c-btn" href="tax--return.html">{ic("i-file")}Xem tờ khai nháp</a><a class="c-btn c-btn--quiet" href="#">{ic("i-download")}Tải XML</a></div></section>'
       '<figure class="c-quote" style="margin:0"><figcaption class="c-quote__from"><b>Chị Lan · kế toán</b> · 07/10 10:20</figcaption>'
       '<blockquote class="c-quote__text">Đã xem, khớp sổ. Bò một nắng là hàng tự chế biến nên tính 3% + 1,5%, muối mua về bán lại tính 1% + 0,5%.</blockquote></figure>'
       '</div><aside class="r-tower__detail" aria-labelledby="rs">' + RULES
       + '<h2 class="r-tower__t r-rail__h2">Diễn biến</h2><ol class="c-timeline c-timeline--quiet" aria-label="Diễn biến">'
       + step('now', 'Chị An', 'Bây giờ', 'Duyệt số thuế')
       + step('ok', 'Chị Lan · kế toán', '10:20', 'Xem tờ khai nháp · ghi chú')
       + step('ok', 'OPC kiểm tra', '08:56', 'Tính thuế từ kỳ đã khoá', 'bộ quy tắc demo-2026.3')
       + step('ok', 'Chị An', '08:55', 'Khoá kỳ Quý III') + '</ol></aside></div></div>')
build('tax', 'Thuế · Quý III/2026', TAX, 'books')
finish('tax', '10:40')

# ---------------- draft return as a document ----------------
DOC = ('<article class="c-doc r-return" aria-labelledby="dt"><div class="r-return__mark" aria-hidden="true">NHÁP · MÔ PHỎNG</div>'
       '<div class="c-doc__head"><div><h2 class="c-doc__title" id="dt">Tờ khai thuế đối với hộ kinh doanh</h2><p class="c-sub">Mẫu 01/CNKD (demo) · khai theo quý</p></div>'
       '<div class="c-doc__no"><span class="c-sub">Kỳ tính thuế</span><b>Quý III/2026</b></div></div>'
       '<p class="r-trust">' + ic('i-alert') + '<span><b>Bản nháp — chưa ký, chưa gửi.</b> Số do bộ quy tắc demo tính; mã chỉ tiêu theo mẫu demo, chờ đối chiếu mẫu mới.</span></p>'
       '<div class="c-doc__party"><span class="c-doc__party-k">Người nộp thuế</span><b>Phạm Thị An · Hộ kinh doanh Đặc sản Cao Nguyên An Nhiên</b>'
       '<span>MST 5901234567 · Pleiku, Gia Lai</span></div>'
       '<div class="c-table__scroll" tabindex="0" role="region" aria-label="Chỉ tiêu tờ khai"><table class="c-table c-table--stack"><thead><tr><th scope="col">Nhóm ngành nghề</th>'
       '<th scope="col" class="c-table__num">Doanh thu</th><th scope="col" class="c-table__num">Thuế GTGT</th><th scope="col" class="c-table__num">Thuế TNCN</th></tr></thead><tbody>'
       '<tr>' + who('[28] Sản xuất, chế biến hàng hoá', '<a href="books.html">nguồn: 214 dòng sổ doanh thu</a> · <a href="#">báo sai dòng này</a>') + num('266.400.000') + lab('GTGT', '7.992.000') + lab('TNCN', '3.996.000') + '</tr>'
       '<tr>' + who('[29] Phân phối, cung cấp hàng hoá', '<a href="books.html">nguồn: 96 dòng sổ doanh thu</a> · <a href="#">báo sai dòng này</a>') + num('72.000.000') + lab('GTGT', '720.000') + lab('TNCN', '360.000') + '</tr>'
       '</tbody></table></div>'
       f'<div class="c-doc__total"><span>Tổng số thuế phải nộp</span><b>13.068.000{CUR}</b></div>'
       '<div class="c-doc__foot"><span>Số liệu từ kỳ đã khoá 07/10 08:55 · bộ quy tắc demo-2026.3 · chị Lan đã xem 10:20</span>'
       '</div></article>')
RET = (f'\n      {sub()}\n      <div class="page"><nav class="c-crumbs" aria-label="Đường dẫn"><a href="tax.html">Thuế Quý III</a><span aria-current="page">Tờ khai nháp</span></nav>'
       '<div class="r-page-head"><div><h1 class="r-page-head__title">Tờ khai nháp</h1><p class="c-sub">Xem trước khi duyệt · mỗi dòng dẫn về sổ, thấy sai thì báo chị Lan ngay tại dòng đó</p></div>'
       f'<div class="r-page-head__acts"><a class="c-btn" href="#">{ic("i-download")}Tải XML bản nháp</a><a class="c-btn c-btn--act" href="tax.html">Quay lại duyệt</a></div></div>'
       + DOC + '</div>')
build('tax--return', 'Thuế · Tờ khai nháp', RET, 'books')
finish('tax--return', '10:41')

# ---------------- file: two levels on one screen ----------------
PROOF = lambda ack, pay: ('<h2 class="r-tower__t" id="pf">Bộ bằng chứng</h2><ul class="r-gate">'
                          + gate_item('ok', 'i-file', 'Có', 'Tờ khai đã duyệt', 'chị An 11:02')
                          + (gate_item('ok', 'i-check', 'Có', 'Thông báo tiếp nhận', ack) if ack else gate_item('wait', 'i-clock', 'Chưa có', 'Thông báo tiếp nhận', 'sau khi gửi'))
                          + (gate_item('ok', 'i-check', 'Có', 'Biên nhận nộp tiền', pay) if pay else gate_item('wait', 'i-clock', 'Chưa có', 'Biên nhận nộp tiền', 'chị nộp xong thì nhập mã'))
                          + '</ul><p class="r-trust r-trust--gate">' + ic('i-lock') + '<span><b>Kỳ chỉ đóng khi đủ 3 thứ này.</b></span></p>')


def option(on, title, meta, tag=''):
    return (f'<button class="c-option{" c-option--best" if on else ""}" type="button" role="radio" aria-checked="{"true" if on else "false"}"><span class="c-option__radio" aria-hidden="true"></span>'
            f'<span class="c-option__body">{tag}<strong class="c-option__title">{title}</strong><span class="c-option__meta">{meta}</span></span></button>')


HOW = ('<ol class="r-howto" aria-label="Các bước trên eTax">'
       f'<li><b>Tải tờ khai</b><span>file XML đã duyệt, đúng mẫu</span><a class="c-btn" href="#">{ic("i-download")}Tải file</a></li>'
       f'<li><b>Mở eTax và đăng nhập</b><span>tài khoản thuế của hộ — OPC không giữ mật khẩu</span><a class="c-btn" href="#">{ic("i-link")}Mở eTax</a></li>'
       '<li><b>Nộp tờ khai từ file</b><span>chọn file vừa tải · ký bằng chữ ký số của hộ · gửi</span></li>'
       '<li><b>Quay lại đây, chụp thông báo tiếp nhận</b><span>bằng nút phía trên · Trợ lý đọc mã; OPC kiểm tra MST, kỳ và số tiền khớp tờ khai</span></li></ol>')
FILE = (head('Gửi tờ khai Quý III', sign('wait', 'i-clock', 'Đã duyệt · chưa gửi'), f'13.068.000{CUR}', 'hạn 31/10 · còn 24 ngày',
             f'<button class="c-btn c-btn--act" type="button">{ic("i-camera")}Chụp thông báo tiếp nhận</button>')
        + journey(3) + '<div class="r-detail__grid r-detail--calm"><div class="stack">'
        '<section class="c-card" aria-labelledby="hw"><div class="c-card__head"><h2 class="c-card__title" id="hw">Gửi bằng cách nào?</h2></div>'
        '<div class="c-options" role="radiogroup" aria-labelledby="hw">'
        + option(True, 'Tự gửi trên eTax', 'Luôn dùng được · OPC chuẩn bị file, chị gửi bằng tài khoản thuế của hộ')
        + option(False, 'Chị ký và gửi ngay tại OPC <span class="c-sim">Mô phỏng</span>', 'Cần kết nối gửi tờ khai (T-VAN) và chữ ký số từ xa · hộ chưa bật')
        + '</div>' + HOW
        + '<p class="c-decide__result">Có thông báo tiếp nhận = tờ khai <b>Đã tiếp nhận</b> · tiếp theo: chị nộp tiền thuế</p></section></div>'
        '<aside class="r-tower__detail" aria-labelledby="pf">' + PROOF('', '') + '</aside></div></div>')
build('tax-file', 'Thuế · Gửi tờ khai', FILE, 'books')
finish('tax-file', '11:05')

# ---------------- accepted (Mô phỏng) → pay outside OPC ----------------
PAY = ('<dl class="c-kv r-pay"><dt>Mã số thuế</dt><dd>5901234567</dd><dt>Kỳ</dt><dd>Quý III/2026</dd>'
       '<dt>Thuế GTGT</dt><dd>8.712.000 ₫ · tiểu mục 1701</dd><dt>Thuế TNCN</dt><dd>4.356.000 ₫ · tiểu mục 1003</dd></dl>'
       '<p class="c-sub">eTax Mobile điền sẵn khi mở từ OPC; app ngân hàng thì chép từ đây. Tiểu mục theo mẫu demo — chị Lan xác nhận.</p>'
       '<label class="c-field"><span class="c-field__label">Đã nộp xong? Mã biên nhận / số giấy nộp tiền</span><span class="c-field__control">'
       '<input class="c-field__input" placeholder="Ví dụ: chụp màn hình biên nhận hoặc gõ mã"></span></label>')
SIGNED = (head('Nộp thuế Quý III', sign('ok', 'i-check', 'Đã tiếp nhận tờ khai'), f'13.068.000{CUR}', 'chị tự nộp · OPC không chuyển tiền',
               f'<a class="c-btn c-btn--act" href="#">{ic("i-link")}Mở eTax Mobile để nộp</a>')
          + journey(4) + '<div class="r-detail__grid r-detail--calm"><div class="stack">'
          '<div class="c-banner c-banner--ok" role="status"><span class="c-banner__pic">' + ic('i-check') + '</span><span class="c-banner__text">'
          '<strong class="c-banner__title">Tờ khai đã được tiếp nhận · 11:06 — chưa nộp tiền</strong><span>Chị ký bằng mã OTP lúc 11:05 · mã giao dịch 11020261007000318 · ' + SIM + '</span></span></div>'
          '<section class="c-card" aria-labelledby="py"><div class="c-card__head"><h2 class="c-card__title" id="py">Nộp tiền thuế</h2></div>' + PAY
          + f'<div class="c-decide__acts"><a class="c-btn" href="#">{ic("i-bank")}Mở app MB</a><button class="c-btn" type="button">{ic("i-camera")}Chụp biên nhận</button></div>'
          '<p class="c-decide__result">Kỳ chỉ thành <b>Đã nộp</b> khi có mã biên nhận · OPC đối chiếu thêm khoản tiền ra trên sao kê MB</p></section></div>'
          '<aside class="r-tower__detail" aria-labelledby="pf">' + PROOF('mã 11020261007000318 · 11:06 · Mô phỏng', '') + '</aside></div></div>')
build('tax-file--signed', 'Thuế · Nộp tiền', SIGNED, 'books')
finish('tax-file--signed', '11:12')

# ---------------- closed: evidence pack ----------------
EVID = ('<ul class="r-gate">'
        + gate_item('ok', 'i-file', 'Đã duyệt', 'Tờ khai Quý III · XML + PDF', 'chị An duyệt 07/10 11:02 · chị Lan xem 10:20', '', f'<a class="c-btn c-btn--quiet" href="tax--return.html">Xem</a>')
        + gate_item('ok', 'i-check', 'Đã tiếp nhận', 'Thông báo tiếp nhận', 'mã 11020261007000318 · 11:06 · Mô phỏng', '', '<a class="c-btn c-btn--quiet" href="#">Xem</a>')
        + gate_item('ok', 'i-banknote', 'Đã nộp', 'Biên nhận nộp tiền · eTax Mobile', 'mã 2026100700318 · chị An nhập 11:24 · khớp tờ khai', '', '<a class="c-btn c-btn--quiet" href="#">Xem</a>')
        + gate_item('match', 'i-bank', 'Khớp biên nhận', 'Tiền ra trên sao kê MB', '11:24 · nội dung nộp thuế · Kết nối MB qua Casso', '13.068.000 ₫', '')
        + gate_item('ok', 'i-book', 'Đã khoá', 'Đối chiếu kỳ và sổ Quý III', '5 việc đã xử lý · ba nguồn khớp', '', '<a class="c-btn c-btn--quiet" href="period--ready.html">Xem</a>')
        + '</ul>')
CLOSED = (head('Quý III/2026', sign('ok', 'i-check', 'Đã đóng'), f'13.068.000{CUR}', 'đã nộp 07/10 · trước hạn 24 ngày',
               f'<a class="c-btn c-btn--act" href="#">{ic("i-download")}Tải bộ bằng chứng</a>')
          + journey(6) + '<div class="r-detail__grid r-detail--calm"><div class="stack">'
          '<section class="c-card" aria-labelledby="ev"><div class="c-card__head"><h2 class="c-card__title" id="ev">Bộ bằng chứng · đủ</h2></div>' + EVID
          + '<p class="c-sub">Sổ Quý III đã khoá. Muốn sửa: mở lại kỳ (chị An duyệt, có lý do) rồi khai bổ sung.</p></section></div>'
          '<aside class="r-tower__detail" aria-labelledby="hs"><h2 class="r-tower__t" id="hs">Diễn biến 07/10</h2><ol class="c-timeline c-timeline--quiet" aria-label="Diễn biến">'
          + step('now', 'OPC kiểm tra', '11:25', 'Đóng kỳ', 'đủ tờ khai, tiếp nhận, biên nhận')
          + step('ok', 'Kết nối · MB', '11:24', 'Thấy tiền ra, khớp biên nhận')
          + step('ok', 'Chị An', '11:24', 'Nộp trên eTax Mobile, nhập mã')
          + step('ok', 'Kết nối · Mô phỏng', '11:06', 'Tờ khai được tiếp nhận')
          + step('ok', 'Chị An', '11:05', 'Ký và gửi bằng OTP')
          + step('ok', 'Chị An', '11:02', 'Duyệt số thuế')
          + step('ok', 'Chị Lan · kế toán', '10:20', 'Xem tờ khai nháp')
          + step('ok', 'OPC kiểm tra', '08:56', 'Tính thuế') + '</ol></aside></div></div>')
build('tax-evidence', 'Thuế · Bằng chứng Quý III', CLOSED, 'books')
finish('tax-evidence', '11:30')
print('tax: 5 screens')

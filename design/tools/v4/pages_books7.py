"""v7.5.0 · Sổ và kê khai, đợt 5. BA verdict: in the pilot OPC never shows a computed tax amount. It shows revenue by quarter
(from invoices + sales without invoice), the running annual total against the revenue thresholds (rule data, versioned, waiting for
the accountant), a filing guide marked "không phải tư vấn thuế", eTax progress the owner records (đã gửi → thông báo tiếp nhận →
chấp nhận), the annual revenue notice and the bank-account notice, and the evidence pack (kept 10 years).
Overwrites tax, tax--return, tax-file, tax-file--signed, tax-evidence (pages_tax.py archived).  Usage: python3 pages_books7.py"""
from erp_lib import *

SEC = 'books'
CR = ('Kê khai', 'tax.html')
RULE = 'bộ quy tắc demo-2026.3 · chờ chị Lan (kế toán) xác nhận'
NOTAX = ('<div class="c-banner" role="note"><span class="c-banner__pic">' + ic('i-shield') + '</span><span class="c-banner__text">'
         '<strong class="c-banner__title">OPC chưa tính số thuế trong giai đoạn thử</strong>'
         '<span>OPC gom doanh thu và chứng từ, nhắc hạn, hướng dẫn từng bước. Đây không phải tư vấn thuế; số phải nộp do chị và kế toán xác định trên eTax.</span></span></div>')


def page(title, sub, body, side, acts='', crumb=CR, trk=''):
    return (f'<div class="page"><nav class="c-crumbs" aria-label="Đường dẫn"><a href="{crumb[1]}">{crumb[0]}</a><span aria-current="page">{title}</span></nav>'
            + head(title, sub, acts) + trk + jump('sd', 'Xem thêm') + f'<div class="r-detail__grid r-detail--calm"><div class="stack">{body}</div>'
            f'<aside class="r-tower__detail" aria-labelledby="sd">{side}</aside></div></div>')


def meter(label, now, cap, pct, why):
    return (f'<div class="c-meter"><div class="c-meter__row"><span class="u-meta">{label} · <b>{now} / {cap}</b></span></div>'
            f'<div class="c-meter__bar" role="img" aria-label="{label}: {now} trên {cap}"><span class="c-meter__fill" style="width:{pct}%"></span></div>'
            f'<p class="c-meter__why">{why}</p></div>')


FILE_T = lambda a, b, c, d: tracks(('Đối soát kỳ', a[0], a[1]), ('Kế toán xem', b[0], b[1]), ('Nộp trên eTax', c[0], c[1]), ('Cơ quan thuế', d[0], d[1]))

# ================================================================== Kê khai · Quý III/2026 overview
REV = ('<dl class="c-kv"><dt>Doanh thu đã giao</dt><dd><b>338.400.000 ₫</b> · nhóm phân phối, cung cấp hàng hoá</dd>'
       '<dt>Có hoá đơn</dt><dd>337.100.000 ₫ · 214 hoá đơn</dd><dt>Chưa có hoá đơn</dt><dd>1.300.000 ₫ · DH-2036 · <a href="period--item.html">xử lý ở Đối soát</a></dd></dl>')
YEAR = (meter('Doanh thu từ 01/01', '718.400.000 ₫', 'mốc 1 tỷ (chờ xác nhận)', 72,   # 718,4 / 1 000 (home uses a 1,5 tỷ scale with a 1 tỷ mark)
              'Trước OPC 380.000.000 ₫ (chị khai lúc đăng ký) + quý III 338.400.000 ₫. Theo nhịp quý III, cả năm ước 1,06 tỷ — cao hơn ước lúc đăng ký (760 triệu).')
        + '<p class="c-sub">Mốc không phải nộp thuế đang có hai con số (200 triệu, 1 tỷ) · chờ chị Lan chốt. Mốc hoá đơn máy tính tiền: 1 tỷ.</p>')
NOTICE = ('<ul class="r-pick">'
          '<li class="r-pick__l"><span class="r-pick__chk r-pick__chk--ok" aria-hidden="true">' + ic('i-check') + '</span><span class="r-pick__name"><b><a href="tax-notice-bank.html">Thông báo tài khoản ngân hàng</a></b>'
          '<small>MB 0901 2345 678 · đã báo 01/07 · thêm tài khoản mới thì báo lại</small></span><span class="r-pick__qty"></span></li>'
          '<li class="r-pick__l"><span class="r-pick__chk" aria-hidden="true"></span><span class="r-pick__name"><b><a href="tax-notice-year.html">Thông báo doanh thu năm 2026</a></b>'
          '<small>mẫu và hạn chờ kế toán xác nhận · OPC chuẩn bị số từ sổ</small></span><span class="r-pick__qty">tháng 01/2027</span></li></ul>')
SIDE1 = ('<h2 class="r-tower__t" id="sd">Diễn biến</h2>' + tl([('01/10', 'ok', 'OPC mở kỳ đối soát quý III', '5 việc trước khi khoá'),
         ('06/10', 'pend', 'Còn 2 việc đối soát', 'chị An'), ('—', 'wait', 'Chị Lan xem số', 'sau khi khoá kỳ'), ('31/10', 'wait', 'Hạn nộp quý III', 'chị nộp trên eTax')]))
T1 = page('Quý III/2026', 'Khai theo quý · hạn nộp 31/10 · còn 25 ngày', NOTAX + card('k1', 'Doanh thu quý III', REV, '<a class="c-btn" href="books.html">Xem sổ</a>')
          + card('k2', 'Luỹ kế năm so với mốc', YEAR) + card('k3', 'Thông báo khác', NOTICE)
          + '<div class="r-form__acts"><a class="c-btn c-btn--act" href="period.html">Đối soát và khoá kỳ</a><a class="c-btn" href="tax--return.html">Xem hướng dẫn khai</a></div>',
          SIDE1, trk=FILE_T(('you', 'Còn 2 việc'), ('wait', 'Chờ khoá kỳ'), ('wait', 'Chưa nộp'), ('wait', '—')), crumb=('Sổ và kê khai', 'period.html'))
save('tax', 'Kê khai · Quý III/2026', T1, sec=SEC)
print('books7: tax')


# ================================================================== filing guide (replaces the computed draft return)
def gstep(n, t, m, act=''):
    return (f'<li class="r-pick__l"><span class="r-pick__chk" aria-hidden="true">{n}</span><span class="r-pick__name"><b>{t}</b><small>{m}</small></span>'
            f'<span class="r-pick__qty">{act}</span></li>')


COPY = lambda v: f'<button class="c-btn" type="button" aria-label="Sao chép {v}">{ic("i-file")}{v}</button>'
GUIDE = ('<ol class="r-pick r-guide7">'
         + gstep(1, 'Mở eTax, đăng nhập bằng VNeID mức 2', 'eTax Mobile hoặc cổng thuế điện tử · OPC không giữ mật khẩu')
         + gstep(2, 'Chọn tờ khai của hộ kinh doanh, kỳ quý III/2026', 'mẫu theo thông tư hiện hành · chị Lan xác nhận mẫu')
         + gstep(3, 'Nhập doanh thu nhóm phân phối, cung cấp hàng hoá', 'lấy từ sổ doanh thu đã khoá kỳ', COPY('338.400.000'))
         + gstep(4, 'Xem số thuế eTax tự tính', 'OPC không tính số này · có thắc mắc thì hỏi chị Lan')
         + gstep(5, 'Ký và gửi', 'chữ ký số hoặc xác thực trên eTax Mobile')
         + gstep(6, 'Lưu thông báo tiếp nhận vào OPC', 'chụp màn hình hoặc tải tệp từ email của cơ quan thuế', '<a class="c-btn" href="tax-file.html">Lưu thông báo</a>')
         + '</ol>')
SIDE2 = ('<h2 class="r-tower__t" id="sd">Số dùng để khai</h2><dl class="c-kv"><dt>Kỳ</dt><dd>quý III/2026 · 01/07–30/09</dd><dt>Doanh thu</dt><dd>338.400.000 ₫</dd>'
         '<dt>Nguồn</dt><dd>sổ doanh thu · khoá kỳ 07/10 · 214 hoá đơn + 1 đơn chưa có hoá đơn</dd><dt>Quy tắc</dt><dd>' + RULE + '</dd></dl>')
T2 = page('Hướng dẫn khai quý III', 'Kỳ đã khoá 07/10 · chị tự nộp trên eTax · OPC chuẩn bị số và chứng từ', NOTAX + card('g1', '6 bước trên eTax', GUIDE), SIDE2,
          '<a class="c-btn" href="tax-evidence.html">' + ic('i-download') + 'Tải bộ chứng từ</a>')
save('tax--return', 'Kê khai · Hướng dẫn quý III', T2, sec=SEC)
print('books7: tax, guide')


# ================================================================== eTax progress: the owner records what eTax returned (OPC has no eTax connection)
def receipt(t, when, txt):
    return (f'<figure class="c-quote" style="margin:0"><figcaption class="c-quote__from"><b>{t}</b> · {when}</figcaption>'
            f'<div class="c-quote__media">{ic("i-file")}<span>{txt}</span></div></figure>')


R1 = receipt('Thông báo tiếp nhận', 'chị An tải lên 08/10 20:14', 'Cơ quan thuế đã tiếp nhận tờ khai quý III/2026 · mã giao dịch 11020260000845123 · <mark>chưa phải chấp nhận</mark>')
F1 = ('<p class="c-sub">eTax gửi 2 thông báo: <b>tiếp nhận</b> (đã nhận hồ sơ) rồi <b>chấp nhận</b> hoặc không chấp nhận. Thường trong 1 ngày làm việc; '
      'OPC nhắc chị kiểm email nếu sau 3 ngày chưa có.</p>'
      '<div class="r-form__acts"><button class="c-btn c-btn--act" type="button">' + ic('i-photo') + 'Đưa thông báo chấp nhận lên</button>'
      '<a class="c-btn c-btn--quiet" href="tax-file--signed.html">Xem khi đã chấp nhận</a></div>')
H5 = tl([('07/10', 'ok', 'Khoá kỳ quý III', 'chị An · chị Lan đã xem số'), ('08/10', 'ok', 'Chị An nộp trên eTax', 'doanh thu 338.400.000 ₫'),
         ('08/10', 'ok', 'Có thông báo tiếp nhận', 'chị tải lên'), ('—', 'pend', 'Chờ thông báo chấp nhận', 'nhắc lại 11/10')])
T3 = page('Nộp quý III · đã gửi', 'Nộp 08/10 trên eTax · chờ cơ quan thuế chấp nhận', card('f1', 'Thông báo từ eTax', R1 + F1),
          '<h2 class="r-tower__t" id="sd">Diễn biến</h2>' + H5,
          trk=FILE_T(('ok', 'Đã khoá 07/10'), ('ok', 'Chị Lan đã xem'), ('ok', 'Đã gửi 08/10'), ('pend', 'Đã tiếp nhận · chờ chấp nhận')))
save('tax-file', 'Kê khai · Đã gửi quý III', T3, sec=SEC)

R2 = R1.replace('<mark>chưa phải chấp nhận</mark>', 'đã tiếp nhận') + receipt('Thông báo chấp nhận', 'chị An tải lên 09/10 08:30', 'Tờ khai quý III/2026 được chấp nhận · <mark>số phải nộp và hạn nộp xem trên eTax</mark>')
F2 = ('<div class="c-banner c-banner--ok" role="status"><span class="c-banner__pic">' + ic('i-check') + '</span><span class="c-banner__text">'
      '<strong class="c-banner__title">Quý III đã được chấp nhận</strong><span>Kỳ đã khoá; sửa số sau này phải làm tờ khai bổ sung. Bộ chứng từ đã đủ để lưu.</span></span></div>'
      '<div class="r-form__acts"><a class="c-btn c-btn--act" href="tax-evidence.html">Xem bộ chứng từ</a><button class="c-btn" type="button">Lưu chứng từ đã nộp thuế</button></div>'
      '<p class="c-sub">Nộp tiền thuế: chị nộp qua eTax hoặc ngân hàng; OPC chỉ ghi lại khi chị đưa chứng từ nộp tiền lên.</p>')
H6 = H5.replace('c-timeline__item--pend', 'c-timeline__item--ok').replace('Chờ thông báo chấp nhận', 'Được chấp nhận').replace('nhắc lại 11/10', 'chị tải lên 09/10').replace('<span class="c-timeline__time">—</span>', '<span class="c-timeline__time">09/10</span>')
T4 = page('Nộp quý III · đã chấp nhận', 'Nộp 08/10 · chấp nhận 09/10', F2 + card('f1', 'Thông báo từ eTax', R2), '<h2 class="r-tower__t" id="sd">Diễn biến</h2>' + H6,
          trk=FILE_T(('ok', 'Đã khoá 07/10'), ('ok', 'Chị Lan đã xem'), ('ok', 'Đã gửi 08/10'), ('ok', 'Đã chấp nhận 09/10')))
save('tax-file--signed', 'Kê khai · Quý III đã chấp nhận', T4, sec=SEC)

# ================================================================== evidence pack (bằng chứng), kept 10 years
EV = ('<ul class="r-pick">' + ''.join(
    f'<li class="r-pick__l"><span class="r-pick__chk r-pick__chk--ok" aria-hidden="true">{ic("i-check")}</span><span class="r-pick__name"><b>{a}</b><small>{b}</small></span><span class="r-pick__qty">{c}</span></li>'
    for a, b, c in [('Sổ doanh thu quý III', 'theo mẫu sổ của hộ kinh doanh (TT 152/2025) · PDF + Excel', '214 dòng'),
                    ('Hoá đơn điện tử đã lập', 'XML + PDF · có mã cơ quan thuế', '214'), ('Sao kê MB 01/07–30/09', 'tệp ngân hàng · khớp với thu tiền', '3 tháng'),
                    ('Chứng từ mua hàng', 'hoá đơn điện tử, ảnh phiếu viết tay MH-0114', '12'), ('Biên bản đối soát và khoá kỳ', 'chị An khoá 07/10 · chị Lan xem', '1'),
                    ('Thông báo tiếp nhận và chấp nhận', 'chị tải từ eTax', '2'), ('Nhật ký thay đổi', 'mọi lần sửa sau khi khoá · chỉ thêm, không xoá', 'không có sửa')]) + '</ul>')
T5 = page('Bộ chứng từ quý III', 'Lưu 10 năm · tải về hoặc gửi kế toán', card('e1', '7 phần · đủ', EV)
          + '<div class="r-form__acts"><button class="c-btn c-btn--act" type="button">' + ic('i-download') + 'Tải bộ chứng từ (ZIP)</button>'
            '<button class="c-btn" type="button">' + ic('i-send') + 'Gửi chị Lan</button></div>',
          '<h2 class="r-tower__t" id="sd">Lưu giữ</h2><dl class="c-kv"><dt>Thời hạn</dt><dd>10 năm · tới hết 2036</dd><dt>Nơi lưu</dt><dd>máy chủ OPC tại Việt Nam · bản sao chị tải về</dd>'
          '<dt>Ai xem</dt><dd>chị An · chị Lan (chỉ xem, tải)</dd></dl>')
save('tax-evidence', 'Kê khai · Bộ chứng từ quý III', T5, sec=SEC)
print('books7: tax, guide, file, signed, evidence')


# ================================================================== period locked (after "Khoá kỳ")
LK = ('<div class="c-banner c-banner--ok" role="status"><span class="c-banner__pic">' + ic('i-lock') + '</span><span class="c-banner__text">'
      '<strong class="c-banner__title">Đã khoá quý III/2026 · 07/10 09:00</strong><span>Số liệu đứng yên để khai. Sửa sau khi khoá: chị Lan mở lại kỳ, ghi lý do; mọi lần sửa vào Nhật ký.</span></span></div>')
LKV = ('<dl class="c-kv"><dt>Doanh thu</dt><dd>338.400.000 ₫ · 214 hoá đơn + 1 đơn chưa có hoá đơn</dd><dt>Ba nguồn</dt><dd>đơn đã giao · hoá đơn · tiền — khớp</dd>'
       '<dt>Người khoá</dt><dd>chị An · chị Lan đã xem số 07/10 08:40</dd></dl>')
LKA = ('<div class="r-form__acts"><a class="c-btn c-btn--act" href="tax--return.html">Khai trên eTax</a><a class="c-btn" href="tax-evidence.html">Bộ chứng từ</a>'
       '<button class="c-btn c-btn--quiet" type="button">Mở lại kỳ…</button></div>')
P1 = page('Quý III/2026 · đã khoá', 'Khoá 07/10 09:00 · hạn khai 31/10', LK + card('l1', 'Số đã khoá', LKV) + LKA,
          '<h2 class="r-tower__t" id="sd">Diễn biến</h2>' + tl([('06/10', 'ok', 'Xử lý 5 việc đối soát', 'anh Khoa, chị Lan'), ('07/10', 'ok', 'Chị Lan xem số', '08:40'), ('07/10', 'ok', 'Chị An khoá kỳ', '09:00'),
                                                                  ('31/10', 'wait', 'Hạn nộp quý III', 'chị nộp trên eTax')]),
          crumb=('Kỳ và đối soát', 'period.html'), trk=FILE_T(('ok', 'Đã khoá 07/10'), ('ok', 'Chị Lan đã xem'), ('wait', 'Chưa nộp'), ('wait', '—')))
save('period--locked', 'Sổ · Quý III đã khoá', P1, sec=SEC)

# ================================================================== bank-account notice (mandatory; form and deadline pending the accountant)
BK = ('<ul class="r-pick">'
      '<li class="r-pick__l"><span class="r-pick__chk r-pick__chk--ok" aria-hidden="true">' + ic('i-check') + '</span><span class="r-pick__name"><b>MB 0901 2345 678 · chủ hộ Phạm Thị An</b>'
      '<small>đã báo 01/07 trên eTax · có thông báo tiếp nhận</small></span><span class="r-pick__qty"></span></li>'
      '<li class="r-pick__l"><span class="r-pick__chk" aria-hidden="true"></span><span class="r-pick__name"><b>Ví MoMo 0935 112 418</b>'
      '<small class="r-recv__short">khách vừa chuyển vào ví này 2 lần · chưa báo cơ quan thuế</small></span><span class="r-pick__qty"><a class="c-btn" href="tax--return.html">Hướng dẫn báo</a></span></li></ul>')
BKN = ('<p class="c-sub">Mọi tài khoản, ví nhận tiền bán hàng phải báo cơ quan thuế · mẫu và hạn chờ chị Lan xác nhận.</p>'
       '<p class="c-sub">OPC nhắc khi tiền bán hàng về một tài khoản chưa báo.</p>')
P2 = page('Tài khoản đã báo cơ quan thuế', 'Chị báo trên eTax · OPC chỉ ghi lại', card('b1', '2 tài khoản nhận tiền', BK + BKN),
          '<h2 class="r-tower__t" id="sd">Vì sao cần</h2><p class="c-sub">Cơ quan thuế đối chiếu tiền về các tài khoản này với doanh thu chị khai.</p>')
save('tax-notice-bank', 'Kê khai · Thông báo tài khoản', P2, sec=SEC)

# ================================================================== annual revenue notice (prepared from the books; filed by the owner)
YR = ('<dl class="c-kv"><dt>Năm</dt><dd>2026 · từ 01/01 đến 31/12</dd><dt>Doanh thu đến 06/10</dt><dd>718.400.000 ₫ · số cả năm chốt sau khi khoá quý IV</dd>'
      '<dt>Mẫu và hạn</dt><dd>chờ chị Lan xác nhận · OPC đang đặt nhắc tháng 01/2027</dd></dl>'
      '<ol class="r-pick r-guide7">' + gstep(1, 'Khoá quý IV/2026', 'sau 31/12') + gstep(2, 'OPC lập bảng doanh thu cả năm', 'từ 4 quý đã khoá', '<button class="c-btn" type="button">Tải bảng</button>')
      + gstep(3, 'Chị gửi trên eTax', 'theo mẫu kế toán xác nhận') + gstep(4, 'Lưu thông báo tiếp nhận vào OPC', 'vào bộ chứng từ năm') + '</ol>')
P3 = page('Thông báo doanh thu năm 2026', 'Chưa tới kỳ · OPC chuẩn bị sẵn số', NOTAX + card('y1', 'Chuẩn bị', YR),
          '<h2 class="r-tower__t" id="sd">Nhắc</h2><p class="c-sub">OPC nhắc chị và chị Lan đầu tháng 01/2027, rồi 7 ngày trước hạn.</p>')
save('tax-notice-year', 'Kê khai · Thông báo doanh thu năm', P3, sec=SEC)
print('books7: + locked, notices')


# ================================================================== sổ chi phí + sổ kho (tabs of Sổ sách; TT 152/2025 forms pending the accountant)
def btabs(sel):
    return ('<div class="c-tabs" role="tablist" aria-label="Sổ">' + ''.join(
        f'<a class="c-tabs__tab" role="tab" aria-selected="{"true" if n == sel else "false"}" href="{h}">{n}</a>'
        for n, h in [('Doanh thu', 'books.html'), ('Chi phí', 'books--cost.html'), ('Tiền', 'money.html'), ('Kho', 'books--stock.html')]) + '</div>')


def book(rows, head, total, label):
    th = ''.join(f'<th scope="col"{" class=c-table__num" if n else ""}>{h}</th>' for h, n in head)
    tr = ''.join('<tr>' + ''.join(f'<td data-l="{head[i][0]}"{" class=c-table__num" if head[i][1] else (" class=c-table__cell--main" if i == 1 else "")}>{c}</td>' for i, c in enumerate(r)) + '</tr>' for r in rows)
    return (f'<div class="c-table__scroll" tabindex="0" role="region" aria-label="{label}"><table class="c-table c-table--stack r-ledger"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody>'
            f'<tfoot><tr>{total}</tr></tfoot></table></div>')


TPL = '<p class="c-sub">Theo mẫu sổ của TT 152/2025 · ký hiệu mẫu chờ kế toán xác nhận · dựng tự động, không nhập tay.</p>'
COST = book([('02/10', 'Túi hút chân không 1.000 cái · Bao bì Phú Mỹ', 'hoá đơn điện tử', '850.000 ₫'),
             ('04/10', 'Xăng xe giao hàng tuần 40', 'biên lai · không có hoá đơn', '850.000 ₫'),
             ('05/10', 'Tiền điện tháng 9 · Điện lực Gia Lai', 'hoá đơn điện tử · chưa trả, hạn 10/10', '1.250.000 ₫')],
            [('Ngày', 0), ('Diễn giải', 0), ('Chứng từ', 0), ('Số tiền', 1)],
            '<td></td><td class="c-table__cell--main">Cộng tháng 10 đến 06/10</td><td></td><td class="c-table__num"><b>2.950.000 ₫</b></td>', 'Sổ chi phí')
B1 = ('<div class="page">' + head('Sổ chi phí', 'Tháng 10/2026 · chi phí không qua kho', '<a class="c-btn" href="tax-evidence.html">' + ic('i-download') + 'Xuất sổ</a>')
      + btabs('Chi phí') + TPL + COST
      + '<p class="c-sub">Giá vốn hàng bán nằm ở sổ Kho, không cộng vào đây. Sổ chi phí chỉ dùng để tính thuế khi kế toán xác nhận hộ thuộc nhóm phải ghi chi phí.</p></div>')
save('books--cost', 'Sổ sách · Sổ chi phí', B1, sec=SEC)

STK = book([('01/10', 'Tồn đầu tháng', '', '', '70', '13.300.000 ₫'),
            ('01–05/10', 'Bán · 6 đơn', '', '8', '62', '11.780.000 ₫'),
            ('06/10', 'DH-2049 · Sunrise Hotel · đã giao', '', '15', '47', '8.930.000 ₫'),
            ('06/10', 'DH-2046 · chị Hoa · đã giao', '', '1', '46', '8.740.000 ₫')],
           [('Ngày', 0), ('Diễn giải', 0), ('Nhập', 1), ('Xuất', 1), ('Tồn', 1), ('Giá trị tồn', 1)],
           '<td></td><td class="c-table__cell--main">Tồn lúc 10:45</td><td></td><td></td><td class="c-table__num"><b>46 gói</b></td><td class="c-table__num"><b>8.740.000 ₫</b></td>', 'Sổ kho bò một nắng')
B2 = ('<div class="page">' + head('Sổ kho · Bò một nắng 500g', 'Tháng 10/2026 · giá vốn bình quân 190.000 ₫/gói', '<a class="c-btn" href="tax-evidence.html">' + ic('i-download') + 'Xuất sổ</a>')
      + btabs('Kho') + TPL + STK
      + '<p class="c-sub"><b>Khả dụng 26 gói</b> = tồn 46 − giữ 20 cho DH-2052 · đơn chưa giao không trừ kho, trừ khi giao xong. Giá vốn bình quân tính lại mỗi lần nhập · cách tính chờ kế toán xác nhận.</p></div>')
save('books--stock', 'Sổ sách · Sổ kho', B2, sec=SEC)
print('books7: + books cost/stock')

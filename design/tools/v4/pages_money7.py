"""v7.4.0 · Tiền, đợt 4. BA verdicts: one payment for many orders, customer statement, "Tiền chưa gán", duplicate detection,
overpayment → "khách trả trước"; cash is counted in Thu chi và đối chiếu (no shift close). OPC never moves money: it reads the bank
feed (if connected) or the owner's confirmation, proposes a match, the owner confirms.
Writes money--split, money--overpay, money--duplicate, money--cash, customer-statement.  Usage: python3 pages_money7.py"""
from erp_lib import *

SEC = 'money'
CR = ('Thu chi và đối chiếu', 'money.html')


def page(title, sub, body, side, crumb=CR, acts=''):
    return (f'<div class="page"><nav class="c-crumbs" aria-label="Đường dẫn"><a href="{crumb[1]}">{crumb[0]}</a><span aria-current="page">{title}</span></nav>'
            + head(title, sub, acts) + jump('sd', 'Xem giải thích') + f'<div class="r-detail__grid r-detail--calm"><div class="stack">{body}</div>'
            f'<aside class="r-tower__detail" aria-labelledby="sd">{side}<p class="c-sub"><a href="audit.html">Nhật ký</a> ghi mọi lần chị xác nhận hoặc sửa.</p></aside></div></div>')


def tx(who, when, memo, amt):
    return (f'<figure class="c-quote" style="margin:0"><figcaption class="c-quote__from"><b>{who}</b> · {when}</figcaption>'
            f'<div class="c-quote__media">{ic("i-bank")}<span>Nội dung “{memo}” · <mark>{amt}</mark></span></div></figure>')


def alloc(rows, total, label):
    tr = ''.join(f'<tr><td class="c-table__cell--main">{a}<small class="u-meta"> · {b}</small></td><td class="c-table__num">{c}</td>'
                 f'<td class="r-qty"><span class="c-field__control"><input class="c-field__input" inputmode="numeric" value="{d}" aria-label="Gán cho {a}"></span></td></tr>'
                 for a, b, c, d in rows)
    return (f'<div class="c-table__scroll" tabindex="0" role="region" aria-label="{label}"><table class="c-table r-lines r-lines--alloc"><thead><tr><th scope="col">Hoá đơn</th>'
            '<th scope="col" class="c-table__num">Còn nợ</th><th scope="col" class="c-table__num">Gán</th></tr></thead>'
            f'<tbody>{tr}</tbody><tfoot><tr><td class="c-table__cell--main">Tổng gán</td><td></td><td class="c-table__num"><b>{total}</b></td></tr></tfoot></table></div>')


# ================================================================== one transfer pays two invoices
S1 = (tx('CONG TY TNHH SUNRISE PLEIKU', 'MB · 10:44 · khớp sao kê', 'SUNRISE T9', '8.400.000 ₫')
      + card('a1', 'OPC đề xuất gán', alloc([('HĐ 00000187', 'DH-2019 · quá hạn 12 ngày', '5.200.000 ₫', '5.200.000'),
                                            ('HĐ 00000193', 'DH-2026 · quá hạn 6 ngày', '3.200.000 ₫', '3.200.000')], '8.400.000 ₫', 'Gán tiền vào hoá đơn'),
             meta='cũ trước, mới sau · sửa được')
      + '<div class="r-form__acts"><p class="c-decide__result">Xác nhận = 2 hoá đơn <b>đã thu đủ</b> · DH-2019, DH-2026 đóng · Sunrise hết nợ cũ '
        '(DH-2052 tính khi giao)</p><a class="c-btn c-btn--act" href="money.html">Xác nhận gán</a><a class="c-btn" href="money--assign.html">Gán khác</a></div>')
A1 = ('<h2 class="r-tower__t" id="sd">Vì sao OPC đề xuất</h2><dl class="c-kv"><dt>Người chuyển</dt><dd>trùng tên khách Sunrise Hotel</dd>'
      '<dt>Số tiền</dt><dd>bằng đúng tổng 2 hoá đơn còn nợ</dd><dt>Nội dung</dt><dd>“T9” = hoá đơn tháng 9</dd></dl>'
      '<p class="c-sub">Khách trả thiếu thì OPC gán cho hoá đơn cũ nhất trước; phần còn lại vẫn là nợ.</p>')
save('money--split', 'Tiền · Một lần trả cho nhiều hoá đơn', page('Gán 8.400.000 ₫ của Sunrise', 'Một lần chuyển · 2 hoá đơn', S1, A1), sec=SEC)
print('money7: split')


def choose(qid, q, opts, result, acts):
    o = ''.join(f'<button class="c-option" type="button" role="radio" aria-checked="{"true" if i == 0 else "false"}"><span class="c-option__radio" aria-hidden="true"></span>'
                f'<span class="c-option__body"><strong class="c-option__title">{t}</strong><span class="c-option__meta">{m}</span></span></button>' for i, (t, m) in enumerate(opts))
    return (f'<div class="c-decide" role="group" aria-labelledby="{qid}"><p class="c-decide__q" id="{qid}">{q}</p>'
            f'<div class="c-options" role="radiogroup" aria-label="{q}">{o}</div><p class="c-decide__result">{result}</p><div class="c-decide__acts">{acts}</div></div>')


# ================================================================== overpayment → customer credit (khách trả trước) or refund
S2 = (tx('HOMESTAY MAY NGAN', 'MB · hôm qua 18:20 · khớp sao kê', 'DH2041', '2.600.000 ₫')
      + '<dl class="c-kv"><dt>DH-2041 còn nợ</dt><dd>2.400.000 ₫ · HĐ 00000226</dd><dt>Dư</dt><dd><b>200.000 ₫</b></dd></dl>'
      + choose('q-over', 'Khách trả dư 200.000 ₫ — giữ thế nào?',
               [('Giữ làm tiền khách trả trước', 'tự trừ vào đơn sau của Homestay Mây Ngàn'), ('Trả lại khách', 'chị chuyển bằng app ngân hàng · OPC ghi khoản chi trả lại')],
               'Xác nhận = DH-2041 <b>đã thu đủ</b> · Homestay Mây Ngàn có <b>200.000 ₫ trả trước</b>',
               '<a class="c-btn c-btn--act" href="money.html">Xác nhận</a><button class="c-btn c-btn--quiet" type="button">' + ic('i-send') + 'Agent soạn tin báo khách</button>'))
A2 = ('<h2 class="r-tower__t" id="sd">Tiền khách trả trước</h2><p class="c-sub">Là tiền của khách đang để ở hộ, không phải doanh thu. Hiện ở hồ sơ khách và trên bảng kê; '
      'đơn sau tự trừ, chị xác nhận khi gán.</p>')
save('money--overpay', 'Tiền · Khách trả dư', page('Homestay Mây Ngàn trả dư', 'DH-2041 · 2.600.000 ₫ cho 2.400.000 ₫', S2, A2), sec=SEC)

# ================================================================== possible duplicate
DUP = ('<ul class="r-pick">'
       '<li class="r-pick__l"><span class="r-pick__chk r-pick__chk--ok" aria-hidden="true">' + ic('i-check') + '</span><span class="r-pick__name"><b>09:05 · LE VAN TOAN · “DH2048”</b>'
       '<small>có trong sao kê MB · đã gán DH-2048</small></span><span class="r-pick__qty"><b>195.000 ₫</b></span></li>'
       '<li class="r-pick__l"><span class="r-pick__chk" aria-hidden="true"></span><span class="r-pick__name"><b>09:06 · LE VAN TOAN · “DH2048”</b>'
       '<small class="r-recv__short">chỉ có trong thông báo · chưa thấy trong sao kê</small></span><span class="r-pick__qty"><b>195.000 ₫</b></span></li></ul>')
S3 = (DUP + choose('q-dup', 'Có thể trùng: cùng người, cùng số tiền, cùng nội dung, cách 1 phút',
                   [('Thông báo bị gửi 2 lần · bỏ khoản 09:06', 'sao kê chỉ có 1 khoản · không đổi tiền, không đổi đơn'),
                    ('Khách chuyển 2 lần thật', 'chờ sao kê xác nhận rồi giữ làm trả trước hoặc trả lại')],
                   'Bỏ = khoản 09:06 ẩn khỏi Thu chi, vẫn lưu trong Nhật ký để kiểm lại',
                   '<a class="c-btn c-btn--act" href="money.html">Xác nhận</a><a class="c-btn" href="money.html">Để sau · giữ ở Cần xem</a>'))
A3 = ('<h2 class="r-tower__t" id="sd">OPC coi là có thể trùng khi</h2><ul class="c-sub"><li>cùng người chuyển, cùng số tiền, cùng nội dung</li><li>cách nhau dưới 10 phút</li>'
      '<li>một bản không có trong sao kê</li></ul><p class="c-sub">OPC không tự xoá khoản nào; chị chọn, mọi lựa chọn ghi vào Nhật ký.</p>')
save('money--duplicate', 'Tiền · Có thể trùng', page('195.000 ₫ có thể trùng', 'DH-2048 · Lê Văn Toàn', S3, A3), sec=SEC)
print('money7: split, overpay, duplicate')


# ================================================================== cash count (replaces Đóng ca): count once a day, difference needs a reason
CNT = ('<div class="r-recv"><label class="c-field"><span class="c-field__label">Tiền mặt đếm được</span><span class="c-field__control"><input class="c-field__input" inputmode="numeric" value="1.470.000"></span>'
       '<span class="c-field__hint">đếm tổng là đủ · không cần đếm từng mệnh giá</span></label>'
       '<dl class="c-kv"><dt>Đầu ngày</dt><dd>1.000.000 ₫ · tiền lẻ để thối</dd><dt>Thu tiền mặt</dt><dd>+ 520.000 ₫ · 2 đơn bán nhanh</dd>'
       '<dt>Chi tiền mặt</dt><dd>− 50.000 ₫ · xăng giao hàng</dd><dt>Theo sổ</dt><dd><b>1.470.000 ₫</b></dd></dl></div>')
CA = choose('q-cash', 'Khớp với sổ · lệch 0 ₫', [('Giữ lại 1.000.000 ₫ làm tiền lẻ ngày mai', '470.000 ₫ chị cất hoặc nộp vào MB'),
                                               ('Nộp hết vào tài khoản MB', 'OPC khớp khi sao kê có khoản nộp')],
            'Xác nhận = tiền mặt hôm nay chốt 1.470.000 ₫ · lệch thì phải ghi lý do, chị An duyệt',
            '<a class="c-btn c-btn--act" href="money.html">Chốt tiền mặt hôm nay</a><a class="c-btn" href="money.html">Đếm lại</a>')
A4 = ('<h2 class="r-tower__t" id="sd">Tiền thu hộ</h2><dl class="c-kv"><dt>Anh Hùng</dt><dd>0 ₫ hôm nay · Sunrise trả theo công nợ</dd></dl>'
      '<p class="c-sub">Người giao thu tiền mặt của khách thì nộp lại cho chị; OPC ghi người nộp và giờ nộp.</p>')
save('money--cash', 'Tiền · Đếm tiền mặt', page('Đếm tiền mặt hôm nay', 'Thứ Ba 06/10 · chị An đếm lúc 18:00', CNT + CA, A4), sec=SEC)

# ================================================================== customer statement (bảng kê công nợ) — sent by the owner, Agent drafts
ROWS_ST = [('HĐ 00000187', 'DH-2019 · 09/09', 'hạn 24/09', '5.200.000 ₫'), ('HĐ 00000193', 'DH-2026 · 15/09', 'hạn 30/09', '3.200.000 ₫'),
           ('HĐ 00000231', 'DH-2049 · 05/10', 'đã trả 06/10', '0 ₫')]
ST = ('<div class="c-table__scroll" tabindex="0" role="region" aria-label="Bảng kê"><table class="c-table r-lines r-lines--alloc"><thead><tr><th scope="col">Hoá đơn</th>'
      '<th scope="col">Hạn</th><th scope="col" class="c-table__num">Còn nợ</th></tr></thead><tbody>'
      + ''.join(f'<tr><td class="c-table__cell--main">{a}<small class="u-meta"> · {b}</small></td><td>{c}</td><td class="c-table__num">{d}</td></tr>' for a, b, c, d in ROWS_ST)
      + '</tbody><tfoot><tr><td class="c-table__cell--main">Còn nợ đến 06/10</td><td></td><td class="c-table__num"><b>8.400.000 ₫</b></td></tr></tfoot></table></div>')
SA = ('<div class="r-form__acts"><p class="c-decide__result">Gửi = Agent đã soạn tin cho chị Mai kèm bảng kê PDF và mã QR tài khoản MB, nội dung “SUNRISE T9” · chị bấm gửi</p>'
      '<button class="c-btn c-btn--act" type="button">' + ic('i-send') + 'Gửi qua Zalo OA</button><button class="c-btn" type="button">' + ic('i-print') + 'Tải PDF</button></div>')
A5 = ('<h2 class="r-tower__t" id="sd">Khách Sunrise Hotel</h2><dl class="c-kv"><dt>Điều khoản</dt><dd>trả 15 ngày</dd><dt>Tiền trả trước</dt><dd>0 ₫</dd>'
      '<dt>Chưa tính</dt><dd>DH-2052 · 6.250.000 ₫ · vào bảng kê sau khi giao và lập hoá đơn</dd></dl>')
save('customer-statement', 'Công nợ · Bảng kê Sunrise', page('Bảng kê công nợ · Sunrise Hotel', 'Từ 01/09 đến 06/10/2026', card('b1', 'Hoá đơn trong kỳ', ST) + SA, A5,
     crumb=('Công nợ', 'receivables.html')), sec=SEC)
print('money7: split, overpay, duplicate, cash, statement')

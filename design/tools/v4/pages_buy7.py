"""v7.2.0 · Mua hàng (Procure-to-Pay), đợt 2. Research: _research (P2P track) + BA 07/10.
One purchase record, four independent sections (Hàng mua · Nhận hàng · Chứng từ · Tiền đã trả) + timeline; receiving and paying are tracked
separately; stock rises once, by the counted quantity; payments can be partial, before or after receipt; buying on credit has a due date.
Writes purchases, purchase-detail (+ --receive, --received, --pay, --doc), purchase-new, purchase-return, purchases--expense.  Usage: python3 pages_buy7.py"""
from pages import build, ic, sign, annhien, SCREENS
from erp_lib import *

def tabs(sel):
    return ('<div class="c-tabs" role="tablist" aria-label="Mua hàng">' + ''.join(
        f'<a class="c-tabs__tab" role="tab" aria-selected="{"true" if n == sel else "false"}" href="{h}">{n} <span class="c-tabs__count">{c}</span></a>'
        for n, h, c in [('Đơn mua', 'purchases.html', 5), ('Chi phí', 'purchases--expense.html', 3), ('Trả hàng', 'purchase-return.html', 1)]) + '</div>')


def chips(items, sel=0):
    return ('<div class="c-filters" role="group" aria-label="Lọc đơn mua">' + ''.join(
        f'<button class="c-filter" type="button" aria-pressed="{"true" if i == sel else "false"}">{t}</button>' for i, t in enumerate(items)) + '</div>')


# ================================================================== list
ROWS = ''.join([
    '<tr class="c-table__row--you">' + who('<a href="purchase-detail--receive.html">MH-0118</a> · HTX Cao Nguyên', '50 hũ muối kiến vàng · về 08:40')
    + cell(sign('you', 'i-alert', 'Về 45/50 · chờ chị')) + cell('Hoá đơn ghi 50 · lệch', 'c-table__cell--hide') + cell('mua chịu 30 ngày') + num('2.000.000 ₫')
    + '<td class="c-table__cell--end"><a class="c-btn" href="purchase-detail--receive.html">Nhận hàng</a></td></tr>',
    '<tr class="c-table__row--you">' + who('<a href="purchase-new.html">MH-0122</a> · Cơ sở Krông Pa', '30 gói bò một nắng · Agent soạn từ tin Zalo')
    + cell(sign('pend', 'i-clock', 'Đề xuất · chờ chị')) + cell('—', 'c-table__cell--hide') + cell('—') + num('5.700.000 ₫')
    + '<td class="c-table__cell--end"><a class="c-btn" href="purchase-new.html">Xem</a></td></tr>',
    '<tr>' + who('<a href="purchase-detail.html">MH-0121</a> · Cơ sở Krông Pa', '40 gói bò một nắng · giao Thứ Năm 08/10')
    + cell('Chưa nhận') + cell('—', 'c-table__cell--hide') + cell('trả trước 3.800.000 ₫') + num('7.600.000 ₫')
    + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="purchase-detail.html">Xem</a></td></tr>',
    '<tr>' + who('<a href="purchase-detail--pay.html">MH-0109</a> · HTX Cao Nguyên', '120 hũ muối kiến vàng · nhận 08/09')
    + cell('Đã nhận đủ') + cell('Có hoá đơn', 'c-table__cell--hide') + cell('còn 2.800.000 ₫ · hạn 08/10') + num('4.800.000 ₫')
    + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="purchase-detail--pay.html">Ghi trả</a></td></tr>',
    '<tr>' + who('<a href="purchase-detail--doc.html">MH-0114</a> · Cơ sở Krông Pa', '50 gói bò một nắng · nhận 15/09')
    + cell('Đã nhận đủ') + cell('<a href="purchase-detail--doc.html">Ảnh phiếu viết tay</a>', 'c-table__cell--hide') + cell('Đã trả đủ') + num('9.500.000 ₫')
    + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="purchase-return.html">Trả hàng</a></td></tr>',
])
TH = ('<thead><tr><th scope="col">Đơn mua</th><th scope="col">Nhận hàng</th><th scope="col" class="c-table__cell--hide">Chứng từ</th>'
      '<th scope="col">Tiền</th><th scope="col" class="c-table__num">Giá trị</th><th scope="col"><span class="u-sr">Việc</span></th></tr></thead>')
LIST = (head('Mua hàng', 'Tháng 10/2026 · phải trả 2.800.000 ₫ · hàng đang về 7.600.000 ₫',
             '<a class="c-btn c-btn--quiet" href="purchase-new.html">Hàng đã về, chưa có đơn</a><a class="c-btn c-btn--act" href="purchase-new.html">Tạo đơn mua</a>')
        + '<div class="page">' + tabs('Đơn mua') + chips(['Tất cả 5', 'Cần chị 2', 'Đang về 1', 'Còn nợ 1', 'Lệch chứng từ 1'])
        + f'<div class="c-table__scroll" tabindex="0" role="region" aria-label="Đơn mua"><table class="c-table c-table--stack r-buy">{TH}<tbody>{ROWS}</tbody></table></div>'
        + '<p class="c-sub">Nhận hàng và trả tiền theo dõi riêng · kho chỉ tăng khi chị xác nhận số thực nhận.</p></div>')
save('purchases', 'Mua hàng · Đơn mua', LIST)


# ================================================================== MH-0121 · ordered, prepaid half, not received
B21 = lines([('Bò một nắng 500g', '40 gói', '190.000 ₫', '7.600.000 ₫')], '7.600.000 ₫')
R21 = ('<p class="c-sub">Chưa nhận · Cơ sở hẹn giao Thứ Năm 08/10. Khi hàng về, chị hoặc anh Khoa đếm và ghi số thực nhận — kho tăng lúc đó.</p>')
D21 = '<p class="c-sub">Chưa có · Cơ sở xuất hoá đơn điện tử khi giao. Hộ chưa nối hộp thư hoá đơn thì chụp ảnh lên đây.</p>'
P21 = ('<dl class="c-kv"><dt>Điều khoản</dt><dd>trả trước 50%, còn lại 15 ngày sau khi nhận</dd>'
       '<dt>Đã trả</dt><dd>3.800.000 ₫ · chuyển khoản 03/10 · khớp sao kê</dd><dt>Còn phải trả</dt><dd><b>3.800.000 ₫</b> · tính hạn từ ngày nhận</dd></dl>')
H21 = tl([('03/10', 'ok', 'Chị An đặt 40 gói', 'gửi Cơ sở qua Zalo OA · Cơ sở xác nhận'), ('03/10', 'ok', 'Trả trước 3.800.000 ₫', 'chuyển khoản · OPC khớp với sao kê'),
          ('08/10', 'pend', 'Hẹn giao', 'kho chỉ tăng khi xác nhận nhận hàng')])
M21 = record('MH-0121', 'Cơ sở Krông Pa', 'Đặt 03/10 · hẹn giao Thứ Năm 08/10 · chị An đặt',
             tracks(('Nhận hàng', 'wait', 'Chưa nhận 0/40'), ('Chứng từ', 'wait', 'Chưa có'), ('Tiền', 'wait', 'Đã trả 3.800.000 · còn 3.800.000 ₫')),
             card('h1', 'Hàng mua', B21) + card('h2', 'Nhận hàng', R21, '<a class="c-btn c-btn--act" href="purchase-detail--receive.html">Nhận hàng</a>')
             + card('h3', 'Chứng từ', D21, '<button class="c-btn" type="button">' + ic('i-photo') + 'Chụp hoá đơn</button>')
             + card('h4', 'Tiền đã trả', P21, '<a class="c-btn" href="purchase-detail--pay.html">Ghi lần trả</a>'), H21,
             '<button class="c-btn c-btn--quiet" type="button">Huỷ đơn</button>')
save('purchase-detail', 'Mua hàng · MH-0121', M21)


# ================================================================== MH-0118 · counting what arrived (45/50), invoice says 50
RECV = ('<div class="r-recv"><ul class="r-pick">' + rline('Muối kiến vàng 100g', 45, 50, 'hũ', 'Thiếu 5 hũ so với đơn', short=True) + '</ul>'
        '<label class="c-field"><span class="c-field__label">Hạn dùng ghi trên hũ <small>(tuỳ chọn)</small></span>'
        '<span class="c-field__control"><input class="c-field__input" value="09/2027"></span></label>'
        '<label class="c-field"><span class="c-field__label">Người nhận</span><span class="c-field__control"><input class="c-field__input" value="anh Khoa"></span></label></div>')
SHORT = ('<div class="c-decide" role="group" aria-labelledby="q-short"><p class="c-decide__q" id="q-short">Thiếu 5 hũ — phần còn lại thế nào?</p>'
         '<div class="c-options" role="radiogroup" aria-label="Phần thiếu">'
         '<button class="c-option" type="button" role="radio" aria-checked="true"><span class="c-option__radio" aria-hidden="true"></span>'
         '<span class="c-option__body"><strong class="c-option__title">Chờ HTX giao bù 5 hũ</strong><span class="c-option__meta">Đơn mở phần 5 hũ · nhận lần 2 vào đơn này</span></span></button>'
         '<button class="c-option" type="button" role="radio" aria-checked="false"><span class="c-option__radio" aria-hidden="true"></span>'
         '<span class="c-option__body"><strong class="c-option__title">Không chờ nữa · đóng phần thiếu</strong><span class="c-option__meta">Đơn chốt 45 hũ · chỉ trả tiền 45 hũ</span></span></button></div>'
         '<p class="c-decide__result">Xác nhận = kho muối <b>+45 hũ</b> (tồn 80 → 125) · phải trả HTX <b>1.800.000 ₫</b>, hạn 05/11 (mua chịu 30 ngày)</p>'
         '<div class="c-decide__acts"><a class="c-btn c-btn--act" href="purchase-detail--received.html">Xác nhận nhận 45 hũ</a>'
         '<button class="c-btn" type="button">Đếm lại</button></div></div>')
DOC18 = ('<figure class="c-quote" style="margin:0"><figcaption class="c-quote__from"><b>Hoá đơn điện tử HTX</b> · nhận qua hộp thư hoá đơn 08:42</figcaption>'
         f'<div class="c-quote__media">{ic("i-file")}<span>HĐ 00000845 · MST 5900112233 · 50 hũ × 40.000 ₫ · <mark>2.000.000 ₫</mark></span></div></figure>'
         '<div class="c-banner c-banner--pend" role="status"><span class="c-banner__pic">' + ic('i-alert') + '</span><span class="c-banner__text">'
         '<strong class="c-banner__title">Hoá đơn ghi 50 hũ, nhận 45</strong><span>Nếu đóng phần thiếu: HTX là bên lập hoá đơn điều chỉnh giảm 200.000 ₫. '
         'Hộ không tự sửa hoá đơn của người bán. Agent soạn tin, chị gửi.</span></span></div>')
H18 = tl([('03/10', 'ok', 'Chị An đặt 50 hũ', 'mua chịu 30 ngày'), ('08:40', 'ok', 'Hàng về · anh Khoa đếm 45', 'chưa vào kho'),
          ('08:42', 'ok', 'Hoá đơn điện tử về', 'OPC đối chiếu với đơn'), ('Bây giờ', 'pend', 'Chờ chị xác nhận số nhận', 'kho tăng một lần khi xác nhận')])
M18 = record('MH-0118', 'HTX Cao Nguyên', 'Đặt 03/10 · về 06/10 08:40 · anh Khoa nhận',
             tracks(('Nhận hàng', 'you', 'Về 45/50 · chờ chị xác nhận'), ('Chứng từ', 'pend', 'Hoá đơn ghi 50 · lệch'), ('Tiền', 'wait', 'Chưa trả · mua chịu 30 ngày')),
             card('h1', 'Nhận hàng · lần 1', RECV, meta='đếm tại kho') + SHORT
             + card('h2', 'Hàng mua', lines([('Muối kiến vàng 100g', '50 hũ', '40.000 ₫', '2.000.000 ₫')], '2.000.000 ₫'))
             + card('h3', 'Chứng từ', DOC18), H18)
save('purchase-detail--receive', 'Mua hàng · Nhận MH-0118', M18)


# ================================================================== MH-0118 · after confirm: +45 in stock, 5 still open, payable 1.800.000
REC2 = ('<ul class="r-pick">' + '<li class="r-pick__l"><span class="r-pick__chk r-pick__chk--ok" aria-hidden="true">' + ic('i-check') + '</span>'
        '<span class="r-pick__name"><b>Lần 1 · 06/10 10:46 · 45 hũ</b><small>anh Khoa nhận · chị An xác nhận · hạn 09/2027</small></span><span class="r-pick__qty"><b>45</b>/50 hũ</span></li>'
        '<li class="r-pick__l"><span class="r-pick__chk" aria-hidden="true"></span><span class="r-pick__name"><b>Còn chờ · 5 hũ</b><small>HTX hẹn giao bù cùng chuyến sau</small></span>'
        '<span class="r-pick__qty">0/5 hũ</span></li></ul>')
DOC2 = ('<dl class="c-kv"><dt>Hoá đơn</dt><dd>HĐ 00000845 · 50 hũ · 2.000.000 ₫</dd><dt>Khớp</dt><dd>Khớp với đơn · khi nhận đủ 50 hũ thì khớp với hàng nhận</dd></dl>')
PAY2 = ('<dl class="c-kv"><dt>Phải trả</dt><dd><b>1.800.000 ₫</b> · theo 45 hũ đã nhận</dd><dt>Hạn</dt><dd>05/11 · mua chịu 30 ngày</dd>'
        '<dt>Khi nhận 5 hũ còn lại</dt><dd>phải trả thêm 200.000 ₫</dd></dl>')
H2 = tl([('03/10', 'ok', 'Chị An đặt 50 hũ', 'mua chịu 30 ngày'), ('08:42', 'ok', 'Hoá đơn điện tử về', 'ghi 50 hũ'),
         ('10:46', 'ok', 'Nhập kho 45 hũ', 'muối: tồn 80 → 125 · chị An xác nhận'), ('—', 'pend', 'Chờ giao bù 5 hũ', 'nhận lần 2 vào đơn này')])
M2 = record('MH-0118', 'HTX Cao Nguyên', 'Đặt 03/10 · nhận lần 1 06/10 · còn chờ 5 hũ',
            '<div class="c-banner c-banner--ok" role="status"><span class="c-banner__pic">' + ic('i-check') + '</span><span class="c-banner__text">'
            '<strong class="c-banner__title">Đã nhập kho 45 hũ muối kiến vàng</strong><span>Khả dụng 50 → 95 hũ · ghi vào sổ kho lúc 10:46 · chị có thể sửa trong hôm nay</span></span></div>'
            + tracks(('Nhận hàng', 'wait', '45/50 · chờ bù 5'), ('Chứng từ', 'ok', 'Có hoá đơn · khớp đơn'), ('Tiền', 'wait', 'Phải trả 1.800.000 ₫ · hạn 05/11')),
            card('h1', 'Nhận hàng', REC2, '<a class="c-btn" href="purchase-detail--receive.html">Nhận lần 2</a>')
            + card('h2', 'Hàng mua', lines([('Muối kiến vàng 100g', '50 hũ', '40.000 ₫', '2.000.000 ₫')], '2.000.000 ₫'))
            + card('h3', 'Chứng từ', DOC2) + card('h4', 'Tiền đã trả', PAY2, '<a class="c-btn" href="purchase-detail--pay.html">Ghi lần trả</a>'), H2,
            '<button class="c-btn" type="button">Đóng phần thiếu</button>')
save('purchase-detail--received', 'Mua hàng · MH-0118 đã nhận', M2)


# ================================================================== MH-0109 · record a payment (partial, 2nd time) — OPC never moves money
PAYS = ('<ul class="r-pick"><li class="r-pick__l"><span class="r-pick__chk r-pick__chk--ok" aria-hidden="true">' + ic('i-check') + '</span>'
        '<span class="r-pick__name"><b>Lần 1 · 15/09 · 2.000.000 ₫</b><small>chuyển khoản · khớp sao kê MB</small></span><span class="r-pick__qty"></span></li></ul>')
FORM = ('<div class="r-recv"><label class="c-field"><span class="c-field__label">Số tiền lần này</span><span class="c-field__control"><input class="c-field__input" inputmode="numeric" value="2.800.000"></span>'
        '<span class="c-field__hint">sửa được · trả một phần thì đơn còn nợ phần còn lại</span></label>'
        '<div class="c-seg" role="radiogroup" aria-label="Cách trả"><button class="c-seg__opt" type="button" role="radio" aria-checked="true">Chuyển khoản</button>'
        '<button class="c-seg__opt" type="button" role="radio" aria-checked="false">Tiền mặt</button></div>'
        '<label class="c-field"><span class="c-field__label">Từ tài khoản</span><span class="c-field__control"><input class="c-field__input" value="MB 0901 2345 678 (đã báo thuế)"></span></label>'
        '<label class="c-field"><span class="c-field__label">Ngày trả</span><span class="c-field__control"><input class="c-field__input" value="06/10/2026"></span></label></div>')
QR = ('<div class="c-banner" role="note"><span class="c-banner__pic">' + ic('i-help') + '</span><span class="c-banner__text">'
      '<strong class="c-banner__title">OPC không chuyển tiền thay chị</strong><span>Chị chuyển bằng app ngân hàng của mình. Có thể mở sẵn mã QR của HTX (tuỳ chọn) — '
      'OPC chỉ ghi lại và khớp với sao kê khi chị bật kết nối ngân hàng.</span></span>'
      '<button class="c-btn" type="button">Mở mã QR của HTX</button></div>')
ACT = ('<div class="r-form__acts"><p class="c-decide__result">Lưu = MH-0109 <b>đã trả đủ 4.800.000 ₫</b> · công nợ HTX còn 1.800.000 ₫ (MH-0118, hạn 05/11)</p>'
       '<button class="c-btn c-btn--act" type="button">Lưu lần trả</button><a class="c-btn" href="purchases.html">Huỷ</a></div>')
H3 = tl([('08/09', 'ok', 'Nhận đủ 120 hũ', 'nhập kho · có hoá đơn'), ('15/09', 'ok', 'Trả lần 1 · 2.000.000 ₫', 'chuyển khoản'),
         ('08/10', 'pend', 'Hạn trả phần còn lại', 'còn 2 ngày')])
M3 = record('MH-0109', 'HTX Cao Nguyên', 'Nhận 08/09 · mua chịu 30 ngày · hạn 08/10',
            tracks(('Nhận hàng', 'ok', 'Đã nhận đủ 120/120'), ('Chứng từ', 'ok', 'Có hoá đơn · khớp'), ('Tiền', 'you', 'Còn 2.800.000 / 4.800.000 ₫ · hạn 08/10')),
            card('h4', 'Tiền đã trả', PAYS) + card('h5', 'Ghi lần trả 2', FORM + QR + ACT), H3)
save('purchase-detail--pay', 'Mua hàng · Ghi trả MH-0109', M3)


# ================================================================== new purchase · Agent proposal MH-0122 (owner approves) + "hàng đã về, chưa có đơn"
NEWF = ('<div class="r-recv"><div class="c-seg" role="radiogroup" aria-label="Loại"><button class="c-seg__opt" type="button" role="radio" aria-checked="true">Đặt hàng trước</button>'
        '<button class="c-seg__opt" type="button" role="radio" aria-checked="false">Hàng đã về, chưa có đơn</button></div>'
        '<label class="c-field"><span class="c-field__label">Nhà cung cấp</span><span class="c-field__control"><input class="c-field__input" value="Cơ sở bò một nắng Krông Pa"></span></label>'
        + lines([('Bò một nắng 500g', '30 gói', '190.000 ₫', '5.700.000 ₫')], '5.700.000 ₫')
        + '<button class="c-btn c-btn--quiet" type="button">' + ic('i-plus') + 'Thêm món</button>'
        '<div class="c-seg" role="radiogroup" aria-label="Thanh toán"><button class="c-seg__opt" type="button" role="radio" aria-checked="false">Trả khi nhận</button>'
        '<button class="c-seg__opt" type="button" role="radio" aria-checked="true">Mua chịu</button><button class="c-seg__opt" type="button" role="radio" aria-checked="false">Trả trước một phần</button></div>'
        '<label class="c-field"><span class="c-field__label">Hạn trả</span><span class="c-field__control"><input class="c-field__input" value="15 ngày sau khi nhận"></span></label>'
        '<label class="c-field"><span class="c-field__label">Hẹn giao</span><span class="c-field__control"><input class="c-field__input" value="Thứ Ba 13/10"></span></label></div>')
WHY = ('<figure class="c-quote" style="margin:0"><figcaption class="c-quote__from"><b>Agent đề xuất</b> · 09:10</figcaption>'
       '<div class="c-quote__media">' + ic('i-chat') + '<span>Bò một nắng còn 26 gói khả dụng sau đơn Phố Núi; 7 ngày qua bán trung bình 6 gói/ngày. '
       'Cơ sở Krông Pa báo giá 190.000 ₫/gói qua Zalo OA hôm qua.</span></div></figure>')
NACT = ('<div class="r-form__acts"><p class="c-decide__result">Đặt = gửi đơn cho Cơ sở (Agent soạn tin, chị bấm gửi) · kho chưa đổi · chưa phải trả gì tới khi nhận</p>'
        '<a class="c-btn c-btn--act" href="purchase-detail--placed.html">Đặt hàng</a><button class="c-btn" type="button">Lưu nháp</button>'
        '<a class="c-btn c-btn--quiet" href="purchases.html">Bỏ đề xuất</a></div>')
HN = tl([('Hôm qua', 'ok', 'Cơ sở báo giá 190.000 ₫', 'tin Zalo OA'), ('09:10', 'ok', 'Agent soạn đề xuất', 'chưa gửi ai'), ('Bây giờ', 'pend', 'Chờ chị duyệt', 'Agent không tự đặt hàng')])
MN = ('<div class="page"><nav class="c-crumbs" aria-label="Đường dẫn"><a href="purchases.html">Đơn mua</a><span aria-current="page">Đơn mua mới</span></nav>'
      + head('MH-0122 · đề xuất', 'Agent soạn · chị duyệt rồi mới gửi')
      + '<div class="r-detail__grid r-detail--calm"><div class="stack">' + card('n1', 'Đơn mua', NEWF) + NACT + '</div>'
      '<aside class="r-tower__detail" aria-labelledby="nw"><h2 class="r-tower__t" id="nw">Vì sao đề xuất</h2>' + WHY + HN + '</aside></div></div>')
save('purchase-new', 'Mua hàng · Đơn mua mới', MN)


# ================================================================== return to supplier · MH-0114, 2 gói hỏng bao (already paid in full)
RL = ('<ul class="r-pick">' + rline('Bò một nắng 500g', 1, 50, 'gói', 'Rách bao, phát hiện khi kiểm kho hôm nay', short=True) + '</ul>'
      '<label class="c-field"><span class="c-field__label">Lý do</span><span class="c-field__control"><input class="c-field__input" value="Hàng lỗi · rách bao hút chân không"></span></label>'
      '<div class="c-seg" role="radiogroup" aria-label="Nhà cung cấp hoàn lại"><button class="c-seg__opt" type="button" role="radio" aria-checked="true">Trừ vào lần mua sau</button>'
      '<button class="c-seg__opt" type="button" role="radio" aria-checked="false">Trả lại tiền</button><button class="c-seg__opt" type="button" role="radio" aria-checked="false">Đổi hàng mới</button></div>'
      '<button class="c-btn" type="button">' + ic('i-photo') + 'Chụp biên bản trả hàng (có chữ ký 2 bên)</button>')
RDOC = ('<div class="c-banner c-banner--pend" role="status"><span class="c-banner__pic">' + ic('i-file') + '</span><span class="c-banner__text">'
        '<strong class="c-banner__title">Cơ sở Krông Pa lập hoá đơn điều chỉnh giảm 190.000 ₫</strong>'
        '<span>Người bán lập hoá đơn gốc HĐ 00000312 nên người bán điều chỉnh; hộ giữ biên bản. Cách lập chờ kế toán xác nhận.</span></span>'
        '<button class="c-btn c-btn--quiet" type="button">' + ic('i-send') + 'Agent soạn tin</button></div>')
RACT = ('<div class="r-form__acts"><p class="c-decide__result">Xác nhận = kho bò <b>−1 gói</b> (xuất trả, không phải bán) · Cơ sở nợ lại hộ <b>190.000 ₫</b>, tự trừ vào MH-0121</p>'
        '<button class="c-btn c-btn--act" type="button">Xác nhận trả hàng</button><a class="c-btn" href="purchases.html">Huỷ</a></div>')
HR = tl([('15/09', 'ok', 'Nhận đủ 50 gói · đã trả 9.500.000 ₫', 'MH-0114'), ('10:20', 'ok', 'Kiểm kho: 1 gói rách bao', 'chị An duyệt · tách khỏi hàng bán'),
         ('Bây giờ', 'pend', 'Phiếu trả TH-0003 · chờ chị xác nhận', 'chưa trừ kho')])
MR = ('<div class="page"><nav class="c-crumbs" aria-label="Đường dẫn"><a href="purchases.html">Đơn mua</a><span aria-current="page">Trả hàng TH-0003</span></nav>'
      + head('Trả hàng cho Cơ sở Krông Pa', 'TH-0003 · từ đơn MH-0114 · 1 gói × 190.000 ₫')
      + tracks(('Hàng trả', 'you', '1 gói · chờ chị xác nhận'), ('Chứng từ', 'wait', 'Chờ hoá đơn điều chỉnh'), ('Tiền', 'wait', 'Cơ sở nợ lại 190.000 ₫'))
      + '<div class="r-detail__grid r-detail--calm"><div class="stack">' + card('t1', 'Hàng trả lại', '<div class="r-recv">' + RL + '</div>') + card('t2', 'Chứng từ', RDOC) + RACT + '</div>'
      '<aside class="r-tower__detail" aria-labelledby="hr"><h2 class="r-tower__t" id="hr">Diễn biến</h2>' + HR + '</aside></div></div>')
save('purchase-return', 'Mua hàng · Trả hàng TH-0003', MR)


# ================================================================== expenses (moved from pages_purchase.py)
EX = ''.join([
    '<tr>' + who('Tiền điện tháng 9 · Điện lực Gia Lai', 'Điện · ảnh hoá đơn chị An chụp') + num('1.250.000 ₫') + cell(sign('wait', 'i-clock', 'Chưa trả · hạn 10/10')) + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="receivables--payables.html">Trả</a></td></tr>',
    '<tr>' + who('Túi hút chân không 1.000 cái · Bao bì Phú Mỹ', 'Bao bì · có hoá đơn điện tử') + num('850.000 ₫') + cell(sign('ok', 'i-check', 'Đã trả tiền mặt 02/10')) + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
    '<tr>' + who('Xăng xe giao hàng tuần 40', 'Vận chuyển · biên lai, không có hoá đơn') + num('850.000 ₫') + cell(sign('ok', 'i-check', 'Đã trả 04/10')) + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
])
LIST = (head('Chi phí', 'Tháng 10/2026 · chi phí không qua kho', '<a class="c-btn c-btn--act" href="purchases--expense.html">' + ic('i-photo') + 'Chụp hoá đơn chi phí</a>') + '<div class="page">' + tabs('Chi phí')
        + '<div class="c-table__scroll" tabindex="0" role="region" aria-label="Chi phí"><table class="c-table c-table--stack"><thead><tr><th scope="col">Chi phí</th><th scope="col" class="c-table__num">Số tiền</th><th scope="col">Tình trạng</th><th scope="col"><span class="u-sr">Việc</span></th></tr></thead><tbody>' + EX + '</tbody></table></div>'
        + '<p class="c-sub">Chi phí không cộng vào giá vốn hàng · chỉ dùng cho sổ chi phí khi kế toán xác nhận hộ thuộc nhóm cần ghi.</p></div>')
DLG = ('<div class="c-dialog" role="dialog" aria-modal="true" aria-labelledby="ex-t"><div class="c-dialog__panel">'
       '<div class="c-dialog__head"><div><span class="c-dialog__k">Chi phí không qua kho</span><h2 class="c-dialog__title" id="ex-t" tabindex="-1">Hoá đơn tiền điện</h2></div>'
       f'<a class="c-icon-btn" href="purchases--expense.html" aria-label="Đóng, không lưu">{ic("i-x")}</a></div>'
       '<div class="c-dialog__body">'
       '<div class="r-capture"><figure class="r-capture__thumb" role="img" aria-label="Ảnh hoá đơn tiền điện EVN kỳ 09/2026, 1.250.000 đồng"><span class="r-capture__logo" aria-hidden="true">EVN</span><i></i><i></i><i class="s"></i><i></i><b aria-hidden="true">1.250.000</b></figure>'
       '<p class="c-quote__from"><b>Ảnh chị An chụp</b> · Trợ lý đã đọc · chắc chắn</p></div>'
       '<dl class="c-kv"><dt>Nhà cung cấp</dt><dd>Điện lực Gia Lai · MST 0300942001-012</dd><dt>Số tiền</dt><dd>1.250.000 ₫</dd>'
       '<dt>Nhóm chi phí</dt><dd><button class="c-btn r-capture__pick" type="button" aria-haspopup="listbox">Điện, nước · Trợ lý đoán' + ic('i-chev') + '</button></dd><dt>Chứng từ</dt><dd>Hoá đơn điện tử · lấy được từ cổng thuế khi hộ bật kết nối</dd></dl>'
       '<div class="c-seg" role="radiogroup" aria-label="Thanh toán"><button class="c-seg__opt" type="button" role="radio" aria-checked="true">Trả sau · hạn 10/10</button>'
       '<button class="c-seg__opt" type="button" role="radio" aria-checked="false">Đã trả rồi</button></div></div>'
       '<div class="c-dialog__foot"><p class="c-decide__result">Lưu = chi phí tháng 10 · phải trả <b>1.250.000 ₫</b> hạn 10/10</p>'
       '<button class="c-btn c-btn--act" type="button">Lưu chi phí</button></div></div></div>')
save('purchases--expense', 'Mua hàng · Chi phí', LIST, overlay=DLG)


# ================================================================== handwritten delivery note: photo + manual entry (no OCR in pilot)
PH = ('<div class="r-capture"><figure class="r-capture__thumb" role="img" aria-label="Ảnh phiếu giao hàng viết tay của Cơ sở Krông Pa, 15/09, 50 gói bò một nắng">'
      '<span class="r-capture__logo" aria-hidden="true">Phiếu giao</span><i></i><i></i><i class="s"></i><i></i><b aria-hidden="true">9.500.000</b></figure>'
      '<div class="r-recv"><p class="c-quote__from"><b>Ảnh anh Khoa chụp</b> · 15/09 16:10</p>'
      '<p class="c-sub">Phiếu viết tay, không phải hoá đơn. OPC chưa đọc chữ viết tay: chị nhập số theo phiếu, OPC so với đơn và hàng đã nhận.</p></div></div>')
MAN = ('<div class="r-form2"><label class="c-field"><span class="c-field__label">Ngày trên phiếu</span><span class="c-field__control"><input class="c-field__input" value="15/09/2026"></span></label>'
       '<label class="c-field"><span class="c-field__label">Số tiền</span><span class="c-field__control"><input class="c-field__input" inputmode="numeric" value="9.500.000"></span></label>'
       '<label class="c-field"><span class="c-field__label">Món · số lượng</span><span class="c-field__control"><input class="c-field__input" value="Bò một nắng 500g · 50 gói"></span></label>'
       '<label class="c-field"><span class="c-field__label">Người bán ký</span><span class="c-field__control"><input class="c-field__input" value="có chữ ký, tên Y Blông"></span></label></div>')
CHK = ('<ul class="c-rules" aria-label="So khớp"><li class="c-rules__r">' + ic('i-check') + 'Khớp đơn MH-0114 · 50 gói × 190.000 ₫<span class="u-sr"> khớp</span></li>'
       '<li class="c-rules__r">' + ic('i-check') + 'Khớp số đã nhận 50/50<span class="u-sr"> khớp</span></li></ul>'
       '<div class="c-banner" role="note"><span class="c-banner__pic">' + ic('i-help') + '</span><span class="c-banner__text"><strong class="c-banner__title">Muốn có hoá đơn?</strong>'
       '<span>Cơ sở có thể xuất hoá đơn điện tử sau. Có thì OPC gắn vào đơn, ảnh phiếu vẫn lưu làm bằng chứng. Kế toán quyết định có cần bảng kê hàng mua không hoá đơn.</span></span>'
       '<button class="c-btn c-btn--quiet" type="button">' + ic('i-send') + 'Agent soạn tin xin hoá đơn</button></div>')
DA = ('<div class="r-form__acts"><p class="c-decide__result">Lưu = chứng từ của MH-0114 là <b>ảnh phiếu viết tay + số chị nhập</b> · lưu 10 năm cùng sổ</p>'
      '<button class="c-btn c-btn--act" type="button">Lưu chứng từ</button><a class="c-btn" href="purchases.html">Huỷ</a></div>')
HD = tl([('15/09', 'ok', 'Nhận đủ 50 gói', 'anh Khoa'), ('15/09', 'ok', 'Chụp phiếu giao hàng', 'chưa nhập số'), ('Bây giờ', 'pend', 'Chị nhập số theo phiếu', 'OPC so khớp với đơn')])
MD = record('MH-0114', 'Cơ sở Krông Pa', 'Nhận 15/09 · đã trả đủ 9.500.000 ₫',
            tracks(('Nhận hàng', 'ok', 'Đã nhận đủ 50/50'), ('Chứng từ', 'you', 'Ảnh phiếu · chờ nhập số'), ('Tiền', 'ok', 'Đã trả đủ')),
            card('c1', 'Chứng từ', PH + MAN) + CHK + DA, HD)
save('purchase-detail--doc', 'Mua hàng · Chứng từ viết tay MH-0114', MD)


# ================================================================== MH-0122 placed (after "Đặt hàng"): sent, waiting for the supplier
T22 = tracks(('Nhận hàng', 'wait', 'Chưa nhận 0/30 · hẹn 13/10'), ('Chứng từ', 'wait', 'Chưa có'), ('Tiền', 'wait', 'Mua chịu 15 ngày sau khi nhận'))
OK22 = ('<div class="c-banner c-banner--ok" role="status"><span class="c-banner__pic">' + ic('i-check') + '</span><span class="c-banner__text">'
        '<strong class="c-banner__title">Đã gửi đơn MH-0122 cho Cơ sở Krông Pa</strong><span>Chị gửi qua Zalo OA lúc 10:47 · kho chưa đổi, chưa phải trả gì</span></span></div>')
H22 = tl([('09:10', 'ok', 'Agent soạn đề xuất', 'chưa gửi ai'), ('10:46', 'ok', 'Chị An duyệt và đặt', '30 gói × 190.000 ₫'), ('10:47', 'ok', 'Chị gửi tin qua Zalo OA', 'Agent soạn, chị bấm gửi'),
          ('13/10', 'wait', 'Hẹn giao', 'Cơ sở chưa xác nhận')])
M22 = record('MH-0122', 'Cơ sở Krông Pa', 'Đặt 06/10 10:46 · hẹn giao Thứ Ba 13/10', OK22 + T22,
             card('h1', 'Hàng mua', lines([('Bò một nắng 500g', '30 gói', '190.000 ₫', '5.700.000 ₫')], '5.700.000 ₫'))
             + card('h2', 'Nhận hàng', '<p class="c-sub">Khi hàng về, đếm và ghi số thực nhận — kho tăng lúc đó.</p>', '<a class="c-btn" href="purchase-detail--receive.html">Nhận hàng</a>')
             + '<div class="r-form__acts"><a class="c-btn c-btn--act" href="purchases.html">Về danh sách đơn mua</a><button class="c-btn c-btn--quiet" type="button">Sửa đơn</button></div>', H22)
save('purchase-detail--placed', 'Mua hàng · MH-0122 đã gửi', M22)


# ================================================================== add a supplier (Sẵn sàng: "khách và nhà cung cấp" is mandatory)
SF = ('<div class="r-form2">'
      + ''.join(f'<label class="c-field"><span class="c-field__label">{l}</span><span class="c-field__control"><input class="c-field__input" value="{v}"{m}></span>'
                f'{"<span class=c-field__hint>" + h + "</span>" if h else ""}</label>'
                for l, v, h, m in [('Tên nhà cung cấp', 'Cơ sở bò một nắng Krông Pa', '', ''), ('Mã số thuế (tuỳ chọn)', '6001234567', 'OPC tra tên đơn vị · không có thì để trống', ' inputmode="numeric"'),
                                   ('Người liên hệ', 'anh Y Blông · 0905 223 118', '', ''), ('Hàng mua', 'Bò một nắng 500g', 'chọn từ danh sách hàng', ''),
                                   ('Điều khoản trả', 'trả trước 50%, còn lại 15 ngày', '', ''), ('Tài khoản nhận tiền của họ', 'Agribank 5300 2051 7788', 'để mở sẵn mã QR khi chị trả', '')])
      + '</div><label class="r-chkrow"><span class="c-check"><input type="checkbox" checked></span><span>Họ có xuất hoá đơn điện tử <small class="u-meta">· OPC nhắc xin hoá đơn khi nhận hàng</small></span></label>')
SA = ('<div class="r-form__acts"><p class="c-decide__result">Lưu = nhà cung cấp dùng được khi tạo đơn mua · Sẵn sàng: việc "khách và nhà cung cấp" xong phần nhà cung cấp</p>'
      '<a class="c-btn c-btn--act" href="suppliers.html">Lưu nhà cung cấp</a><a class="c-btn" href="suppliers.html">Huỷ</a></div>')
SN = ('<div class="page"><nav class="c-crumbs" aria-label="Đường dẫn"><a href="suppliers.html">Nhà cung cấp</a><span aria-current="page">Thêm nhà cung cấp</span></nav>'
      + head('Thêm nhà cung cấp', 'Chụp danh thiếp hoặc hoá đơn cũ thì OPC điền giúp', '<button class="c-btn" type="button">' + ic('i-photo') + 'Chụp để điền</button>')
      + '<div class="r-detail__grid r-detail--calm"><div class="stack">' + card('n1', 'Thông tin', SF) + SA + '</div>'
      '<aside class="r-tower__detail" aria-labelledby="sd"><h2 class="r-tower__t" id="sd">Dùng để làm gì</h2><p class="c-sub">Đơn mua, công nợ phải trả và sổ chi phí. '
      'Số tài khoản của họ chỉ để mở mã QR; OPC không chuyển tiền.</p></aside></div></div>')
save('supplier-new', 'Mua hàng · Thêm nhà cung cấp', SN)

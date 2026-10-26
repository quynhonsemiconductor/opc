"""v7.3.0 · Bán hàng (Order-to-Cash), đợt 3. BA verdicts (E2E-SCOPE): an order has 4 independent tracks Đơn · Giao · Hoá đơn · Tiền;
confirm only within available stock; "Đã giao" = delivered in full → stock out once + one e-invoice (NĐ 123/2020 Điều 9 as amended);
leftover = a new order; credit is information only; price edits are shown as "đã sửa so với bảng giá"; the order closes when money is linked.
Writes order-detail (+ --invoice, --invoice-error, --return).  Usage: python3 pages_sell7.py"""
from erp_lib import *

SEC = 'orders'
CR = ('Đơn bán', 'orders.html')
GOODS = lines([('Bò một nắng 500g', '20 gói', '230.000 ₫', '4.600.000 ₫'), ('Muối kiến vàng 100g', '30 hũ', '55.000 ₫', '1.650.000 ₫')],
              '6.250.000 ₫', label='Hàng bán', price='Giá bán')
BUYER = ('<dl class="c-kv"><dt>Người mua</dt><dd>Công ty TNHH Sunrise Pleiku · MST 5900987654</dd>'
         '<dt>Địa chỉ</dt><dd>12 Trần Hưng Đạo, Pleiku</dd><dt>Gửi hoá đơn tới</dt><dd>ketoan@sunrisehotel.vn</dd></dl>')


def order(sub, trk, body, side, acts='', banner=''):
    return record('DH-2052', 'Sunrise Hotel', sub, banner + trk, body, side, acts, crumb=CR)


# ================================================================== DH-2052 · confirmed, goods held, delivering today
T1 = tracks(('Đơn', 'ok', 'Đã xác nhận · giữ hàng'), ('Giao', 'wait', 'Chờ giao · trước 15:00 · anh Hùng'),
            ('Hoá đơn', 'wait', 'Lập khi đã giao'), ('Tiền', 'wait', 'Chưa thu · trả sau 15 ngày'))
G1 = ('<dl class="c-kv"><dt>Người giao</dt><dd>anh Hùng · xe máy</dd><dt>Hẹn</dt><dd>trước 15:00 hôm nay · cổng bếp</dd>'
      '<dt>Kho</dt><dd>đã giữ 20 gói bò, 30 hũ muối · trừ kho khi giao đủ</dd></dl>')
I1 = (BUYER + '<p class="c-sub">Khách cần hoá đơn công ty. OPC lập một hoá đơn điện tử khi chị bấm "Đã giao".</p>')
M1 = ('<dl class="c-kv"><dt>Điều khoản</dt><dd>trả sau 15 ngày · chuyển khoản</dd>'
      '<dt>Khách đang nợ</dt><dd>8.400.000 ₫ (các đơn trước) · chỉ để chị biết, không chặn đơn</dd></dl>')
H1 = tl([('09:02', 'ok', 'Sunrise nhắn qua Zalo OA', '20 gói bò, 30 hũ muối'), ('09:03', 'ok', 'Agent soạn đơn', 'giá khách sạn · đủ tồn'),
         ('09:15', 'ok', 'Chị An xác nhận · giữ hàng', 'khả dụng bò 46 → 26'), ('15:00', 'wait', 'Hẹn giao trước 15:00', 'anh Hùng')])
O1 = order('Đặt 06/10 09:02 qua Zalo OA · giao trước 15:00 hôm nay', T1,
           card('s1', 'Hàng bán', GOODS, meta='giá theo bảng giá khách sạn')
           + card('s2', 'Giao hàng', G1, '<a class="c-btn c-btn--act" href="delivery--pick.html">Soạn hàng</a><a class="c-btn" href="order-detail--delivering.html">Đã soạn đủ · bàn giao</a>')
           + card('s3', 'Hoá đơn', I1) + card('s4', 'Tiền', M1), H1,
           '<button class="c-btn c-btn--quiet" type="button">Huỷ đơn</button>')
save('order-detail', 'Đơn bán · DH-2052', O1, sec=SEC)
print('sell7: detail')


# ================================================================== delivered in full → stock out once + one e-invoice issued
T2 = tracks(('Đơn', 'ok', 'Đã xác nhận'), ('Giao', 'ok', 'Đã giao đủ 14:40'), ('Hoá đơn', 'ok', 'Đã lập · có mã cơ quan thuế'), ('Tiền', 'wait', 'Chưa thu · hạn 21/10'))
BN2 = ('<div class="c-banner c-banner--ok" role="status"><span class="c-banner__pic">' + ic('i-check') + '</span><span class="c-banner__text">'
       '<strong class="c-banner__title">Đã giao đủ · đã trừ kho · đã lập hoá đơn</strong><span>Bò 46 → 26 gói, muối 125 → 95 hũ · hoá đơn đã gửi tới ketoan@sunrisehotel.vn</span></span></div>')
G2 = ('<dl class="c-kv"><dt>Đã giao</dt><dd>14:40 · anh Hùng · đủ 20 gói, 30 hũ</dd><dt>Bằng chứng</dt><dd>ảnh người nhận ký · chị Mai, lễ tân</dd></dl>')
I2 = (BUYER.replace('</dl>', '') + '<dt>Hoá đơn</dt><dd>số 00000128 · ký hiệu 1C26TAN · 6.250.000 ₫</dd><dt>Mã cơ quan thuế</dt><dd>đã cấp 14:41</dd></dl>')
M2 = ('<dl class="c-kv"><dt>Phải thu</dt><dd><b>6.250.000 ₫</b> · hạn 21/10</dd><dt>Khi khách chuyển</dt><dd>OPC khớp với sao kê nếu đã nối ngân hàng · '
      'một lần chuyển trả được nhiều đơn</dd></dl>')
H2 = tl([('09:15', 'ok', 'Chị An xác nhận · giữ hàng', ''), ('14:40', 'ok', 'Anh Hùng giao đủ', 'trừ kho một lần'),
         ('14:41', 'ok', 'Hoá đơn 00000128 được cấp mã', 'gửi khách qua email'), ('21/10', 'pend', 'Hạn thu tiền', 'đơn đóng khi gắn được tiền')])
O2 = order('Đặt 06/10 09:02 · giao 14:40 · trả sau 15 ngày', T2,
           card('s2', 'Giao hàng', G2) + card('s3', 'Hoá đơn', I2, '<a class="c-btn" href="invoice-detail.html">Xem hoá đơn</a>')
           + card('s4', 'Tiền', M2, '<button class="c-btn c-btn--quiet" type="button">' + ic('i-send') + 'Agent soạn nhắc</button>') + card('s1', 'Hàng bán', GOODS), H2,
           '<a class="c-btn" href="order-detail--return.html">Khách trả hàng</a>', banner=BN2)
save('order-detail--invoice', 'Đơn bán · DH-2052 đã giao', O2, sec=SEC)


# ================================================================== invoice rejected by the provider (buyer tax code wrong) — goods are delivered, only the invoice track is red
T3 = tracks(('Đơn', 'ok', 'Đã xác nhận'), ('Giao', 'ok', 'Đã giao đủ 14:40'), ('Hoá đơn', 'err', 'Chưa cấp mã · MST người mua sai'), ('Tiền', 'wait', 'Chưa thu · hạn 21/10'))
FIX = ('<div class="c-decide" role="group" aria-labelledby="q-inv"><p class="c-decide__q" id="q-inv">Cơ quan thuế không cấp mã: MST 5900987645 không tồn tại</p>'
       '<label class="c-field"><span class="c-field__label">MST người mua</span><span class="c-field__control"><input class="c-field__input" value="5900987654"></span>'
       '<span class="c-field__hint">OPC tra được: Công ty TNHH Sunrise Pleiku · đang hoạt động</span></label>'
       '<p class="c-decide__result">Gửi lại = cùng một hoá đơn, chưa có mã nên chưa cần hoá đơn điều chỉnh · kho và tiền không đổi</p>'
       '<div class="c-decide__acts"><a class="c-btn c-btn--act" href="order-detail--invoice.html">Sửa và gửi lại</a>'
       '<button class="c-btn" type="button">' + ic('i-send') + 'Hỏi lại khách</button></div></div>')
H3 = tl([('14:40', 'ok', 'Anh Hùng giao đủ', 'trừ kho một lần'), ('14:41', 'err', 'Cơ quan thuế từ chối cấp mã', 'MST người mua sai 2 số cuối'),
         ('Bây giờ', 'pend', 'Chờ chị sửa', 'Kết nối hoá đơn vẫn hoạt động')])
O3 = order('Đặt 06/10 09:02 · giao 14:40', T3, FIX + card('s3', 'Hoá đơn', BUYER) + card('s1', 'Hàng bán', GOODS), H3)
save('order-detail--invoice-error', 'Đơn bán · DH-2052 hoá đơn lỗi', O3, sec=SEC)
print('sell7: detail, invoice, invoice-error')


# ================================================================== customer returns 2 bags (minimal return) — hộ is the seller, so hộ issues the adjustment invoice
T4 = tracks(('Đơn', 'ok', 'Đã giao · có hàng trả'), ('Hàng trả', 'you', '2 gói · chờ chị xác nhận'), ('Hoá đơn', 'wait', 'Nháp điều chỉnh giảm 460.000 ₫'), ('Tiền', 'wait', 'Phải thu 6.250.000 → 5.790.000 ₫'))
RT = ('<div class="r-recv"><ul class="r-pick">' + rline('Bò một nắng 500g', 2, 20, 'gói', 'Khách báo: giao dư so với thực đơn tuần này', short=True) + '</ul>'
      '<div class="c-seg" role="radiogroup" aria-label="Tình trạng hàng trả"><button class="c-seg__opt" type="button" role="radio" aria-checked="true">Còn tốt · nhập lại kho</button>'
      '<button class="c-seg__opt" type="button" role="radio" aria-checked="false">Hỏng · không bán lại</button></div>'
      '<div class="c-seg" role="radiogroup" aria-label="Tiền"><button class="c-seg__opt" type="button" role="radio" aria-checked="true">Trừ vào tiền khách nợ</button>'
      '<button class="c-seg__opt" type="button" role="radio" aria-checked="false">Trả lại tiền cho khách</button></div></div>')
RI = ('<div class="c-banner c-banner--pend" role="status"><span class="c-banner__pic">' + ic('i-file') + '</span><span class="c-banner__text">'
      '<strong class="c-banner__title">Hộ lập hoá đơn điều chỉnh giảm 460.000 ₫ · bản nháp</strong>'
      '<span>Hộ là người bán của hoá đơn 00000128. OPC soạn sẵn; chị kiểm rồi ký gửi qua bên hoá đơn điện tử. Cách lập chờ kế toán xác nhận.</span></span></div>')
RA = ('<div class="r-form__acts"><p class="c-decide__result">Xác nhận (còn tốt) = kho bò <b>+2 gói</b> (26 → 28) · mở nháp hoá đơn điều chỉnh để chị ký · Sunrise còn phải trả <b>5.790.000 ₫</b>. Chọn "Hỏng" thì không cộng kho, ghi hao hụt.</p>'
      '<button class="c-btn c-btn--act" type="button">Xác nhận trả hàng</button><a class="c-btn" href="order-detail--invoice.html">Huỷ</a></div>')
H4 = tl([('14:40', 'ok', 'Giao đủ · hoá đơn 00000128', 'trừ kho một lần'), ('16:05', 'ok', 'Sunrise nhắn trả 2 gói', 'Zalo OA · có ảnh'),
         ('Bây giờ', 'pend', 'Chờ chị xác nhận', 'chưa đổi kho, chưa điều chỉnh')])
O4 = order('Giao 14:40 · khách trả 2 gói lúc 16:05', T4, card('r1', 'Hàng khách trả', RT) + card('r2', 'Hoá đơn', RI) + RA + card('s1', 'Hàng bán', GOODS), H4)
save('order-detail--return', 'Đơn bán · DH-2052 khách trả hàng', O4, sec=SEC)
print('sell7: detail, invoice, invoice-error, return')


# ================================================================== Bán nhanh (replaces Quầy + Đóng ca): sale, handover and payment in one go → one order record
def qline(name, price, n, unit, ro=False):
    if ro:
        return (f'<li class="r-pick__l"><span class="r-pick__name"><b>{name}</b><small>{n} {unit} × {price}</small></span><span></span>'
                f'<span class="r-pick__qty"><b>{n * int(price.replace(".", "").split()[0]):,} ₫</b></span></li>'.replace(',', '.'))
    return (f'<li class="r-pick__l"><span class="r-pick__name"><b>{name}</b><small>{price} / {unit}</small></span>'
            f'<span class="r-step" role="group" aria-label="Số lượng {name}"><button class="c-icon-btn" type="button" aria-label="Bớt 1">{ic("i-minus")}</button>'
            f'<b aria-live="polite">{n}</b><button class="c-icon-btn" type="button" aria-label="Thêm 1">{ic("i-plus")}</button></span>'
            f'<span class="r-pick__qty"><b>{n * int(price.replace(".", "").split()[0]):,} ₫</b></span></li>'.replace(',', '.'))


PICKS = ('<div class="r-quick__goods" role="group" aria-label="Thêm nhanh">'
         + ''.join(f'<button class="c-btn" type="button">{ic("i-plus")}{n}<small class="u-meta"> · còn {k}</small></button>' for n, k in [('Bò một nắng 500g', '26'), ('Muối kiến vàng 100g', '50')])
         + '</div>')
CART = ('<ul class="r-pick">' + qline('Bò một nắng 500g', '260.000 ₫', 2, 'gói') + qline('Muối kiến vàng 100g', '65.000 ₫', 3, 'hũ') + '</ul>'
        '<p class="r-quick__total"><span>Tổng · giá lẻ</span><b>715.000 ₫</b></p>')
CART_RO = ('<ul class="r-pick">' + qline('Bò một nắng 500g', '260.000 ₫', 2, 'gói', True) + qline('Muối kiến vàng 100g', '65.000 ₫', 3, 'hũ', True) + '</ul>'
           '<p class="r-quick__total"><span>Tổng · giá lẻ</span><b>715.000 ₫</b></p>')
PAYQ = ('<div class="r-recv"><div class="c-seg" role="radiogroup" aria-label="Khách trả bằng"><button class="c-seg__opt" type="button" role="radio" aria-checked="true">Chuyển khoản QR</button>'
        '<button class="c-seg__opt" type="button" role="radio" aria-checked="false">Tiền mặt</button><button class="c-seg__opt" type="button" role="radio" aria-checked="false">Ghi nợ</button></div>'
        '<label class="r-chkrow"><span class="c-check"><input type="checkbox"></span><span>Khách cần hoá đơn <small class="u-meta">· nhập tên, MST hoặc số định danh</small></span></label></div>')
QA = ('<div class="r-form__acts"><p class="c-decide__result">Thu = đơn DH-2053 giao ngay tại chỗ · kho trừ một lần (bò khả dụng 26 → 24) · tiền ghi khi khớp</p>'
      '<a class="c-btn c-btn--act" href="quick-sale--qr.html">Thu 715.000 ₫</a><button class="c-btn" type="button">Lưu nháp</button></div>')
Q1 = (head('Bán nhanh', 'Khách mua tại chỗ · giao và thu tiền ngay · thành một đơn bán như mọi đơn')
      + '<div class="page"><div class="r-detail__grid r-detail--calm"><div class="stack">'
      + card('q1', 'Khách lẻ', '<label class="c-field"><span class="c-field__label">Tìm món</span><span class="c-field__control"><input class="c-field__input" placeholder="Tên món hoặc quét mã"></span></label>' + PICKS)
      + card('q2', 'Giỏ hàng', CART, meta='giá lẻ theo bảng giá') + card('q3', 'Thanh toán', PAYQ) + QA + '</div>'
      '<aside class="r-tower__detail" aria-labelledby="qh"><h2 class="r-tower__t" id="qh">Hôm nay</h2><dl class="c-kv"><dt>Bán nhanh</dt><dd>5 đơn · 1.950.000 ₫</dd>'
      '<dt>Tiền mặt</dt><dd>520.000 ₫ · đếm và ghi ở Thu chi và đối chiếu</dd><dt>Chuyển khoản</dt><dd>1.430.000 ₫ · 3 khớp sao kê</dd></dl></aside></div></div>')
save('quick-sale', 'Bán hàng · Bán nhanh', Q1, sec=SEC)
print('sell7: + quick-sale')


# ---- Bán nhanh · QR shown, waiting for the transfer
QR = ('<figure class="c-qrcard"><img src="../../../system/assets/qr-demo.svg" alt="Mã VietQR tài khoản MB của hộ, số tiền 715.000 ₫, nội dung DH2053">'
      '<figcaption><b class="c-qrcard__amt">715.000<span class="u-cur">₫</span></b><span class="u-meta">VietQR · MB 0901 2345 678 · nội dung DH2053</span></figcaption></figure>')
QW = ('<div class="c-decide" role="group" aria-labelledby="q-wait"><p class="c-decide__q" id="q-wait">Chờ khách chuyển 715.000 ₫</p>'
      '<p class="c-sub">Đã nối ngân hàng: OPC tự báo khi tiền về khớp nội dung DH2053. Chưa nối: chị xem app ngân hàng rồi bấm "Tôi đã thấy tiền về".</p>'
      '<div class="c-decide__acts"><a class="c-btn c-btn--act" href="quick-sale--done.html">Tôi đã thấy tiền về</a>'
      '<a class="c-btn" href="quick-sale.html">Đổi sang tiền mặt</a><a class="c-btn c-btn--quiet" href="quick-sale.html">Quay lại giỏ</a></div></div>')
Q2 = (head('Bán nhanh · DH-2053', 'Khách lẻ · 2 gói bò, 3 hũ muối · giá lẻ')
      + '<div class="page"><div class="r-detail__grid r-detail--calm"><div class="stack">' + QR + QW + '</div>'
      '<aside class="r-tower__detail" aria-labelledby="qh"><h2 class="r-tower__t" id="qh">Giỏ hàng</h2>' + CART_RO + '</aside></div></div>')
save('quick-sale--qr', 'Bán nhanh · chờ chuyển khoản', Q2, sec=SEC)

# ---- Bán nhanh · done: one order, all four tracks settled at once
T5 = tracks(('Đơn', 'ok', 'DH-2053 · khách lẻ'), ('Giao', 'ok', 'Giao tại chỗ 10:46'), ('Hoá đơn', 'ok', 'Khách không lấy'), ('Tiền', 'ok', 'Đã nhận 715.000 ₫ · khớp sao kê'))
DONE = ('<div class="c-banner c-banner--ok" role="status"><span class="c-banner__pic">' + ic('i-check') + '</span><span class="c-banner__text">'
        '<strong class="c-banner__title">Xong DH-2053 · 715.000 ₫</strong><span>Đã trừ kho (bò khả dụng 26 → 24, muối 50 → 47) · doanh thu vào sổ hôm nay · đơn đã đóng</span></span></div>')
DA = ('<div class="r-form__acts"><a class="c-btn c-btn--act" href="quick-sale.html">Bán tiếp</a><button class="c-btn" type="button">' + ic('i-print') + 'In phiếu</button>'
      '<a class="c-btn" href="order-detail.html">Khách cần hoá đơn</a></div>'
      '<p class="c-sub">Khách đổi ý muốn lấy hoá đơn: lập từ đơn này, trong ngày. Hộ dùng hoá đơn từ máy tính tiền khi doanh thu tới ngưỡng bắt buộc (chờ kế toán xác nhận).</p>')
Q3 = (head('Bán nhanh · DH-2053', 'Khách lẻ · 10:46') + '<div class="page">' + DONE + T5
      + '<div class="r-detail__grid r-detail--calm"><div class="stack">' + card('q2', 'Hàng bán', CART_RO) + DA + '</div>'
      '<aside class="r-tower__detail" aria-labelledby="hx"><h2 class="r-tower__t" id="hx">Diễn biến</h2>'
      + tl([('10:45', 'ok', 'Chị An bán nhanh', 'giá lẻ'), ('10:46', 'ok', 'Khách chuyển 715.000 ₫', 'MB · khớp DH2053'), ('10:46', 'ok', 'Đơn đóng', 'kho trừ một lần')]) + '</aside></div></div>')
save('quick-sale--done', 'Bán nhanh · xong', Q3, sec=SEC)
print('sell7: + quick-sale qr/done')


# ================================================================== giao thiếu = confirm the split (audit A: missing; eval v730: needs a confirm step)
GOODS18 = lines([('Bò một nắng 500g', '20 gói', '230.000 ₫', '4.600.000 ₫'), ('Muối kiến vàng 100g', '18 hũ', '55.000 ₫', '990.000 ₫')], '5.590.000 ₫', label='Hàng giao hôm nay', price='Giá bán')
SPLIT = ('<div class="c-decide" role="group" aria-labelledby="q-split"><p class="c-decide__q" id="q-split">Giao thiếu 12 hũ muối — chị xác nhận?</p>'
         '<dl class="c-kv"><dt>DH-2052 hôm nay</dt><dd>20 gói bò · <b>18 hũ muối</b> · 5.590.000 ₫ · một hoá đơn khi giao xong</dd>'
         '<dt>Đơn mới DH-2056</dt><dd>12 hũ muối · 660.000 ₫ · cùng giá khách sạn · giao khi có hàng</dd></dl>'
         '<p class="c-decide__result">Xác nhận = DH-2052 sửa còn 18 hũ · giữ hàng 12 hũ chuyển sang DH-2056 · Agent soạn tin báo chị Mai, chị bấm gửi</p>'
         '<div class="c-decide__acts"><a class="c-btn c-btn--act" href="delivery.html">Xác nhận giao thiếu</a>'
         '<a class="c-btn" href="delivery--pick.html">Quay lại soạn tiếp</a></div></div>')
O5 = order('Soạn lúc 13:40 · kho chỉ đủ 18/30 hũ muối', tracks(('Đơn', 'you', 'Sửa còn 18 hũ · chờ chị'), ('Giao', 'wait', 'Chưa bàn giao'), ('Hoá đơn', 'wait', 'Lập khi đã giao'), ('Tiền', 'wait', 'Chưa thu')),
           SPLIT + card('s1', 'Hàng giao hôm nay', GOODS18),
           tl([('09:15', 'ok', 'Chị An xác nhận · giữ hàng', '20 gói, 30 hũ'), ('13:40', 'err', 'Anh Khoa soạn: kệ chỉ đếm được 18 hũ muối', 'lệch 12 hũ so với sổ · gửi chị duyệt ở Kiểm kho'), ('Bây giờ', 'you', 'Chờ chị xác nhận giao thiếu', '')]))
save('order-detail--split', 'Đơn bán · DH-2052 giao thiếu', O5, sec=SEC)

# ================================================================== handed over, out for delivery (before "Đã giao")
T6 = tracks(('Đơn', 'ok', 'Đã xác nhận · giữ hàng'), ('Giao', 'wait', 'Anh Hùng đang giao · đi 14:05'), ('Hoá đơn', 'wait', 'Lập khi đã giao'), ('Tiền', 'wait', 'Chưa thu · trả sau 15 ngày'))
G6 = ('<dl class="c-kv"><dt>Người giao</dt><dd>anh Hùng · đã nhận link qua Zalo 14:05</dd><dt>Khi giao xong</dt><dd>anh Hùng bấm "Đã giao" trên link và chụp người nhận ký</dd>'
      '<dt>Kho</dt><dd>vẫn đang giữ · trừ một lần khi đã giao</dd></dl>')
O6 = order('Bàn giao 14:05 · giao trước 15:00', T6,
           card('s2', 'Giao hàng', G6, '<a class="c-btn c-btn--act" href="order-detail--invoice.html">Anh Hùng báo đã giao</a>') + card('s1', 'Hàng bán', GOODS),
           tl([('09:15', 'ok', 'Chị An xác nhận · giữ hàng', ''), ('13:50', 'ok', 'Anh Khoa soạn đủ', '20 gói, 30 hũ'), ('14:05', 'ok', 'Bàn giao cho anh Hùng', 'gửi link qua Zalo'),
               ('15:00', 'wait', 'Hẹn giao', 'cổng bếp Sunrise')]))
save('order-detail--delivering', 'Đơn bán · DH-2052 đang giao', O6, sec=SEC)
print('sell7: + split, delivering')

"""v4.2 · Hàng hoá → Nhập hàng & chi phí (BA UI-07, FLOWS.md ③; SCOPE §7 #1). BA demo data (An Nhiên).
Writes purchases.html (datatable: purchase orders + expenses), purchase-receive.html (receive MH-0118: short 5 kg,
supplier invoice read by the assistant does not match → owner decides), purchases--expense.html (expense without
stock: photo of the electricity bill → assistant reads → owner confirms). Usage: python3 pages_purchase.py"""
from pages import build, ic, sign, subnav, annhien, SCREENS

CUR = '<span class="u-cur">₫</span>'


def sub(cur='Nhập hàng & chi phí'):
    return subnav('Hàng hoá', [('Danh sách & giá', 'products.html'), ('Tồn kho', 'stock.html'), ('Chế biến', 'production.html'), ('Nhập hàng & chi phí', 'purchases.html'), ('Nhà cung cấp', 'suppliers.html')], cur)


def tabs(sel):
    return ('<div class="c-tabs" role="tablist" aria-label="Nhập hàng và chi phí">' + ''.join(
        f'<a class="c-tabs__tab" role="tab" aria-selected="{"true" if n == sel else "false"}" href="{h}">{n} <span class="c-tabs__count">{c}</span></a>'
        for n, h, c in [('Đơn mua', 'purchases.html', 4), ('Chi phí', 'purchases--expense.html', 3)]) + '</div>')


who = lambda n, m: f'<td class="c-table__cell--main c-table__who"><b>{n}</b><small>{m}</small></td>'
num = lambda v: f'<td class="c-table__num">{v}</td>'
st = lambda k, i, t: f'<td>{sign(k, i, t)}</td>'


def table(head, rows, label):
    th = ''.join(f'<th scope="col"{" class=\"c-table__num\"" if n == 1 else " class=\"c-table__cell--hide\"" if n == 2 else ""}>{h}</th>' for h, n in head)
    return (f'<div class="c-table__scroll" tabindex="0" role="region" aria-label="{label}"><table class="c-table c-table--stack">'
            f'<thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table></div>')


HEAD = ('<div class="r-page-head"><div><h1 class="r-page-head__title">Nhập hàng & chi phí</h1><p class="c-sub">Tháng 10/2026</p></div>'
        f'<div class="r-page-head__acts"><a class="c-btn" href="purchases--expense.html">{ic("i-photo")}Chụp hoá đơn chi phí</a>'
        f'<a class="c-btn c-btn--act" href="#">{ic("i-plus")}Tạo đơn mua</a></div></div>')

PO = ''.join([
    '<tr class="c-table__row--you">' + who('MH-0118 · HTX Cao Nguyên', '40 kg thịt bò tươi · 50 hũ muối kiến vàng · nhận hôm nay 08:40')
    + num('12.600.000 ₫') + st('you', 'i-alert', 'Nhận thiếu 5 kg · chờ chị')
    + '<td class="c-table__cell--end"><a class="c-btn" href="purchase-receive.html">Xem & xác nhận</a></td></tr>',
    '<tr>' + who('MH-0121 · HTX Cao Nguyên', '30 kg thịt bò tươi · giao Thứ Năm 08/10') + num('8.400.000 ₫') + st('wait', 'i-clock', 'Đã đặt · chờ giao')
    + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
    '<tr>' + who('MH-0114 · HTX Cao Nguyên', '34 kg thịt bò tươi · nhận 05/10 · lô TB-1005') + num('9.520.000 ₫') + st('ok', 'i-check', 'Đã nhận · đã trả 05/10')
    + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
    '<tr>' + who('MH-0109 · HTX Cao Nguyên', '120 hũ muối kiến vàng · 60 gói gia vị ướp · nhận 08/09') + num('4.800.000 ₫') + st('wait', 'i-clock', 'Đã nhận · trả trước 08/10')
    + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="receivables--payables.html">Trả</a></td></tr>',
])
LH = ('<section class="r-listhead" aria-label="Hàng đang về"><div class="r-listhead__fig"><span class="c-stat__label">Đang về · 2 đơn mua</span>'
      f'<b class="c-figure">21.000.000{CUR}</b></div><div class="r-listhead__bar"><div class="c-split__bar" role="img" aria-label="Đã nhận tháng 10 9.520.000 ₫, đang về 21.000.000 ₫"><i class="c-split__cash" style="flex:9520"></i><i class="c-split__you" style="flex:21000"></i></div>'
      '<p class="c-sub">đã nhận tháng 10: 9.520.000 ₫</p></div>'
      f'<a class="r-listhead__due" href="purchase-receive.html"><span class="c-stat__label">MH-0118 <span class="r-listhead__late">thiếu 5 kg</span></span><span class="r-listhead__duev">Xem & xác nhận</span>{ic("i-chev-r")}</a></section>')
LOW = ('<div class="c-banner c-banner--pend" role="status"><span class="c-banner__pic">' + ic('i-alert') + '</span><span class="c-banner__text">'
       '<strong class="c-banner__title">Thịt bò tươi còn 6 kg</strong><span>Dưới mức tối thiểu 20 kg · lệnh LCB-0413 (Thứ Năm) cần 34 kg — đủ khi chị xác nhận MH-0118</span></span>'
       '</div>')
main = (f'\n      {sub()}\n      {HEAD}\n      <div class="page">{LH}{LOW}{tabs("Đơn mua")}'
        + table([('Đơn mua', 0), ('Giá trị', 1), ('Tình trạng', 0), ('', 0)], PO, 'Đơn mua')
        + '</div>')
build('purchases', 'Hàng hoá · Nhập hàng', main, 'goods')
annhien(SCREENS / 'purchases.html')


# ---------------- receive MH-0118 ----------------
def rline(name, ordered, got, unit, lot, short=False):
    chk = '' if short else ic('i-check')
    cls = 'r-pick__chk' + ('' if short else ' r-pick__chk--ok')
    note = f'<small class="r-recv__short">Thiếu {ordered - got} {unit} so với đơn</small>' if short else f'<small>Lô {lot}</small>'
    return (f'<li class="r-pick__l"><span class="{cls}" aria-hidden="true">{chk}</span><span class="r-pick__name"><b>{name}</b>{note}</span>'
            f'<span class="r-pick__qty{" r-pick__qty--short" if short else ""}"><b>{got}</b>/{ordered} {unit}<span class="u-sr">{" — thiếu" if short else " — đủ"}</span></span></li>')


DECIDE = ('<div class="c-decide" role="group" aria-labelledby="q-short"><p class="c-decide__q" id="q-short">Thiếu 5 kg thịt bò — xử lý thế nào?</p>'
          '<div class="c-options" role="radiogroup" aria-label="Cách xử lý phần thiếu">'
          '<button class="c-option c-option--best" type="button" role="radio" aria-checked="true"><span class="c-option__radio" aria-hidden="true"></span>'
          '<span class="c-option__body"><span class="c-option__tag c-option__tag--best">Trợ lý gợi ý</span><strong class="c-option__title">Nhận 35 kg, HTX giao bù 5 kg</strong>'
          '<span class="c-option__meta">MH-0118 mở phần 5 kg · trả theo số đã nhận</span></span></button>'
          '<button class="c-option" type="button" role="radio" aria-checked="false"><span class="c-option__radio" aria-hidden="true"></span>'
          '<span class="c-option__body"><strong class="c-option__title">Nhận 35 kg, đóng đơn mua</strong><span class="c-option__meta">Không chờ giao bù</span></span></button></div>'
          '<label class="c-field"><span class="c-field__label">Ghi chú cho HTX (tuỳ chọn)</span><span class="c-field__control"><input class="c-field__input" placeholder="Ví dụ: giao bù cùng chuyến Thứ Năm"></span></label>'
          '<p class="c-decide__result">Xác nhận = nhập kho một lần (35 kg → lô TB-1006, 50 hũ → lô MKV-1006) · phải trả <b>11.200.000 ₫</b> hạn 05/11</p>'
          '<div class="c-decide__acts"><button class="c-btn c-btn--act" type="button">Xác nhận nhận hàng</button><button class="c-btn" type="button">Đếm lại</button></div></div>')
DOC = ('<figure class="c-quote" style="margin:0"><figcaption class="c-quote__from"><b>Hoá đơn HTX</b> · chụp 08:42</figcaption>'
       f'<div class="c-quote__media">{ic("i-file")}<span>HĐ 0000845 · MST 5900112233 · 40 kg thịt bò tươi, 50 hũ muối · <mark>12.600.000 ₫</mark></span></div></figure>'
       '<div class="c-banner c-banner--err" role="status"><span class="c-banner__pic">' + ic('i-x') + '</span><span class="c-banner__text">'
       '<strong class="c-banner__title">Lệch số lượng: hoá đơn 40 kg, nhận 35 kg</strong><span>Nhờ HTX lập hoá đơn điều chỉnh giảm 1.400.000 ₫ — tới lúc đó chứng từ ghi “Lệch”.</span></span>'
       f'<button class="c-btn" type="button">{ic("i-send")}Nhắn HTX</button></div>'
       '<ul class="c-rules" aria-label="Khớp"><li class="c-rules__r">' + ic('i-check') + 'Nhà cung cấp<span class="u-sr"> khớp</span></li>'
       '<li class="c-rules__r">' + ic('i-check') + 'Đơn giá 280.000 ₫/kg<span class="u-sr"> khớp</span></li></ul>')
RECV = (f'\n      {sub()}\n      <div class="page"><nav class="c-crumbs" aria-label="Đường dẫn"><a href="purchases.html">Nhập hàng</a><span aria-current="page">Nhận MH-0118</span></nav>'
        '<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">Nhận hàng MH-0118 · HTX Cao Nguyên '
        + sign('you', 'i-alert', 'Thiếu 5 kg') + '</h1>'
        '<p class="r-detail__fig"><span class="c-sub">Đặt 03/10 · giao 06/10 08:40 · anh Khoa nhận</span></p></div></div>'
        '<div class="r-detail__grid r-detail--calm"><div class="stack">'
        '<section class="c-card" aria-labelledby="rv"><div class="c-card__head"><h2 class="c-card__title" id="rv">Hàng thực nhận</h2></div><ul class="r-pick">'
        + rline('Thịt bò tươi', 40, 35, 'kg', 'TB-1006', short=True) + rline('Muối kiến vàng 100g', 50, 50, 'hũ', 'MKV-1006 · hạn 10/2027') + '</ul></section>'
        + DECIDE + '</div><aside class="r-tower__detail" aria-labelledby="dc"><h2 class="r-tower__t" id="dc">Chứng từ đầu vào</h2>' + DOC + '</aside></div></div>')
build('purchase-receive', 'Nhập hàng · Nhận MH-0118', RECV, 'goods')
annhien(SCREENS / 'purchase-receive.html')

# ---------------- expense without stock ----------------
EX = ''.join([
    '<tr>' + who('Tiền điện tháng 9 · Điện lực Gia Lai', 'Điện · ảnh hoá đơn chị An chụp') + num('1.250.000 ₫') + st('wait', 'i-clock', 'Chưa trả · hạn 10/10') + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="receivables--payables.html">Trả</a></td></tr>',
    '<tr>' + who('Túi hút chân không 1.000 cái · Bao bì Phú Mỹ', 'Bao bì · có hoá đơn điện tử') + num('850.000 ₫') + st('ok', 'i-check', 'Đã trả tiền mặt 02/10') + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
    '<tr>' + who('Xăng xe giao hàng tuần 40', 'Vận chuyển · biên lai, không có hoá đơn') + num('850.000 ₫') + st('ok', 'i-check', 'Đã trả 04/10') + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
])
LIST = (f'\n      {sub()}\n      {HEAD}\n      <div class="page">{tabs("Chi phí")}'
        + table([('Chi phí', 0), ('Số tiền', 1), ('Tình trạng', 0), ('', 0)], EX, 'Chi phí') + '</div>')
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
build('purchases--expense', 'Hàng hoá · Chi phí', LIST, 'goods', overlay=DLG)
annhien(SCREENS / 'purchases--expense.html')
print('purchases: 3 screens')

"""v7.0.0 · Kho hàng → Tồn kho, kiểm kho. One warehouse, goods bought to resell, no lots (BA 07/10; research T14: optional expiry date per item,
traceability through purchase and sale invoices). Writes stock.html (thực · đã giữ · khả dụng · hạn gần nhất), stock-count.html (count → differences
with a reason → the owner approves; stock is never edited directly). Usage: python3 pages_stock.py"""
from pages import build, ic, sign, subnav, annhien, SCREENS


def sub(cur='Tồn kho'):
    return subnav('Hàng hoá', [('Danh sách & giá', 'products.html'), ('Tồn kho', 'stock.html'), ('Chế biến', 'production.html'), ('Nhập hàng & chi phí', 'purchases.html'), ('Nhà cung cấp', 'suppliers.html')], cur)


num = lambda v: f'<td class="c-table__num">{v}</td>'


def item(name, kind, lots, phone=''):
    ph = f'<small class="c-table__phone">{phone}</small>' if phone else ''
    return f'<td class="c-table__cell--main c-table__who"><b>{name}</b><small>{kind} · {lots}</small>{ph}</td>'


hide = lambda v: f'<td class="c-table__num c-table__cell--hide">{v}</td>'
held = lambda n, o: f'<td class="c-table__num c-table__cell--hide"><a class="r-stock__held" href="order-detail.html">{n}</a><small class="r-stock__note">{o}</small></td>'
avail = lambda v, x='': f'<td class="c-table__num r-stock__avail{x}"><b>{v}</b><small class="c-table__phone"> khả dụng</small></td>'


lot = lambda code, rest, href='#': f'<a href="{href}">{code}</a> {rest}'

ROWS = ''.join([
    '<tr class="c-table__row--you">' + item('Muối kiến vàng 100g', 'mua của HTX Cao Nguyên', 'hạn gần nhất 09/2027') + hide('80 hũ') + held('30', 'DH-2052') + avail('50 hũ')
    + f'<td>{sign("you", "i-alert", "45 hũ đã về")}<small class="r-stock__note">MH-0118 thiếu 5 hũ · chờ chị xác nhận nhập kho</small></td>'
    + '<td class="c-table__cell--end"><a class="c-btn" href="purchase-detail--receive.html">Nhận hàng</a></td></tr>',
    '<tr>' + item('Bò một nắng 500g', 'mua của Cơ sở Krông Pa', 'hạn gần nhất 15/11', 'tồn 46 · giữ 20 cho DH-2052')
    + hide('46 gói') + held('20', 'DH-2052') + avail('26 gói')
    + f'<td>{sign("ok", "i-check", "Đủ bán")}<small class="r-stock__note">+40 gói khi nhận MH-0121 Thứ Năm</small></td>'
    + '<td class="c-table__cell--end r-stock__quietact"><a class="c-btn c-btn--quiet" href="product-detail.html">Xem</a></td></tr>',
])
TABLE = ('<div class="c-table__scroll" tabindex="0" role="region" aria-label="Tồn kho theo món"><table class="c-table c-table--stack r-stock">'
         '<thead><tr><th scope="col">Món</th><th scope="col" class="c-table__num">Tồn thực</th><th scope="col" class="c-table__num">Đã giữ cho đơn</th>'
         '<th scope="col" class="c-table__num r-stock__avail">Khả dụng</th><th scope="col">Tình trạng</th><th scope="col"><span class="u-sr">Việc</span></th></tr></thead>'
         f'<tbody>{ROWS}</tbody></table></div>')
HEAD = ('<div class="r-page-head"><div><h1 class="r-page-head__title">Tồn kho</h1><p class="c-sub">Kho chính · cập nhật 10:45 · '
        'chỉ trừ khi Đã giao</p></div>'
        f'<div class="r-page-head__acts"><a class="c-btn" href="#">{ic("i-book")}Sổ biến động</a>'
        f'<a class="c-btn c-btn--act" href="stock-count.html">{ic("i-scale")}Kiểm kho</a></div></div>')
QUIET = ('<p class="r-stock__quiet">' + sign('ok', 'i-check', 'Không món nào cận hạn trong 7 ngày tới')
         + '<span class="c-sub">Khả dụng = tồn thực − đã giữ · trừ kho một lần khi Đã giao</span></p>')
main = f'\n      {sub()}\n      {HEAD}\n      <div class="page">{QUIET}{TABLE}</div>'
build('stock', 'Kho hàng · Tồn kho', main, 'goods')
annhien(SCREENS / 'stock.html')


# ---------------- count ----------------
def cline(name, book, got, unit, diff='', reason=None):
    ok = not diff
    mark = f'<span class="r-pick__chk r-pick__chk--ok" aria-hidden="true">{ic("i-check")}</span>' if ok else f'<span class="r-pick__chk r-pick__chk--warn" aria-hidden="true">{ic("i-alert")}</span>'
    d = '<span class="r-count__d">khớp</span>' if ok else f'<span class="r-count__d r-count__d--off">{diff}</span>'
    row = (f'<li class="r-count__l{" r-count__l--ok" if ok else " r-count__l--off"}">{mark}<span class="r-pick__name"><b>{name}</b><small>sổ {book} {unit}</small></span>'
           f'<label class="r-count__in"><span class="u-sr">Đếm được, {name}</span><input class="c-field__input" inputmode="decimal" value="{got}"><span class="r-count__u">{unit}</span></label>{d}')
    if reason is not None:
        picked, note, hint = reason
        opts = ''.join(f'<button class="c-seg__opt" type="button" role="radio" aria-checked="{"true" if o == picked else "false"}">{o}</button>'
                       for o in ['Hỏng', 'Hao hụt', 'Đếm sai', 'Khác'])
        h = f'<p class="r-count__hint"><span class="c-tag">Trợ lý gợi ý</span>{hint}</p>' if hint else ''
        row += (f'<div class="r-count__why"><div class="c-seg" role="radiogroup" aria-label="Lý do lệch, {name}">{opts}</div>{h}'
                f'<label class="c-field"><span class="u-sr">Ghi chú, {name}</span><span class="c-field__control"><input class="c-field__input" value="{note}" placeholder="Ghi chú (tuỳ chọn)"></span></label></div>')
    return row + '</li>'


COUNT = ('<ul class="r-count" aria-label="Dòng kiểm kho">'
         + cline('Bò một nắng 500g', '46', '45', 'gói', '−1 gói', ('Hỏng', '1 gói rách bao bì, đã bỏ', ''))
         + cline('Muối kiến vàng 100g', '80', '80', 'hũ')
         + '</ul>')
CNT = (f'\n      {sub()}\n      <div class="page"><nav class="c-crumbs" aria-label="Đường dẫn"><a href="stock.html">Tồn kho</a><span aria-current="page">Kiểm kho 06/10</span></nav>'
       '<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">Kiểm kho · Kho chính ' + sign('pend', 'i-clock', 'Đang đếm') + '</h1>'
       '<p class="r-detail__fig"><span class="c-sub">Anh Khoa bắt đầu 10:20 · đã đếm 2/2 món · vẫn bán bình thường, OPC tính cả phần bán trong lúc đếm</span></p></div></div>'
       '<section class="c-card r-count__card" aria-labelledby="cl"><div class="c-card__head"><h2 class="c-card__title" id="cl">1 món lệch so với sổ</h2></div>' + COUNT
       + '<div class="r-count__foot"><p class="c-decide__result">Gửi = chưa đổi tồn. Chị An duyệt thì OPC ghi 1 điều chỉnh vào sổ kho · giá vốn khoảng <b>190.000 ₫</b></p>'
       f'<div class="c-decide__acts"><button class="c-btn c-btn--act" type="button">Gửi chị An duyệt</button>'
       '<button class="c-btn" type="button">Lưu, đếm tiếp sau</button></div></div></section></div>')
build('stock-count', 'Kho hàng · Kiểm kho', CNT, 'goods')
annhien(SCREENS / 'stock-count.html')
print('stock: 2 screens')

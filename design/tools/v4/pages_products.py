"""v7.0.0 (was v4.2) · Kho hàng → Hàng và giá; goods bought to resell (no recipes, no lots; optional expiry date) (BA F02.03–F02.05). An Nhiên data.
Writes products.html, product-detail.html, pricelist.html, pricelist--edit.html (drawer: scheduled price change,
approved by the owner; confirmed orders keep their price). Usage: python3 pages_products.py"""
from pages import build, ic, sign, subnav, annhien, SCREENS

CUR = '<span class="u-cur">₫</span>'


def sub(cur='Danh sách & giá'):
    return subnav('Hàng hoá', [('Danh sách & giá', 'products.html'), ('Tồn kho', 'stock.html'), ('Chế biến', 'production.html'),
                               ('Nhập hàng & chi phí', 'purchases.html'), ('Nhà cung cấp', 'suppliers.html')], cur)


def tabs(sel):
    return ('<div class="c-tabs" role="tablist" aria-label="Danh sách và giá">' + ''.join(
        f'<a class="c-tabs__tab" role="tab" aria-selected="{"true" if n == sel else "false"}" href="{h}">{n} <span class="c-tabs__count">{c}</span></a>'
        for n, h, c in [('Món bán', 'products.html', 2), ('Bảng giá', 'pricelist.html', 2)]) + '</div>')


who = lambda n, m: f'<td class="c-table__cell--main c-table__who"><b>{n}</b><small>{m}</small></td>'
num = lambda v, c='': f'<td class="c-table__num{c}">{v}</td>'

ROWS = ''.join([
    '<tr>' + who('<a href="product-detail.html">Bò một nắng 500g</a>', 'gói · mua của Cơ sở Krông Pa · theo dõi hạn dùng') + num('<span class="c-table__phone">lẻ </span><b>260.000</b>') + num('<span class="c-table__phone">khách sạn </span><b>230.000</b>')
    + '<td class="c-table__cell--hide">phân phối</td>' + num('<span class="c-table__phone">khả dụng </span>26 gói', ' r-prices__stock') + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="product-detail.html">Xem</a></td></tr>',
    '<tr>' + who('Muối kiến vàng 100g', 'hũ · mua của HTX Cao Nguyên · theo dõi hạn dùng') + num('<span class="c-table__phone">lẻ </span><b>65.000</b>') + num('<span class="c-table__phone">khách sạn </span><b>55.000</b>')
    + '<td class="c-table__cell--hide">phân phối</td>' + num('<span class="c-table__phone">khả dụng </span>50 hũ', ' r-prices__stock') + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
])
LIST = (f'\n      {sub()}\n      <div class="r-page-head"><div><h1 class="r-page-head__title">Danh sách & giá</h1>'
        '<p class="c-sub">2 món bán · 2 bảng giá · mọi giá đang dùng đều đã được chị An duyệt</p></div>'
        f'<div class="r-page-head__acts"><a class="c-btn" href="#">{ic("i-photo")}Chụp bảng giá</a><a class="c-btn c-btn--act" href="#">{ic("i-plus")}Thêm món</a></div></div>'
        f'<div class="page">{tabs("Món bán")}<p class="r-trust r-trust--gate r-prices__rule">{ic("i-check")}<span><b>Giá nào cho đơn nào:</b> quầy và khách chưa gán → giá lẻ · khách gán bảng riêng → giá bảng đó · đơn đã xác nhận giữ giá lúc xác nhận</span></p>'
        '<div class="c-table__scroll" tabindex="0" role="region" aria-label="Món bán và giá"><table class="c-table c-table--stack r-prices">'
        '<thead><tr><th scope="col">Món</th><th scope="col" class="c-table__num">Giá lẻ <span class="r-prices__def">mặc định</span></th><th scope="col" class="c-table__num"><a href="pricelist.html">Giá khách sạn & nhà hàng</a></th>'
        '<th scope="col">Nhóm thuế</th><th scope="col" class="c-table__num">Khả dụng</th><th scope="col"><span class="u-sr">Việc</span></th></tr></thead>'
        f'<tbody>{ROWS}</tbody></table></div>'
        '</div>')
build('products', 'Hàng hoá · Danh sách & giá', LIST, 'goods')
annhien(SCREENS / 'products.html')


# ---------------- product detail ----------------
def step(kind, src, time, what, detail=''):
    d = f'<span class="c-timeline__who">{detail}</span>' if detail else ''
    return (f'<li class="c-timeline__item c-timeline__item--{kind}"><span class="c-timeline__time">{time}</span>'
            f'<span class="c-timeline__dot" aria-hidden="true"></span><span class="c-timeline__body">'
            f'<span class="c-timeline__src">{src}</span><span class="c-timeline__what">{what}</span>{d}</span></li>')


PRICES = ('<ul class="r-plist">'
          '<li class="r-plist__main"><span class="r-plist__k"><b>Giá lẻ <span class="r-prices__def">mặc định</span></b><small>quầy, Homestay Mây Ngàn và khách chưa gán</small></span><b class="r-plist__v">260.000 ₫</b></li>'
          '<li><span class="r-plist__k"><b><a href="pricelist.html">Giá khách sạn & nhà hàng</a></b><small>Sunrise Hotel · Nhà hàng Phố Núi</small></span><b class="r-plist__v">230.000 ₫</b></li></ul>')
FACTS = ('<dl class="c-kv"><dt>Đơn vị</dt><dd>gói 500g · mã vạch 8936 0123 4501</dd><dt>Mua của</dt><dd><a href="suppliers.html">Cơ sở bò một nắng Krông Pa</a> · giá mua gần nhất 190.000 ₫/gói</dd>'
         '<dt>Hạn dùng</dt><dd>có theo dõi · nhập khi nhận hàng · OPC báo trước 7 ngày</dd><dt>Nhóm thuế</dt><dd>phân phối, cung cấp hàng hoá (chờ kế toán xác nhận)</dd>'
         '<dt>Tồn</dt><dd><a href="stock.html">46 gói · 20 đã giữ · 26 khả dụng</a></dd></dl>')
DET = (f'\n      {sub()}\n      <div class="page"><nav class="c-crumbs" aria-label="Đường dẫn"><a href="products.html">Danh sách & giá</a><span aria-current="page">Bò một nắng 500g</span></nav>'
       '<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">Bò một nắng 500g ' + sign('pass', 'i-check', 'Đang bán') + '</h1>'
       '<p class="r-detail__fig"><span class="c-sub">gói · mua về bán · 2 bảng giá</span></p></div>'
       '<div class="r-detail__acts"><a class="c-btn c-btn--act" href="pricelist--edit.html">Đổi giá</a></div></div>'
       '<div class="r-detail__grid r-detail--calm"><div class="stack">'
       '<section class="c-card" aria-labelledby="pr"><div class="c-card__head"><h2 class="c-card__title" id="pr">Giá đang dùng</h2></div>' + PRICES + '</section>'
       '<section class="c-card" aria-labelledby="fc"><div class="c-card__head"><h2 class="c-card__title" id="fc">Thông tin món</h2></div>' + FACTS + '</section></div>'
       '<aside class="r-tower__detail" aria-labelledby="hs"><h2 class="r-tower__t" id="hs">Lịch sử giá</h2><ol class="c-timeline c-timeline--quiet" aria-label="Lịch sử giá">'
       + step('ok', 'Chị An duyệt', '01/09', 'Giá lẻ 250.000 → 260.000 ₫', 'anh Khoa đề nghị · lý do: giá mua Krông Pa tăng')
       + step('ok', 'Chị An duyệt', '01/07', 'Bảng giá khách sạn & nhà hàng: 230.000 ₫', '09:40 · tạo khi bắt đầu dùng OPC')
       + step('ok', 'Nhập dữ liệu', '01/07', 'Giá lẻ 250.000 ₫', '09:12 · Trợ lý đọc ảnh bảng giá · chị An xem lại')
       + '</ol><p class="c-sub">Lịch sử chỉ ghi thêm. Đơn cũ giữ giá lúc xác nhận.</p></aside></div></div>')
build('product-detail', 'Hàng hoá · Bò một nắng 500g', DET, 'goods')
annhien(SCREENS / 'product-detail.html')


# ---------------- price list ----------------
PL_ROWS = ''.join([
    '<tr>' + who('Bò một nắng 500g', 'giá lẻ 260.000') + num('<b>230.000</b>') + num('<span class="r-prices__delta">−11,5%</span>') + '<td class="u-nowrap">từ 01/07</td>'
    + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="pricelist--edit.html">Đổi giá</a></td></tr>',
    '<tr>' + who('Muối kiến vàng 100g', 'giá lẻ 65.000') + num('<b>55.000</b>') + num('<span class="r-prices__delta">−15,4%</span>') + '<td class="u-nowrap">từ 01/07</td>'
    + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="pricelist--edit.html">Đổi giá</a></td></tr>',
])


def pl_page(name, overlay=None):
    m = (f'\n      {sub()}\n      <div class="r-page-head"><div><h1 class="r-page-head__title">Giá khách sạn & nhà hàng</h1>'
         '<p class="c-sub">Bảng giá riêng · 2 khách · chị An duyệt 01/07</p></div>'
         f'<div class="r-page-head__acts"><button class="c-btn c-btn--act" type="button">{ic("i-plus")}Gán thêm khách</button></div></div>'
         f'<div class="page">{tabs("Bảng giá")}<div class="r-detail__grid r-detail--calm"><div class="stack">'
         '<div class="c-table__scroll" tabindex="0" role="region" aria-label="Giá trong bảng"><table class="c-table c-table--stack">'
         '<thead><tr><th scope="col">Món</th><th scope="col" class="c-table__num">Giá trong bảng</th><th scope="col" class="c-table__num">So với giá lẻ</th><th scope="col">Hiệu lực</th><th scope="col"><span class="u-sr">Việc</span></th></tr></thead>'
         f'<tbody>{PL_ROWS}</tbody></table></div></div>'
         '<aside class="r-tower__detail" aria-labelledby="cu"><h2 class="r-tower__t" id="cu">Khách dùng bảng này</h2><ul class="r-plist">'
         '<li><span class="r-plist__k"><b>Sunrise Hotel</b><small>chị Mai · thường trả 15 ngày</small></span></li>'
         '<li><span class="r-plist__k"><b>Nhà hàng Phố Núi</b><small>thường trả 7 ngày</small></span></li></ul>'
         '<p class="c-sub">Bảng giá khác: <a href="products.html">Giá lẻ</a> (mặc định).</p></aside></div></div>')
    build(name, 'Hàng hoá · Bảng giá khách sạn & nhà hàng', m, 'goods', overlay=overlay)
    annhien(SCREENS / f'{name}.html')


pl_page('pricelist')

DRW = ('<div class="c-drawer c-drawer--wide"><div class="c-drawer__panel" role="dialog" aria-modal="true" aria-labelledby="ed-t">'
       f'<div class="c-drawer__head"><div><span class="c-drawer__k">Giá khách sạn & nhà hàng</span><h2 class="c-drawer__title" id="ed-t" tabindex="-1">Đổi giá · Bò một nắng 500g</h2></div>'
       f'<a class="c-icon-btn" href="pricelist.html" aria-label="Đóng, không lưu">{ic("i-x")}</a></div>'
       '<div class="c-drawer__body"><div class="r-form2">'
       '<label class="c-field"><span class="c-field__label">Giá mới</span><span class="c-field__control"><input class="c-field__input" inputmode="numeric" value="240.000"><span class="c-field__suffix">₫ / gói</span></span>'
       '<span class="c-field__hint">đang 230.000 ₫ · +4,3% · <span class="r-prices__ok">vẫn dưới giá lẻ 260.000 ₫</span></span></label>'
       '<div class="c-field"><span class="c-field__label">Áp dụng từ</span><button class="c-btn r-capture__pick" type="button" aria-haspopup="dialog">01/11/2026' + ic('i-chev') + '</button>'
       '<span class="c-field__hint">đơn xác nhận từ ngày này</span></div></div>'
       '<label class="c-field"><span class="c-field__label">Lý do (cho chị An)</span><span class="c-field__control"><input class="c-field__input" value="Cơ sở Krông Pa tăng giá mua 190.000 → 200.000 ₫/gói từ tháng 11"></span></label>'
       '<ul class="c-rules" aria-label="OPC kiểm tra">'
       '<li class="c-rules__r">' + ic('i-check') + 'Không cao hơn giá lẻ — cao hơn thì OPC chặn gửi<span class="u-sr"> đạt</span></li>'
       '<li class="c-rules__r">' + ic('i-check') + 'DH-2052 Sunrise đã xác nhận → giữ 230.000 ₫<span class="u-sr"> đạt</span></li>'
       '<li class="c-rules__r">' + ic('i-check') + '2 khách dùng bảng này: Sunrise Hotel, Nhà hàng Phố Núi<span class="u-sr"> đạt</span></li></ul>'
       '<button class="c-switch c-switch--row" type="button" role="switch" aria-checked="true"><span class="c-switch__label">Báo khách trước qua Zalo OA'
       '<span class="c-switch__sub">Trợ lý soạn tin báo giá mới từ 01/11 · gửi sau khi chị An duyệt</span></span><span class="c-switch__track" aria-hidden="true"></span></button></div>'
       '<div class="c-drawer__foot"><p class="c-decide__result">Gửi = chưa đổi giá · chị An duyệt thì <b>đơn mới của 2 khách</b> dùng giá mới từ ngày đã chọn</p>'
       '<button class="c-btn c-btn--act" type="button">Gửi chị An duyệt</button></div></div></div>')
pl_page('pricelist--edit', DRW)

print('products: 4 screens')

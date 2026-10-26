"""v4.2 · Bán → Yêu cầu: one inbox for every source (FLOWS.md ②a, SCOPE §7 #11b). BA demo data (An Nhiên).
Writes sales-inbox.html (Sunrise, Zalo OA, all matched), sales-inbox--unclear.html (photo, missing info → ask),
sales-inbox--add.html (add a request by hand: paste, photo, voice, PDF, type). Usage: python3 pages_sales.py"""
from pages import build, ic, sign, subnav, annhien, SCREENS


def sub():
    return subnav('Bán', [('Yêu cầu', 'sales-inbox.html'), ('Đơn hàng', 'orders.html'), ('Giao hàng', 'delivery.html'), ('Khách hàng', 'customers.html')], 'Yêu cầu')


def req(kind, icon, state, who, what, src, when, cur=False, href='#'):
    c = ' aria-current="true"' if cur else ''
    return (f'<li><a class="c-work" href="{href}"{c}><span class="c-work__state">{sign(kind, icon, state)}</span>'
            f'<span class="c-work__when">{when}</span><span class="c-work__t">{who}</span>'
            f'<span class="c-work__m">{what}</span><span class="c-work__src">{src}</span></a></li>')


LIST = lambda cur: ''.join([
    req('ok', 'i-check', 'Đã hiểu · chờ kiểm tra', 'Sunrise Hotel · chị Mai', '20 gói bò, 30 hũ muối · trước 15:00 mai',
        f'{ic("i-chat")} Zalo OA', '09:02', cur == 'sun', 'sales-inbox.html'),
    req('pend', 'i-alert', 'Cần làm rõ', 'Quán Gió Núi', 'Ảnh đơn viết tay · chưa rõ số hũ muối', f'{ic("i-photo")} Thêm thủ công · chị An', '10:41',
        cur == 'gio', 'sales-inbox--unclear.html'),
    req('wait', 'i-clock', 'Trợ lý đang đọc', 'Nhà hàng Phố Núi', 'Ghi âm cuộc gọi 1 phút 12 giây', f'{ic("i-mic")} Thêm thủ công · anh Khoa', '10:52'),
])   # v4.5.2: the Cần xem tab lists only its 3 — the converted request lives under Đã thành đơn

HEAD = lambda: (sub() + '<div class="r-page-head"><div><h1 class="r-page-head__title">Yêu cầu bán</h1>'
                '<p class="c-sub">Trợ lý đọc · OPC kiểm tra · chị quyết</p></div>'
                f'<div class="r-page-head__acts"><a class="c-btn" href="sales-inbox--add.html">{ic("i-plus")}Thêm yêu cầu</a></div></div>')

FILTER = ('<div class="c-tabs" role="tablist" aria-label="Lọc yêu cầu">'
          '<button class="c-tabs__tab c-tabs__tab--you" role="tab" aria-selected="true" type="button">Cần xem <span class="c-tabs__count">3</span></button>'
          '<button class="c-tabs__tab" role="tab" aria-selected="false" type="button">Đã thành đơn <span class="c-tabs__count">6</span></button>'
          '<button class="c-tabs__tab" role="tab" aria-selected="false" type="button">Bỏ qua <span class="c-tabs__count">1</span></button></div>')


def line(said, item, qty, price, total, unsure=''):
    cls = ' c-match--unsure' if unsure else ''
    note = unsure or f'Khớp: {item}'
    return (f'<tr><td class="c-table__cell--main"><span class="c-match{cls}"><b>{said}</b><small>{note}</small></span></td>'
            f'<td class="c-table__num">{qty}</td><td class="c-table__num">{price}</td><td class="c-table__num">{total}</td></tr>')


def table(rows, total, label='Tổng (giá riêng khách sạn)'):
    return ('<div class="c-table__scroll" tabindex="0" role="region" aria-label="Món Trợ lý đọc được"><table class="c-table c-table--stack">'
            '<thead><tr><th scope="col">Khách viết → món</th><th scope="col" class="c-table__num">SL</th>'
            '<th scope="col" class="c-table__num">Đơn giá</th><th scope="col" class="c-table__num">Thành tiền</th></tr></thead>'
            f'<tbody>{rows}</tbody><tfoot><tr><th scope="row" colspan="3">{label}</th><td class="c-table__num"><b>{total}</b></td></tr></tfoot></table></div>')


SUN = (
    '<p class="r-tower__k">Zalo OA · 09:02</p><h2 class="r-tower__t" id="d-h">Sunrise Hotel · chị Mai (bếp)</h2>'
    '<figure class="c-quote" style="margin:0"><figcaption class="c-quote__from"><b>Chị Mai</b> · 09:01</figcaption>'
    '<p class="c-quote__text">Khách sạn Sunrise cần 20 gói bò một nắng 500g và 30 hũ muối kiến vàng 100g. Giao trước 15:00 ngày mai và xuất hoá đơn.</p></figure>'
    '<h3 class="c-card__title" style="margin-top:var(--space-4)">Trợ lý hiểu là</h3>'
    + table(line('“20 gói bò một nắng 500g”', 'Bò một nắng 500g', '20 gói', '230.000 ₫', '4.600.000 ₫')
            + line('“30 hũ muối kiến vàng 100g”', 'Muối kiến vàng 100g', '30 hũ', '55.000 ₫', '1.650.000 ₫'), '6.250.000 ₫')
    + '<dl class="c-kv"><dt>Khách</dt><dd>Sunrise Hotel · khớp hồ sơ</dd>'
      '<dt>Giao</dt><dd>Trước 15:00 thứ Ba · cổng bếp theo hồ sơ</dd>'
      '<dt>Hoá đơn</dt><dd>Có mã · người mua Sunrise Hotel</dd>'
      '<dt>Còn thiếu</dt><dd>Không</dd></dl>'
    + '<div class="c-decide__acts" style="margin-top:var(--space-4)"><a class="c-btn c-btn--act" href="order-detail.html">Kiểm tra và tạo đơn</a>'
      '<button class="c-btn" type="button">Sửa</button><button class="c-btn c-btn--quiet" type="button">Bỏ qua</button></div>'
    + '<p class="c-decide__who" style="margin-top:var(--space-2)">Chưa có đơn, chưa giữ hàng — OPC chỉ tạo đơn sau khi kiểm tra đạt</p>')

GIO = (
    '<p class="r-tower__k">Thêm thủ công · ảnh · chị An · 10:41</p><h2 class="r-tower__t" id="d-h">Quán Gió Núi · cần làm rõ 1 điều</h2>'
    f'<figure class="c-quote" style="margin:0"><figcaption class="c-quote__from"><b>Ảnh đơn viết tay</b> chị An chụp lúc 10:40</figcaption>'
    f'<div class="c-quote__media">{ic("i-photo")}<span>“Gió Núi — bò 1 nắng 10 gói, muối kiến <mark>1? 7?</mark> hũ, chiều thứ 4 lấy”</span></div></figure>'
    '<h3 class="c-card__title" style="margin-top:var(--space-4)">Trợ lý hiểu là</h3>'
    + table(line('“bò 1 nắng 10 gói”', 'Bò một nắng 500g', '10 gói', '260.000 ₫', '2.600.000 ₫')
            + line('“muối kiến 1? 7? hũ”', 'Muối kiến vàng 100g', '? hũ', '65.000 ₫', '—', unsure='Chưa rõ: 1 hay 7 hũ'), '2.600.000 ₫', 'Tạm tính, chưa gồm muối (giá lẻ)')
    + '<dl class="c-kv"><dt>Khách</dt><dd>Quán Gió Núi · chưa có hồ sơ → tạo khách mới khi chốt đơn (giá lẻ)</dd>'
      '<dt>Giao</dt><dd>Khách tự lấy · chiều Thứ Tư 07/10/2026</dd></dl>'
    + '<div class="c-decide" role="group" aria-labelledby="q-gio"><p class="c-decide__q" id="q-gio">Hỏi lại khách</p>'
      '<label class="c-field"><span class="c-field__label">Trợ lý soạn sẵn — chị sửa nếu cần</span><span class="c-field__control">'
      '<input class="c-field__input" value="Dạ quán Gió Núi lấy muối kiến vàng 1 hũ hay 7 hũ ạ?"></span></label>'
      f'<div class="c-decide__acts"><button class="c-btn c-btn--act" type="button">{ic("i-send")}Gửi qua Zalo OA</button>'
      f'<button class="c-btn" type="button">{ic("i-phone")}Gọi khách</button><button class="c-btn c-btn--quiet" type="button">Tự sửa số lượng</button></div>'
      '<p class="c-decide__who">Quán Gió Núi chưa nhắn vào Zalo OA của hộ — nếu gửi không được, chị gọi điện cho khách rồi bấm "Tự sửa"</p></div>')


def page(name, cur, detail, title):
    main = (f'\n      {HEAD()}\n      <div class="page">\n        {FILTER}\n        <div class="r-tower r-tower--list">\n'
            f'          <section aria-label="Danh sách yêu cầu"><ul class="c-works">{LIST(cur)}</ul></section>\n'
            f'          <section class="r-tower__detail" aria-labelledby="d-h">{detail}</section>\n        </div>\n      </div>')
    build(name, title, main, 'orders')
    annhien(SCREENS / f'{name}.html')


page('sales-inbox', 'sun', SUN, 'Bán · Yêu cầu · Sunrise Hotel')
page('sales-inbox--unclear', 'gio', GIO, 'Bán · Yêu cầu · cần làm rõ')

# add a request by hand — every source that has no connector
OPT = lambda i, t, m: (f'<button class="c-option c-option--big c-option--action" type="button"><span class="c-option__pic" aria-hidden="true">{ic(i)}</span>'
                       f'<span class="c-option__body"><strong class="c-option__title">{t}</strong><span class="c-option__meta">{m}</span></span></button>')
ADD = ('<div class="c-dialog" role="dialog" aria-modal="true" aria-labelledby="add-t"><div class="c-dialog__panel">'
       '<div class="c-dialog__head"><div><p class="c-dialog__k">Bán · Yêu cầu</p><h2 class="c-dialog__title" id="add-t">Thêm yêu cầu</h2></div>'
       f'<a class="c-icon-btn" href="sales-inbox.html" aria-label="Đóng">{ic("i-x")}</a></div>'
       '<div class="c-dialog__body"><p class="c-sub">Khách đặt qua kênh khác? Đưa vào đây — Trợ lý đọc giúp, OPC kiểm tra như mọi đơn.</p>'
       '<div class="r-pick" style="display:grid;gap:var(--space-2)">'
       + OPT('i-chat', 'Dán hoặc chia sẻ tin nhắn', 'tin nhắn Messenger, SMS… — chép rồi dán, hoặc chia sẻ sang OPC')
       + OPT('i-photo', 'Chụp ảnh đơn', 'Đơn viết tay, bảng kê, ảnh chụp màn hình')
       + OPT('i-mic', 'Ghi âm', 'Khách gọi điện — nói lại đơn, Trợ lý ghi ra chữ')
       + OPT('i-file', 'Tải file', 'Đơn đặt hàng PDF hoặc Excel từ khách sạn, nhà hàng')
       + OPT('i-orders', 'Tự nhập đơn', 'Chọn khách, chọn món — không cần Trợ lý')
       + '</div><label class="c-field" style="margin-top:var(--space-4)"><span class="c-field__label">Khách (nếu biết)</span>'
         '<span class="c-field__control"><input class="c-field__input" placeholder="Tên, số điện thoại hoặc mã số thuế"></span></label>'
         '</div><div class="c-dialog__foot"><p class="c-dialog__note">Đơn định kỳ (ví dụ Sunrise đặt mỗi thứ Hai) đặt trong hồ sơ khách</p></div></div></div>')
main = (f'\n      {HEAD()}\n      <div class="page">\n        {FILTER}\n        <div class="r-tower r-tower--list">\n'
        f'          <section aria-label="Danh sách yêu cầu"><ul class="c-works">{LIST("sun")}</ul></section>\n'
        f'          <section class="r-tower__detail" aria-labelledby="d-h">{SUN}</section>\n        </div>\n      </div>')
build('sales-inbox--add', 'Bán · Thêm yêu cầu', main, 'orders', overlay=ADD)
annhien(SCREENS / 'sales-inbox--add.html')
print('sales inbox: 3 screens')

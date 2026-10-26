"""v4.4 · Destinations the rail needed (were dead links): Bán › Khách hàng (customers, customer-detail = Sunrise),
Hàng hoá › Nhà cung cấp (suppliers), Trợ giúp & hỗ trợ (help). An Nhiên data. Usage: python3 pages_partners.py"""
from pages import build, ic, sign, subnav, CUR

def who(n, m, href='#'):
    n = n if '<a ' in n else f'<a href="{href}">{n}</a>'
    return f'<td class="c-table__cell--main c-table__who"><b>{n}</b><small>{m}</small></td>'
num = lambda v, x='': f'<td class="c-table__num{x}">{v}</td>'
SUB_B = lambda cur: subnav('Bán', [('Yêu cầu', 'sales-inbox.html'), ('Đơn hàng', 'orders.html'), ('Giao hàng', 'delivery.html'), ('Khách hàng', 'customers.html')], cur)
SUB_G = lambda cur: subnav('Hàng hoá', [('Danh sách & giá', 'products.html'), ('Tồn kho', 'stock.html'), ('Chế biến', 'production.html'), ('Nhập hàng & chi phí', 'purchases.html'), ('Nhà cung cấp', 'suppliers.html')], cur)


def head(t, sub, primary):
    return f'<div class="r-page-head"><div><h1 class="r-page-head__title">{t}</h1><p class="c-sub">{sub}</p></div><div class="r-page-head__acts">{primary}</div></div>'


def table(head_cols, rows, label, foot=''):
    cls = lambda n: {1: ' class="c-table__num"', 2: ' class="c-table__cell--opt"'}.get(n, '')
    th = ''.join(f'<th scope="col"{cls(n)}>{h}</th>' for h, n in head_cols)
    return (f'<div class="c-table__scroll" tabindex="0" role="region" aria-label="{label}"><table class="c-table c-table--stack">'
            f'<thead><tr>{th}<th scope="col" class="c-table__cell--act"><span class="u-sr">Xem</span></th></tr></thead><tbody>{rows}</tbody>{foot}</table></div>')


C_ROWS = ''.join([
    '<tr class="c-table__row--you">' + who('<a href="customer-detail.html">Sunrise Hotel</a>', 'khách sạn · chị Mai (bếp) · Zalo OA<span class="c-table__optline"> · trả 15 ngày</span>') + '<td class="c-table__cell--opt">Giá khách sạn & nhà hàng</td><td class="c-table__cell--opt">15 ngày</td>'
    + num('<b>8.400.000 ₫</b>') + f'<td>{sign("err", "i-alert", "Quá hạn 12 ngày")}</td><td class="c-table__cell--end c-table__cell--act"><a class="c-btn" href="customer-detail.html">Xem</a></td></tr>',
    '<tr>' + who('Nhà hàng Phố Núi', 'nhà hàng · Zalo OA<span class="c-table__optline"> · trả 7 ngày</span>') + '<td class="c-table__cell--opt">Giá khách sạn & nhà hàng</td><td class="c-table__cell--opt">7 ngày</td>'
    + num('3.900.000 ₫') + f'<td>{sign("wait", "i-clock", "Hạn 12/10")}</td><td class="c-table__cell--end c-table__cell--act"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
    '<tr>' + who('Homestay Mây Ngàn', 'homestay · thêm tay<span class="c-table__optline"> · trả 15 ngày</span>') + '<td class="c-table__cell--opt">Giá lẻ</td><td class="c-table__cell--opt">15 ngày</td>'
    + num('2.400.000 ₫') + f'<td>{sign("you", "i-alert", "Thiếu email nhận hoá đơn")}</td><td class="c-table__cell--end c-table__cell--act"><a class="c-btn c-btn--quiet" href="#">Sửa</a></td></tr>',
    '<tr>' + who('Chị Thảo', 'Quy Nhơn · gửi xe khách, thu hộ') + '<td class="c-table__cell--opt">Giá lẻ</td><td class="c-table__cell--opt">trả khi nhận</td>' + num('<span class="c-table__zero">0 ₫</span>') + f'<td>{sign("pass", "i-check", "Không nợ")}</td><td class="c-table__cell--end c-table__cell--act"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
    '<tr>' + who('Anh Nam', 'đặt qua Facebook · khách quen') + '<td class="c-table__cell--opt">Giá lẻ</td><td class="c-table__cell--opt">trả trước</td>' + num('<span class="c-table__zero">0 ₫</span>') + f'<td>{sign("pass", "i-check", "Không nợ")}</td><td class="c-table__cell--end c-table__cell--act"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
    '<tr>' + who('Chị Hoa', 'Zalo OA · giao GHTK') + '<td class="c-table__cell--opt">Giá lẻ</td><td class="c-table__cell--opt">thu hộ</td>' + num('<span class="c-table__zero">0 ₫</span>') + f'<td>{sign("pass", "i-check", "Không nợ")}</td><td class="c-table__cell--end c-table__cell--act"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
])
C_FOOT = ('<tfoot><tr><td class="c-table__cell--main">Tổng đang nợ<small class="c-table__foot-note"> · thêm 3.000.000 ₫ thu hộ chờ đối soát ở <a href="receivables.html">Công nợ</a></small></td>'
          '<td class="c-table__cell--opt"></td><td class="c-table__cell--opt"></td><td class="c-table__num"><b>14.700.000 ₫</b></td><td></td><td class="c-table__cell--act"></td></tr></tfoot>')
S_FOOT = ('<tfoot><tr><td class="c-table__cell--main">Tổng phải trả</td><td class="c-table__cell--opt"></td><td class="c-table__num"><b>6.050.000 ₫</b></td><td></td><td class="c-table__cell--act"></td></tr></tfoot>')
CUST = (f'\n      {SUB_B("Khách hàng")}\n      ' + head('Khách hàng', '6 khách quen · 3 khách sỉ ghi nợ · khách lẻ không cần hồ sơ',
                                                   f'<a class="c-btn c-btn--act" href="#">{ic("i-plus")}Thêm khách</a>')
        + '<div class="page"><p class="r-trust r-trust--gate">' + ic('i-search') + '<span><b>Gõ mã số thuế là tự điền</b> tên, địa chỉ cho khách doanh nghiệp. Công nợ chỉ để chị theo dõi: OPC nhắc khi quá hạn, không chặn đơn.</span></p>'
        + table([('Khách', 0), ('Bảng giá', 2), ('Điều khoản', 2), ('Đang nợ', 1), ('Tình trạng', 0)], C_ROWS, 'Khách hàng', C_FOOT) + '</div>')
build('customers', 'Bán · Khách hàng', CUST, 'orders')


def step(kind, src, time, what, detail=''):
    d = f'<span class="c-timeline__who">{detail}</span>' if detail else ''
    return (f'<li class="c-timeline__item c-timeline__item--{kind}"><span class="c-timeline__time">{time}</span><span class="c-timeline__dot" aria-hidden="true"></span>'
            f'<span class="c-timeline__body"><span class="c-timeline__src">{src}</span><span class="c-timeline__what">{what}</span>{d}</span></li>')


DET = (f'\n      {SUB_B("Khách hàng")}\n      <div class="page"><nav class="c-crumbs" aria-label="Đường dẫn"><a href="customers.html">Khách hàng</a><span aria-current="page">Sunrise Hotel</span></nav>'
       '<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">Sunrise Hotel ' + sign('err', 'i-alert', 'Nợ quá hạn 12 ngày') + '</h1>'
       f'<p class="r-detail__fig"><b class="c-figure">8.400.000{CUR}</b><span class="c-sub">đang nợ · trả 15 ngày · quá hạn 12 ngày</span></p></div>'
       f'<div class="r-detail__acts"><a class="c-btn c-btn--act" href="receivable-detail.html">Nhắc nợ</a><a class="c-btn" href="#">{ic("i-plus")}Tạo đơn</a></div></div>'   # overdue → chasing is the primary
       '<div class="r-detail__grid r-detail--calm"><div class="stack">'
       '<p class="c-sub">Công nợ chỉ để chị theo dõi · OPC nhắc khi tới hạn hoặc quá hạn, không chặn đơn mới.</p>'
       '<section class="c-card" aria-labelledby="tt"><div class="c-card__head"><h2 class="c-card__title" id="tt">Thông tin & điều khoản</h2></div>'
       '<dl class="c-kv"><dt>MST</dt><dd>5900987654 · tra từ mã số thuế</dd><dt>Người đặt</dt><dd>chị Mai · bếp · Zalo OA “Đặc sản An Nhiên”</dd>'
       '<dt>Giao đến</dt><dd>cổng bếp, 12 Trần Hưng Đạo, Pleiku</dd><dt>Bảng giá</dt><dd><a href="pricelist.html">Giá khách sạn & nhà hàng</a></dd>'
       '<dt>Hoá đơn</dt><dd>có mã · gửi ketoan@sunrisehotel.vn</dd><dt>Đơn định kỳ</dt><dd>thứ Hai · 15 gói bò, 20 hũ muối</dd></dl></section>'
       '<section class="c-card" aria-labelledby="dg"><div class="c-card__head"><h2 class="c-card__title" id="dg">Đơn gần đây</h2><a class="c-link" href="orders--search.html">Tất cả 14 đơn' + ic('i-chev-r') + '</a></div>'
       '<ul class="c-orders"><li class="c-orders__row"><a href="order-detail.html"><span class="c-orders__who">DH-2052<small>06/10 · Zalo OA</small></span><span class="c-orders__st">' + sign('pend', 'i-box', 'Đã giữ hàng') + '</span><span class="c-orders__amt u-money">6.250.000 ₫</span></a></li>'
       '<li class="c-orders__row"><a href="invoice-detail.html"><span class="c-orders__who">DH-2049<small>06/10 · định kỳ</small></span><span class="c-orders__st">' + sign('ok', 'i-check', 'Đã đóng') + '</span><span class="c-orders__amt u-money">4.550.000 ₫</span></a></li>'
       '<li class="c-orders__row"><a href="receivable-detail.html"><span class="c-orders__who">HĐ 00000193<small>10/09 · chưa trả</small></span><span class="c-orders__st">' + sign('err', 'i-alert', 'Quá hạn') + '</span><span class="c-orders__amt u-money">3.200.000 ₫</span></a></li>'
       '<li class="c-orders__row"><a href="receivable-detail.html"><span class="c-orders__who">HĐ 00000187<small>09/09 · chưa trả</small></span><span class="c-orders__st">' + sign('err', 'i-alert', 'Quá hạn') + '</span><span class="c-orders__amt u-money">5.200.000 ₫</span></a></li></ul></section></div>'
       '<aside class="r-tower__detail" aria-labelledby="hs"><h2 class="r-tower__t" id="hs">Trao đổi gần đây</h2><ol class="c-timeline c-timeline--quiet" aria-label="Trao đổi">'
       + step('now', 'Trợ lý nhắc · Zalo OA', '08:00', 'Nhắc lần 2: 8.400.000 ₫', 'chưa trả lời')
       + step('ok', 'Chị Mai · Zalo OA', '09:02', 'Đặt 20 gói bò, 30 hũ muối', '→ DH-2052')
       + step('ok', 'Chị An', '09:15', 'Xác nhận DH-2052', 'khách hẹn trả nợ cũ khi nhận hàng')
       + step('ok', 'Trợ lý nhắc · Zalo OA', '01/10', 'Nhắc lần 1', 'chị Mai: “cuối tuần chuyển”') + '</ol></aside></div></div>')
build('customer-detail', 'Bán · Khách hàng · Sunrise Hotel', DET, 'orders')

S_ROWS = ''.join([
    '<tr class="c-table__row--you">' + who('HTX Cao Nguyên', href='purchase-detail--receive.html', m='muối kiến vàng<span class="c-table__optline"> · trả 30 ngày</span>') + '<td class="c-table__cell--opt">30 ngày</td>' + num('<b>4.800.000 ₫</b>')
    + f'<td>{sign("you", "i-alert", "MH-0118 thiếu 5 hũ · chờ chị")}</td><td class="c-table__cell--end c-table__cell--act"><a class="c-btn" href="purchase-detail--receive.html">Xem</a></td></tr>',
    '<tr>' + who('Cơ sở bò một nắng Krông Pa', 'bò một nắng 500g<span class="c-table__optline"> · trả 15 ngày</span>') + '<td class="c-table__cell--opt">15 ngày</td>' + num('<span class="c-table__zero">0 ₫</span>')
    + f'<td>{sign("wait", "i-clock", "MH-0121 về Thứ Năm")}</td><td class="c-table__cell--end c-table__cell--act"><a class="c-btn c-btn--quiet" href="purchases.html">Xem</a></td></tr>',
    '<tr>' + who('Điện lực Gia Lai', href='receivables--payables.html', m='tiền điện · MST 0300942001-012') + '<td class="c-table__cell--opt">theo hoá đơn</td>' + num('1.250.000 ₫') + f'<td>{sign("wait", "i-clock", "Hạn 10/10")}</td><td class="c-table__cell--end c-table__cell--act"><a class="c-btn c-btn--quiet" href="receivables--payables.html">Xem</a></td></tr>',
    '<tr>' + who('Bao bì Phú Mỹ', 'túi, thùng giao hàng · có hoá đơn điện tử') + '<td class="c-table__cell--opt">trả ngay</td>' + num('<span class="c-table__zero">0 ₫</span>') + f'<td>{sign("pass", "i-check", "Không nợ")}</td><td class="c-table__cell--end c-table__cell--act"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
])
SUP = (f'\n      {SUB_G("Nhà cung cấp")}\n      ' + head('Nhà cung cấp', '4 nhà cung cấp · chị An tự chuyển tiền trong app ngân hàng, OPC ghi nhận',
                                                    f'<a class="c-btn c-btn--act" href="#">{ic("i-plus")}Thêm nhà cung cấp</a>')
       + '<div class="page">' + table([('Nhà cung cấp', 0), ('Điều khoản', 2), ('Phải trả', 1), ('Tình trạng', 0)], S_ROWS, 'Nhà cung cấp', S_FOOT) + '</div>')
build('suppliers', 'Hàng hoá · Nhà cung cấp', SUP, 'goods')


def card(icon, t, m, act, href='#', primary=False):
    return (f'<li class="r-help__c"><span class="r-gate__pic">{ic(icon)}</span><span class="r-gate__b"><b>{t}</b><small>{m}</small></span>'
            f'<a class="c-btn{" c-btn--act" if primary else ""}" href="{href}">{act}</a></li>')


HELP = ('\n      ' + head('Trợ giúp & hỗ trợ', 'Hỏi Trợ lý trước; cần người thật thì OPC Gia Lai ở ngay đây', '')
        + '<div class="page"><label class="c-search c-search--strong r-help__find">' + ic('i-search') + '<span class="u-sr">Tìm hướng dẫn</span><input class="c-search__input" type="search" placeholder="Ví dụ: tiền QR chưa về, đổi giá, đóng ca…"></label>'
        '<div class="r-detail__grid r-detail--calm"><div class="stack">'
        '<section class="c-card" aria-labelledby="hp1"><div class="c-card__head"><h2 class="c-card__title" id="hp1">Cần giúp ngay</h2></div><ul class="r-help__list">'
        + card('i-chat', 'Hỏi Trợ lý', 'trả lời theo đúng màn chị đang xem · không tự làm thay chị', 'Hỏi', 'home--assistant.html', primary=True)
        + card('i-phone', 'Gọi chị Thu · OPC Gia Lai', '8:00–17:00, Thứ Hai đến Thứ Bảy · 0269 3 812 400', 'Gọi')
        + card('i-chat', 'Nhắn Zalo OPC Gia Lai', 'trả lời trung bình 18 phút', 'Nhắn')
        + card('i-people', 'Hẹn nhân viên đến hộ', 'đếm tồn, nhập khách, hướng dẫn người mới', 'Đặt lịch') + '</ul></section>'
        '<section class="c-card" aria-labelledby="hp2"><div class="c-card__head"><h2 class="c-card__title" id="hp2">Hướng dẫn 30 giây</h2></div><ul class="r-help__list">'
        + card('i-play', 'Bán ở quầy và thu QR', 'Hạnh, Quầy', 'Xem', 'counter.html')
        + card('i-play', 'Nhận đơn khách sỉ từ Zalo OA', 'Yêu cầu → đơn → giữ hàng', 'Xem', 'sales-inbox.html')
        + card('i-play', 'Đóng ca và nộp tiền thu hộ', 'Tiền › Đóng ca', 'Xem', 'shift-close.html')
        + card('i-play', 'Đối chiếu kỳ trước khi khai thuế', 'Sổ & thuế › Kỳ thuế', 'Xem', 'period.html') + '</ul></section></div>'
        '<aside class="r-tower__detail" aria-labelledby="st"><h2 class="r-tower__t" id="st">Tình trạng lúc này</h2><ul class="r-gate">'
        '<li class="r-gate__i r-gate__i--unk"><span class="r-gate__b"><b>X Invoice không trả lời</b><small><span class="r-gate__st">Từ 10:12</span> · hoá đơn B2B làm tay trên cổng X Invoice được</small></span><span class="r-gate__amt"></span><span class="r-gate__act"><a class="c-btn c-btn--quiet" href="connections.html">Xem</a></span></li>'
        '<li class="r-gate__i r-gate__i--ok"><span class="r-gate__b"><b>MB, Hilo, Zalo OA</b><small><span class="r-gate__st">Hoạt động</span> · cập nhật 2 phút trước</small></span><span class="r-gate__amt"></span><span class="r-gate__act"></span></li></ul>'
        '<p class="c-sub">Báo lỗi kèm ảnh màn hình: nhân viên OPC thấy đúng màn chị đang xem, không thấy mật khẩu.</p></aside></div></div>')
build('help', 'Trợ giúp & hỗ trợ', HELP, 'help')
print('partners: 4 screens')

"""v4.3 · Đơn hàng sources in An Nhiên data: src_v40/orders*.html (Cô Hai) → src_v43/orders*.html. pages_orders.py
reads src_v43 when present. Today 06/10 to 10:45: 8 orders across Quầy / Zalo OA / Thêm tay / Định kỳ (source column).
Usage: python3 orders43.py (before pages_orders.py)"""
import re, pathlib
HERE = pathlib.Path(__file__).parent
ic = lambda i: f'<svg class="c-ic" aria-hidden="true"><use href="#{i}"/></svg>'
sg = lambda k, i, t: f'<span class="c-sign c-sign--{k}"><span class="c-sign__pic">{ic(i)}</span>{t}</span>'
OK_INV = lambda n: f'{n}<span class="u-sr"> · có mã</span>'   # v4.5.1: a number = has a code; only problems get a sign
#        code      time     who                 channel     items total        pay        status                                          invoice                         you
ROWS = [('DH-2053', '10:44', 'Khách lẻ',          'Quầy',      2, '715.000',   'QR',       sg('wait', 'i-qr', 'Chờ khách chuyển'),           '—', False),
        ('DH-2052', '09:02', 'Sunrise Hotel',     'Zalo OA',   2, '6.250.000', 'Công nợ',  sg('pend', 'i-box', 'Đã giữ hàng · giao 15:00'),  'đề xuất khi giao', False),
        ('DH-2051', '08:50', 'Nhà hàng Phố Núi',  'Zalo OA',   2, '1.150.000', 'Thu hộ',   sg('wait', 'i-clock', 'Đang giao'),              '—', False),
        ('DH-2049', '08:30', 'Sunrise Hotel',     'Định kỳ',   2, '4.550.000', 'QR',       sg('ok', 'i-check', 'Đã đóng'),                   OK_INV('00000231'), False),
        ('DH-2048', '09:05', 'Khách lẻ',          'Quầy',      1, '195.000',   'QR',       sg('ok', 'i-check', 'Đã đóng'),                   OK_INV('00001288'), False),
        ('DH-2047', '08:15', 'Nhà hàng Phố Núi',  'Zalo OA',   1, '1.840.000', 'Công nợ',  sg('you', 'i-alert', 'Chờ tiền'), sg('unk', 'i-clock', 'Chưa rõ kết quả'), True),
        ('DH-2046', '07:50', 'Chị Hoa',           'Zalo OA',   1, '260.000',   'Thu hộ',   sg('wait', 'i-clock', 'Đã giao · chờ GHTK trả'),  OK_INV('00001281'), False),
        ('DH-2045', '07:40', 'Homestay Mây Ngàn', 'Thêm tay',  1, '390.000',   'Chuyển khoản', sg('pend', 'i-alert', 'Chờ xác minh · quá 30 phút'), OK_INV('00000230'), True)]
LINE = {'pend': (2, 'chờ xác minh'), 'wait': (1, 'chưa thu'), 'you': (1, 'chưa thu')}


def row(r, check=False, checked=False):
    code, t, who, ch, n, tot, pay, st, inv, you = r
    k = re.search(r'c-sign--(\w+)', st).group(1)
    ml = (f'<span class="c-moneyline" data-step="{LINE[k][0]}" role="img" aria-label="Bước {LINE[k][0]}/3: {LINE[k][1]}"><s></s><s></s><s></s></span>' if k in LINE else '')
    total = f'<span class="c-table__total">{ml}<span class="u-money">{tot} ₫</span></span>' if ml else f'<span class="u-money">{tot} ₫</span>'
    c = (f'<td class="c-table__cell--hide"><label class="c-check"><input class="c-check__input" type="checkbox" aria-label="Chọn {code}"{" checked" if checked else ""}></label></td>' if check else '')
    return (f'<tr{" class=" + chr(34) + "c-table__row--you" + chr(34) if you else ""}>{c}<td class="c-table__code c-table__cell--main">{code}</td><td class="c-table__cell--hide c-table__cell--opt">{t}</td>'
            f'<td class="c-table__cell--wide">{who}<span class="c-table__phone"> · {ch}</span><span class="u-sr"> · {t} · {n} món · {pay}</span></td><td class="c-table__cell--hide c-table__cell--opt">{ch}</td>'
            f'<td class="c-table__num c-table__cell--hide c-table__cell--opt">{n}</td>\n                <td class="c-table__num c-table__cell--end">{total}</td><td class="c-table__cell--hide">{pay}</td>\n'
            f'                <td class="c-table__cell--wide">{st}</td><td class="c-table__cell--hide c-table__cell--opt">{inv}</td></tr>')


FILTERED = [('DH-2047', '06/10', 'Nhà hàng Phố Núi', 'Zalo OA', 1, '1.840.000', 'Công nợ', sg('you', 'i-alert', 'Chờ tiền · hạn 13/10'), sg('unk', 'i-clock', 'Chưa rõ kết quả'), True),
            ('DH-2044', '05/10', 'Nhà hàng Phố Núi', 'Zalo OA', 2, '3.900.000', 'Công nợ', sg('wait', 'i-clock', 'Chờ tiền · hạn 12/10'), OK_INV('00000228'), False),
            ('DH-2041', '03/10', 'Homestay Mây Ngàn', 'Zalo OA', 2, '2.400.000', 'Công nợ', sg('wait', 'i-clock', 'Chờ tiền · hạn 18/10'), OK_INV('00000226'), False)]

COMMON = [
    ('<nav class="c-subnav" aria-label="Bán"><a class="c-subnav__item" href="orders.html" aria-current="page">Đơn hàng</a><a class="c-subnav__item" href="#">Giao hàng</a><a class="c-subnav__item" href="customers.html">Khách hàng</a></nav>',
     '<nav class="c-subnav" aria-label="Bán"><a class="c-subnav__item" href="sales-inbox.html">Yêu cầu</a><a class="c-subnav__item" href="orders.html" aria-current="page">Đơn hàng</a><a class="c-subnav__item" href="delivery.html">Giao hàng</a><a class="c-subnav__item" href="customers.html">Khách hàng</a></nav>'),
    ('Thứ Sáu, 02/10/2026 · 23 đơn', 'Thứ Ba, 06/10/2026 · 8 đơn · Quầy, Zalo OA, thêm tay, định kỳ'),
    ('Thứ Sáu, 02/10/2026 · 4 đơn trong bộ lọc', 'Thứ Ba, 06/10/2026 · 3 đơn trong bộ lọc'),
    ('Chờ xác minh <span class="c-tabs__count">2</span>', 'Chờ xác minh <span class="c-tabs__count">1</span>'),
    ('Hoàn tất <span class="c-tabs__count">19</span>', 'Đã đóng <span class="c-tabs__count">2</span>'),
    ('Hôm nay <span class="c-tabs__count">23</span>', 'Hôm nay <span class="c-tabs__count">8</span>'),
    ('Xem thêm 11 đơn', 'Xem đơn hôm qua'),
    # filters panel
    ('>Tại quầy<', '>Quầy<'), ('>Zalo<', '>Zalo OA<'), ('>Shopee<', '>Thêm tay<'), ('>Điện thoại<', '>Định kỳ<'),
    ('>Đơn chờ xác nhận<', '>Chờ duyệt<'), ('>Hoàn tất<', '>Đã đóng<'), ('>Chờ mã<', '>Chưa rõ kết quả<'), ('Xem 4 đơn', 'Xem 3 đơn'),
    # filtered
    ('Chưa thu <b>9.870.000 ₫</b> trong 4 đơn — <b>DH-0866</b> quá hạn 2 ngày, nhắc khách trước.', 'Chưa thu <b>8.140.000 ₫</b> trong 3 đơn — chưa đơn nào quá hạn; DH-2047 cần rõ hoá đơn trước khi nhắc.'),
    ('4 đơn · 9.870.000 ₫', '3 đơn · 8.140.000 ₫'), ('<span class="c-chip__k">Thời gian:</span> 26/9 – 02/10', '<span class="c-chip__k">Thời gian:</span> 30/9 – 06/10'), ('<span class="c-chip__k">Kênh:</span> Zalo, Shopee', '<span class="c-chip__k">Kênh:</span> Zalo OA'),
    # daterange
    ('7 ngày · 168 đơn', '7 ngày · 54 đơn'),
    # noresult
    ('DH-0999', 'DH-1999'),
    # bulk
    ('2 đơn · 5.570.000 ₫', '2 đơn · 2.100.000 ₫'), ('2 đơn · <b>5.570.000 ₫</b>', '2 đơn · <b>2.100.000 ₫</b>'), ('<span class="c-bulkbar__sum">5.570.000 ₫</span>', '<span class="c-bulkbar__sum">2.100.000 ₫</span>'),
    ('Đã xuất 23 đơn ra Excel', 'Đã xuất 8 đơn ra Excel'),
    # search
    ('value="hải âu"', 'value="sunrise"'),
    ('<span>Khách sạn <mark>Hải Âu</mark><span class="c-menu__sub">8 đơn · công nợ 3.420.000 ₫</span></span>', '<span><mark>Sunrise</mark> Hotel<span class="c-menu__sub">14 đơn · nợ 8.400.000 ₫, quá hạn 12 ngày</span></span>'),
    ('<span>DH-1040<span class="c-menu__sub">Khách sạn <mark>Hải Âu</mark> · 02/10 · 3.420.000 ₫</span></span>', '<span>DH-2052<span class="c-menu__sub"><mark>Sunrise</mark> Hotel · 06/10 · 6.250.000 ₫ · đã giữ hàng</span></span>'),
    ('<span>DH-0866<span class="c-menu__sub">Khách sạn <mark>Hải Âu</mark> · 27/9 · 3.150.000 ₫</span></span>', '<span>DH-2049<span class="c-menu__sub"><mark>Sunrise</mark> Hotel · 06/10 · 4.550.000 ₫ · định kỳ</span></span>'),
    ('Tìm “hải âu” trong tất cả thời gian', 'Tìm “sunrise” trong tất cả thời gian'),
]
PEEK = [('Xem nhanh · 09:48 hôm nay', 'Xem nhanh · 09:02 hôm nay'), ('id="peek-title">DH-1040', 'id="peek-title">DH-2052'),
        ('Chờ xác nhận · giao 15:00</span></div>', 'Đã giữ hàng · giao trước 15:00</span></div>'),
        ('<dt>Khách</dt><dd>Khách sạn Hải Âu</dd>', '<dt>Khách</dt><dd>Sunrise Hotel · giá khách sạn</dd>'),
        ('<dt>Người đặt</dt><dd>anh Quang · 0914 223 456</dd>', '<dt>Người đặt</dt><dd>chị Mai · bếp · Zalo OA</dd>'),
        ('<dt>Giao đến</dt><dd>18 Nguyễn Huệ, Quy Nhơn · 15:00</dd>', '<dt>Giao đến</dt><dd>cổng bếp, 12 Trần Hưng Đạo, Pleiku · trước 15:00</dd>'),
        ('<span class="c-list__name">Cá cơm sấy giòn</span><span class="c-list__amt">2.040.000 ₫</span><span class="c-list__meta">3 kg × 680.000 ₫</span>', '<span class="c-list__name">Bò một nắng 500g</span><span class="c-list__amt">4.600.000 ₫</span><span class="c-list__meta">20 gói × 230.000 ₫</span>'),
        ('<span class="c-list__name">Tôm khô loại 1</span><span class="c-list__amt">1.380.000 ₫</span><span class="c-list__meta">2 kg × 690.000 ₫</span>', '<span class="c-list__name">Muối kiến vàng 100g</span><span class="c-list__amt">1.650.000 ₫</span><span class="c-list__meta">30 hũ × 55.000 ₫</span>'),
        ('<span class="u-money">3.420.000 ₫</span><span class="c-sign c-sign--wait">', '<span class="u-money">6.250.000 ₫</span><span class="c-sign c-sign--wait">'),
        ('Chưa thu · công nợ</span>', 'Chưa thu · công nợ 15 ngày</span>'),
        ('<span class="c-timeline__what">Chờ chị xác nhận</span><span class="c-timeline__who">giao hàng lúc 15:00</span>', '<span class="c-timeline__what">Chờ soạn hàng</span><span class="c-timeline__who">giao trước 15:00 · anh Hùng giao</span>'),
        ('<span class="c-timeline__time">09:50</span><span class="c-timeline__dot" aria-hidden="true"></span><span class="c-timeline__body"><span class="c-timeline__what">OPC tạo đơn từ tin nhắn</span><span class="c-timeline__who">Trợ lý · Phúc kiểm tra</span>',
         '<span class="c-timeline__time">09:15</span><span class="c-timeline__dot" aria-hidden="true"></span><span class="c-timeline__body"><span class="c-timeline__what">Chị An xác nhận · giữ hàng</span><span class="c-timeline__who">OPC giữ 20 gói bò, 30 hũ muối</span>'),
        ('<span class="c-timeline__time">09:48</span><span class="c-timeline__dot" aria-hidden="true"></span><span class="c-timeline__body"><span class="c-timeline__what">Khách đặt qua Zalo</span><span class="c-timeline__who">“3kg cá cơm, 2kg tôm khô, giao 3h chiều”</span>',
         '<span class="c-timeline__time">09:02</span><span class="c-timeline__dot" aria-hidden="true"></span><span class="c-timeline__body"><span class="c-timeline__what">Trợ lý đọc tin Zalo OA của chị Mai</span><span class="c-timeline__who">“20 gói bò, 30 hũ muối, giao trước 3h chiều mai”</span>'),
        ('Xác nhận đơn' + ic('i-arrow'), 'Soạn hàng' + ic('i-arrow')), ('<button class="c-btn c-btn--act" type="button">Soạn hàng', '<a class="c-btn c-btn--act" href="delivery--pick.html">Soạn hàng')]
PREVIEW = [('Gửi nhắc nợ cho 2 khách · 5.570.000 ₫', 'Gửi nhắc nợ cho 2 khách · 2.100.000 ₫'),
           ('Nhà hàng Biển Đông có thể đã trả', 'Chị Hoa đã trả cho GHTK'),
           ('Khoản 2.150.000 ₫ lúc 09:15 chưa gán vào đơn. Bỏ khách này khỏi lần gửi?', 'Tiền thu hộ 260.000 ₫ đang ở GHTK, chưa về tài khoản. Bỏ khách này khỏi lần gửi?'),
           ('Gán tiền trước', 'Bỏ khỏi lần gửi'),
           ('Khách sạn Hải Âu · anh Quang', 'Nhà hàng Phố Núi'), ('3.420.000 ₫', '1.840.000 ₫'),
           ('DH-1040 · hạn trả 09/10/2026 · Zalo 0914 223 456', 'DH-2047 · hạn trả 13/10/2026 · Zalo OA'),
           ('Nhà hàng Biển Đông', 'Chị Hoa'), ('2.150.000 ₫', '260.000 ₫'), ('DH-1038 · có khoản chuyển 09:15 chưa gán — nên gán trước khi nhắc', 'DH-2046 · GHTK chưa trả tiền thu hộ — nên nhắc GHTK, không nhắc khách'),
           ('<span class="c-hh__mark" aria-hidden="true">CH</span><span>Hải sản khô Cô Hai<small>qua OPC · Zalo · mẫu “Nhắc thanh toán”</small>', '<span class="c-hh__mark" aria-hidden="true">AN</span><span>Đặc sản An Nhiên<small>qua Zalo OA · mẫu “Nhắc thanh toán”</small>'),
           ('Kính gửi anh Quang (Khách sạn Hải Âu), đơn DH-1040 · 1.840.000 ₫ đến hạn thanh toán ngày 09/10/2026.', 'Kính gửi Nhà hàng Phố Núi, đơn DH-2047 · 1.840.000 ₫ đến hạn thanh toán ngày 13/10/2026.'),
           ('Gửi 2 tin nhắc', 'Gửi 1 tin nhắc')]


def build_src(name):
    s = (HERE / f'src_v40/{name}.html').read_text()
    for a, b in COMMON:
        s = s.replace(a, b)
    tb = re.search(r'<tbody>(.*?)</tbody>', s, re.S)
    if tb and 'c-skel' not in tb.group(1) and tb.group(1).strip():
        check = 'c-check' in tb.group(1)
        if name == 'orders--filtered':
            body = ''.join(row(r) for r in FILTERED)
        else:
            body = ''.join(row(r, check, checked=check and r[0] in ('DH-2047', 'DH-2046')) for r in ROWS)
        s = s[:tb.start(1)] + '\n              ' + body + '\n            ' + s[tb.end(1):]
    if name == 'orders--peek':
        for a, b in PEEK:
            assert a in s, (name, a[:60]); s = s.replace(a, b)
        # v4.5.6: on a phone the read-only peek body scrolls — keyboard users need to reach it (axe scrollable-region-focusable)
        s = s.replace('<div class="c-drawer__body">', '<div class="c-drawer__body" tabindex="0" role="region" aria-label="Chi tiết đơn">', 1)
    if name == 'orders--bulk--preview':
        for a, b in PREVIEW:
            assert a in s, (name, a[:60]); s = s.replace(a, b)
    s = s.replace('<button class="c-btn" type="button">Xoá tìm kiếm', '<button class="c-btn c-btn--quiet" type="button">Xoá tìm kiếm')   # v4.5.6: reason + one primary + a text link
    if name == 'orders--daterange':   # v4.5.10: both date fields the same height; the hint spans both
        s = re.sub(r'(<div class="c-field__control"><input class="c-field__input" id="d-to"[^>]*></div>)<span class="c-field__hint">([^<]*)</span>', r'\1', s)
        s = s.replace('</div>\n    </div>\n    <div class="c-dialog__foot">', '</div>\n      <p class="c-field__hint r-dates__hint">Không chọn được ngày sau hôm nay.</p>\n    </div>\n    <div class="c-dialog__foot">', 1)
    # v4.5.1 icons budget: labelled controls carry no icon (the verb is written)
    s = s.replace('<svg class="c-ic" aria-hidden="true"><use href="#i-menu"/></svg>Lọc</button>', 'Lọc</button>')
    s = s.replace('Mở quầy<svg class="c-ic" aria-hidden="true"><use href="#i-arrow"/></svg></a>', 'Mở quầy</a>')
    s = s.replace('<svg class="c-ic" aria-hidden="true"><use href="#i-plus"/></svg>Tạo đơn</button>', 'Tạo đơn</button>')
    for ico in ('i-send', 'i-print', 'i-download'):   # labelled bulk actions
        s = re.sub(r'(<(?:a|button) class="c-btn[^"]*"[^>]*>[^<]+)<svg class="c-ic" aria-hidden="true"><use href="#' + ico + r'"/></svg>', r'\1', s)
        s = re.sub(r'(<(?:a|button) class="c-btn[^"]*"[^>]*>)<svg class="c-ic" aria-hidden="true"><use href="#' + ico + r'"/></svg>', r'\1', s)
    s = s.replace('<svg class="c-ic" aria-hidden="true"><use href="#i-search"/></svg><span>Tìm “sunrise”', '<span>Tìm “sunrise”')
    (HERE / f'src_v43/{name}.html').write_text(s)
    left = [w for w in ['Hải Âu', 'Biển Đông', 'Biển Xanh', 'Cô Hai', 'Phúc', 'Quy Nhơn', 'DH-10', 'DH-08', 'Shopee', 'Chị Thu', 'cá cơm', 'Tôm'] if w in s[s.find('<main'):]]
    print(name, 'LEFT ' + ','.join(left) if left else 'ok')


for n in ['orders', 'orders--search', 'orders--filters', 'orders--daterange', 'orders--filtered', 'orders--noresult',
          'orders--loading', 'orders--peek', 'orders--bulk', 'orders--bulk--preview']:
    build_src(n)

"""v4.9.0 · Kết nối at scale, part 2:
  connections--delivery  category hub "Giao hàng": the ways to deliver (own staff / carriers / bus), how the carrier is chosen, a quote preview
  connections--many      "Đã nối" when the household has connected many accounts (14): problems first, chips, grouped compact rows
Usage: python3 pages_connect3b.py — after pages_connect3.py."""
from connect_lib import *


def carrier(mono, name, attrs, state, default=False, href='#'):
    d = '<span class="r-car__def">Mặc định</span>' if default else '<a class="c-btn c-btn--quiet" href="#">Đặt mặc định</a>'
    chips = ''.join(f'<li>{a}</li>' for a in attrs)
    return (f'<li class="r-car"><span class="r-acct__logo" aria-hidden="true">{mono}</span><span class="r-car__b"><b class="r-car__n"><a class="r-dir__link" href="{href}">{name}</a> {state}</b>'
            f'<ul class="r-car__attrs">{chips}</ul></span>{d}</li>')


CARS = ''.join([
    carrier('N', 'Người của hộ · anh Hùng', ['link cho người giao, không cần tài khoản', 'thu hộ: hộ thu', 'Pleiku'], '', True),
    carrier('G', 'GHTK', ['thu hộ ✓', 'toàn quốc', 'đối soát thứ Sáu'], '<span class="c-sim">Mô phỏng</span>', False, 'connections--info.html'),
    carrier('Đ', 'Nhà xe Đức Long', ['nhập mã biên nhận', 'thu hộ: khi khách nhận', 'Quy Nhơn'], ''),
])


def opt(on, t, m, dis=False):
    return (f'<button class="c-option{" c-option--on" if on else ""}" type="button" role="radio" aria-checked="{"true" if on else "false"}"{" aria-disabled=\"true\"" if dis else ""}>'
            f'<span class="c-option__radio" aria-hidden="true"></span><span class="c-option__body"><strong class="c-option__title">{t}</strong><span class="c-option__meta">{m}</span></span></button>')


def q(cls, t, price, when, note=''):
    return (f'<li class="r-quote__i{cls}"><span class="r-quote__n"><b>{t}</b><small>{note}</small></span><span class="r-quote__p">{price}</span><span class="r-quote__w">{when}</span></li>')


QUOTE = ''.join([q(' r-quote__i--pick', 'GHTK · Trợ lý đề xuất', '32.000 ₫', '3 ngày', 'rẻ nhất · thu hộ ✓'),
                 q('', 'Nhà xe Đức Long', '60.000 ₫', '1 ngày', 'thu hộ khi khách nhận'),
                 q(' r-quote__i--no', 'Người của hộ', '—', 'không giao được', 'ngoài Pleiku')])

DELIVERY = (crumb(('Kết nối', 'connections.html'), 'Giao hàng')
            + dhead('Giao hàng', '', '3 cách giao đang dùng · mặc định: người của hộ', '<a class="c-btn c-btn--act" href="connections--add.html">Thêm hãng</a>')
            + grid(card('cw', 'Cách giao đang dùng', f'<ul class="r-car__list">{CARS}</ul>')
                   + card('cc', 'Cách chọn hãng', '<div class="c-options" role="radiogroup" aria-label="Cách chọn hãng">'
                          + opt(True, 'Trợ lý đề xuất, người bàn giao chọn', 'hiện giá và thời gian từng hãng khi tạo vận đơn')
                          + opt(False, 'Luôn dùng hãng mặc định', 'không hỏi lại, chị đổi được từng đơn')
                          + opt(False, 'Quy tắc tự động', 'theo cân nặng, vùng, giao trong ngày · sắp có', True) + '</div>'),
                   '<aside class="r-tower__detail" aria-labelledby="rl"><h2 class="r-tower__t" id="rl">Ví dụ: bàn giao DH-2046</h2>'
                   '<p class="c-sub">Chị Hoa · Quy Nhơn · thu hộ 260.000 ₫ · số liệu mô phỏng</p>'
                   f'<ul class="r-quote">{QUOTE}</ul></aside>'))
save('connections--delivery', 'Kết nối · Giao hàng', '<div class="page">' + DELIVERY + '</div>')

# ---------------------------------------------------------------- Đã nối with many accounts
G = [('Giao hàng', 'connections--delivery.html', [('G', 'GHTK', 'thu hộ · đối soát', 'ok'), ('G', 'GHN', 'thu hộ', 'ok'), ('J', 'J&T Express', 'đồng ý hết hạn 12/11', 'exp'), ('A', 'Ahamove', 'giao trong ngày', 'ok')]),
     ('Bán online', '#', [('S', 'Shopee · Cửa hàng 1', 'đơn, tiền sàn', 'ok'), ('S', 'Shopee · Cửa hàng 2', 'cần đăng nhập lại', 'exp'), ('T', 'TikTok Shop', 'đơn, tiền sàn', 'ok')]),
     ('Tiền và ngân hàng', '#', [('M', 'MB qua Casso', 'tiền về · QR · chuyển tiền', 'ok'), ('p', 'payOS', 'QR thu tiền', 'ok')]),
     ('Hoá đơn và thuế', '#', [('H', 'Hilo', 'hoá đơn quầy', 'ok'), ('X', 'X Invoice', 'im lặng từ 10:12', 'err'), ('G', 'Casso GDT Hub', 'hoá đơn mua vào', 'ok')]),
     ('Nhận đơn và định danh', '#', [('Z', 'Zalo OA · Đặc sản An Nhiên', 'nhận đơn · trả lời khách', 'ok'), ('C', 'Cas ID', 'chị An · mức L1', 'ok')])]
ST = {'ok': sign('pass', 'i-check', 'Hoạt động'), 'err': sign('err', 'i-x', 'Lỗi'), 'exp': sign('pend', 'i-clock', 'Sắp hết hạn')}


def crow(m, n, j, st):
    href = 'connections--detail.html' if st == 'err' else 'connections--account.html'
    return (f'<li class="r-crow r-crow--{st}"><a class="r-crow__a" href="{href}"><span class="r-acct__logo r-crow__logo" aria-hidden="true">{m}</span>'
            f'<span class="r-crow__b"><b>{n}</b><small>{j}</small></span><span class="r-crow__st">{ST[st]}</span></a></li>')


GROUPS = ''.join(f'<section class="r-crow__g" aria-labelledby="k{i}"><h2 class="r-dir__h" id="k{i}"><a class="r-dir__link" href="{h}">{t}</a> <span class="u-meta">{len(ps)}</span></h2><ul class="r-crow__list">'
                 + ''.join(crow(*p) for p in ps) + '</ul></section>' for i, (t, h, ps) in enumerate(G))
NEEDS = ''.join([
    row('unk', 'Lỗi', 'X Invoice · DH-2047 chưa rõ kết quả', '', '<a class="c-btn" href="connections--detail.html">Xem</a>'),
    row('wait', 'Sắp hết hạn', 'J&T Express · 12/11', '', '<a class="c-btn" href="connections--consent.html">Nối lại</a>'),
    row('wait', 'Cần đăng nhập lại', 'Shopee · Cửa hàng 2', '', '<a class="c-btn" href="connections--consent.html">Nối lại</a>')])
MANY = (head('Kết nối', '14 tài khoản · 11 chạy tốt · 1 lỗi · 2 sắp hết hạn', '<a class="c-btn c-btn--act" href="connections--category.html">Thêm kết nối</a>')
        + '<div class="page">' + tabs('Đã nối', 14)
        + card('nd', 'Cần chị xem · 3', f'<ul class="r-gate">{NEEDS}</ul>')
        + chips('Lọc tài khoản', ['Tất cả 14', 'Lỗi 1', 'Sắp hết hạn 2', 'Theo nhóm'], 3)
        + GROUPS + '</div>')
save('connections--many', 'Kết nối · Khi nối nhiều', MANY)
print('connect3b: delivery + many')

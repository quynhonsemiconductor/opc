"""v4.3 · Counter templates in An Nhiên data (FLOWS §0.1 + ①). Reads src/counter*.html (Cô Hai), writes
src_v43/counter.html and src_v43/counter--qr.html: 2 products with 'còn · đã giữ', known-customer chips, order
DH-2053 = 2 gói bò + 3 hũ muối = 715.000 ₫, cashier Hạnh. Run before states.py. Usage: python3 src43.py"""
import re, pathlib

import re as _re
def strip_quiet_icons(h):
    """v4.5.3 icons budget: money-step dots and labelled payment options carry no icon."""
    h = _re.sub(r'(<span class="c-paysteps__dot">)<svg[^>]*>.*?</svg>', r'\1', h, flags=_re.S)
    h = _re.sub(r'(<button class="c-seg__opt"[^>]*>)<svg class="c-ic"[^>]*>.*?</svg>', r'\1', h, flags=_re.S)
    return h
HERE = pathlib.Path(__file__).parent
ic = lambda i: f'<svg class="c-ic" aria-hidden="true"><use href="#{i}"/></svg>'


def tile(name, price, meta, pic, incart=None, low=False):
    q = f'<span class="c-tile__qty" aria-hidden="true">{ic("i-check")}×{incart}</span>' if incart else ''
    lab = f' data-incart aria-label="{name}, {price} ₫, trong đơn {incart}, {meta}"' if incart else f' aria-label="{name}, {price} ₫, {meta}"'
    return (f'<button class="c-tile c-tile--big" type="button"{lab}><span class="c-tile__pic c-tile__pic--{pic[0]}" aria-hidden="true"><svg class="c-ic"><use href="#{pic[1]}"/></svg></span>{q}'
            f'<span class="c-tile__name">{name}</span><span class="c-tile__price">{price} ₫</span>'
            f'<span class="c-tile__meta{" c-tile__meta--low" if low else ""}">{meta}</span><span class="c-tile__add" aria-hidden="true"><svg class="c-ic"><use href="#i-plus"/></svg></span></button>')


TILES = ('<div class="c-tiles c-tiles--few">'
         + tile('Bò một nắng 500g', '260.000', 'còn 26 · đã giữ 20', ('warm', 'i-box'), 2)
         + tile('Muối kiến vàng 100g', '65.000', 'còn 50 · đã giữ 30', ('leaf', 'i-jar'), 3)
         + '</div>')
KNOWN = ('<div class="r-pos__known" role="group" aria-label="Khách quen"><span class="u-meta">Khách quen:</span>'
         '<button class="c-chip r-pos__kc" type="button">Sunrise Hotel</button><button class="c-chip r-pos__kc" type="button">Nhà hàng Phố Núi</button>'
         '<button class="c-chip r-pos__kc" type="button">Homestay Mây Ngàn</button></div>')


def stepper(label, v):
    return (f'<span class="c-stepper"><button class="c-stepper__btn" type="button" aria-label="Bớt {label}">{ic("i-minus")}</button>'
            f'<output class="c-stepper__value">{v}</output><button class="c-stepper__btn" type="button" aria-label="Thêm {label}">{ic("i-plus")}</button></span>')


LINES = ('<ul class="r-order__lines">'
         f'<li class="c-oline"><span class="c-oline__name">Bò một nắng 500g</span><span class="c-oline__amt">520.000 ₫</span><span class="c-oline__calc">2 × 260.000 ₫ · lô BMN-0405</span>\n          {stepper("bò một nắng", 2)}</li>'
         f'<li class="c-oline"><span class="c-oline__name">Muối kiến vàng 100g</span><span class="c-oline__amt">195.000 ₫</span><span class="c-oline__calc">3 × 65.000 ₫ · lô MKV-0921</span>\n          {stepper("muối kiến vàng", 3)}</li>'
         '</ul>')


def common(s):
    s = s.replace('<span>Ca sáng · từ 07:00 · Phúc</span>', '<span>Ca sáng · từ 07:00 · Hạnh</span>')
    s = s.replace('<button class="c-btn r-pos__desk" type="button">Đóng ca</button>', '<a class="c-btn r-pos__desk" href="shift-close.html">Đóng ca</a>')
    s = re.sub(r'<div class="c-filters" role="toolbar" aria-label="Nhóm hàng">[\s\S]*?</div>', KNOWN, s, count=1)
    s = re.sub(r'<div class="c-tiles">[\s\S]*?</div>\n      <div class="r-pos__keys"', TILES + '\n      <div class="r-pos__keys"', s, count=1)
    s = s.replace('DH-1043', 'DH-2053').replace('DH1043', 'DH2053').replace('1.020.000', '715.000')
    s = s.replace('4 món · tại quầy', '2 món · tại quầy').replace('4 món · Khách lẻ', '2 món · Khách lẻ').replace('DH-2053 · 4 món · xem giỏ', 'DH-2053 · 2 món · xem giỏ')
    s = s.replace('bạn đặt', 'chị An đặt')
    s = s.replace('Hoá đơn máy tính tiền tự phát hành sau khi thu · không có dòng thuế GTGT', 'Bấm Thu tiền = phát hành hoá đơn máy tính tiền (Hilo)')
    s = s.replace('Hoá đơn máy tính tiền tự phát hành sau khi thu · Hilo hoạt động', 'Bấm Thu tiền = phát hành hoá đơn máy tính tiền (Hilo)')
    return s


a = (HERE / 'src/counter.html').read_text()
a = common(a)
a = re.sub(r'<ul class="r-order__lines">[\s\S]*?</ul>', LINES, a, count=1)
a = a.replace('<a class="r-cartbar" href="#">', '<a class="r-cartbar" href="counter--cart.html">')
(HERE / 'src_v43/counter.html').write_text(strip_quiet_icons(a))
b = common((HERE / 'src/counter--qr.html').read_text())
b = _re.sub(r'\s*<p class="c-note">.*?</p>', '', b, count=1, flags=_re.S)   # v4.5.3: the 'giao được' rule is said once, when money arrives
(HERE / 'src_v43/counter--qr.html').write_text(strip_quiet_icons(b))
left = [w for w in ['Mực', 'Cá ', 'Chả cá', 'Bánh tráng', 'Phúc', 'Quy Nhơn', '1.020'] if w in a or w in b]
print('src_v43 ok', 'LEFT ' + ','.join(left) if left else '')

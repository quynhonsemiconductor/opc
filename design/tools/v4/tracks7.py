"""v7.6.0 · sales-order lists show the v7 tracks (BA: Đơn · Giao · Hoá đơn · Tiền are independent) instead of the old
Thanh toán · Trạng thái · Hoá đơn columns. Rewrites the table head and every order row on orders*.html (list + its states).
One row of data per order; states follow system/maps/status.json. Runs after inert, before facts7.  Usage: python3 tracks7.py"""
import re
from pages import SCREENS, ic
from onboard_lib import sprite

ICON = {'ok': 'i-check', 'pass': 'i-check', 'pend': 'i-clock', 'wait': 'i-clock', 'you': 'i-alert', 'err': 'i-x', 'unk': 'i-help'}
S = lambda k, t: f'<span class="c-sign c-sign--{k}"><span class="c-sign__pic">{ic(ICON[k])}</span>{t}</span>'
# order: (Giao, Hoá đơn, Tiền, which one the phone shows)
T = {
    'DH-2053': (('ok', 'Tại chỗ'), ('pass', 'Không lấy'), ('wait', 'Chờ chuyển QR'), 2),
    'DH-2052': (('wait', 'Giao trước 15:00'), ('wait', 'Lập khi giao'), ('wait', 'Trả sau 15 ngày'), 0),
    'DH-2051': (('wait', 'Đang giao'), ('wait', 'Lập khi giao'), ('wait', 'Thu hộ khi giao'), 0),
    'DH-2049': (('ok', 'Đã giao'), ('ok', '00000231'), ('ok', 'Đã thu QR'), 2),
    'DH-2048': (('ok', 'Tại chỗ'), ('ok', '00001288'), ('ok', 'Đã thu QR'), 2),
    'DH-2047': (('ok', 'Đã giao'), ('unk', 'Chưa rõ kết quả'), ('wait', 'Trả sau 7 ngày'), 1),
    'DH-2046': (('ok', 'Đã giao'), ('ok', '00001281'), ('wait', 'Chờ đơn vị giao'), 2),
    'DH-2045': (('ok', 'Đã giao'), ('ok', '00000230'), ('pend', 'Chờ xác minh'), 2),
    'DH-2044': (('ok', 'Đã giao'), ('ok', '00000228'), ('wait', 'Hạn 12/10'), 2),
    'DH-2041': (('ok', 'Đã giao'), ('ok', '00000226'), ('you', 'Chờ gán'), 2),
}
OLD_HEAD = '<th>Khách · đơn</th><th>Thanh toán</th><th>Trạng thái</th><th class="c-table__cell--opt">Hoá đơn</th><th class="c-table__num">Tổng</th>'
NEW_HEAD = '<th>Khách · đơn</th><th>Giao</th><th class="c-table__cell--opt">Hoá đơn</th><th>Tiền</th><th class="c-table__num">Tổng</th>'
ROW = re.compile(r'(<tr[^>]*>(?:(?!</tr>).)*?<small>(DH-\d+)[^<]*</small>.*?</td>)'      # who cell (+ optional check cell before it)
                 r'<td class="c-table__cell--hide">.*?</td><td class="c-table__cell--wide">.*?</td><td class="c-table__cell--hide c-table__cell--opt">.*?</td>'
                 r'(<td class="c-table__num c-table__cell--end">)', re.S)


def cells(m):
    head, code, tail = m.groups()
    if code not in T:
        return m.group(0)
    g, h, t, ph = T[code]
    trio = (g, h, t)
    return (head + f'<td class="c-table__cell--hide">{S(*g)}</td><td class="c-table__cell--hide c-table__cell--opt">{S(*h)}</td>'
            f'<td class="c-table__cell--hide">{S(*t)}</td><td class="c-table__cell--wide r-phone-only">{S(*trio[ph])}</td>' + tail)


n = 0
for f in sorted(SCREENS.glob('orders*.html')):
    s = o = f.read_text()
    s = s.replace(OLD_HEAD, NEW_HEAD)
    s = ROW.sub(cells, s)
    if s != o:
        f.write_text(sprite(s)); n += 1
print(f'tracks7: {n} screens')

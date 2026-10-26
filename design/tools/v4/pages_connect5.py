"""v5.1.0 · Kết nối, features first.  Usage: python3 pages_connect5.py — after pages_connect4.py.
  connections--category   "Việc OPC làm": the 11 things OPC does, by tier (Cần để bắt đầu / Nên có / Khi cần), the way in use, its state; overwrites the old 17-category table
  connections--feature    one feature (Nhận tiền chuyển khoản): ways in use + add another way + what happens with none
A provider is a way to do a feature. Tiers come from the business model (capabilities.py)."""
from connect_lib import *
from capabilities import FEATS, FBY, TIERS, BY, selectable

HREF = {'receive': 'connections--feature.html', 'invoice': 'connections--detail.html', 'buyin': 'connections--provider.html', 'ship': 'connections--delivery.html',
        'chat': 'connections--account.html', 'notify': 'connections--account.html', 'identity': '', 'sign': '', 'shop': '', 'tax': '', 'books': ''}
ST = {'ok': sign('pass', 'i-check', 'Hoạt động'), 'err': sign('err', 'i-x', 'Lỗi'), 'wait': sign('wait', 'i-clock', 'Chờ'), 'none': 'Làm tay'}
ACT = {'ok': 'Xem', 'err': 'Xem', 'wait': 'Xem', 'none': 'Chọn cách'}


def frow(f):
    h = HREF.get(f['id'], '')
    cls = ' r-feat__i--err' if f['demo'] == 'err' else ''
    act = f'<a class="c-btn{" c-btn--quiet" if f["demo"] != "none" else ""}" href="{h}">{ACT[f["demo"]]}</a>' if h else ''
    return (f'<li class="r-feat__i{cls}"><span class="r-feat__b"><b>{f["name"]}</b><small>{f["what"]}</small></span>'
            f'<span class="r-feat__way">{ST[f["demo"]]}<small>{f["way"]}</small></span><span class="r-feat__act">{act}</span></li>')


def tier(key, title):
    fs = [f for f in FEATS if f['tier'] == key]
    return (f'<section class="c-card" aria-labelledby="t-{key}"><div class="c-card__head"><h2 class="c-card__title" id="t-{key}">{title} · {len(fs)}</h2></div>'
            f'<ul class="r-feat">' + ''.join(frow(f) for f in fs) + '</ul></section>')


n_ok = sum(f['demo'] == 'ok' for f in FEATS)
HUB = (head('Việc OPC làm', f'{len(FEATS)} việc · {n_ok} chạy tốt · {sum(f["demo"] == "err" for f in FEATS)} lỗi · {sum(f["demo"] == "wait" for f in FEATS)} chờ · {sum(f["demo"] == "none" for f in FEATS)} đang làm tay', '<a class="c-btn" href="connections--add.html">Thêm cách nối</a>')
       + '<div class="page">' + tabs('Theo nhóm việc') + '<div class="stack">' + ''.join(tier(k, t) for k, t in TIERS) + '</div></div>')
save('connections--category', 'Kết nối · Việc OPC làm', HUB)

# ------------------------------------------------------------------ one feature (Nhận tiền chuyển khoản)
F = FBY['receive']
INUSE = ('<ul class="r-gate">' + row('ok', 'Hoạt động', 'MB qua Casso', 'cập nhật 2 phút trước · đồng ý đến 28/12', '<a class="c-btn c-btn--quiet" href="connections--account.html">Xem</a>')
         + row('ok', 'Hoạt động', 'payOS', 'tiền về cuối 09:48', '<a class="c-btn c-btn--quiet" href="connections--manage.html">Xem</a>') + '</ul>')
soon = [p for p in F['choices'] if not selectable(p) and p not in ('mb', 'payos')]
PILLS = '<ul class="r-dir__pills">' + ''.join(f'<li><button class="r-dir__pill" type="button" aria-label="Báo tôi khi có {BY[p]["name"]}">{BY[p]["name"]}</button></li>' for p in soon) + '</ul>'
FEAT = (crumb(('Kết nối', 'connections.html'), ('Việc OPC làm', 'connections--category.html'), F['name'])
        + dhead(F['name'], sign('pass', 'i-check', 'Hoạt động'), 'Cần để bắt đầu · ' + F['what'], '<a class="c-btn" href="connections--add.html">Thêm cách nối</a>')
        + grid(card('iu', 'Đang dùng', INUSE)
               + card('jb', 'OPC làm gì với việc này', '<dl class="c-kv"><dt>Đọc</dt><dd>tiền vào tài khoản, chỉ đọc</dd><dt>Làm</dt><dd>tạo QR cho từng đơn khi anh Khoa bấm</dd><dt>Khớp</dt><dd>tiền về với đơn, chờ người duyệt trước khi ghi</dd><dt>Không làm</dt><dd>chuyển tiền đi</dd></dl>')
               + card('ad', 'Thêm một cách nữa', '<p class="c-sub">Nhiều tài khoản cùng nhận tiền được · tất cả về một sổ.</p>' + PILLS),
               '<aside class="r-tower__detail" aria-labelledby="nn"><h2 class="r-tower__t" id="nn">Nếu không có cách nào</h2><ul class="r-gate">'
               + row('wait', '', 'Chưa nhận được tiền chuyển khoản', 'vẫn bán tiền mặt ở quầy') + row('ok', '', 'Nhờ nhân viên OPC nối giúp', 'chị Thu hẹn giờ') + '</ul></aside>'))
save('connections--feature', 'Kết nối · Nhận tiền chuyển khoản', '<div class="page">' + FEAT + '</div>')
print('connect5: hub + feature')

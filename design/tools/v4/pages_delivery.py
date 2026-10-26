"""v4.2 · Bán → Giao hàng (BA UI-12, FLOWS.md ②b steps 9–13, SCOPE §7 #14–15). BA demo data (An Nhiên).
Pattern: board (shipments move through 4 stages and the household moves them; phone = one stage at a time).
Writes delivery.html (board), delivery--pick.html (picking DH-2052 → hand-over), delivery--courier.html (the link
anh Hùng opens on his phone — no account, no app shell). Usage: python3 pages_delivery.py"""
import re, json
from pages import build, ic, sign, subnav, annhien, SCREENS, ICONS


def sub(cur='Giao hàng'):
    return subnav('Bán', [('Yêu cầu', 'sales-inbox.html'), ('Đơn hàng', 'orders.html'), ('Giao hàng', 'delivery.html'), ('Khách hàng', 'customers.html')], cur)


METHOD = {'staff': ('i-people', 'Nhân viên'), 'pickup': ('i-bag', 'Khách tự lấy'), 'bus': ('i-transfer', 'Gửi nhà xe'),
          'carrier': ('i-link', 'Đơn vị vận chuyển')}


def card(code, who, lines, when, method, by, extra='', state=None, act=None, raise_=False):
    i, m = METHOD[method]
    st = f'<span class="r-board__meta">{state}</span>' if state else ''
    a = f'<span class="r-board__acts">{act}</span>' if act else ''
    return (f'<li><article class="r-board__card{" r-board__card--you" if raise_ else ""}" aria-labelledby="c-{code}"><span class="r-board__meta"><b>{code}</b><span>{when}</span></span>'
            f'<h3 class="r-board__t" id="c-{code}">{who}</h3><span class="r-board__lines">{lines}</span>'
            f'<span class="r-board__how">{m}{(" · " + by) if by else ""}</span>{extra}{st}{a}</article></li>')


def col(name, n, cards, empty='', sub=''):
    body = ''.join(cards) if cards else f'<li class="r-board__empty">{empty}</li>'
    return (f'<section class="r-board__col" aria-labelledby="h-{name}"><h2 class="r-board__head" id="h-{name}">{name}'
            f' <span class="r-board__count">{n}</span>{("<span class=\"r-board__sum\">" + sub + "</span>") if sub else ""}</h2><ul class="r-board__list">{body}</ul></section>')


COD = lambda t: f'<span class="r-board__cod">{ic("i-cash")}Thu hộ {t}</span>'
COLS = [
    col('Chờ soạn', 2, sub='không thu hộ', cards=[
        card('DH-2052', 'Sunrise Hotel', '20 gói bò · 30 hũ muối', '<b class="r-board__due">Gấp · trước 15:00</b>', 'staff', 'anh Hùng',
             act='<a class="c-btn c-btn--act" href="delivery--pick.html">Soạn hàng</a>'),
        card('DH-2055', 'Quán Gió Núi', '10 gói bò · 7 hũ muối', 'chiều Thứ Tư', 'pickup', '',
             act='<a class="c-btn c-btn--quiet" href="delivery--pick.html">Soạn</a>')]),
    col('Đã soạn', 1, sub='thu hộ 1.300.000 ₫', cards=[
        card('DH-2043', 'Chị Thảo (Quy Nhơn)', '5 gói bò', 'xe 16:30 hôm nay', 'bus', 'nhà xe Đức Long', COD('1.300.000 ₫'),
             act='<a class="c-btn c-btn--quiet" href="#">Bàn giao</a>')]),
    col('Đang giao', 3, sub='thu hộ 1.150.000 ₫', cards=[
        card('DH-2042', 'Homestay Mây Ngàn', '6 hũ muối', 'giao lúc 09:40', 'staff', 'anh Hùng',
             state=sign('err', 'i-alert', 'Không giao được · khách đóng cửa'),
             act='<a class="c-btn" href="#">Giao lại</a><a class="c-btn c-btn--quiet" href="#">Hoàn về kho</a>', raise_=True),
        card('DH-2051', 'Nhà hàng Phố Núi', '4 gói bò · 2 hũ muối', 'đi lúc 10:20', 'staff', 'anh Hùng', COD('1.150.000 ₫'),
             state=sign('wait', 'i-clock', 'Đang giao · 20 phút')),
        card('DH-2050', 'Anh Nam (đặt qua Facebook)', '2 gói bò · 1 hũ muối', 'hẹn mai', 'carrier', 'GHTK · S2210478',
             state=sign('wait', 'i-clock', 'GHTK: đang trung chuyển') + '<span class="c-sim">Mô phỏng</span>')]),
    col('Đã giao hôm nay', 3, sub='thu 4.745.000 ₫', cards=[
        card('DH-2049', 'Sunrise Hotel', '15 gói bò · 20 hũ muối', '08:30', 'staff', 'anh Hùng', state=sign('ok', 'i-check', 'Chị Mai nhận · đã trả QR')),
        card('DH-2048', 'Khách lẻ', '3 hũ muối', '09:05', 'pickup', '', state=sign('ok', 'i-check', 'Đã lấy')),
        card('DH-2046', 'Chị Hoa (Zalo OA)', '1 gói bò', '10:02', 'carrier', 'GHTK', state=sign('ok', 'i-check', 'GHTK: đã giao') + '<span class="c-sim">Mô phỏng</span>')]),
]
TABS = ('<div class="r-board__tabs c-tabs" role="tablist" aria-label="Chặng giao hàng">'
        + ''.join(f'<button class="c-tabs__tab" role="tab" aria-selected="{"true" if i == 0 else "false"}" type="button">{n} <span class="c-tabs__count">{c}</span></button>'
                  for i, (n, c) in enumerate([('Chờ soạn', 2), ('Đã soạn', 1), ('Đang giao', 3), ('Đã giao', 3)])) + '</div>')

ALERT = ('<div class="c-banner c-banner--err r-mob-only" role="status"><span class="c-banner__pic">' + ic('i-x') + '</span><span class="c-banner__text">'
         '<strong class="c-banner__title">DH-2042 không giao được</strong><span>Homestay Mây Ngàn đóng cửa · 6 hũ muối vẫn đang giữ</span></span>'
         '<a class="c-btn" href="delivery--pick.html">Giao lại</a></div>')   # v7.7: phone shows one stage at a time, so the exception goes on top
main = (f'\n      {sub()}\n      <div class="r-page-head"><div><h1 class="r-page-head__title">Giao hàng hôm nay</h1>'
        '<p class="c-sub">Thứ Ba 06/10/2026 · 9 đơn · 1 đơn gấp · 1 đơn không giao được</p></div>'
        '<div class="r-page-head__acts"><button class="c-btn" type="button">Hôm nay</button></div></div>\n'
        f'      <div class="page">{ALERT}{TABS}<div class="r-board" aria-label="Bảng giao hàng">{"".join(COLS)}</div></div>')
build('delivery', 'Bán · Giao hàng hôm nay', main, 'orders')
annhien(SCREENS / 'delivery.html')

# ---------- picking DH-2052 → hand-over ----------
def pickline(name, qty, lot, done, of):
    ok = done == of
    return (f'<li class="r-pick__l"><span class="r-pick__chk{" r-pick__chk--ok" if ok else ""}" aria-hidden="true">{ic("i-check") if ok else ""}</span>'
            f'<span class="r-pick__name"><b>{name}</b><small>{lot}</small></span>'
            f'<span class="r-pick__qty"><b>{done}</b>/{of} {qty}<span class="u-sr">{" — đủ" if ok else " — còn thiếu"}</span></span></li>')


PICK = (f'\n      {sub()}\n      <div class="page">\n        <nav class="c-crumbs" aria-label="Đường dẫn"><a href="delivery.html">Giao hàng</a><span aria-current="page">Soạn DH-2052</span></nav>'
        '<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">Soạn DH-2052 · Sunrise Hotel</h1>'
        '<p class="r-detail__fig"><span class="c-sub">Giao trước 15:00 · cổng bếp · đã giữ từ 09:15</span></p></div></div>'
        '<div class="r-detail__grid r-detail--calm"><div class="stack">'
        '<section class="c-card" aria-labelledby="pk"><div class="c-card__head"><h2 class="c-card__title" id="pk">Lấy hàng · 1/2 món xong</h2></div>'
        '<ul class="r-pick">' + pickline('Bò một nắng 500g', 'gói', 'kệ lạnh · hạn gần nhất 15/11, lấy trước', 20, 20) + pickline('Muối kiến vàng 100g', 'hũ', 'kệ khô · hạn 09/2027', 18, 30) + '</ul>'
        '<p class="c-sub">Còn 12 hũ muối chưa soạn.</p></section>'
        '<section class="c-card" aria-labelledby="hv"><div class="c-card__head"><h2 class="c-card__title" id="hv">Bàn giao</h2></div>'
        '<dl class="c-kv"><dt>Cách giao</dt><dd>Nhân viên của hộ <a href="connections--delivery.html">đổi</a></dd><dt>Người giao</dt><dd>Anh Hùng · nhận link qua Zalo</dd>'
        '<dt>Thu hộ</dt><dd>Không — khách trả theo công nợ</dd></dl>'
        '<div class="c-decide__acts"><button class="c-btn c-btn--act" type="button" aria-disabled="true">' + ic('i-lock') + 'Bàn giao cho anh Hùng</button>'
        '<a class="c-btn" href="order-detail--split.html">Giao thiếu · 18 hũ</a></div>'
        '<p class="c-decide__who">Mở khi soạn đủ 30 hũ. Giao thiếu = đơn sửa còn 18 hũ, 12 hũ thành đơn mới. Kho <b>trừ một lần</b> khi anh Hùng báo đã giao.</p></section>'
        '</div><aside class="r-tower__detail" aria-labelledby="tl"><h2 class="r-tower__t" id="tl">Đã giữ cho đơn này</h2>'
        '<dl class="c-kv"><dt>Đang giữ</dt><dd>20 gói bò · 30 hũ muối cho DH-2052</dd><dt>Trừ kho</dt><dd>một lần, khi chị bấm Đã giao đủ</dd></dl>'
        '</aside></div></div>')
build('delivery--pick', 'Giao hàng · Soạn DH-2052', PICK, 'orders')
annhien(SCREENS / 'delivery--pick.html')

# ---------- the deliverer's link (no account, no app shell) ----------
tpl = (SCREENS / '_onboard-template.html').read_text()
head = tpl[:tpl.index('<body')]
head = re.sub(r'<title>.*?</title>', '<title>Giao DH-2051 · Đặc sản An Nhiên</title>', head)
used = ['i-phone', 'i-link', 'i-cash', 'i-qr', 'i-camera', 'i-check', 'i-alert', 'i-arrow', 'i-help']
sprite = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">\n'
          + '\n'.join(f'  <symbol id="{u}" viewBox="0 0 24 24">{ICONS[u]}</symbol>' for u in used) + '\n</svg>')
COURIER = f'''<body data-density="touch">
{sprite}
<div class="r-onboard">
  <header class="r-onboard__top">
    <span class="c-hh__mark" aria-hidden="true">AN</span>
    <div><b>Đặc sản An Nhiên</b><span class="c-sub"> · link giao hàng cho anh Hùng</span></div>
    <a class="r-onboard__help" href="tel:0905000111">{ic('i-help')}Gọi chị An</a>
  </header>
  <main class="r-onboard__body">
    <p class="c-sub">Giao DH-2051 · đi lúc 10:20</p>
    <h1 class="r-onboard__title">Nhà hàng Phố Núi</h1>
    <dl class="c-kv"><dt>Địa chỉ</dt><dd>45 Phạm Văn Đồng, Pleiku · gặp anh Tâm (quản lý)</dd>
      <dt>Hàng</dt><dd>4 gói bò một nắng · 2 hũ muối kiến vàng</dd></dl>
    <div class="c-decide__acts"><a class="c-btn" href="tel:0905000222">{ic('i-phone')}Gọi khách</a><a class="c-btn" href="#">{ic('i-link')}Chỉ đường</a></div>
    <section class="c-decide" aria-labelledby="cod"><p class="c-decide__q" id="cod">Thu hộ</p><p class="r-courier__cod">1.150.000 ₫</p>
      <div class="c-seg" role="radiogroup" aria-label="Khách trả bằng"><button class="c-seg__opt" type="button" role="radio" aria-checked="true">{ic('i-cash')}Tiền mặt</button><button class="c-seg__opt" type="button" role="radio" aria-checked="false">{ic('i-qr')}QR của hộ</button></div>
      <p class="c-decide__who">Thu tiền mặt, cuối ngày nộp lại cho chị An — OPC đối chiếu như đóng ca.</p></section>
    <section class="c-decide" aria-labelledby="pf"><p class="c-decide__q" id="pf">Bằng chứng đã giao <span class="u-meta">(cần ảnh hoặc tên người nhận)</span></p>
      <button class="c-btn c-btn--block" type="button">{ic('i-camera')}Chụp ảnh hàng đã giao</button>
      <p class="r-courier__or" aria-hidden="true">hoặc</p>
      <label class="c-field"><span class="c-field__label">Tên người nhận</span><span class="c-field__control"><input class="c-field__input" placeholder="Ví dụ: anh Tâm"></span></label></section>
  </main>
  <footer class="r-onboard__foot">
    <button class="c-btn c-btn--act c-btn--block" type="button" aria-disabled="true">{ic('i-check')}Đã giao xong · cần ảnh hoặc tên người nhận</button>
    <p class="r-courier__issue">Có vấn đề? <a href="#">Giao một phần</a> · <a href="#">Không giao được</a></p>
  </footer>
</div>
</body>
</html>
'''
(SCREENS / 'delivery--courier.html').write_text(head + COURIER)
print('delivery: 3 screens')

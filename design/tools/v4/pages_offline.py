"""v4.2 · Offline pattern (FLOWS §0 principle 8) on picking DH-2052, + demo Scenario Switcher (BA UC-06 / demo scope).
Writes delivery--pick--offline.html, delivery--pick--queue.html (drawer), delivery--pick--back.html (reconnect with a
conflict: the order was edited while offline), demo.html + demo--reset.html (demo console, not part of the product).
Usage: python3 pages_offline.py  (run after pages_delivery.py)"""
import re
from pages import build, ic, sign, subnav, annhien, SCREENS


def sub():
    return subnav('Bán', [('Yêu cầu', 'sales-inbox.html'), ('Đơn hàng', 'orders.html'), ('Giao hàng', 'delivery.html'), ('Khách hàng', 'customers.html')], 'Giao hàng')


def finish(name, clock, chip):
    p = SCREENS / f'{name}.html'
    annhien(p)
    s = p.read_text()
    s = re.sub(r'<span class="c-health r-shell__desk"[^>]*>[\s\S]*?</span>', chip.replace('{clock}', clock), s, count=1)
    p.write_text(s)


OFF_CHIP = '<span class="c-health c-health--off r-shell__desk" role="status" tabindex="0" data-tip="Không có mạng từ 10:51 · lưu trên máy 10:58 · 2 việc chờ gửi">Mất mạng · <b>2 việc chờ</b></span>'
ON_CHIP = '<span class="c-health r-shell__desk" role="status" tabindex="0" data-tip="Có mạng lại lúc 11:04 · đã gửi 1 việc · 1 việc dừng chờ chị xem">Đã có mạng · <b>{clock}</b></span>'


def pickline(name, unit, lot, done, of, note=None, err=False):
    ok = done == of and not err
    mark = (f'<span class="r-pick__chk r-pick__chk--ok" aria-hidden="true">{ic("i-check")}</span>' if ok else
            f'<span class="r-pick__chk r-pick__chk--err" aria-hidden="true">{ic("i-x")}</span>' if err else '<span class="r-pick__chk" aria-hidden="true"></span>')
    n = note or f'hạn gần nhất {lot}'
    return (f'<li class="r-pick__l{" r-pick__l--err" if err else ""}">{mark}<span class="r-pick__name"><b>{name}</b><small>{n}</small></span>'
            f'<span class="r-pick__qty"><b>{done}</b>/{of} {unit}<span class="u-sr">{" — lỗi" if err else " — đủ" if ok else ""}</span></span></li>')


def page(name, title_state, banner, lines, handover, aside, overlay=None):
    m = (f'\n      {sub()}\n      <div class="page">{banner}<nav class="c-crumbs" aria-label="Đường dẫn"><a href="delivery.html">Giao hàng</a><span aria-current="page">Soạn DH-2052</span></nav>'
         '<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">Soạn DH-2052 · Sunrise Hotel ' + title_state + '</h1>'
         '<p class="r-detail__fig"><span class="c-sub">Giao trước 15:00 · cổng bếp · đã giữ từ 09:15</span></p></div></div>'
         '<div class="r-detail__grid r-detail--calm"><div class="stack">'
         f'<section class="c-card" aria-labelledby="pk"><div class="c-card__head"><h2 class="c-card__title" id="pk">Lấy hàng</h2></div><ul class="r-pick">{lines}</ul></section>'
         f'<section class="c-card" aria-labelledby="hv"><div class="c-card__head"><h2 class="c-card__title" id="hv">Bàn giao</h2></div>{handover}</section></div>'
         f'<aside class="r-tower__detail" aria-labelledby="dv">{aside}</aside></div></div>')
    build(name, 'Giao hàng · Soạn DH-2052', m, 'orders', overlay=overlay)


OFF_BANNER = ('<div class="c-banner r-offbar" role="status"><span class="c-banner__pic">' + ic('i-offline') + '</span><span class="c-banner__text">'
              '<strong class="c-banner__title">Không có mạng từ 10:51 — vẫn làm tiếp được</strong>'
              '<span>Mọi thao tác lưu trên máy này. Việc cần gửi đi xếp hàng chờ, gửi theo thứ tự khi có mạng, không gửi trùng.</span></span>'
              '<a class="c-btn" href="delivery--pick--queue.html">Xem 2 việc chờ</a></div>')
LINES_OFF = (pickline('Bò một nắng 500g', 'gói', '15/11', 20, 20) + pickline('Muối kiến vàng 100g', 'hũ', '09/2027', 30, 30))
HAND_OFF = ('<dl class="c-kv"><dt>Người giao</dt><dd>Anh Hùng · nhận link qua Zalo</dd><dt>Thu hộ</dt><dd>Không — khách trả theo công nợ</dd></dl>'
            '<p class="r-qchip">' + ic('i-clock') + '<span><b>Soạn xong</b> · đã ghi trên máy 10:56 · <b>chờ gửi</b></span></p>'
            f'<div class="c-decide__acts"><button class="c-btn c-btn--act" type="button" aria-disabled="true">{ic("i-lock")}Bàn giao · cần mạng để trừ kho đúng một lần</button></div>'
            '<p class="c-decide__who">Đã giao phải có mạng: OPC kiểm tra đơn và giữ hàng trên máy chủ rồi mới trừ kho, để hai máy không trừ hai lần.</p>')
ASIDE_OFF = ('<h2 class="r-tower__t" id="dv">Trên máy này</h2><dl class="c-kv"><dt>Lưu lần cuối</dt><dd>10:58</dd><dt>Dữ liệu tới</dt><dd>10:51 — số tồn, giữ hàng có thể đã đổi</dd>'
             '<dt>Chờ gửi</dt><dd>2 việc</dd></dl>'
             '<ul class="r-offrules" aria-label="Khi mất mạng">'
             f'<li>{ic("i-check")}<span><b>Làm được:</b> soạn, đếm, kiểm kê, bán tiền mặt ở quầy</span></li>'
             f'<li>{ic("i-clock")}<span><b>Xếp hàng chờ:</b> soạn xong, tin nhắn, ảnh chứng từ</span></li>'
             f'<li>{ic("i-lock")}<span><b>Cần mạng:</b> bàn giao, QR, hoá đơn có mã, duyệt, chuyển tiền</span></li></ul>')
page('delivery--pick--offline', sign('wait', 'i-clock', 'Soạn xong · chờ gửi'), OFF_BANNER, LINES_OFF, HAND_OFF, ASIDE_OFF)
finish('delivery--pick--offline', '10:58', OFF_CHIP)


def qitem(n, t, m, when, can=True):
    c = '<button class="c-btn c-btn--quiet" type="button">Huỷ</button>' if can else ''
    return (f'<li class="r-queue__i"><span class="r-queue__n">{n}</span><span class="r-queue__b"><b>{t}</b><small>{m}</small></span>'
            f'<span class="r-queue__t">{when}</span><span class="r-queue__a">{c}</span></li>')


QUEUE = ('<div class="c-drawer"><div class="c-drawer__panel" role="dialog" aria-modal="true" aria-labelledby="q-t">'
         f'<div class="c-drawer__head"><div><span class="c-drawer__k">Không có mạng từ 10:51</span><h2 class="c-drawer__title" id="q-t" tabindex="-1">2 việc chờ gửi</h2></div>'
         f'<a class="c-icon-btn" href="delivery--pick--offline.html" aria-label="Đóng">{ic("i-x")}</a></div>'
         '<div class="c-drawer__body"><ol class="r-queue" aria-label="Thứ tự gửi">'
         + qitem(1, 'Soạn xong DH-2052', '20 gói bò · 30 hũ muối · anh Khoa', '10:56')
         + qitem(2, 'Tin Zalo cho chị Mai', '“Hàng đã soạn xong, giao khoảng 14:00” · Trợ lý soạn, anh Khoa duyệt · gửi sau việc 1', '10:57')
         + '</ol><p class="r-trust r-trust--gate">' + ic('i-shield') + '<span><b>Gửi theo thứ tự, không gửi trùng.</b> Mỗi việc mang một mã riêng; OPC kiểm tra lại từng việc khi có mạng. '
         'Việc nào cần chị quyết thì dừng ở đó, việc sau chờ — không tự làm tiếp.</span></p></div>'
         f'<div class="c-drawer__foot"><button class="c-btn c-btn--act" type="button">{ic("i-offline")}Thử kết nối lại</button></div></div></div>')
page('delivery--pick--queue', sign('wait', 'i-clock', 'Soạn xong · chờ gửi'), OFF_BANNER, LINES_OFF, HAND_OFF, ASIDE_OFF, overlay=QUEUE)
finish('delivery--pick--queue', '10:58', OFF_CHIP)

BACK_BANNER = ('<div class="c-banner c-banner--err" role="alert"><span class="c-banner__pic">' + ic('i-alert') + '</span><span class="c-banner__text">'
               '<strong class="c-banner__title">Có mạng lại lúc 11:04 · 1 việc dừng chờ anh xem</strong>'
               '<span>Trong lúc mất mạng, chị An sửa DH-2052 còn 10 gói bò (10:52). OPC nhận phần muối; phần bò soạn lại theo đơn mới; tin Zalo cho chị Mai đang giữ lại.</span></span></div>')
LINES_BACK = (pickline('Bò một nắng 500g', 'gói', '15/11', 0, 10, '<b class="r-pick__why">Đơn đã sửa còn 10 gói</b> · 20 gói vừa lấy, trả 10 gói về kệ', err=True)
              + pickline('Muối kiến vàng 100g', 'hũ', '09/2027', 30, 30, 'OPC đã nhận 11:04'))
HAND_BACK = ('<dl class="c-kv"><dt>Người giao</dt><dd>Anh Hùng · nhận link qua Zalo</dd></dl>'
             '<p class="c-decide__result">Soạn lại 10 gói theo đơn mới → Đã giao · tin Zalo chị gửi sau khi giao</p>'
             f'<div class="c-decide__acts"><a class="c-btn c-btn--act" href="#">Đã soạn lại 10 gói</a><a class="c-btn" href="order-detail.html">Xem đơn đã sửa</a></div>')
ASIDE_BACK = ('<h2 class="r-tower__t" id="dv">Kết quả gửi lúc 11:04</h2><ol class="r-queue r-queue--done" aria-label="Kết quả từng việc">'
              + qitem(sign('pass', 'i-check', 'Đã nhận'), 'Soạn xong · phần muối', '30 hũ', '11:04', can=False)
              + qitem(sign('err', 'i-x', 'Dừng'), 'Soạn xong · phần bò', 'đơn sửa lúc 10:52', '11:04', can=False)
              + qitem(sign('pend', 'i-clock', 'Giữ lại'), 'Tin Zalo cho chị Mai', 'chờ việc trước xong', '—', can=False)
              + '</ol><p class="c-sub">Không trừ kho hai lần · mọi kết quả ghi Nhật ký</p>')
page('delivery--pick--back', '', BACK_BANNER, LINES_BACK, HAND_BACK, ASIDE_BACK)
finish('delivery--pick--back', '11:04', ON_CHIP)


# ---------------- demo console (not part of the product) ----------------
HEAD = (SCREENS / 'stock.html').read_text().split('<body')[0].replace('<title>Hàng hoá · Tồn kho — OPC</title>', '<title>Bảng điều khiển demo — OPC</title>')
SPR = re.search(r'<svg width="0" height="0"[\s\S]*?</svg>', (SCREENS / 'stock.html').read_text()).group(0)


def scen(t, m, href, chips):
    ch = ''.join(f'<span class="c-tag">{c}</span>' for c in chips)
    return f'<li><a class="r-demo__card" href="{href}"><b>{t}</b><span>{m}</span><span class="r-demo__chips">{ch}</span></a></li>'


PATH = [('UI-01', 'Cần xử lý', 'approvals.html'), ('UC-01', 'Sẵn sàng', 'readiness.html'), ('UC-02', 'Nhận hàng', 'purchase-detail--receive.html'),
        ('UC-03', 'Nhận đơn Zalo', 'sales-inbox.html'), ('UC-06', 'Duyệt ngoại lệ', 'approvals--detail.html'), ('UC-04a', 'Soạn, giao', 'delivery--pick.html'),
        ('UC-04b', 'Hoá đơn, tiền', 'order-detail--invoice.html'), ('UC-05', 'Đối chiếu kỳ', 'period.html'), ('UC-05', 'Thuế & bằng chứng', 'tax.html'), ('UC-07', 'Kết quả pilot', 'program.html')]
STEPS = '<ol class="r-demo__path">' + ''.join(f'<li><a{" class=" + chr(34) + "r-demo__start" + chr(34) if n == 0 else ""} href="{h}"><span class="r-demo__id">{i}{" · bắt đầu" if n == 0 else ""}</span><b>{t}</b></a></li>' for n, (i, t, h) in enumerate(PATH)) + '</ol>'
CASES = ('<ul class="r-demo__grid">'
         + scen('Khách nợ quá hạn', 'Sunrise nợ 8.400.000 ₫ quá 12 ngày · đơn mới chờ chị An duyệt', 'approvals--detail.html', ['UC-06', 'Chị An'])
         + scen('Thiếu tồn', 'Khách hỏi 30 gói bò, kho còn 26 · sửa đơn hoặc nhập thêm', 'stock.html', ['Bán', 'Chị An'])
         + scen('Hoá đơn chưa rõ kết quả', 'X Invoice không trả lời · OPC không tự gửi lại', 'approvals--error.html', ['UC-04', 'Kết nối'])
         + scen('Tiền không khớp', 'Một khoản về cho hai hoá đơn · gán tay', 'receivable-detail--assign.html', ['UC-04', 'Anh Khoa'])
         + scen('Kết nối lỗi', 'X Invoice lỗi · làm tay trên cổng nhà cung cấp', 'connections.html', ['UC-01', 'Kết nối'])
         + scen('Mất mạng', 'Soạn hàng khi mất mạng → có mạng lại, đơn đã bị sửa', 'delivery--pick--offline.html', ['Nguyên tắc 8', 'Anh Khoa'])
         + scen('Hàng cận hạn', 'Muối kiến vàng còn 30 ngày · bán trước, nhắc khi nhận hàng', 'stock.html', ['Kho', 'Chị An'])
         + scen('Kỳ thuế đủ bằng chứng', 'Quý III: khai, nộp ngoài OPC, khớp sao kê', 'tax-evidence.html', ['UC-05', 'Chị An']) + '</ul>')


def seg(label, opts, sel):
    return (f'<div class="r-demo__ctl"><span class="r-demo__lab">{label}</span><div class="c-seg" role="radiogroup" aria-label="{label}">'
            + ''.join(f'<button class="c-seg__opt" type="button" role="radio" aria-checked="{"true" if o == sel else "false"}">{o}</button>' for o in opts) + '</div></div>')


CONNS = [('Ngân hàng MB', 'Hoạt động'), ('Hilo · hoá đơn quầy', 'Hoạt động'), ('X Invoice · hoá đơn B2B', 'Không trả lời'), ('Zalo OA', 'Hoạt động'), ('Cổng thuế', 'Chưa kết nối'), ('Mạng của máy', 'Có mạng')]
CONN = '<ul class="r-demo__conns">' + ''.join(
    f'<li{" class=" + chr(34) + "r-demo__bad" + chr(34) if v in ("Không trả lời",) else ""}><span>{n}</span><button class="c-btn r-capture__pick" type="button" aria-haspopup="listbox" aria-label="{n}: {v}">{v}{ic("i-chev")}</button></li>' for n, v in CONNS) + '</ul>'


def demo(name, dialog=''):
    body = (f'<body class="r-demo">{SPR}<main class="r-demo__main" aria-labelledby="dm">'
            '<header class="r-demo__head"><span class="r-demo__badge">DEMO · không có trong sản phẩm</span>'
            '<h1 id="dm">Bảng điều khiển demo</h1><p class="c-sub">Đặc sản Cao Nguyên An Nhiên · dữ liệu mẫu của BA, design bổ sung · mọi kết nối là Mô phỏng</p>'
            f'<div class="r-demo__acts"><a class="c-btn c-btn--act" href="approvals.html">{ic("i-play")}Bắt đầu luồng demo</a>'
            f'<a class="c-btn" href="demo--reset.html">{ic("i-undo")}Đặt lại dữ liệu</a></div></header>'
            '<section class="r-demo__panel" aria-labelledby="p3"><h2 id="p3" class="r-demo__h">Đặt trước khi trình bày</h2><div class="r-demo__levers">'
            + seg('Xem với vai', ['Chị An · chủ hộ', 'Anh Khoa · vận hành', 'Hạnh · thu ngân', 'Chị Lan · kế toán', 'PM Quang · chương trình'], 'Anh Khoa · vận hành')
            + seg('Giờ demo', ['06/10 10:45', '06/10 16:05', '07/10 11:30'], '06/10 10:45')
            + '</div><div class="r-demo__ctl"><span class="r-demo__lab">Kết nối mô phỏng · X Invoice đang “không trả lời”</span>' + CONN + '</div></section>'
            '<section aria-labelledby="p1"><h2 id="p1" class="r-demo__h">Luồng xuyên suốt · 10 bước · bắt đầu ở đây</h2>' + STEPS + '</section>'
            '<section class="r-demo__sec2" aria-labelledby="p2"><h2 id="p2" class="r-demo__h">Kịch bản ngoại lệ · nhảy thẳng vào</h2>' + CASES + '</section>'
            f'</main>{dialog}</body></html>')
    (SCREENS / f'{name}.html').write_text(HEAD + body)
    print(name, 'ok')


demo('demo')
RESET = ('<div class="c-dialog" role="dialog" aria-modal="true" aria-labelledby="rs-t"><div class="c-dialog__panel">'
         '<div class="c-dialog__head"><div><span class="c-dialog__k">Chỉ dữ liệu demo</span><h2 class="c-dialog__title" id="rs-t" tabindex="-1">Đặt lại dữ liệu demo?</h2></div>'
         f'<a class="c-icon-btn" href="demo.html" aria-label="Đóng, không đặt lại">{ic("i-x")}</a></div>'
         '<div class="c-dialog__body"><p>Mọi thao tác đã làm trong buổi demo này sẽ mất; dữ liệu quay về 06/10/2026 10:45:</p>'
         '<ul class="r-lock"><li>' + ic('i-undo') + '<span>Đơn, giữ hàng, giao hàng, tiền, hoá đơn, kỳ thuế — về như bộ mẫu</span></li>'
         '<li>' + ic('i-undo') + '<span>Kết nối mô phỏng về mặc định (X Invoice không trả lời)</span></li>'
         '<li>' + ic('i-shield') + '<span>Không ảnh hưởng dữ liệu thật — bản demo không nối với hộ nào</span></li></ul></div>'
         '<div class="c-dialog__foot"><a class="c-btn" href="demo.html">Không đặt lại</a><button class="c-btn c-btn--danger" type="button">Đặt lại dữ liệu demo</button></div></div></div>')
demo('demo--reset', RESET)
print('offline + demo: 5 screens')

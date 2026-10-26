"""v4.2 · Cần xử lý = the owner's Control Tower (FLOWS.md ⑤-②, SCOPE §7 #19). BA demo data (An Nhiên).
Writes approvals.html (Cần chị quyết), approvals--running.html, approvals--error.html, approvals--detail.html (phone).
Replaces the v4.1 approvals page (pages_queue.py no longer builds it). Usage: python3 pages_control.py"""
from pages import build, ic, sign, annhien, SCREENS


TABS = [('wait', 'Cần chị quyết', 2), ('run', 'Đang chạy', 4), ('conn', 'Chờ kết nối', 1), ('err', 'Lỗi', 1), ('done', 'Xong hôm nay', 9)]


def tabs(sel):
    out = []
    for key, label, n in TABS:
        you = ' c-tabs__tab--you' if key == 'wait' else ''
        out.append(f'<button class="c-tabs__tab{you}" role="tab" aria-selected="{"true" if key == sel else "false"}" type="button">'
                   f'{label} <span class="c-tabs__count">{n}</span></button>')
    return '<div class="c-tabs" role="tablist" aria-label="Việc theo trạng thái">' + ''.join(out) + '</div>'


def work(kind, icon, state, title, meta, src, when, cur=False, href='approvals--detail.html'):
    c = ' aria-current="true"' if cur else ''
    return (f'<li><a class="c-work" href="{href}"{c}><span class="c-work__state">{sign(kind, icon, state)}</span>'
            f'<span class="c-work__when">{when}</span><span class="c-work__t">{title}</span>'
            f'<span class="c-work__m">{meta}</span><span class="c-work__src">{src}</span></a></li>')


def step(kind, src, time, what, detail='', extra=''):
    d = f'<span class="c-timeline__who">{detail}</span>' if detail else ''
    return (f'<li class="c-timeline__item c-timeline__item--{kind}"><span class="c-timeline__time">{time}</span>'
            f'<span class="c-timeline__dot" aria-hidden="true"></span><span class="c-timeline__body">'
            f'<span class="c-timeline__src">{src}</span><span class="c-timeline__what">{what}</span>{d}{extra}</span></li>')


def rules(*rs):
    out = []
    for name, ok in rs:
        out.append(f'<li class="c-rules__r{"" if ok else " c-rules__r--fail"}">{ic("i-check" if ok else "i-x")}{name}'
                   f'<span class="u-sr">{" đạt" if ok else " không đạt"}</span></li>')
    return '<ul class="c-rules" aria-label="Kết quả kiểm tra">' + ''.join(out) + '</ul>'


# ---------- detail: Sunrise order waiting for the owner ----------
DECIDE = ('<div class="c-decide" role="group" aria-labelledby="q-sun"><p class="c-decide__q" id="q-sun">Khách hỏi 30 gói bò, kho còn 26 gói bán được</p>'
          '<dl class="c-kv"><dt>Vấn đề</dt><dd>Không xác nhận vượt tồn: 20 gói đã giữ cho Sunrise Hotel</dd>'
          '<dt>Hai cách</dt><dd>Sửa đơn còn 26 gói và báo chị Hạnh, hoặc nhận MH-0121 (40 gói, Thứ Năm) rồi xác nhận đủ 30</dd>'
          '<dt>Để chị biết</dt><dd>Phố Núi đang nợ 3.900.000 ₫, hạn 12/10 · không chặn đơn</dd></dl>'
          '<div class="c-decide__acts"><button class="c-btn c-btn--act" type="button">Sửa còn 26 gói và xác nhận</button>'
          '<button class="c-btn" type="button">Chờ hàng về</button>'
          f'<button class="c-btn c-btn--quiet" type="button">{ic("i-phone")}Gọi chị Hạnh</button></div>'
          '<p class="c-decide__who">Đơn do Agent soạn luôn chờ chị duyệt · chị tự báo khách qua Zalo, Agent soạn sẵn câu trả lời</p></div>')
SUNRISE = (
    '<p class="r-tower__k">Đơn từ Zalo OA · DH-2054</p><h2 class="r-tower__t" id="d-h">Nhà hàng Phố Núi · 6.900.000 ₫</h2>'
    '<ol class="c-timeline">'
    + step('ai', 'Agent đề xuất', '09:40', 'Đọc tin của chị Hạnh (bếp Phố Núi)',
           '30 gói bò một nắng 500g · giao sáng mai · xuất hoá đơn · <a href="#">Xem tin gốc</a>')
    + step('ok', 'OPC kiểm tra', '09:40', 'Giá riêng nhà hàng · tồn khả dụng',
           'Bò còn 26 gói bán được', rules(('Khách', True), ('Giá', True), ('Tồn', False)))
    + step('now', 'Chờ chị duyệt', 'Bây giờ', 'Đơn chưa xác nhận — chưa giữ hàng, chưa báo khách', '', DECIDE)
    + step('next', 'Sau khi chị xác nhận', '', 'OPC kiểm tra lại tồn → giữ hàng → chị báo khách',
           'Kho chỉ bị trừ khi Đã giao')
    + '</ol>')

# ---------- detail: production running ----------
PROD = (
    '<p class="r-tower__k">Mua hàng · đơn mua MH-0121 · Cơ sở Krông Pa</p><h2 class="r-tower__t" id="d-h">40 gói bò một nắng 500g đang về</h2>'
    '<ol class="c-timeline">'
    + step('ok', 'Chị An', '04/10', 'Xác nhận đơn mua 40 gói · 190.000 ₫/gói', 'chưa tăng kho')
    + step('now', 'Đang chờ', 'Thứ Năm', 'Cơ sở Krông Pa giao qua nhà xe', 'Trợ lý nhắc chị khi xe tới')
    + step('next', 'Khi hàng tới', '', 'Chị đếm và xác nhận số thực nhận → OPC tăng kho đúng số đó')
    + '</ol>'
    + '<div class="c-decide__acts"><a class="c-btn" href="purchases.html">Mở đơn mua</a></div>')

# ---------- detail: invoice error, outcome unknown ----------
ERR = (
    '<p class="r-tower__k">Hoá đơn · DH-2047 · Nhà hàng Phố Núi · 1.840.000 ₫</p><h2 class="r-tower__t" id="d-h">Chưa rõ hoá đơn đã phát hành hay chưa</h2><p class="c-decide__auto">'+ic('i-clock')+'OPC không tự gửi lại · đang tự hỏi lại, lần sau 11:15</p>'
    '<ol class="c-timeline">'
    + step('ok', 'Chị An', '10:11', 'Bấm phát hành hoá đơn')
    + step('err', 'Kết nối · X Invoice', '10:12', 'Không trả lời sau 30 giây',
           'OPC <b>không tự gửi lại</b>, để tránh hai hoá đơn trùng số')
    + step('now', 'OPC đang hỏi lại', '10:45', 'Hỏi trạng thái lần 3 · lần sau lúc 11:15', 'Đã hỏi lúc 10:15 và 10:27')
    + '</ol>'
    + '<div class="c-decide" role="group" aria-labelledby="q-err"><p class="c-decide__q" id="q-err">Không muốn chờ?</p>'
      '<p class="c-sub">Mở cổng X Invoice và tìm hoá đơn của đơn DH-2047. Có rồi thì ghi số hoá đơn vào đây; chưa có thì phát hành lại từ OPC.</p>'
      '<div class="c-decide__acts"><a class="c-btn c-btn--act" href="#">Mở cổng X Invoice</a>'
      '<button class="c-btn" type="button">Ghi số hoá đơn đã có</button>'
      '<button class="c-btn c-btn--quiet" type="button" aria-disabled="true">'+ic('i-lock')+'Phát hành lại</button></div>'
      '<p class="c-decide__who">Phát hành lại chỉ mở khi chị xác nhận trên cổng chưa có hoá đơn này</p></div>')

LISTS = {
    'wait': [('you', 'i-alert', 'Cần chị quyết', 'Đơn Nhà hàng Phố Núi · 30 gói bò', 'Khách hỏi 30, kho còn 26 bán được', 'Zalo OA · Agent soạn', '09:40', True),
             ('you', 'i-alert', 'Cần chị quyết', 'Nhận hàng HTX Cao Nguyên', 'Về 45/50 hũ muối so với đơn mua MH-0118', 'Anh Khoa đếm', '08:40', False)],
    'run': [('wait', 'i-clock', 'Đang chạy', 'Đơn mua MH-0121 · 40 gói bò một nắng', 'Đang về · giao Thứ Năm qua nhà xe', 'Cơ sở Krông Pa · chị An xác nhận', '04/10', True),
            ('wait', 'i-clock', 'Đang chạy', 'Giao DH-2051 · Nhà hàng Phố Núi', 'Anh Hùng đang giao · thu hộ 1.150.000 ₫', 'Nhân viên của hộ', '10:20', False),
            ('wait', 'i-clock', 'Đang chạy', 'Trợ lý đang đọc yêu cầu mới', 'Ảnh đơn viết tay của Quán Gió Núi', 'Thêm thủ công · chị An', '10:41', False),
            ('wait', 'i-clock', 'Chờ chị', 'Bảng kê công nợ Sunrise · 8.400.000 ₫', 'Agent soạn sẵn tin nhắc · chị gửi qua Zalo', 'Công nợ', '08:00', False)],
    'err': [('err', 'i-alert', 'Lỗi', 'Hoá đơn DH-2047 · Nhà hàng Phố Núi', 'Chưa rõ đã phát hành · OPC hỏi lại lúc 11:15', 'Kết nối X Invoice', '10:12', True)],
}

HEAD = ('<div class="r-page-head"><div><h1 class="r-page-head__title">Cần xử lý</h1>'
        '<p class="c-sub">OPC đang theo dõi 17 việc</p></div></div>')


def page(name, sel, detail, title):
    items = ''.join(work(*it) for it in LISTS[sel])
    main = (f'\n      {HEAD}\n      <div class="page">\n        {tabs(sel)}\n'
            f'        <div class="r-tower r-tower--list">\n          <section aria-label="Danh sách việc"><ul class="c-works">{items}</ul></section>\n'
            f'          <section class="r-tower__detail" aria-labelledby="d-h">{detail}</section>\n        </div>\n      </div>')
    build(name, title, main, 'approvals')
    annhien(SCREENS / f'{name}.html')


page('approvals', 'wait', SUNRISE, 'Cần xử lý · Cần chị quyết')
page('approvals--running', 'run', PROD, 'Cần xử lý · Đang chạy')
page('approvals--error', 'err', ERR, 'Cần xử lý · Lỗi')

# phone: one job opened full screen
main = ('\n      <div class="page">\n        <a class="r-detail__back" href="approvals.html">Cần xử lý</a>\n'
        f'        <section class="r-tower__detail" aria-labelledby="d-h">{SUNRISE}</section>\n      </div>')
build('approvals--detail', 'Cần xử lý · Đơn Sunrise Hotel', main, 'approvals')
annhien(SCREENS / 'approvals--detail.html')
print('control tower: 4 screens')

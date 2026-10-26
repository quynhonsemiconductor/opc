"""v4.8.0 · Kết nối redesigned: provider-led front door, capability engine inside, categories as the gap-finder.
  connections            Đã nối: health strip + one card per connected ACCOUNT (jobs as chips) + "chưa có cách nối"
  connections--use       after connecting: "Dùng tài khoản này để làm gì?" (capability checklist, smart defaults)
  connections--account   one account (Zalo OA): per-job switches, consent, disconnect
  connections--disconnect  same page + confirm dialog with consequences
(connections--category = the old 17-category table, written by pages_setup.py; --detail/--provider/--consent/--testing/--unknown/--log
 are written by pages_connect.py and now hang off these.)  Usage: python3 pages_connect2.py — after pages_connect.py."""
from pages import build, ic, sign, SCREENS, annhien

OWNER = ('Nguyễn Minh Khoa · Người vận hành', 'Phạm Thị An · Chủ hộ')


SHOWN = {'Theo nhóm việc': 'Việc OPC làm'}


def tabs(sel, n=6):
    t = [('Đã nối', 'connections.html', f' <span class="c-tabs__count">{n}</span>'), ('Theo nhóm việc', 'connections--category.html', ''),
         ('Nhật ký', 'connections--log.html', '')]
    return ('<div class="c-tabs" role="tablist" aria-label="Kết nối">' + ''.join(
        f'<a class="c-tabs__tab" role="tab" aria-selected="{"true" if k == sel else "false"}" href="{h}">{SHOWN.get(k, k)}{c}</a>' for k, h, c in t) + '</div>')


def head(title, sub, acts=''):
    return (f'<div class="r-page-head"><div><h1 class="r-page-head__title">{title}</h1><p class="c-sub">{sub}</p></div>'
            f'<div class="r-page-head__acts">{acts}</div></div>')


def save(name, title, main, owner=True):
    build(name, title, '\n      ' + main, 'connections')
    p = SCREENS / f'{name}.html'
    annhien(p)
    s = p.read_text()
    if owner:
        s = s.replace(OWNER[0], OWNER[1]).replace('<span class="c-avatar__face" aria-hidden="true">K', '<span class="c-avatar__face" aria-hidden="true">A')
    p.write_text(s)


# ------------------------------------------------------------------ 1 · Đã nối
def card(mono, name, state, jobs, meta, href='connections--account.html', tone='ok'):
    chips = ''.join(f'<li class="r-acct__job r-acct__job--{t}">{j}</li>' for j, t in jobs)
    return (f'<li class="r-acct r-acct--{tone}"><a class="r-acct__a" href="{href}"><span class="r-acct__logo" aria-hidden="true">{mono}</span>'
            f'<span class="r-acct__b"><b class="r-acct__n">{name}</b><span class="r-acct__m">{meta}</span></span><span class="r-acct__st">{state}</span></a>'
            f'<ul class="r-acct__jobs" aria-label="Việc đang dùng">{chips}</ul></li>')


CARDS = ''.join([
    card('Z', 'Zalo OA · Đặc sản An Nhiên', sign('pass', 'i-check', 'Hoạt động'), [('Nhận đơn từ tin nhắn', 'on'), ('Gửi thông báo ZNS · cần mẫu duyệt', 'wait')], 'tin cuối 09:02 · đồng ý đến 04/04/2027'),
    card('M', 'MB qua Casso', sign('pass', 'i-check', 'Hoạt động'), [('Tiền về tài khoản', 'on'), ('QR thu tiền', 'on'), ('Đề nghị chuyển tiền', 'on')], 'cập nhật 2 phút trước · đồng ý đến 28/12', '#'),
    card('H', 'Hilo', sign('pass', 'i-check', 'Hoạt động'), [('Hoá đơn máy tính tiền ở quầy', 'on')], 'hoá đơn cuối 10:44', '#'),
    card('X', 'X Invoice', sign('err', 'i-x', 'Lỗi'), [('Hoá đơn có mã cho khách sỉ', 'err'), ('Chữ ký số · chờ quyết định', 'wait')], 'im lặng từ 10:12', 'connections--detail.html', 'err'),
    card('p', 'payOS', sign('pass', 'i-check', 'Hoạt động'), [('Link thanh toán cho khách xa', 'on')], 'khoá nhập 12/09 · tiền về cuối 09:48', 'connections--manage.html'),
    card('C', 'Cas ID', sign('pass', 'i-check', 'Đã xác minh'), [('Xác minh chủ hộ', 'on')], 'chị An · mức L1 · 01/07', '#'),
])
GAPS = ''.join(
    f'<li class="r-gate__i r-gate__i--{t}"><span class="r-gate__b"><b>{n}</b><small>{m}</small></span><span class="r-gate__amt"></span><span class="r-gate__act">{a}</span></li>'
    for t, n, m, a in [
        ('you', 'Hoá đơn mua vào từ cổng thuế', 'đang làm tay · chị Lan tải bảng kê', '<a class="c-btn" href="connections--provider.html">Nối Casso GDT Hub</a>'),
        ('wait', 'Chữ ký số cho tờ khai', 'chờ chương trình chọn nhà cung cấp', '<a class="c-btn c-btn--quiet" href="connections--category.html">Xem</a>'),
        ('wait', 'Gửi tờ khai', 'làm tay qua eTax · trong demo là Mô phỏng', '')])

save('connections', 'Kết nối',
     head('Kết nối', '6 tài khoản · 5 chạy tốt · 1 lỗi · 3 việc còn làm tay', '<a class="c-btn c-btn--act" href="connections--category.html">Thêm kết nối</a>')
     + '<div class="page">' + tabs('Đã nối')
     + '<ul class="r-acct__grid" aria-label="Tài khoản đã nối">' + CARDS + '</ul>'
     + '<section class="c-card" aria-labelledby="gp"><div class="c-card__head"><h2 class="c-card__title" id="gp">Chưa có cách nối · đang làm tay</h2></div>'
       f'<ul class="r-gate">{GAPS}</ul></section></div>')

# ------------------------------------------------------------------ 3 · Dùng tài khoản này để làm gì? (after connecting)
def chk(on, t, m, note=''):
    box = ic('i-check') if on else ''
    n = f'<span class="r-model__plan">{note}</span>' if note else ''
    return (f'<button class="c-option{" c-option--on" if on else ""}" type="button" role="checkbox" aria-checked="{"true" if on else "false"}">'
            f'<span class="c-option__box" aria-hidden="true">{box}</span><span class="c-option__body"><strong class="c-option__title">{t}</strong>'
            f'<span class="c-option__meta">{m}</span>{n}</span></button>')


def crumb(parent, t):
    return f'<nav class="c-crumbs" aria-label="Đường dẫn"><a href="connections.html">Kết nối</a><span aria-current="page">{t}</span></nav>'


def grid(left, right):
    return f'<div class="r-detail__grid r-detail--calm"><div class="stack">{left}</div>{right}</div>'


def rail(items):
    return f'<aside class="r-tower__detail" aria-labelledby="rl"><h2 class="r-tower__t" id="rl">Khi xong</h2><ul class="r-gate">{items}</ul></aside>'


def rrow(st, t, m):
    return f'<li class="r-gate__i r-gate__i--ok"><span class="r-gate__b"><b>{t}</b><small>{m}</small></span><span class="r-gate__amt"></span><span class="r-gate__act"></span></li>'


save('connections--use', 'Kết nối · Dùng để làm gì',
     '<div class="page">' + crumb('', 'Zalo OA')
     + '<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">Dùng Zalo OA để làm gì?</h1>'
       '<p class="r-detail__fig"><span class="c-sub">Đã nối Zalo OA Đặc sản An Nhiên · chị đổi lại được bất cứ lúc nào</span></p></div>'
       '</div>'
     + grid('<section class="c-card" aria-labelledby="uw"><div class="c-card__head"><h2 class="c-card__title" id="uw">Chọn việc</h2><span class="u-meta">OPC gợi ý theo cách chị bán</span></div><div class="c-options" role="group" aria-labelledby="uw">'
            + chk(True, 'Nhận đơn từ tin nhắn', 'OPC đọc tin khách gửi và soạn đơn cho chị duyệt', 'gợi ý: chị bán cho khách sỉ qua Zalo')
            + chk(True, 'Trả lời khách', 'Trợ lý soạn, anh Khoa bấm gửi · OPC không tự gửi')
            + chk(False, 'Gửi thông báo ZNS', 'hoá đơn, nhắc nợ tới số điện thoại khách', 'cần mẫu tin được Zalo duyệt · có phí mỗi tin · xin đồng ý riêng') + '</div>'
                   '<div class="c-decide__acts r-use__acts"><a class="c-btn c-btn--act" href="connections--account.html">Xong, bắt đầu dùng</a><a class="c-btn c-btn--quiet" href="connections.html">Để sau</a></div></section>',
            rail(rrow('ok', 'Yêu cầu từ Zalo vào Hộp yêu cầu', 'chờ chị hoặc anh Khoa xem')
                 + rrow('ok', 'Chưa có tin nào gửi đi', 'cho tới khi chị bấm gửi')
                 + rrow('ok', 'Không nối được thì sao', 'dán tin, chụp ảnh, gõ tay như trước')))
     + '</div>')

# ------------------------------------------------------------------ 4 · tài khoản (Zalo OA) + hộp xác nhận ngắt
def sw(on, t, sub, state='', lock=False):
    st = f'<span class="c-switch__state">{state}</span>' if state else ''
    return (f'<li class="c-list__row"><button class="c-switch c-switch--row" type="button" role="switch" aria-checked="{"true" if on else "false"}">'
            f'<span class="c-switch__label">{t}<span class="c-switch__sub">{sub}</span></span>{st}<span class="c-switch__track" aria-hidden="true"></span></button></li>')


def account_main(dialog=False):
    return ('<div class="page">' + crumb('', 'Zalo OA')
            + '<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">Zalo OA · Đặc sản An Nhiên ' + sign('pass', 'i-check', 'Hoạt động') + '</h1>'
              '<p class="r-detail__fig"><span class="c-sub">Đồng ý bởi chị An ngày 04/10/2026 · đến 04/04/2027</span></p></div>'
              '<div class="r-detail__acts"><button class="c-btn" type="button">Nối lại</button><button class="c-btn c-btn--danger c-btn--quiet" type="button">Ngắt kết nối</button></div></div>'
            + grid('<section class="c-card" aria-labelledby="jb"><div class="c-card__head"><h2 class="c-card__title" id="jb">OPC dùng tài khoản này để</h2></div><ul class="c-list">'
                   + sw(True, 'Nhận đơn từ tin nhắn', 'đọc tin khách gửi · soạn đơn cho chị duyệt')
                   + sw(True, 'Trả lời khách', 'anh Khoa bấm gửi · OPC không tự gửi')
                   + sw(False, 'Gửi thông báo ZNS', 'cần mẫu tin được Zalo duyệt · có phí mỗi tin · xin đồng ý riêng khi bật') + '</ul></section>'
                   + '<section class="c-card" aria-labelledby="nn"><div class="c-card__head"><h2 class="c-card__title" id="nn">Nếu không nối</h2></div>'
                     '<p class="c-sub">Dán tin, chụp ảnh hoặc gõ tay vào Hộp yêu cầu · đơn vẫn tạo được.</p></section>',
                   '<aside class="r-tower__detail" aria-labelledby="rl"><h2 class="r-tower__t" id="rl">Hôm nay</h2><ol class="c-timeline c-timeline--quiet" aria-label="Hôm nay">'
                   '<li class="c-timeline__item c-timeline__item--ok"><span class="c-timeline__time">09:02</span><span class="c-timeline__dot" aria-hidden="true"></span><span class="c-timeline__body"><span class="c-timeline__src">Zalo OA</span><span class="c-timeline__what">Tin của chị Mai → DH-2052</span></span></li>'
                   '<li class="c-timeline__item c-timeline__item--ok"><span class="c-timeline__time">08:00</span><span class="c-timeline__dot" aria-hidden="true"></span><span class="c-timeline__body"><span class="c-timeline__src">Trợ lý</span><span class="c-timeline__what">Nhắc Sunrise lần 2</span></span></li></ol></aside>')
            + '</div>')


DLG = ('<div class="c-dialog" role="dialog" aria-modal="true" aria-labelledby="dc-t"><div class="c-dialog__panel"><div class="c-dialog__head"><div><span class="c-dialog__k">Zalo OA</span>'
       '<h2 class="c-dialog__title" id="dc-t" tabindex="-1">Ngắt kết nối Zalo?</h2></div><button class="c-icon-btn" type="button" aria-label="Đóng, giữ kết nối">' + ic('i-x') + '</button></div>'
       '<div class="c-dialog__body"><ul class="r-gate"><li class="r-gate__i r-gate__i--wait"><span class="r-gate__b"><b>Tin khách gửi sẽ không vào Hộp yêu cầu nữa</b><small>chị dán tin hoặc gõ tay như trước</small></span><span class="r-gate__amt"></span><span class="r-gate__act"></span></li>'
       '<li class="r-gate__i r-gate__i--ok"><span class="r-gate__b"><b>Đơn và lịch sử đã về OPC vẫn giữ nguyên</b><small>chỉ dừng nhận tin mới</small></span><span class="r-gate__amt"></span><span class="r-gate__act"></span></li></ul></div>'
       '<div class="c-dialog__foot"><button class="c-btn" type="button">Giữ kết nối</button><button class="c-btn c-btn--danger" type="button">Ngắt kết nối</button></div></div></div>')
save('connections--account', 'Kết nối · Zalo OA', account_main())
save('connections--disconnect', 'Kết nối · Ngắt Zalo OA', account_main())
import pathlib
p = SCREENS / 'connections--disconnect.html'
s = p.read_text().replace('</body>', DLG + '\n</body>')
p.write_text(s)
print('connect2: 5 screens')


# ------------------------------------------------------------------ 5 · X Invoice (account in error) — replaces the old category-shaped detail
def job(st, t, m, tone):
    return (f'<li class="r-gate__i r-gate__i--{tone}"><span class="r-gate__b"><b>{t}</b><small><span class="r-gate__st">{st}</span> · {m}</small></span>'
            f'<span class="r-gate__amt"></span><span class="r-gate__act"></span></li>')


def tl(kind, src, time, what, who=''):
    w = f'<span class="c-timeline__who">{who}</span>' if who else ''
    return (f'<li class="c-timeline__item c-timeline__item--{kind}"><span class="c-timeline__time">{time}</span><span class="c-timeline__dot" aria-hidden="true"></span>'
            f'<span class="c-timeline__body"><span class="c-timeline__src">{src}</span><span class="c-timeline__what">{what}</span>{w}</span></li>')


save('connections--detail', 'Kết nối · X Invoice',
     '<div class="page">' + crumb('', 'X Invoice')
     + '<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">X Invoice ' + sign('err', 'i-x', 'Lỗi') + '</h1>'
       '<p class="r-detail__fig"><span class="c-sub">Im lặng từ 10:12 · đồng ý đến 12/12/2027</span></p></div>'
       '<div class="r-detail__acts"><button class="c-btn c-btn--act" type="button">Hỏi lại X Invoice</button><a class="c-btn" href="order-detail--invoice.html">Lập tay trên cổng</a></div></div>'
     + grid('<section class="c-card" aria-labelledby="jb"><div class="c-card__head"><h2 class="c-card__title" id="jb">OPC dùng tài khoản này để</h2></div><ul class="r-gate">'
            + job('Lỗi', 'Hoá đơn có mã cho khách sỉ', 'DH-2047 chưa rõ kết quả', 'unk')
            + job('Hoạt động', 'Tra cứu mã số thuế khách', 'phản hồi 10:08', 'ok')
            + job('Chờ quyết định', 'Chữ ký số cho tờ khai', 'chưa chọn nhà cung cấp', 'wait') + '</ul></section>'
            + '<section class="c-card" aria-labelledby="nn"><div class="c-card__head"><h2 class="c-card__title" id="nn">OPC không làm</h2></div>'
              '<p class="c-sub">Tự gửi lại hoá đơn chưa rõ kết quả · nộp thuế thay chị.</p></section>',
            '<aside class="r-tower__detail" aria-labelledby="rl"><h2 class="r-tower__t" id="rl">Diễn biến hôm nay</h2><ol class="c-timeline c-timeline--quiet" aria-label="Diễn biến">'
            + tl('ok', 'OPC kiểm tra', '10:27', 'Hỏi lại trạng thái (chỉ đọc)', 'vẫn chưa có phản hồi')
            + tl('now', 'X Invoice', '10:12', 'DH-2047 chưa rõ kết quả', 'OPC không tự gửi lại') + '</ol></aside>')
     + '</div>')
print('connect2: +detail')

"""v4.3 · Tiền → Đóng ca (ca sáng 06/10, Hạnh) incl. COD hand-in. Writes shift-close.html (count by denomination vs
expected; difference needs a reason), shift-close--cod.html (dialog: anh Hùng hands over COD at 12:40),
shift-close--done.html (shift report, hand-over confirmed by chị An). Usage: python3 pages_shift.py"""
import re
from pages import build, ic, sign, subnav, SCREENS

CUR = '<span class="u-cur">₫</span>'
SUB = lambda: subnav('Tiền', [('Thu chi &amp; đối chiếu', 'money.html'), ('Công nợ', 'receivables.html'), ('Đóng ca', 'shift-close.html')], 'Đóng ca')


def as_cashier(name, clock):
    p = SCREENS / f'{name}.html'
    s = p.read_text()
    for a, b in [('Nguyễn Minh Khoa · Người vận hành', 'Hạnh · Thu ngân'), ('<span class="c-avatar__face" aria-hidden="true">K', '<span class="c-avatar__face" aria-hidden="true">H'),
                 ('Đã lưu 10:45', f'Đã lưu {clock}'), ('Đã lưu · <b>10:45</b>', f'Đã lưu · <b>{clock}</b>')]:
        s = s.replace(a, b)
    import navtree
    s = navtree.apply(s, 'money', name, role='cashier')   # v4.4: the cashier's rail
    p.write_text(s)


def rec(k, m, v, base=False, d=''):
    return (f'<li class="r-recon__r{" r-recon__r--base" if base else ""}"><span class="r-recon__k"><b>{k}</b><small>{m}</small></span>'
            f'<span class="r-recon__v">{v}</span><span class="r-recon__d">{d}</span></li>')


EXPECT = ('<ul class="r-recon r-shift__exp" aria-label="Tiền mặt phải có">'
          + rec('Đầu ca', 'Hạnh nhận 07:00', '500.000 ₫')
          + rec('+ Bán tiền mặt', '2 đơn · DH-2055, DH-2057', '845.000 ₫')
          + rec('+ Thu hộ nộp về', 'anh Hùng · DH-2051 Phố Núi · 12:40', '1.150.000 ₫')
          + rec('− Chi tiền mặt', 'cước xe khách DH-2043 · 13:10 · có biên lai', '<span class="r-shift__minus">−50.000 ₫</span>')
          + rec('Phải có trong két', 'OPC tính từ đơn và phiếu chi trong ca', f'<span class="r-shift__big">2.445.000{CUR}</span>', base=True)
          + rec('Đếm được', 'Hạnh đếm theo mệnh giá bên dưới · 14:02', f'<span class="r-shift__big">2.425.000{CUR}</span>', d=sign('err', 'i-x', 'Thiếu 20.000 ₫')) + '</ul>')
DEN = [('500.000', 4), ('200.000', 2), ('100.000', 0), ('50.000', 0), ('20.000', 1), ('10.000', 0), ('5.000', 1), ('2.000', 0), ('1.000', 0)]


def den_rows():
    out = []
    for v, n in DEN:
        tot = int(v.replace('.', '')) * n
        t = f'{tot:,}'.replace(',', '.') if tot else '—'
        out.append(f'<li class="r-den__i{" r-den__i--zero" if not n else ""}"><span class="r-den__v">{v}</span>'
                   f'<label class="r-den__n"><span class="u-sr">Số tờ {v} đồng</span><input class="c-field__input" inputmode="numeric" value="{n}"></label>'
                   f'<span class="r-den__t">{t}</span></li>')
    return '<ul class="r-den" aria-label="Đếm theo mệnh giá">' + ''.join(out) + '</ul>'


REASON = ('<div class="r-count__why r-shift__why"><p class="r-count__need" id="why-h">Chênh 20.000 ₫ — chọn lý do để đóng ca</p>'
          '<div class="c-seg" role="radiogroup" aria-labelledby="why-h" aria-required="true">'
          + ''.join(f'<button class="c-seg__opt" type="button" role="radio" aria-checked="false">{o}</button>' for o in ['Thối nhầm', 'Chi chưa ghi', 'Khách trả thiếu', 'Khác'])
          + '</div><label class="c-field"><span class="u-sr">Ghi chú</span><span class="c-field__control"><input class="c-field__input" placeholder="Ghi chú (tuỳ chọn)"></span></label>'
          '<p class="c-sub">Chênh dưới 50.000 ₫: chỉ cần lý do, chị An được báo. Từ 50.000 ₫: chị An duyệt.</p></div>')


def cod(t, m, amt, st):
    return f'<li class="r-plist__row"><span class="r-plist__k"><b>{t}</b><small>{m}</small></span><span class="r-shift__amt">{amt}</span>{st}</li>'


RAIL = ('<h2 class="r-tower__t" id="ca">Trong ca</h2><dl class="c-kv"><dt>QR tại quầy</dt><dd>2 khoản · 1.105.000 ₫ · đã xác minh cả 2</dd>'
        '<dt>Hoá đơn máy tính tiền</dt><dd>4 hoá đơn · có mã cả 4</dd><dt>Đơn tại quầy</dt><dd>5 đơn · 1 huỷ (có lý do)</dd></dl>'
        '<h2 class="r-tower__t r-rail__h2">Tiền thu hộ</h2><ul class="r-plist r-shift__cod">'
        + cod('Anh Hùng · DH-2051', 'Phố Núi · nộp 12:40', '1.150.000 ₫', sign('pass', 'i-check', 'Đã nhận'))
        + cod('Nhà xe Đức Long · DH-2043', 'chị Thảo · xe 16:30, thu khi khách nhận', '1.300.000 ₫', sign('wait', 'i-clock', 'Ngoài ca'))
        + cod('GHTK · DH-2046', 'chị Hoa · chuyển khoản kỳ thứ Sáu', '260.000 ₫', sign('wait', 'i-clock', 'Chờ đối soát'))
        + '</ul><p class="c-sub">Thu hộ của nhà xe và GHTK không vào két; OPC theo dõi ở Công nợ › Phải thu.</p>')
GATE = ('<div class="r-count__foot r-shift__foot"><p class="c-decide__result">Đóng ca = khoá số ca sáng · để lại <b>500.000 ₫</b> đầu ca chiều · nộp chị An <b>1.925.000 ₫</b></p>'
        f'<div class="c-decide__acts"><button class="c-btn c-btn--act" type="button" aria-disabled="true">{ic("i-lock")}Đóng ca · cần lý do chênh 20.000 ₫</button>'
        '<button class="c-btn" type="button">Đếm lại</button></div></div>')


def page(name, overlay=None, clock='14:02'):
    m = (f'\n      {SUB()}\n      <div class="page"><div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">Đóng ca sáng ' + sign('you', 'i-alert', 'Thiếu 20.000 ₫') + '</h1>'
         f'<p class="r-detail__fig"><span class="c-sub">Thứ Ba 06/10 · 07:00–14:00 · Hạnh · máy quầy</span></p></div></div>'
         '<div class="r-detail__grid r-detail--calm"><div class="stack">'
         '<section class="c-card r-count__card" aria-labelledby="cnt"><div class="c-card__head"><h2 class="c-card__title" id="cnt">Tiền mặt trong két</h2></div>'
         + EXPECT
         + '<h3 class="r-ready__h">Đếm theo mệnh giá</h3>' + den_rows()

         + REASON + GATE + '</section></div>'
         f'<aside class="r-tower__detail" aria-labelledby="ca">{RAIL}</aside></div></div>')
    build(name, 'Tiền · Đóng ca sáng', m, 'money', overlay=overlay)
    as_cashier(name, clock)


page('shift-close')

COD = ('<div class="c-dialog" role="dialog" aria-modal="true" aria-labelledby="cod-t"><div class="c-dialog__panel">'
       '<div class="c-dialog__head"><div><span class="c-dialog__k">Tiền thu hộ · 12:40</span><h2 class="c-dialog__title" id="cod-t" tabindex="-1">Nhận tiền từ anh Hùng</h2></div>'
       f'<a class="c-icon-btn" href="shift-close.html" aria-label="Đóng, chưa nhận">{ic("i-x")}</a></div>'
       '<div class="c-dialog__body"><dl class="c-kv"><dt>Đơn</dt><dd>DH-2051 · Nhà hàng Phố Núi · 4 gói bò, 2 hũ muối</dd>'
       '<dt>Anh Hùng thu</dt><dd>11:05 · khách ký nhận trên link giao hàng</dd><dt>Phải nộp</dt><dd><b>1.150.000 ₫</b></dd></dl>'
       '<label class="c-field"><span class="c-field__label">Hạnh đếm được</span><span class="c-field__control c-field__control--ok"><input class="c-field__input" inputmode="numeric" value="1.150.000"><span class="c-field__suffix">₫</span></span>'
       '<span class="c-field__hint">' + sign('ok', 'i-check', 'Khớp số phải nộp') + '</span></label></div>'
       '<div class="c-dialog__foot"><p class="c-decide__result">Nhận = tiền vào két ca sáng · DH-2051 thành <b>Đã thu</b> (tiền mặt) · anh Hùng hết giữ tiền của hộ</p>'
       '<button class="c-btn c-btn--quiet" type="button">Đếm lệch</button><button class="c-btn c-btn--act" type="button">Đã nhận 1.150.000 ₫</button></div></div></div>')
page('shift-close--cod', overlay=COD, clock='12:40')


# ---------------- report after close ----------------
def step(kind, src, time, what, detail=''):
    d = f'<span class="c-timeline__who">{detail}</span>' if detail else ''
    return (f'<li class="c-timeline__item c-timeline__item--{kind}"><span class="c-timeline__time">{time}</span><span class="c-timeline__dot" aria-hidden="true"></span>'
            f'<span class="c-timeline__body"><span class="c-timeline__src">{src}</span><span class="c-timeline__what">{what}</span>{d}</span></li>')


DONE = (f'\n      {SUB()}\n      <div class="page"><div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">Ca sáng đã đóng ' + sign('ok', 'i-check', 'Chị An đã nhận tiền') + '</h1>'
        f'<p class="r-detail__fig"><b class="c-figure">2.425.000{CUR}</b><span class="c-sub">tiền mặt cuối ca · thiếu 20.000 ₫ · lý do: thối nhầm · Hạnh đóng 14:06</span></p></div>'
        f'<div class="r-detail__acts"><button class="c-btn" type="button">{ic("i-print")}In biên bản ca</button></div></div>'
        '<div class="r-detail__grid r-detail--calm"><div class="stack">'
        '<section class="c-card" aria-labelledby="bb"><div class="c-card__head"><h2 class="c-card__title" id="bb">Biên bản ca</h2></div>'
        '<dl class="c-kv"><dt>Phải có</dt><dd>2.445.000 ₫ (đầu ca 500.000 + bán 845.000 + thu hộ 1.150.000 − chi 50.000)</dd>'
        '<dt>Ghi chú chênh</dt><dd>thối nhầm cho khách DH-2057</dd>'
        '<dt>QR tại quầy</dt><dd>2 khoản · 1.105.000 ₫ · đã xác minh</dd><dt>Hoá đơn</dt><dd>4 hoá đơn máy tính tiền · có mã</dd>'
        '<dt>Để lại đầu ca chiều</dt><dd>500.000 ₫ · ca chiều anh Khoa nhận 14:10</dd><dt>Nộp chị An</dt><dd>1.925.000 ₫ · chị An xác nhận 14:20</dd></dl></section></div>'
        '<aside class="r-tower__detail" aria-labelledby="dg"><h2 class="r-tower__t" id="dg">Diễn biến</h2><ol class="c-timeline c-timeline--quiet" aria-label="Diễn biến">'
        + step('ok', 'Chị An', '14:20', 'Xác nhận đã nhận 1.925.000 ₫', 'trên điện thoại chị An')
        + step('ok', 'Anh Khoa', '14:10', 'Nhận đầu ca chiều 500.000 ₫')
        + step('now', 'Hạnh', '14:06', 'Đóng ca · lý do chênh: thối nhầm', 'dưới 50.000 ₫ → không cần duyệt, chị An được báo')
        + step('ok', 'OPC kiểm tra', '14:02', 'Tính tiền phải có 2.445.000 ₫', 'từ 2 đơn tiền mặt, 1 khoản thu hộ, 1 phiếu chi')
        + step('ok', 'Hạnh', '12:40', 'Nhận 1.150.000 ₫ thu hộ từ anh Hùng', 'DH-2051')
        + step('ok', 'Hạnh', '07:00', 'Mở ca · đầu ca 500.000 ₫') + '</ol>'
        '<p class="c-sub">Số ca đã khoá; sửa phải mở lại ca, có lý do và chị An duyệt.</p></aside></div></div>')
build('shift-close--done', 'Tiền · Ca sáng đã đóng', DONE, 'money')
as_cashier('shift-close--done', '14:20')
print('shift: 3 screens')

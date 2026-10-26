"""v4.3 · Home (UI-01) + the shared shell in An Nhiên data. Rewrites screens/home.html — the shell every page.build()
uses — from src_v43/home.v42.html (the last Cô Hai home), and writes overlay sources src_v43/home--*.html for
home_states.py. Today = Thứ Ba 06/10/2026 10:45; user anh Khoa. Run FIRST, then states/home_states/pages_*.
Usage: python3 home43.py"""
import json, re, pathlib
HERE = pathlib.Path(__file__).parent
SCREENS = HERE.parents[1] / 'apps/app/screens'
SYS = HERE.parents[1] / 'system'
ICONS = {**json.load(open(SYS / 'assets/icons/lucide-map.json')), **json.load(open(SYS / 'assets/icons/lucide-extra.json'))}
ic = lambda i: f'<svg class="c-ic" aria-hidden="true"><use href="#{i}"/></svg>'
CUR = '<span class="u-cur">₫</span>'
sign = lambda k, i, t: f'<span class="c-sign c-sign--{k}"><span class="c-sign__pic">{ic(i)}</span>{t}</span>'

s = (HERE / 'src_v43/home.v42.html').read_text()
# ---- shell ----
for a, b in [('Đổi hộ kinh doanh — đang chọn Hải sản khô Cô Hai, Nhơn Lý', 'Đổi hộ kinh doanh — đang chọn Đặc sản Cao Nguyên An Nhiên, Pleiku'),
             ('<span class="c-hh__mark" aria-hidden="true">CH</span>', '<span class="c-hh__mark" aria-hidden="true">AN</span>'),
             ('Cô Hai · Nhơn Lý', 'An Nhiên · Pleiku'), ('Đổi hộ kinh doanh — đang chọn Hải sản khô Cô Hai', 'Đổi hộ kinh doanh — đang chọn Đặc sản An Nhiên'),
             ('<strong class="c-hh__name">Hải sản khô Cô Hai</strong><span class="c-hh__sub">Nhơn Lý</span>', '<strong class="c-hh__name">Đặc sản An Nhiên</strong><span class="c-hh__sub">Pleiku</span>'),
             ('Nguyễn Văn Phúc · Quản lý', 'Nguyễn Minh Khoa · Người vận hành'), ('<span class="c-avatar__face" aria-hidden="true">P</span>', '<span class="c-avatar__face" aria-hidden="true">K</span>'),
             ('<a class="c-nav__item" href="#">' + ic('i-box') + 'Hàng hoá</a>', '<a class="c-nav__item" href="products.html">' + ic('i-box') + 'Hàng hoá</a>'),
             ('<a class="c-nav__item" href="invoices.html">', '<a class="c-nav__item" href="period.html">'),
             ('<a class="c-nav__item" href="settings-users.html">', '<a class="c-nav__item" href="readiness.html">'),
             ('aria-label="6 việc cần xem">6<', 'aria-label="3 việc cần chị: 2 cần quyết, 1 lỗi">3<'),
             ('aria-label="6 việc cần làm">6<', 'aria-label="3 việc cần làm">3<'),
             ('data-tip="MB (qua Casso) cập nhật 2 phút trước · Hoá đơn Hilo hoạt động · Cổng thuế chưa bật · Đã lưu 10:45"',
              'data-tip="MB (qua Casso) cập nhật 2 phút trước · Hilo hoạt động · X Invoice không trả lời 10:12 · Cổng thuế chưa bật · Đã lưu 10:45"')]:
    assert a in s, a[:60]
    s = s.replace(a, b)


import navtree
s = re.sub(r'<ul class="c-nav__list">[\s\S]*?</ul>\s*<ul class="c-nav__list(?: c-nav__list--foot)?">[\s\S]*?</ul>(?=\s*</nav>)', lambda _: navtree.lists('home'), s, count=1)
s = re.sub(r'(<a class="c-tabbar__item" href="money.html">[\s\S]*?Tiền)<span class="c-tabbar__count" aria-label="3 cần xem">3</span>', r'\1<span class="c-tabbar__count" aria-label="2 khoản cần xem">2</span>', s, count=1)
# ---- main ----
def bar(v, k, tip, today=False):
    t = f' data-tip="{tip}"' if not today else ''
    val = ''   # the hero already says today's figure once
    return (f'<li class="c-bars__d{" c-bars__d--today" if today else ""}" style="--v:{v}"{t}><span class="c-bars__col"><span class="c-bars__bar"></span>{val}</span>'
            f'<span class="c-bars__k">{k}<span class="u-sr">{": 7.235.000 ₫, đang bán" if today else " " + tip}</span></span></li>')


BARS = ''.join([bar(.635, 'T4', 'T4 30/9 · 6.100.000 ₫'), bar(.563, 'T5', 'T5 01/10 · 5.400.000 ₫'), bar(.927, 'T6', 'T6 02/10 · 8.900.000 ₫'),
                bar(1, 'T7', 'T7 03/10 · 9.600.000 ₫'), bar(.75, 'CN', 'CN 04/10 · 7.200.000 ₫'), bar(.708, 'T2', 'T2 05/10 · 6.800.000 ₫'),
                bar(.754, 'Hôm nay', '', today=True)])
ORD = lambda who, meta, st, amt, href='order-detail.html': (f'<li class="c-orders__row"><a href="{href}"><span class="c-orders__who">{who}<small>{meta}</small></span>'
                                                             f'<span class="c-orders__st">{st}</span><span class="c-orders__amt u-money">{amt}</span></a></li>')
MAIN = f'''
      <div class="r-page-head">
        <div>
          <h1 class="r-page-head__title">Hôm nay</h1>
          <p class="c-sub">Thứ Ba, 06/10/2026 · Ca sáng từ 07:00 · Hạnh ở quầy</p>
        </div>
        <div class="r-page-head__acts r-page-head__acts--desk">
          <a class="c-btn" href="shift-close.html">Đóng ca</a>
          <button class="c-btn" type="button">{ic("i-plus")}Tạo đơn</button>
          <button class="c-icon-btn c-icon-btn--outline" type="button" aria-label="Thao tác khác: ghi khoản chi, nhập hàng" data-tip="Ghi khoản chi · Nhập hàng" data-tip-end>{ic("i-more")}</button>
        </div>
      </div>

      <div class="r-home">
        <!-- 1 · the answer: how is today, and is the money real -->
        <section class="c-stat r-home__hero" aria-labelledby="h-rev">
          <div class="c-stat__top">
            <h2 class="c-stat__label" id="h-rev">Doanh thu hôm nay · 5 đơn đã giao</h2>
            <span class="c-stat__fresh">MB · cập nhật 2 phút trước</span>
          </div>
          <div class="c-stat__main">
            <div>
              <p class="c-stat__fig">7.235.000{CUR}</p>
              <p class="c-stat__delta"><span class="c-stat__chip">{ic("i-trend")}6%</span>so với thứ Ba trước</p>
              <a class="c-stat__why" href="home--assistant.html">Vì sao?{ic("i-chev-r")}</a>
            </div>
            <ol class="c-bars" aria-label="Doanh thu 7 ngày gần nhất" data-cap="7 ngày">
              {BARS}
            </ol>
          </div>
          <div class="c-split">
            <div class="c-split__bar" role="img" aria-label="Đã xác minh 4.745.000 ₫, chờ xác minh 390.000 ₫, chưa thu 2.100.000 ₫"><i class="c-split__ok" style="flex:4745"></i><i class="c-split__pend" style="flex:390"></i><i class="c-split__you" style="flex:2100"></i></div>
            <p class="r-home__moneyline"><span class="r-home__mk r-home__mk--ok">phần lớn đã khớp sao kê</span><a class="r-home__mk r-home__mk--pend" href="money.html">1 khoản chờ xác minh</a><a class="r-home__mk r-home__mk--you" href="receivables.html">2 đơn chưa thu</a><a class="r-home__tomoney" href="money.html">chi tiết ở Tiền</a></p>
          </div>
        </section>

        <!-- 2 · what needs me now -->
        <section class="c-card r-home__todo" aria-labelledby="h-todo">
          <div class="c-card__head"><h2 class="c-card__title" id="h-todo">Cần làm <span class="c-count" aria-label="3 việc">3</span></h2><a class="c-link" href="approvals.html">Xem tất cả</a></div>
          <a class="r-home__run" href="approvals--running.html">{ic("i-clock")}<span>OPC đang chạy <b>3 việc</b></span><span class="r-home__err">{ic("i-alert")}1 lỗi</span>{ic("i-chev-r")}</a>
          <ol class="c-todo">
            <li class="c-todo__item c-todo__item--now" id="todo-1"><span class="c-todo__n" aria-hidden="true">1</span>
              <div><h3 class="c-todo__t">Soạn DH-2052 cho Sunrise Hotel</h3><p class="c-todo__m">20 gói bò, 30 hũ muối · trước 15:00</p></div>
              <a class="c-btn c-btn--act c-todo__go" href="delivery--pick.html">Soạn hàng</a></li>
            <li class="c-todo__item"><span class="c-todo__n" aria-hidden="true">2</span>
              <div><h3 class="c-todo__t">Nhận hàng MH-0118 thiếu 5 kg</h3><p class="c-todo__m">HTX Cao Nguyên · chờ chị quyết</p></div>
              <a class="c-btn c-todo__go" href="purchase-detail--receive.html">Xem</a></li>
            <li class="c-todo__item"><span class="c-todo__n" aria-hidden="true">3</span>
              <div><h3 class="c-todo__t">Hoá đơn DH-2047 chưa rõ kết quả</h3><p class="c-todo__m"><span class="u-money">1.840.000 ₫</span> · X Invoice im lặng từ 10:12</p></div>
              <a class="c-btn c-todo__go" href="approvals--error.html">Xem</a></li>
          </ol>
          <a class="c-todo__later" href="approvals.html"><span><b>4 việc không gấp</b></span>{ic("i-chev-r")}</a>
        </section>

        <!-- 3 · recent orders -->
        <section class="c-card r-home__orders" aria-labelledby="h-orders">
          <div class="c-card__head"><h2 class="c-card__title" id="h-orders">Đơn gần đây</h2><a class="c-link" href="orders.html">Tất cả đơn</a></div>
          <ul class="c-orders">
            {ORD("Khách lẻ", "DH-2053 · Quầy · 10:44", sign("wait", "i-qr", "Chờ khách chuyển"), "715.000 ₫", "counter--qr.html")}
            {ORD("Nhà hàng Phố Núi", "DH-2051 · Zalo OA · 10:20", sign("wait", "i-clock", "Đang giao · thu hộ"), "1.150.000 ₫", "delivery.html")}
            {ORD("Sunrise Hotel", "DH-2052 · Zalo OA · 09:02", sign("pend", "i-box", "Đã giữ hàng"), "6.250.000 ₫")}
            {ORD("Homestay Mây Ngàn", "DH-2045 · Thêm tay · 09:40", sign("pend", "i-clock", "Chờ xác minh"), "390.000 ₫", "money.html")}
            {ORD("Sunrise Hotel", "DH-2049 · Định kỳ · 08:30", sign("ok", "i-check", "Đã đóng"), "4.550.000 ₫", "receivables.html")}
          </ul>
        </section>

        <!-- 4 · period + receivables + readiness -->
        <section class="c-card r-home__side" aria-label="Kỳ thuế, công nợ, mua và kho">
          <div class="r-home__part" aria-labelledby="h-tax">
            <div class="c-card__head"><h2 class="c-card__title" id="h-tax">Kỳ Quý III</h2><a class="c-link" href="period.html">Đối chiếu</a></div>
            <p class="c-sub"><b>5 việc</b> · hạn khai 31/10</p>
            <div class="c-meter c-meter--quiet">
              <div class="c-meter__row"><span class="u-meta">Doanh thu từ 01/01 · <b>718,4 triệu</b></span><span class="u-meta u-nowrap">mốc 1 tỷ</span></div>
              <div class="c-meter__bar" role="img" aria-label="Doanh thu từ 01/01 718.400.000 ₫, dưới mốc 1 tỷ"><span class="c-meter__fill" style="width:71.8%"></span></div>
              <p class="c-meter__why">{ic("i-alert")}Nhịp năm khoảng 1,06 tỷ · mốc chờ kế toán xác nhận</p>
            </div>
          </div>
          <div class="r-home__part" aria-labelledby="h-debt">
            <div class="c-card__head"><h2 class="c-card__title" id="h-debt">Khách còn nợ</h2><span class="u-money">17.700.000 ₫</span></div>
            <ul class="c-debts">
              <li class="c-debts__row"><span class="c-debts__k">Sunrise Hotel</span><span class="c-debts__v">8.400.000 ₫</span><span class="c-debts__m">quá hạn 12 ngày · bảng kê chờ chị gửi nay</span></li>
              <li class="c-debts__row"><span class="c-debts__k">Nhà hàng Phố Núi</span><span class="c-debts__v">3.900.000 ₫</span><span class="c-debts__m">hạn 12/10</span></li>
            </ul>
          </div>
          <div class="r-home__part" aria-labelledby="h-buy">
            <div class="c-card__head"><h2 class="c-card__title" id="h-buy">Mua và kho</h2><a class="c-link" href="purchases.html">Đơn mua{ic("i-chev-r")}</a></div>
            <ul class="c-debts">
              <li class="c-debts__row"><span class="c-debts__k"><a href="purchase-detail--receive.html">MH-0118 đã về</a></span><span class="c-debts__v">45/50 hũ</span><span class="c-debts__m">chờ chị xác nhận nhập kho</span></li>
              <li class="c-debts__row"><span class="c-debts__k">Bò một nắng</span><span class="c-debts__v">26 gói</span><span class="c-debts__m">khả dụng · +40 gói Thứ Năm (MH-0121)</span></li>
              <li class="c-debts__row"><span class="c-debts__k"><a href="receivables--payables.html">Phải trả tuần này</a></span><span class="c-debts__v">4.050.000 ₫</span><span class="c-debts__m">HTX 2.800.000 ₫ hạn 08/10</span></li>
            </ul>
          </div>
        </section>
      </div>
'''
a = s.index('<main class="r-shell__content">') + len('<main class="r-shell__content">'); b = s.index('</main>')
s = s[:a] + MAIN + '    ' + s[b:]
used = list(dict.fromkeys(re.findall(r'href="#(i-[\w-]+)"', s)))
sprite = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">\n'
          + '\n'.join(f'  <symbol id="{u}" viewBox="0 0 24 24">{ICONS[u]}</symbol>' for u in used if u in ICONS) + '\n</svg>')
s = re.sub(r'<svg width="0" height="0" style="position:absolute"[^>]*>[\s\S]*?</svg>', lambda m: sprite, s, count=1) if '<svg width="0"' in s else s.replace('<body>', '<body>\n' + sprite, 1)
s = re.sub(r'<title>[^<]*</title>', '<title>Hôm nay · Đặc sản An Nhiên — OPC</title>', s, count=1)
(SCREENS / 'home.html').write_text(s)

# ---- overlays for home_states (src_v43/home--*.html: '<nav class="c-tabbar"></nav>' + overlay + '</body>') ----
old = lambda n: (lambda t: t[t.index('</nav>', t.index('<nav class="c-tabbar"')) + 6:t.index('</body>')])((HERE / f'src_v31/{n}.html').read_text())
REPL = {
 'home--more': [('4 chờ chị duyệt · 2 cảnh báo', '2 cần chị quyết · 1 lỗi'), ('<span class="c-menulist__count">6</span>', '<span class="c-menulist__count">3</span>'),
                ('href="#">' + ic('i-box'), 'href="products.html">' + ic('i-box')),
                ('Danh sách &amp; giá · Lịch sử giá · Tồn kho (2 sắp hết) · Nhập hàng · Nhà cung cấp', 'Hàng và giá · Tồn kho · Kiểm kho'),
                ('href="invoices.html">', 'href="period.html">'),
                ('Hoá đơn · Sổ sách · Thuế &amp; tờ khai quý III: 6.184.500 ₫, hạn 31/10 · Báo cáo', 'Kỳ thuế Quý III: 5 việc, hạn 31/10 · Sổ sách · Hoá đơn · Nhật ký'),
                ('href="settings-users.html">', 'href="readiness.html">'), ('Người dùng · Tính năng · Kết nối · Nhật ký hoạt động', 'Sẵn sàng · Kết nối · Vai trò &amp; duyệt · Tính năng'),
                ('Gọi chị Lan · Zalo OPC Gia Lai', 'Nhân viên OPC Gia Lai · Zalo OPC')],
 'home--notifications': [('Hộ Cô Hai · Nhơn Lý', 'Đặc sản An Nhiên · Pleiku'),
                ('Đã xác minh 1.020.000 ₫ · DH-1043', 'Đã xác minh 4.550.000 ₫ · DH-2049'), ('<span class="c-notice__time">10:47</span><span class="c-notice__text">Ngân hàng đã xác nhận. Đơn hoàn tất phần tiền.', '<span class="c-notice__time">08:43</span><span class="c-notice__text">Sunrise trả QR khi nhận hàng. Đơn đã đóng.'),
                ('Có tiền mới 1.020.000 ₫ chờ xác minh', 'Có tiền mới 390.000 ₫ chờ xác minh'), ('<span class="c-notice__time">10:44</span><span class="c-notice__text">Từ QR tại quầy, đơn DH-1043.', '<span class="c-notice__time">09:52</span><span class="c-notice__text">Homestay Mây Ngàn chuyển khoản, đơn DH-2045.'),
                ('Hoá đơn 00000418 đang chờ mã CQT', 'Hoá đơn DH-2047 chưa rõ kết quả'), ('<span class="c-notice__time">10:20</span><span class="c-notice__text">Hilo báo lỗi lúc 08:34, OPC đã gửi lại.', '<span class="c-notice__time">10:12</span><span class="c-notice__text">X Invoice không trả lời. OPC không tự gửi lại, đang hỏi lại.'),
                ('Chuyển khoản 2.150.000 ₫ chưa có mã đơn', 'Nhận hàng MH-0118 thiếu 5 hũ'), ('<span class="c-notice__time">09:15</span><span class="c-notice__text">Từ NHA HANG BIEN DONG. Chị chọn đơn để gán.', '<span class="c-notice__time">08:40</span><span class="c-notice__text">HTX Cao Nguyên giao 45/50 hũ muối. Chị xác nhận số thực nhận.'),
                ('Liên kết MB cần đồng ý lại trước 17/10', 'Liên kết MB cần đồng ý lại trước 28/12'),
                ('Nhắc: khai thuế quý III hạn 31/10', 'Nhắc: đối chiếu Quý III, hạn khai 31/10'), ('Tạm tính 6.184.500 ₫.', 'Còn 5 việc trước khi khoá kỳ.')],
 'home--command': [('value="dh-104"', 'value="dh-205"'), ('<mark>DH-104</mark>', '<mark>DH-205</mark>'),
                ('</mark>3<span class="c-menu__sub">Khách lẻ · chờ xác minh</span></span><span class="c-menu__aside">1.020.000 ₫', '</mark>3<span class="c-menu__sub">Khách lẻ · chờ khách chuyển</span></span><span class="c-menu__aside">715.000 ₫'),
                ('</mark>2<span class="c-menu__sub">Khách lẻ · hoàn tất</span></span><span class="c-menu__aside">245.000 ₫', '</mark>2<span class="c-menu__sub">Sunrise Hotel · đã giữ hàng</span></span><span class="c-menu__aside">6.250.000 ₫'),
                ('</mark>1<span class="c-menu__sub">Chị Thu · chờ xác minh</span></span><span class="c-menu__aside">360.000 ₫', '</mark>1<span class="c-menu__sub">Nhà hàng Phố Núi · đang giao</span></span><span class="c-menu__aside">1.150.000 ₫'),
                ('</mark>0<span class="c-menu__sub">Khách sạn Hải Âu · chờ xác nhận</span></span><span class="c-menu__aside">3.420.000 ₫', '</mark>0<span class="c-menu__sub">Anh Nam · hẹn giao mai</span></span><span class="c-menu__aside">585.000 ₫')],
 'home--assistant': [('Vì sao hôm nay tăng 19%?', 'Vì sao hôm nay tăng 6%?'), ('Quý III nộp bao nhiêu thuế?', 'Quý III còn thiếu gì?'),
                ('Doanh thu tăng 1.340.000 ₫ so với hôm qua, chủ yếu từ DH-1027 của Công ty TNHH Du lịch Biển Xanh (1.690.000 ₫) — khách mới, mua 6 món.',
                 'Doanh thu tăng 410.000 ₫ so với thứ Ba tuần trước, chủ yếu vì đơn định kỳ DH-2049 của Sunrise Hotel (4.550.000 ₫) có thêm 5 gói bò.'),
                ('Nguồn: Đơn hôm nay (23) · Sao kê MB đến 10:44', 'Nguồn: 5 đơn đã giao hôm nay · sao kê MB đến 10:44'),
                ('Hỏi người thật · chị Lan', 'Hỏi người thật · nhân viên OPC'),
                ('Lưu Công ty TNHH Du lịch Biển Xanh làm khách quen.', 'Đặt đơn định kỳ thứ Hai cho Sunrise thành 20 gói bò, vì 4 tuần liền chị Mai xin thêm.')],
}
TREE = ('<nav class="c-nav c-nav--sheet" aria-label="Tất cả mục">' + navtree.lists('home', None, open_all=True)   # v4.5.6: the sheet shows where you came from (Hôm nay)
        + '<p class="u-meta">Hôm nay, Quầy, Bán và Tiền cũng ở thanh dưới màn hình.</p></nav>')
REPL['home--more'] = [('__TREE__', TREE)]
for n, rep in REPL.items():
    o = old(n)
    if n == 'home--more':
        o = re.sub(r'<nav class="c-menulist"[\s\S]*?</nav>', '__TREE__', o, count=1)
    for a, b in rep:
        assert a in o, (n, a[:60])
        o = o.replace(a, b)
    (HERE / f'src_v43/{n}.html').write_text('<nav class="c-tabbar"></nav>' + o + '</body>')
print('home43 ok')

"""v4.2 · Chương trình → Pilot dashboard (BA UI-20, UC-07, F15.02–F15.05). Program Viewer shell (PM Quang):
aggregate results only; households appear with stage and flags, never money/orders/customers.
Writes program.html, program--help.html, program-report.html. Usage: python3 pages_program.py"""
import re
from pages import build, ic, sign, SCREENS, ICONS


def shell(name, cur):
    p = SCREENS / f'{name}.html'
    s = p.read_text()
    nav = (f'<ul class="c-nav__list">'
           f'<li><a class="c-nav__item" href="program.html"{" aria-current=" + chr(34) + "page" + chr(34) if cur == "home" else ""}>{ic("i-trend")}Tổng quan pilot</a></li>'
           f'<li><a class="c-nav__item" href="program--help.html"{" aria-current=" + chr(34) + "page" + chr(34) if cur == "help" else ""}>{ic("i-people")}Hộ tham gia<span class="c-nav__count" aria-label="4 hộ cần hỗ trợ">4</span></a></li>'
           f'<li><a class="c-nav__item" href="program-report.html"{" aria-current=" + chr(34) + "page" + chr(34) if cur == "report" else ""}>{ic("i-file")}Báo cáo</a></li></ul>'
           f'<ul class="c-nav__list"><li><a class="c-nav__item" href="#">{ic("i-shield")}Dữ liệu được xem</a></li><li><a class="c-nav__item" href="#">{ic("i-help")}Trợ giúp</a></li></ul>')
    s = re.sub(r'<ul class="c-nav__list">[\s\S]*?(?=\s*</nav>)', lambda m: nav, s, count=1)   # v4.5.2: the household rail now nests lists
    hh = ('<span class="c-hh__mark" aria-hidden="true">KN</span><span class="c-hh__text"><strong class="c-hh__name">Kế nghiệp số · Gia Lai</strong>'
          '<span class="c-hh__sub">Pilot đợt 1 · 8 hộ</span></span>')
    s = re.sub(r'(<button class="c-hh" type="button" aria-label=")[^"]*(">)[\s\S]*?(</button>)',
               lambda m: m.group(1) + 'Chương trình Kế nghiệp số Gia Lai, pilot đợt 1' + m.group(2) + hh + m.group(3), s, count=1)
    s = re.sub(r'(<button class="c-hh c-hh--bar r-shell__phone" type="button" aria-label=")[^"]*(">)[\s\S]*?(</button>)',
               lambda m: m.group(1) + 'Chương trình Kế nghiệp số Gia Lai' + m.group(2) + hh + m.group(3), s, count=1)
    s = s.replace('placeholder="Tìm đơn, món, khách…"', 'placeholder="Tìm hộ tham gia…"').replace('aria-label="Tìm đơn, món, khách"', 'aria-label="Tìm hộ tham gia"')
    s = re.sub(r'<span class="c-health r-shell__desk"[^>]*>[\s\S]*?</span>', '<span class="c-health r-shell__desk" role="status" tabindex="0" data-tip="Số liệu tổng hợp, cập nhật mỗi đêm · lần cuối 06/10 02:00">Cập nhật · <b>02:00</b></span>', s, count=1)
    s = re.sub(r'<a class="c-btn c-btn--quiet r-shell__desk" href="home--assistant.html">[\s\S]*?</a>', '', s, count=1)
    s = re.sub(r'<button class="c-avatar r-shell__desk" type="button" aria-label="[^"]*"><span class="c-avatar__face" aria-hidden="true">.',
               '<button class="c-avatar r-shell__desk" type="button" aria-label="PM Quang · Xem chương trình — tài khoản"><span class="c-avatar__face" aria-hidden="true">Q', s, count=1)
    tab = ('<nav class="c-tabbar" aria-label="Điều hướng nhanh">'
           f'<a class="c-tabbar__item" href="program.html"{" aria-current=" + chr(34) + "page" + chr(34) if cur == "home" else ""}>{ic("i-trend")}Tổng quan</a>'
           f'<a class="c-tabbar__item" href="program--help.html"{" aria-current=" + chr(34) + "page" + chr(34) if cur == "help" else ""}>{ic("i-people")}Hộ<span class="c-tabbar__count" aria-label="4 cần hỗ trợ">4</span></a>'
           f'<a class="c-tabbar__item" href="program-report.html"{" aria-current=" + chr(34) + "page" + chr(34) if cur == "report" else ""}>{ic("i-file")}Báo cáo</a></nav>')
    s = re.sub(r'<nav class="c-tabbar"[\s\S]*?</nav>', lambda m: tab, s, count=1)
    s = s.replace('class="r-shell"', 'class="r-shell r-shell--program"', 1)
    used = sorted(set(re.findall(r'href="#(i-[a-z0-9-]+)"', s)))
    sprite = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">\n'
              + '\n'.join(f'  <symbol id="{u}" viewBox="0 0 24 24">{ICONS[u]}</symbol>' for u in used if u in ICONS) + '\n</svg>')
    s = re.sub(r'<svg width="0" height="0" style="position:absolute"[^>]*>[\s\S]*?</svg>', lambda m: sprite, s, count=1)
    p.write_text(s)


def head(title, subline, primary):
    return (f'<div class="r-page-head"><div><h1 class="r-page-head__title">{title}</h1><p class="c-sub">{subline}</p></div>'
            f'<div class="r-page-head__acts">{primary}</div></div>')


PRIV = ('<p class="r-trust r-trust--gate">' + ic('i-shield') + '<span><b>Chỉ thấy tiến độ theo bước</b> · không thấy dữ liệu kinh doanh của từng hộ, nhóm dưới 3 hộ được gộp</span></p>')


def stage(n, of, t, m, tone=''):
    pct = round(100 * n / of)
    return (f'<li class="r-funnel__s{" r-funnel__s--" + tone if tone else ""}"><span class="r-funnel__k"><b>{t}</b>' + (f'<small>{m}</small>' if m else '') + '</span>'
            f'<span class="r-funnel__bar" aria-hidden="true"><i style="width:{pct}%"></i></span><span class="r-funnel__v"><b>{n}</b>/{of}</span></li>')


FUNNEL = ('<ol class="r-funnel" aria-label="Hộ qua từng bước của pilot">'
          + stage(8, 8, 'Tham gia', '2 hộ sớm · 6 hộ đợt 1')
          + stage(6, 8, 'Thiết lập xong', '')
          + stage(6, 8, 'Có giao dịch bán thật', '')
          + stage(5, 8, 'Đã phát hành hoá đơn', '')
          + '</ol><h3 class="r-funnel__h">Trên 2 hộ đã đủ thời gian (hộ sớm)</h3><ol class="r-funnel r-funnel--part" aria-label="Các bước chỉ tính trên hộ đủ thời gian">'
          + stage(1, 2, 'Hoàn thành một kỳ thuế', '', 'part')
          + stage(2, 2, 'Còn dùng sau 90 ngày', 'đợt 1 tính từ 14/12', 'part')
          + '</ol>')


def issue(n, t, m, href):
    return (f'<li><a class="c-work" href="{href}"><span class="c-work__state"><span class="r-issue__n">{n} hộ</span></span>'
            f'<span class="c-work__t">{t}</span><span class="c-work__m">{m}</span></a></li>')


ISSUES = ('<ul class="c-works" aria-label="Cần hỗ trợ theo loại vấn đề">'
          + issue(1, 'Bị chặn khi thiết lập', 'thiếu bảng giá 6 ngày', 'program--help.html#h1')
          + issue(1, 'Chưa liên kết tài khoản tên hộ', 'đang thu vào tài khoản cá nhân', 'program--help.html#h2')
          + issue(1, 'Chưa có chữ ký số', 'chờ chương trình chọn nhà cung cấp', 'program--help.html#h3')
          + issue(1, 'Quý III còn 2 việc', 'hạn 31/10', 'program--help.html#h4')
          + '</ul>')


def bar(t, n, of=7):
    return (f'<li class="r-adopt__r"><span>{t}</span><span class="r-adopt__bar" aria-hidden="true"><i style="width:{round(100 * n / of)}%"></i></span>'
            f'<span class="r-adopt__v">{n}/{of}</span></li>')


ADOPT = ('<ul class="r-adopt" aria-label="Số hộ dùng từng nhóm tính năng trong 30 ngày, trên 7 hộ đang hoạt động">'
         + bar('Bán nhanh', 7) + bar('Nhập hàng', 6) + bar('Trợ lý đọc tin, chứng từ', 6) + bar('Đơn từ Zalo OA', 5)
         + bar('Giữ hàng & giao', 5) + bar('Hoá đơn có mã', 4) + bar('Trả tiền nhà cung cấp', 3) + bar('Đối chiếu kỳ', 2) + '</ul>')
STATS = ('<dl class="r-pstats"><div><dt>Hoạt động 7 ngày qua</dt><dd><b>7</b>/8 hộ<small>tuần trước 6/8</small></dd></div>'
         '<div><dt>Đơn qua OPC · 30 ngày</dt><dd><b>1.426</b> đơn<small>30 ngày trước 612</small></dd></div>'
         '<div><dt>Đối chiếu tự động</dt><dd><b>91%</b> giao dịch<small>tuần trước 88%</small></dd></div>'
         '<div><dt>Hỗ trợ · phản hồi trung vị</dt><dd><b>18</b> phút<small>tuần trước 26 phút</small></dd></div></dl>')
HOME = ('\n      ' + head('Pilot Kế nghiệp số · đợt 1', 'Ngày 6 của Quý IV/2026 · 8 hộ · cập nhật mỗi đêm',
                          f'<a class="c-btn c-btn--act" href="program-report.html">{ic("i-download")}Xuất báo cáo</a>')
        + '<div class="page">' + PRIV + STATS
        + '<div class="r-detail__grid r-detail--calm"><div class="stack">'
        '<section class="c-card" aria-labelledby="fn"><div class="c-card__head"><h2 class="c-card__title" id="fn">Hộ qua từng bước</h2>'
        '<a class="c-link" href="program-report.html">Cách tính từng bước</a></div>' + FUNNEL + '</section>'
        '<section class="c-card" aria-labelledby="ad"><div class="c-card__head"><h2 class="c-card__title" id="ad">Đang dùng gì · 30 ngày</h2><span class="u-meta">trên 7 hộ đang hoạt động</span></div>' + ADOPT + '</section></div>'
        '<aside class="r-tower__detail" aria-labelledby="hp"><h2 class="r-tower__t" id="hp">Cần hỗ trợ · 4 hộ</h2>' + ISSUES
        + f'<p><a class="c-btn c-btn--quiet" href="program--help.html">Xem 4 hộ{ic("i-chev-r")}</a></p></aside></div></div>')
build('program', 'Chương trình · Pilot', HOME, 'home')
shell('program', 'home')

# ---------------- need help: households × stage × issue (no values) ----------------
who = lambda n, m: f'<td class="c-table__cell--main c-table__who"><b>{n}</b><small>{m}</small></td>'
ROWS = ''.join([
    '<tr class="r-conn__g"><th scope="rowgroup" colspan="4">Cần hỗ trợ · 4</th></tr>'
    '<tr class="c-table__row--you" id="h1">' + who('Mật ong Đak Đoa', 'đợt 1 · vào 30/09') + '<td>Thiết lập · Hàng hoá</td>'
    + f'<td>{sign("err", "i-x", "Bị chặn")}<small class="r-stock__note">thiếu bảng giá · 6 ngày</small></td><td>chị Thu · hẹn 07/10</td></tr>',
    '<tr id="h2">' + who('Măng khô K\'Bang', 'đợt 1 · vào 25/09') + '<td>Có giao dịch</td>'
    + f'<td>{sign("you", "i-alert", "Cần hỗ trợ")}<small class="r-stock__note">tài khoản cá nhân · 4 ngày</small></td><td>anh Tín · gọi 06/10</td></tr>',
    '<tr id="h3">' + who('Cà phê Chư Sê', 'đợt 1 · vào 15/09') + '<td>Có giao dịch</td>'
    + f'<td>{sign("pend", "i-help", "Chờ chương trình")}<small class="r-stock__note">chưa có chữ ký số · 9 ngày</small></td><td>chờ quyết định Câu 2</td></tr>',
    '<tr id="h4">' + who('Gạo Ia Ly', 'hộ sớm · vào 05/07') + '<td>Kỳ thuế Quý III</td>'
    + f'<td>{sign("wait", "i-clock", "Đang làm")}<small class="r-stock__note">còn 2 việc · hạn 31/10</small></td><td>chị Thu · 08/10</td></tr>',
])
OK_ROWS = '<tr class="r-conn__g"><th scope="rowgroup" colspan="4">Ổn · 4</th></tr>' + ''.join(f'<tr class="c-table__row--muted">' + who(n, m) + f'<td>{st}</td><td>{sign("pass", "i-check", "Ổn")}</td><td>—</td></tr>' for n, m, st in [
    ('Đặc sản Cao Nguyên An Nhiên', 'hộ sớm · vào 01/07', 'Đã xong kỳ Quý III'), ('Rau sạch Ia Grai', 'đợt 1 · vào 18/09', 'Có hoá đơn'),
    ('Bánh tráng Kon Thụp', 'đợt 1 · vào 22/09', 'Có hoá đơn'), ('Thổ cẩm Plei Phung', 'đợt 1 · vào 01/10', 'Có giao dịch')])
HELP = ('\n      ' + head('Hộ tham gia', '8 hộ · 4 cần hỗ trợ · chỉ hiện bước và vấn đề, không hiện số liệu kinh doanh', '')
        + '<div class="page">' + PRIV
        + ''
        '<div class="c-table__scroll" tabindex="0" role="region" aria-label="Hộ tham gia"><table class="c-table c-table--stack r-conn">'
        '<thead><tr><th scope="col">Hộ</th><th scope="col">Đang ở bước</th><th scope="col">Vấn đề</th><th scope="col">Ai hỗ trợ</th></tr></thead>'
        f'<tbody>{ROWS}{OK_ROWS}</tbody></table></div></div>')
build('program--help', 'Chương trình · Hộ tham gia', HELP, 'home')
shell('program--help', 'help')

# ---------------- controlled aggregate report ----------------
KPI = ('<div class="c-table__scroll" tabindex="0" role="region" aria-label="Chỉ số pilot"><table class="c-table c-table--stack">'
       '<thead><tr><th scope="col">Chỉ số</th><th scope="col" class="c-table__num">Kết quả</th><th scope="col">Cách tính</th></tr></thead><tbody>'
       '<tr><td>Tham gia</td><td class="c-table__num"><b>8</b></td><td>hộ đã đồng ý tham gia và chia sẻ ở mức bước · gốc cho các dòng dưới</td></tr>'
       '<tr><td>Thiết lập xong</td><td class="c-table__num"><b>6/8</b></td><td>Sẵn sàng hoặc Sẵn sàng có điều kiện</td></tr>'
       '<tr><td>Có giao dịch bán thật</td><td class="c-table__num"><b>6/8</b></td><td>ít nhất 1 đơn đã giao và thu tiền</td></tr>'
       '<tr><td>Đã phát hành hoá đơn</td><td class="c-table__num"><b>5/8</b></td><td>ít nhất 1 hoá đơn có mã hoặc máy tính tiền</td></tr>'
       '<tr class="r-conn__g"><th scope="rowgroup" colspan="3">Chỉ tính hộ đã đủ thời gian · 2 hộ sớm</th></tr>'
       '<tr><td>Hoàn thành một kỳ thuế <span class="u-meta">(2 hộ sớm)</span></td><td class="c-table__num"><b>1/2</b></td><td>trên hộ đã qua một kỳ · có tờ khai, biên nhận, bằng chứng</td></tr>'
       '<tr><td>Còn dùng sau 90 ngày <span class="u-meta">(2 hộ sớm)</span></td><td class="c-table__num"><b>2/2</b></td><td>trên hộ đủ 90 ngày · có thao tác nghiệp vụ trong 7 ngày cuối</td></tr>'
       '<tr><td>Hoạt động 7 ngày</td><td class="c-table__num"><b>7/8</b></td><td>có thao tác nghiệp vụ trong 7 ngày</td></tr>'
       '<tr><td>Đối chiếu tự động (hệ thống)</td><td class="c-table__num"><b>91%</b></td><td>tỷ lệ giao dịch tổng 8 hộ · phần còn lại xác minh tay</td></tr>'
       '</tbody></table></div>')
REPORT = ('\n      ' + head('Báo cáo pilot · đến 06/10/2026', 'Tổng hợp, có kiểm soát dữ liệu · dùng cho review 30/90 ngày (S16.09)',
                            f'<a class="c-btn c-btn--act" href="#">{ic("i-download")}Tải PDF</a>')
          + '<div class="page"><article class="c-doc r-preport" aria-labelledby="rp"><div class="c-doc__head"><div><h2 class="c-doc__title" id="rp">Pilot Kế nghiệp số Gia Lai · đợt 1</h2>'
          '<p class="c-sub">8 hộ · 01/07–06/10/2026 · số liệu đêm 06/10</p></div></div>' + PRIV
          + '<nav class="r-preport__toc" aria-label="Mục lục"><a href="#k">Kết quả</a><a href="#t">Thấy gì</a><a href="#d">Đề xuất</a></nav>'
          + '<h3 class="r-preport__h" id="k">Kết quả</h3>' + KPI
          + '<h3 class="r-preport__h" id="t">Thấy gì</h3><ul class="r-preport__list">'
          '<li>Hộ dừng ở thiết lập vì <b>bảng giá</b> và <b>tài khoản ngân hàng tên hộ</b> — đều cần người hỗ trợ ngồi cùng hộ.</li>'
          '<li><b>Chữ ký số</b> đang chặn hoá đơn có mã cho 1 hộ — chờ chương trình chọn nhà cung cấp (Câu 2).</li>'
          '<li>Kỳ thuế đầu tiên của đợt 1 là <b>Quý IV</b>, hạn 31/01/2027 — chưa có kết luận về tỷ lệ hoàn thành kỳ thuế.</li></ul>'
          '<h3 class="r-preport__h" id="d">Đề xuất</h3><ul class="r-preport__list"><li>Chốt nhà cung cấp chữ ký số trước 15/10.</li>'
          '<li>Thêm buổi hỗ trợ tại chỗ cho 2 hộ dừng ở thiết lập.</li><li>Đặt mục tiêu thành công sau khi có số đợt 1 ngày 30 (05/11).</li></ul>'
          '<div class="c-doc__foot"><span>Định nghĩa theo BRD §6 · không có dữ liệu tiền, đơn, khách của từng hộ · nhóm dưới 3 hộ được gộp</span></div></article></div>')
build('program-report', 'Chương trình · Báo cáo pilot', REPORT, 'home')
shell('program-report', 'report')
print('program: 3 screens')

"""v4.2 · Cài đặt → Thiết lập (BA UI-02..06, FLOWS.md ⓪ phần B; Kết nối moved to pages_connect*.py). An Nhiên data.
Writes setup-business.html, setup-data.html, setup-policy.html (owner view). The Kết nối screens are written by pages_connect*.py.
Usage: python3 pages_setup.py"""
from pages import build, ic, sign, subnav, annhien, SCREENS

SIM = '<span class="c-sim">Mô phỏng</span>'


def sub(cur):
    return subnav('Cài đặt', [('Sẵn sàng', 'readiness.html'), ('Hộ & mô hình', 'setup-business.html'), ('Dữ liệu nền', 'setup-data.html'),
                              ('Vai trò & duyệt', 'setup-policy.html'), ('Tính năng', 'settings-features.html'),
                              ('Hiển thị', 'settings-display.html')], cur)


def finish(name, owner=False):
    p = SCREENS / f'{name}.html'
    annhien(p)
    s = p.read_text().replace('class="c-nav__item" href="settings-users.html"', 'class="c-nav__item" href="readiness.html"')
    s = s.replace('class="c-nav__item" href="invoices.html"', 'class="c-nav__item" href="period.html"')
    if owner:
        s = s.replace('Nguyễn Minh Khoa · Người vận hành', 'Phạm Thị An · Chủ hộ').replace('<span class="c-avatar__face" aria-hidden="true">K', '<span class="c-avatar__face" aria-hidden="true">A')
    p.write_text(s)


def gi(tone, icon, st, t, m, act='', href='#'):
    a = f'<a class="c-btn" href="{href}">{act}</a>' if act else ''
    return (f'<li class="r-gate__i r-gate__i--{tone}"><span class="r-gate__b"><b>{t}</b>'
            + (f'<small><span class="r-gate__st">{st}</span> · {m}</small></span>' if st else f'<small>{m}</small></span>') + f'<span class="r-gate__amt"></span><span class="r-gate__act">{a}</span></li>')


def head(title, state, subline, primary):
    return (f'<div class="r-page-head"><div><h1 class="r-page-head__title">{title} {state}</h1><p class="c-sub">{subline}</p></div>'
            f'<div class="r-page-head__acts">{primary}</div></div>')


# ---------------- business profile & model ----------------
def chk(on, t, m, plan=''):
    return (f'<button class="c-option{" c-option--on" if on else ""}" type="button" role="checkbox" aria-checked="{"true" if on else "false"}">'
            f'<span class="c-option__box" aria-hidden="true">{ic("i-check") if on else ""}</span><span class="c-option__body"><strong class="c-option__title">{t}</strong>'
            f'<span class="c-option__meta">{m}</span>' + (f'<span class="r-model__plan">{plan}</span>' if plan else '') + '</span></button>')


BIZ = (f'\n      {sub("Hộ & mô hình")}\n      '
       + head('Hộ & mô hình kinh doanh', sign('ok', 'i-check', 'Đủ dữ liệu'), 'Lưu = tính lại Sẵn sàng · không mất dữ liệu',
              '<button class="c-btn c-btn--act" type="button">Lưu</button>')
       + '<div class="page"><div class="r-detail__grid r-detail--calm"><div class="stack">'
       '<section class="c-card" aria-labelledby="sl"><div class="c-card__head"><h2 class="c-card__title" id="sl">Chị bán thế nào?</h2><span class="u-meta">chọn mọi cách đang dùng</span></div>'
       '<div class="c-options r-model" role="group" aria-labelledby="sl">'
       + chk(True, 'Khách đến mua tại chỗ', 'trả tiền mặt hoặc QR', 'thêm: bán nhanh, hoá đơn ngay khi giao')
       + chk(True, 'Khách sỉ, khách sạn, nhà hàng', 'đặt qua Zalo, giá riêng, ghi nợ', 'thêm: bảng giá riêng, hoá đơn có mã, cách giao')
       + chk(False, 'Online, trên sàn', 'Shopee, TikTok Shop…', 'nếu chọn: kênh bán, đối chiếu tiền sàn')
       + '</div></section>'
       '<section class="c-card" aria-labelledby="src"><div class="c-card__head"><h2 class="c-card__title" id="src">Hàng từ đâu?</h2></div>'
       '<div class="c-options r-model" role="group" aria-labelledby="src">'
       + chk(True, 'Mua về bán lại', 'bò một nắng từ Krông Pa, muối kiến vàng từ HTX', 'thêm: nhà cung cấp, nhận hàng, trả tiền mua')
       + chk(False, 'Tự làm, chế biến', 'chưa có trong bản này · OPC ghi như hàng mua về', '')
       + '</div></section></div>'
       '<aside class="r-tower__detail" aria-labelledby="pf"><h2 class="r-tower__t" id="pf">Hồ sơ hộ</h2>'
       '<p class="r-trust r-trust--gate">' + ic('i-search') + '<span><b>OPC tra từ mã số thuế</b> · Kết nối tra cứu · 01/07 — chị An xác nhận</span></p>'
       '<dl class="c-kv"><dt>Tên hộ</dt><dd>Hộ kinh doanh Đặc sản Cao Nguyên An Nhiên</dd><dt>MST</dt><dd>5901234567</dd><dt>Chủ hộ</dt><dd>Phạm Thị An · xác minh L1</dd>'
       '<dt>Địa chỉ</dt><dd>Pleiku, Gia Lai</dd><dt>Ngành nghề</dt><dd>bán buôn, bán lẻ thực phẩm</dd><dt>Doanh thu 2026</dt><dd>1.284.500.000 ₫ · trên 1 tỷ</dd>'
       '<dt>Kỳ khai thuế</dt><dd>theo quý</dd></dl>'
       '<p class="c-sub">Sai thông tin? Sửa ở cơ quan thuế rồi tra lại</p>'
       f'<p><button class="c-btn c-btn--quiet" type="button">{ic("i-search")}Tra lại</button></p></aside></div></div>')
build('setup-business', 'Cài đặt · Hộ & mô hình', BIZ, 'settings')
finish('setup-business')

# ---------------- base data ----------------
who = lambda n, m: f'<td class="c-table__cell--main c-table__who"><b>{n}</b><small>{m}</small></td>'
num = lambda v: f'<td class="c-table__num">{v}</td>'
DROWS = ''.join([
    '<tr class="c-table__row--you">' + who('Khách hàng', 'Sunrise Hotel · Nhà hàng Phố Núi · Homestay Mây Ngàn') + num('3')
    + f'<td>{sign("you", "i-alert", "1 cần sửa")}<small class="r-stock__note">Homestay chưa có email nhận hoá đơn</small></td><td class="c-table__cell--end"><a class="c-btn" href="#">Sửa</a></td></tr>',
    '<tr>' + who('Hàng hoá & bảng giá', 'bò một nắng 500g, muối kiến vàng 100g · giá lẻ + giá khách sạn') + num('2')
    + f'<td>{sign("pass", "i-check", "Đạt")}</td><td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
    '<tr>' + who('Hạn dùng', 'bò một nắng, muối kiến vàng · theo dõi khi nhận hàng') + num('2')
    + f'<td>{sign("pass", "i-check", "Đạt")}</td><td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="stock.html">Xem</a></td></tr>',
    '<tr>' + who('Nhà cung cấp', 'HTX Cao Nguyên · Bao bì Phú Mỹ · Điện lực Gia Lai') + num('3')
    + f'<td>{sign("pass", "i-check", "Đạt")}</td><td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
    '<tr>' + who('Tồn đầu kỳ theo lô', 'đếm 01/07 · khớp kiểm kê 30/09') + num('5 lô')
    + f'<td>{sign("pass", "i-check", "Đạt")}</td><td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="stock.html">Xem</a></td></tr>',
    '<tr>' + who('Công nợ đầu kỳ', 'phải thu, phải trả lúc bắt đầu dùng OPC') + num('0')
    + f'<td>{sign("pass", "i-check", "Đạt")}<small class="r-stock__note">không có nợ cũ lúc 01/07</small></td><td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
])
DATA = (f'\n      {sub("Dữ liệu nền")}\n      '
        + head('Dữ liệu nền', '', '6 nhóm · 1 cần sửa · OPC kiểm tra mỗi khi nhập thêm',
               f'<a class="c-btn c-btn--act" href="#">{ic("i-plus")}Nhập dữ liệu</a>')
        + '<div class="page"><div class="c-table__scroll" tabindex="0" role="region" aria-label="Dữ liệu nền"><table class="c-table c-table--stack">'
        '<thead><tr><th scope="col">Nhóm</th><th scope="col" class="c-table__num">Số lượng</th><th scope="col">Kiểm tra</th><th scope="col"><span class="u-sr">Việc</span></th></tr></thead>'
        f'<tbody>{DROWS}</tbody></table></div>'
        '<section class="c-card r-import" aria-labelledby="im"><div class="c-card__head"><h2 class="c-card__title" id="im">Nhập cách nào cũng được</h2></div><ul class="r-import__list">'
        f'<li class="r-import__best">{ic("i-photo")}<b>Chụp ảnh <span class="c-option__tag c-option__tag--best">nhanh nhất</span></b><span>bảng giá, sổ tay, danh sách khách · Trợ lý đọc, chị xem lại từng dòng</span></li>'
        f'<li>{ic("i-download")}<b>File Excel</b><span>mẫu có sẵn · OPC báo dòng nào thiếu hoặc trùng</span></li>'
        f'<li>{ic("i-search")}<b>Gõ mã số thuế</b><span>khách, nhà cung cấp tự điền tên, địa chỉ</span></li>'
        f'<li>{ic("i-help")}<b>Nhân viên OPC nhập giúp</b><span>khi ngồi cùng hộ · ghi tên người nhập</span></li></ul></section></div>')
build('setup-data', 'Cài đặt · Dữ liệu nền', DATA, 'settings')
finish('setup-data')


# ---------------- roles & approval policy (owner) ----------------
ROLES = ('<div class="c-table__scroll" tabindex="0" role="region" aria-label="Người dùng và vai trò"><table class="c-table c-table--stack r-roster">'
         '<thead><tr><th scope="col">Người</th><th scope="col">Vai trò</th><th scope="col">Làm được</th></tr></thead><tbody>'
         '<tr>' + who('Phạm Thị An', 'chủ hộ · xác minh L1') + '<td>Chủ hộ</td><td>mọi việc · duyệt thuế, tiền, người dùng</td></tr>'
         '<tr>' + who('Nguyễn Minh Khoa', 'con · 0905 xxx 214') + '<td>Người vận hành</td><td>bán, mua, kho, gán tiền</td></tr>'
         '<tr>' + who('Hạnh', 'ca sáng') + '<td>Thu ngân</td><td>quầy, đóng ca, hoá đơn quầy</td></tr>'
         '<tr>' + who('anh Hùng', 'không cần tài khoản') + '<td>Người giao</td><td>chỉ mở link giao hàng của từng đơn</td></tr>'
         '<tr>' + who('chị Lan', f'kế toán dịch vụ · {sign("unk", "i-clock", "uỷ quyền đến 31/12/2026")}') + '<td>Kế toán</td><td>xem sổ, lập nháp · không duyệt, không gửi</td></tr>'
         '</tbody></table></div>')


def rule(t, who_, val, note='', lock=False):
    n = f'<small>{note}</small>' if note else ''
    v = (ic('i-lock') + val) if lock else val
    return f'<li class="r-policy__r{" r-policy__r--lock" if lock else ""}"><span class="r-policy__t"><b>{t}</b>{n}</span><span class="r-policy__who">{who_}</span><span class="r-policy__v">{v}</span></li>'


AMT = lambda v: f'<label class="r-policy__amt"><span class="u-sr">Ngưỡng, từ 0 đến 20.000.000 đồng</span><input class="c-field__input" inputmode="numeric" value="{v}"><span>₫</span></label>'
POLICY = ('<ul class="r-policy">'
          + rule('Giao hàng khi tiền mới “Đã nhận · chờ xác minh”', 'trên ngưỡng → chị An xác nhận', AMT('2.000.000'), 'dưới ngưỡng thì giao luôn')
          + rule('Đơn do Agent soạn', 'chị An duyệt trước khi xác nhận', 'luôn', 'đơn chị tự tạo: không duyệt thêm')
          + rule('Nhận hàng thiếu, lệch chứng từ', 'chị An quyết', 'luôn')
          + rule('Kiểm kho lệch', 'cần lý do · chị An duyệt điều chỉnh', 'luôn')
          + rule('Đổi bảng giá, giá riêng theo khách', 'anh Khoa đề nghị · chị An duyệt', 'luôn', 'đơn đã xác nhận giữ giá cũ')
          + rule('Hoá đơn bán ra', 'phát hành khi Đã giao', 'luôn', 'bán nhanh: phát hành ngay khi giao')
          + rule('Khoá kỳ · xác nhận số liệu kê khai', 'chỉ chị An', 'không đổi được', 'gửi tờ khai, nộp thuế, chuyển tiền: chị làm ngoài OPC', lock=True)
          + '</ul>')
POL = (f'\n      {sub("Vai trò & duyệt")}\n      '
       + head('Vai trò & ngưỡng duyệt', '', '5 người · 9 quy tắc · đổi cần OTP của chị An',
              '<button class="c-btn c-btn--act" type="button">Lưu chính sách</button>')
       + '<div class="page"><div class="r-detail__grid r-detail--calm"><div class="stack">'
       '<section class="c-card" aria-labelledby="rl"><div class="c-card__head"><h2 class="c-card__title" id="rl">Ai làm được gì</h2>'
       f'<button class="c-btn c-btn--quiet" type="button">{ic("i-plus")}Mời người dùng</button></div>' + ROLES + '</section>'
       '<section class="c-card" aria-labelledby="pl"><div class="c-card__head"><h2 class="c-card__title" id="pl">Khi nào cần người duyệt</h2></div>' + POLICY + '</section></div>'
       '<aside class="r-tower__detail" aria-labelledby="th"><h2 class="r-tower__t" id="th">Ba vai ở mọi bước</h2><ul class="r-roles">'
       '<li><span class="c-tag">Trợ lý đề xuất</span><span>đọc tin, soạn, gợi ý · không tự duyệt</span></li>'
       '<li><span class="c-tag">OPC kiểm tra</span><span>chặn khi sai giá, tồn, nợ, thuế</span></li>'
       '<li><span class="c-tag">Người duyệt</span><span>chị An hoặc người được giao</span></li>'
       '<li><span class="c-tag">Kết nối</span><span>ngân hàng, hoá đơn, cổng thuế</span></li></ul>'
       '<p class="c-sub">Mọi quyết định ghi vào Nhật ký</p>'
       '<h2 class="r-tower__t r-rail__h2">Mẫu chính sách</h2><div class="c-seg" role="radiogroup" aria-label="Mẫu chính sách">'
       '<button class="c-seg__opt" type="button" role="radio" aria-checked="true">Mặc định</button><button class="c-seg__opt" type="button" role="radio" aria-checked="false">Chặt hơn</button></div>'
       '<p class="c-sub">“Chặt hơn”: mọi ghi nợ, giảm giá chờ chị An</p></aside></div></div>')
build('setup-policy', 'Cài đặt · Vai trò & duyệt', POL, 'settings')
finish('setup-policy', owner=True)
print('setup: 5 screens')

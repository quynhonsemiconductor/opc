"""v4.2 · Hàng hoá → Chế biến (BA UI-09, FLOWS.md ④). BA demo data (An Nhiên), today 06/10.
Writes production.html (orders list), production-new.html (plan LCB-0413: OPC computes materials, start blocked on
shortage), production-detail.html (LCB-0412 running), production-detail--finish.html (16:05: actual vs expected,
low yield needs a reason, new lot BMN-0412). Usage: python3 pages_production.py"""
from pages import build, ic, sign, subnav, annhien, SCREENS


def sub(cur='Chế biến'):
    return subnav('Hàng hoá', [('Danh sách & giá', 'products.html'), ('Tồn kho', 'stock.html'), ('Chế biến', 'production.html'),
                               ('Nhập hàng & chi phí', 'purchases.html'), ('Nhà cung cấp', 'suppliers.html')], cur)


def at(name, hhmm):
    """the shell clock for a state that happens later in the day"""
    p = SCREENS / f'{name}.html'
    s = p.read_text().replace('Đã lưu 10:45', f'Đã lưu {hhmm}').replace('Đã lưu · <b>10:45</b>', f'Đã lưu · <b>{hhmm}</b>')
    p.write_text(s)


who = lambda n, m: f'<td class="c-table__cell--main c-table__who"><b>{n}</b><small>{m}</small></td>'
td = lambda v, c='': f'<td{" class=" + chr(34) + c + chr(34) if c else ""}>{v}</td>'

num = lambda v: f'<td class="c-table__num">{v}</td>'
ROWS = ''.join([
    '<tr class="c-table__row--you">' + who('LCB-0413', 'Bò một nắng 500g · anh Khoa') + td('Thứ Năm 08/10', 'c-table__cell--hide') + num('<span class="r-dash">–</span> / 40') + td('BMN-0413', 'c-table__cell--hide')
    + td(sign('you', 'i-alert', 'Thiếu 28 kg thịt bò'))
    + '<td class="c-table__cell--end"><a class="c-btn" href="production-new.html">Xem</a></td></tr>',
    '<tr>' + who('LCB-0412', 'Bò một nắng 500g · anh Khoa') + td('hôm nay, xong ~16:00', 'c-table__cell--hide') + num('<span class="r-dash">–</span> / 40') + td('BMN-0412', 'c-table__cell--hide')
    + td(sign('wait', 'i-clock', 'Đang làm'))
    + '<td class="c-table__cell--end"><a class="c-btn" href="production-detail.html">Mở</a></td></tr>',
    '<tr>' + who('LCB-0410', 'Bò một nắng 500g · anh Khoa') + td('01/10', 'c-table__cell--hide') + num('<b>40</b> / 40') + td('BMN-0410', 'c-table__cell--hide')
    + td(sign('ok', 'i-check', 'Xong'))
    + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
    '<tr>' + who('<a href="stock-lot.html">LCB-0405</a>', 'Bò một nắng 500g · anh Khoa') + td('16/09', 'c-table__cell--hide') + num('<b>40</b> / 40') + td('BMN-0405', 'c-table__cell--hide')
    + td(sign('ok', 'i-check', 'Xong'))
    + '<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="#">Xem</a></td></tr>',
])
LIST = (f'\n      {sub()}\n      <div class="r-page-head"><div><h1 class="r-page-head__title">Chế biến</h1>'
        '<p class="c-sub">Tuần này 2 lệnh · 80 gói dự kiến</p></div>'
        f'<div class="r-page-head__acts"><a class="c-btn c-btn--act" href="production-new.html">{ic("i-plus")}Lập lệnh chế biến</a></div></div>'
        '<div class="page"><div class="c-table__scroll" tabindex="0" role="region" aria-label="Lệnh chế biến"><table class="c-table c-table--stack">'
        '<thead><tr><th scope="col">Lệnh</th><th scope="col">Ngày</th><th scope="col" class="c-table__num">Gói ra / dự kiến</th><th scope="col">Lô</th><th scope="col">Tình trạng</th><th scope="col"><span class="u-sr">Việc</span></th></tr></thead>'
        f'<tbody>{ROWS}</tbody></table></div></div>')
build('production', 'Hàng hoá · Chế biến', LIST, 'goods')
annhien(SCREENS / 'production.html')


# ---------------- new order: OPC computes materials, start blocked on shortage ----------------
def field(label, value, suffix='', btn=False):
    if btn:
        return (f'<div class="c-field"><span class="c-field__label">{label}</span>'
                f'<button class="c-btn r-capture__pick" type="button" aria-haspopup="listbox">{value}{ic("i-chev")}</button></div>')
    sx = f'<span class="c-field__suffix">{suffix}</span>' if suffix else ''
    return (f'<label class="c-field"><span class="c-field__label">{label}</span><span class="c-field__control">'
            f'<input class="c-field__input" value="{value}"{" inputmode=" + chr(34) + "numeric" + chr(34) if suffix else ""}>{sx}</span></label>')


MAT = ('<div class="c-table__scroll" tabindex="0" role="region" aria-label="Nguyên liệu cần"><table class="c-table c-table--stack r-mat">'
       '<thead><tr><th scope="col">Nguyên liệu</th><th scope="col" class="c-table__num">Cần</th><th scope="col" class="c-table__num">Khả dụng</th><th scope="col">Kết quả</th></tr></thead><tbody>'
       '<tr class="c-table__row--you">' + who('Thịt bò tươi', 'lô TB-0998 · đông lạnh') + '<td class="c-table__num"><b>34 kg</b></td><td class="c-table__num r-mat__have">6 kg</td>'
       + td(sign('err', 'i-x', '<b>Thiếu 28 kg</b>') + '<a class="r-mat__cure" href="purchase-receive.html">35 kg đã về · MH-0118' + ic('i-chev-r') + '</a>') + '</tr>'
       '<tr>' + who('Gia vị ướp', 'lô GV-0908') + '<td class="c-table__num"><b>2 gói</b></td><td class="c-table__num">54 gói</td>'
       + td(sign('ok', 'i-check', 'Đủ')) + '</tr></tbody></table></div>')
NEW = (f'\n      {sub()}\n      <div class="page"><nav class="c-crumbs" aria-label="Đường dẫn"><a href="production.html">Chế biến</a><span aria-current="page">LCB-0413</span></nav>'
       '<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">Lệnh chế biến LCB-0413 ' + sign('pend', 'i-clock', 'Nháp') + '</h1>'
       '<p class="r-detail__fig"><span class="c-sub">Chưa trừ kho gì cho tới khi bắt đầu</span></p></div></div>'
       '<div class="r-detail__grid r-detail--calm"><div class="stack">'
       '<section class="c-card" aria-labelledby="w"><div class="c-card__head"><h2 class="c-card__title" id="w">Làm gì</h2></div><div class="r-form2">'
       + field('Thành phẩm', 'Bò một nắng 500g', btn=True) + field('Số lượng', '40', 'gói')
       + field('Ngày làm', 'Thứ Năm 08/10', btn=True) + field('Người làm', 'anh Khoa', btn=True) + '</div></section>'
       '<section class="c-card" aria-labelledby="m"><div class="c-card__head"><h2 class="c-card__title" id="m">Nguyên liệu</h2></div>'
       '<p class="r-trace__sum"><span class="c-tag">OPC kiểm tra</span><span>Tính theo 3 lần gần nhất: 34 kg thịt + 2 gói gia vị → 39–40 gói</span></p>'
       + MAT + '</section>'
       '<div class="c-decide__acts r-form__acts"><p class="c-decide__result">Lưu nháp = chưa trừ kho. Bắt đầu = xuất nguyên liệu, trừ kho một lần · 08/10 OPC nhắc anh Khoa</p>'
       f'<button class="c-btn c-btn--act" type="button" aria-disabled="true">{ic("i-lock")}Bắt đầu · thiếu 28 kg</button>'
       '<button class="c-btn" type="button">Lưu lệnh nháp</button></div>'
       '</div><aside class="r-tower__detail r-rail--quiet" aria-labelledby="out"><h2 class="r-tower__t" id="out">Sẽ ra</h2>'
       '<p class="r-rail__lot">Lô mới <b>BMN-0413</b></p><dl class="c-kv"><dt>Hạn dùng</dt><dd>60 ngày từ ngày làm · 07/12</dd><dt>Dùng cho</dt><dd>Quầy và đơn mới · tồn bò một nắng thường hết sau ~10 ngày</dd></dl>'
       '</aside></div></div>')
build('production-new', 'Chế biến · Lệnh mới', NEW, 'goods')
annhien(SCREENS / 'production-new.html')


# ---------------- running / finish ----------------
STAGES = ['Nháp', 'Xuất nguyên liệu', 'Đang làm', 'Ghi kết quả', 'Nhập kho']


def journey(now):
    out = []
    for i, s in enumerate(STAGES):
        cls = 'c-journey__s' + (' c-journey__s--done' if i < now else ' c-journey__s--now' if i == now else '')
        cur = ' aria-current="step"' if i == now else ''
        st = ' — xong' if i < now else ' — đang ở đây' if i == now else ''
        out.append(f'<li class="{cls}"{cur}>{s}<span class="u-sr">{st}</span></li>')
    return '<ol class="c-journey" aria-label="Lệnh đang ở đâu">' + ''.join(out) + '</ol>'


def step(kind, src, time, what, detail=''):
    d = f'<span class="c-timeline__who">{detail}</span>' if detail else ''
    return (f'<li class="c-timeline__item c-timeline__item--{kind}"><span class="c-timeline__time">{time}</span>'
            f'<span class="c-timeline__dot" aria-hidden="true"></span><span class="c-timeline__body">'
            f'<span class="c-timeline__src">{src}</span><span class="c-timeline__what">{what}</span>{d}</span></li>')


def tl(finish):
    return ('<ol class="c-timeline" aria-label="Diễn biến lệnh">'
            + (step('now', 'Anh Khoa', '16:05', 'Ghi kết quả', 'đang nhập') if finish else '')
            + step('ok', 'OPC kiểm tra', '07:30', 'Trừ kho nguyên liệu một lần', 'đủ tồn · không âm kho')
            + step('ok', 'Anh Khoa', '07:30', 'Bắt đầu, xuất nguyên liệu')
            + step('ok', 'Anh Khoa', '05/10', 'Lập lệnh 40 gói', 'OPC tính nguyên liệu theo 3 lần gần nhất')
            + '</ol>')


ISSUED = ('<div class="c-table__scroll" tabindex="0" role="region" aria-label="Nguyên liệu đã xuất"><table class="c-table c-table--stack">'
          '<thead><tr><th scope="col">Nguyên liệu</th><th scope="col" class="c-table__num">Đã xuất</th></tr></thead><tbody>'
          '<tr>' + who('Thịt bò tươi', 'lô TB-1005 · MH-0114, nhận 05/10') + '<td class="c-table__num">34 kg</td></tr>'
          '<tr>' + who('Gia vị ướp', 'lô GV-0908 · MH-0109') + '<td class="c-table__num">2 gói</td></tr></tbody></table></div>')


def head(state, primary, subline, fig='', meta=''):
    meta = f'<p class="c-sub r-detail__meta">{meta}</p>' if meta else ''
    f = f'<b class="c-figure">{fig}</b>' if fig else ''
    return (f'\n      {sub()}\n      <div class="page"><nav class="c-crumbs" aria-label="Đường dẫn"><a href="production.html">Chế biến</a><span aria-current="page">LCB-0412</span></nav>'
            '<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">LCB-0412 · Bò một nắng 500g ' + state + '</h1>'
            f'<p class="r-detail__fig">{f}<span class="c-sub">{subline}</span></p>{meta}</div><div class="r-detail__acts">{primary}</div></div>')


RUN = (head(sign('wait', 'i-clock', 'Đang làm'), '<a class="c-btn c-btn--act" href="production-detail--finish.html">Ghi kết quả</a>',
            'dự kiến · thường 39–40 từ 34 kg', '40 gói', 'anh Khoa · bắt đầu 07:30 · xong khoảng 16:00')
       + journey(2) + '<div class="r-detail__grid r-detail--calm"><div class="stack">'
       '<section class="c-card" aria-labelledby="is"><div class="c-card__head"><h2 class="c-card__title" id="is">Nguyên liệu đã xuất</h2></div>' + ISSUED
       + '<p class="c-sub">Kho nguyên liệu đã trừ lúc 07:30. Phần không dùng hết thì ghi lại khi xong, OPC nhập lại kho.</p></section>'
       '<section class="c-card" aria-labelledby="ex"><div class="c-card__head"><h2 class="c-card__title" id="ex">Thành phẩm dự kiến</h2></div>'
       '<dl class="c-kv"><dt>Lô mới</dt><dd>BMN-0412 · hạn 05/12 (60 ngày)</dd><dt>Vào kho</dt><dd>khi anh Khoa ghi kết quả — quầy bán được ngay</dd></dl></section></div>'
       '<aside class="r-tower__detail" aria-labelledby="t"><h2 class="r-tower__t" id="t">Diễn biến</h2>' + tl(False) + '</aside></div></div>')
build('production-detail', 'Chế biến · LCB-0412', RUN, 'goods')
annhien(SCREENS / 'production-detail.html')


def rline(name, meta, got, unit, diff='', reason=None):
    ok = not diff
    mark = f'<span class="r-pick__chk r-pick__chk--ok" aria-hidden="true">{ic("i-check")}</span>' if ok else f'<span class="r-pick__chk r-pick__chk--warn" aria-hidden="true">{ic("i-alert")}</span>'
    d = '<span class="r-count__d">khớp</span>' if ok else f'<span class="r-count__d r-count__d--off">{diff}</span>'
    row = (f'<li class="r-count__l{" r-count__l--ok" if ok else " r-count__l--off"}">{mark}<span class="r-pick__name"><b>{name}</b><small>{meta}</small></span>'
           f'<label class="r-count__in"><span class="u-sr">{name}</span><input class="c-field__input" inputmode="decimal" value="{got}"><span class="r-count__u">{unit}</span></label>{d}')
    if reason:
        opts = ''.join(f'<button class="c-seg__opt" type="button" role="radio" aria-checked="false">{o}</button>' for o in reason)
        row += (f'<div class="r-count__why"><p class="r-count__hint" id="need"><span class="c-tag">OPC kiểm tra</span>Thấp hơn mức thường 39–40 → chọn lý do để nhập kho</p>'
                f'<div class="c-seg" role="radiogroup" aria-label="Lý do sản lượng thấp" aria-describedby="need" aria-required="true">{opts}</div>'
                '<label class="c-field"><span class="u-sr">Ghi chú</span><span class="c-field__control"><input class="c-field__input" placeholder="Ghi chú (tuỳ chọn)"></span></label></div>')
    return row + '</li>'


FIN = (head(sign('you', 'i-alert', 'Chờ ghi kết quả'), '', 'anh Khoa · bắt đầu 07:30 · sấy xong 16:00')
       + journey(3) + '<div class="r-detail__grid r-detail--calm"><div class="stack">'
       '<section class="c-card r-count__card" aria-labelledby="rs"><div class="c-card__head"><h2 class="c-card__title" id="rs">Kết quả · 1 dòng khác mức thường</h2></div>'
       '<ul class="r-count" aria-label="Thực dùng và sản lượng">'
       + rline('Sản lượng · bò một nắng 500g', 'dự kiến 40 gói', '38', 'gói', '−2 gói', ['Sấy quá khô', 'Bỏ phần hỏng', 'Cân sai', 'Khác'])
       + rline('Thịt bò tươi đã dùng', 'lô TB-1005 · đã xuất 34 kg', '34', 'kg')
       + rline('Gia vị ướp đã dùng', 'lô GV-0908 · đã xuất 2 gói', '2', 'gói')
       + '</ul>'
       '<button class="c-switch c-switch--row r-fin__print" type="button" role="switch" aria-checked="true"><span class="c-switch__label">In 38 tem lô BMN-0412<span class="c-switch__sub">sau khi nhập kho · tem có mã truy xuất, chỉ công khai khi chị bật</span></span><span class="c-switch__track" aria-hidden="true"></span></button>'
       '<div class="r-count__foot"><p class="c-decide__result">Nhập kho = tạo lô <b>BMN-0412</b> · hạn 05/12 · quầy và đơn mới bán được ngay</p>'
       f'<div class="c-decide__acts"><button class="c-btn c-btn--act" type="button" aria-disabled="true">{ic("i-lock")}Nhập kho 38 gói · cần lý do sản lượng thấp</button>'
       '<button class="c-btn" type="button">Lưu, ghi tiếp sau</button></div></div></section></div>'
       '<aside class="r-tower__detail" aria-labelledby="t"><h2 class="r-tower__t" id="t">Diễn biến</h2>' + tl(True) + '</aside></div></div>')
build('production-detail--finish', 'Chế biến · Ghi kết quả LCB-0412', FIN, 'goods')
annhien(SCREENS / 'production-detail--finish.html')
at('production-detail--finish', '16:05')
print('production: 4 screens')

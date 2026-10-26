"""v4.3 · Sổ & thuế → Hoá đơn, Nhật ký + phiếu quầy, rebuilt in An Nhiên data (replaces pages_books.py/pages_detail.py
outputs): invoices, invoices--accountant (chị Lan, delegated), invoice-detail (HĐ 00000231 · Sunrise · có mã),
receipt (phiếu DH-2053), audit (UI-19: before/after, source, event id). Decisions: mẫu số 2 (hoá đơn bán hàng),
two series — Hilo máy tính tiền 2C26MAN / X Invoice có mã 2C26TAN; "Chưa rõ kết quả" never auto-resent; corrections go
through the provider portal. Usage: python3 pages_books43.py"""
from pages import build, ic, sign, subnav, SCREENS, CUR

SUB = lambda cur: subnav('Sổ & thuế', [('Kỳ thuế', 'period.html'), ('Sổ sách', 'books.html'), ('Hoá đơn', 'invoices.html'), ('Nhật ký', 'audit.html')], cur)
who = lambda n, m: f'<td class="c-table__cell--main c-table__who"><b>{n}</b><small>{m}</small></td>'
num = lambda v: f'<td class="c-table__num c-table__cell--end">{v}</td>'
OK = sign('pass', 'i-check', 'Có mã')


def inv_row(no, meta, buyer, st, amt, href='invoice-detail.html', you=False):
    return (f'<tr{" class=" + chr(34) + "c-table__row--you" + chr(34) if you else ""}>' + who(no, meta) + f'<td>{buyer}</td><td>{st}</td>' + num(amt)
            + f'<td class="c-table__cell--end"><a class="c-btn c-btn--quiet" href="{href}">Xem</a></td></tr>')


def table(rows, label):
    return (f'<div class="c-table__scroll" tabindex="0" role="region" aria-label="{label}"><table class="c-table c-table--stack">'
            '<thead><tr><th scope="col">Hoá đơn</th><th scope="col">Người mua</th><th scope="col">Mã CQT</th><th scope="col" class="c-table__num">Tổng</th>'
            f'<th scope="col"><span class="u-sr">Xem</span></th></tr></thead><tbody>{rows}</tbody></table></div>')


def listhead(k, fig, parts, aria, due_k, due_v, href):
    bar = ''.join(f'<i class="c-split__{c}" style="flex:{n}"></i>' for c, n, _ in parts)
    sub = ' · '.join(t for _, _, t in parts)
    return (f'<section class="r-listhead" aria-label="Hoá đơn trong kỳ"><div class="r-listhead__fig"><span class="c-stat__label">{k}</span><b class="c-figure">{fig}</b></div>'
            f'<div class="r-listhead__bar"><div class="c-split__bar" role="img" aria-label="{aria}">{bar}</div><p class="c-sub">{sub}</p></div>'
            f'<a class="r-listhead__due" href="{href}"><span class="c-stat__label">{due_k}</span><span class="r-listhead__duev">{due_v}</span>{ic("i-chev-r")}</a></section>')


def tabs(items):
    return ('<div class="c-tabs" role="tablist" aria-label="Lọc theo trạng thái">' + ''.join(
        f'<button class="c-tabs__tab{" c-tabs__tab--you" if you else ""}" role="tab" aria-selected="{"true" if sel else "false"}" type="button">{t} <span class="c-tabs__count">{n}</span></button>'
        for t, n, sel, you in items) + '</div>')


UNK = sign('unk', 'i-clock', 'Chưa rõ kết quả')
ROWS = ''.join([
    inv_row('DH-2047 · chưa có số', 'X Invoice · 06/10 10:11 · chị An bấm phát hành', 'Nhà hàng Phố Núi', UNK, '1.840.000 ₫', 'approvals--error.html', you=True),
    inv_row('00000231', 'DH-2049 · 06/10 08:41 · có mã', 'Sunrise Hotel', OK, '4.550.000 ₫'),
    inv_row('00000230', 'DH-2045 · 06/10 07:42 · có mã', 'Homestay Mây Ngàn', OK, '390.000 ₫'),
    inv_row('00001288', 'DH-2048 · 06/10 09:05 · máy tính tiền', 'Khách lẻ', OK, '195.000 ₫', 'receipt.html'),
    inv_row('00001281', 'DH-2046 · 06/10 07:50 · máy tính tiền', 'Chị Hoa', OK, '260.000 ₫', 'receipt.html'),
    inv_row('00000228', 'DH-2044 · 05/10 · có mã', 'Nhà hàng Phố Núi', OK, '3.900.000 ₫'),
    inv_row('00000226', 'DH-2041 · 03/10 · có mã', 'Homestay Mây Ngàn', OK, '2.400.000 ₫'),
])
BANNER = ('<div class="c-banner c-banner--pend" role="status"><span class="c-banner__pic">' + ic('i-clock') + '</span><span class="c-banner__text">'
          '<strong class="c-banner__title">Hoá đơn DH-2047 chưa rõ kết quả · từ 10:12</strong><span class="c-banner__body">X Invoice không trả lời. OPC không tự gửi lại để tránh hai hoá đơn trùng; đang hỏi lại, lần sau 11:15.</span></span>'
          f'<span class="c-banner__actions"><a class="c-btn" href="approvals--error.html">Xem</a></span></div>')
INV = (f'\n      {SUB("Hoá đơn")}\n      <div class="r-page-head"><div><h1 class="r-page-head__title">Hoá đơn</h1>'
       '<p class="c-sub">Mẫu số 2 · hoá đơn bán hàng · quầy: Hilo máy tính tiền (2C26MAN) · khách sỉ: X Invoice có mã (2C26TAN)</p></div>'
       f'<div class="r-page-head__acts"><a class="c-btn" href="#">{ic("i-download")}Xuất Excel</a></div></div>'
       '<div class="page">'
       + listhead('Tháng 10/2026 · 41 hoá đơn', f'24.610.000{CUR}', [('ok', 40, 'có mã 40'), ('pend', 1, 'chưa rõ kết quả 1')],
                  'Có mã 40 hoá đơn, chưa rõ kết quả 1 hoá đơn', 'Chưa rõ · DH-2047', '1.840.000 ₫', 'approvals--error.html')
       + BANNER + tabs([('Cần xem', 1, False, True), ('Có mã', 40, False, False), ('Bị từ chối', 0, False, False), ('Tất cả', 41, True, False)])
       + '<section class="c-card r-listcard" aria-label="Danh sách hoá đơn">' + table(ROWS, 'Hoá đơn tháng 10') + '</section>'
       '<p class="c-sub">Sửa hoặc thay thế một hoá đơn đã có mã: làm trên cổng nhà cung cấp (Hilo, X Invoice); OPC ghi lại số hoá đơn mới và liên kết với đơn.</p></div>')
build('invoices', 'Sổ & thuế · Hoá đơn', INV, 'books')

# ---------------- accountant (chị Lan, delegated): Tháng 9, compact ----------------
ACC_ROWS = ''.join([
    inv_row('00001172', 'quầy · 30/09 18:02 · máy tính tiền', 'Khách lẻ', UNK, '640.000 ₫', 'period.html', you=True),
    inv_row('00001171', 'quầy · 30/09 17:44 · máy tính tiền', 'Khách lẻ', OK, '260.000 ₫', 'receipt.html'),
    inv_row('00001170', 'quầy · 30/09 17:12 · máy tính tiền', 'Khách lẻ', OK, '325.000 ₫', 'receipt.html'),
    inv_row('00000201', 'DH-2036 · 28/09 · lập trên X Invoice, OPC chưa kéo về', 'Homestay Mây Ngàn', sign('you', 'i-alert', 'Chưa có trong OPC'), '1.300.000 ₫', 'period.html'),
    inv_row('00000199', 'DH-2031 · 25/09 · có mã', 'Nhà hàng Phố Núi', OK, '690.000 ₫'),
    inv_row('00000193', '10/09 · có mã', 'Sunrise Hotel', OK, '3.200.000 ₫'),
    inv_row('00000187', '09/09 · có mã', 'Sunrise Hotel', OK, '5.200.000 ₫'),
])
ACC = (f'\n      {SUB("Hoá đơn")}\n      <div class="r-page-head"><div><h1 class="r-page-head__title">Hoá đơn · Tháng 9/2026</h1>'
       '<p class="c-sub">Chị Lan · kế toán dịch vụ · uỷ quyền đến 31/12/2026 · xem và lập nháp, không phát hành</p></div>'
       f'<div class="r-page-head__acts"><a class="c-btn c-btn--act" href="#">{ic("i-download")}Xuất Excel cho kế toán</a></div></div>'
       '<div class="page">'
       + listhead('Tháng 9 · 236 hoá đơn', f'118.200.000{CUR}', [('ok', 234, 'có mã 234'), ('pend', 1, 'chưa rõ 1'), ('you', 1, 'chưa có trong OPC 1')],
                  'Có mã 234, chưa rõ kết quả 1, chưa có trong OPC 1', 'Đối chiếu Quý III', '5 việc · hạn 31/10', 'period.html')
       + tabs([('Cần xem', 2, False, True), ('Có mã', 234, False, False), ('Tất cả', 236, True, False)])
       + '<section class="c-card r-listcard" aria-label="Danh sách hoá đơn tháng 9">' + table(ACC_ROWS, 'Hoá đơn tháng 9') + '</section></div>')
build('invoices--accountant', 'Sổ & thuế · Hoá đơn (kế toán)', ACC, 'books', html_attrs='data-density="compact"')
p = SCREENS / 'invoices--accountant.html'
s = p.read_text().replace('Nguyễn Minh Khoa · Người vận hành', 'Chị Lan · Kế toán (uỷ quyền)').replace('<span class="c-avatar__face" aria-hidden="true">K', '<span class="c-avatar__face" aria-hidden="true">L')
import navtree
s = navtree.apply(s, 'books', 'invoices--accountant', role='accountant')   # v4.4: the accountant's rail
p.write_text(s)


# ---------------- invoice detail: 00000231 · Sunrise · có mã ----------------
def step(kind, src, time, what, detail=''):
    d = f'<span class="c-timeline__who">{detail}</span>' if detail else ''
    return (f'<li class="c-timeline__item c-timeline__item--{kind}"><span class="c-timeline__time">{time}</span><span class="c-timeline__dot" aria-hidden="true"></span>'
            f'<span class="c-timeline__body"><span class="c-timeline__src">{src}</span><span class="c-timeline__what">{what}</span>{d}</span></li>')


LINES = ('<div class="c-table__scroll" tabindex="0" role="region" aria-label="Hàng hoá trên hoá đơn"><table class="c-table c-table--stack">'
         '<thead><tr><th scope="col">Hàng hoá</th><th scope="col" class="c-table__num c-table__cell--hide">Số lượng</th><th scope="col" class="c-table__num c-table__cell--hide">Đơn giá</th><th scope="col" class="c-table__num">Thành tiền</th></tr></thead><tbody>'
         '<tr><td class="c-table__cell--main">Bò một nắng 500g<span class="c-table__phone"> · 15 × 230.000 ₫</span></td><td class="c-table__num c-table__cell--hide">15 gói</td><td class="c-table__num c-table__cell--hide">230.000 ₫</td><td class="c-table__num c-table__cell--end">3.450.000 ₫</td></tr>'
         '<tr><td class="c-table__cell--main">Muối kiến vàng 100g<span class="c-table__phone"> · 20 × 55.000 ₫</span></td><td class="c-table__num c-table__cell--hide">20 hũ</td><td class="c-table__num c-table__cell--hide">55.000 ₫</td><td class="c-table__num c-table__cell--end">1.100.000 ₫</td></tr>'
         '</tbody></table></div>')
DOC = ('<article class="c-doc" aria-labelledby="dt"><header class="c-doc__head"><div><h2 class="c-doc__title" id="dt">Hoá đơn bán hàng</h2><p class="c-sub">Mẫu số 2 · có mã của cơ quan thuế</p></div>'
       '<span class="c-doc__no">Ký hiệu 2C26TAN<b>Số 00000231</b>06/10/2026 08:41</span></header>'
       '<div class="c-doc__party"><span class="c-doc__party-k">Người bán</span><strong>HỘ KINH DOANH ĐẶC SẢN CAO NGUYÊN AN NHIÊN</strong><span>MST 5901234567 · Pleiku, Gia Lai</span></div>'
       '<div class="c-doc__party"><span class="c-doc__party-k">Người mua</span><strong>Sunrise Hotel</strong><span>MST 5900987654 · đơn DH-2049 (định kỳ thứ Hai)</span></div>'
       + LINES + f'<div class="c-doc__total"><span>Tổng tiền thanh toán</span><b>4.550.000{CUR}</b></div><p>Bằng chữ: Bốn triệu năm trăm năm mươi nghìn đồng.</p>'
       '<div class="c-doc__foot"><span>Mã của cơ quan thuế (CQT): 00A1B2C3D4E5F6071829304A5B6C7D8E</span><span>Tra cứu tại hoadondientu.gdt.gov.vn</span></div></article>')
DET = (f'\n      {SUB("Hoá đơn")}\n      <div class="page"><nav class="c-crumbs" aria-label="Đường dẫn"><a href="invoices.html">Hoá đơn</a><span aria-current="page">00000231</span></nav>'
       '<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">Hoá đơn 00000231 ' + sign('ok', 'i-check', 'Có mã CQT') + '</h1>'
       f'<p class="r-detail__fig"><b class="c-figure">4.550.000{CUR}</b><span class="c-sub">Sunrise Hotel · DH-2049 · 06/10/2026 08:41 · X Invoice</span></p></div>'
       f'<div class="r-detail__acts"><button class="c-btn c-btn--act" type="button">{ic("i-send")}Gửi chị Mai qua Zalo OA</button><a class="c-btn" href="#">{ic("i-download")}Tải PDF</a></div></div>'
       '<div class="r-detail__grid r-detail--calm"><div class="stack">' + DOC + '</div>'
       '<aside class="r-tower__detail" aria-labelledby="hs"><h2 class="r-tower__t" id="hs">Diễn biến</h2><ol class="c-timeline c-timeline--quiet" aria-label="Diễn biến">'
       + step('ok', 'Kết nối · X Invoice', '08:41', 'Có mã của cơ quan thuế', 'sau 2 phút 40 giây')
       + step('ok', 'Chị An', '08:38', 'Phát hành hoá đơn', 'Trợ lý đề xuất sau khi giao · OPC kiểm tra giá, MST')
       + step('ok', 'Kết nối · MB', '08:41', 'Đã xác minh 4.550.000 ₫', 'Sunrise trả QR khi nhận hàng')
       + step('ok', 'Anh Hùng', '08:30', 'Giao xong DH-2049', 'chị Mai ký nhận')
       + '</ol><p class="c-sub">Sai thông tin? Điều chỉnh hoặc thay thế trên cổng X Invoice — OPC ghi lại hoá đơn mới và liên kết với đơn. OPC không tự huỷ hoá đơn.</p></aside></div></div>')
build('invoice-detail', 'Sổ & thuế · Hoá đơn 00000231', DET, 'books')

# ---------------- counter receipt DH-2053 ----------------
REC = ('\n      <div class="page"><nav class="c-crumbs" aria-label="Đường dẫn"><a href="orders.html">Đơn hàng</a><span aria-current="page">Phiếu DH-2053</span></nav>'
       '<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">Phiếu DH-2053 ' + sign('ok', 'i-check', 'Đã xác minh · QR') + '</h1>'
       f'<p class="r-detail__fig"><b class="c-figure">715.000{CUR}</b><span class="c-sub">hoá đơn máy tính tiền 00001291 · 06/10/2026 10:47 · Hạnh</span></p></div>'
       f'<div class="r-detail__acts"><button class="c-btn c-btn--act" type="button">{ic("i-print")}In phiếu</button><button class="c-btn" type="button">{ic("i-download")}Tải PDF</button><button class="c-btn" type="button">Gửi Zalo cho khách</button></div></div>'
       '<div class="r-detail__grid r-detail--calm"><article class="c-receipt" aria-label="Phiếu bán hàng DH-2053">'
       '<header class="c-receipt__shop"><strong>Đặc sản Cao Nguyên An Nhiên</strong><span>Pleiku, Gia Lai</span><span>MST 5901234567</span><span>06/10/2026 10:47</span></header>'
       '<ul class="c-receipt__lines"><li class="c-receipt__line"><span>Bò một nắng 500g</span><b>520.000 ₫</b><small>2 × 260.000 ₫</small></li>'
       '<li class="c-receipt__line"><span>Muối kiến vàng 100g</span><b>195.000 ₫</b><small>3 × 65.000 ₫</small></li></ul>'
       '<div class="c-receipt__total"><span>Tổng</span><b>715.000 ₫</b></div>'
       '<div class="c-receipt__foot"><span>Đã thanh toán QR · Hoá đơn 00001291</span><span>Mã tra cứu</span><span class="c-receipt__code">M1-26-AN7P4-00000001291</span>'
       '<img src="../../../system/assets/qr-demo.svg" alt="Mã QR tra cứu hoá đơn 00001291" width="96" height="96"><span>Cảm ơn quý khách — hẹn gặp lại!</span></div></article>'
       '<div class="stack"><section class="c-card" aria-labelledby="h-zalo"><div class="c-card__head"><h2 class="c-card__title" id="h-zalo">Tin Zalo khách sẽ nhận</h2></div>'
       '<div class="c-msgcard"><div class="c-msgcard__from"><span class="c-hh__mark" aria-hidden="true">AN</span><span>Đặc sản An Nhiên<small>qua Zalo OA</small></span></div>'
       '<div class="c-msgcard__body"><strong>Cảm ơn quý khách đã mua hàng</strong><dl class="c-kv"><dt>Đơn</dt><dd>DH-2053</dd><dt>Số tiền</dt><dd>715.000 ₫</dd><dt>Hoá đơn</dt><dd>00001291</dd></dl></div>'
       '<div class="c-msgcard__actions"><a href="#">Xem hoá đơn</a><a href="#">Quan tâm Zalo OA</a></div></div></section>'
       '<p class="c-sub">Khách nhận tin khi chị bấm Gửi Zalo — chỉ gửi được nếu khách đã quan tâm Zalo OA của hộ.</p></div></div></div>')
build('receipt', 'Đơn hàng · Phiếu DH-2053', REC, 'orders')


# ---------------- audit log (UI-19) ----------------
def ev(kind, time, what, by, src, eid, change=''):
    ch = f'<span class="r-audit__chg">{change}</span>' if change else ''
    return (f'<li class="c-timeline__item c-timeline__item--{kind}"><span class="c-timeline__time">{time}</span><span class="c-timeline__dot" aria-hidden="true"></span>'
            f'<span class="c-timeline__body"><span class="c-timeline__src">{by}</span><span class="c-timeline__what">{what}</span>{ch}'
            f'<span class="c-timeline__who">{src} · <span class="r-audit__id">mã {eid}</span></span></span></li>')


EVENTS = ('<ol class="c-timeline r-audit" aria-label="Nhật ký hôm nay, mới nhất trước">'
          + ev('ok', '10:47', 'Đã xác minh 715.000 ₫ · <a href="receipt.html">DH-2053</a>', 'Kết nối · MB qua Casso', 'khớp sao kê', 'EV-9F31', 'Tiền: Đã nhận · chờ xác minh → Đã xác minh')
          + ev('you', '10:44', 'Thu tiền DH-2053 = phát hành hoá đơn máy tính tiền 00001291', 'Hạnh · thu ngân', 'máy quầy', 'EV-9F2C', 'Đơn: Đang bán → Đã giao · kho: bò 26 → 24 khả dụng')
          + ev('err', '10:12', 'Phát hành hoá đơn DH-2047 → X Invoice không trả lời', 'Chị An · kết nối X Invoice', 'điện thoại chị An', 'EV-9E70', 'Hoá đơn: Nháp → Chưa rõ kết quả · không tự gửi lại')
          + ev('you', '09:15', 'Duyệt <a href="order-detail.html">DH-2052</a> do Agent soạn', 'Chị An · chủ hộ', 'điện thoại chị An', 'EV-9D02', 'Đơn: Đề xuất → Đã xác nhận · giữ 20 gói bò, 30 hũ muối')
          + ev('ai', '09:02', 'Soạn nháp DH-2052 từ tin Zalo OA của chị Mai', 'Agent', 'chưa có hiệu lực tới khi duyệt', 'EV-9CF1')
          + ev('ok', '08:41', 'Đã xác minh 4.550.000 ₫ · DH-2049', 'Kết nối · MB qua Casso', 'khớp sao kê', 'EV-9C88')
          + ev('you', '08:40', 'Nhận hàng MH-0118: đếm 45/50 hũ muối', 'Anh Khoa · vận hành', 'điện thoại anh Khoa', 'EV-9C80', 'Chưa nhập kho — chờ chị An xác nhận số thực nhận')
          + ev('ok', '07:30', 'Kiểm kho: bò một nắng 45/46 gói, 1 gói hỏng', 'Anh Khoa · vận hành', 'điện thoại anh Khoa', 'EV-9B41', 'Chờ chị An duyệt điều chỉnh')
          + ev('ok', '07:00', 'Mở ca sáng · tiền đầu ca 500.000 ₫', 'Hạnh · thu ngân', 'máy quầy', 'EV-9B10')
          + '</ol>')
FILT = ('<div class="r-audit__filters"><div class="c-seg" role="radiogroup" aria-label="Thời gian"><button class="c-seg__opt" type="button" role="radio" aria-checked="true">Hôm nay</button>'
        '<button class="c-seg__opt" type="button" role="radio" aria-checked="false">7 ngày</button><button class="c-seg__opt" type="button" role="radio" aria-checked="false">Tháng này</button></div>'
        '<label class="c-search r-audit__find">' + ic('i-search') + '<span class="u-sr">Tìm theo đối tượng</span><input class="c-search__input" type="search" placeholder="Đơn, hoá đơn, lô, người, mã sự kiện…"></label>'
        '<div class="c-filters" role="group" aria-label="Ai làm"><button class="c-filter" type="button" aria-pressed="true">Tất cả</button><button class="c-filter" type="button" aria-pressed="false">Người</button>'
        '<button class="c-filter" type="button" aria-pressed="false">Trợ lý</button><button class="c-filter" type="button" aria-pressed="false">OPC kiểm tra</button><button class="c-filter" type="button" aria-pressed="false">Kết nối</button></div></div>')
AUD = (f'\n      {SUB("Nhật ký")}\n      <div class="r-page-head"><div><h1 class="r-page-head__title">Nhật ký</h1><p class="c-sub">Thứ Ba, 06/10/2026 · 9 ghi nhận đến 10:47 · chỉ ghi thêm, không sửa hay xoá được</p></div>'
       f'<div class="r-page-head__acts"><a class="c-btn" href="#">{ic("i-download")}Xuất nhật ký</a></div></div>'
       '<div class="page">' + FILT + '<section class="c-card" aria-label="Nhật ký hôm nay">' + EVENTS + '</section>'
       '<p class="c-sub">Mỗi dòng ghi ai làm, lúc nào, từ đâu, trước → sau và lý do. Kế toán và chương trình chỉ xem phần được chị An cho phép.</p></div>')
build('audit', 'Sổ & thuế · Nhật ký', AUD, 'books')
print('books43: 5 screens')

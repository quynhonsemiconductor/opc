"""v4.2 · Order 360 (BA UI-11, FLOWS.md ②): one order's whole life on one page. BA demo data (An Nhiên).
Writes order-detail.html (DH-2052 Sunrise, approved + reserved, next: pick) and order-detail--invoice.html
(delivered, invoice proposed for the owner to issue). Replaces the v4.1 order-detail (pages_detail.py keeps
invoice-detail and receipt). Usage: python3 pages_order360.py"""
from pages import build, ic, sign, subnav, annhien, SCREENS

CUR = '<span class="u-cur">₫</span>'
STAGES = ['Nhận yêu cầu', 'Kiểm tra', 'Chị duyệt', 'Giữ hàng', 'Soạn', 'Giao', 'Hoá đơn', 'Tiền', 'Đóng đơn']


def journey(now, warn=()):
    out = []
    for i, s in enumerate(STAGES):
        cls = ['c-journey__s']
        if i < now: cls.append('c-journey__s--done')
        if i == now: cls.append('c-journey__s--now')
        if s in warn: cls.append('c-journey__s--warn')
        cur = ' aria-current="step"' if i == now else ''
        state = ' — xong' if i < now else ' — đang ở đây' if i == now else ''
        out.append(f'<li class="{" ".join(cls)}"{cur}>{s}<span class="u-sr">{state}</span></li>')
    return '<ol class="c-journey" aria-label="Đơn đang ở đâu">' + ''.join(out) + '</ol>'


def step(kind, src, time, what, detail=''):
    d = f'<span class="c-timeline__who">{detail}</span>' if detail else ''
    return (f'<li class="c-timeline__item c-timeline__item--{kind}"><span class="c-timeline__time">{time}</span>'
            f'<span class="c-timeline__dot" aria-hidden="true"></span><span class="c-timeline__body">'
            f'<span class="c-timeline__src">{src}</span><span class="c-timeline__what">{what}</span>{d}</span></li>')


def lines(extra_col):
    head = '<th scope="col">Lô</th>' if extra_col == 'lot' else '<th scope="col">Đã giao</th>'
    r1 = 'BMN-0405 · 20 gói' if extra_col == 'lot' else '20 gói'
    r2 = 'MKV-0921 · 30 hũ' if extra_col == 'lot' else '30 hũ'
    return ('<div class="c-table__scroll" tabindex="0" role="region" aria-label="Món trong đơn"><table class="c-table c-table--stack"><thead><tr>'
            f'<th scope="col">Món</th><th scope="col" class="c-table__num">SL</th>{head}<th scope="col" class="c-table__num">Thành tiền</th></tr></thead><tbody>'
            f'<tr><td class="c-table__cell--main">Bò một nắng 500g<small class="u-meta"> · 230.000 ₫/gói</small></td><td class="c-table__num">20</td><td>{r1}</td><td class="c-table__num">4.600.000 ₫</td></tr>'
            f'<tr><td class="c-table__cell--main">Muối kiến vàng 100g<small class="u-meta"> · 55.000 ₫/hũ</small></td><td class="c-table__num">30</td><td>{r2}</td><td class="c-table__num">1.650.000 ₫</td></tr>'
            '</tbody><tfoot><tr><th scope="row" colspan="3">Tổng · giá riêng khách sạn</th><td class="c-table__num"><b>6.250.000 ₫</b></td></tr></tfoot></table></div>')


def section(t, body, i):
    return f'<section class="c-card" aria-labelledby="{i}"><div class="c-card__head"><h2 class="c-card__title" id="{i}">{t}</h2></div>{body}</section>'


def head(state_html, primary, fig_sub):
    return (subnav('Bán', [('Yêu cầu', 'sales-inbox.html'), ('Đơn hàng', 'orders.html'), ('Giao hàng', 'delivery.html'), ('Khách hàng', 'customers.html')], 'Đơn hàng')
            + '<div class="page"><nav class="c-crumbs" aria-label="Đường dẫn"><a href="orders.html">Đơn hàng</a><span aria-current="page">DH-2052</span></nav>'
            + '<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">DH-2052 · Sunrise Hotel ' + state_html + '</h1>'
            + f'<p class="r-detail__fig"><b class="c-figure">6.250.000{CUR}</b><span class="c-sub">{fig_sub}</span></p></div>'
            + f'<div class="r-detail__acts">{primary}</div></div>')


TIMELINE_BASE = (step('ai', 'Trợ lý đề xuất', '09:02', 'Đọc tin Zalo OA của chị Mai', '20 gói bò, 30 hũ muối · trước 15:00')
                 + step('ok', 'OPC kiểm tra', '09:02', 'Giá ✓ · Tồn ✓ · Công nợ ✗', 'nợ quá hạn 12 ngày')
                 + step('ok', 'Chị An duyệt', '09:15', 'Duyệt dù khách nợ quá hạn', '“Khách quen, hẹn trả khi nhận”')
                 + step('ok', 'OPC kiểm tra lại', '09:15', 'Giữ 20 gói bò · 30 hũ muối')
                 + step('ok', 'Anh Khoa gửi', '09:18', 'Xác nhận cho chị Mai · Zalo OA'))

# ---------- state 1: approved and reserved → next: pick ----------
main1 = (head(sign('ok', 'i-check', 'Đã xác nhận · đã giữ hàng'),
              '<a class="c-btn c-btn--act" href="#">Soạn hàng</a><button class="c-btn" type="button">Sửa đơn</button>'
              '<button class="c-btn c-btn--danger c-btn--quiet" type="button">Huỷ đơn</button>',
              'Zalo OA · giao trước 15:00 hôm nay · trả 15 ngày')
         + journey(4)
         + '<div class="r-detail__grid r-detail--calm"><div class="stack">'
         + section('Món · hàng đang giữ', lines('lot') + '<p class="c-sub">Giữ tới 15:00 · trừ kho khi bàn giao</p>', 's1')
         + section('Giao hàng', '<dl class="c-kv"><dt>Người giao</dt><dd>Anh Hùng <a href="#">đổi</a></dd>'
                   '<dt>Giao đến</dt><dd>Cổng bếp, 12 Trần Hưng Đạo · chị Mai</dd>'
                   '<dt>Thu hộ</dt><dd>Không · ghi công nợ</dd></dl>', 's2')
         + section('Hoá đơn', '<p class="c-sub">Sau khi giao · OPC đề xuất, chị phát hành</p>', 's3')
         + section('Tiền · công nợ của khách', '<dl class="c-kv"><dt>Đang nợ</dt><dd>8.400.000 ₫ · <span class="c-sign c-sign--err"><span class="c-sign__pic">'
                   + ic('i-alert') + '</span>quá hạn 12 ngày</span></dd><dt>Sau đơn này</dt><dd>14.650.000 ₫ · hạn mức 15.000.000 ₫</dd>'
                   '</dl>', 's4')
         + '</div><aside class="r-tower__detail" aria-labelledby="tl"><h2 class="r-tower__t" id="tl">Diễn biến</h2><ol class="c-timeline">'
         + TIMELINE_BASE + step('next', 'Tiếp theo', '', 'Soạn hàng → giao anh Hùng trước 15:00') + '</ol></aside></div></div>')
build('order-detail', 'DH-2052 · Sunrise Hotel', main1, 'orders')
annhien(SCREENS / 'order-detail.html')

# ---------- state 2: delivered → invoice proposed, owner issues ----------
INV = ('<div class="c-decide" role="group" aria-labelledby="q-inv"><p class="c-decide__q" id="q-inv">Phát hành hoá đơn cho Sunrise Hotel?</p>'
       '<dl class="c-kv"><dt>Loại</dt><dd>Hoá đơn bán hàng (mẫu số 2) có mã · qua X Invoice</dd>'
       '<dt>Người mua</dt><dd>Sunrise Hotel · MST 5900987654</dd>'
       '<dt>Theo số đã giao</dt><dd>20 gói bò · 30 hũ muối · <b>6.250.000 ₫</b></dd>'
       '<dt>Chữ ký số</dt><dd>Của hộ, hết hạn 12/2027</dd></dl>'
       '<div class="c-decide__acts"><button class="c-btn c-btn--act" type="button">Phát hành hoá đơn</button>'
       '<button class="c-btn" type="button">Sửa thông tin</button></div>'
       '<p class="c-decide__who">Có mã CQT → OPC tạo phải thu hạn 21/10, soạn tin gửi hoá đơn</p></div>')
main2 = (head(sign('pend', 'i-clock', 'Đã giao · chờ hoá đơn'),
              '<button class="c-btn" type="button">In phiếu giao</button>', 'Đã giao 13:42 hôm nay · chị Mai nhận')
         + journey(6)
         + '<div class="r-detail__grid r-detail--calm"><div class="stack">'
         + section('Hoá đơn', INV, 's3')
         + section('Món · đã giao', lines('deliv') + '<p class="c-sub">Kho đã trừ lúc bàn giao 12:50 · lô BMN-0405</p>', 's1')
         + section('Giao hàng', '<dl class="c-kv"><dt>Người giao</dt><dd>Anh Hùng · xác nhận qua link</dd>'
                   '<dt>Bằng chứng</dt><dd>Ảnh lúc 13:42 · người nhận: chị Mai</dd></dl>', 's2')
         + '</div><aside class="r-tower__detail" aria-labelledby="tl"><h2 class="r-tower__t" id="tl">Diễn biến</h2><ol class="c-timeline">'
         + TIMELINE_BASE
         + step('ok', 'Anh Khoa', '12:46', 'Soạn xong 20 gói bò (lô BMN-0405), 30 hũ muối')
         + step('ok', 'Anh Khoa bàn giao', '12:50', 'Cho anh Hùng · OPC trừ kho')
         + step('ok', 'Anh Hùng', '13:42', 'Đã giao · ảnh và tên người nhận')
         + step('now', 'Chờ chị phát hành', 'Bây giờ', 'OPC đã soạn hoá đơn theo số đã giao')
         + '</ol></aside></div></div>')
build('order-detail--invoice', 'DH-2052 · đã giao, chờ hoá đơn', main2, 'orders')
annhien(SCREENS / 'order-detail--invoice.html')
print('order 360: 2 screens')

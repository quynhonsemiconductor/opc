"""v7.5.3 · demo facts: one source of truth at 06/10/2026 10:45 (design/_research/audit-e2e-v752.md). Older generators and the
src_v31/src_v43 snapshots still carry numbers from earlier stories; this pass rewrites them on the built screens. Runs after relink.
Year-to-date revenue 718.400.000 ₫ (under 1 tỷ) · muối tồn 80 / giữ 30 / khả dụng 50 · DH-2052 đặt 09:02, giữ 09:15, giao trước 15:00
hôm nay · HTX còn phải trả 2.800.000 ₫ · tiền mặt 1.000.000 ₫ đầu ngày + bán nhanh.  Usage: python3 facts7.py"""
from pages import SCREENS

YTD_METER = ('<div class="c-meter__row"><span class="u-meta">Doanh thu 2026 · <b>1,28 tỷ</b></span><span class="u-meta u-nowrap">ngưỡng 1 tỷ</span></div>',
             '<div class="c-meter__row"><span class="u-meta">Doanh thu từ 01/01 · <b>718,4 triệu</b></span><span class="u-meta u-nowrap">mốc 1 tỷ</span></div>')
FACTS = [
    YTD_METER,
    ('aria-label="Doanh thu 2026 1.284.500.000 ₫, đã vượt mốc 1 tỷ"><span class="c-meter__fill" style="width:85.6%">',
     'aria-label="Doanh thu từ 01/01 718.400.000 ₫, dưới mốc 1 tỷ"><span class="c-meter__fill" style="width:47.9%">'),
    ('<span class="c-meter__mark" style="left:66.7%"><span>1 tỷ</span></span>', ''),
    ('Trên 1 tỷ → bán lẻ dùng hoá đơn máy tính tiền', 'Nhịp năm khoảng 1,06 tỷ · mốc chờ kế toán xác nhận'),
    ('Không tắt được: doanh thu 2026 là 1.284.500.000 ₫, trên 1 tỷ.', 'Không tắt được · sổ bắt buộc'),
    ('Doanh thu 2026 1.284.500.000 ₫ · trên 1 tỷ', 'Doanh thu từ 01/01 718.400.000 ₫ · dưới 1 tỷ · nhịp năm khoảng 1,06 tỷ'),
    ('Giao trước 15:00 ngày mai và xuất hoá đơn.', 'Giao trước 15:00 hôm nay và xuất hoá đơn.'),
    ('MH-0118 thiếu 5 kg', 'MH-0118 thiếu 5 hũ'), ('(thiếu 5 kg)', '(thiếu 5 hũ)'),
    ('chờ chị xác nhận nhận hàng (thiếu 5 hũ) 11.200.000', 'chờ chị xác nhận nhận hàng (thiếu 5 hũ) 1.800.000'),
    ('cập nhật 14:05', 'cập nhật 10:44'), ('8.400.000 ₫ · 14:05', '8.400.000 ₫ · 10:44'),
    ('6.250.000 ₫ đơn đã giao, vào công nợ khi chị phát hành hoá đơn', '6.250.000 ₫ đang giao, vào công nợ khi giao xong và có hoá đơn'),
    ('đơn đã giao, vào công nợ khi chị phát hành hoá đơn', 'đang giao, vào công nợ khi giao xong và có hoá đơn'),
    ('<td class="c-table__cell--opt">30 ngày</td><td class="c-table__num"><b>4.800.000 ₫</b>', '<td class="c-table__cell--opt">30 ngày</td><td class="c-table__num"><b>2.800.000 ₫</b>'),
    ('Phải trả 6.050.000 ₫: HTX 4.800.000 ₫ hạn 08/10', 'Phải trả 4.050.000 ₫: HTX 2.800.000 ₫ hạn 08/10'),
    ('<b>6.050.000 ₫</b>', '<b>4.050.000 ₫</b>'), ('6.050.000', '4.050.000'),
    ('Trả 4.800.000 ₫ mở app ngân hàng', 'Trả 2.800.000 ₫ mở app ngân hàng'),
    ('Tiền mặt hôm nay</span><span class="c-debts__v">1.000.000 ₫</span>', 'Tiền mặt hôm nay</span><span class="c-debts__v">1.520.000 ₫</span>'),
    # leftover POS words (audit A)
    ('OPC đối chiếu như đóng ca', 'OPC đối chiếu khi chị đếm tiền cuối ngày'), ('/* Quầy is in the phone tab bar */', '/* Bán nhanh is reached from Bán */'),
    ('quầy: hoá đơn máy tính tiền', 'bán lẻ: hoá đơn máy tính tiền'),
    ('1.284.500.000 ₫ · trên 1 tỷ', '718.400.000 ₫ từ 01/01 · dưới 1 tỷ'),
    ('<small>Đơn mua MH-0109 · 30 ngày</small></td><td class="c-table__num">4.800.000 ₫', '<small>Đơn mua MH-0109 · còn lại sau lần trả 15/09</small></td><td class="c-table__num">2.800.000 ₫'),
    ('<a class="c-btn c-btn--act" href="#">Trả 4.800.000 ₫</a>', '<a class="c-btn c-btn--act" href="purchase-detail--pay.html">Ghi trả 2.800.000 ₫</a>'),
    ('(thiếu 5 hũ)   11.200.000 ₫', '(thiếu 5 hũ)   1.800.000 ₫'), ('(thiếu 5 hũ) 11.200.000 ₫', '(thiếu 5 hũ) 1.800.000 ₫'), ('11.200.000 ₫', '1.800.000 ₫'),
    ('Hoá đơn quầy hoạt động', 'Hoá đơn bán lẻ hoạt động'), ('Hilo (quầy)', 'Hilo (bán lẻ)'), ('Khi khách quét QR, quầy của chị hiện:', 'Khi khách quét QR, OPC hiện:'),
    ('<h1 class="r-page-head__title">Đơn hàng</h1>', '<h1 class="r-page-head__title">Đơn bán</h1>'), ('<title>Đơn hàng ·', '<title>Đơn bán ·'),
    ('<a class="c-btn desk-only" href="quick-sale.html">Bán nhanh</a>', '<a class="c-btn" href="quick-sale.html">Bán nhanh</a>'),   # audit A: reachable on phone
    # dead links found by the audit (v7.5.3)
    ('<a href="#">Nhờ người thân làm giúp</a>', '<a href="onboard-help.html">Nhờ người thân làm giúp</a>'),
    ('<a href="#">Tra lại mã</a>', '<a href="onboard-household--read.html">Tra lại mã</a>'),
    ('<a href="#">Mở Cổng dịch vụ công</a>', '<a href="https://dichvucong.gov.vn" rel="noopener">Mở Cổng dịch vụ công</a>'),
    ('<a class="c-icon-btn c-icon-btn--outline" href="#" aria-label="Quay lại bước trước">', '<a class="c-icon-btn c-icon-btn--outline" href="onboard-opening.html" aria-label="Quay lại bước trước">'),
    ('<a class="c-btn" href="#">Xuất Excel</a>', '<a class="c-btn" href="tax-evidence.html">Xuất Excel</a>'),
    ('<a class="c-btn" href="#">Hỏi lại bên hoá đơn</a>', '<a class="c-btn" href="connections--detail.html">Hỏi lại bên hoá đơn</a>'),
    ('<button class="c-btn c-btn--act" type="button">Gửi chị An khoá kỳ</button>', '<a class="c-btn c-btn--act" href="period--locked.html">Khoá kỳ quý III</a>'),
    ('<a class="c-btn c-btn--act" href="#">Thêm nhà cung cấp</a>', '<a class="c-btn c-btn--act" href="supplier-new.html">Thêm nhà cung cấp</a>'),
    ('<a href="#">Cách báo tài khoản cho cơ quan thuế</a>', '<a href="tax-notice-bank.html">Cách báo tài khoản cho cơ quan thuế</a>'),
    ('<a class="c-work" href="#">', '<a class="c-work" href="sales-inbox--unclear.html">'),
]

# per-screen fixes (a generic string would hit other screens)
FILE_FACTS = {
    'onboard-products.html': [('<button class="c-btn c-btn--act c-btn--block" type="button">Tiếp tục</button>', '<a class="c-btn c-btn--act c-btn--block" href="onboard-products--review.html">Tiếp tục</a>')],
    'period--item.html': [('<button class="c-btn c-btn--act" type="button">Lưu quyết định</button>', '<a class="c-btn c-btn--act" href="period--ready.html">Lưu quyết định</a>')],
    'orders--search.html': [('14 đơn · nợ 8.400.000 ₫, quá hạn 12 ngày', '14 đơn · nợ 8.400.000 ₫'), ('Tìm “sunrise” trong tất cả thời gian', 'Tìm trong mọi thời gian')],
    'receivables.html': [('Homestay · 15 ngày', 'Homestay · 15 ngày · đã chuyển 2.600.000 ₫, chờ gán')],
}

n = 0
for f in sorted(SCREENS.glob('*.html')):
    if f.name.startswith(('_', 'platform', 'program')):
        continue
    s = o = f.read_text()
    for a, b in FACTS + FILE_FACTS.get(f.name, []):
        s = s.replace(a, b)
    if f.name == 'receivables.html':
        i = s.find('Homestay Mây Ngàn')
        if i > 0:
            s = s[:i] + s[i:].replace('<a class="c-btn c-btn--quiet" href="#">Xem</a>', '<a class="c-btn c-btn--quiet" href="money--overpay.html">Gán tiền</a>', 1)
    if s != o:
        f.write_text(s); n += 1
print(f'facts7: {n} screens')

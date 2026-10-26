"""v7.7.0 · wire the remaining dead links (href="#") on household screens. A rule = (screen or '*', visible text, target); the first
link on that screen whose text starts with the given text gets the target. Detail pages are demo records (one customer, one order …):
a row of another customer opens the same record type — FE replaces it with the real id. Runs after facts7.  Usage: python3 links7.py"""
import re
from pages import SCREENS

R = [
    ('*', 'Xem tin gốc', 'sales-inbox.html'), ('approvals--error.html', 'Mở cổng hoá đơn điện tử', 'connections--detail.html'),
    ('audit.html', 'Xuất nhật ký', 'tax-evidence.html'), ('books.html', 'Xuất sổ', 'tax-evidence.html'), ('books.html', 'Xem tất cả', 'invoices.html'),
    ('connections--delivery.html', 'Người của hộ', 'connections--use.html'), ('connections--delivery.html', 'Nhà xe Đức Long', 'connections--use.html'),
    ('connections--many.html', 'Bán online', 'connections--category.html'), ('connections--many.html', 'Tiền và ngân hàng', 'connections--category.html'),
    ('connections--many.html', 'Hoá đơn và thuế', 'connections--category.html'), ('connections--many.html', 'Nhận đơn và định danh', 'connections--category.html'),
    ('connections--unknown.html', 'Nhắn chị Lan', 'audit.html'),
    ('connections.html', 'MB', 'connections--account.html'), ('connections.html', 'Hilo', 'connections--detail.html'), ('connections.html', 'Cas ID', 'connections--account.html'),
    ('customer-detail.html', 'Tạo đơn', 'sales-inbox--add.html'),
    ('customers.html', 'Thêm khách', 'setup-data.html'), ('customers.html', 'Nhà hàng Phố Núi', 'customer-detail.html'), ('customers.html', 'Homestay Mây Ngàn', 'customer-detail.html'),
    ('customers.html', 'Chị Thảo', 'customer-detail.html'), ('customers.html', 'Anh Nam', 'customer-detail.html'), ('customers.html', 'Chị Hoa', 'customer-detail.html'),
    ('customers.html', 'Xem', 'customer-detail.html'), ('customers.html', 'Sửa', 'customer-detail.html'),
    ('delivery--courier.html', 'Chỉ đường', 'https://maps.google.com/?q=12+Tr%E1%BA%A7n+H%C6%B0ng+%C4%90%E1%BA%A1o+Pleiku'),
    ('delivery--courier.html', 'Giao một phần', 'order-detail--split.html'), ('delivery--courier.html', 'Không giao được', 'delivery.html'),
    ('delivery--pick--back.html', 'Đã soạn lại', 'order-detail--delivering.html'),
    ('delivery.html', 'Bàn giao', 'order-detail--delivering.html'), ('delivery.html', 'Giao lại', 'delivery--pick.html'), ('delivery.html', 'Hoàn về kho', 'stock.html'),
    ('help.html', 'Gọi', 'tel:19001234'), ('help.html', 'Nhắn', 'onboard-help.html'), ('help.html', 'Đặt lịch', 'onboard-help.html'),
    ('home--firstrun.html', 'Nhập doanh thu', 'onboard-tax.html'),
    ('home--notifications.html', 'Đã xác minh', 'money.html'), ('home--notifications.html', 'Có tiền mới', 'money.html'),
    ('home--notifications.html', 'Hoá đơn DH-2047', 'approvals--error.html'), ('home--notifications.html', 'Nhận hàng MH-0118', 'purchase-detail--receive.html'),
    ('home--notifications.html', 'Liên kết MB', 'connections--account.html'), ('home--notifications.html', 'Nhắc: đối chiếu', 'period.html'),
    ('home--notifications.html', 'Cài đặt thông báo', 'settings-display.html'),
    ('invoice-detail.html', 'Tải PDF', 'tax-evidence.html'), ('invoices--accountant.html', 'Xuất Excel', 'tax-evidence.html'),
    ('money--help.html', 'Video', 'help.html'), ('onboard-assisted.html', 'Thoát hỗ trợ', 'readiness--new.html'),
    ('onboard-bank--mismatch.html', 'Để sau', 'onboard-invoice.html'), ('onboard-bank.html', 'Ngân hàng khác', 'connections--add.html'), ('onboard-bank.html', 'Để sau', 'onboard-invoice.html'),
    ('onboard-bankacc.html', 'Thêm tài khoản', 'tax-notice-bank.html'), ('onboard-help.html', 'Nhắn Zalo', 'help.html'), ('onboard-help.html', 'Nhờ người thân', 'onboard-assisted.html'),
    ('onboard-otp--wrong.html', 'Gửi qua SMS', 'onboard-otp.html'), ('onboard-otp.html', 'Chưa nhận được', 'onboard-otp.html'),
    ('onboard-products--review.html', 'Chụp thêm', 'onboard-products.html'), ('onboard-products--unreadable.html', 'Để sau', 'onboard-opening--empty.html'),
    ('onboard-welcome.html', 'Đã có tài khoản', 'onboard-phone.html'), ('onboard-welcome.html', 'Cần giúp', 'onboard-help.html'),
    ('orders--bulk--preview.html', 'Xem đơn', 'order-detail.html'), ('orders--bulk--preview.html', 'Gọi cửa hàng', 'tel:0935112418'),
    ('orders--search.html', 'Sunrise Hotel', 'customer-detail.html'), ('orders--search.html', 'DH-2052', 'order-detail.html'), ('orders--search.html', 'DH-2049', 'order-detail--invoice.html'),
    ('orders--search.html', 'Tìm trong mọi thời gian', 'orders--daterange.html'),
    ('*', 'Quý IV/2026', 'tax.html'), ('*', 'Quý II/2026', 'tax-file--signed.html'),
    ('products.html', 'Chụp bảng giá', 'onboard-products.html'), ('products.html', 'Thêm món', 'product-detail.html'), ('products.html', 'Xem', 'product-detail.html'),
    ('purchases--expense.html', 'Xem', 'purchases--expense.html'),
    ('receipt.html', 'Xem hoá đơn', 'invoice-detail.html'), ('receipt.html', 'Quan tâm Zalo OA', 'https://zalo.me/'),
    ('receivables--payables.html', 'HTX Cao Nguyên', 'purchase-detail--pay.html'), ('receivables--payables.html', 'Trả', 'purchases--expense.html'),
    ('receivables.html', 'Xem', 'customer-statement.html'),
    ('setup-data.html', 'Nhập dữ liệu', 'onboard-products.html'), ('setup-data.html', 'Sửa', 'customer-detail.html'), ('setup-data.html', 'Xem', 'products.html'),
    ('stock.html', 'Sổ biến động', 'books--stock.html'),
    ('suppliers.html', 'Cơ sở bò một nắng', 'purchase-detail.html'), ('suppliers.html', 'Bao bì Phú Mỹ', 'purchases--expense.html'), ('suppliers.html', 'Xem', 'purchase-detail.html'),
]
A = re.compile(r'<a([^>]*?)href="#"([^>]*)>(.*?)</a>', re.S)

n = left = 0
for f in sorted(SCREENS.glob('*.html')):
    if f.name.startswith(('_', 'platform', 'program', 'demo')):
        continue
    s = o = f.read_text()
    rules = [r for r in R if r[0] in ('*', f.name)]

    def fix(m):
        text = re.sub(r'<[^>]+>', '', m.group(3)).strip()
        for _, t, h in rules:
            if text.startswith(t) or (len(text) > 1 and text[1:].startswith(t) and text[0] == t[0]):   # list rows start with a monogram letter
                ext = ' rel="noopener"' if h.startswith('http') else ''
                return f'<a{m.group(1)}href="{h}"{ext}{m.group(2)}>{m.group(3)}</a>'
        if 'c-btn' in m.group(1) + m.group(2):   # in-place action, not navigation → a real button
            return f'<button{m.group(1).rstrip()} type="button"{m.group(2)}>{m.group(3)}</button>'
        return m.group(0)
    s = A.sub(fix, s)
    left += len(A.findall(s))
    if s != o:
        f.write_text(s); n += 1
print(f'links7: {n} screens · {left} links still "#"')

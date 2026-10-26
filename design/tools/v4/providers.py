"""v5.0.0 · THE provider catalog (data, not UI). Every screen that lists providers — the household directory, the platform registry —
renders from here. Removing a provider from OPC = delete one row (or set status 'hidden').  Nothing here is a partner commitment.

MODE = who holds the credential:
  casso   Casso's Cas Link page holds it. The household types it there; OPC never sees it. Revoked on Casso.
  oauth   The household approves on the provider's own page; OPC keeps a token (encrypted, expires, owner-only OTP).
  key     The household pastes a key / token into OPC. OPC keeps it in a vault, shows it masked, can rotate it.
  link    No credential. OPC opens the provider's app with data filled in (eTax, bank app). A person finishes.
  assist  Needs a contract or registration with the provider first; OPC staff help. Nothing to paste yet.
STATUS = ok (connected in the demo) · can (can connect now) · sim (demo only, Mô phỏng) · soon (Báo tôi) · partner (needs a partner/legal gate first)
SRC    = BA (named in the BA/CEO docs) · Web (confirmed to exist in Vietnam, 2026-10-07) · Tôi (my knowledge, unverified)
Jobs of another provider are not listed (ZNS = a job of Zalo OA; IDKit/tra MST = a job of Casso).
Zalo personal accounts are deliberately NOT here: Zalo offers an API for Official Accounts only.
"""
MODES = {'opc': ('OPC lo sẵn', 'Không cần nối · OPC gửi bằng tài khoản của OPC'),
         'casso': ('Nối qua Casso', 'Chị nhập ở trang của Casso · OPC không giữ mật khẩu'),
         'oauth': ('Cho phép trên trang của họ', 'Chị bấm cho phép ở trang của họ · OPC giữ mã có hạn'),
         'key': ('Dán khoá kết nối', 'Chị dán khoá lấy từ trang của họ · OPC cất kín'),
         'link': ('Mở app của họ', 'Không cần khoá · OPC mở app với thông tin điền sẵn, chị bấm cuối'),
         'assist': ('Cần đăng ký trước', 'Phải đăng ký hoặc ký hợp đồng với họ · OPC hỗ trợ')}
SHORT = {'opc': 'OPC lo sẵn', 'casso': 'Qua Casso', 'oauth': 'Cho phép', 'key': 'Dán khoá', 'link': 'Mở app', 'assist': 'Cần đăng ký'}   # one or two words for a tile
GROUPS = [('chat', 'Nhận đơn và trò chuyện'), ('notify', 'Thông báo cho khách'), ('bank', 'Tiền và ngân hàng'), ('inv', 'Hoá đơn và thuế'),
          ('sign', 'Chữ ký số'), ('id', 'Định danh và tra cứu'), ('ship', 'Giao hàng'), ('shop', 'Bán online'), ('data', 'Sổ sách và dữ liệu')]

# (id, mono, name, group, mode, status, households, src)
P = [
    ('opc-notify', 'O', 'Tin nhắn của OPC (Zalo, SMS)', 'notify', 'opc', 'ok', 8, 'BA'),
    ('zalo-oa', 'Z', 'Zalo OA', 'chat', 'oauth', 'ok', 8, 'BA'),
    ('messenger', 'F', 'Messenger (Facebook Page)', 'chat', 'oauth', 'soon', 0, 'Tôi'),
    ('instagram', 'I', 'Instagram', 'chat', 'oauth', 'soon', 0, 'Tôi'),
    ('tiktok-dm', 'T', 'TikTok tin nhắn', 'chat', 'oauth', 'soon', 0, 'Tôi'),
    ('telegram', 'T', 'Telegram (dự phòng)', 'chat', 'key', 'soon', 0, 'BA'),
    ('email', 'E', 'Hộp thư email', 'chat', 'oauth', 'soon', 0, 'Tôi'),

    ('esms', 'e', 'eSMS', 'notify', 'key', 'soon', 0, 'Tôi'),
    ('speedsms', 'S', 'SpeedSMS', 'notify', 'key', 'soon', 0, 'Tôi'),
    ('viettel-sms', 'V', 'Viettel SMS Brandname', 'notify', 'assist', 'soon', 0, 'Tôi'),

    ('mb', 'M', 'MB qua Casso', 'bank', 'casso', 'ok', 6, 'BA'),
    ('bidv', 'B', 'BIDV qua Casso', 'bank', 'casso', 'partner', 0, 'BA'),
    ('techcombank', 'T', 'Techcombank qua Casso', 'bank', 'casso', 'soon', 0, 'BA'),
    ('vietcombank', 'V', 'Vietcombank qua Casso', 'bank', 'casso', 'soon', 0, 'BA'),
    ('agribank', 'A', 'Agribank qua Casso', 'bank', 'casso', 'soon', 0, 'BA'),
    ('baokim', 'B', 'Ví Bảo Kim qua Casso', 'bank', 'casso', 'soon', 0, 'BA'),
    ('sepay', 'S', 'SePay', 'bank', 'key', 'soon', 0, 'BA'),
    ('payos', 'p', 'payOS', 'bank', 'key', 'ok', 1, 'Web'),
    ('bank-link', 'b', 'Mở app ngân hàng (điền sẵn)', 'bank', 'link', 'can', 0, 'BA'),
    ('vnpay', 'V', 'VNPAY', 'bank', 'assist', 'soon', 0, 'Web'),
    ('momo', 'm', 'MoMo', 'bank', 'assist', 'soon', 0, 'Web'),
    ('zalopay', 'Z', 'ZaloPay', 'bank', 'assist', 'soon', 0, 'Web'),
    ('shopeepay', 'S', 'ShopeePay', 'bank', 'assist', 'soon', 0, 'Web'),
    ('viettelpay', 'V', 'ViettelPay', 'bank', 'assist', 'soon', 0, 'Web'),

    ('hilo', 'H', 'Hilo', 'inv', 'casso', 'ok', 4, 'BA'),
    ('xinvoice', 'X', 'X Invoice', 'inv', 'casso', 'ok', 3, 'BA'),
    ('sinvoice', 'S', 'Viettel S-Invoice', 'inv', 'casso', 'can', 0, 'BA'),
    ('bkav', 'B', 'Bkav eHoadon', 'inv', 'casso', 'soon', 0, 'BA'),
    ('meinvoice', 'M', 'MISA meInvoice', 'inv', 'assist', 'soon', 0, 'Web'),
    ('vnpt-inv', 'V', 'VNPT Invoice', 'inv', 'assist', 'soon', 0, 'Web'),
    ('fpt-inv', 'F', 'FPT eInvoice', 'inv', 'assist', 'soon', 0, 'Web'),
    ('easyinvoice', 'E', 'EasyInvoice', 'inv', 'assist', 'soon', 0, 'Tôi'),
    ('gdt-hub', 'G', 'Casso GDT Hub (cổng thuế)', 'inv', 'casso', 'can', 0, 'BA'),
    ('casso-tvan', 'C', 'Casso TVAN (nộp tờ khai)', 'inv', 'casso', 'partner', 0, 'BA'),
    ('ts24', 'T', 'TS24 (T-VAN)', 'inv', 'assist', 'soon', 0, 'Tôi'),
    ('thaison', 'T', 'Thái Sơn (T-VAN)', 'inv', 'assist', 'soon', 0, 'Tôi'),
    ('etax', 'e', 'eTax Mobile (nộp thuế)', 'inv', 'link', 'can', 0, 'BA'),

    ('cas-cert', 'C', 'CAS CERT (Cas ID)', 'sign', 'assist', 'partner', 0, 'BA'),
    ('smartca', 'V', 'VNPT SmartCA', 'sign', 'assist', 'soon', 0, 'Web'),
    ('mysign', 'V', 'Viettel MySign', 'sign', 'assist', 'soon', 0, 'Web'),
    ('fpt-esign', 'F', 'FPT.eSign', 'sign', 'assist', 'soon', 0, 'Web'),
    ('misa-esign', 'M', 'MISA eSign', 'sign', 'assist', 'soon', 0, 'Tôi'),
    ('bkavca', 'B', 'BkavCA', 'sign', 'assist', 'soon', 0, 'Tôi'),

    ('cas-id', 'C', 'Cas ID (xác minh chủ hộ)', 'id', 'assist', 'ok', 7, 'BA'),
    ('vnpt-ekyc', 'V', 'VNPT eKYC', 'id', 'assist', 'soon', 0, 'Tôi'),
    ('fpt-ai', 'F', 'FPT.AI eKYC', 'id', 'assist', 'soon', 0, 'Tôi'),
    ('vietqr-lookup', 'V', 'VietQR tra tên tài khoản', 'id', 'key', 'soon', 0, 'BA'),

    ('ghtk', 'G', 'GHTK', 'ship', 'key', 'sim', 0, 'Tôi'),
    ('ghn', 'G', 'GHN', 'ship', 'key', 'soon', 0, 'Web'),
    ('viettelpost', 'V', 'Viettel Post', 'ship', 'key', 'soon', 0, 'Web'),
    ('vnpost', 'V', 'VNPost', 'ship', 'key', 'soon', 0, 'Web'),
    ('jt', 'J', 'J&T Express', 'ship', 'key', 'soon', 0, 'Tôi'),
    ('ninjavan', 'N', 'Ninja Van', 'ship', 'key', 'soon', 0, 'Web'),
    ('spx', 'S', 'SPX Express (Shopee)', 'ship', 'key', 'soon', 0, 'Web'),
    ('best', 'B', 'BEST Express', 'ship', 'key', 'soon', 0, 'Tôi'),
    ('ahamove', 'A', 'Ahamove', 'ship', 'key', 'soon', 0, 'Web'),
    ('grabexpress', 'G', 'Grab Express', 'ship', 'assist', 'soon', 0, 'Tôi'),
    ('lalamove', 'L', 'Lalamove', 'ship', 'key', 'soon', 0, 'Tôi'),

    ('shopee', 'S', 'Shopee', 'shop', 'oauth', 'soon', 0, 'Web'),
    ('tiktokshop', 'T', 'TikTok Shop', 'shop', 'oauth', 'soon', 0, 'Web'),
    ('lazada', 'L', 'Lazada', 'shop', 'oauth', 'soon', 0, 'Web'),
    ('tiki', 'T', 'Tiki', 'shop', 'oauth', 'soon', 0, 'Web'),
    ('shopeefood', 'S', 'ShopeeFood', 'shop', 'assist', 'soon', 0, 'Tôi'),
    ('grabfood', 'G', 'GrabFood', 'shop', 'assist', 'soon', 0, 'Tôi'),
    ('haravan', 'H', 'Haravan', 'shop', 'oauth', 'soon', 0, 'Tôi'),
    ('sapo', 'S', 'Sapo', 'shop', 'oauth', 'soon', 0, 'Tôi'),
    ('kiotviet', 'K', 'KiotViet', 'shop', 'key', 'soon', 0, 'Tôi'),
    ('nhanh', 'N', 'Nhanh.vn', 'shop', 'key', 'soon', 0, 'Tôi'),
    ('woocommerce', 'W', 'WooCommerce', 'shop', 'key', 'soon', 0, 'Tôi'),

    ('gsheets', 'G', 'Google Sheets', 'data', 'oauth', 'soon', 0, 'Tôi'),
    ('misa-acc', 'M', 'Xuất cho MISA', 'data', 'link', 'soon', 0, 'BA'),
    ('fast-acc', 'F', 'Xuất cho Fast', 'data', 'link', 'soon', 0, 'Tôi'),
    ('bravo-acc', 'B', 'Xuất cho Bravo', 'data', 'link', 'soon', 0, 'Tôi'),
]
# What blocks a provider on the platform side (shown in the platform registry, never to a household)
GATE = {'gdt-hub': 'Chờ kiểm tra pháp lý N-15', 'bidv': 'Cần ký hợp đồng tài khoản ảo (2–5 ngày)', 'casso-tvan': 'Chưa thử · không dùng ở thí điểm',
        'cas-cert': 'Chờ chọn nhà cung cấp chữ ký số (Câu 2)', 'sinvoice': 'Sandbox chưa gửi thuế sau 15 phút'}
KEYS = ('id', 'mono', 'name', 'group', 'mode', 'status', 'hh', 'src')
CAT = [dict(zip(KEYS, r)) for r in P]
GROUP_NAME = dict(GROUPS)

if __name__ == '__main__':
    from collections import Counter
    print(len(CAT), 'providers;', Counter(c['status'] for c in CAT), Counter(c['mode'] for c in CAT))
    assert len({c['id'] for c in CAT}) == len(CAT)


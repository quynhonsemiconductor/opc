"""v7.0.0 · Sẵn sàng — everything a hộ kinh doanh needs end to end, by chain (system/E2E-SCOPE.md). Data, not UI.
tier: need = bắt buộc (law, or the chain cannot be correct without it) · optional = tuỳ chọn, hiện với "Bỏ qua".
state per household: done · todo · wait (waiting on someone/a decision) · err (connection failing) · skip (owner skipped an optional item).
gate = what stays locked until it is done (shown on the row; the rest of the app keeps working). Legal items are versioned rules to be confirmed by an accountant."""
CHAINS = [('base', 'Hộ và dữ liệu nền'), ('buy', 'Mua hàng và kho'), ('sell', 'Bán hàng, hoá đơn và tiền'), ('tax', 'Sổ sách và kê khai')]
# (id, chain, name, meta, tier, gate, action, href, state new household, state established household)
R = [
    ('profile', 'base', 'Hồ sơ hộ từ giấy đăng ký', 'tên hộ, ngành nghề, địa điểm, chủ hộ', 'need', '', '', '', 'done', 'done'),
    ('consent', 'base', 'Đồng ý xử lý dữ liệu', 'chị An đồng ý 01/07', 'need', '', '', '', 'done', 'done'),
    ('catalog', 'base', 'Hàng hoá, quy cách và bảng giá', '2 món · giá lẻ và giá khách sạn', 'need', '', '', 'products.html', 'done', 'done'),
    ('parties', 'base', 'Khách và nhà cung cấp', 'gõ mã số thuế là tự điền', 'need', 'đơn mua, đơn bán có tên', 'Thêm', 'setup-data.html', 'todo', 'done'),
    ('staff', 'base', 'Mời nhân viên bán', 'mỗi người một tên đăng nhập', 'optional', '', 'Mời', 'setup-policy.html', 'todo', 'done'),
    ('accountant', 'base', 'Mời kế toán', 'chỉ xem và xuất dữ liệu', 'optional', '', 'Mời', 'setup-policy.html', 'todo', 'done'),
    ('install', 'base', 'Cài OPC lên màn hình chính', 'mở nhanh, nhận thông báo', 'optional', '', 'Hướng dẫn', 'help.html', 'todo', 'todo'),
    ('identity', 'base', 'Xác minh chủ hộ', 'chỉ khi ngân hàng hoặc nhà cung cấp hoá đơn đòi', 'optional', '', 'Xem', 'onboard-verify.html', 'skip', 'done'),

    ('stock0', 'buy', 'Tồn đầu kỳ đã đếm', 'đếm một lần, chị xác nhận', 'need', 'bán theo tồn, giữ hàng', 'Bắt đầu đếm', 'stock-count.html', 'todo', 'done'),
    ('expense', 'buy', 'Nhóm chi phí', 'điện, nước, thuê, vận chuyển, bao bì', 'need', 'ghi chi phí vào sổ', 'Xem', 'purchases--expense.html', 'todo', 'done'),
    ('buyin', 'buy', 'Hoá đơn mua vào tự về từ cổng thuế', 'làm tay: tải lên file hoặc chụp', 'optional', '', 'Chọn cách', 'connections--category.html', 'todo', 'todo'),
    ('paylink', 'buy', 'Mở app ngân hàng khi trả nhà cung cấp', 'OPC điền sẵn, chị tự chuyển', 'optional', '', 'Bật', 'purchase-detail--pay.html', 'todo', 'todo'),
    ('expiry', 'buy', 'Hạn dùng cho hàng cần theo dõi', 'cảnh báo hàng cận hạn', 'optional', '', 'Chọn hàng', 'products.html', 'todo', 'done'),

    ('invoice', 'sell', 'Hoá đơn điện tử bán ra', 'khách sỉ cần hoá đơn', 'need', 'phát hành khi Đã giao', 'Xem', 'onboard-invoice.html', 'wait', 'err'),
    ('delivery', 'sell', 'Cách giao mặc định', 'người của hộ, nhà xe hoặc khách tự lấy', 'need', 'nhận đơn sỉ', 'Chọn', 'connections--delivery.html', 'todo', 'done'),
    ('bankfeed', 'sell', 'Nối ngân hàng để tiền về tự khớp', 'làm tay: xác nhận theo sao kê', 'optional', '', 'Nối', 'onboard-bank.html', 'todo', 'done'),
    ('chat', 'sell', 'Nối Zalo OA để yêu cầu tự vào', 'làm tay: dán tin, chụp ảnh', 'optional', '', 'Nối', 'connections--category.html', 'todo', 'done'),
    ('softlimit', 'sell', 'Hạn mức nợ chỉ để cảnh báo', 'không chặn đơn', 'optional', '', 'Đặt', 'setup-policy.html', 'todo', 'todo'),
    ('zns', 'sell', 'Báo tin cho khách qua Zalo', 'cần mẫu tin được duyệt', 'optional', '', 'Xem', 'connections--category.html', 'todo', 'wait'),

    ('opening', 'tax', 'Số đầu kỳ: tiền mặt, tiền gửi, công nợ', 'hoặc bắt đầu từ 0', 'need', 'sổ quỹ, công nợ', 'Nhập', 'onboard-opening.html', 'done', 'done'),
    ('period', 'tax', 'Kỳ khai thuế', 'quý · chị xác nhận theo cách đã khai', 'need', '', '', 'tax.html', 'done', 'done'),
    ('accounts', 'tax', 'Báo tài khoản dùng kinh doanh cho cơ quan thuế', 'MB 0901 2345 678 · chị đã báo', 'need', '', '', 'tax-notice-bank.html', 'done', 'done'),
    ('etax', 'tax', 'VNeID mức 2 và tài khoản eTax của chủ hộ', 'cần để kê khai · OPC không giữ mật khẩu', 'need', 'kê khai', 'Hướng dẫn', 'onboard-gov.html', 'todo', 'done'),
    ('rules', 'tax', 'Bộ quy tắc thuế đã xác nhận', 'kế toán đối chiếu trước khi dùng', 'need', 'thuế ước tính, hướng dẫn tờ khai', 'Xem', 'tax.html', 'wait', 'wait'),
    ('export', 'tax', 'Xuất dữ liệu cho kế toán', 'Excel, CSV có sẵn', 'optional', '', '', 'tax-evidence.html', 'done', 'done'),
]
K = ('id', 'chain', 'name', 'meta', 'tier', 'gate', 'act', 'href', 'new', 'est')
ITEMS = [dict(zip(K, r)) for r in R]
CLOSED = ('done', 'skip')


def count(state_key='new', tier=None, open_only=True):
    return sum(1 for i in ITEMS if (tier is None or i['tier'] == tier) and (i[state_key] not in CLOSED if open_only else True))


if __name__ == '__main__':
    for sk in ('new', 'est'):
        print(sk, {t: count(sk, t) for t in ('need', 'optional')}, 'closed', sum(i[sk] in CLOSED for i in ITEMS), 'of', len(ITEMS))

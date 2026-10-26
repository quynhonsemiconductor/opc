"""v7.0.0 · Việc OPC làm cho hộ (features first). Providers are the choices underneath (providers.py).
TIER  need     = cần nối thì chuỗi mới đúng luật (only the e-invoice provider today, when the hộ must or needs to issue invoices)
      opc      = OPC lo sẵn: dịch vụ của OPC, hộ không phải nối gì
      optional = tuỳ chọn, nên có — hiện trong onboarding với "Bỏ qua", không chặn chuỗi nào
Every feature has a manual path. Source: system/E2E-SCOPE.md.
DEMO  state at 06/10/2026 10:45 in Kết nối: ok / err / wait / none
"""
from providers import CAT

BY = {c['id']: c for c in CAT}
# (id, name, what OPC does (owner's words), tier, why (from the model), recommended, provider ids, manual path, categories, demo state, demo way)
F = [
    ('invoice', 'Xuất hoá đơn điện tử', 'Bấm "Đã giao" là hoá đơn ra, có mã của cơ quan thuế', 'need', 'chị bán cho khách sỉ, khách cần hoá đơn', 'hilo',
     ['hilo', 'xinvoice', 'sinvoice', 'bkav', 'meinvoice', 'vnpt-inv', 'fpt-inv', 'easyinvoice'], 'không có: hoá đơn điện tử chỉ phát hành qua nhà cung cấp', [4, 8],
     'err', 'Hilo (quầy) · X Invoice (khách sỉ, đang lỗi)'),
    ('login', 'Gửi mã đăng nhập', 'Mã 6 số qua tin nhắn khi chị đăng nhập trên máy mới', 'opc', 'mọi hộ', 'opc-notify', ['opc-notify'], '', [14], 'ok', 'OPC lo sẵn · tin nhắn SMS'),
    ('notify', 'Báo việc cho chị', 'Tiền về, hoá đơn lỗi, việc cần chị quyết, hạn kê khai', 'opc', 'mọi hộ', 'opc-notify', ['opc-notify'], '', [14], 'ok', 'OPC lo sẵn · Zalo của OPC, SMS'),
    ('chat', 'Nhận yêu cầu từ Zalo', 'Tin khách nhắn vào Zalo OA tự vào Hộp yêu cầu, Agent soạn đơn', 'optional', 'chị nhận đơn sỉ qua Zalo', 'zalo-oa',
     ['zalo-oa', 'messenger', 'instagram', 'tiktok-dm', 'email'], 'dán tin, chụp ảnh hoặc gõ tay vào Hộp yêu cầu', [11], 'ok', 'Zalo OA'),
    ('receive', 'Tiền về tự khớp', 'Tiền chuyển khoản tự khớp với đơn, có QR theo từng đơn', 'optional', 'khách chuyển khoản nhiều', 'mb',
     ['mb', 'payos', 'sepay', 'bidv', 'techcombank', 'vietcombank', 'agribank', 'momo', 'zalopay'], 'chị xác nhận theo sao kê ngân hàng', [1, 2], 'ok', 'MB qua Casso · payOS'),
    ('buyin', 'Hoá đơn mua vào tự về', 'Hoá đơn của nhà cung cấp tự về sổ từ cổng thuế', 'optional', 'chị mua hàng về bán', 'gdt-hub', ['gdt-hub'],
     'tải lên file hoá đơn hoặc chụp chứng từ', [5], 'none', 'đang làm tay'),
    ('pay', 'Mở app ngân hàng khi trả tiền', 'OPC điền sẵn số tài khoản, số tiền; chị tự chuyển', 'optional', 'chị trả nhà cung cấp bằng chuyển khoản', 'bank-link',
     ['bank-link', 'vietqr-lookup'], 'chép số tài khoản và số tiền vào app ngân hàng', [3], 'none', 'làm tay'),
    ('notifycust', 'Báo tin cho khách', 'Gửi hoá đơn, nhắc nợ qua Zalo ZNS, chị bấm gửi', 'optional', 'chị có khách ghi nợ', 'zalo-oa',
     ['zalo-oa', 'esms', 'speedsms', 'viettel-sms'], 'chị tự nhắn hoặc gọi', [14], 'wait', 'Zalo ZNS · chờ mẫu tin được duyệt'),
    ('ship', 'Giao qua hãng', 'Tạo vận đơn, theo dõi, thu hộ', 'optional', 'giao bằng người của hộ cũng được', 'ghtk',
     ['ghtk', 'ghn', 'viettelpost', 'vnpost', 'jt', 'ninjavan', 'spx', 'best', 'ahamove', 'grabexpress', 'lalamove'], 'người của hộ, nhà xe, nhập mã vận đơn', [13], 'none', 'người của hộ'),
    ('identity', 'Xác minh chủ hộ', 'Khi ngân hàng hoặc nhà cung cấp hoá đơn đòi', 'optional', 'chỉ khi có bên đòi', 'cas-id', ['cas-id', 'vnpt-ekyc', 'fpt-ai'],
     'nhân viên OPC kiểm giấy tờ tại chỗ', [9], 'ok', 'Cas ID · chị An'),
    ('books', 'Xuất cho kế toán', 'Excel, CSV hoặc theo mẫu phần mềm kế toán', 'optional', 'luôn có Excel', 'misa-acc', ['gsheets', 'misa-acc', 'fast-acc', 'bravo-acc'],
     'Excel/CSV có sẵn', [16, 17], 'ok', 'Excel/CSV có sẵn'),
]
K = ('id', 'name', 'what', 'tier', 'why', 'rec', 'choices', 'manual', 'cats', 'demo', 'way')
LOCK = {'invoice': 'chưa phát hành được hoá đơn điện tử'}
FEATS = [dict(zip(K, r), lock=LOCK.get(r[0], ''), when='') for r in F]
FBY = {f['id']: f for f in FEATS}
TIERS = [('need', 'Cần nối'), ('opc', 'OPC lo sẵn'), ('optional', 'Tuỳ chọn · bỏ qua được')]


def selectable(p):   # a household can pick it now (not "Sắp có")
    return BY[p]['status'] in ('ok', 'can', 'sim')


if __name__ == '__main__':
    for f in FEATS:
        assert all(p in BY for p in f['choices']), f['id']
        print(f['id'], f['tier'], len(f['choices']), 'selectable:', [p for p in f['choices'] if selectable(p)])

"""v7.0.0 · Onboarding "Mở hộ" — six steps holding every mandatory item of a hộ kinh doanh (system/E2E-SCOPE.md, _research/mandatory-2026.md).
  1 Số điện thoại    onboard-phone · otp · otp--wrong · consent (explicit data consent, Luật 91/2025)
  2 Hộ kinh doanh    onboard-household (đã có / chưa có giấy đăng ký) · --read (OPC đọc từ ảnh) · --notfound · --unregistered (hướng dẫn đăng ký ở xã)
  3 Cách bán         onboard-model (cách bán, hàng từ đâu, thuê người, thực phẩm) → onboard-features → onboard-feature   (features: onboard_features.py)
  4 Thuế và tài khoản onboard-gov (VNeID mức 2, eTax) · onboard-tax (doanh thu, kỳ khai) · onboard-bankacc (tài khoản dùng kinh doanh, đã báo thuế)
  5 Hoá đơn          onboard-invoice (cách xuất) · --register (chữ ký số, nối nhà cung cấp, 01/ĐKTĐ-HĐĐT, ký hiệu)
  6 Số đầu kỳ        onboard-products (+review/unreadable/help) · onboard-opening (tồn đã đếm, tiền, công nợ)
  → onboard-done (giao dịch đầu tiên). Gates reached from Sẵn sàng, no step bar: onboard-verify* (xác minh chủ hộ, tuỳ chọn), onboard-bank* (nối ngân hàng, tuỳ chọn).
Legal numbers shown to the owner are rules "chờ kế toán xác nhận". Runs after onboard43.py and onboard_features.py.  Usage: python3 onboard_flow.py"""
import re
from onboard_lib import *
from readiness_model import count

P = lambda n: SCREENS / f'{n}.html'
CK = ic('i-check')


def patch(name, pairs, sub=None):
    s = P(name).read_text()
    for a, b in pairs:
        s = s.replace(a, b)
    if sub:
        s = sub(s)
    P(name).write_text(sprite(s))


def main(title, body, say=''):
    return (f'<main class="r-onboard__body">\n    <h1 class="r-onboard__title">{title}</h1>\n' + (f'    <p class="c-say">{say}</p>\n' if say else '')
            + body + '\n    <p class="r-onboard__saved">Đã lưu — làm tiếp lúc nào cũng được</p>\n  </main>')


def gate_row(tone, st, t, m):
    s = f'<span class="r-gate__st">{st}</span> · ' if st else ''
    pic = {'ok': 'i-check', 'wait': 'i-clock', 'err': 'i-alert'}.get(tone)   # v7.5.1: state readable without colour
    pic = f'<span class="r-gate__ic r-gate__ic--{tone}" aria-hidden="true">{ic(pic)}</span>' if pic else ''
    return (f'<li class="r-gate__i r-gate__i--{tone}"><span class="r-gate__b"><b>{pic}{t}</b><small>{s}{m}</small></span><span class="r-gate__amt"></span><span class="r-gate__act"></span></li>')


def yesno(qid, q, yes, no, on_yes=True, yes_m='', no_m=''):
    hint = f'<p class="u-meta r-yn__hint">{no_m if not on_yes and no_m else yes_m if yes_m else no_m}</p>' if (yes_m or no_m) else ''
    return (f'<fieldset class="r-yn"><legend class="r-yn__q">{q}</legend><div class="c-options r-yn__opts" role="radiogroup" aria-label="{q}">'
            + opt(on_yes, yes, '') + opt(not on_yes, no, '') + f'</div>{hint}</fieldset>')


def unstep(s, label):
    s = re.sub(r'<div class="c-steps" role="img" aria-label="[^"]*"><span class="c-steps__label">.*?</ol></div>',
               f'<div class="c-steps" role="img" aria-label="Sẵn sàng: {label}"><span class="c-steps__label"><b>Sẵn sàng</b> · {label}</span></div>', s, count=1, flags=re.S)
    s = re.sub(r'href="[^"]*" aria-label="Quay lại bước trước"', 'href="readiness--new.html" aria-label="Quay lại Sẵn sàng"', s, count=1)
    return re.sub(r'<aside class="r-onboard__aside[^"]*".*?</aside>\s*', '', s, flags=re.S)


# ================================================================== 1 · Số điện thoại + đồng ý dữ liệu
patch('onboard-phone', [('Gửi mã qua Zalo', 'Gửi mã cho tôi'), ('Số MobiFone hợp lệ · có Zalo — mã gửi qua Zalo, không mất phí', 'OPC gửi mã 6 số qua tin nhắn · chị không mất phí')])
for n in ('onboard-otp', 'onboard-otp--wrong'):
    patch(n, [('Mở tin nhắn Zalo từ OPC Gia Lai — mã sẽ tự điền', 'Mã đến qua tin nhắn SMS hoặc Zalo của OPC · máy cho phép thì tự điền'),
              ('Nhập mã 6 số OPC vừa gửi qua Zalo', 'Nhập mã 6 số OPC vừa gửi'), ('Không nhận được? Gửi qua tin nhắn SMS', 'Chưa nhận được? Gửi lại mã'),
              ('href="onboard-household.html"', 'href="onboard-consent.html"')])

CONSENT = main('OPC dùng dữ liệu của hộ thế nào', (
    '    <p class="r-yn__hint">' + ic('i-check') + 'Số điện thoại đã xác nhận · dùng để đăng nhập và nhận mã</p>\n'
    '    <ul class="r-gate">' + gate_row('ok', '', 'Hồ sơ hộ, hàng, giao dịch, hoá đơn, sổ', 'để vận hành và lập sổ cho chị')
    + gate_row('ok', '', 'Tên, số điện thoại, địa chỉ của khách', 'chỉ để bán và giao · khách được báo và có quyền yêu cầu xoá')
    + gate_row('ok', '', 'Chị xuất hoặc xoá dữ liệu lúc nào cũng được', 'OPC không bán dữ liệu') + '</ul>\n'
    '    <div class="c-options r-model" role="group" aria-label="Đồng ý">'
    + opt(True, 'Tôi đồng ý OPC xử lý dữ liệu của hộ', 'bắt buộc để dùng OPC', kind='checkbox')
    + opt(False, 'Cho Agent đọc tin nhắn, ảnh tôi gửi', 'tuỳ chọn · để soạn đơn và đọc chứng từ · bật sau cũng được', kind='checkbox') + '</div>'),
    'Theo Luật Bảo vệ dữ liệu cá nhân, chị cần đồng ý trước khi OPC lưu dữ liệu.')
shell('onboard-consent', 'Đăng ký · Đồng ý dữ liệu', 'onboard-otp.html', CONSENT,
      foot(btn('Đồng ý và tiếp tục', 'onboard-household.html'), '<a href="help.html">Đọc chính sách dữ liệu đầy đủ</a><a href="onboard-help.html">Hỏi nhân viên OPC</a>'), 1)

# ================================================================== 2 · Hộ kinh doanh
HH = main('Hộ của chị đã có giấy đăng ký kinh doanh chưa?', (
    '    <div class="c-options" role="radiogroup" aria-label="Giấy đăng ký hộ kinh doanh">'
    + opt(True, 'Đã có giấy đăng ký', 'chụp giấy, OPC đọc tên hộ, ngành nghề, địa điểm, chủ hộ')
    + opt(False, 'Chưa có', 'OPC hướng dẫn đăng ký ở xã, nhân viên OPC làm cùng chị') + '</div>'),
    'Mã số thuế của hộ là số định danh trên căn cước của chủ hộ.')
shell('onboard-household', 'Đăng ký · Hộ kinh doanh', 'onboard-consent.html', HH,
      foot(btn('Chụp giấy đăng ký', 'onboard-household--read.html', False), '<a href="onboard-household--notfound.html">Không chụp được, nhập mã số thuế</a>'), 2)

READ = main('Đây có đúng hộ của chị?', (
    '    <dl class="c-kv"><dt>Tên hộ</dt><dd>HỘ KINH DOANH ĐẶC SẢN CAO NGUYÊN AN NHIÊN</dd><dt>Chủ hộ</dt><dd>PHẠM THỊ AN</dd><dt>Mã số thuế</dt><dd>5901234567</dd>'
    '<dt>Ngành nghề</dt><dd>Bán buôn, bán lẻ thực phẩm</dd></dl>\n'
    '    <div class="c-field" data-check><label class="c-field__label" for="hh-addr">Địa điểm kinh doanh</label><div class="c-field__control"><input class="c-field__input" id="hh-addr" value="86 Lê Lợi, phường Pleiku, Gia Lai"></div>'
    '<span class="c-field__hint"><b>OPC chưa chắc dòng này</b> · ảnh bị loá ở góc · chạm để sửa</span></div>'),
    'OPC đọc từ ảnh giấy đăng ký chụp 10:02. Dòng nào sai, chị sửa ngay.')
shell('onboard-household--read', 'Đăng ký · Kiểm tra thông tin hộ', 'onboard-household.html', READ,
      foot(btn('Đúng, tiếp tục', 'onboard-model.html'), '<a href="onboard-household.html">Chụp lại</a><a href="onboard-help.html">Nhờ nhân viên OPC</a>'), 2)

NF = main('Nhập mã số thuế của hộ', (
    '    ' + field('hh-mst', 'Mã số thuế hoặc số định danh chủ hộ', '5901234568', 'OPC chưa tìm thấy số này · có thể gõ nhầm một số', bad=True, mode='numeric') + '\n'
    '    <p class="c-say">Không sao. Chụp giấy đăng ký, OPC đọc giúp và nhân viên sẽ kiểm tra lại.</p>'))
shell('onboard-household--notfound', 'Đăng ký · Nhập mã số thuế', 'onboard-household.html', NF,
      foot(btn('Chụp giấy đăng ký', 'onboard-household--read.html', False), '<a href="#">Tra lại mã</a><a href="onboard-help.html">Gọi chị Thu</a>'), 2)

UNREG = main('Đăng ký hộ kinh doanh trước', (
    '    <ul class="r-gate">' + gate_row('wait', '', 'Nộp ở UBND xã, phường nơi kinh doanh', 'hoặc trên Cổng dịch vụ công quốc gia')
    + '</ul>\n    <div class="c-options r-model" role="group" aria-label="Giấy tờ chị chuẩn bị">'
    + opt(True, 'Căn cước của chủ hộ', 'bản gốc', kind='checkbox') + opt(False, 'Tên hộ muốn đặt', 'ví dụ: Đặc sản Cao Nguyên An Nhiên', kind='checkbox')
    + opt(False, 'Ngành nghề', 'bán buôn, bán lẻ thực phẩm', kind='checkbox') + opt(False, 'Địa điểm kinh doanh', 'giấy tờ nhà hoặc hợp đồng thuê', kind='checkbox') + '</div>\n'
    '    <section class="c-card c-card--tight r-onb-hero" aria-labelledby="ur-h"><h2 class="c-card__title" id="ur-h">Lịch hẹn với chị Thu (nhân viên OPC)</h2>'
    '<p class="r-open__head"><b>Thứ Năm 02/07 · 8:00 · tại UBND phường</b><button class="c-btn" type="button">Đổi giờ</button></p></section>\n'
    '    <p class="c-say">Trong lúc chờ, chị vẫn nhập hàng và giá vào OPC. Bán hàng và hoá đơn mở khi có giấy đăng ký.</p>\n'
    '    <p class="u-meta">Thủ tục theo Nghị định 168/2025/NĐ-CP · nhân viên OPC kiểm giấy tờ mới nhất.</p>'),
    'Hộ kinh doanh cần giấy đăng ký trước khi bán hàng.')
shell('onboard-household--unregistered', 'Đăng ký · Chưa có giấy đăng ký', 'onboard-household.html', UNREG,
      foot(btn('Hẹn nhân viên OPC', 'onboard-help.html', False), '<a href="#">Mở Cổng dịch vụ công</a><a href="onboard-household.html">Tôi đã có giấy</a>'), 2)
for old in ('onboard-household--open',):
    if P(old).exists():
        P(old).unlink()

# ================================================================== 3 · Cách bán (model page = the template for every other step screen: keep its structure)
N_NEED, N_OPT = count('new', 'need'), count('new', 'optional')
MODEL = main('Chị bán thế nào?', (
    '    <section aria-labelledby="m-sell"><h2 class="c-card__title" id="m-sell">Bán cho ai</h2><div class="c-options r-model" role="group" aria-labelledby="m-sell">'
    + opt(True, 'Khách đến mua tại chỗ', 'trả tiền mặt hoặc QR', kind='checkbox')
    + opt(True, 'Khách sỉ, khách sạn, nhà hàng', 'đặt qua Zalo, giá riêng, cần hoá đơn', kind='checkbox')
    + opt(False, 'Online, trên sàn', 'Shopee, TikTok Shop', kind='checkbox') + '</div></section>\n'
    '    <section aria-labelledby="m-src"><h2 class="c-card__title" id="m-src">Hàng từ đâu</h2><div class="c-options r-model" role="group" aria-labelledby="m-src">'
    + opt(True, 'Mua về bán lại', 'từ nhà cung cấp, HTX', kind='checkbox')
    + opt(False, 'Tự làm, chế biến', 'OPC ghi như hàng mua về · chế biến chi tiết có sau', kind='checkbox') + '</div></section>\n'
    '    ' + yesno('emp', 'Có thuê người làm không?', 'Có', 'Không', False, 'Có thuê thì OPC nhắc bảo hiểm xã hội cho người làm.', '')
    + '\n    ' + yesno('food', 'Có bán thực phẩm không?', 'Có', 'Không', True, 'OPC nhắc giấy an toàn thực phẩm và theo dõi hạn dùng.', '')))
shell('onboard-model', 'Đăng ký · Cách bán', 'onboard-household--read.html', MODEL,
      foot(f'<p class="c-decide__result r-model__sum" role="status">OPC lập danh sách: <b>{N_NEED} việc bắt buộc</b> · {N_OPT} việc tuỳ chọn, bỏ qua được</p>\n    '
           + btn('Tiếp tục', 'onboard-features.html'), '<a href="onboard-help.html">Chưa chắc — nhờ nhân viên OPC</a>'), 3)

# ================================================================== 4 · Thuế và tài khoản
GOV = main('VNeID và tài khoản thuế của chủ hộ', (
    '    ' + yesno('vneid', 'Chị đã có VNeID mức 2 chưa?', 'Đã có', 'Chưa có', True, 'Chưa có thì nhân viên OPC hướng dẫn kích hoạt ở công an xã.', '')
    + '\n    ' + yesno('etax', 'Chị đã có tài khoản thuế điện tử (eTax) chưa?', 'Đã có', 'Chưa có', False, '', 'OPC hướng dẫn đăng ký eTax Mobile bằng VNeID, khoảng 5 phút.')
    + '\n    <div class="c-banner c-banner--pend" role="note"><span class="c-banner__pic">' + ic('i-clock') + '</span><span class="c-banner__text"><strong class="c-banner__title">Hạn liên kết eTax với VNeID: 31/12/2026</strong><span class="c-banner__body">OPC không hỏi và không giữ mật khẩu của chị.</span></span></div>'),
    'Chị khai và nộp thuế trên eTax của nhà nước. OPC chuẩn bị số liệu và hướng dẫn.')
shell('onboard-gov', 'Đăng ký · VNeID và eTax', 'onboard-features.html', GOV, foot(btn('Tiếp tục', 'onboard-tax.html'), '<a href="onboard-help.html">Nhờ nhân viên OPC</a>'), 4)

TAX = main('Hộ khai thuế thế nào', (
    '    ' + field('tx-ytd', 'Doanh thu từ 01/01 đến trước ngày dùng OPC', '380.000.000', 'gồm tiền mặt và chuyển khoản · ước tính được', mode='numeric', suffix='đồng') + '\n'
    '    <section class="c-card c-card--tight" aria-labelledby="tx-s"><div class="c-card__head"><h2 class="c-card__title" id="tx-s">OPC gợi ý</h2><span class="c-sim">Chờ kế toán xác nhận</span></div>'
    '<dl class="c-kv"><dt>Cả năm ước khoảng</dt><dd>760 triệu</dd><dt>Kỳ khai</dt><dd>theo quý</dd><dt>Hoá đơn</dt><dd>cần cho khách sỉ</dd></dl></section>\n'
    '    <div class="c-options" role="radiogroup" aria-label="Kỳ khai chị đã đăng ký">'
    + opt(True, 'Đúng, tôi khai theo quý', '') + opt(False, 'Tôi khai theo tháng', '') + opt(False, 'Chưa khai lần nào hoặc chưa chắc', 'kế toán hoặc nhân viên OPC xem cùng chị') + '</div>'),
    'Từ năm 2026 hộ tự khai doanh thu. OPC dùng số này để nhắc đúng kỳ và đúng mốc.')
shell('onboard-tax', 'Đăng ký · Cách khai thuế', 'onboard-gov.html', TAX, foot(btn('Tiếp tục', 'onboard-bankacc.html'), '<a href="onboard-help.html">Nhờ kế toán xem</a>'), 4)

BANKACC = main('Tài khoản dùng cho kinh doanh', (
    '    <ul class="r-gate">' + gate_row('ok', 'Đã báo cơ quan thuế', 'MB 0901 2345 678', 'chủ hộ Phạm Thị An').replace('<span class="r-gate__act"></span>', '<span class="r-gate__act"><button class="c-btn" type="button" aria-label="Sửa tài khoản MB 0901 2345 678">Sửa</button><button class="c-btn c-btn--quiet" type="button" aria-label="Bỏ tài khoản MB 0901 2345 678">Bỏ</button></span>') + '</ul>\n'
    '    <a class="c-btn c-btn--block" href="#">Thêm tài khoản hoặc ví điện tử</a>\n'
    '    <div class="c-banner c-banner--pend" role="note"><span class="c-banner__pic">' + ic('i-shield') + '</span><span class="c-banner__text"><strong class="c-banner__title">Mọi tài khoản, ví nhận tiền bán hàng phải báo cơ quan thuế</strong><span class="c-banner__body">Không bắt buộc tài khoản đứng tên hộ.</span></span></div>\n'
    '    <section class="c-card c-card--tight" aria-labelledby="ba-o"><div class="c-card__head"><h2 class="c-card__title" id="ba-o">Tuỳ chọn: nối để tiền về tự khớp</h2></div>'
    '<p class="c-sub">Làm tay vẫn được: chị xác nhận tiền theo sao kê.</p><div class="c-decide__acts"><a class="c-btn" href="onboard-bank.html">Nối ngân hàng</a><a class="r-skip" href="onboard-invoice.html">Bỏ qua, làm tay</a></div></section>'))
shell('onboard-bankacc', 'Đăng ký · Tài khoản kinh doanh', 'onboard-tax.html', BANKACC, foot(btn('Tiếp tục', 'onboard-invoice.html'), '<a href="#">Cách báo tài khoản cho cơ quan thuế</a>'), 4)

# ================================================================== 5 · Hoá đơn
INV = main('Hoá đơn điện tử', (
    '    <div class="c-options" role="radiogroup" aria-label="Cách xuất hoá đơn">'
    + opt(True, 'Qua nhà cung cấp hoá đơn', 'Hilo cho khách tại chỗ, X Invoice cho khách sỉ · OPC nối sẵn', 'OPC gợi ý')
    + opt(False, 'Hoá đơn miễn phí của cơ quan thuế', '12 tháng · chỉ khi hộ đủ điều kiện · nhân viên OPC kiểm giúp')
    + opt(False, 'Đã có hoá đơn điện tử ở nơi khác', 'nối tài khoản chị đang dùng') + '</div>\n'
    '    <p class="u-meta">Không chọn "chưa cần" được: chị bán cho khách sỉ, khách cần hoá đơn.</p>'),
    'Hoá đơn điện tử chỉ xuất được qua một nhà cung cấp đã đăng ký với cơ quan thuế. Đây là kết nối bắt buộc duy nhất khi mở hộ.')
shell('onboard-invoice', 'Đăng ký · Hoá đơn điện tử', 'onboard-bankacc.html', INV, foot(btn('Tiếp tục', 'onboard-invoice--register.html'), '<a href="onboard-help.html">Nhờ nhân viên OPC</a>'), 5)

REG = main('Đăng ký dùng hoá đơn', (
    '    <div class="c-banner c-banner--pend" role="status"><span class="c-banner__pic">' + ic('i-clock') + '</span><span class="c-banner__text"><strong class="c-banner__title">Đang chờ cơ quan thuế chấp nhận</strong><span class="c-banner__body">Đã gửi 10:20 · thường 1 ngày làm việc. Chị không cần chờ: bấm Tiếp tục, OPC báo khi có kết quả.</span></span></div>\n'
    '    <ol class="r-gate">' + gate_row('ok', 'Xong', 'Chữ ký số', 'VNPT SmartCA trên VNeID · hoá đơn máy tính tiền không cần')
    + gate_row('ok', 'Xong', 'Nối Hilo và X Invoice', 'chị đăng nhập ở trang của nhà cung cấp, OPC không giữ mật khẩu')
    + gate_row('wait', 'Chờ cơ quan thuế', 'Gửi tờ đăng ký dùng hoá đơn điện tử', 'mẫu 01/ĐKTĐ-HĐĐT · đã gửi 10:20')
    + gate_row('wait', 'Sau khi được chấp nhận', 'Ký hiệu hoá đơn', 'nhà cung cấp cấp, OPC tự điền') + '</ol>\n'
    '    <p class="c-say">Chờ chấp nhận không chặn bước tiếp. Hoá đơn bật khi có kết quả.</p>'))
shell('onboard-invoice--register', 'Đăng ký · Đăng ký hoá đơn', 'onboard-invoice.html', REG, foot(btn('Tiếp tục', 'onboard-products.html'), '<a href="connections--casso.html">Xem cách nối nhà cung cấp</a>'), 5)

# ================================================================== 6 · Số đầu kỳ
for n in ('onboard-products', 'onboard-help'):
    patch(n, [('Chọn từ mẫu Hải sản khô', 'Chọn từ mẫu đặc sản'), ('24 món hay bán, sửa giá cho đúng', '24 món hay bán, chị sửa giá cho đúng'),
              ('<button class="c-btn c-btn--act c-btn--block" type="button">Tiếp tục</button>', '<a class="c-btn c-btn--act c-btn--block" href="onboard-products--review.html">Tiếp tục</a>'),
              ('<div class="r-onboard__alt"><a href="#">Để sau</a>', '<div class="r-onboard__alt"><a href="onboard-opening--empty.html">Để sau</a>')])
patch('onboard-products--review', [('<button class="c-btn c-btn--act c-btn--block c-btn--wrap" type="button">Lưu 2 món · 1 giá chưa xác nhận</button>',
                                    '<a class="c-btn c-btn--act c-btn--block c-btn--wrap" href="onboard-opening.html">Lưu 2 món · 1 giá chưa xác nhận</a>')])

ROWS = ''.join(f'<li class="r-open__i"><span class="r-open__n"><b>{n}</b><small>{u}</small></span>'
               f'<label class="u-sr" for="op-{i}">Số {u} đã đếm của {n}</label><input class="c-field__input r-open__q" id="op-{i}" inputmode="numeric" value="{q}"></li>'
               for i, (n, u, q) in enumerate([('Bò một nắng 500g', 'gói', '40'), ('Muối kiến vàng 100g', 'hũ', '60')]))
OPEN = main('Số đầu kỳ ngày 01/07/2026', (
    '    <section aria-labelledby="op-s"><div class="r-open__head"><h2 class="c-card__title" id="op-s">Tồn đã đếm</h2><a class="c-btn" href="onboard-products.html">' + ic('i-plus') + 'Thêm món khác</a></div>'
    '<p class="u-meta">2 món từ bảng giá chị vừa chụp</p><ul class="r-open">' + ROWS + '</ul></section>\n'
    '    ' + field('op-cash', 'Tiền mặt đang có', '2.500.000', '', mode='numeric', suffix='đồng') + '\n'
    '    ' + field('op-bank', 'Tiền trong tài khoản MB', '18.400.000', 'theo sao kê ngày 30/06', mode='numeric', suffix='đồng') + '\n'
    '    <dl class="c-kv"><dt>Khách đang nợ</dt><dd>0 · thêm sau ở Công nợ</dd><dt>Chị đang nợ nhà cung cấp</dt><dd>0</dd></dl>'),
    'Đếm thật một lần, chị xác nhận. Hộ mới chưa có gì thì chọn "Bắt đầu từ 0" ở dưới.')
EMPTY = main('Số đầu kỳ ngày 01/07/2026', (
    '    <section class="c-card c-card--tight r-onb-hero" aria-labelledby="oe-h"><h2 class="c-card__title" id="oe-h">Chưa có món hàng nào</h2>'
    '<p class="c-sub">Tồn đầu kỳ cần danh sách hàng. Chị thêm hàng trước, hoặc bắt đầu từ 0 rồi nhập hàng khi có đơn mua đầu tiên.</p>'
    '<div class="c-decide__acts"><a class="c-btn c-btn--act" href="onboard-products.html">Thêm hàng</a></div></section>\n'
    '    ' + field('op-cash', 'Tiền mặt đang có', '', 'để trống nếu chưa biết', mode='numeric', suffix='đồng', ph='0')),
    'Chị đã bỏ qua phần thêm hàng.')
shell('onboard-opening--empty', 'Đăng ký · Số đầu kỳ (chưa có hàng)', 'onboard-products.html', EMPTY,
      foot('<a class="c-btn c-btn--block" href="onboard-done.html">Bắt đầu từ 0</a>', '<a href="onboard-help.html">Nhân viên OPC đếm cùng</a>'), 6)
shell('onboard-opening', 'Đăng ký · Số đầu kỳ', 'onboard-products--review.html', OPEN,
      foot(btn('Xác nhận số đầu kỳ', 'onboard-done.html', False), '<a href="onboard-opening--empty.html">Bắt đầu từ 0</a><a href="onboard-help.html">Nhân viên OPC đếm cùng</a>'), 6)

# ================================================================== done → giao dịch đầu tiên
REC = [('Số điện thoại và đồng ý dữ liệu', '0935 112 418'), ('Hộ kinh doanh', 'MST 5901234567 · bán buôn, bán lẻ thực phẩm'), ('Cách bán', 'tại chỗ · khách sỉ · mua về bán · có thực phẩm'),
       ('Thuế và tài khoản', 'khai theo quý · MB đã báo cơ quan thuế'), ('Hoá đơn', 'Hilo, X Invoice · chờ cơ quan thuế chấp nhận'), ('Hàng và số đầu kỳ', '2 món · tồn đã đếm · tiền 20.900.000 đồng')]
rec = ''.join(f'<li class="c-todo__item c-todo__item--done"><span class="c-todo__n" aria-hidden="true">{CK}</span><div><h3 class="c-todo__t">{t}</h3><p class="c-todo__m">{m}</p></div></li>' for t, m in REC)
DONE = ('<main class="r-onboard__body">\n    <h1 class="r-onboard__title">Hộ Đặc sản An Nhiên đã sẵn sàng</h1>\n'
        f'    <details class="r-onboard__recap"><summary><span class="c-sign c-sign--ok"><span class="c-sign__pic">{CK}</span>6/6 bước</span><span class="u-meta">Xem lại 6 bước</span></summary>'
        f'<ol class="c-todo" aria-label="Đã làm xong">{rec}</ol></details>\n'
        '    <div class="c-options" role="radiogroup" aria-label="Giao dịch đầu tiên">' + opt(True, 'Bán thử một đơn', 'OPC hướng dẫn từng bước, đơn thử không vào sổ')
        + opt(False, 'Nhập một đơn mua', 'hàng mới về từ nhà cung cấp') + '</div>\n'
        f'    <p class="u-meta">Sau đó: còn {count("new", "need")} việc bắt buộc trong Sẵn sàng, như khách và nhà cung cấp, nhóm chi phí, cách giao. Việc tuỳ chọn bỏ qua được.</p>\n'
        '    <p class="r-onboard__saved">Đã lưu — làm tiếp lúc nào cũng được</p>\n  </main>')
s = P('onboard-done').read_text()
s = re.sub(r'<main class="r-onboard__body">[\s\S]*?</main>', lambda m: DONE, s, count=1)
s = re.sub(r'<footer class="r-onboard__foot">[\s\S]*?</footer>', lambda m: foot(btn('Bắt đầu', 'onboard-firstsale.html'), '<a href="readiness--new.html">Xem danh sách Sẵn sàng</a>'), s, count=1)
P('onboard-done').write_text(sprite(s))

# ================================================================== gates (no step bar): xác minh chủ hộ, nối ngân hàng — both optional
VP = [('Để chỉ chị đồng ý được các kết nối và ký. Chưa xác minh thì chị vẫn thêm hàng và bán tiền mặt.', 'Chỉ cần khi ngân hàng hoặc nhà cung cấp hoá đơn đòi. Không xác minh thì OPC vẫn dùng đủ.'),
      ('chưa nối được ngân hàng và hoá đơn', 'bỏ qua, làm sau khi có bên đòi'), ('Chị vẫn thêm hàng và bán tiền mặt được. Chỉ nối ngân hàng và hoá đơn cần xác minh.', 'Không xác minh vẫn dùng OPC được.')]
SAFE = '<p class="u-meta">OPC chỉ lưu họ tên và số căn cước (mã hoá), không lưu ảnh.</p>'
V = main('Xác minh chủ hộ', '    <div class="c-options" role="radiogroup" aria-label="Cách xác minh">'
         + opt(False, ic('i-phone') + 'Tự xác minh trên điện thoại', 'nhanh nhất · cần căn cước gắn chip và máy có NFC · khoảng 2 phút')
         + opt(False, ic('i-people') + 'Nhân viên OPC xác minh cùng chị', 'dễ nhất · chị Thu mang máy đọc thẻ · Thứ Năm 02/07, 8:00')
         + opt(False, ic('i-clock') + 'Để sau', 'không mất gì · làm khi ngân hàng hoặc bên hoá đơn đòi') + '</div>\n    <p class="r-yn__hint" id="vf-why">Chọn một cách để tiếp tục.</p>\n    ' + SAFE,
         'Chỉ cần khi ngân hàng hoặc nhà cung cấp hoá đơn đòi. Không xác minh thì OPC vẫn dùng đủ.')
shell('onboard-verify', 'Sẵn sàng · Xác minh chủ hộ', 'readiness--new.html', V,
      foot('<button class="c-btn c-btn--act c-btn--block" type="button" aria-disabled="true" aria-describedby="vf-why">Tiếp tục</button>', '<a href="help.html">Vì sao có bên đòi xác minh?</a>'), 4)
APP = main('Quét mã bằng app Cas ID', ('    <p class="c-say">Đang dùng chính điện thoại này? Nó không tự quét mã trên màn hình của nó được. Nhờ người thân quét giúp, hoặc chọn nhân viên OPC.</p>\n'
           '    <ol class="r-guide__mini"><li>Mở app Cas ID trên một điện thoại khác</li><li>Quét mã này, đặt căn cước gắn chip sau điện thoại</li><li>Bấm đồng ý chia sẻ họ tên và số căn cước cho OPC</li></ol>\n'
           '    <div class="c-qr c-qr--large"><img class="c-qr__img" src="../../../system/assets/qr-demo.svg" alt="Mã QR để quét bằng app Cas ID">'
           '<div class="c-qr__meta"><span class="c-qr__k">Mã hết hạn sau</span><span class="c-qr__amt">4:32</span></div>'
           '<p class="c-qr__status" aria-live="polite"><span class="c-qr__status-pic">' + ic('i-clock') + '</span>Đang chờ chị quét…</p></div>'))
shell('onboard-verify--app', 'Sẵn sàng · Quét mã Cas ID', 'onboard-verify.html', APP,
      foot('<a class="c-btn c-btn--block" href="onboard-verify--failed.html">Tạo mã mới</a>', '<a href="onboard-help.html">Nhân viên OPC xác minh cùng chị</a>'), 4)
FAIL = main('Chưa xác minh được', ('    <div class="c-banner c-banner--pend" role="status"><span class="c-banner__pic">' + ic('i-clock') + '</span><span class="c-banner__text"><strong class="c-banner__title">Mã đã hết 5 phút</strong>'
            '<span class="c-banner__body">Chưa mất gì cả. Chị tạo mã mới và quét lại.</span></span></div>\n'
            '    <ul class="r-gate">' + gate_row('wait', '', 'Máy không có NFC?', 'nhân viên OPC xác minh cùng chị bằng máy của họ')
            + gate_row('wait', '', 'Căn cước chưa kích hoạt chip?', 'nhân viên OPC hướng dẫn kích hoạt') + '</ul>\n'
            '    <p class="c-say">Không xác minh vẫn dùng OPC được.</p>'))
shell('onboard-verify--failed', 'Sẵn sàng · Chưa xác minh được', 'onboard-verify--app.html', FAIL,
      foot('<a class="c-btn c-btn--act c-btn--block" href="onboard-verify--app.html">Tạo mã mới</a>\n    <a class="c-btn c-btn--quiet c-btn--block" href="onboard-help.html">Hẹn nhân viên OPC · Thứ Năm 02/07</a>',
           '<a href="readiness--new.html">Để sau</a>'), 4)
for n in ('onboard-verify', 'onboard-verify--app', 'onboard-verify--failed'):
    if P(n).exists():
        patch(n, VP, sub=lambda s: unstep(s, 'Xác minh chủ hộ').replace('href="onboard-products.html">Để sau', 'href="readiness--new.html">Để sau'))
for n in ('onboard-bank', 'onboard-bank--done', 'onboard-bank--mismatch'):
    patch(n, [], sub=lambda s: unstep(s, 'Nối ngân hàng · tuỳ chọn'))

# staff view: same six steps
AS = ''.join(f'<li class="c-todo__item c-todo__item--done"><span class="c-todo__n" aria-hidden="true">{CK}</span><div><h3 class="c-todo__t">{t}</h3><p class="c-todo__m">{m}</p></div></li>' for t, m in
             [('Số điện thoại', 'Xong 10:01 · chị An đồng ý dữ liệu'), ('Hộ kinh doanh', 'Xong 10:03 · đọc từ ảnh giấy đăng ký'), ('Cách bán', 'Xong 10:05')])
AS += ''.join(f'<li class="c-todo__item{" c-todo__item--now" if i == 4 else ""}"{" aria-current=" + chr(34) + "step" + chr(34) if i == 4 else ""}><span class="c-todo__n" aria-hidden="true">{i}</span><div><h3 class="c-todo__t">{t}</h3><p class="c-todo__m">{m}</p></div></li>'
              for i, t, m in [(4, 'Thuế và tài khoản', 'Chị An chưa có tài khoản eTax · hướng dẫn đăng ký bằng VNeID'), (5, 'Hoá đơn', 'Tiếp theo'), (6, 'Số đầu kỳ', 'Tiếp theo · đếm tồn cùng chị An')])
AS_PANEL = ('<section class="c-card" aria-labelledby="as-qr"><div class="as-stack"><h2 class="c-card__title" id="as-qr">Đăng ký eTax cho chị An</h2>'
            '<ol class="r-guide__mini"><li>Mở eTax Mobile trên điện thoại chị An</li><li>Chọn đăng nhập bằng VNeID, chị An xác nhận trên VNeID</li><li>Kiểm mã số thuế 5901234567 khớp giấy đăng ký</li></ol>'
            '<p class="c-say">Nói với chị An: <b>OPC không cần mật khẩu eTax của chị.</b></p>'
            '<div class="as-wrap"><button class="c-btn" type="button">Đánh dấu đã có eTax</button><button class="c-btn c-btn--quiet" type="button">Làm sau</button></div></div></section>')
AS_PHONE = ('<section class="c-card c-card--tight" aria-labelledby="as-ph"><div class="c-card__head"><h2 class="c-card__title" id="as-ph">Trên điện thoại chị An</h2></div>'
            '<dl class="c-kv"><dt>Bước</dt><dd>Bước 4/6 · Thuế và tài khoản</dd><dt>Số điện thoại</dt><dd>0935 112 418</dd></dl></section>')
patch('onboard-assisted', [], sub=lambda s: re.sub(r'<ol class="c-todo">.*?</ol>', lambda m: f'<ol class="c-todo">{AS}</ol>', s, count=1, flags=re.S)
      .replace('Bước 4/5 · làm theo thứ tự số', 'Bước 4/6 · làm theo thứ tự số'))
patch('onboard-assisted', [], sub=lambda s: re.sub(r'<section class="c-card c-card--tight" aria-labelledby="as-ph">.*?</section>', lambda m: AS_PHONE, re.sub(r'<section class="c-card" aria-labelledby="as-qr">.*?</section>', lambda m: AS_PANEL, s, count=1, flags=re.S), count=1, flags=re.S))
print('onboard_flow v7: done')

"""v5.0.0 · Kết nối, the whole catalog + credential handling.  Usage: python3 pages_connect4.py — after pages_connect3b.py.
  connections--add        "Thêm cách nối": the ways to do each feature (providers.py), grouped by FEATURE; connections--request = dialog over it
  connections--casso      "Nối qua Casso" hand-off (Viettel S-Invoice): what to prepare, what OPC never sees
  connections--key        "Dán khoá kết nối" (payOS): fields, where to find them, webhook for the provider to call; --key--error
  connections--guide      step-by-step guide per provider (payOS, S-Invoice) — rendered from GUIDES
  connections--manage     one key-based account: keys masked, webhook, test, rotate, remove; --rotate / --remove dialogs
  platform-providers      QNSC console: the registry (enable, hide, remove, who is connected)
  platform-provider       one provider on the platform side (Casso): platform keys, webhook, visibility
  platform-provider--remove / --new
Guide steps for third-party portals are written from general knowledge and MUST be checked against each portal before release (NOTES)."""
from connect_lib import *
from providers import CAT, GROUPS, MODES, GATE, GROUP_NAME, SHORT

# ------------------------------------------------------------------ 1 · "Thêm cách nối": grouped by FEATURE, providers are plain text (v5.1.1)
from capabilities import FEATS
LINK = {'zalo-oa': 'connections--account.html', 'payos': 'connections--manage.html', 'xinvoice': 'connections--detail.html', 'ghtk': 'connections--info.html',
        'sinvoice': 'connections--casso.html', 'gdt-hub': 'connections--provider.html', 'mb': '', 'hilo': '', 'cas-id': ''}
NEW = {'can': '<a class="c-btn" href="{h}">Nối</a>', 'ok': sign('pass', 'i-check', 'Đã nối'), 'sim': '<span class="c-sim">Mô phỏng</span>',
       'soon': '<button class="c-btn c-btn--quiet" type="button">Báo tôi</button>'}
NEW['partner'] = NEW['soon']
ORDER = {'ok': 0, 'can': 1, 'sim': 2}


def tile(c):
    h = LINK.get(c['id'], '')
    st = c['status']
    name = f'<a class="r-dir__link" href="{h}">{c["name"]}</a>' if h else c['name']
    badge = NEW[st].replace('{h}', h or 'connections--provider.html')
    if c['mode'] == 'opc':
        badge = '<span class="u-meta">Có sẵn</span>'
    return (f'<li class="r-dir__p r-dir__p--{"soon" if st == "partner" else st}"><span class="r-dir__nb"><b class="r-dir__n">{name}</b><small>{SHORT[c["mode"]]}</small></span>'
            f'<span class="r-dir__st">{badge}</span></li>')


def pill(c):
    return f'<li><button class="r-dir__pill" type="button" aria-label="Báo tôi khi có {c["name"]}">{c["name"]}</button></li>'


def group(i, f):
    ps = [BY_ID[p] for p in f['choices']]
    live = sorted([c for c in ps if c['status'] in ORDER], key=lambda c: ORDER[c['status']])
    soon = [c for c in ps if c['status'] not in ORDER]
    body = '<ul class="r-dir__list">' + ''.join(tile(c) for c in live) + '</ul>' if live else ''
    more = ('<div class="r-dir__soon"><p class="u-meta">Sắp có</p><ul class="r-dir__pills">' + ''.join(pill(c) for c in soon) + '</ul></div>') if soon else ''
    return (f'<section class="r-dir__g" aria-labelledby="g{i}"><h2 class="r-dir__h" id="g{i}">{f["name"]}</h2>'
            f'<p class="c-sub">{f["what"]}</p>{body}{more}</section>')


BY_ID = {c['id']: c for c in CAT}
n_all = len(CAT)
ADD = (head('Thêm cách nối', 'Chọn việc chị muốn làm · OPC gợi ý cách phù hợp với hộ của chị', '<a class="c-btn" href="connections--category.html">Về Việc OPC làm</a>')
       + '<div class="page">' + tabs('Theo nhóm việc')
       + '<label class="c-search c-search--strong r-dir__find">' + ic('i-search') + '<span class="u-sr">Tìm việc hoặc nơi nối</span><input class="c-search__input" type="search" placeholder="Tìm: nhận tiền, giao hàng, hoá đơn…"></label>'
       + '<nav class="r-jump" aria-label="Nhảy tới việc">' + ''.join(f'<a class="r-jump__a" href="#g{i}">{f["name"]}</a>' for i, f in enumerate(FEATS)) + '</nav>'
       + ''.join(group(i, f) for i, f in enumerate(FEATS))
       + '<p class="c-sub r-dir__help">Chưa thấy cách chị cần? <a href="connections--request.html">Nói với OPC</a> hoặc <a href="help.html">nhờ chị Thu</a> nối giúp.</p></div>')
save('connections--add', 'Kết nối · Thêm cách nối', ADD)
print('connect4: add-by-feature', len(FEATS))
# ---- "Chị cần nối với nơi nào?": dialog over the directory (moved here from pages_connect3 so it sits on the current page)
DLG = ('<div class="c-dialog" role="dialog" aria-modal="true" aria-labelledby="rq-t"><div class="c-dialog__panel"><div class="c-dialog__head"><div><span class="c-dialog__k">Thêm kết nối</span>'
       '<h2 class="c-dialog__title" id="rq-t" tabindex="-1">Chị cần nối với nơi nào?</h2></div><button class="c-icon-btn" type="button" aria-label="Đóng">' + ic('i-x') + '</button></div>'
       '<div class="c-dialog__body"><div class="c-field"><label class="c-field__label" for="rq-n">Tên nơi chị muốn nối</label><div class="c-field__control"><input class="c-field__input" id="rq-n" placeholder="Ví dụ: Viettel Post"></div></div>'
       '<div class="c-field"><label class="c-field__label" for="rq-w">Chị dùng để làm gì?</label><div class="c-field__control"><input class="c-field__input" id="rq-w" placeholder="Ví dụ: giao hàng đi Quy Nhơn"></div></div>'
       '<p class="c-sub">OPC báo chị khi có. Nhiều hộ cùng yêu cầu thì được làm trước.</p></div>'
       '<div class="c-dialog__foot"><button class="c-btn" type="button">Huỷ</button><button class="c-btn c-btn--act" type="button">Gửi yêu cầu</button></div></div></div>')
save('connections--request', 'Kết nối · Nói với OPC', ADD, overlay=DLG)



# ------------------------------------------------------------------ shared bits for the credential screens
def fld(fid, label, value='', hint='', secret=False, bad=False, ro=False, act=''):
    a = f'<button class="c-btn c-btn--quiet" type="button">{act}</button>' if act else (f'<button class="c-btn c-btn--quiet" type="button" aria-label="Hiện {label}">Hiện</button>' if secret else '')
    ty = 'password' if secret else 'text'
    ro = ' readonly' if ro else ''
    return (f'<div class="c-field"{" data-invalid" if bad else ""}><label class="c-field__label" for="{fid}">{label}</label><div class="c-field__control">'
            f'<input class="c-field__input" id="{fid}" type="{ty}" value="{value}" autocomplete="off" spellcheck="false"{ro}{" aria-invalid=\"true\"" if bad else ""}>{a}</div>'
            f'<span class="c-field__hint">{hint}</span></div>')


def side(title, items, tone='ok'):
    return (f'<aside class="r-tower__detail" aria-labelledby="sd"><h2 class="r-tower__t" id="sd">{title}</h2><ul class="r-gate">'
            + ''.join(row(tone, '', t, m) for t, m in items) + '</ul></aside>')


def sw(on, t, sub):
    return (f'<li class="c-list__row"><button class="c-switch c-switch--row" type="button" role="switch" aria-checked="{"true" if on else "false"}">'
            f'<span class="c-switch__label">{t}<span class="c-switch__sub">{sub}</span></span><span class="c-switch__track" aria-hidden="true"></span></button></li>')


def dialog(kick, title, body, foot, did):
    return (f'<div class="c-dialog" role="dialog" aria-modal="true" aria-labelledby="{did}"><div class="c-dialog__panel"><div class="c-dialog__head"><div><span class="c-dialog__k">{kick}</span>'
            f'<h2 class="c-dialog__title" id="{did}" tabindex="-1">{title}</h2></div><button class="c-icon-btn" type="button" aria-label="Đóng">' + ic('i-x') + '</button></div>'
            f'<div class="c-dialog__body">{body}</div><div class="c-dialog__foot">{foot}</div></div></div>')


# ------------------------------------------------------------------ 2 · Nối qua Casso (Viettel S-Invoice)
CASSO = (crumb(('Kết nối', 'connections.html'), ('Thêm cách nối', 'connections--add.html'), 'Viettel S-Invoice')
         + dhead('Nối Viettel S-Invoice', sign('pend', 'i-lock', 'Chỉ chị An'), 'Qua Casso · hoá đơn có mã cho khách sỉ',
                 '<a class="c-btn c-btn--act" href="connections--testing.html">Mở trang nối của Casso</a>')
         + grid(card('cb', 'Chị cần có', '<ul class="r-gate">' + row('ok', '', 'Tài khoản S-Invoice của hộ', 'tên đăng nhập và mật khẩu chị dùng để vào S-Invoice')
                     + row('ok', '', 'Mã số thuế 5901234567', 'đã có trong hồ sơ hộ')
                     + row('wait', '', 'Loại tài khoản doanh nghiệp', 'Casso chỉ nối S-Invoice loại này · hộ chưa có thì dùng Hilo hoặc X Invoice') + '</ul>', '<a class="c-link" href="connections--guide-casso.html">Xem hướng dẫn</a>')
                + card('ch', 'Chị sẽ làm', '<ol class="r-guide__mini"><li>Bấm <b>Mở trang nối của Casso</b></li><li>Nhập tài khoản S-Invoice ở trang đó</li><li>Quay lại OPC, OPC đọc thử một hoá đơn</li></ol>'),
                side('OPC không bao giờ', [('Thấy mật khẩu S-Invoice', 'chị nhập ở trang của Casso'), ('Lưu mật khẩu', 'OPC chỉ nhận một mã truy cập'),
                                           ('Tự phát hành hoá đơn', 'chị bấm, OPC chuẩn bị')]).replace('r-gate__i--ok', 'r-gate__i--ok')))
save('connections--casso', 'Kết nối · Nối qua Casso', '<div class="page">' + CASSO + '</div>')

# ------------------------------------------------------------------ 3 · Dán khoá (payOS) + lỗi
WEBHOOK = ('https://hook.opc.vn/w/an-nhien/payos', 'whsec_••••••••••a41c')


def key_page(err=False):
    f1 = fld('k1', 'Client ID', '3f9a2c10-7b1e-4c55-9a20-5d8e1f0a7c42', 'payOS → Kênh thanh toán → Cài đặt')
    f2 = fld('k2', 'API Key', '••••••••••••••••••••', 'khoá dài, bắt đầu bằng chữ và số', True)
    f3 = fld('k3', 'Checksum Key', '••••••••••••••••••••', 'Checksum Key không đúng — payOS từ chối chữ ký thử. Kiểm lại ký tự đầu và cuối.' if err else 'OPC dùng khoá này để kiểm chữ ký payOS gửi về', True, bad=err)
    banner = ('<div class="c-banner c-banner--err" role="alert"><span class="c-banner__pic">' + ic('i-alert') + '</span><span class="c-banner__text"><strong class="c-banner__title">payOS chưa nhận khoá này</strong>'
              '<span class="c-banner__body">Chưa lưu gì. Chị sửa Checksum Key rồi thử lại, hoặc xem <a href="connections--guide.html">hướng dẫn</a>.</span></span></div>') if err else ''
    return ('<div class="page">' + crumb(('Kết nối', 'connections.html'), ('Thêm cách nối', 'connections--add.html'), 'payOS')
            + dhead('Nối payOS', sign('pend', 'i-lock', 'Chỉ chị An'), 'Dán khoá kết nối · link thanh toán cho khách ở xa',
                    '<button class="c-btn c-btn--act" type="button">Thử kết nối</button>')
            + banner
            + grid(card('kk', 'Khoá từ payOS', '<div class="r-keys">' + f1 + f2 + f3 + '</div>', '<a class="c-link" href="connections--guide.html">Cách lấy khoá</a>')
                   + card('wh', 'Dán vào payOS · nơi nhận báo tiền', '<div class="r-keys">' + fld('w1', 'Địa chỉ nhận báo tiền', WEBHOOK[0], 'payOS gọi địa chỉ này khi khách trả tiền', ro=True, act='Chép')
                                                                     + '</div>'),
                   side('Khoá của chị được giữ thế nào', [('Cất kín, mã hoá', 'chỉ chị An nhập được'), ('Chỉ hiện 4 số cuối', 'sau khi lưu, OPC không hiện lại khoá đầy đủ'),
                                                          ('Đổi hoặc xoá bất cứ lúc nào', 'ở trang Kết nối'), ('Không chuyển tiền', 'khoá chỉ dùng để tạo link và nhận báo tiền')])) + '</div>')


save('connections--key', 'Kết nối · Dán khoá payOS', key_page())
save('connections--key--error', 'Kết nối · Khoá payOS sai', key_page(True))



# ------------------------------------------------------------------ 4 · guides (data → page). Steps for third-party portals are from general knowledge: verify before release.
GUIDES = {
    'payos': dict(page='connections--guide', title='Lấy khoá payOS', name='payOS', time='Khoảng 5 phút', back=('Tôi đã có khoá, quay lại', 'connections--key.html'),
                  need=[('Tài khoản payOS của hộ', 'đã đăng ký và đăng nhập được'), ('Tài khoản ngân hàng nhận tiền', 'đã liên kết với payOS')],
                  steps=[('Ở payOS', 'Mở kênh thanh toán của hộ', 'Chưa có thì tạo một kênh mới.', 'Thấy tên kênh và trạng thái đang hoạt động.'),
                         ('Ở payOS', 'Chép ba khoá: Client ID, API Key, Checksum Key', 'Nằm trong phần cài đặt của kênh.', 'Chỉ gửi cho OPC qua trang nối, không gửi qua Zalo hay email.'),
                         ('Ở OPC', 'Dán ba khoá vào trang nối, bấm Thử kết nối', 'OPC chỉ đọc, chưa tạo giao dịch nào.', 'Thấy “payOS đã nhận khoá”.'),
                         ('Ở payOS', 'Dán địa chỉ nhận báo tiền mà OPC đưa vào ô webhook của kênh', 'Bấm xác nhận ở payOS.', 'payOS báo xác nhận thành công.'),
                         ('Ở OPC', 'Bấm Lưu kết nối', 'Từ giờ link thanh toán tạo được, tiền về tự ghi.', 'Thấy payOS trong danh sách Đã nối.')],
                  errs=[('Client ID hoặc API Key không đúng', '', 'chép lại từ cài đặt kênh, đủ ký tự'),
                        ('Checksum Key không đúng', '', 'chép lại, đủ từ ký tự đầu đến cuối'),
                        ('Khách trả tiền mà OPC không nhận được báo', '', 'xác nhận lại địa chỉ nhận báo tiền ở payOS'),
                        ('Nghi khoá bị lộ', '', 'tạo khoá mới ở payOS, rồi Đổi khoá ở OPC')]),
    'sinvoice': dict(page='connections--guide-casso', title='Nối Viettel S-Invoice qua Casso', name='S-Invoice', time='Khoảng 5 phút', back=('Về trang nối', 'connections--casso.html'),
                     need=[('Tài khoản S-Invoice loại doanh nghiệp', 'tên đăng nhập và mật khẩu'), ('Chị An cầm điện thoại', 'Casso có thể hỏi xác nhận')],
                     steps=[('Ở OPC', 'Bấm Mở trang nối của Casso', 'Trang mở ra là của Casso, không phải của OPC.', 'Thấy danh sách nơi có thể nối.'),
                            ('Ở Casso', 'Chọn nhà cung cấp hoá đơn, rồi Viettel S-Invoice', 'Chọn loại doanh nghiệp.', 'Thấy ô tên đăng nhập và mật khẩu.'),
                            ('Ở Casso', 'Nhập tên đăng nhập và mật khẩu S-Invoice, bấm “Cho phép”', 'OPC không thấy hai thông tin này.', 'Casso báo đã liên kết và đưa chị về OPC.'),
                            ('Ở OPC', 'OPC đọc thử một hoá đơn', 'Chỉ đọc, không phát hành gì.', 'Thấy “Đã nối” kèm việc được phép làm.')],
                     errs=[('Tài khoản đã nối với app khác của Casso', '', 'mở Cas ID, cấp quyền cho OPC'),
                           ('Hoá đơn lập rồi vẫn “chưa gửi” thuế', '', 'bấm Hỏi lại, OPC không tự gửi lại'),
                           ('Casso báo loại tài khoản không phù hợp', '', 'dùng Hilo hoặc X Invoice, hoặc nhờ chị Thu')])}


def guide_page(g):
    steps = ''.join(f'<li class="r-guide__s"><div class="r-guide__b"><span class="r-guide__where">{w}</span><b>{t}</b><span>{d}</span><span class="r-guide__see">{see}</span></div></li>' for w, t, d, see in g['steps'])
    errs = ''.join(row('wait', '', m, f) for m, c, f in g['errs'])
    return ('<div class="page">' + crumb(('Kết nối', 'connections.html'), ('Thêm cách nối', 'connections--add.html'), 'Hướng dẫn ' + g['name'])
            + dhead(g['title'], '', g['time'] + ' · làm trên máy tính sẽ dễ hơn', f'<a class="c-btn c-btn--act" href="{g["back"][1]}">{g["back"][0]}</a>')
            + grid(card('gn', 'Chị cần có', '<ul class="r-gate">' + ''.join(row('ok', '', t, m) for t, m in g['need']) + '</ul>')
                   + card('gs', 'Các bước', f'<ol class="r-guide">{steps}</ol>'),
                   '<aside class="r-tower__detail" aria-labelledby="ge"><h2 class="r-tower__t" id="ge">Gặp lỗi</h2><ul class="r-gate">' + errs + '</ul>'
                   '<p class="c-sub">Có thể lệch nếu giao diện đổi. <a href="help.html">Nhờ chị Thu</a> làm cùng chị.</p></aside>') + '</div>')


for g in GUIDES.values():
    save(g['page'], 'Kết nối · ' + g['title'], guide_page(g))

# ------------------------------------------------------------------ 5 · manage a key-based account (payOS) + rotate / remove dialogs
def kv(k, v):
    return f'<dt>{k}</dt><dd>{v}</dd>'


def tlx(kind, src, time, what, who=''):
    w = f'<span class="c-timeline__who">{who}</span>' if who else ''
    return (f'<li class="c-timeline__item c-timeline__item--{kind}"><span class="c-timeline__time">{time}</span><span class="c-timeline__dot" aria-hidden="true"></span>'
            f'<span class="c-timeline__body"><span class="c-timeline__src">{src}</span><span class="c-timeline__what">{what}</span>{w}</span></li>')


def manage_main():
    return ('<div class="page">' + crumb(('Kết nối', 'connections.html'), 'payOS')
            + dhead('payOS', sign('pass', 'i-check', 'Hoạt động'), 'Nối ngày 12/09/2026 bởi chị An · khoá chưa đổi 25 ngày',
                    '<button class="c-btn" type="button">Thử lại</button><a class="c-btn" href="connections--rotate.html">Đổi khoá</a><a class="c-btn c-btn--danger c-btn--quiet" href="connections--remove.html">Gỡ kết nối</a>')
            + grid(card('jb', 'OPC dùng tài khoản này để', '<ul class="c-list">' + sw(True, 'Tạo link thanh toán', 'anh Khoa bấm tạo, khách trả bằng app ngân hàng')
                                                       + sw(True, 'Nhận báo tiền về', 'khớp với đơn, chờ người duyệt trước khi ghi') + '</ul>')
                   + card('ky', 'Khoá kết nối', '<dl class="c-kv">' + kv('Client ID', '3f9a…7c42') + kv('API Key', '••••••••9f3c') + kv('Checksum Key', '••••••••d71e')
                          + kv('Lưu lúc', '12/09/2026 · chị An') + kv('Dùng lần cuối', 'hôm nay 09:48') + '</dl><p class="c-sub">OPC không hiện lại khoá đầy đủ. Mất khoá thì lấy khoá mới ở payOS.</p>')
                   + card('wk', 'Địa chỉ nhận báo tiền', '<dl class="c-kv">' + kv('Địa chỉ', 'hook.opc.vn/w/an-nhien/payos') + kv('Báo cuối', 'hôm nay 09:48 · chữ ký đúng') + '</dl>'),
                   '<aside class="r-tower__detail" aria-labelledby="rl"><h2 class="r-tower__t" id="rl">Hôm nay</h2><ol class="c-timeline c-timeline--quiet" aria-label="Hôm nay">'
                   + tlx('ok', 'payOS', '09:48', 'Tiền về 320.000 ₫', 'khớp DH-2046') + tlx('ok', 'OPC', '09:41', 'Tạo link thanh toán cho DH-2046', 'anh Khoa bấm') + '</ol></aside>') + '</div>')


save('connections--manage', 'Kết nối · payOS', manage_main())
ROT = dialog('payOS', 'Đổi khoá payOS',
             '<div class="r-keys">' + fld('n1', 'API Key mới', '', 'dán khoá mới từ payOS', True) + fld('n2', 'Checksum Key mới', '', 'nếu payOS cũng đổi khoá này', True)
             + '</div><p class="c-sub">Khoá cũ vẫn chạy cho tới khi khoá mới qua bước thử. Xong nhớ xoá khoá cũ ở payOS.</p>',
             '<button class="c-btn" type="button">Huỷ</button><button class="c-btn c-btn--act" type="button" aria-disabled="true">Thử rồi đổi</button>', 'rt-t')
save('connections--rotate', 'Kết nối · Đổi khoá payOS', manage_main(), overlay=ROT)
RM = dialog('payOS', 'Gỡ payOS?',
            '<ul class="r-gate">' + row('wait', '', '2 link thanh toán chưa trả sẽ hết tác dụng', 'khách bấm vào sẽ không trả được')
            + row('ok', '', 'Đơn và tiền đã về vẫn giữ nguyên', 'chỉ dừng nhận báo tiền mới')
            + row('wait', '', 'OPC xoá khoá khỏi kho ngay', 'chị nên xoá khoá cũ ở payOS nữa') + '</ul>',
            '<button class="c-btn" type="button">Giữ kết nối</button><button class="c-btn c-btn--danger" type="button">Gỡ payOS</button>', 'rm-t')
save('connections--remove', 'Kết nối · Gỡ payOS', manage_main(), overlay=RM)
print('connect4: guides + manage + rotate + remove')


# ------------------------------------------------------------------ 6 · QNSC console: the provider registry (platform side)
import re
from pages import build, ICONS
from providers import GATE
NEED = {'sinvoice', 'gdt-hub', 'bidv', 'cas-cert'}   # need a look from QNSC (the others are parked on purpose)


def pshell(name, cur):
    p = SCREENS / f'{name}.html'
    s = p.read_text()
    a = lambda k: ' aria-current="page"' if cur == k else ''
    nav = (f'<ul class="c-nav__list"><li><a class="c-nav__item" href="platform-providers.html"{a("prov")}>{ic("i-link")}Nhà cung cấp</a></li>'
           f'<li><a class="c-nav__item" href="program.html">{ic("i-people")}Hộ tham gia</a></li>'
           f'<li><a class="c-nav__item" href="#">{ic("i-book")}Nhật ký nền tảng</a></li></ul>'
           f'<ul class="c-nav__list"><li><a class="c-nav__item" href="#">{ic("i-shield")}Khoá truy cập</a></li><li><a class="c-nav__item" href="#">{ic("i-help")}Trợ giúp</a></li></ul>')
    s = re.sub(r'<ul class="c-nav__list">[\s\S]*?(?=\s*</nav>)', lambda m: nav, s, count=1)
    hh = ('<span class="c-hh__mark" aria-hidden="true">QN</span><span class="c-hh__text"><strong class="c-hh__name">QNSC · Nền tảng OPC</strong><span class="c-hh__sub">Quản trị nền tảng</span></span>')
    s = re.sub(r'(<button class="c-hh" type="button" aria-label=")[^"]*(">)[\s\S]*?(</button>)', lambda m: m.group(1) + 'QNSC, quản trị nền tảng OPC' + m.group(2) + hh + m.group(3), s, count=1)
    s = re.sub(r'(<button class="c-hh c-hh--bar r-shell__phone" type="button" aria-label=")[^"]*(">)[\s\S]*?(</button>)', lambda m: m.group(1) + 'QNSC, quản trị nền tảng OPC' + m.group(2) + hh + m.group(3), s, count=1)
    s = s.replace('placeholder="Tìm đơn, món, khách…"', 'placeholder="Tìm nhà cung cấp…"').replace('aria-label="Tìm đơn, món, khách"', 'aria-label="Tìm nhà cung cấp"')
    s = re.sub(r'<a class="c-btn c-btn--quiet r-shell__desk" href="home--assistant.html">[\s\S]*?</a>', '', s, count=1)
    s = re.sub(r'<button class="c-avatar r-shell__desk" type="button" aria-label="[^"]*"><span class="c-avatar__face" aria-hidden="true">.',
               '<button class="c-avatar r-shell__desk" type="button" aria-label="Quang · Quản trị nền tảng"><span class="c-avatar__face" aria-hidden="true">Q', s, count=1)
    tab = ('<nav class="c-tabbar" aria-label="Điều hướng nhanh">'
           f'<a class="c-tabbar__item" href="platform-providers.html"{a("prov")}>{ic("i-link")}Nhà cung cấp</a>'
           f'<a class="c-tabbar__item" href="program.html">{ic("i-people")}Hộ</a>'
           f'<a class="c-tabbar__item" href="#">{ic("i-book")}Nhật ký</a></nav>')
    s = re.sub(r'<nav class="c-tabbar"[\s\S]*?</nav>', lambda m: tab, s, count=1)
    s = s.replace('class="r-shell"', 'class="r-shell r-shell--program"', 1)
    used = sorted(set(re.findall(r'href="#(i-[a-z0-9-]+)"', s)))
    sprite = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">\n' + '\n'.join(f'  <symbol id="{u}" viewBox="0 0 24 24">{ICONS[u]}</symbol>' for u in used if u in ICONS) + '\n</svg>')
    s = re.sub(r'<svg width="0" height="0" style="position:absolute"[^>]*>[\s\S]*?</svg>', lambda m: sprite, s, count=1)
    p.write_text(s)


def psave(name, title, main, cur='prov', overlay=''):
    build(name, title, '\n      ' + main, 'home', overlay=overlay)
    pshell(name, cur)


MODE_TXT = dict(SHORT)
ST_TXT = {'ok': ('Đang dùng', 'pass', 'i-check'), 'can': ('Cho hộ nối', 'pass', 'i-check'), 'sim': ('Mô phỏng', 'pend', 'i-clock'),
          'partner': ('Chờ điều kiện', 'wait', 'i-clock'), 'soon': ('Sắp có', '', '')}
KEYS_OK = {'zalo-oa': 'Có', 'telegram': 'Thiếu'}
SHOW = ['zalo-oa', 'mb', 'payos', 'hilo', 'xinvoice', 'sinvoice', 'gdt-hub', 'bidv', 'etax', 'cas-id', 'ghtk', 'cas-cert', 'casso-tvan', 'ghn', 'shopee', 'momo']


def st_cell(c):
    t, tone, icn = ST_TXT[c['status']]
    gate = GATE.get(c['id'])
    txt = f'{t}' if not gate else f'{t}'
    s = sign(tone, icn, t) if tone else t
    return s + (f'<small>{gate}</small>' if gate else '')


def prow(c, href='platform-provider.html'):
    if c['mode'] == 'oauth':
        key = 'Có' if c['status'] == 'ok' else 'Thiếu'
    else:
        key = 'Qua Casso' if c['mode'] == 'casso' else 'Không cần'
    n = c['hh'] if c['hh'] else '0'
    cls = ' class="c-table__row--you"' if c['id'] in NEED else ''
    return (f'<tr{cls}><td class="c-table__cell--main c-table__who"><b><a class="r-dir__link" href="{href}">{c["name"]}</a></b><small>{GROUP_NAME[c["group"]]}</small></td>'
            f'<td data-l="Cách nối">{MODE_TXT[c["mode"]]}</td><td class="r-reg__st">{st_cell(c)}</td><td class="c-table__num" data-l="Hộ đang nối">{n}</td><td data-l="Khoá nền tảng">{key}</td></tr>')


HUB = ('<tr><td class="c-table__cell--main c-table__who"><b><a class="r-dir__link" href="platform-provider.html">Casso (Cas API)</a></b><small>Đường nối chung · 11 nhà cung cấp đi qua</small></td>'
       '<td data-l="Cách nối">Đường nối chung</td><td class="r-reg__st">' + sign('pass', 'i-check', 'Đang dùng') + '<small>sandbox · chưa chạy thật</small></td><td class="c-table__num" data-l="Hộ đang nối">6</td><td data-l="Khoá nền tảng">Có</td></tr>')
by = {c['id']: c for c in CAT}
ROWS = HUB + ''.join(prow(by[i]) for i in SHOW)
PFILTER = chips('Lọc', [f'Tất cả {n_all + 1}', 'Đang dùng 6', 'Cần xem 4', 'Đã ẩn 0', 'Sắp có 58'])
PTABLE = ('<div class="c-table__scroll" tabindex="0" role="region" aria-label="Nhà cung cấp"><table class="c-table c-table--stack r-reg"><thead><tr><th scope="col">Nhà cung cấp</th><th scope="col">Cách nối</th>'
          '<th scope="col">Trạng thái</th><th scope="col" class="c-table__num">Hộ đang nối</th><th scope="col">Khoá nền tảng</th></tr></thead>'
          f'<tbody>{ROWS}</tbody></table></div><p class="c-sub">Hiện 17 trên {n_all + 1} · <a href="platform-providers.html">Xem tiếp</a></p>')
psave('platform-providers', 'Nền tảng · Nhà cung cấp',
      head('Nhà cung cấp', f'{n_all + 1} nhà cung cấp · 6 đang có hộ dùng · 4 cần xem', '<a class="c-btn c-btn--act" href="platform-provider--new.html">Thêm nhà cung cấp</a>')
      + '<div class="page"><p class="r-trust r-trust--gate">' + ic('i-shield') + '<span><b>Chỉ thấy số hộ</b> · không thấy hộ nào, đơn nào, tiền nào</span></p>'
      + PFILTER + PTABLE + '</div>')
print('connect4: platform registry')


# ------------------------------------------------------------------ 7 · one provider on the platform side (Casso) + remove + new
def pcrumb(t):
    return crumb(('Nhà cung cấp', 'platform-providers.html'), t)


ROUTES = [('MB qua Casso', 'Đang dùng', 6), ('Hilo', 'Đang dùng', 4), ('X Invoice', 'Đang dùng', 3), ('Viettel S-Invoice', 'Cho hộ nối', 0), ('Casso GDT Hub', 'Cho hộ nối', 0),
          ('BIDV qua Casso', 'Chờ điều kiện', 0)]
CASSO_MAIN = ('<div class="page">' + pcrumb('Casso (Cas API)')
              + dhead('Casso (Cas API)', sign('pass', 'i-check', 'Đang dùng'), 'Đường nối chung · 11 nhà cung cấp đi qua · môi trường sandbox',
                      '<a class="c-btn" href="platform-provider--remove.html">Ẩn hoặc gỡ</a>')
              + grid(card('pk', 'Khoá của QNSC', '<dl class="c-kv">' + kv('Môi trường', 'Sandbox · chưa chạy thật') + kv('API Key', '••••••••b7e2') + kv('Secret', '••••••••41cd')
                          + kv('Lưu lúc', '23/09/2026 · Quang') + '</dl><p class="c-sub">Khoá nằm trên máy chủ OPC, không nằm trong app. Mỗi lần đổi khoá có mã xác nhận của Quang.</p>'
                          '<div class="c-decide__acts"><button class="c-btn" type="button">Thử kết nối</button><button class="c-btn" type="button">Đổi khoá</button></div>')
                     + card('pw', 'Nơi Casso gọi về OPC', '<dl class="c-kv">' + kv('Địa chỉ', 'hook.opc.vn/casso') + kv('Mã bí mật', '••••••••a41c') + kv('Báo cuối', 'hôm nay 09:48')
                            + kv('Chữ ký', 'Casso không ký báo tiền · OPC tự xác minh lại trước khi ghi') + '</dl>')
                     + card('pr', 'Nhà cung cấp đi qua Casso', '<ul class="r-gate">' + ''.join(row('ok' if t == 'Đang dùng' else 'wait', t, n, f'{h} hộ đang nối' if h else '') for n, t, h in ROUTES)
                            + '</ul><p class="c-sub">Và 5 nơi nữa · <a href="platform-providers.html">Xem tất cả</a></p>'),
                     side('Nếu gỡ Casso', [('6 hộ về cách làm tay', 'thu tiền, hoá đơn, định danh'), ('11 nhà cung cấp ngừng cùng lúc', 'chúng chỉ đi qua Casso'),
                                           ('Hợp đồng vẫn còn', 'phí tối thiểu 500 USD mỗi tháng · gỡ ở OPC không huỷ hợp đồng')], 'wait')) + '</div>')
psave('platform-provider', 'Nền tảng · Casso', CASSO_MAIN)


def popt(on, t, m):
    return (f'<button class="c-option c-option--big" type="button" role="radio" aria-checked="{"true" if on else "false"}"><span class="c-option__radio" aria-hidden="true"></span>'
            f'<span class="c-option__body"><strong class="c-option__title">{t}</strong><span class="c-option__meta">{m}</span></span></button>')


RMBODY = ('<div class="c-options" role="radiogroup" aria-label="Cách gỡ">' + popt(True, 'Ẩn khỏi danh mục', 'hộ đang nối vẫn chạy · hộ mới không thấy')
          + popt(False, 'Gỡ hẳn', 'ngắt 6 hộ, xoá khoá · không hoàn tác').replace('c-option c-option--big','c-option c-option--big r-opt--danger') + '</div>'
          '<ul class="r-gate">' + row('wait', '', '6 hộ quay về cách làm tay', 'nếu gỡ hẳn') + row('wait', '', '11 nhà cung cấp đi qua Casso cùng ngừng', 'nếu gỡ hẳn')
          + row('ok', '', 'Đơn, sổ và hoá đơn đã có giữ nguyên', 'cả hai cách') + '</ul>'
          '<div class="c-field"><label class="c-field__label" for="rs">Lý do · ghi vào nhật ký</label><div class="c-field__control"><input class="c-field__input" id="rs" placeholder="Ví dụ: chưa ký hợp đồng"></div>'
          '<span class="c-field__hint">Bắt buộc. Nút chỉ bật khi đã có lý do.</span></div>')
RMDLG = dialog('Casso (Cas API)', 'Ẩn hay gỡ Casso?', RMBODY,
               '<button class="c-btn" type="button">Huỷ</button><button class="c-btn c-btn--danger" type="button" aria-disabled="true">Ẩn Casso</button>', 'pr-t')
psave('platform-provider--remove', 'Nền tảng · Ẩn hoặc gỡ Casso', CASSO_MAIN, overlay=RMDLG)

# add a provider to the catalog
KIND = ''.join(popt(k == 'key', MODES[k][0], MODES[k][1]) for k in ('casso', 'oauth', 'key', 'link', 'assist'))
NEWMAIN = ('<div class="page">' + pcrumb('Thêm nhà cung cấp')
           + dhead('Thêm nhà cung cấp', '', 'Hộ chỉ thấy khi chị bật trạng thái. Thêm một dòng là đủ.',
                   '')
           + grid(card('n1', 'Thông tin', '<div class="r-keys">' + fld('nn', 'Tên', 'Viettel Post', 'hộ sẽ thấy đúng tên này') + fld('ng', 'Nhóm việc', 'Giao hàng', 'nhóm hộ sẽ thấy trong Thêm kết nối', act='Đổi')
                         + '</div>')
                  + card('n2', 'Hộ nối bằng cách nào', '<div class="c-options" role="radiogroup" aria-label="Cách nối">' + KIND + '</div>')
                  + card('n3', 'Hộ phải nhập gì', '<div class="r-keys">' + fld('f1', 'Ô 1', 'Token', 'tên ô hộ nhìn thấy') + fld('f2', 'Ô 2', 'Mã cửa hàng', 'không bí mật, hiện lại được')
                         + '</div><p class="c-sub">Ô bí mật được che và chỉ hiện 4 số cuối sau khi lưu.</p><div class="r-save"><button class="c-btn" type="button">Thêm ô</button></div>')
                  + card('n4', 'Trạng thái và hướng dẫn', '<div class="c-options" role="radiogroup" aria-label="Trạng thái">' + popt(True, 'Sắp có', 'hộ chỉ thấy nút Báo tôi') + popt(False, 'Mô phỏng', 'chỉ dùng khi demo')
                         + popt(False, 'Cho hộ nối', 'hộ nối được thật') + '</div><a class="c-link" href="connections--guide.html">Soạn hướng dẫn</a>') + '<div class="r-save r-save--bar"><button class="c-btn c-btn--act" type="button">Lưu nhà cung cấp</button><a class="c-btn" href="platform-providers.html">Huỷ</a></div>',
                  '<aside class="r-tower__detail" aria-labelledby="pv"><h2 class="r-tower__t" id="pv">Hộ sẽ thấy</h2><ul class="r-dir__list r-dir__list--one"><li class="r-dir__p r-dir__p--soon">'
                  '<span class="r-acct__logo" aria-hidden="true">V</span><span class="r-dir__nb"><b class="r-dir__n">Viettel Post</b><small>Dán khoá</small></span><span class="r-dir__st"><button class="c-btn c-btn--quiet" type="button">Báo tôi</button></span></li></ul></aside>')
           + '</div>')
psave('platform-provider--new', 'Nền tảng · Thêm nhà cung cấp', NEWMAIN)
print('connect4: platform provider + remove + new')


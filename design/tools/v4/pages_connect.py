"""v4.5.10 · Connector flow (Kết nối is now a top-level item). The list (connections.html) was a table with dead buttons.
Five screens (connections--detail now comes from pages_connect2.py), An Nhiên data, demo "today" 06/10/2026 10:45:
  connections--provider  choose the provider for a category (Hoá đơn mua vào, cổng thuế)
  connections--consent   consent + scope + duration + OTP of the owner (only chị An)
  connections--testing   first read: connect → read one invoice → match with the ledger
  connections--unknown   "Chưa rõ kết quả": OPC never auto-resends; owner picks
  connections--log       what happened on every connection today
Usage: python3 pages_connect.py (after pages_setup.py, before quiet_icons.py / inert.py)"""
import pathlib
from pages import build, ic, sign, CUR, SCREENS
from pages import annhien

CRUMB = lambda t: ('<nav class="c-crumbs" aria-label="Đường dẫn"><a href="connections.html">Kết nối</a>'
                   f'<span aria-current="page">{t}</span></nav>')


def head(title, state, sub, acts):
    return ('<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">' + title + ' ' + state + '</h1>'
            f'<p class="r-detail__fig"><span class="c-sub">{sub}</span></p></div><div class="r-detail__acts">{acts}</div></div>')


def row(tone, st, t, m, act='', href='#'):
    a = f'<a class="c-btn" href="{href}">{act}</a>' if act else ''
    return (f'<li class="r-gate__i r-gate__i--{tone}"><span class="r-gate__b"><b>{t}</b><small><span class="r-gate__st">{st}</span> · {m}</small></span>'
            f'<span class="r-gate__amt"></span><span class="r-gate__act">{a}</span></li>')


def card(tid, title, inner):
    return (f'<section class="c-card" aria-labelledby="{tid}"><div class="c-card__head"><h2 class="c-card__title" id="{tid}">{title}</h2></div>{inner}</section>')


def step(kind, src, time, what, detail=''):
    d = f'<span class="c-timeline__who">{detail}</span>' if detail else ''
    return (f'<li class="c-timeline__item c-timeline__item--{kind}"><span class="c-timeline__time">{time}</span><span class="c-timeline__dot" aria-hidden="true"></span>'
            f'<span class="c-timeline__body"><span class="c-timeline__src">{src}</span><span class="c-timeline__what">{what}</span>{d}</span></li>')


def rail(title, items):
    return (f'<aside class="r-tower__detail" aria-labelledby="rl"><h2 class="r-tower__t" id="rl">{title}</h2>'
            f'<ol class="c-timeline c-timeline--quiet" aria-label="{title}">{items}</ol></aside>')


def grid(left, right):
    return f'<div class="r-detail__grid r-detail--calm"><div class="stack">{left}</div>{right}</div>'


def page(name, title, crumb, main, owner=True):
    build(name, title, '\n      <div class="page">' + CRUMB(crumb) + main + '</div>', 'connections')
    p = SCREENS / f'{name}.html'
    annhien(p)
    s = p.read_text()
    if owner:
        s = s.replace('Nguyễn Minh Khoa · Người vận hành', 'Phạm Thị An · Chủ hộ').replace('<span class="c-avatar__face" aria-hidden="true">K', '<span class="c-avatar__face" aria-hidden="true">A')
    p.write_text(s)


# ---------------------------------------------------------------- 2 · provider
OPT = lambda on, t, m, tag='': (f'<button class="c-option c-option--big" type="button" role="radio" aria-checked="{"true" if on else "false"}"><span class="c-option__radio" aria-hidden="true"></span>'
                                f'<span class="c-option__body"><strong class="c-option__title">{t}</strong><span class="c-option__meta">{m}</span></span>{tag}</button>')
def _wr(t, m):
    return (f'<li class="r-gate__i r-gate__i--ok"><span class="r-gate__b"><b>{t}</b><small>{m}</small></span><span class="r-gate__amt"></span><span class="r-gate__act"></span></li>')


page('connections--provider', 'Kết nối · Chọn nhà cung cấp', 'Hoá đơn mua vào, cổng thuế',
     head('Hoá đơn mua vào', sign('unk', 'i-clock', 'Chưa kết nối'), 'Chọn cách đưa hoá đơn mua vào về sổ', '')
     + grid('<section class="c-card r-conn__choose" aria-labelledby="cp"><div class="c-card__head"><h2 class="c-card__title" id="cp">Nhà cung cấp</h2></div><div class="c-options" role="radiogroup" aria-label="Nhà cung cấp">'
            + OPT(True, 'Casso GDT Hub', 'tự lấy hoá đơn từ cổng thuế · chị An đồng ý')
            + OPT(False, 'Tải bảng kê tay', 'chị Lan tải mỗi kỳ · không cần kết nối')
            + OPT(False, 'Nhà cung cấp khác', 'chưa hỗ trợ trong bản này').replace('aria-checked="false"', 'aria-checked="false" aria-disabled="true"') + '</div>'
            '<div class="c-decide__acts r-use__acts r-use__acts--stack"><a class="c-btn c-btn--act" href="connections--consent.html">Tiếp tục</a><a class="c-btn c-btn--quiet" href="connections.html">Dùng cách làm tay</a></div></section>',
            '<aside class="r-tower__detail" aria-labelledby="rl"><h2 class="r-tower__t" id="rl">Khi xong</h2><ul class="r-gate">'
            + _wr('Hoá đơn mua vào tự về sổ', 'chị Lan chỉ còn đối chiếu')
            + _wr('Chỉ đọc', 'không gửi, không nộp, không sửa hoá đơn')
            + _wr('Vẫn làm tay được', 'tắt bất cứ lúc nào ở Kết nối') + '</ul></aside>'))

# ---------------------------------------------------------------- 3 · consent (owner only)
OTP = ''.join(f'<input class="c-otp__box" type="text" inputmode="numeric" maxlength="1" aria-label="Số {i}"{" autofocus" if i == 1 else ""}>' for i in range(1, 7))
page('connections--consent', 'Kết nối · Đồng ý', 'Đồng ý cho Casso GDT Hub',
     head('Đồng ý đọc hoá đơn mua vào', sign('pend', 'i-lock', 'Chỉ chị An'), 'MST 5901234567 · hoá đơn mua vào',
          '<button class="c-btn c-btn--act" type="button" aria-disabled="true">Đồng ý & kết nối</button>')
     + grid(
         card('dr', 'OPC sẽ', '<dl class="c-kv"><dt>Đọc</dt><dd>hoá đơn mua vào của hộ từ 01/07/2026</dd><dt>Thời hạn</dt><dd>180 ngày, đến 04/04/2027 · gia hạn khi chị đồng ý lại</dd>'
              '<dt>Không bao giờ</dt><dd>gửi tờ khai, nộp thuế hay sửa hoá đơn</dd></dl>')
         + card('ot', 'Xác nhận bằng mã', '<div class="c-field"><label class="c-field__label" for="otp1">Mã 6 số gửi qua Zalo tới 0935 112 418</label>'
                f'<div class="c-otp" role="group" aria-label="Mã xác nhận 6 số">{OTP.replace(" autofocus", "")}</div>'
                '<span class="c-field__hint">Mã hết hạn sau 5 phút · nhập đủ 6 số để bật nút Đồng ý</span></div>'),
         rail('Vì sao cần chị', step('you', 'Quy định', '', 'Quyền đọc dữ liệu thuế chỉ chủ hộ cấp', 'anh Khoa và chị Lan không đồng ý thay được')
              + step('ok', 'Thu hồi', '', 'Chị tắt bất cứ lúc nào ở Kết nối', 'dữ liệu đã về sổ vẫn giữ'))))

# ---------------------------------------------------------------- 4 · testing
page('connections--testing', 'Kết nối · Kiểm tra', 'Kiểm tra kết nối',
     head('Đang kiểm tra', sign('wait', 'i-clock', 'Chờ phản hồi'), 'Casso GDT Hub · đọc thử 1 hoá đơn, chưa ghi gì vào sổ',
          '<button class="c-btn" type="button">Dừng kiểm tra</button>')
     + grid(card('st', 'Ba bước', '<ul class="r-gate">'
                 + row('ok', 'Xong 10:48', 'Kết nối tới Casso GDT Hub', 'chị An đã đồng ý')
                 + row('wait', 'Đang chạy', 'Đọc thử 1 hoá đơn mua vào', 'Điện lực Gia Lai · 1.180.000 ₫')
                 + row('wait', 'Chờ', 'Đối chiếu với sổ', 'chỉ so, không ghi') + '</ul>'
                 '<div class="c-meter"><div class="c-meter__bar" role="img" aria-label="Bước 2 trên 3"><span class="c-meter__fill" style="width:50%"></span></div></div>'
                 '<p class="c-waitbar" role="status"><span class="c-waitbar__spin" aria-hidden="true"></span><span><b>Đang chờ phản hồi</b>OPC không tự gửi lại nếu không rõ kết quả</span></p>'),
            rail('Nếu lỗi', step('next', 'Không trả lời', '', 'OPC báo "Chưa rõ kết quả"', 'không tự thử lại')
                 + step('ok', 'Luôn có', '', 'đường làm tay', 'kế toán tải bảng kê'))))

# ---------------------------------------------------------------- 5 · unknown result
page('connections--unknown', 'Kết nối · Chưa rõ kết quả', 'Chưa rõ kết quả',
     head('Casso GDT Hub', sign('unk', 'i-clock', 'Chưa rõ kết quả'), 'Không trả lời lúc 10:52 · OPC chưa biết hoá đơn đã đọc được chưa',
          '<button class="c-btn c-btn--act" type="button">Hỏi lại trạng thái</button><a class="c-btn" href="connections--log.html">Xem nhật ký</a>')
     + grid(card('ch', 'Chị chọn', '<ul class="r-gate">'
                 + row('you', 'Hỏi lại', 'Hỏi trạng thái (chỉ đọc)', 'không tạo thêm việc, không ghi sổ')
                 + row('wait', 'Làm tay', 'Chị Lan tải bảng kê Quý III', 'như cách đang dùng', 'Nhắn chị Lan')
                 + row('wait', 'Để sau', 'Giữ kết nối, thử lại ngày mai', 'chị bấm, OPC không tự thử') + '</ul>'),
            rail('Vì sao OPC không tự gửi lại', step('ok', 'Nguyên tắc', '', 'Chưa rõ kết quả có thể đã thành công', 'gửi lại dễ tạo trùng')
                 + step('next', 'Chị quyết', '', 'hỏi lại chỉ đọc trạng thái', ''))))

# ---------------------------------------------------------------- 6 · log
LOG = [('10:52', 'Casso GDT Hub', 'Đọc thử hoá đơn Điện lực', sign('unk', 'i-clock', 'Chưa rõ kết quả'), 'OPC'),
       ('10:48', 'Casso GDT Hub', 'Chị An đồng ý 180 ngày', sign('pass', 'i-check', 'Xong'), 'chị An'),
       ('10:44', 'Hilo', 'Hoá đơn quầy 00001291', sign('pass', 'i-check', 'Có mã'), 'Hạnh'),
       ('10:27', 'X Invoice', 'Hỏi lại trạng thái DH-2047', sign('unk', 'i-clock', 'Chưa có phản hồi'), 'OPC'),
       ('10:12', 'X Invoice', 'Gửi hoá đơn DH-2047', sign('unk', 'i-clock', 'Chưa rõ kết quả'), 'anh Khoa'),
       ('10:43', 'MB qua Casso', 'Cập nhật sao kê', sign('pass', 'i-check', 'Xong'), 'OPC'),
       ('09:20', 'MB qua Casso', 'Tiền về 585.000 ₫', sign('pass', 'i-check', 'Đã ghi'), 'OPC'),
       ('08:00', 'Zalo OA', 'Nhắc Sunrise lần 2', sign('pass', 'i-check', 'Đã gửi'), 'Trợ lý')]
rows = ''.join(f'<tr{" class=\"c-table__row--you\"" if "Chưa" in r else ""}><td class="c-table__cell--main c-table__who"><b>{t}</b><small>{k}</small></td><td>{e}</td><td>{r}</td><td class="c-table__cell--opt">{w}</td></tr>' for t, k, e, r, w in sorted(LOG, key=lambda x: x[0], reverse=True))
page('connections--log', 'Kết nối · Nhật ký', 'Nhật ký',
     head('Nhật ký kết nối', '', 'Hôm nay 06/10 · 8 sự kiện · mọi lần gửi đều ghi tên người hoặc OPC', '<a class="c-btn" href="connections.html">Về danh sách</a>')
     + '<div class="c-table__scroll" tabindex="0" role="region" aria-label="Nhật ký kết nối"><table class="c-table c-table--stack"><thead><tr><th scope="col">Giờ · kết nối</th><th scope="col">Sự kiện</th><th scope="col">Kết quả</th><th scope="col" class="c-table__cell--opt">Ai</th></tr></thead>'
       f'<tbody>{rows}</tbody></table></div>')
print('connect: 6 screens')

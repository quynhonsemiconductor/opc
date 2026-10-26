"""v7.7.0 · offline states for v7 record screens (BA: offline = draft only, marked "chưa đồng bộ"; anything that moves stock, money or
an invoice waits for the network so it never happens twice). Built from the finished screens, so it runs last.
Writes quick-sale--offline, purchase-detail--receive--offline.  Usage: python3 offline7.py"""
from pages import SCREENS, ic
from onboard_lib import sprite

CHIP_ON = '<span class="c-health r-shell__desk"'
CHIP_OFF = ('<span class="c-health c-health--off r-shell__desk" role="status" tabindex="0" data-tip="Không có mạng từ 10:51 · lưu trên máy 10:58 · {n} việc chờ gửi">'
            'Mất mạng · <b>{n} việc chờ</b></span>')


def banner(t, m):
    return ('<div class="c-banner r-offbar" role="status"><span class="c-banner__pic">' + ic('i-offline') + '</span><span class="c-banner__text">'
            f'<strong class="c-banner__title">{t}</strong><span>{m}</span></span><a class="c-btn" href="delivery--pick--queue.html">Xem việc chờ</a></div>')


def make(src, dst, title, edits, ban, n):
    s = (SCREENS / src).read_text()
    i = s.find(CHIP_ON)
    if i >= 0:
        j = s.find('</span>', s.find('>', i)) + 7
        s = s[:i] + CHIP_OFF.format(n=n) + s[j:]
    for a, b in edits:
        assert a in s, (dst, a[:60])
        s = s.replace(a, b, 1)
    s = s.replace('<div class="page">', '<div class="page">' + ban, 1)
    s = s.replace('<title>', f'<title>{title} · ', 1)
    (SCREENS / dst).write_text(sprite(s))


make('quick-sale.html', 'quick-sale--offline.html', 'Mất mạng', [
    ('<button class="c-seg__opt" type="button" role="radio" aria-checked="true">Chuyển khoản QR</button>',
     '<button class="c-seg__opt" type="button" role="radio" aria-checked="false" aria-disabled="true">QR · cần mạng</button>'),
    ('<button class="c-seg__opt" type="button" role="radio" aria-checked="false">Tiền mặt</button>',
     '<button class="c-seg__opt" type="button" role="radio" aria-checked="true">Tiền mặt</button>'),
    ('Thu = đơn DH-2053 giao ngay tại chỗ · kho trừ một lần (bò khả dụng 26 → 24) · tiền ghi khi khớp',
     'Lưu = đơn nháp trên máy, <b>chưa đồng bộ</b> · có mạng lại thì OPC kiểm tồn rồi mới trừ kho, không trừ hai lần'),
    ('<label class="r-chkrow"><span class="c-check"><input type="checkbox"></span><span>Khách cần hoá đơn', '<label class="r-chkrow"><span class="c-check"><input type="checkbox" disabled></span><span>Khách cần hoá đơn · lập khi có mạng'),
    ('<a class="c-btn c-btn--act" href="quick-sale--qr.html">Thu 715.000 ₫</a>', '<a class="c-btn c-btn--act" href="quick-sale.html">Thu 715.000 ₫ tiền mặt · lưu trên máy</a>'),
], banner('Không có mạng từ 10:51 — vẫn bán tiền mặt được', 'Đơn lưu trên máy, ghi "chưa đồng bộ". QR, hoá đơn có mã cần mạng.'), 2)

make('purchase-detail--receive.html', 'purchase-detail--receive--offline.html', 'Mất mạng', [
    ('<a class="c-btn c-btn--act" href="purchase-detail--received.html">Xác nhận nhận 45 hũ</a>',
     '<a class="c-btn c-btn--act" href="purchase-detail--receive.html">Lưu số đếm trên máy</a>'
     '<button class="c-btn" type="button" aria-disabled="true">' + ic('i-lock') + 'Nhập kho · cần mạng</button>'),
    ('<button class="c-btn" type="button">Đếm lại</button>', ''),
], banner('Không có mạng từ 10:51 — vẫn đếm được', 'Số đếm 45/50 hũ lưu trên máy, chưa đồng bộ. Nhập kho cần mạng để kho chỉ tăng một lần.'), 1)
print('offline7: 2 screens')

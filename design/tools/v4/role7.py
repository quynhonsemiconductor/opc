"""v7.7.0 · role views of v7 screens (BA roles: owner decides; optional sales staff; accountant = view + export only).
Built from finished screens, then nav7 re-renders the rail for the role (nav7.ROLE). Runs after offline7, then nav7 again.
Writes tax--accountant (chị Lan: sees the quarter, downloads, marks "đã xem"; cannot lock the period or file) and
quick-sale--staff (Hạnh: sells cash/QR; "Ghi nợ" needs chị An; no cost prices, no day totals).  Usage: python3 role7.py"""
import re
from pages import SCREENS, ic
from onboard_lib import sprite

WHO = {'accountant': ('Chị Lan · Kế toán (uỷ quyền)', 'L'), 'staff': ('Hạnh · Bán hàng', 'H')}
LOCK = ic('i-lock')


def make(src, dst, role, edits, note):
    s = (SCREENS / src).read_text()
    name, face = WHO[role]
    s = re.sub(r'aria-label="[^"]*— tài khoản"><span class="c-avatar__face" aria-hidden="true">.', f'aria-label="{name} — tài khoản"><span class="c-avatar__face" aria-hidden="true">{face}', s, count=1)
    for a, b in edits:
        assert a in s, (dst, a[:70])
        s = s.replace(a, b, 1)
    s = s.replace('<div class="page">', '<div class="page">' + note, 1)
    (SCREENS / dst).write_text(sprite(s))


def note(t, m):
    return (f'<div class="c-banner" role="note"><span class="c-banner__pic">{ic("i-shield")}</span><span class="c-banner__text">'
            f'<strong class="c-banner__title">{t}</strong><span>{m}</span></span></div>')


make('tax.html', 'tax--accountant.html', 'accountant', [
    ('<a class="c-btn c-btn--act" href="period.html">Đối soát và khoá kỳ</a>', '<button class="c-btn c-btn--act" type="button">Đánh dấu đã xem số quý III</button>'),
    ('<a class="c-btn" href="tax--return.html">Xem hướng dẫn khai</a>', '<a class="c-btn" href="tax-evidence.html">' + ic('i-download') + 'Tải bộ chứng từ</a>'
     '<button class="c-btn" type="button" aria-disabled="true">' + LOCK + 'Khoá kỳ · chỉ chị An</button>'),
], note('Chị Lan xem với quyền kế toán', 'Xem và tải mọi số, ghi chú cho chị An. Khoá kỳ, nộp trên eTax và mọi thay đổi số liệu chỉ chị An làm.'))

make('quick-sale.html', 'quick-sale--staff.html', 'staff', [
    ('<button class="c-seg__opt" type="button" role="radio" aria-checked="false">Ghi nợ</button>',
     '<button class="c-seg__opt" type="button" role="radio" aria-checked="false" aria-disabled="true">' + LOCK + 'Ghi nợ · chị An duyệt</button>'),
], note('Hạnh bán với quyền nhân viên', 'Bán tiền mặt và QR, in phiếu. Ghi nợ, sửa giá, huỷ đơn cần chị An duyệt.'))
s = (SCREENS / 'quick-sale--staff.html').read_text()   # staff does not see the day totals
s = re.sub(r'<aside class="r-tower__detail" aria-labelledby="qh">.*?</aside>',
           '<aside class="r-tower__detail" aria-labelledby="qh"><h2 class="r-tower__t" id="qh">Ca của Hạnh</h2><p class="c-sub">2 đơn từ 07:00 · tổng tiền trong ngày chỉ chị An xem.</p></aside>', s, count=1, flags=re.S)
(SCREENS / 'quick-sale--staff.html').write_text(s)
print('role7: 2 screens')

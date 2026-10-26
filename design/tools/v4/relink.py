"""v7.3.0 · Quầy + Đóng ca are gone (BA: "Bán nhanh"; cash is counted in Thu chi và đối chiếu). Runs after every generator, before nav7:
repoints links on all screens and renames the visible labels that went with them.  Usage: python3 relink.py"""
import re
from pages import SCREENS

HREF = [(r'counter--qr\.html', 'quick-sale--qr.html'), (r'counter--payment--(verified|received)\.html', 'quick-sale--done.html'),
        (r'counter(--[a-z-]+)?\.html', 'quick-sale.html'), (r'shift-close(--[a-z-]+)?\.html', 'money.html')]
TEXT = [('>Mở quầy<', '>Bán nhanh<'), ('Mở quầy', 'Bán nhanh'), ('>Đóng ca<', '>Đối chiếu tiền<'), (' · Quầy · ', ' · Bán nhanh · '),
        ('Bán tại quầy', 'Bán nhanh'), ('tại quầy', 'tại chỗ'),
        ('Quầy và Đóng ca · ca sáng', 'Bán nhanh và đối chiếu tiền'), ('Ca sáng từ 07:00 · Hạnh ở quầy', 'Hạnh bán hàng từ 07:00'),
        ('Quầy, Zalo OA', 'Bán nhanh, Zalo OA'), ('quầy dùng hoá đơn máy tính tiền', 'bán lẻ dùng hoá đơn máy tính tiền'),
        ('Hoá đơn quầy', 'Hoá đơn bán lẻ'), ('hoá đơn quầy', 'hoá đơn bán lẻ'), ('HĐ quầy', 'HĐ bán lẻ'),
        ('Máy quầy', 'Máy bán hàng'), ('máy quầy', 'máy bán hàng'), ('Hạnh · thu ngân', 'Hạnh · bán hàng'), ('>Thu ngân<', '>Bán hàng<'),
        ('Thu ngân', 'Nhân viên bán hàng'), ('ca sáng · Hạnh', 'sáng nay · Hạnh'),
        ('ở quầy', 'tại chỗ'), ('Tiền › Đóng ca', 'Tiền › Thu chi và đối chiếu'), ('quầy, đóng ca,', 'bán nhanh, đối chiếu tiền,'), ('Quầy OPC', 'Bán nhanh OPC'),
        ('quầy · 30/09', 'bán lẻ · 30/09'), ('quầy, Homestay', 'bán lẻ, Homestay'), ('>Quầy<', '>Bán nhanh<'),
        ('quầy và khách chưa gán', 'bán nhanh và khách chưa gán'), ('Đóng ca và nộp tiền thu hộ', 'Nộp tiền thu hộ'), ('đổi giá, đóng ca…', 'đổi giá, đối chiếu tiền…'), ('màn hình quầy', 'màn hình bán nhanh')]

n = 0
for f in sorted(SCREENS.glob('*.html')):
    if f.name.startswith(('_', 'counter', 'shift-close')):
        continue
    s = o = f.read_text()
    for a, b in HREF:
        s = re.sub(r'href="' + a, 'href="' + b, s)
    for a, b in TEXT:
        s = s.replace(a, b)
    if s != o:
        f.write_text(s); n += 1
print(f'relink: {n} screens')

# v7.5.1 · no provider names on household screens (CEO: "bỏ hẳn"). Providers stay named only where the owner picks or manages them:
# Kết nối (connections*), registration (onboard*), QNSC console (platform*, program*), demo pages.
BRAND = [('Mở cổng X Invoice', 'Mở cổng hoá đơn điện tử'), ('cổng nhà cung cấp (Hilo, X Invoice)', 'cổng bên hoá đơn'), ('cổng X Invoice', 'cổng hoá đơn điện tử'),
         ('Hilo máy tính tiền (2C26MAN)', 'hoá đơn máy tính tiền (2C26MAN)'), ('X Invoice có mã (2C26TAN)', 'hoá đơn có mã (2C26TAN)'),
         ('Kết nối hoá đơn Hilo', 'Kết nối hoá đơn máy tính tiền'), ('MB, Hilo, Zalo OA', 'MB, hoá đơn, Zalo OA'),
         ('kết nối X Invoice', 'kết nối hoá đơn điện tử'), ('Kết nối X Invoice', 'Kết nối hoá đơn điện tử'), ('MB qua Casso', 'ngân hàng MB'),
         ('X Invoice im lặng', 'bên hoá đơn im lặng'), ('X Invoice không trả lời', 'bên hoá đơn không trả lời'), ('lập trên X Invoice', 'lập trên cổng hoá đơn'),
         ('→ X Invoice', '→ bên hoá đơn'), (' · X Invoice', ' · hoá đơn điện tử'), ('X Invoice', 'bên hoá đơn điện tử'), ('Hilo', 'bên hoá đơn máy tính tiền'),
         ('Casso', 'dịch vụ đọc sao kê'),
         ('GHTK thu hộ', 'Đơn vị giao hàng thu hộ'), ('Đơn vị vận chuyển · GHTK', 'Đơn vị vận chuyển'), ('giao GHTK', 'giao qua đơn vị vận chuyển'),
         ('GHTK: ', 'Đơn vị vận chuyển: '), ('chờ GHTK trả', 'chờ đơn vị giao trả'), ('nên nhắc GHTK', 'nên nhắc đơn vị giao'), ('cho GHTK', 'cho đơn vị giao hàng'),
         ('ở GHTK', 'ở đơn vị giao hàng'), ('GHTK', 'Đơn vị giao hàng'),
         # tidy after the generic swaps
         ('MB (qua dịch vụ đọc sao kê) cập nhật', 'Ngân hàng MB cập nhật'), ('bên hoá đơn máy tính tiền hoạt động · bên hoá đơn không trả lời', 'hoá đơn máy tính tiền hoạt động · hoá đơn điện tử không trả lời'),
         ('>bên hoá đơn', '>Bên hoá đơn'), ('>đơn vị giao', '>Đơn vị giao')]
k = 0
for f in sorted(SCREENS.glob('*.html')):
    if f.name.startswith(('_', 'connections', 'onboard', 'platform', 'program', 'demo')):
        continue
    s = o = f.read_text()
    for a, b in BRAND:
        s = s.replace(a, b)
    if s != o:
        f.write_text(s); k += 1
print(f'debrand: {k} screens')

"""v5.1.1 · OPC voice. Household screens outside Kết nối lead with OPC's own words; third-party brands are named only where the owner manages
or chooses them (Kết nối, chooser, consent) or where the law needs it. Rewrites text in the shared chrome (health tooltip) and a few onboarding lines.
Runs before quiet_icons.py / inert.py.  Usage: python3 brand.py"""
import re, pathlib
SCREENS = pathlib.Path(__file__).resolve().parents[2] / 'apps' / 'app' / 'screens'
KEEP = ('connections', 'platform-')          # the places where a provider is the subject
R = [
    ('MB (qua Casso) cập nhật 2 phút trước · Hilo hoạt động · X Invoice không trả lời 10:12 · Cổng thuế chưa bật',
     'Ngân hàng cập nhật 2 phút trước · Hoá đơn quầy hoạt động · Hoá đơn khách sỉ không trả lời 10:12 · Cổng thuế chưa bật'),
    ('MB (qua Casso) cập nhật 2 phút trước · Hoá đơn Hilo hoạt động', 'Ngân hàng cập nhật 2 phút trước · Hoá đơn hoạt động'),
    ('MB (qua Casso) cập nhật 2 phút trước · Hilo hoạt động', 'Ngân hàng cập nhật 2 phút trước · Hoá đơn hoạt động'),
    ('Kết nối chính thức: Ngân hàng MB · Casso · Cổng thuế', 'OPC kết nối chính thức với ngân hàng và cổng thuế'),
    ('Đã xác minh · khớp sao kê MB', 'Đã xác minh · khớp sao kê ngân hàng'),
    ('Nhận tiền · MB qua Casso', 'Nhận tiền · tài khoản MB'),
    ('Kết nối qua Casso — đơn vị OPC dùng để nối với ngân hàng', 'OPC nối với ngân hàng giúp chị · chị không phải cài thêm gì'),
    ('aria-label="OPC đọc tiền vào qua Casso từ MB, chỉ đọc"', 'aria-label="OPC đọc tiền vào từ MB, chỉ đọc"'),
]
n = 0
for p in sorted(SCREENS.glob('*.html')):
    s = o = p.read_text()
    for a, b in (R[:3] if p.stem.startswith(KEEP) else R):   # the health tooltip is shared chrome: OPC voice everywhere
        s = s.replace(a, b)
    s = re.sub(r'<b><svg[^>]*>.*?</svg>Casso</b><svg[^>]*>.*?</svg>', '', s, flags=re.S) if p.stem.startswith('onboard-bank') else s
    if s != o:
        p.write_text(s); n += 1
print('brand: rewrote', n, 'screens')

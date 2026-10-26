"""v4.3 · Cài đặt sources in An Nhiên data: src_v40/settings-*.html → src_v43/settings-*.html (pages_settings.py reads
src_v43 when present). New Cài đặt sub-nav (v4.2.8); users = chị An, anh Khoa, Hạnh, chị Lan (+ anh Hùng link-only).
Usage: python3 settings43.py (before pages_settings.py)"""
import re, pathlib
HERE = pathlib.Path(__file__).parent
SUBNAV = lambda cur: ('<nav class="c-subnav c-subnav--wrap" aria-label="Cài đặt">' + ''.join(
    f'<a class="c-subnav__item" href="{h}"' + (' aria-current="page"' if t == cur else '') + f'>{t}</a>'
    for t, h in [('Sẵn sàng', 'readiness.html'), ('Hộ & mô hình', 'setup-business.html'), ('Dữ liệu nền', 'setup-data.html'), 
                 ('Vai trò & duyệt', 'setup-policy.html'), ('Tính năng', 'settings-features.html'), ('Hiển thị', 'settings-display.html')]) + '</nav>')
CUR = {'settings-users': 'Vai trò & duyệt', 'settings-users--otp': 'Vai trò & duyệt', 'settings-features': 'Tính năng', 'settings-display': 'Hiển thị'}
USERS = [('Trần Thị Hai', 'Phạm Thị An'), ('Điện thoại chị Hai', 'Điện thoại chị An'), ('Nguyễn Văn Phúc', 'Nguyễn Minh Khoa'), ('Điện thoại Phúc', 'Laptop anh Khoa'),
         ('Lê Thị Hoa', 'Hạnh'), ('Laptop quầy', 'Máy quầy'), ('Lê Văn Minh', 'chị Lan'), ('>Quản lý<', '>Người vận hành<'),
         ('Mọi việc, trừ đổi tài khoản ngân hàng và người dùng', 'Bán, mua, kho, gán tiền · không duyệt thuế, tiền'),
         ('Kế toán · Sổ &amp; thuế, Hoá đơn, Công nợ · chỉ xem và lập nháp', 'Kế toán dịch vụ · Sổ &amp; thuế, Hoá đơn, Công nợ · xem và lập nháp'),
         ('<th scope="col">Quản lý</th>', '<th scope="col">Người vận hành</th>'), ('4 người dùng · 3 thiết bị đang đăng nhập', '4 người dùng · 3 thiết bị · anh Hùng dùng link'),
         ('hoạt động 10:44</span>', 'hoạt động 10:12</span>', 1), ('Nguyễn Minh Khoa · hoạt động 10:31', 'Nguyễn Minh Khoa · hoạt động 10:45'),
         ('Hạnh · hoạt động 10:42', 'Hạnh · hoạt động 10:44'),
         ('Mã gửi qua Zalo tới 0905 812 347', 'Mã gửi qua Zalo tới 0935 112 418 (chị An)')]
DISPLAY = [('Giữ chế độ Gọn cho chị Hai', 'Giữ chế độ Gọn cho chị An'), ('Aa 1.020.000 ₫', 'Aa 715.000 ₫'),
           ('2 khoản QR chờ xác minh</h3><p class="c-todo__m"><span class="u-money">1.380.000 ₫</span>', 'Soạn DH-2052 cho Sunrise Hotel</h3><p class="c-todo__m"><span class="u-money">giao trước 15:00</span>'),
           ('Ví dụ: đã xác minh 4.560.000 ₫, chờ xác minh 1.380.000 ₫, tiền mặt 2.520.000 ₫', 'Ví dụ: đã xác minh 4.745.000 ₫, chờ xác minh 390.000 ₫, chưa thu 2.100.000 ₫'),
           ('style="flex:4560"', 'style="flex:4745"'), ('style="flex:1380"', 'style="flex:390"'), ('style="flex:2520"', 'style="flex:2100"'),
           ('<span class="c-split__k">Chờ xác minh · 2 khoản</span><b class="c-split__v">1.380.000', '<span class="c-split__k">Chờ xác minh · 1 khoản</span><b class="c-split__v">390.000'),
           ('<span class="c-split__k">Đã xác minh</span><b class="c-split__v">4.560.000', '<span class="c-split__k">Đã xác minh</span><b class="c-split__v">4.745.000'),
           ('<span class="c-split__k">Tiền mặt</span><b class="c-split__v">2.520.000', '<span class="c-split__k">Chưa thu</span><b class="c-split__v">2.100.000')]
FEATURES = [('Chị Hai, Phúc, Hoa và kế toán cùng làm việc.', 'Chị An, anh Khoa, Hạnh và chị Lan (kế toán) cùng làm việc.'),
            ('Chị có đơn Zalo cần giao tận nơi.', 'Chị có đơn Zalo OA cần giao tận nơi, giao xe khách, thu hộ.'),
            ('Mã QR trên bao bì đặc sản. Báo OPC nếu chị cần.', 'Mã QR trên tem lô bò một nắng · trang công khai chỉ khi chị bật. Báo OPC nếu chị cần.')]


def run(name):
    s = (HERE / f'src_v40/{name}.html').read_text()
    s = re.sub(r'<nav class="c-subnav c-subnav--wrap" aria-label="Cài đặt">[\s\S]*?</nav>', lambda m: SUBNAV(CUR[name]), s, count=1)
    s = s.replace('Hải sản khô Cô Hai', 'Đặc sản An Nhiên')
    for item in USERS + DISPLAY + FEATURES:
        a, b = item[0], item[1]
        s = s.replace(a, b, item[2]) if len(item) == 3 else s.replace(a, b)
    (HERE / f'src_v43/{name}.html').write_text(s)
    m = s[s.find('<main'):]
    left = [w for w in ['Cô Hai', 'chị Hai', 'Chị Hai', 'Phúc', 'Hoa ', 'Lê Văn Minh', '1.020.000', '1.380.000', 'Nhơn Lý'] if w in m]
    print(name, 'LEFT ' + ','.join(left) if left else 'ok')


for n in CUR:
    run(n)

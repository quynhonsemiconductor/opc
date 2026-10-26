"""v4.3 · Onboarding ⓪ phần A in An Nhiên data (01/07/2026, chị An) + new step "Mô hình kinh doanh".
Steps: see onboard_lib.STEPS (v7.0.0: 6) → Bán thử →
Xong = "Bắt đầu nhanh xong" → Sẵn sàng (readiness--new). Hoá đơn moves to phần B (onboard-invoice is reached from
Sẵn sàng). Onboarding screens are hand-edited HTML: this script snapshots them once (src_v43/onboard_v42/) and
rewrites from the snapshot, so it is idempotent. Run before onboard_aside.py. Usage: python3 onboard43.py"""
import re, shutil, pathlib
HERE = pathlib.Path(__file__).parent
SCREENS = HERE.parents[1] / 'apps/app/screens'
SNAP = HERE / 'src_v43/onboard_v42'
ic = lambda i: f'<svg class="c-ic" aria-hidden="true"><use href="#{i}"/></svg>'
if not SNAP.exists():
    SNAP.mkdir(parents=True)
    for f in SCREENS.glob('onboard-*.html'):
        if f.name != 'onboard-firstsale.html':
            shutil.copy(f, SNAP / f.name)

from onboard_lib import STEPS, STEP_OF   # v7.0.0: single source


def steps(n):
    t = STEPS[n - 1]
    segs = ''.join(f'<li class="c-steps__seg {"c-steps__seg--done" if i < n else "c-steps__seg--now" if i == n else ""}"></li>' for i in range(1, len(STEPS) + 1))
    return (f'<div class="c-steps" role="img" aria-label="Bước {n} trên {len(STEPS)}: {t}"><span class="c-steps__label"><b>Bước {n}/{len(STEPS)}</b> · {t}</span>'
            f'<ol class="c-steps__bar">{segs}</ol></div>')


GLOBAL = [
    ('HỘ KINH DOANH TRẦN THỊ HAI', 'HỘ KINH DOANH ĐẶC SẢN CAO NGUYÊN AN NHIÊN'), ('HO KINH DOANH TRAN THI HAI', 'HKD DAC SAN CAO NGUYEN AN NHIEN'),
    ('TRAN THI HAI', 'PHAM THI AN'), ('Trần Thị Hai', 'Phạm Thị An'), ('NGUYEN VAN PHUC', 'NGUYEN MINH KHOA'),
    ('Hải sản khô Cô Hai', 'Đặc sản An Nhiên'), ('Cô Hai', 'An Nhiên'), ('chị Hai', 'chị An'), ('Chị Hai', 'Chị An'),
    ('4101678913', '5901234568'), ('4101678912', '5901234567'),
    ('thôn Lý Hưng, Nhơn Lý, Quy Nhơn, Gia Lai', '86 Lê Lợi, phường Pleiku, Gia Lai'),
    ('<dt>Ngành</dt><dd>Bán lẻ thực phẩm</dd>', '<dt>Ngành</dt><dd>Chế biến thịt · bán buôn, bán lẻ thực phẩm</dd>'),
    ('Bán chính<br><b>Hải sản khô</b>', 'Bán chính<br><b>Đặc sản Tây Nguyên · bò một nắng, muối kiến vàng</b>'),
    ('0905 812 347', '0935 112 418'), ('0123 4567 89', '0901 2345 678'), ('0987 6543 21', '0905 214 778'),
    ('Nguyễn Thị Lan · Tổ hỗ trợ OPC Nhơn Lý', 'Trần Thị Thu · OPC Gia Lai, Pleiku'), ('hỗ trợ xã Nhơn Lý', 'OPC Gia Lai · Pleiku'),
    ('Gọi chị Lan', 'Gọi chị Thu'), ('Hẹn chị Lan', 'Hẹn chị Thu'), ('chị Lan', 'chị Thu'),
    ('Thứ Bảy 03/10/2026, 8:00', 'Thứ Năm 02/07/2026, 8:00'), ('Thứ Bảy 03/10', 'Thứ Năm 02/07'), ('02/10/2026', '01/07/2026'),
    ('“mực khô một triệu hai trăm năm mươi một ký”', '“bò một nắng gói nửa ký hai trăm sáu mươi nghìn”'),
    ('Hải sản khô 24 món hay bán', 'Đặc sản Tây Nguyên 18 món hay bán'),
    ('Khoảng 15 phút · làm dở vẫn lưu', 'Khoảng 10 phút · làm dở vẫn lưu'),
]

REVIEW = f'''<main class="r-onboard__body">
    <h1 class="r-onboard__title">AI đọc được 2 món, 4 giá — chị kiểm tra trước khi lưu</h1>
    <p class="c-say">Từ ảnh <b>bảng giá viết tay</b> · chụp 10:12 · 01/07/2026 · có 2 cột: giá lẻ và giá khách sạn</p>
    <p class="c-say" role="status"><b>3 giá chắc chắn · 1 giá cần kiểm tra.</b> Ô vàng nét đứt là chỗ AI chưa chắc. Lưu xong vẫn sửa được.</p>
    <section aria-labelledby="h-check">
      <h2 class="c-card__title" id="h-check">1 giá chị cần kiểm tra</h2>
      <ul class="m-rows" aria-labelledby="h-check">
        <li class="m-row">
          <span class="c-list__name">Muối kiến vàng 100g · giá khách sạn</span>
          <div class="m-check">
            <label class="c-field" data-check><span class="c-field__label">Giá khách sạn</span><span class="c-field__control"><input class="c-field__input" inputmode="numeric" value="55.000" aria-describedby="h-p3"><span class="c-field__suffix">₫/hũ</span></span><span class="c-field__hint" id="h-p3">Ảnh ghi <b>“5?.000”</b> · AI đoán <b>55.000</b> — chị sửa nếu chưa đúng</span></label>
            <div class="m-act"><button class="c-btn" type="button">Đúng rồi</button><button class="c-btn c-btn--quiet" type="button">{ic("i-photo")}Xem trong ảnh</button></div>
          </div>
        </li>
      </ul>
    </section>
    <details class="r-onboard__recap" open>
      <summary><span class="c-sign c-sign--ok" id="h-sure"><span class="c-sign__pic">{ic("i-check")}</span>3 giá AI đọc chắc chắn</span><span class="u-meta">Thu gọn</span></summary>
      <ul class="c-list" aria-labelledby="h-sure">
        <li class="c-list__row"><span class="c-list__name">Bò một nắng 500g · giá lẻ</span><span class="m-amt"><span class="c-list__amt r-sure">260.000 ₫/gói</span><button class="c-btn c-btn--quiet" type="button">Sửa</button></span></li>
        <li class="c-list__row"><span class="c-list__name">Bò một nắng 500g · giá khách sạn</span><span class="m-amt"><span class="c-list__amt r-sure">230.000 ₫/gói</span><button class="c-btn c-btn--quiet" type="button">Sửa</button></span></li>
        <li class="c-list__row"><span class="c-list__name">Muối kiến vàng 100g · giá lẻ</span><span class="m-amt"><span class="c-list__amt r-sure">65.000 ₫/hũ</span><button class="c-btn c-btn--quiet" type="button">Sửa</button></span></li>
      </ul>
    </details>
    <p class="c-say">Cột “giá khách sạn” sẽ thành một <b>bảng giá riêng</b>; chị gán khách nào dùng bảng này ở bước Sẵn sàng.</p>
    <p class="r-onboard__saved">Đã lưu — làm tiếp lúc nào cũng được</p>
  </main>'''


def chk(on, t, m, plan):
    return (f'<button class="c-option{" c-option--on" if on else ""}" type="button" role="checkbox" aria-checked="{"true" if on else "false"}">'
            f'<span class="c-option__box" aria-hidden="true">{ic("i-check") if on else ""}</span><span class="c-option__body"><strong class="c-option__title">{t}</strong>'
            f'<span class="c-option__meta">{m}</span><span class="r-model__plan">{plan}</span></span></button>')


MODEL_MAIN = f'''<main class="r-onboard__body">
    <h1 class="r-onboard__title">Chị bán thế nào, hàng từ đâu?</h1>
    <p class="c-say">Chọn mọi cách chị đang làm. OPC dựa vào đây để lập danh sách việc cần chuẩn bị — đổi lại lúc nào cũng được.</p>
    <section aria-labelledby="m-sell"><h2 class="c-card__title" id="m-sell">Chị bán thế nào?</h2>
      <div class="c-options r-model" role="group" aria-labelledby="m-sell">
        {chk(True, 'Tại quầy', 'khách đến mua, trả QR hoặc tiền mặt', 'thêm: hoá đơn máy tính tiền, bán thử ở quầy')}
        {chk(True, 'Cho khách sỉ, khách sạn, nhà hàng', 'đặt qua Zalo, giá riêng, ghi nợ, giao tận nơi', 'thêm: khách + hạn mức, giá riêng, hoá đơn có mã, cách giao')}
        {chk(False, 'Online, trên sàn', 'Shopee, TikTok Shop…', 'nếu chọn: kênh bán, đối chiếu tiền sàn')}
      </div></section>
    <section aria-labelledby="m-src"><h2 class="c-card__title" id="m-src">Hàng từ đâu?</h2>
      <div class="c-options r-model" role="group" aria-labelledby="m-src">
        {chk(True, 'Mua về bán lại', 'ví dụ muối kiến vàng từ HTX', 'thêm: nhà cung cấp, nhận hàng')}
        {chk(True, 'Tự chế biến', 'ví dụ bò một nắng từ thịt bò tươi', 'thêm: tồn đầu kỳ theo lô, chế biến, truy xuất')}
      </div></section>
    <p class="r-onboard__saved">Đã lưu — làm tiếp lúc nào cũng được</p>
  </main>'''

DONE_MAIN = f'''<main class="r-onboard__body">
    <h1 class="r-onboard__title">Xong phần bắt đầu! Quầy đã bán được</h1>
    <details class="r-onboard__recap">
      <summary><span class="c-sign c-sign--ok"><span class="c-sign__pic">{ic("i-check")}</span>6/6 bước · bán thử xong · 01/07/2026</span><span class="u-meta">Xem lại</span></summary>
      <ol class="c-todo" aria-label="Đã làm xong">
        <li class="c-todo__item c-todo__item--done"><span class="c-todo__n" aria-hidden="true">{ic("i-check")}</span><div><h3 class="c-todo__t">Số điện thoại</h3><p class="c-todo__m">0935 112 418</p></div></li>
        <li class="c-todo__item c-todo__item--done"><span class="c-todo__n" aria-hidden="true">{ic("i-check")}</span><div><h3 class="c-todo__t">Hộ kinh doanh</h3><p class="c-todo__m">MST 5901234567</p></div></li>
        <li class="c-todo__item c-todo__item--done"><span class="c-todo__n" aria-hidden="true">{ic("i-check")}</span><div><h3 class="c-todo__t">Mô hình kinh doanh</h3><p class="c-todo__m">quầy · khách sỉ · mua về bán · tự chế biến</p></div></li>
        <li class="c-todo__item c-todo__item--done"><span class="c-todo__n" aria-hidden="true">{ic("i-check")}</span><div><h3 class="c-todo__t">Việc OPC làm</h3><p class="c-todo__m">4 việc cần nối · đã chọn cách</p></div></li>
        <li class="c-todo__item c-todo__item--done"><span class="c-todo__n" aria-hidden="true">{ic("i-check")}</span><div><h3 class="c-todo__t">Xác minh chủ hộ</h3><p class="c-todo__m">chị An · L1</p></div></li>
        <li class="c-todo__item c-todo__item--done"><span class="c-todo__n" aria-hidden="true">{ic("i-check")}</span><div><h3 class="c-todo__t">Nhận tiền · MB qua Casso</h3><p class="c-todo__m">tài khoản tổ chức tên hộ 0901 2345 678</p></div></li>
        <li class="c-todo__item c-todo__item--done"><span class="c-todo__n" aria-hidden="true">{ic("i-check")}</span><div><h3 class="c-todo__t">Hàng hoá</h3><p class="c-todo__m">2 món · giá lẻ và giá khách sạn</p></div></li>
      </ol>
    </details>
    <section class="c-card c-card--tight" aria-labelledby="dn-next"><div class="c-card__head"><h2 class="c-card__title" id="dn-next">Để bán cho khách sỉ: còn 6 việc bắt buộc</h2></div>
      <p class="c-sub">OPC lập theo mô hình của chị — tồn đầu kỳ theo lô, khách và hạn mức, nhà cung cấp, hoá đơn có mã, cách giao, người dùng. Bán ở quầy thì dùng được ngay.</p></section>
    <p class="r-onboard__saved">Đã lưu — làm tiếp lúc nào cũng được</p>
  </main>'''
DONE_FOOT = (f'<footer class="r-onboard__foot">\n    <a class="c-btn c-btn--act c-btn--block" href="readiness--new.html">Xem danh sách Sẵn sàng{ic("i-arrow")}</a>\n'
             '    <div class="r-onboard__alt"><a href="counter.html">Hoặc mở quầy bán hàng ngay</a></div>\n  </footer>')   # v4.5.6: one primary


def run(name, src=None):
    s = (SNAP / f'{src or name}.html').read_text()
    for a, b in GLOBAL:
        s = s.replace(a, b)
    n = STEP_OF.get(name)
    if n:
        s = re.sub(r'<div class="c-steps" role="img" aria-label="[^"]*"><span class="c-steps__label">.*?</ol></div>', lambda m: steps(n), s, count=1, flags=re.S)
    if n:
        s = re.sub(r'<title>Bước \d/\d', f'<title>Bước {n}/{len(STEPS)}', s)
        s = re.sub(r'(<title>[^<]*?)Bước \d/\d', lambda m: m.group(1) + f'Bước {n}/{len(STEPS)}', s)
        s = re.sub(r'Bước \d/\d( · Hàng hoá</span>)', lambda m: f'Bước {n}/{len(STEPS)}' + m.group(1), s)
        s = s.replace('<title>Bước ' + str(n) + '/7 · Ngân hàng', '<title>Bước ' + str(n) + '/7 · Nhận tiền')
    if name == 'onboard-household':
        s = s.replace('href="onboard-verify.html">Đúng, tiếp tục', 'href="onboard-model.html">Đúng, tiếp tục')
        # v4.5.5 eval: the confirmed tax code is the first read of this step (figure-led, like the rest of OPC)
        s = s.replace('<p class="c-say">Chị vừa nhập mã số thuế <b>5901234567</b> · OPC tra từ cổng thuế lúc 10:02 · <a href="#">Sửa</a></p>',
                      '<p class="r-onboard__fig"><b class="c-figure">5901234567</b><span class="c-sign c-sign--ok"><span class="c-sign__pic">' + ic('i-check') + '</span>Khớp mã số thuế</span></p>'
                      '<p class="c-say">OPC tra từ cổng thuế lúc 10:02 · <a href="#">Sửa mã</a></p>')
        s = re.sub(r'(<h2 class="c-card__title" id="hh-r">Cổng thuế trả về</h2>)<span class="c-sign c-sign--ok"><span class="c-sign__pic">.*?</span>Khớp mã số thuế</span>', r'\1', s, count=1, flags=re.S)
    if name == 'onboard-products--review':
        s = re.sub(r'<main class="r-onboard__body">[\s\S]*?</main>', lambda m: REVIEW, s, count=1)
        s = re.sub(r'Lưu 9 món · còn 2 món chưa kiểm tra', 'Lưu 2 món · 1 giá chưa xác nhận', s)
    if name == 'onboard-model':
        s = re.sub(r'<main class="r-onboard__body">[\s\S]*?</main>', lambda m: MODEL_MAIN, s, count=1)
        s = re.sub(r'<footer class="r-onboard__foot">[\s\S]*?</footer>', lambda m: (
            f'<footer class="r-onboard__foot">\n    <p class="c-decide__result r-model__sum" role="status">Kế hoạch của chị: <b>17 việc</b> · 6 bắt buộc trước khi bán cho khách sỉ · 4 nên có · 7 xong ngay khi đăng ký</p>\n'
            f'    <a class="c-btn c-btn--act c-btn--block" href="onboard-verify.html">Tiếp tục{ic("i-arrow")}</a>\n'
            '    <div class="r-onboard__alt"><a href="onboard-help.html">Chưa chắc — nhờ nhân viên OPC hỏi giúp</a></div>\n  </footer>'), s, count=1)
        s = s.replace('href="onboard-otp.html" aria-label="Quay lại bước trước"', 'href="onboard-household.html" aria-label="Quay lại bước trước"')
        s = re.sub(r'<title>[^<]*</title>', '<title>Đăng ký · Mô hình kinh doanh — OPC</title>', s)
    if name == 'onboard-done':
        s = re.sub(r'<main class="r-onboard__body">[\s\S]*?</main>', lambda m: DONE_MAIN, s, count=1)
        s = re.sub(r'<footer class="r-onboard__foot">[\s\S]*?</footer>', lambda m: DONE_FOOT, s, count=1)
    if name == 'onboard-invoice':
        s = re.sub(r'<title>Bước \d/\d · Hoá đơn', '<title>Sẵn sàng · Hoá đơn', s)
    if name == 'onboard-invoice':   # phần B: reached from Sẵn sàng, no step counter
        s = re.sub(r'<div class="c-steps" role="img" aria-label="[^"]*"><span class="c-steps__label">.*?</ol></div>',
                   '<div class="c-steps" role="img" aria-label="Sẵn sàng: Hoá đơn"><span class="c-steps__label"><b>Sẵn sàng</b> · Hoá đơn</span></div>', s, count=1, flags=re.S)
        s = s.replace('Hộ bán trên 1 tỷ đồng mỗi năm (khoảng 2,7 triệu mỗi ngày) phải xuất hoá đơn điện tử từ máy tính tiền. OPC làm tự động mỗi khi bán.',
                      'Hộ bán trên 1 tỷ đồng mỗi năm phải xuất hoá đơn máy tính tiền ở quầy. Bán cho khách sỉ thì thêm hoá đơn có mã và chữ ký số. Bấm Thu tiền = phát hành.')
    if name == 'onboard-assisted':
        s = s.replace('Bước 3/6', 'Bước 4/5').replace('Bước 4/6', 'Bước 4/5')
        CK = ic('i-check')
        todo = ('<ol class="c-todo">'
                f'<li class="c-todo__item c-todo__item--done"><span class="c-todo__n" aria-hidden="true">{CK}</span><div><h3 class="c-todo__t">Số điện thoại</h3><p class="c-todo__m">Xong 10:01</p></div></li>'
                f'<li class="c-todo__item c-todo__item--done"><span class="c-todo__n" aria-hidden="true">{CK}</span><div><h3 class="c-todo__t">Hộ kinh doanh</h3><p class="c-todo__m">Xong 10:02</p></div></li>'
                f'<li class="c-todo__item c-todo__item--done"><span class="c-todo__n" aria-hidden="true">{CK}</span><div><h3 class="c-todo__t">Mô hình kinh doanh</h3><p class="c-todo__m">Xong 10:04 · quầy, khách sỉ, mua về bán, tự chế biến</p></div></li>'
                f'<li class="c-todo__item c-todo__item--done"><span class="c-todo__n" aria-hidden="true">{CK}</span><div><h3 class="c-todo__t">Việc OPC làm</h3><p class="c-todo__m">Xong 10:06 · 4 việc cần nối đã chọn cách</p></div></li>'
                '<li class="c-todo__item c-todo__item--now" aria-current="step"><span class="c-todo__n" aria-hidden="true">5</span><div><h3 class="c-todo__t">Xác minh chủ hộ</h3><p class="c-todo__m">Chị An quét mã bên phải bằng app Cas ID.</p></div></li>'
                '<li class="c-todo__item"><span class="c-todo__n" aria-hidden="true">6</span><div><h3 class="c-todo__t">Nhận tiền</h3><p class="c-todo__m">Tiếp theo</p></div></li>'
                '<li class="c-todo__item"><span class="c-todo__n" aria-hidden="true">7</span><div><h3 class="c-todo__t">Hàng hoá</h3><p class="c-todo__m">Tiếp theo · sau đó bán thử</p></div></li></ol>')
        s = re.sub(r'<ol class="c-todo">.*?</ol>', lambda m: todo, s, count=1, flags=re.S)
    (SCREENS / f'{name}.html').write_text(s)
    m = s[s.find('<body'):]
    left = [w for w in ['Cô Hai', 'Nhơn Lý', 'Quy Nhơn', 'Trần Thị Hai', 'Phúc', 'Mực', 'Cá ', 'chị Lan', '4101678'] if w in m]
    print(name, 'LEFT ' + ','.join(left) if left else 'ok')


for f in sorted(SNAP.glob('onboard-*.html')):
    run(f.stem)
run('onboard-model', src='onboard-household')

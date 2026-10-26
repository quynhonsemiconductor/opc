# v4.0 catalog + registry update: title/intro/colour swatches → Calm, Lucide sprite filled, one section per new
# component family (every variant/state), registry entries for every new c-* class. Usage: python3 catalog_v4.py
import json, re, pathlib
SYS = (pathlib.Path(__file__).resolve().parents[2] / 'system')
CAT = SYS / 'components/catalog.html'
REG = SYS / 'components/registry.json'
ICONS = {**json.load(open(SYS / 'assets/icons/lucide-map.json')), **json.load(open(SYS / 'assets/icons/lucide-extra.json'))}
ic = lambda i: f'<svg class="c-ic" aria-hidden="true"><use href="#{i}"/></svg>'
sign = lambda k, i, t: f'<span class="c-sign c-sign--{k}"><span class="c-sign__pic">{ic(i)}</span>{t}</span>'
cur = '<span class="u-cur">₫</span>'

def paysteps(state):
    S = [('i-qr', 'Chờ khách chuyển'), ('i-clock', 'Đã nhận · chờ xác minh'), ('i-check', 'Đã xác minh')]
    idx = {'wait': 0, 'pend': 1, 'ok': 2}[state]; now = {'wait': 'now', 'pend': 'pendnow', 'ok': 'oknow'}[state]; out = []
    for n, (i, t) in enumerate(S):
        if n < idx: out.append(f'<li class="c-paysteps__s c-paysteps__s--done"><span class="c-paysteps__dot">{ic("i-check")}</span><span>{t}</span></li>')
        elif n == idx: out.append(f'<li class="c-paysteps__s c-paysteps__s--{now}" aria-current="step"><span class="c-paysteps__dot">{ic(i)}</span><span>{t}<span class="c-paysteps__here">Đang ở đây</span></span></li>')
        else: out.append(f'<li class="c-paysteps__s c-paysteps__s--next"><span class="c-paysteps__dot">{ic(i)}</span><span>{t}</span></li>')
    return f'<ol class="c-paysteps" aria-label="Trạng thái tiền: {state}">' + ''.join(out) + '</ol>'

bars = ''.join(f'<li class="c-bars__d{" c-bars__d--today" if k=="Hôm nay" else ""}" style="--v:{v}"><span class="c-bars__col"><span class="c-bars__bar"></span>{"<span class=\"c-bars__v\" aria-hidden=\"true\">8,46 tr</span>" if k=="Hôm nay" else ""}</span><span class="c-bars__k">{k}</span></li>'
               for v, k in [(.87, 'T7'), (1, 'CN'), (.56, 'T2'), (.53, 'T3'), (.6, 'T4'), (.63, 'T5'), (.75, 'Hôm nay')])
tile = lambda name, price, extra='', attrs='', unit='': f'<button class="c-tile" type="button"{attrs}>{extra}<span class="c-tile__name">{name}</span><span class="c-tile__price">{price}{unit}</span></button>'
qty = lambda t: f'<span class="c-tile__qty" aria-hidden="true">{ic("i-check")}{t}</span>'

SECTIONS = f'''
  <!-- ===================== v4.0 "Modern · Calm" ===================== -->
  <section class="sec" aria-labelledby="s-v4-stat">
    <h2 id="s-v4-stat">Số của hôm nay · c-stat, c-bars, c-split</h2>
    <p>Một con số trả lời “hôm nay thế nào”, biểu đồ 7 ngày (chỉ cột hôm nay mang màu thương hiệu) và thanh <b>tiền thật</b> — chữ ký của OPC: xanh đặc = đã xác minh, hổ phách gạch chéo + viền đứt = chờ xác minh, xám = tiền mặt. Khoản chờ là một liên kết tới việc cần làm.</p>
    <section class="c-stat" aria-labelledby="cat-rev">
      <div class="c-stat__top"><h3 class="c-stat__label" id="cat-rev">Doanh thu hôm nay</h3><span class="c-stat__fresh">MB · cập nhật 2 phút trước</span></div>
      <div class="c-stat__main"><div><p class="c-stat__fig">8.460.000{cur}</p><p class="c-stat__delta"><span class="c-stat__chip">{ic("i-trend")}19%</span>so với hôm qua · 23 đơn</p><a class="c-stat__why" href="#">Vì sao tăng?{ic("i-chev-r")}</a></div>
        <ol class="c-bars" aria-label="Doanh thu 7 ngày">{bars}</ol></div>
      <div class="c-split"><div class="c-split__bar" role="img" aria-label="Đã xác minh 4.560.000 ₫, chờ 1.380.000 ₫, tiền mặt 2.520.000 ₫"><i class="c-split__ok" style="flex:4560"></i><i class="c-split__pend" style="flex:1380"></i><i class="c-split__cash" style="flex:2520"></i></div>
        <ul class="c-split__legend"><li class="c-split__item c-split__item--ok"><span class="c-split__k">QR đã xác minh</span><b class="c-split__v">4.560.000{cur}</b></li><li class="c-split__item c-split__item--pend"><a href="#"><span class="c-split__k">Chờ xác minh · 2 khoản</span><b class="c-split__v">1.380.000{cur}</b></a></li><li class="c-split__item c-split__item--cash"><span class="c-split__k">Tiền mặt</span><b class="c-split__v">2.520.000{cur}</b></li></ul></div>
    </section>
    <div class="grid2">
      <div class="demo-col"><span class="lbl">--stale · mất kết nối</span><span class="c-stat__fresh c-stat__fresh--stale">số liệu đến 10:44 · đang chờ MB</span></div>
      <div class="demo-col"><span class="lbl">--zero · lần đầu</span><p class="c-stat__fig c-stat__fig--zero">0{cur}</p></div>
    </div>
  </section>

  <section class="sec" aria-labelledby="s-v4-health">
    <h2 id="s-v4-health">Trạng thái kết nối · c-health · c-off</h2>
    <p>Mọi kết nối gom vào MỘT viên; chi tiết ở tooltip (máy tính) hoặc khi chạm (điện thoại). Đỏ chỉ khi mất kết nối.</p>
    <div class="demo"><span class="c-health" tabindex="0" data-tip="MB cập nhật 2 phút trước · Hilo hoạt động">Đã lưu · <b>10:45</b></span><span class="c-health c-health--err" tabindex="0">MB mất kết nối · <b>10:45</b></span><span class="c-off">Cổng thuế chưa bật</span><span class="c-count">6</span><a class="c-link" href="#">Xem tất cả{ic("i-chev-r")}</a></div>
  </section>

  <section class="sec" aria-labelledby="s-v4-todo">
    <h2 id="s-v4-todo">Cần làm · c-todo</h2>
    <p>Số thứ tự = làm trước. Mỗi việc một nút; chỉ việc số 1 có nút chính. Việc đã xong giữ dấu ✓ (thiết lập lần đầu).</p>
    <div class="surface mid"><ol class="c-todo">
      <li class="c-todo__item c-todo__item--done"><span class="c-todo__n" aria-hidden="true">{ic("i-check")}</span><div><h3 class="c-todo__t">Xác minh chủ hộ</h3><p class="c-todo__m">Xong 01/10/2026 · mức L1</p></div></li>
      <li class="c-todo__item c-todo__item--now"><span class="c-todo__n" aria-hidden="true">1</span><div><h3 class="c-todo__t">2 khoản QR chờ xác minh</h3><p class="c-todo__m">DH-1043 lúc 10:42 · DH-1041 lúc 10:05</p></div><a class="c-btn c-btn--act c-todo__go" href="#">Đối chiếu</a></li>
      <li class="c-todo__item"><span class="c-todo__n" aria-hidden="true">2</span><div><h3 class="c-todo__t">Chuyển khoản chưa có mã đơn</h3><p class="c-todo__m"><span class="u-money">2.150.000 ₫</span> · có thể của Nhà hàng Biển Đông</p></div><a class="c-btn c-todo__go" href="#">Gán đơn</a></li>
    </ol><a class="c-todo__later" href="#"><span><b>3 việc không gấp</b> · hoá đơn chờ mã CQT, sắp hết hàng</span>{ic("i-chev-r")}</a></div>
  </section>

  <section class="sec" aria-labelledby="s-v4-orders">
    <h2 id="s-v4-orders">Danh sách đơn · c-orders · c-debts · c-figure</h2>
    <p>Dòng thay cho bảng: ai mua trước, số tiền nổi nhất, trạng thái là nhãn màu + chữ + icon.</p>
    <div class="grid2">
      <ul class="c-orders surface">
        <li class="c-orders__row"><a href="#"><span class="c-orders__who">Khách lẻ<small>DH-1043 · Tại quầy · 10:42</small></span><span class="c-orders__st">{sign("pend", "i-clock", "Chờ xác minh")}</span><span class="c-orders__amt u-money">1.020.000 ₫</span></a></li>
        <li class="c-orders__row"><a href="#"><span class="c-orders__who">Khách lẻ<small>DH-1042 · Tại quầy · 10:31</small></span><span class="c-orders__st">{sign("ok", "i-check", "Hoàn tất")}</span><span class="c-orders__amt u-money">245.000 ₫</span></a></li>
        <li class="c-orders__row"><a href="#"><span class="c-orders__who">Khách sạn Hải Âu<small>DH-1040 · Zalo · 09:48</small></span><span class="c-orders__st">{sign("you", "i-arrow", "Chờ xác nhận")}</span><span class="c-orders__amt u-money">3.420.000 ₫</span></a></li>
        <li class="c-orders__row"><a href="#"><span class="c-orders__who">Chị Thu<small>DH-1038 · Shopee · 08:55</small></span><span class="c-orders__st">{sign("err", "i-alert", "Lỗi hoá đơn")}</span><span class="c-orders__amt u-money">360.000 ₫</span></a></li>
      </ul>
      <div class="surface"><p class="c-figure">6.184.500{cur}</p><p class="c-sub">tạm tính · hạn nộp 31/10 · còn 29 ngày</p>
        <ul class="c-debts"><li class="c-debts__row"><span class="c-debts__k">Khách sạn Hải Âu</span><span class="c-debts__v">3.420.000 ₫</span><span class="c-debts__m">đơn Zalo chờ xác nhận · việc số 3</span></li><li class="c-debts__row"><span class="c-debts__k">Nhà hàng Biển Đông</span><span class="c-debts__v">2.150.000 ₫</span><span class="c-debts__m">có thể đã trả · việc số 2</span></li></ul></div>
    </div>
  </section>

  <section class="sec" aria-labelledby="s-v4-tile">
    <h2 id="s-v4-tile">Món ở Quầy · c-tiles, c-tile</h2>
    <p>Chữ trước, ảnh thật khi chủ hộ thêm. Trong đơn = nền xanh nhạt + nhãn số lượng; vừa thêm = nảy một lần; sắp hết = hổ phách + icon.</p>
    <div class="c-tiles" style="max-width:860px">
      {tile("Cá thu một nắng", "380.000 ₫", unit="<small>/kg</small>")}
      <button class="c-tile" type="button" data-incart>{qty("0,5 kg")}<span class="c-tile__name">Mực khô loại 1</span><span class="c-tile__price">1.250.000 ₫<small>/kg</small></span><span class="c-tile__meta c-tile__meta--low">{ic("i-alert")}còn 3,2 kg</span></button>
      <button class="c-tile" type="button" data-incart data-justadded>{qty("×2")}<span class="c-tile__name">Cá cơm sấy giòn hũ 250 g</span><span class="c-tile__price">95.000 ₫</span></button>
      <button class="c-tile" type="button"><span class="c-tile__name">Ruốc biển hũ 200 g</span><span class="c-tile__price">65.000 ₫</span><span class="c-tile__meta">{ic("i-scale")}bán theo cân</span></button>
    </div>
  </section>

  <section class="sec" aria-labelledby="s-v4-order">
    <h2 id="s-v4-order">Đơn đang bán · c-oline, c-stepper, c-seg, c-btn--xl, c-oempty</h2>
    <p>Dòng món → tổng (số lớn nhất màn) → cách thanh toán → một nút chính. Lựa chọn không dùng được bị gạch kèm lý do; nút khoá luôn nói cần làm gì.</p>
    <div class="grid2">
      <div class="surface demo-col">
        <ul class="r-order__lines" style="padding:0"><li class="c-oline"><span class="c-oline__name">Mực khô loại 1</span><span class="c-oline__amt">625.000 ₫</span><span class="c-oline__calc">0,5 kg × 1.250.000 ₫</span><span class="c-stepper"><button class="c-stepper__btn" type="button" aria-label="Bớt">{ic("i-minus")}</button><output class="c-stepper__value">0,5 kg</output><button class="c-stepper__btn" type="button" aria-label="Thêm">{ic("i-plus")}</button></span></li></ul>
        <div class="c-seg" role="radiogroup" aria-label="Cách thanh toán"><button class="c-seg__opt" type="button" role="radio" aria-checked="true">{ic("i-qr")}QR</button><button class="c-seg__opt" type="button" role="radio" aria-checked="false">{ic("i-cash")}Tiền mặt</button><button class="c-seg__opt" type="button" role="radio" aria-checked="false">{ic("i-book")}Công nợ</button></div>
        <div class="c-seg" role="radiogroup" aria-label="Cách thanh toán, mất kết nối"><button class="c-seg__opt" type="button" role="radio" aria-checked="false" aria-disabled="true">{ic("i-qr")}QR tạm tắt</button><button class="c-seg__opt" type="button" role="radio" aria-checked="true">{ic("i-cash")}Tiền mặt</button><button class="c-seg__opt" type="button" role="radio" aria-checked="false">{ic("i-book")}Công nợ</button></div>
        <div class="r-order__acts"><button class="c-btn c-btn--xl" type="button">Lưu tạm</button><button class="c-btn c-btn--act c-btn--xl" type="button">Thu tiền<span class="c-kbd" aria-hidden="true">F9</span></button></div>
        <button class="c-btn c-btn--xl" type="button" aria-disabled="true">{ic("i-lock")}Thêm món để thu tiền</button>
      </div>
      <div class="surface"><div class="c-oempty"><span class="c-oempty__pic">{ic("i-bag")}</span><b>Chưa có món nào</b><span>Chạm món bên trái, gõ <span class="c-kbd">/</span> để tìm, hoặc quét mã vạch</span></div></div>
    </div>
  </section>

  <section class="sec" aria-labelledby="s-v4-pay">
    <h2 id="s-v4-pay">Thu tiền QR · c-qrcard, c-paysteps, c-waitbar, c-arrived, c-note</h2>
    <p>Ba bước tiền, chỉ bước hiện tại có màu: <b>xanh biển</b> = đang chờ khách · <b>hổ phách gạch chéo</b> = đã nhận, chờ xác minh · <b>xanh lá</b> = đã xác minh. Lúc tiền về, thẻ QR được thay bằng c-arrived (hoạt ảnh một lần, thông báo cho trình đọc màn hình).</p>
    <div class="grid3">
      <div class="surface demo-col"><span class="lbl">Chờ khách chuyển</span><figure class="c-qrcard"><img src="../assets/qr-demo.svg" alt="Mã VietQR mẫu"><figcaption><b class="c-qrcard__amt">1.020.000{cur}</b><span class="u-meta">VietQR · MB · DH1043</span></figcaption></figure>{paysteps("wait")}<p class="c-waitbar" role="status"><span class="c-waitbar__spin" aria-hidden="true"></span><span><b>Đang chờ khách chuyển</b>OPC tự chuyển bước khi ngân hàng báo</span></p></div>
      <div class="surface demo-col"><span class="lbl">Đã nhận · chờ xác minh</span><figure class="c-arrived" role="status"><span class="c-arrived__pic">{ic("i-clock")}</span><figcaption><span class="c-arrived__k">Đã nhận lúc 10:44 · chờ xác minh</span><br><b class="c-arrived__amt">1.020.000{cur}</b><br><span class="c-arrived__m">từ NGUYEN VAN HUNG</span></figcaption></figure>{paysteps("pend")}<p class="c-note">{ic("i-check")}<span><b>Giao hàng được</b> — đơn dưới mức 2.000.000 ₫.</span></p></div>
      <div class="surface demo-col"><span class="lbl">Đã xác minh</span><figure class="c-arrived c-arrived--ok" role="status"><span class="c-arrived__pic">{ic("i-check")}</span><figcaption><span class="c-arrived__k">Đã xác minh · 10:47</span><br><b class="c-arrived__amt">1.020.000{cur}</b><br><span class="c-arrived__m">DH-1043 hoàn tất</span></figcaption></figure>{paysteps("ok")}</div>
    </div>
  </section>

  <section class="sec" aria-labelledby="s-v4-cash">
    <h2 id="s-v4-cash">Thu tiền mặt · c-cashpad, c-quick, c-change</h2>
    <p>Khách đưa → tiền thối (nền tối, số thứ hai quan trọng nhất). Số tiền nhanh có “vừa đủ”. Chưa nhập thì tiền thối là “—”.</p>
    <div class="grid2">
      <div class="surface demo-col"><div class="c-cashpad"><div class="c-cashpad__field"><label for="cat-g1">Khách đưa</label><input class="c-cashpad__input" id="cat-g1" inputmode="numeric" value="1.100.000"><span class="u-cur">₫</span></div><div class="c-quick" role="group" aria-label="Số tiền khách đưa"><button class="c-quick__btn" type="button" aria-pressed="false">1.020.000<small>vừa đủ</small></button><button class="c-quick__btn" type="button" aria-pressed="false">1.050.000</button><button class="c-quick__btn" type="button" aria-pressed="true">1.100.000</button></div></div><p class="c-change"><span>Tiền thối cho khách</span><b>80.000{cur}</b></p></div>
      <div class="surface demo-col"><div class="c-cashpad c-cashpad--empty"><div class="c-cashpad__field"><label for="cat-g2">Khách đưa</label><input class="c-cashpad__input" id="cat-g2" inputmode="numeric" placeholder="0"><span class="u-cur">₫</span></div></div><p class="c-change c-change--none"><span>Tiền thối cho khách</span><b>—</b></p></div>
    </div>
  </section>

  <section class="sec" aria-labelledby="s-v4-toast">
    <h2 id="s-v4-toast">Phản hồi · c-toasts, c-toast</h2>
    <p>Viên tối ở giữa dưới vùng làm việc. Tự tắt sau 4 giây, trừ lỗi. Xoá luôn đi kèm “Hoàn tác”. Trên điện thoại khi ngăn thu tiền đang mở thì không hiện (ngăn đã tự báo).</p>
    <div class="c-toasts cat-static" role="region" aria-label="Ví dụ thông báo">
      <div class="c-toast c-toast--pend"><span class="c-toast__pic">{ic("i-clock")}</span><span class="c-toast__text"><b>Đã nhận 1.020.000 ₫</b> · DH-1043 · giao hàng được</span></div>
      <div class="c-toast c-toast--ok"><span class="c-toast__pic">{ic("i-check")}</span><span class="c-toast__text"><b>Đã xác minh 1.020.000 ₫</b> · DH-1043 hoàn tất</span></div>
      <div class="c-toast"><span class="c-toast__pic">{ic("i-x")}</span><span class="c-toast__text"><b>Đã bỏ Chả cá Quy Nhơn</b> · 85.000 ₫</span><button class="c-btn" type="button">{ic("i-undo")}Hoàn tác</button></div>
    </div>
  </section>
'''

s = CAT.read_text()
s = s.replace('<title>Catalog · OPC Design System v1.0</title>', '<title>Catalog · OPC Design System v4.0</title>')
s = re.sub(r'<h1>Thư viện thành phần · v[\d.]+</h1>\s*<p class="c-say">.*?</p>',
  '<h1>Thư viện thành phần · v4.0 “Modern · Calm”</h1>\n    <p class="c-say">Nền lặng, một điểm nhấn: trang trắng, chia vùng bằng đường kẻ mảnh; <b>xanh biển</b> chỉ cho hành động chính, chỗ đang đứng và hôm nay. Chữ ký là <b>tiền thật</b>: xanh đặc = đã xác minh · hổ phách gạch chéo = đang chờ · xám = tiền mặt. Số thứ tự = việc làm trước.</p>', s, flags=re.S)
s = re.sub(r'(<h2 id="s-color">Màu theo việc</h2>\s*<p>).*?(</p>)', r'\1Mỗi màu một việc. <b>Xanh biển</b> = hành động chính / chỗ đang đứng / hôm nay. Xanh lá = đã xác minh. Hổ phách gạch chéo + viền đứt = đang chờ ngân hàng/CQT. Đỏ chỉ cho lỗi. Tiền mặt luôn xám trung tính.\2', s, flags=re.S)
s = s.replace('<span class="lbl">act · làm ngay</span>', '<span class="lbl">act · hành động chính</span>')
s = s.replace('<div class="swatch"><i style="background:var(--neutral-fill)"></i><span class="lbl">neutral · tiền mặt</span></div>',
  '<div class="swatch"><i style="background:var(--truth-cash)"></i><span class="lbl">truth-cash · tiền mặt</span></div>\n      <div class="swatch"><i style="background:var(--truth-ok)"></i><span class="lbl">truth-ok · thanh tiền thật</span></div>\n      <div class="swatch"><i style="background:var(--truth-hatch);outline:1.5px dashed var(--truth-pend);outline-offset:2px"></i><span class="lbl">truth-hatch · đang chờ</span></div>\n      <div class="swatch"><i style="background:var(--canvas-quiet)"></i><span class="lbl">canvas-quiet · panel phẳng</span></div>')
s = s.replace('.grid2 > *, .grid3 > *, .demo-col > * { min-width: 0; }', '.grid2 > *, .grid3 > *, .demo-col > * { min-width: 0; }\n.cat-static { position: static; transform: none; width: auto; justify-items: start; }   /* toasts shown in place */')
if 's-v4-stat' not in s: s = s.replace('</main>', SECTIONS + '\n</main>')
used = list(dict.fromkeys(re.findall(r'href="#(i-[\w-]+)"', s)))
sprite = '\n'.join(f'  <symbol id="{u}" viewBox="0 0 24 24">{ICONS[u]}</symbol>' for u in used if u in ICONS)
s = re.sub(r'(<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">)[\s\S]*?(</svg>)', lambda m: m.group(1) + '\n' + sprite + '\n' + m.group(2), s, count=1)
CAT.write_text(s)
print('catalog icons', len(used), 'missing', [u for u in used if u not in ICONS])

R = json.load(open(REG))
NEW = {
 'c-stat': ('TodayFigure', None, 'region', [], ['top', 'label', 'fresh', 'main', 'fig', 'delta', 'chip', 'why', 'skel'], 'Card (custom) + recharts not needed'),
 'c-bars': ('DayBars', None, 'img list (7 values, sr text per bar)', [], ['d', 'col', 'bar', 'k', 'v'], 'custom (CSS grid) or recharts BarChart'),
 'c-split': ('MoneyTruthBar', None, 'img + legend list', ['legend-only'], ['bar', 'ok', 'pend', 'cash', 'legend', 'item', 'k', 'v', 'go', 'explain', 'skel'], 'custom'),
 'c-health': ('ConnectionPill', 'tooltip', 'status', ['err'], [], 'Badge + Tooltip / Popover on touch'),
 'c-off': ('OffLabel', None, 'text', [], [], 'span'),
 'c-count': ('CountBadge', None, 'text', [], [], 'Badge variant=secondary'),
 'c-link': ('TextLink', 'link', 'link', [], [], 'Button variant=link'),
 'c-sub': ('Subline', None, 'text', [], [], 'p'),
 'c-figure': ('Figure', None, 'text', [], [], 'span'),
 'c-todo': ('TodoList', None, 'list', [], ['item', 'item--now', 'item--done', 'n', 't', 'm', 'go', 'later', 'skel'], 'custom list + Button'),
 'c-orders': ('OrderRows', None, 'list of links', [], ['row', 'who', 'st', 'amt', 'skel', 'skelrow'], 'custom list (not Table)'),
 'c-debts': ('DebtList', None, 'list', [], ['row', 'k', 'v', 'm'], 'custom list'),
 'c-tiles': ('ProductGrid', None, 'group', [], [], 'CSS grid'),
 'c-tile': ('ProductTile', 'button', 'button', ['incart (data)', 'justadded (data)'], ['pic', 'name', 'price', 'meta', 'meta--low', 'qty', 'add'], 'button (custom)'),
 'c-oline': ('OrderLine', None, 'listitem', [], ['name', 'amt', 'calc'], 'custom + Stepper'),
 'c-oempty': ('OrderEmpty', None, 'status', [], ['pic'], 'Empty (custom)'),
 'c-qrcard': ('QrCard', None, 'figure', [], ['amt'], 'figure + img'),
 'c-paysteps': ('PaymentSteps', None, 'list (aria-current=step)', [], ['s', 's--now', 's--pendnow', 's--oknow', 's--done', 's--next', 'dot', 'here'], 'custom Stepper'),
 'c-waitbar': ('WaitBar', None, 'status (live polite)', [], ['spin'], 'custom'),
 'c-arrived': ('MoneyArrived', None, 'status (live assertive)', ['ok'], ['pic', 'k', 'amt', 'm'], 'custom + motion'),
 'c-note': ('InlineNote', None, 'note', [], [], 'Alert (subtle)'),
 'c-cashpad': ('CashPad', None, 'group', ['empty'], ['field', 'input'], 'Input (numeric) custom'),
 'c-quick': ('QuickAmounts', 'toggle button group', 'group', [], ['btn'], 'ToggleGroup'),
 'c-change': ('ChangeDue', None, 'status', ['none'], [], 'custom'),
 'c-toasts': ('ToastRegion', None, 'region (live polite)', [], [], 'Sonner <Toaster position="bottom-center"/>'),
 'c-term': ('Term', 'tooltip', 'term with tooltip', [], [], 'Tooltip'),
 'c-stamp': ('Stamp (deprecated v4 — not used by any screen)', None, 'img', [], [], 'none'),
}
for k, (name, apg, role, var, parts, shad) in NEW.items():
    R[k] = {'name': name, 'apg': apg, 'role': role, 'variants': var, 'parts': parts, 'shadcn': shad, 'since': '4.0.0' if k not in ('c-term', 'c-stamp') else '3.x'}
if 'c-toast' in R: R['c-toast']['variants'] = sorted(set(R['c-toast']['variants']) | {'pend', 'ok'})
if 'c-seg' in R: R['c-seg'].setdefault('states', []); R['c-seg']['note'] = 'option aria-disabled="true" = unavailable (struck through, reason in label)'
for k in ('r-home', 'r-pos', 'r-order', 'r-cartbar'):
    R[k] = {'name': {'r-home': 'HomeLayout', 'r-pos': 'CounterLayout', 'r-order': 'OrderPanel', 'r-cartbar': 'PhoneCartBar'}[k], 'apg': 'dialog' if k == 'r-order' else None,
            'role': 'recipe', 'variants': {'r-pos': ['sheet'], 'r-order': ['pay']}.get(k, []), 'parts': [], 'shadcn': {'r-order': 'Sheet on phone (side="bottom")'}.get(k, 'layout'), 'since': '4.0.0'}
json.dump(R, open(REG, 'w'), ensure_ascii=False, indent=1)
print('registry', len(R) - 1)

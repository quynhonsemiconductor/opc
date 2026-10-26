# Builds the v4 Calm counter STATES into apps/app/screens from the two Calm templates in src/.
# Each state = template + replaced order panel (body/foot) + optional flags (sheet on phone, toast, health, tiles).
# v4.3: reads src_v43 (An Nhiên data, run src43.py first). Usage: python3 states.py
import json, re, pathlib

import re as _re
def strip_quiet_icons(h):
    """v4.5.3 icons budget: money-step dots and labelled payment options carry no icon."""
    h = _re.sub(r'(<span class="c-paysteps__dot">)<svg[^>]*>.*?</svg>', r'\1', h, flags=_re.S)
    h = _re.sub(r'(<button class="c-seg__opt"[^>]*>)<svg class="c-ic"[^>]*>.*?</svg>', r'\1', h, flags=_re.S)
    return h

HERE = pathlib.Path(__file__).parent
OUT = HERE.parents[1] / 'apps/app/screens'
SYS = (HERE.parents[1] / 'system')
ICONS = {**json.load(open(SYS / 'assets/icons/lucide-map.json')), **json.load(open(SYS / 'assets/icons/lucide-extra.json'))}

def ic(i, cls='c-ic'): return f'<svg class="{cls}" aria-hidden="true"><use href="#{i}"/></svg>'

def finish(html, title):
    html = re.sub(r'<link rel="stylesheet" href="(?:\.\./tokens-override|\.\./skin-modern|redesign|calm)\.css">\n', '', html)
    html = (html.replace('href="../../../tokens.css"', 'href="../../../system/tokens.css"')
                .replace('href="../../../components/', 'href="../../../system/components/')
                .replace('href="../../../../apps/app/app-tokens.css"', 'href="../app-tokens.css"')
                .replace('src="../../../assets/', 'src="../../../system/assets/'))
    html = re.sub(r'<title>[^<]*</title>', f'<title>{title} — OPC</title>', html)
    used = list(dict.fromkeys(re.findall(r'href="#(i-[\w-]+)"', html)))
    missing = [u for u in used if u not in ICONS]
    sprite = '<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">\n' + \
        '\n'.join(f'  <symbol id="{u}" viewBox="0 0 24 24">{ICONS[u]}</symbol>' for u in used if u in ICONS) + '\n</svg>'
    return html.replace('<!--@icons-->', sprite), missing

SEG = lambda on, qr_off=False: '<div class="c-seg" role="radiogroup" aria-label="Cách thanh toán">' + ''.join(
    f'<button class="c-seg__opt" type="button" role="radio" aria-checked="{"true" if k == on else "false"}"'
    + (' aria-disabled="true" aria-label="QR tạm tắt — cần mạng"' if (k == 'qr' and qr_off) else '')
    + f'>{"QR tạm tắt" if (k == "qr" and qr_off) else t}</button>'   # v4.5.3: labelled options carry no icon
    for k, i, t in [('qr', 'i-qr', 'QR'), ('cash', 'i-cash', 'Tiền mặt'), ('debt', 'i-book', 'Công nợ')]) + '</div>'

def steps(state):  # wait | pend | ok
    S = [('i-qr', 'Chờ khách chuyển'), ('i-clock', 'Đã nhận · chờ xác minh'), ('i-check', 'Đã xác minh')]
    idx = {'wait': 0, 'pend': 1, 'ok': 2}[state]
    now_cls = {'wait': 'c-paysteps__s--now', 'pend': 'c-paysteps__s--pendnow', 'ok': 'c-paysteps__s--oknow'}[state]
    li = []
    for n, (i, t) in enumerate(S):
        if n < idx: li.append(f'<li class="c-paysteps__s c-paysteps__s--done"><span class="c-paysteps__dot"></span><span>{t}</span></li>')
        elif n == idx: li.append(f'<li class="c-paysteps__s {now_cls}" aria-current="step"><span class="c-paysteps__dot"></span><span>{t}<span class="c-paysteps__here">Đang ở đây</span></span></li>')
        else: li.append(f'<li class="c-paysteps__s c-paysteps__s--next"><span class="c-paysteps__dot"></span><span>{t}</span></li>')
    return '<ol class="c-paysteps" aria-label="Trạng thái tiền của đơn này">' + ''.join(li) + '</ol>'

OPTS = '''<div class="r-order__opts">
          <button class="c-switch" type="button" role="switch" aria-checked="true"><span class="c-switch__track" aria-hidden="true"></span><span class="c-switch__label">In phiếu</span></button>
          <button class="c-switch" type="button" role="switch" aria-checked="false"><span class="c-switch__track" aria-hidden="true"></span><span class="c-switch__label">Hoá đơn công ty<span class="c-switch__sub">nhập MST của khách</span></span></button>
        </div>'''
QUICK = lambda sel: '<div class="c-quick" role="group" aria-label="Số tiền khách đưa">' + ''.join(
    f'<button class="c-quick__btn" type="button" aria-pressed="{"true" if v == sel else "false"}">{v}{"<small>vừa đủ</small>" if n == 0 else ""}</button>'
    for n, v in enumerate(['715.000', '720.000', '750.000', '800.000', '1.000.000', '2.000.000'])) + '</div>'
NOTE_INV = '<p class="r-order__note">Bấm Thu tiền = phát hành hoá đơn máy tính tiền (Hilo)</p>'

PAY = {
 'received': dict(seg=SEG('qr'), body=f'''<figure class="c-arrived" role="status" aria-live="assertive">
          <span class="c-arrived__pic">{ic("i-clock")}</span>
          <figcaption><span class="c-arrived__k">Đã nhận lúc 10:44 · chờ xác minh</span><br><b class="c-arrived__amt">715.000<span class="u-cur">₫</span></b><br><span class="c-arrived__m">từ TRAN THI THU · nội dung DH2053</span></figcaption>
        </figure>
        {steps("pend")}
        <p class="c-note">{ic("i-check")}<span><b>Giao hàng được</b> · dưới mức 2.000.000 ₫ · OPC tự xác nhận khi MB khớp</span></p>
        {OPTS}''', foot=f'''<a class="c-btn c-btn--act c-btn--xl" href="counter--empty.html">Giao hàng · bán đơn tiếp<span class="c-kbd" aria-hidden="true">N</span></a>
        <p class="r-order__note">Đơn này tự chuyển sang “Đã xác minh” — không cần quay lại</p>''',
   toast=('pend', 'i-clock', '<b>Đã nhận 715.000 ₫</b> · DH-2053 · giao hàng được', None)),
 'verified': dict(seg=SEG('qr'), body=f'''<figure class="c-arrived c-arrived--ok" role="status" aria-live="polite">
          <span class="c-arrived__pic">{ic("i-check")}</span>
          <figcaption><span class="c-arrived__k">Đã xác minh · MB khớp sao kê 10:47</span><br><b class="c-arrived__amt">715.000<span class="u-cur">₫</span></b><br><span class="c-arrived__m">Đơn DH-2053 hoàn tất · đang in phiếu</span></figcaption>
        </figure>
        {steps("ok")}
        <div class="r-order__opts"><p class="c-switch"><span class="c-sign c-sign--ok"><span class="c-sign__pic">{ic("i-check")}</span>Hoá đơn máy tính tiền đã phát hành</span><span class="c-switch__label"><span class="c-switch__sub">HĐ 00001291 · có mã máy tính tiền · Hilo 10:44</span></span></p></div>''',
   foot='''<a class="c-btn c-btn--act c-btn--xl" href="counter--empty.html">Đơn mới DH-2054<span class="c-kbd" aria-hidden="true">N</span></a>
        <button class="c-btn" type="button">In lại phiếu</button>''',
   toast=('ok', 'i-check', '<b>Đã xác minh 715.000 ₫</b> · DH-2053 hoàn tất', None)),
 'cash': dict(seg=SEG('cash'), body=f'''<div class="c-cashpad">
          <div class="c-cashpad__field"><label for="given">Khách đưa</label><input class="c-cashpad__input" id="given" inputmode="numeric" value="1.000.000"><span class="u-cur">₫</span></div>
          {QUICK("1.000.000")}
        </div>
        <p class="c-change" role="status"><span>Tiền thối cho khách</span><b>285.000<span class="u-cur">₫</span></b></p>
        {OPTS}''', foot=f'''<button class="c-btn c-btn--act c-btn--xl" type="button">Đã thu tiền mặt · thối 285.000 ₫<span class="c-kbd" aria-hidden="true">F9</span></button>
        {NOTE_INV}'''),
 'offline': dict(seg=SEG('cash', qr_off=True), body=f'''<div class="c-banner r-offbar" role="status"><span class="c-banner__pic">{ic("i-offline")}</span><span class="c-banner__text"><strong class="c-banner__title">Không có mạng từ 10:51 — vẫn bán tiền mặt</strong><span class="c-banner__body">QR cần mạng nên tạm tắt. Đơn, hoá đơn máy tính tiền lưu trên máy, gửi Hilo theo thứ tự khi có mạng.</span></span></div>
        <div class="c-cashpad c-cashpad--empty">
          <div class="c-cashpad__field"><label for="given">Khách đưa</label><input class="c-cashpad__input" id="given" inputmode="numeric" placeholder="0"><span class="u-cur">₫</span></div>
          {QUICK(None)}
        </div>
        <p class="c-change c-change--none" role="status"><span>Tiền thối cho khách</span><b>—</b></p>''',
   foot=f'''<button class="c-btn c-btn--xl" type="button" aria-disabled="true">{ic("i-lock")}Nhập số tiền khách đưa để thu</button>
        <p class="r-order__note">Hoá đơn lưu trên máy · gửi Hilo khi có mạng, không gửi trùng</p>''', health=('off', 'Mất mạng · <b>lưu trên máy</b>', 'Mất mạng')),
}
PAY['debt'] = dict(seg=SEG('debt'), body=f'''<div class="r-order__custok"><b>Sunrise Hotel</b><span class="u-meta">giá khách sạn &amp; nhà hàng · trả 15 ngày · hạn mức 15.000.000 ₫</span></div>
        <div class="c-banner c-banner--pend" role="status"><span class="c-banner__pic">{ic("i-alert")}</span><span class="c-banner__text"><strong class="c-banner__title">Ghi nợ cần chị An duyệt</strong><span class="c-banner__body">Sunrise đang nợ 8.400.000 ₫, quá hạn 12 ngày. Hoặc thu QR / tiền mặt ngay thì không cần duyệt.</span></span></div>
        <p class="c-decide__result">Duyệt xong = giao hàng, hoá đơn có mã cho Sunrise, phải thu 625.000 ₫ hạn 21/10</p>''',
   foot=f'''<button class="c-btn c-btn--act c-btn--xl" type="button">Gửi chị An duyệt ghi nợ</button>
        <button class="c-btn" type="button">{ic("i-qr")}Khách trả QR ngay</button>''')

def pay_state(name, key, title, sheet=False):
    s = (HERE / 'src_v43/counter--qr.html').read_text()
    st = PAY[key]
    a = s.index('<div class="r-order__body">'); b = s.index('</aside>')
    s = s[:a] + f'''<div class="r-order__body">
        {st["seg"]}
        {st["body"]}
      </div>
      <div class="r-order__foot">
        {st["foot"]}
      </div>
    ''' + s[b:]
    if key == 'debt':
        s = s.replace('<span class="u-meta">2 món · Khách lẻ</span>', '<span class="u-meta">2 món · Sunrise Hotel</span>').replace('715.000', '625.000')
        s = s.replace('<span class="c-tile__price">260.000 ₫</span>', '<span class="c-tile__price">230.000 ₫<small> giá khách sạn</small></span>').replace('<span class="c-tile__price">65.000 ₫</span>', '<span class="c-tile__price">55.000 ₫<small> giá khách sạn</small></span>')
        s = s.replace('<button class="c-chip r-pos__kc" type="button">Sunrise Hotel</button>', '<button class="c-chip r-pos__kc" type="button" aria-pressed="true">Sunrise Hotel</button>')
    if key in ('cash', 'offline'): s = s.replace('<h2 class="r-order__code" id="h-order">Thu tiền · DH-2053</h2>', '<h2 class="r-order__code" id="h-order">Thu tiền mặt · DH-2053</h2>')
    return decorate(s, st, title, sheet)

def decorate(s, st, title, sheet):
    if sheet:
        s = s.replace('<div class="r-pos">', '<div class="r-pos r-pos--sheet">')
        s = s.replace('<aside class="r-order', '<aside role="dialog" aria-modal="true" class="r-order', 1).replace('<div class="r-order__head">', '<span class="r-order__grip" aria-hidden="true"></span>\n      <div class="r-order__head">', 1)
    h = st.get('health')
    if h:
        s = re.sub(r'<span class="c-health"([^>]*)data-tip="[^"]*"([^>]*)><span class="r-pos__desk">.*?</span><span class="r-pos__phone">.*?</span></span>',
                   f'<span class="c-health c-health--{h[0]}"\\1data-tip="Không có mạng từ 10:51 · lưu trên máy 10:58 · 1 hoá đơn chờ gửi"\\2><span class="r-pos__desk">{h[1]}</span><span class="r-pos__phone">{h[2]}</span></span>', s)
    t = st.get('toast')
    if t:
        kind, i, text, btn = t
        b = f'<button class="c-btn" type="button">{btn}</button>' if btn else ''
        s = s.replace('</body>', f'<div class="c-toasts" role="region" aria-live="polite" aria-label="Thông báo">\n  <div class="c-toast c-toast--{kind}"><span class="c-toast__pic">{ic(i)}</span><span class="c-toast__text">{text}</span>{b}</div>\n</div>\n</body>')
    return finish(s, title)

def order_state(name, title, sheet=False, empty=False, undo=False, justadded=False):
    s = (HERE / 'src_v43/counter.html').read_text()
    st = {}
    if empty:
        s = s.replace(' data-incart', '')
        s = re.sub(r'<span class="c-tile__qty"[^>]*>.*?</span>(?=<span class="c-tile__name">)', '', s)
        s = re.sub(r' aria-label="([^"]*?), trong đơn [^"]*"', '', s)
        a = s.index('<ul class="r-order__lines">'); b = s.index('</ul>', a) + 5
        s = s[:a] + f'<div class="r-order__lines"><div class="c-oempty"><span class="c-oempty__pic">{ic("i-bag")}</span><b>Chưa có món nào</b><span>Chạm món bên trái, gõ <span class="c-kbd">/</span> để tìm, hoặc quét mã vạch</span></div></div>' + s[b:]
        s = s.replace('DH-2053</h2><span class="u-meta">2 món · tại quầy', 'DH-2054</h2><span class="u-meta">đơn mới · tại quầy')
        s = s.replace('<b>715.000<span class="u-cur">₫</span></b></div>', '<b>0<span class="u-cur">₫</span></b></div>', 1)
        s = re.sub(r'<a class="c-btn c-btn--act c-btn--xl" href="counter--qr.html">Thu tiền<span class="c-kbd" aria-hidden="true">F9</span></a>',
                   f'<button class="c-btn c-btn--xl" type="button" aria-disabled="true">{ic("i-lock")}Thêm món để thu tiền</button>', s)
        s = s.replace('<button class="c-btn c-btn--xl" type="button">Lưu tạm</button>', '<button class="c-btn c-btn--xl" type="button" aria-disabled="true">Lưu tạm</button>')
        s = re.sub(r'<a class="r-cartbar" href="[^"]*">.*?</a>', '', s, flags=re.S)
        st['toast'] = ('ok', 'i-check', '<b>DH-2053 đã xong</b> · 715.000 ₫ QR', None) if not undo else None
    if undo:
        a = s.index('<li class="c-oline"><span class="c-oline__name">Muối kiến vàng 100g'); b = s.index('</li>', a) + 5
        s = s[:a] + s[b:]
        s = s.replace('2 món · tại quầy', '1 món · tại quầy').replace('<b>715.000<span class="u-cur">₫</span></b></div>', '<b>520.000<span class="u-cur">₫</span></b></div>', 1)
        s = s.replace('DH-2053 · 2 món · xem giỏ</span><strong>715.000', 'DH-2053 · 1 món · xem giỏ</span><strong>520.000')
        s = re.sub(r'<button class="c-tile c-tile--big" type="button" data-incart aria-label="Muối kiến vàng 100g, 65.000 ₫, trong đơn 3, ([^"]*)">(<span class="c-tile__pic[^>]*>.*?</span>)<span class="c-tile__qty"[^>]*>.*?</span>',
                   r'<button class="c-tile c-tile--big" type="button" aria-label="Muối kiến vàng 100g, 65.000 ₫, \1">\2', s, count=1)
        st['toast'] = ('undo', 'i-x', '<b>Đã bỏ Muối kiến vàng 100g</b> · 195.000 ₫', f'{ic("i-undo")}Hoàn tác')
    if justadded:
        s = s.replace('<button class="c-tile c-tile--big" type="button" data-incart aria-label="Bò một nắng 500g', '<button class="c-tile c-tile--big" type="button" data-incart data-justadded aria-label="Bò một nắng 500g', 1)
    return decorate(s, st, title, sheet)

JOBS = {
  'counter': lambda: decorate((HERE / 'src_v43/counter.html').read_text(), {}, 'Quầy bán hàng · DH-2053', False),
  'counter--qr': lambda: decorate((HERE / 'src_v43/counter--qr.html').read_text(), {}, 'Quầy · Thu tiền QR · DH-2053', False),
  'counter--debt': lambda: pay_state('debt', 'debt', 'Quầy · Khách quen ghi nợ, cần duyệt · DH-2053'),
  'counter--received': lambda: pay_state('received', 'received', 'Quầy · Đã nhận, chờ xác minh · DH-2053'),
  'counter--verified': lambda: pay_state('verified', 'verified', 'Quầy · Đã xác minh · DH-2053'),
  'counter--cash': lambda: pay_state('cash', 'cash', 'Quầy · Thu tiền mặt · DH-2053'),
  'counter--offline': lambda: pay_state('offline', 'offline', 'Quầy · Mất mạng, vẫn bán tiền mặt · DH-2053'),
  'counter--empty': lambda: order_state('empty', 'Quầy · Đơn mới DH-2054', empty=True),
  'counter--undo': lambda: order_state('undo', 'Quầy · Vừa bỏ một món · DH-2053', undo=True),
  'counter--cart': lambda: order_state('cart', 'Quầy · Giỏ hàng (điện thoại) · DH-2053', sheet=True, justadded=True),
  'counter--payment': lambda: decorate((HERE / 'src_v43/counter--qr.html').read_text(), {}, 'Quầy · Thu tiền QR (điện thoại) · DH-2053', True),
  'counter--payment--received': lambda: pay_state('received', 'received', 'Quầy · Đã nhận (điện thoại) · DH-2053', sheet=True),
  'counter--payment--verified': lambda: pay_state('verified', 'verified', 'Quầy · Đã xác minh (điện thoại) · DH-2053', sheet=True),
}
for name, job in JOBS.items():
    html, missing = job()
    (OUT / f'{name}.html').write_text(strip_quiet_icons(html))
    print(name, 'MISSING ' + ','.join(missing) if missing else 'ok')

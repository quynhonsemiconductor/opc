# Builds the v4 Calm HOME states into apps/app/screens from the Calm home.html.
# Overlay states (more / assistant / notifications / command) keep their overlay markup from the v3.1 backup and sit
# on top of the new page. Content states (offline / loading / firstrun / simple) rewrite regions of the page.
# Usage: python3 home_states.py
import json, re, pathlib

HERE = pathlib.Path(__file__).parent
SCREENS = HERE.parents[3] / 'apps/app/screens'
OLD = HERE.parents[4] / 'design-backup-v3.1-2026-10-02/apps/app/screens'
SYS = HERE.parents[2]
ICONS = {**json.load(open(SYS / 'assets/icons/lucide-map.json')), **json.load(open(SYS / 'assets/icons/lucide-extra.json'))}
BASE = (SCREENS / 'home.html').read_text()
ic = lambda i: f'<svg class="c-ic" aria-hidden="true"><use href="#{i}"/></svg>'

def finish(s, title):
    s = re.sub(r'<svg width="0" height="0" style="position:absolute"[^>]*>[\s\S]*?</svg>', '<!--@icons-->', s, count=1)
    used = list(dict.fromkeys(re.findall(r'href="#(i-[\w-]+)"', s)))
    missing = [u for u in used if u not in ICONS]
    sprite = '<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">\n' + \
        '\n'.join(f'  <symbol id="{u}" viewBox="0 0 24 24">{ICONS[u]}</symbol>' for u in used if u in ICONS) + '\n</svg>'
    s = re.sub(r'<title>[^<]*</title>', f'<title>{title} — OPC</title>', s)
    return s.replace('<!--@icons-->', sprite), missing

def cut(s, start, end_tag, inner=False):
    """Return (a, b) indices of the element that begins at `start` and ends with the matching `end_tag`."""
    a = s.index(start); tag = re.match(r'<(\w+)', start).group(1)
    depth, i = 0, a
    for m in re.finditer(rf'<{tag}\b|</{tag}>', s[a:]):
        depth += 1 if not m.group(0).startswith('</') else -1
        if depth == 0: return a, a + m.end()
    raise ValueError(start)

def replace_el(s, start, new):
    a, b = cut(s, start, None); return s[:a] + new + s[b:]

def overlay(name, title, more_current=False, extra_style=''):
    old = (OLD / f'{name}.html').read_text()
    tab_end = old.index('</nav>', old.index('<nav class="c-tabbar"')) + len('</nav>')
    ov = old[tab_end:old.index('</body>')].strip()
    ov = ov.replace('<input type="text" role="combobox"', '<input class="c-command__field" type="text" role="combobox"')
    s = BASE.replace('</body>', ov + '\n</body>')
    if more_current:
        s = s.replace('<a class="c-tabbar__item" href="home.html" aria-current="page">', '<a class="c-tabbar__item" href="home.html">')
        s = s.replace('<a class="c-tabbar__item" href="home--more.html">', '<a class="c-tabbar__item" href="home--more.html" aria-current="page">')
    if extra_style: s = s.replace('</head>', f'<style>\n/* layout only */\n{extra_style}\n</style>\n</head>')
    return finish(s, title)

def offline():
    s = BASE
    s = s.replace('<div class="r-page-head">', f'''<div class="c-banner c-banner--err" role="alert"><span class="c-banner__pic">{ic("i-offline")}</span><span class="c-banner__text"><strong class="c-banner__title">Mất kết nối MB lúc 10:45</strong><span class="c-banner__body">Tiền QR mới sẽ hiện khi có lại kết nối. Vẫn bán được bằng tiền mặt — OPC thử lại mỗi phút.</span></span><span class="c-banner__actions"><button class="c-btn" type="button">Thử lại ngay</button></span></div>
      <div class="r-page-head">''', 1)
    s = s.replace('<span class="c-stat__fresh">MB · cập nhật 2 phút trước</span>', '<span class="c-stat__fresh c-stat__fresh--stale">số liệu đến 10:44 · đang chờ MB</span>')
    s = re.sub(r'<span class="c-health r-shell__desk"([^>]*)data-tip="[^"]*">.*?</span>',
               r'<span class="c-health c-health--err r-shell__desk"\1data-tip="MB (qua Casso) mất kết nối lúc 10:45 · Hoá đơn Hilo hoạt động · Đã lưu trên máy 10:45">MB mất kết nối · <b>10:45</b></span>', s, count=1)
    return finish(s, 'Tổng quan · Mất kết nối ngân hàng')

def loading():
    s = BASE
    sk = lambda kind, w=None, h=None: f'<span class="c-skel c-skel--{kind}"' + (f' style="--skel-w:{w}"' if w else '') + (f' style="--skel-h:{h}"' if h else '') + '></span>'
    s = s.replace('<span class="c-stat__fresh">MB · cập nhật 2 phút trước</span>', '<span class="c-skel-note" role="status">Đang tải… · số liệu trước đó 10:43</span>')
    a, b = cut(s, '<div class="c-stat__main">', None)
    bars = ''.join(f'<li class="c-bars__d" style="--v:{v}"><span class="c-bars__col"><span class="c-bars__bar c-skel"></span></span><span class="c-bars__k">{k}</span></li>'
                   for v, k in [(.87, 'T7'), (1, 'CN'), (.56, 'T2'), (.53, 'T3'), (.6, 'T4'), (.63, 'T5'), (.4, 'Hôm nay')])
    s = s[:a] + f'''<div class="c-stat__main" aria-busy="true">
            <div class="c-stat__skel">{sk("figure", "80%")}{sk("line", "55%")}{sk("line", "35%")}</div>
            <ol class="c-bars" aria-hidden="true">{bars}</ol>
          </div>''' + s[b:]
    a, b = cut(s, '<div class="c-split">', None)
    s = s[:a] + f'<div class="c-split" aria-hidden="true"><span class="c-skel c-skel--bar"></span><div class="c-split__skel">{sk("line", "70%")}{sk("line", "70%")}{sk("line", "70%")}</div></div>' + s[b:]
    a, b = cut(s, '<ol class="c-todo">', None)
    s = s[:a] + '<div class="c-todo__skel" aria-busy="true">' + '<span class="c-skel c-skel--block c-skel--row"></span>' * 3 + '</div>' + s[b:]
    s = s.replace('<span class="c-count" aria-label="6 việc">6</span>', '')
    a, b = cut(s, '<ul class="c-orders">', None)
    s = s[:a] + '<div class="c-orders__skel" aria-busy="true">' + (f'<div class="c-orders__skelrow">{sk("line", "40%")}{sk("line", "22%")}</div>' * 5) + '</div>' + s[b:]
    return finish(s, 'Tổng quan · Đang tải')

def firstrun():
    s = BASE
    s = s.replace('<h1 class="r-page-head__title">Hôm nay</h1>\n          <p class="c-sub">Thứ Sáu, 02/10/2026 · Ca sáng từ 07:00 · Phúc</p>',
                  '<h1 class="r-page-head__title">Chào chị Hai</h1>\n          <p class="c-sub">Còn 3 bước nữa là bán được hàng với OPC · khoảng 10 phút</p>')
    a, b = cut(s, '<div class="c-stat__main">', None)
    s = s[:a] + f'''<div class="c-stat__main c-stat__main--empty">
            <div><p class="c-stat__fig c-stat__fig--zero">0<span class="u-cur">₫</span></p>
              <p class="c-stat__delta">Chưa có đơn nào hôm nay — bán đơn đầu tiên ở Quầy sau khi thêm hàng.</p></div>
          </div>''' + s[b:]
    a, b = cut(s, '<div class="c-split">', None)
    s = s[:a] + f'''<div class="c-split c-split--legend-only">
            <p class="c-split__explain"><span class="c-split__k c-split__item--ok">Đã xác minh</span> ngân hàng đã khớp sao kê · <span class="c-split__k c-split__item--pend">Chờ xác minh</span> khách đã chuyển, đang đối chiếu · <span class="c-split__k c-split__item--cash">Tiền mặt</span></p>
          </div>''' + s[b:]
    s = s.replace('<span class="c-stat__fresh">MB · cập nhật 2 phút trước</span>', '<span class="c-off">MB chưa liên kết</span>')
    todo = f'''<section class="c-card r-home__todo" aria-labelledby="h-todo">
          <div class="c-card__head"><h2 class="c-card__title" id="h-todo">Thiết lập <span class="c-count" aria-label="còn 3 bước">1/4</span></h2><a class="c-link" href="onboard-help.html">Cần giúp?{ic("i-chev-r")}</a></div>
          <ol class="c-todo">
            <li class="c-todo__item c-todo__item--done"><span class="c-todo__n" aria-hidden="true">{ic("i-check")}</span>
              <div><h3 class="c-todo__t">Xác minh chủ hộ</h3><p class="c-todo__m">Xong 01/10/2026 · mức L1</p></div></li>
            <li class="c-todo__item c-todo__item--now"><span class="c-todo__n" aria-hidden="true">1</span>
              <div><h3 class="c-todo__t">Liên kết tài khoản MB</h3><p class="c-todo__m">để OPC biết khách đã chuyển và tự đối chiếu</p></div>
              <a class="c-btn c-btn--act c-todo__go" href="onboard-bank.html">Liên kết</a></li>
            <li class="c-todo__item"><span class="c-todo__n" aria-hidden="true">2</span>
              <div><h3 class="c-todo__t">Thêm hàng hoá</h3><p class="c-todo__m">chụp bảng giá, OPC đọc giúp</p></div>
              <a class="c-btn c-todo__go" href="onboard-products.html">Thêm món</a></li>
            <li class="c-todo__item"><span class="c-todo__n" aria-hidden="true">3</span>
              <div><h3 class="c-todo__t">Kết nối hoá đơn Hilo</h3><p class="c-todo__m">hoá đơn tự phát hành sau mỗi đơn</p></div>
              <a class="c-btn c-todo__go" href="onboard-invoice.html">Kết nối</a></li>
          </ol>
        </section>'''
    s = replace_el(s, '<section class="c-card r-home__todo"', todo)
    orders = f'''<section class="c-card r-home__orders" aria-labelledby="h-orders">
          <div class="c-card__head"><h2 class="c-card__title" id="h-orders">Đơn gần đây</h2></div>
          <div class="c-empty c-empty--flush"><span class="c-empty__pic">{ic("i-bag")}</span><strong class="c-empty__title">Chưa có đơn nào</strong><p class="c-empty__body">Đơn bán ở Quầy, Zalo hay Shopee sẽ hiện ở đây.</p></div>
        </section>'''
    s = replace_el(s, '<section class="c-card r-home__orders"', orders)
    side = f'''<section class="c-card r-home__side" aria-labelledby="h-tax">
          <div class="r-home__part">
            <div class="c-card__head"><h2 class="c-card__title" id="h-tax">Thuế &amp; ngưỡng 1 tỷ</h2><span class="c-off">Cổng thuế chưa bật</span></div>
            <p class="c-sub">Nhập doanh thu năm 2026 đến nay để OPC tính thuế quý và báo trước khi vượt ngưỡng.</p>
            <div class="c-card__acts"><a class="c-btn" href="#">Nhập doanh thu</a></div>
          </div>
        </section>'''
    s = replace_el(s, '<section class="c-card r-home__side"', side)
    s = re.sub(r'<span class="c-(?:nav|tabbar)__count"[^>]*>\d+</span>', '', s)
    s = s.replace('<span class="c-icon-btn__badge" aria-hidden="true">4</span>', '').replace('Thông báo — 4 chưa đọc', 'Thông báo')
    return finish(s, 'Tổng quan · Lần đầu')

def simple():
    s = BASE.replace('<html lang="vi">', '<html lang="vi" data-textsize="lg">').replace('<body>', '<body data-view="simple">')
    s = s.replace('<button class="c-icon-btn c-icon-btn--outline" type="button" aria-label="Thao tác khác', '<button class="c-icon-btn c-icon-btn--outline u-pro" type="button" aria-label="Thao tác khác')
    s = s.replace('<a class="c-stat__why"', '<a class="c-stat__why u-pro"')
    return finish(s, 'Tổng quan · Chế độ Gọn, chữ lớn')

ASSIST = '.fill { flex: 1 1 0; min-width: 0; }\n.stack { display: grid; gap: var(--space-2); }\n.composer { display: flex; align-items: center; gap: var(--space-2); width: 100%; }'
JOBS = {
  'home--more': lambda: overlay('home--more', 'Tổng quan · Thêm', more_current=True),
  'home--assistant': lambda: overlay('home--assistant', 'Tổng quan · Trợ lý', extra_style=ASSIST),
  'home--notifications': lambda: overlay('home--notifications', 'Tổng quan · Thông báo'),
  'home--command': lambda: overlay('home--command', 'Tổng quan · Tìm nhanh ⌘K'),
  'home--offline': offline, 'home--loading': loading, 'home--firstrun': firstrun, 'home--simple': simple,
}
for name, job in JOBS.items():
    html, missing = job()
    (SCREENS / f'{name}.html').write_text(html)
    print(name, 'MISSING ' + ','.join(missing) if missing else 'ok')

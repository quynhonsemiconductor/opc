"""v6.0.0 · Sẵn sàng by chain (replaces the flat 'Bắt buộc / Nên có / Đã xong' lists that lived in pages_setup.py).
  readiness--new   a household right after Mở hộ (01/07/2026): 9 việc bắt buộc still open
  readiness        the established household (06/10/2026): most done, X Invoice failing, quy tắc thuế waiting
Source: readiness_model.py.  Needs show first with the gate they unlock; everything else is folded but its names stay visible.  Usage: python3 pages_readiness.py"""
import re
from pages import build, ic, sign, subnav, annhien, SCREENS
from readiness_model import CHAINS, ITEMS, count

DONE = ('done', 'skip')
TONE = {('need', 'todo'): 'you', ('need', 'wait'): 'wait', ('need', 'err'): 'err'}
ST = {'wait': 'Chờ quyết định', 'err': 'Đang lỗi'}
ST_ID = {'rules': 'Chờ chị Lan'}


def sub(cur):
    return subnav('Cài đặt', [('Sẵn sàng', 'readiness.html'), ('Hộ & mô hình', 'setup-business.html'), ('Dữ liệu nền', 'setup-data.html'),
                              ('Vai trò & duyệt', 'setup-policy.html'), ('Tính năng', 'settings-features.html'), ('Hiển thị', 'settings-display.html')], cur)


def row(i, sk, quiet=False):
    state = i[sk]
    tone = 'ok' if state in DONE else TONE.get((i['tier'], state), 'wait' if state == 'wait' else 'err' if state == 'err' else 'nice')
    st = ST_ID.get(i['id'], '') if state == 'wait' and i['id'] in ST_ID else ST.get(state, '')
    m = i['meta'] + (f' · khoá: {i["gate"]}' if i['gate'] and state not in DONE else '')
    a = '<span class="u-meta">việc tiếp theo</span>' if quiet else (f'<a class="c-btn" href="{i["href"] or "#"}">{i["act"]}</a>' if i['act'] and state not in DONE else '')
    s = f'<span class="r-gate__st">{st}</span> · ' if st else ''
    return (f'<li class="r-gate__i r-gate__i--{tone}"><span class="r-gate__b"><b>{i["name"]}</b><small>{s}{m}</small></span><span class="r-gate__amt"></span><span class="r-gate__act">{a}</span></li>')


def fold(title, items, sk):
    if not items:
        return ''
    names = ', '.join(i['name'] for i in items[:2]) + ('…' if len(items) > 2 else '')
    return (f'<details class="r-feat__more"><summary>{title} · {len(items)} <span class="u-meta">{names}</span></summary><ul class="r-gate">'
            + ''.join(row(i, sk) for i in items) + '</ul></details>')


def chain(key, title, sk):
    its = [i for i in ITEMS if i['chain'] == key]
    need = [i for i in its if i['tier'] == 'need' and i[sk] not in DONE]
    opt = [i for i in its if i['tier'] == 'optional' and i[sk] not in DONE]
    done = [i for i in its if i[sk] in DONE]
    meta = f'{len(need)} bắt buộc còn lại · {len(opt)} tuỳ chọn · {len(done)} xong'
    nxt = next((i for i in ITEMS if i['tier'] == 'need' and i[sk] == 'todo' and i['act']), None)
    body = ('<ul class="r-gate">' + ''.join(row(i, sk, quiet=(i is nxt)) for i in need) + '</ul>') if need else '<p class="c-sub">Đủ việc bắt buộc.</p>'
    if opt:
        body += ('<div class="r-ready__opt"><h3 class="r-ready__h">Tuỳ chọn · bỏ qua được</h3><button class="c-btn c-btn--quiet" type="button" aria-haspopup="dialog">Bỏ qua cả nhóm…</button></div>'
                 '<ul class="r-gate">' + ''.join(row(i, sk) for i in opt) + '</ul>')
    return (f'<section class="c-card" aria-labelledby="c-{key}"><div class="c-card__head"><h2 class="c-card__title" id="c-{key}">{title}</h2><span class="u-meta">{meta}</span></div>'
            + body + fold('Đã xong hoặc bỏ qua', done, sk) + '</section>')


def head(title, state, subline, primary):
    return (f'<div class="r-page-head"><div><h1 class="r-page-head__title">{title} {state}</h1><p class="c-sub">{subline}</p></div><div class="r-page-head__acts">{primary}</div></div>')


def page(name, sk, state, subline, primary, aside_extra):
    nxt = next((i for i in ITEMS if i['tier'] == 'need' and i[sk] == 'todo' and i['act']), None)
    hero = (f'<section class="c-card r-ready__next" aria-labelledby="nx"><div><p class="u-meta">Việc tiếp theo</p><h2 class="c-card__title" id="nx">{nxt["name"]}</h2><p class="c-sub">mở khoá: {nxt["gate"]}</p></div>'
            f'<a class="c-btn c-btn--act" href="{nxt["href"] or "#"}">{nxt["act"]}</a></section>') if nxt else ''
    tot = count(sk, 'need', open_only=False); done = tot - count(sk, 'need')   # v7.5.1: progress of mandatory items
    hero = (f'<div class="c-meter"><div class="c-meter__row"><span class="u-meta">Việc bắt buộc đã xong · <b>{done}/{tot}</b></span></div>'
            f'<div class="c-meter__bar" role="img" aria-label="Đã xong {done} trên {tot} việc bắt buộc"><span class="c-meter__fill" style="width:{round(100 * done / tot)}%"></span></div></div>') + hero
    main = (f'\n      {sub("Sẵn sàng")}\n      ' + head('Sẵn sàng', state, subline, '' if nxt else primary)
            + '<div class="page"><div class="r-detail__grid r-detail--calm"><div class="stack">' + hero + ''.join(chain(k, t, sk) for k, t in CHAINS) + '</div>'
            '<aside class="r-tower__detail" aria-labelledby="pl"><h2 class="r-tower__t" id="pl">Danh sách này từ đâu</h2>'
            f'<p class="c-sub">Theo cách bán và nghĩa vụ của hộ · {len(ITEMS)} việc</p><p><a class="c-btn c-btn--quiet" href="setup-business.html">Đổi cách bán</a></p>' + aside_extra + '</aside></div></div>')
    build(name, 'Cài đặt · Sẵn sàng' + (' (hộ mới)' if sk == 'new' else ''), main, 'settings')
    p = SCREENS / f'{name}.html'
    annhien(p)
    s = p.read_text().replace('class="c-nav__item" href="settings-users.html"', 'class="c-nav__item" href="readiness.html"').replace('class="c-nav__item" href="invoices.html"', 'class="c-nav__item" href="period.html"')
    if sk == 'new':
        s = s.replace('Nguyễn Minh Khoa · Người vận hành', 'Phạm Thị An · Chủ hộ').replace('<span class="c-avatar__face" aria-hidden="true">K', '<span class="c-avatar__face" aria-hidden="true">A')
        s = re.sub(r'<span class="c-(nav|tabbar)__count" aria-label="3 (việc cần xem|cần xem)">3</span>', '', s)
        for a, b in [('aria-label="3 việc cần chị: 2 cần quyết, 1 lỗi">3<', f'aria-label="{count("new", "need")} việc cần làm">{count("new", "need")}<'), ('aria-label="3 việc cần làm">3<', f'aria-label="{count("new", "need")} việc cần làm">{count("new", "need")}<')]:
            s = s.replace(a, b)
    p.write_text(s)
    print(name, 'ok')


n_need_new = count('new', 'need')
page('readiness--new', 'new', sign('pend', 'i-clock', 'Đang thiết lập'), f'Còn {n_need_new} việc bắt buộc · việc tuỳ chọn bỏ qua được',
     f'<a class="c-btn c-btn--act" href="stock-count.html">{ic("i-scale")}Bắt đầu: đếm tồn đầu kỳ</a>',
     '<h2 class="r-tower__t r-rail__h2">Nhân viên OPC hỗ trợ</h2><p class="c-sub">Chị Thu hẹn Thứ Năm 02/07, 8:00 · đếm tồn, thêm khách</p>'
     f'<p><a class="c-btn c-btn--quiet" href="onboard-assisted.html">{ic("i-help")}Mở chế độ hỗ trợ</a></p>')
n_need_est = count('est', 'need')
page('readiness', 'est', sign('pend', 'i-clock', 'Sẵn sàng có điều kiện'), f'Đủ để vận hành · còn {n_need_est} việc bắt buộc chờ hoặc lỗi',
     f'<a class="c-btn c-btn--act" href="connections--category.html">{ic("i-link")}Chọn cách nối</a>',
     '<h2 class="r-tower__t r-rail__h2">Nhân viên OPC hỗ trợ</h2><p class="c-sub">Nhân viên thấy cùng danh sách và làm giúp, mọi thao tác ghi tên.</p>'
     f'<p><a class="c-btn c-btn--quiet" href="onboard-assisted.html">{ic("i-help")}Mở chế độ hỗ trợ</a></p>')

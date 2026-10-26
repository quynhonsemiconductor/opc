"""Shared helpers for the connections screens (v4.9.0). pages_connect3.py uses these; pages_connect / pages_connect2 keep their own copies."""
from pages import build, ic, sign, SCREENS, annhien

OWNER = ('Nguyễn Minh Khoa · Người vận hành', 'Phạm Thị An · Chủ hộ')


SHOWN = {'Theo nhóm việc': 'Việc OPC làm'}


def tabs(sel, n=6):
    t = [('Đã nối', 'connections.html', f' <span class="c-tabs__count">{n}</span>'), ('Theo nhóm việc', 'connections--category.html', ''),
         ('Nhật ký', 'connections--log.html', '')]
    return ('<div class="c-tabs" role="tablist" aria-label="Kết nối">' + ''.join(
        f'<a class="c-tabs__tab" role="tab" aria-selected="{"true" if k == sel else "false"}" href="{h}">{SHOWN.get(k, k)}{c}</a>' for k, h, c in t) + '</div>')


def head(title, sub, acts=''):
    return (f'<div class="r-page-head"><div><h1 class="r-page-head__title">{title}</h1><p class="c-sub">{sub}</p></div>'
            f'<div class="r-page-head__acts">{acts}</div></div>')


def dhead(title, state, sub, acts=''):
    return (f'<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">{title} {state}</h1>'
            f'<p class="r-detail__fig"><span class="c-sub">{sub}</span></p></div><div class="r-detail__acts">{acts}</div></div>')


def crumb(*parts):
    links = ''.join(f'<a href="{h}">{t}</a>' for t, h in parts[:-1])
    return f'<nav class="c-crumbs" aria-label="Đường dẫn">{links}<span aria-current="page">{parts[-1]}</span></nav>'


def grid(left, right=''):
    return f'<div class="r-detail__grid r-detail--calm"><div class="stack">{left}</div>{right}</div>'


def card(tid, title, inner, aside=''):
    return (f'<section class="c-card" aria-labelledby="{tid}"><div class="c-card__head"><h2 class="c-card__title" id="{tid}">{title}</h2>{aside}</div>{inner}</section>')


def row(tone, st, t, m, act=''):
    s = f'<span class="r-gate__st">{st}</span>' + (' · ' if m else '') if st else ''
    return (f'<li class="r-gate__i r-gate__i--{tone}"><span class="r-gate__b"><b>{t}</b><small>{s}{m}</small></span>'
            f'<span class="r-gate__amt"></span><span class="r-gate__act">{act}</span></li>')


def save(name, title, main, owner=True, overlay=''):
    build(name, title, '\n      ' + main, 'connections', overlay=overlay)
    p = SCREENS / f'{name}.html'
    annhien(p)
    s = p.read_text()
    if owner:
        s = s.replace(OWNER[0], OWNER[1]).replace('<span class="c-avatar__face" aria-hidden="true">K', '<span class="c-avatar__face" aria-hidden="true">A')
    p.write_text(s)


def chips(label, items, sel=0):
    return (f'<div class="c-filters" role="group" aria-label="{label}">' + ''.join(
        f'<button class="c-filter" type="button" aria-pressed="{"true" if i == sel else "false"}">{t}</button>' for i, t in enumerate(items)) + '</div>')

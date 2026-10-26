"""v7 · shared helpers for ERP record screens (Mua, Bán): one record = sections + independent tracks + Diễn biến."""
from pages import build, ic, sign, annhien, SCREENS

CUR = '<span class="u-cur">₫</span>'
who = lambda n, m: f'<td class="c-table__cell--main c-table__who"><b>{n}</b><small>{m}</small></td>'
num = lambda v: f'<td class="c-table__num">{v}</td>'
cell = lambda v, c='': f'<td{" class=" + chr(34) + c + chr(34) if c else ""}>{v}</td>'


def save(name, title, main, overlay='', sec='goods'):
    build(name, title, '\n      ' + main, sec, overlay=overlay)
    annhien(SCREENS / f'{name}.html')


def head(title, sub, acts=''):
    return (f'<div class="r-page-head"><div><h1 class="r-page-head__title">{title}</h1><p class="c-sub">{sub}</p></div>'
            f'<div class="r-page-head__acts">{acts}</div></div>')


def card(i, title, body, acts='', meta=''):
    m = f'<span class="c-sub">{meta}</span>' if meta else ''
    return (f'<section class="c-card" aria-labelledby="{i}"><div class="c-card__head"><h2 class="c-card__title" id="{i}">{title}</h2>{m}'
            f'{f"<div class=c-card__acts>{acts}</div>" if acts else ""}</div>{body}</section>')


def lines(rows, total, label='Hàng mua', price='Giá mua'):
    tr = ''.join(f'<tr><td class="c-table__cell--main">{n}</td><td class="c-table__num">{q}</td><td class="c-table__num">{p}</td><td class="c-table__num">{t}</td></tr>' for n, q, p, t in rows)
    return ('<div class="c-table__scroll" tabindex="0" role="region" aria-label="{label}"><table class="c-table r-lines"><thead><tr><th scope="col">Món</th><th scope="col" class="c-table__num">Số lượng</th>'
            f'<th scope="col" class="c-table__num">{price}</th><th scope="col" class="c-table__num">Thành tiền</th></tr></thead>'
            f'<tbody>{tr}</tbody><tfoot><tr><td class="c-table__cell--main">Tổng</td><td></td><td></td><td class="c-table__num"><b>{total}</b></td></tr></tfoot></table></div>')


def tl(items):
    li = ''.join(f'<li class="c-timeline__item c-timeline__item--{k}"><span class="c-timeline__time">{t}</span><span class="c-timeline__dot" aria-hidden="true"></span>'
                 f'<span class="c-timeline__body"><span class="c-timeline__what">{w}</span><span class="c-timeline__who">{b}</span></span></li>' for t, k, w, b in items)
    return f'<ol class="c-timeline">{li}</ol>'


def tracks(*t):
    return '<ul class="r-tracks" aria-label="Tình trạng">' + ''.join(f'<li class="r-tracks__t r-tracks__t--{k}"><span>{n}</span><b>{v}</b></li>' for n, k, v in t) + '</ul>'


def jump(target, label='Xem diễn biến'):
    """Phone only: the side panel stacks below the actions, so offer a jump to it right under the header (v7.5.1)."""
    return f'<a class="r-jump7" href="#{target}">{label}{ic("i-chev")}</a>'


def record(code, sup, sub, trk, body, side, acts='', crumb=('Đơn mua', 'purchases.html')):
    return (f'<div class="page"><nav class="c-crumbs" aria-label="Đường dẫn"><a href="{crumb[1]}">{crumb[0]}</a>'
            f'<span aria-current="page">{code}</span></nav>'
            f'<div class="r-detail__head r-detail__head--calm"><div><h1 class="r-detail__title">{code} · {sup}</h1>'
            f'<p class="r-detail__fig"><span class="c-sub">{sub}</span></p></div><div class="r-page-head__acts">{acts}</div></div>'
            + trk + jump('hx') + f'<div class="r-detail__grid r-detail--calm"><div class="stack">{body}</div>'
            f'<aside class="r-tower__detail" aria-labelledby="hx"><h2 class="r-tower__t" id="hx">Diễn biến</h2>{side}</aside></div></div>')


def rline(name, got, ordered, unit, note, short=False):
    cls = 'r-pick__chk' + ('' if short else ' r-pick__chk--ok')
    return (f'<li class="r-pick__l"><span class="{cls}" aria-hidden="true">{"" if short else ic("i-check")}</span>'
            f'<span class="r-pick__name"><b>{name}</b><small{" class=r-recv__short" if short else ""}>{note}</small></span>'
            f'<label class="r-qty"><span class="u-sr">Số thực nhận {name}</span><span class="c-field__control"><input class="c-field__input" inputmode="numeric" value="{got}" aria-describedby="q-{ordered}-{got}"></span></label>'
            f'<span class="r-pick__qty{" r-pick__qty--short" if short else ""}" id="q-{ordered}-{got}">/{ordered} {unit}</span></li>')



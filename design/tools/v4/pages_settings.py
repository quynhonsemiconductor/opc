# v4.1 · Cài đặt group: settings-display, -features, -users, -users--otp. Usage: python3 pages_settings.py
# Settings pattern = grouped list (iOS Settings): flat grouped surfaces, label left, control right, and every switch
# says its state in words (Bật / Tắt / Bắt buộc / Sắp có) — never the track alone.
import re, pathlib
from pages import build, ic

SRC = pathlib.Path(__file__).parent / 'src_v40'

def parts(name):
    src = SRC.parent / 'src_v43' / f'{name}.html'   # v4.3 An Nhiên (settings43.py)
    s = (src if src.exists() else SRC / f'{name}.html').read_text()
    style = re.search(r'<style>([\s\S]*?)</style>', s); style = style.group(1).replace('/* layout only */', '') if style else ''
    mo = re.search(r'<main class="r-shell__content"[^>]*>', s); main = s[mo.end():s.index('</main>')]
    after = s[s.index('</nav>', s.index('<nav class="c-tabbar"')) + len('</nav>'):s.index('</body>')].strip()
    title = re.search(r'<title>(.*?) — OPC</title>', s).group(1)
    return main, after, style, title

def switch(m):
    btn = m.group(0)
    on = 'aria-checked="true"' in btn
    locked = ' disabled' in btn or 'aria-disabled="true"' in btn
    label = re.search(r'<span class="c-switch__label">(.*?)<span class="c-switch__sub">(.*?)</span></span>', btn, re.S)
    if not label: return btn
    name, sub = label.group(1), label.group(2)
    soon = sub.startswith('Sắp có')
    sub = re.sub(r'^(Bật|Sắp có)\s*·\s*', '', sub)
    sub = re.sub(r'\s*Đang (tắt|bật)\.\s*$', '', sub)
    if locked and on: state, kind = 'Bắt buộc', 'lock'
    elif soon: state, kind = 'Sắp có', 'soon'
    else: state, kind = ('Bật', 'on') if on else ('Tắt', 'off')
    if locked and on: sub = re.sub(r'^bắt buộc,\s*', '', sub)
    sub = sub[:1].upper() + sub[1:]
    pic = ic('i-lock') if kind == 'lock' else ''
    head = btn[:btn.index('>') + 1].replace('class="c-switch"', 'class="c-switch c-switch--row"')
    return (f'{head}<span class="c-switch__label">{name}<span class="c-switch__sub">{sub}</span></span>'
            f'<span class="c-switch__state c-switch__state--{kind}">{pic}{state}</span>'
            f'<span class="c-switch__track" aria-hidden="true"></span></button>')

def calm(main):
    main = main.replace('<p class="r-page-head__sub u-meta">', '<p class="c-sub">')
    main = re.sub(r'<button class="c-switch" type="button" role="switch".*?</button>', switch, main, flags=re.S)
    main = main.replace('<div class="page">', '<div class="page r-settings">', 1)
    return main

# display — split the two switches into two rows
main, after, style, title = parts('settings-display')
main = calm(main)
main = re.sub(r'(<li class="c-list__row">)(<button class="c-switch c-switch--row".*?</button>)\s*(<button class="c-switch c-switch--row".*?</button>)(</li>)',
              r'\1\2\4\n            \1\3\4', main, count=1, flags=re.S)
build('settings-display', title, main, 'settings', overlay=after, style=style)

# features — the explainer becomes the subline (say it once)
main, after, style, title = parts('settings-features')
main = calm(main)
say = re.search(r'\s*<p class="c-say">(Bật thêm khi chị cần[^<]*)</p>', main)
if say:
    main = main.replace(say.group(0), '')
    main = main.replace('<p class="c-sub">3 đang bật · 3 đang tắt</p>', f'<p class="c-sub">3 đang bật · 3 đang tắt · {say.group(1)}</p>')
# v4.1 polish: group by state — what is on now, then what is coming; the subline counts both
_m = re.search(r'<section class="c-card" aria-label="Danh sách tính năng">\s*<ul class="c-list">(.*?)</ul>\s*</section>', main, flags=re.S)
if _m:
    _rows = re.findall(r'<li class="c-list__row">.*?</li>', _m.group(1), flags=re.S)
    _on = [r for r in _rows if 'c-switch__state--soon' not in r]
    _soon = [r for r in _rows if 'c-switch__state--soon' in r]
    _sec = lambda i, h, rs: (f'<section class="c-card" aria-labelledby="{i}"><div class="c-card__head"><h2 class="c-card__title" id="{i}">{h}</h2></div>'
                             f'<ul class="c-list">' + ''.join(rs) + '</ul></section>')
    main = main.replace(_m.group(0), _sec('f-on', f'Đang dùng · {len(_on)}', _on) + '\n        ' + _sec('f-soon', f'Sắp có · {len(_soon)}', _soon))
    main = main.replace('3 đang bật · 3 đang tắt', f'{len(_on)} đang dùng · {len(_soon)} sắp có')
build('settings-features', title, main, 'settings', overlay=after, style=style)

for n in ('settings-users', 'settings-users--otp'):
    main, after, style, title = parts(n)
    build(n, title, calm(main), 'settings', overlay=after, style=style)

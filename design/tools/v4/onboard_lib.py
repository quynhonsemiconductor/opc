"""v6.0.0 · shared helpers for the generated onboarding screens (template = the generated onboard-model.html).
v7.0.0: six steps, every mandatory item of a hộ kinh doanh (system/E2E-SCOPE.md, _research/mandatory-2026.md). Single source of STEPS for onboard43 / onboard_aside / onboard_flow."""
import re, pathlib
from pages import ICONS
HERE = pathlib.Path(__file__).parent
SCREENS = HERE.parents[1] / 'apps/app/screens'
STEPS = ['Số điện thoại', 'Hộ kinh doanh', 'Cách bán', 'Thuế và tài khoản', 'Hoá đơn', 'Hàng và số đầu kỳ']
# (time, why) for the step map
ABOUT = [('1 phút', 'Đăng nhập bằng mã 6 số, rồi chị đồng ý cách OPC dùng dữ liệu.'),
         ('2 phút', 'Chụp giấy đăng ký hộ kinh doanh, OPC đọc giúp. Chưa có giấy thì OPC hướng dẫn đăng ký.'),
         ('2 phút', 'Chị bán thế nào, có thuê người, có bán thực phẩm không — để biết hộ cần làm những gì.'),
         ('3 phút', 'VNeID, eTax, cách khai thuế và tài khoản ngân hàng dùng kinh doanh.'),
         ('3 phút', 'Hoá đơn điện tử: chọn cách xuất và chữ ký số, đăng ký với cơ quan thuế.'),
         ('5 phút', 'Thêm hàng và giá, rồi điền tồn đã đếm, tiền và công nợ lúc bắt đầu.')]
STEP_OF = {'onboard-phone': 1, 'onboard-otp': 1, 'onboard-otp--wrong': 1, 'onboard-consent': 1,
           'onboard-household': 2, 'onboard-household--read': 2, 'onboard-household--notfound': 2, 'onboard-household--unregistered': 2,
           'onboard-model': 3, 'onboard-features': 3, 'onboard-feature': 3,
           'onboard-gov': 4, 'onboard-tax': 4, 'onboard-bankacc': 4,
           'onboard-invoice': 5, 'onboard-invoice--register': 5,
           'onboard-products': 6, 'onboard-products--review': 6, 'onboard-products--unreadable': 6, 'onboard-help': 6, 'onboard-opening': 6, 'onboard-opening--empty': 6}
ic = lambda i: f'<svg class="c-ic" aria-hidden="true"><use href="#{i}"/></svg>'


def bar(n, label=''):
    segs = ''.join(f'<li class="c-steps__seg {"c-steps__seg--done" if i < n else "c-steps__seg--now" if i == n else ""}"></li>' for i in range(1, len(STEPS) + 1))
    return (f'<div class="c-steps" role="img" aria-label="Bước {n} trên {len(STEPS)}: {label or STEPS[n - 1]}"><span class="c-steps__label"><b>Bước {n}/{len(STEPS)}</b> · {label or STEPS[n - 1]}</span>'
            f'<ol class="c-steps__bar">{segs}</ol></div>')


def sprite(s):
    used = sorted(set(re.findall(r'href="#(i-[a-z0-9-]+)"', s)))
    sp = ('<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">\n' + '\n'.join(f'  <symbol id="{u}" viewBox="0 0 24 24">{ICONS[u]}</symbol>' for u in used if u in ICONS) + '\n</svg>')
    return re.sub(r'<svg width="0" height="0" style="position:absolute"[^>]*>[\s\S]*?</svg>', lambda m: sp, s, count=1)


def shell(name, title, back, main, foot, n, label=''):
    s = (SCREENS / 'onboard-model.html').read_text()
    s = re.sub(r'<div class="c-steps" role="img".*?</ol></div>', lambda m: bar(n, label), s, count=1, flags=re.S)
    s = re.sub(r'href="[^"]*" aria-label="Quay lại bước trước"', f'href="{back}" aria-label="Quay lại bước trước"', s, count=1)
    s = re.sub(r'<main class="r-onboard__body">[\s\S]*?</main>', lambda m: main, s, count=1)
    s = re.sub(r'<footer class="r-onboard__foot">[\s\S]*?</footer>', lambda m: foot, s, count=1)
    s = re.sub(r'<title>[^<]*</title>', f'<title>{title} — OPC</title>', s)
    (SCREENS / f'{name}.html').write_text(sprite(s))
    print(name, 'ok')


def foot(primary, alt=''):
    return f'<footer class="r-onboard__foot">\n    {primary}\n' + (f'    <div class="r-onboard__alt">{alt}</div>\n' if alt else '') + '  </footer>'


def btn(label, href, arrow=True):
    return f'<a class="c-btn c-btn--act c-btn--block" href="{href}">{label}' + (ic('i-arrow') if arrow else '') + '</a>'


def field(fid, label, value='', hint='', bad=False, mode='text', suffix='', ph=''):
    suf = f'<span class="c-field__suffix">{suffix}</span>' if suffix else ''
    return (f'<div class="c-field"{" data-invalid" if bad else ""}><label class="c-field__label" for="{fid}">{label}</label><div class="c-field__control">'
            f'<input class="c-field__input" id="{fid}" inputmode="{mode}" value="{value}" placeholder="{ph}"{" aria-invalid=\"true\"" if bad else ""}>{suf}</div>'
            + (f'<span class="c-field__hint">{hint}</span>' if hint else '') + '</div>')


def opt(on, title, meta, plan='', kind='radio'):
    pl = f'<span class="r-model__plan">{plan}</span>' if plan else ''
    mark = (f'<span class="c-option__box" aria-hidden="true">{ic("i-check") if on else ""}</span>' if kind == 'checkbox'
            else '<span class="c-option__radio" aria-hidden="true"></span>')
    on_cls = ' c-option--on' if (on and kind == 'checkbox') else ''
    return (f'<button class="c-option c-option--big{on_cls}" type="button" role="{kind}" aria-checked="{"true" if on else "false"}">{mark}'
            f'<span class="c-option__body"><strong class="c-option__title">{title}</strong>' + (f'<span class="c-option__meta">{meta}</span>' if meta else '') + f'{pl}</span></button>')

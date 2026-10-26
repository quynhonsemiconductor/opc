"""v6.0.0 · Onboarding step 3 (second screen) "Việc OPC làm" (features first, providers are the choices).
  onboard-features   the plan: what OPC does for this household, grouped Cần để bắt đầu / Nên có / Khi cần; a way is pre-chosen (OPC gợi ý), "Đổi" opens the chooser
  onboard-feature    choose a way for one feature (Nhận tiền chuyển khoản): selectable providers, "Nhờ nhân viên OPC nối giúp", "Sắp có" folded
Runs after onboard43.py (needs onboard-model.html as the template) and before onboard_aside.py. Back link of onboard-features = the model screen.  Usage: python3 onboard_features.py"""
from onboard_lib import shell as _shell, ic
from capabilities import FEATS, FBY, TIERS, BY, selectable
NAME = lambda pid: BY[pid]['name'].replace(' qua Casso', '')   # onboarding names the way, not the hub behind it


def shell(name, title, back, main, foot, n=3, label='Việc OPC làm'):
    _shell(name, title, back, main, foot, n, label)


# ------------------------------------------------------------------ the plan
def way(f):
    return f'<span class="r-feat__way">OPC chọn sẵn: {NAME(f["rec"])}</span>'


def need_row(f):
    return (f'<li class="r-feat__i"><span class="r-feat__b"><b>{f["name"]}</b><small>{f["why"]}</small></span>'
            f'{way(f)}<span class="r-feat__act"><a class="c-btn" href="onboard-feature.html">Đổi bên hoá đơn</a></span></li>')


def soft(key, title, note):
    fs = [f for f in FEATS if f['tier'] == key]
    rows = ''.join(f'<li class="r-feat__i r-feat__i--soft"><span class="r-feat__b"><b>{f["name"]}</b><small>{f["what"]}</small></span>'
                   f'<span class="r-feat__way">{note(f)}</span><span class="r-feat__act"></span></li>' for f in fs)
    if key == 'optional':
        names = ', '.join(f['name'].lower() if i else f['name'] for i, f in enumerate(fs[:3])) + '…'
        return f'<details class="r-feat__more"><summary><span>{title} · {len(fs)} <span class="u-meta">{names}</span></span><span class="r-feat__open">Xem {len(fs)} việc{ic('i-chev')}</span></summary><ul class="r-feat">{rows}</ul></details>'
    return f'<section aria-labelledby="ft-{key}"><h2 class="c-card__title" id="ft-{key}">{title} · {len(fs)}</h2><ul class="r-feat">{rows}</ul></section>'


NEED = [f for f in FEATS if f['tier'] == 'need']
MAIN = ('<main class="r-onboard__body">\n    <h1 class="r-onboard__title">Việc OPC làm cho chị</h1>\n'
        '    <p class="c-say">Chỉ hoá đơn điện tử cần nối ngay. Việc tuỳ chọn chị bỏ qua được, làm tay vẫn đủ.</p>\n'
        f'    <section aria-labelledby="ft-n"><h2 class="c-card__title" id="ft-n">Cần nối · {len(NEED)}</h2><ul class="r-feat">' + ''.join(need_row(f) for f in NEED) + '</ul></section>\n'
        '    ' + soft('opc', 'OPC lo sẵn', lambda f: 'không cần nối') + '\n'
        '    ' + soft('optional', 'Tuỳ chọn · bỏ qua được', lambda f: 'Làm tay: ' + (f['manual'] or 'có sẵn')) + '\n'
        '    <p class="r-onboard__saved">Đã lưu — làm tiếp lúc nào cũng được</p>\n  </main>')
FOOT = (f'<footer class="r-onboard__foot">\n'
        f'    <a class="c-btn c-btn--act c-btn--block" href="onboard-gov.html">Tiếp tục{ic("i-arrow")}</a>\n'
        '    <div class="r-onboard__alt"><a href="onboard-help.html">Nhờ nhân viên OPC nối giúp</a></div>\n  </footer>')
shell('onboard-features', 'Đăng ký · Việc OPC làm', 'onboard-model.html', MAIN, FOOT)


# ------------------------------------------------------------------ choose a way for one feature
def opt(on, title, meta, plan=''):
    pl = f'<span class="r-model__plan">{plan}</span>' if plan else ''
    return (f'<button class="c-option c-option--big" type="button" role="radio" aria-checked="{"true" if on else "false"}"><span class="c-option__radio" aria-hidden="true"></span>'
            f'<span class="c-option__body"><strong class="c-option__title">{title}</strong><span class="c-option__meta">{meta}</span>{pl}</span></button>')


META = {'hilo': 'hoá đơn máy tính tiền cho khách tại chỗ · có mã ngay', 'xinvoice': 'hoá đơn có mã cho khách sỉ', 'sinvoice': 'hoá đơn của Viettel'}


def chooser(f):
    sel = [p for p in f['choices'] if selectable(p)]
    soon = [p for p in f['choices'] if not selectable(p)]
    opts = ''.join(opt(p == f['rec'], NAME(p), META.get(p, ''), 'OPC gợi ý' if p == f['rec'] else '') for p in sel)
    opts += opt(False, 'Nhờ nhân viên OPC nối giúp', 'chị Thu hẹn giờ, làm cùng chị')
    pills = ''.join(f'<li><button class="r-dir__pill" type="button" aria-label="Báo tôi khi có {NAME(p)}">{NAME(p)}</button></li>' for p in soon[:4])
    return (f'<div class="c-options" role="radiogroup" aria-label="{f["name"]}">{opts}</div>'
            f'<div class="r-dir__soon"><p class="u-meta">Sắp có {len(soon)} cách · bấm để OPC báo</p><ul class="r-dir__pills">{pills}</ul></div>'
            f'<p class="c-sub">Việc này cần một cách nối để bắt đầu. Chưa nối: {f["lock"]}.</p>')


F = FBY['invoice']
MAIN2 = ('<main class="r-onboard__body">\n    <h1 class="r-onboard__title">Chị xuất hoá đơn qua nhà cung cấp nào?</h1>\n'
         f'    <p class="c-say">{F["what"]}.</p>\n    ' + chooser(F) + '\n    <p class="r-onboard__saved">Đã lưu — làm tiếp lúc nào cũng được</p>\n  </main>')
FOOT2 = (f'<footer class="r-onboard__foot">\n    <a class="c-btn c-btn--act c-btn--block" href="onboard-features.html">Dùng cách này</a>\n'
         '    <div class="r-onboard__alt"><a href="onboard-help.html">Chưa chắc — nhờ nhân viên OPC hỏi giúp</a></div>\n  </footer>')
shell('onboard-feature', 'Đăng ký · Chọn nhà cung cấp hoá đơn', 'onboard-features.html', MAIN2, FOOT2)

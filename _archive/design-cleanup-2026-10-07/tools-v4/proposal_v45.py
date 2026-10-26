"""v4.5 proposal · type budget (references/budgets.md §5) — one scale, three weights, wrap-safe line-height.

  sizes   14 · 16 · 18 · 24 · 32 · 44   (was 14·15·16·17·18·19·20·22·24·28·34·44 — five sizes within ×1.12)
          meta/note 14 · body/control 16 · lead/amount-s/h3 18 · amount/h2 24 · amount-l/h1 32 · total 44
  weights 400 text · 600 titles, labels, controls · 700 figures   (was 400·500·600·650·700·750·800·900)
  line-h  multi-line titles/labels ≥ 1.35 (Vietnamese stacked diacritics)

Usage:
  python3 proposal_v45.py            → sandbox copy in design/_proposal-v45/ (real files untouched)
  python3 proposal_v45.py --apply    → transform the real system/app CSS in place (only after the owner approves)
"""
import re, shutil, sys, pathlib

D = pathlib.Path(__file__).resolve().parents[2]          # …/opc/design
CSS = ['system/tokens.css', 'system/components/components.css', 'system/components/recipes.css', 'apps/app/app-tokens.css']

TOKENS = {'--fs-note': 'var(--p-size-14)', '--fs-control': 'var(--p-size-16)', '--fs-amount-s': 'var(--p-size-18)', '--fs-h3': 'var(--p-size-18)',
          '--fs-amount': 'var(--p-size-24)', '--fs-amount-l': 'var(--p-size-32)', '--fs-h1': 'var(--p-size-32)'}
TEXTSIZE = {
    'lg': '--fs-meta: 16px; --fs-note: 16px; --fs-body: 18px; --fs-control: 18px; --fs-lead: 21px; --fs-amount-s: 21px; --fs-h3: 21px; --fs-amount: 27px; --fs-h2: 27px;',
    'xl': '--fs-meta: 18px; --fs-note: 18px; --fs-body: 20px; --fs-control: 20px; --fs-lead: 23px; --fs-amount-s: 23px; --fs-h3: 23px; --fs-amount: 29px; --fs-h2: 29px; --target: 56px;'}
TITLE = re.compile(r'title|__t\b|__h\b|head|label|__k\b|btn|tab|chip|seg|kbd|th\b|nav__item--here', re.I)
CTRL600 = re.compile(r'c-btn--wrap|c-btn--xl|chip__k|c-kbd')
LH_FIX = ['.c-todo__t', '.c-banner__title', '.c-seg__opt']


def weight(sel, w):
    w = int(w)
    if w <= 400: return '400'
    if w == 500: return '600' if CTRL600.search(sel) else '400'
    if w == 600: return '600'
    if w == 650: return '600' if TITLE.search(sel) and 'money' not in sel and 'amt' not in sel else '700'
    return '700'


def transform(css, name):
    if name.endswith('tokens.css') and name.startswith('system'):
        css = css.replace('--p-size-34: 34px; --p-size-44: 44px;', '--p-size-32: 32px; --p-size-34: 34px; --p-size-44: 44px;')
        for k, v in TOKENS.items():
            css = re.sub(rf'({re.escape(k)}:\s*)[^;]+;', rf'\g<1>{v};', css, count=1)
        for t, body in TEXTSIZE.items():
            css = re.sub(rf'\[data-textsize="{t}"\] \{{[^}}]*\}}', f'[data-textsize="{t}"] {{ {body} }}', css, count=1)
        return css

    def rule(m):
        sel, body = m.group(1), m.group(2)
        body = re.sub(r'(font-weight:\s*)(\d{3})', lambda x: x.group(1) + weight(sel, x.group(2)), body)
        body = re.sub(r'(font:\s*)(\d{3})(\s)', lambda x: x.group(1) + weight(sel, x.group(2)) + x.group(3), body)
        body = re.sub(r'font-size:\s*13px', 'font-size: var(--fs-meta)', body)
        if any(s.strip().startswith(f) and s.strip() == f for s in sel.split(',') for f in LH_FIX):
            body = re.sub(r'(font:[^;/]*/)1\.(1\d|2\d|3)\b', r'\g<1>1.35', body)
            body = re.sub(r'(line-height:\s*)1\.(1\d|2\d)\b', r'\g<1>1.35', body)
        return sel + '{' + body + '}'
    css = re.sub(r'([^{}]+)\{([^{}]*)\}', rule, css)
    if name.endswith('components.css') and 'v4.5 type' not in css:
        css += '\n/* v4.5 type budget: nested bold never escalates (bolder → 900) */\nb, strong { font-weight: 700; }\n'
    return css


def main():
    apply = '--apply' in sys.argv
    out = D if apply else D / '_proposal-v45'
    if not apply:
        if out.exists(): shutil.rmtree(out)
        shutil.copytree(D / 'apps/app/screens', out / 'apps/app/screens')
        (out / 'system/components').mkdir(parents=True, exist_ok=True)
    for rel in CSS:
        src = (D / rel).read_text()
        (out / rel).write_text(transform(src, rel))
    print(('applied to real CSS' if apply else f'sandbox → {out}') + f' · {len(CSS)} stylesheets')


if __name__ == '__main__':
    main()

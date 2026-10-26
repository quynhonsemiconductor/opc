"""v4.1 clean-up: fold repeated top-level blocks of the same selector (v1 → v3 → v4 → v4.1 layers) into one.
Safe by construction:
  - a declaration overridden later by the same selector + same property is dropped (unless !important stops it);
  - a surviving earlier declaration moves into the LAST block only if no rule in between (any selector, any
    @media) and no later block of this selector touches the same property family (border-*, font-*, inset…);
    otherwise it stays where it is.
Only top-level style rules are folded; @media/@supports/@keyframes are left in place. Usage: python3 css_fold.py [--dry]"""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
FILES = [ROOT / 'system/components/components.css', ROOT / 'system/components/recipes.css']
INSET = {'top', 'right', 'bottom', 'left', 'inset'}


def family(p):
    p = p.strip().lower()
    if p.startswith('--'): return p
    if p in INSET or p.startswith('inset'): return 'inset'
    if p in ('gap', 'row-gap', 'column-gap', 'grid-gap'): return 'gap'
    return p.split('-')[0]


def blocks(css):
    """Top-level items: ('rule', start, end, prelude, body) or ('other', start, end). Comments/space = 'other'."""
    out, i, n = [], 0, len(css)
    while i < n:
        if css.startswith('/*', i):
            j = css.index('*/', i) + 2; out.append(('other', i, j)); i = j; continue
        if css[i].isspace():
            j = i
            while j < n and css[j].isspace(): j += 1
            out.append(('other', i, j)); i = j; continue
        j = css.index('{', i); depth, k = 1, j + 1
        while depth:
            if css.startswith('/*', k): k = css.index('*/', k) + 2; continue
            depth += {'{': 1, '}': -1}.get(css[k], 0); k += 1
        pre = css[i:j]
        out.append(('rule' if not pre.strip().startswith('@') else 'at', i, k, pre, css[j + 1:k - 1]))
        i = k
    return out


def decls(body):
    body = re.sub(r'/\*.*?\*/', '', body, flags=re.S)
    out = []
    for d in re.split(r';(?![^(]*\))', body):
        if ':' in d and d.strip():
            p, v = d.split(':', 1)
            out.append((p.strip(), v.strip()))
    return out


def families_in(text):
    fams = set()
    for b in re.findall(r'\{([^{}]*)\}', re.sub(r'/\*.*?\*/', '', text, flags=re.S)):
        for p, _ in decls(b): fams.add(family(p))
    return fams


def fold(css, stats):
    items = blocks(css)
    by_sel = {}
    for idx, it in enumerate(items):
        if it[0] == 'rule':
            by_sel.setdefault(re.sub(r'\s+', ' ', it[3].strip()), []).append(idx)
    new_body = {}
    for sel, idxs in by_sel.items():
        if len(idxs) < 2: continue
        last = idxs[-1]
        moved = []
        for pos, e in enumerate(idxs[:-1]):
            keep = []
            later_same = idxs[pos + 1:]
            for p, v in decls(new_body.get(e, items[e][4])):
                imp = '!important' in v
                over = any(p == q and (not imp or '!important' in w) for L in later_same for q, w in decls(items[L][4]))
                if over:
                    stats['dropped'] += 1; continue
                between = css[items[e][2]:items[last][1]]
                fams = families_in(between)
                fams_later = {family(q) for L in later_same for q, _ in decls(items[L][4]) if q != p}
                if family(p) in fams or family(p) in fams_later:
                    keep.append((p, v)); stats['kept'] += 1
                else:
                    moved.append((p, v)); stats['moved'] += 1
            new_body[e] = '; '.join(f'{p}: {v}' for p, v in keep)
        if moved:
            new_body[last] = ' ' + '; '.join(f'{p}: {v}' for p, v in moved) + ';' + items[last][4]
    out = []
    for idx, it in enumerate(items):
        if idx in new_body and it[0] == 'rule':
            b = new_body[idx].strip()
            if not b.strip(' ;'):
                stats['blocks'] += 1; continue
            out.append(it[3] + '{ ' + b.rstrip(' ;') + '; }')
        else:
            out.append(css[it[1]:it[2]])
    return ''.join(out)


if __name__ == '__main__':
    for f in FILES:
        css = f.read_text(); stats = {'dropped': 0, 'moved': 0, 'kept': 0, 'blocks': 0}
        new = re.sub(r'\n{3,}', '\n\n', fold(css, stats))
        print(f.name, f'{len(css.splitlines())} → {len(new.splitlines())} lines', stats)
        if '--dry' not in sys.argv: f.write_text(new)

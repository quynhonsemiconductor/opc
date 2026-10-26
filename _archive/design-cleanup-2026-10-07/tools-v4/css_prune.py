"""v4.1 clean-up: drop CSS for classes no screen and no catalog demo uses (retired components, dead states).
Selector lists are trimmed per selector; a rule goes only when none of its selectors survive. Comments that sat
directly above a removed rule go with it. @keyframes / @font-face are kept. Usage: python3 css_prune.py [--dry]"""
import re, sys, glob, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
FILES = [ROOT / 'system/components/components.css', ROOT / 'system/components/recipes.css']
KEEP_ALWAYS = {'u-sr', 'c-ic'}


def used_classes():
    html = ' '.join(pathlib.Path(f).read_text() for f in glob.glob(str(ROOT / 'apps/app/screens/*.html')) + [str(ROOT / 'system/components/catalog.html')])
    u = set(KEEP_ALWAYS)
    for cl in re.findall(r'class="([^"]+)"', html):
        u.update(cl.split())
    return u


def split_top(sel):
    out, depth, cur = [], 0, ''
    for ch in sel:
        if ch in '([': depth += 1
        if ch in ')]': depth -= 1
        if ch == ',' and depth == 0:
            out.append(cur); cur = ''
        else:
            cur += ch
    out.append(cur)
    return out


def dead_sel(sel, used):
    return any(c not in used for c in re.findall(r'\.((?:c|r|u)-[a-zA-Z0-9_-]+)', sel))


def prune(css, used, stats):
    """css = a block body (top level or inside @media). Returns the pruned text."""
    out, i, n = [], 0, len(css)
    pending = ''   # whitespace + comments waiting to see whether the next rule survives
    while i < n:
        if css.startswith('/*', i):
            j = css.index('*/', i) + 2; pending += css[i:j]; i = j; continue
        if css[i].isspace():
            j = i
            while j < n and css[j].isspace(): j += 1
            pending += css[i:j]; i = j; continue
        j = css.index('{', i)
        prelude = css[i:j]
        depth, k = 1, j + 1
        while depth:
            if css.startswith('/*', k): k = css.index('*/', k) + 2; continue
            if css[k] == '{': depth += 1
            elif css[k] == '}': depth -= 1
            k += 1
        body = css[j + 1:k - 1]
        p = prelude.strip()
        if p.startswith('@keyframes') or p.startswith('@font-face'):
            out.append(pending + css[i:k]); pending = ''
        elif p.startswith('@'):
            inner = prune(body, used, stats)
            if inner.strip() and re.search(r'\{', re.sub(r'/\*.*?\*/', '', inner, flags=re.S)):
                out.append(pending + prelude + '{' + inner + '}')
            else:
                stats['rules'] += 1
            pending = ''
        else:
            sels = split_top(prelude)
            keep = [s for s in sels if not dead_sel(s, used)]
            stats['sels'] += len(sels) - len(keep)
            if keep:
                new_prelude = ','.join(keep) if len(keep) < len(sels) else prelude
                out.append(pending + new_prelude.rstrip() + (' ' if len(keep) < len(sels) else '') + '{' + body + '}')
            else:
                stats['rules'] += 1
                # keep a pending section banner (=====) even if the rule under it goes
                banners = re.findall(r'/\* =+.*?\*/', pending, flags=re.S)
                if banners: out.append('\n\n' + '\n'.join(banners))
            pending = ''
        i = k
    out.append(pending)
    return ''.join(out)


if __name__ == '__main__':
    used = used_classes()
    for f in FILES:
        css = f.read_text(); stats = {'rules': 0, 'sels': 0}
        new = prune(css, used, stats)
        new = re.sub(r'(/\* =+[^*]*?=+ \*/\s*)+(?=/\* =+)', '', new)   # banners with nothing under them
        new = re.sub(r'\n{3,}', '\n\n', new)
        print(f.name, f'{len(css.splitlines())} → {len(new.splitlines())} lines · rules removed {stats["rules"]} · selectors trimmed {stats["sels"]}')
        if '--dry' not in sys.argv:
            f.write_text(new)

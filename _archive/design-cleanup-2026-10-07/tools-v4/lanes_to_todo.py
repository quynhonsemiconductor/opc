"""One-off v4.1 clean-up: replace the retired c-lanes/c-lane markup with c-todo (same meaning: numbered rows,
done / now / next, one action). Idempotent: does nothing when a file has no c-lane left.
Usage: python3 lanes_to_todo.py <screen.html>…"""
import re, sys, pathlib


def text(html):
    return re.sub(r'\s+', ' ', re.sub(r'<svg.*?</svg>', '', html, flags=re.S)).strip()


def inner(li, cls):
    m = re.search(rf'<(\w+) class="{cls}"[^>]*>(.*?)</\1>', li, flags=re.S)
    return m.group(2) if m else ''


def row(li):
    k = 'done' if 'c-lane--done' in li else 'now' if 'c-lane--now' in li else ''
    n = inner(li, 'c-lane__n')
    n = '<svg class="c-ic" aria-hidden="true"><use href="#i-check"/></svg>' if 'i-check' in n else text(n)
    title = inner(li, 'c-lane__title')
    kicker = text(inner(li, 'c-lane__kicker'))
    meta = text(re.sub(r'<span class="c-lane__hint">|</span>', '', inner(li, 'c-lane__amt'))) or text(inner(li, 'c-lane__detail'))
    if kicker and k != 'now':
        meta = f'{kicker} · {meta}' if meta else kicker
    acts = inner(li, 'c-lane__actions').strip()
    acts = re.sub(r'<a class="c-btn([^"]*)"', r'<a class="c-btn\1 c-todo__go"', acts)
    cls = f'c-todo__item c-todo__item--{k}' if k else 'c-todo__item'
    cur = ' aria-current="step"' if k == 'now' else ''
    m = f'<p class="c-todo__m">{meta}</p>' if meta else ''
    return (f'<li class="{cls}"{cur}><span class="c-todo__n" aria-hidden="true">{n}</span>'
            f'<div><h3 class="c-todo__t">{title}</h3>{m}</div>{acts}</li>')


def convert(path):
    s = path.read_text()
    out, n = s, 0
    for m in re.finditer(r'<ol class="c-lanes"([^>]*)>(.*?)</ol>', s, flags=re.S):
        lis = re.findall(r'<li class="c-lane[^"]*">.*?</li>', m.group(2), flags=re.S)
        new = f'<ol class="c-todo"{m.group(1)}>' + ''.join(row(li) for li in lis) + '</ol>'
        out = out.replace(m.group(0), new, 1); n += 1
    if n:
        path.write_text(out)
    return n


if __name__ == '__main__':
    for f in sys.argv[1:]:
        print(pathlib.Path(f).name, convert(pathlib.Path(f)), 'list(s)')

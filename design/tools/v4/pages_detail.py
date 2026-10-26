# v4.1 · detail pages (order-detail now; invoice-detail reuses it). Calm shell, a first-read figure under the title,
# sections as hairline regions (r-detail--calm), the timeline as the one raised panel. Usage: python3 pages_detail.py
import re, pathlib, sys
from pages import build, CUR

SRC = pathlib.Path(__file__).parent / 'src_v40'

def detail(name, current, figure_html, title_from=None):
    s = (SRC / f'{name}.html').read_text()
    style = re.search(r'<style>([\s\S]*?)</style>', s); style = style.group(1).replace('/* layout only */', '') if style else ''
    mo = re.search(r'<main class="r-shell__content"[^>]*>', s); main = s[mo.end():s.index('</main>')]
    after = s[s.index('</nav>', s.index('<nav class="c-tabbar"')) + len('</nav>'):s.index('</body>')].strip()
    main = main.replace('<div class="r-detail__head">', '<div class="r-detail__head r-detail__head--calm">', 1)
    main = re.sub(r'(<h1 class="r-detail__title">[^<]*</h1>)', r'\1' + figure_html, main, count=1)
    main = main.replace('<div class="r-detail__grid">', '<div class="r-detail__grid r-detail--calm">', 1)
    title = re.search(r'<title>(.*?) — OPC</title>', s).group(1)
    build(name, title, main, current, overlay=after, style=style)

if __name__ == '__main__':
    # v4.2: order-detail is built by pages_order360.py (Order 360)
    if False: detail('order-detail', 'orders', f'<p class="r-detail__fig"><b class="c-figure">3.420.000{CUR}</b><span class="c-sub">2 món · công nợ, hạn trả 09/10/2026 · Zalo 09:48</span></p>')

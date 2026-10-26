# v4.1 · Cần xử lý group: approvals (queue), audit (feed). Usage: python3 pages_queue.py
import re, pathlib
from pages import build, ic

SRC = pathlib.Path(__file__).parent / 'src_v40'

def parts(name):
    s = (SRC / f'{name}.html').read_text()
    style = re.search(r'<style>([\s\S]*?)</style>', s); style = style.group(1).replace('/* layout only */', '') if style else ''
    mo = re.search(r'<main class="r-shell__content"[^>]*>', s); main = s[mo.end():s.index('</main>')]
    after = s[s.index('</nav>', s.index('<nav class="c-tabbar"')) + len('</nav>'):s.index('</body>')].strip()
    title = re.search(r'<title>(.*?) — OPC</title>', s).group(1)
    return main, after, style, title

# approvals — the promise ("only drafts until you approve") becomes the subline; #1 is the raised panel
main, after, style, title = parts('approvals')
main = main.replace('<p class="r-page-head__sub u-meta">Thứ Sáu, 02/10/2026 · 4 việc chờ chị</p>',
                    '<p class="c-sub">4 việc chờ chị · OPC và Trợ lý chỉ soạn sẵn — chị duyệt thì mới thành thật</p>')
main = re.sub(r'\s*<p class="c-say">OPC và Trợ lý chỉ soạn sẵn[^<]*</p>', '', main, count=1)
build('approvals', title, main, 'approvals', overlay=after, style=style + '\n.page { max-width: var(--read-w); }')

# audit — one filter bar (time · kind · who), the feed under a day heading, no card chrome
main, after, style, title = parts('audit')
main = main.replace('<p class="r-page-head__sub u-meta">', '<p class="c-sub">')
kinds = re.search(r'<div class="c-filters" role="toolbar" aria-label="Lọc theo loại việc">.*?</div>', main, re.S).group(0)
who = re.search(r'<div class="c-filters" role="group" aria-label="Lọc theo người thực hiện">.*?</div>', main, re.S).group(0)
seg = re.search(r'<div class="c-seg" role="radiogroup" aria-label="Thời gian">.*?</div>', main, re.S).group(0)
for x in (kinds, who, seg): main = main.replace(x, '', 1)
bar = f'''<div class="r-feedbar">
          {seg}
          <div class="r-feedbar__group"><span class="r-feedbar__k" aria-hidden="true">Việc</span>{kinds}</div>
          <div class="r-feedbar__group"><span class="r-feedbar__k" aria-hidden="true">Ai làm</span>{who}</div>
        </div>'''
main = main.replace('<div class="page">', '<div class="page">\n        ' + bar, 1)
main = main.replace('<section class="c-card" aria-label="Nhật ký hoạt động hôm nay">',
                    '<section class="r-listcard" aria-label="Nhật ký hoạt động hôm nay">\n          <h2 class="c-timeline__day">Hôm nay · Thứ Sáu 02/10/2026</h2>')
main = re.sub(r'(<li class="c-timeline__item) c-timeline__item--pend(">(?:(?!</li>).)*?Trợ lý)', r'\1 c-timeline__item--ai\2', main, flags=re.S)
# v4.1 polish: "Ai làm" is one menu button beside the time segment, so only one row of chips remains
main = re.sub(r'<div class="r-feedbar__group"><span class="r-feedbar__k" aria-hidden="true">Ai làm</span>.*?</div></div>', '', main, count=1, flags=re.S)
main = re.sub(r'(<div class="c-seg" role="radiogroup" aria-label="Thời gian">.*?</div>)',
              lambda m: '<div class="r-feedbar__row">' + m.group(1) + '<button class="c-btn r-feedbar__who" type="button" aria-haspopup="listbox">Ai làm: <b>Tất cả</b>' + ic('i-chev') + '</button></div>',
              main, count=1, flags=re.S)
main = main.replace('<h2 class="c-timeline__day">', '<ul class="r-feedbar__key" aria-label="Chú thích chấm"><li><i></i>Xong · đã xác minh</li><li><i class="p"></i>Đang chờ · Trợ lý soạn, chờ duyệt</li><li><i class="y"></i>Người trong hộ làm</li><li><i class="s"></i>Hệ thống tự động</li></ul>\n          <h2 class="c-timeline__day">', 1)
build('audit', title, main, 'settings', overlay=after, style=style + '\n.page { max-width: var(--read-w); }')

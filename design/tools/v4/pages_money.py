# v4.1 · Tiền group: money, money--assign, money--help.  Usage: python3 pages_money.py
# Job: "is the money real?" → the VERIFIED amount is the first read (evaluator: verified must dominate pending);
# what needs the owner sits in the one raised panel; the ledger below is rows, not a table.
import re
from pages import build, ic, sign, CUR, subnav, old_overlay

SUB = subnav('Tiền', [('Thu chi &amp; đối chiếu', 'money.html'), ('Công nợ', 'receivables.html'), ('Đóng ca', 'shift-close.html')], 'Thu chi &amp; đối chiếu')

TXN = [  # time, payer, content, amount, match, state, note, href — An Nhiên, 06/10 to 10:45 (v4.3)
  ('09:20', 'NGUYEN VAN NAM', 'gui tien bo kho', '585.000 ₫', None, 'you', 'không có mã đơn', 'money--assign.html'),
  ('09:52', 'HOMESTAY MAY NGAN', 'DH2045', '390.000 ₫', 'DH-2045', 'late', 'quá 30 phút · kiểm tra trong app MB', 'order-detail.html'),
  ('09:05', 'LE VAN TOAN', 'DH2048', '195.000 ₫', 'DH-2048', 'ok', 'khớp sao kê 09:06', 'order-detail.html'),
  ('08:41', 'CONG TY TNHH SUNRISE', 'DH2049 SUNRISE', '4.550.000 ₫', 'DH-2049', 'ok', 'khớp sao kê 08:42', 'receivables.html'),
]
ST = {'pend': ('pend', 'i-clock', 'Chờ xác minh'), 'late': ('pend', 'i-alert', 'Chờ quá 30 phút'),
      'you': ('you', 'i-arrow', 'Chưa gán'), 'ok': ('ok', 'i-check', 'Đã xác minh')}

def rows():
    out = []
    for t, who, content, amt, match, st, note, href in TXN:
        m = f'→ {match}' if match else 'chưa có đơn'
        out.append(f'<li class="c-orders__row"><a href="{href}"><span class="c-orders__who">{who}<small>{t} · “{content}” · {m}</small></span>'
                   f'<span class="c-orders__st">{sign(*ST[st])}</span><span class="c-orders__amt u-money">{amt}</span></a></li>')
    return '\n            '.join(out)

def main(assign_quiet=False):
    go1 = 'c-btn c-todo__go' if assign_quiet else 'c-btn c-btn--act c-todo__go'
    return f'''      {SUB}
      <div class="r-page-head">
        <div>
          <h1 class="r-page-head__title">Tiền &amp; đối chiếu</h1>
          <p class="c-sub">Thứ Ba 06/10 · MB 0901 2345 678</p>
        </div>
        <div class="r-page-head__acts r-page-head__acts--desk">
          <a class="c-btn" href="money--help.html">{ic("i-help")}Trợ giúp</a>
          <a class="c-btn" href="shift-close.html">{ic("i-cash")}Đóng ca</a>
        </div>
      </div>

      <div class="r-home">
        <section class="c-stat r-home__hero" aria-labelledby="h-real">
          <div class="c-stat__top">
            <h2 class="c-stat__label" id="h-real">Đã khớp sao kê MB hôm nay</h2>
            <span class="c-stat__fresh">MB · cập nhật 10:43</span>
          </div>
          <div class="c-stat__main m-main">
            <div>
              <p class="c-stat__fig">4.745.000{CUR}</p>
              <p class="c-stat__delta"><span class="c-sign c-sign--ok"><span class="c-sign__pic">{ic("i-check")}</span>Đã xác minh</span><span class="m-match"><b>2/4</b> khoản đã khớp · 1 chờ · <a href="money--assign.html">1 chưa gán</a></span></p>
            </div>
            <ul class="c-debts m-facts" aria-label="Số dư và tiền mặt">
              <li class="c-debts__row"><span class="c-debts__k">Số dư MB</span><span class="c-debts__v">62.480.000 ₫</span><span class="c-debts__m">gồm cả tiền chưa xác minh</span></li>
              <li class="c-debts__row"><span class="c-debts__k">Tiền mặt hôm nay</span><span class="c-debts__v">1.000.000 ₫</span><span class="c-debts__m"><a href="money--cash.html">đếm cuối ngày</a></span></li>
            </ul>
          </div>
          <div class="c-split">
            <div class="c-split__bar" role="img" aria-label="Tiền vào MB hôm nay 5.720.000 ₫: đã xác minh 4.745.000 ₫, chờ xác minh 390.000 ₫, chưa gán 585.000 ₫"><i class="c-split__ok" style="flex:4745"></i><i class="c-split__pend" style="flex:390"></i><i class="c-split__you" style="flex:585"></i></div>
            <ul class="c-split__legend">
              <li class="c-split__item c-split__item--ok"><span class="c-split__k">Đã xác minh · 2 khoản</span></li>
              <li class="c-split__item c-split__item--pend c-split__item--quiet"><a href="#txn"><span class="c-split__k">Chờ xác minh · 1 khoản</span><b class="c-split__v">390.000{CUR}</b></a></li>
              <li class="c-split__item c-split__item--you"><a href="money--assign.html"><span class="c-split__k">Chưa gán · 1 khoản</span><b class="c-split__v">585.000{CUR}</b></a></li>
            </ul>
            <p class="c-split__explain"><b>Chờ xác minh</b> = ngân hàng đã báo, chưa khớp sao kê</p>
          </div>
        </section>

        <section class="c-card r-home__todo" aria-labelledby="h-todo">
          <div class="c-card__head"><h2 class="c-card__title" id="h-todo">Cần xem <span class="c-count" aria-label="4 khoản">4</span></h2></div>
          <ol class="c-todo">
            <li class="c-todo__item c-todo__item--now"><span class="c-todo__n" aria-hidden="true">1</span>
              <div><h3 class="c-todo__t">Gán 585.000 ₫ vào đơn</h3><p class="c-todo__m">NGUYEN VAN NAM · 09:20 · có thể là DH-2050</p></div>
              <a class="{go1}" href="money--assign.html">Gán đơn</a></li>
            <li class="c-todo__item"><span class="c-todo__n" aria-hidden="true">2</span>
              <div><h3 class="c-todo__t">DH-2045 chờ quá 30 phút</h3><p class="c-todo__m">390.000 ₫ · Homestay Mây Ngàn</p></div>
              <a class="c-btn c-todo__go" href="order-detail.html">Kiểm tra</a></li>
            <li class="c-todo__item"><span class="c-todo__n" aria-hidden="true">3</span>
              <div><h3 class="c-todo__t">Sunrise vừa chuyển 8.400.000 ₫</h3><p class="c-todo__m">2 hoá đơn tháng 9</p></div>
              <a class="c-btn c-todo__go" href="money--split.html">Xem đề xuất</a></li>
            <li class="c-todo__item"><span class="c-todo__n" aria-hidden="true">4</span>
              <div><h3 class="c-todo__t">195.000 ₫ có thể trùng</h3><p class="c-todo__m">DH-2048 · 09:06</p></div>
              <a class="c-btn c-todo__go" href="money--duplicate.html">Kiểm tra</a></li>
          </ol>
        </section>

        <section class="c-card r-home__orders m-ledger" id="txn" aria-labelledby="h-txn">
          <div class="c-card__head"><h2 class="c-card__title" id="h-txn">Tiền vào MB hôm nay</h2><span class="u-money">5.720.000 ₫</span></div>
          <div class="c-tabs" role="tablist" aria-label="Lọc theo trạng thái">
            <button class="c-tabs__tab" role="tab" aria-selected="true" type="button">Tất cả <span class="c-tabs__count">4</span></button>
            <button class="c-tabs__tab" role="tab" aria-selected="false" type="button">Chờ xác minh <span class="c-tabs__count">1</span></button>
            <button class="c-tabs__tab c-tabs__tab--you" role="tab" aria-selected="false" type="button">Chưa gán <span class="c-tabs__count">1</span></button>
            <button class="c-tabs__tab" role="tab" aria-selected="false" type="button">Đã xác minh <span class="c-tabs__count">2</span></button>
          </div>
          <div role="tabpanel" aria-label="Tất cả 4 khoản"><ul class="c-orders">
            {rows()}
          </ul></div>
        </section>
      </div>'''

STYLE = '''.m-ledger { grid-column: 1 / -1; }
.m-match { margin-left: var(--space-2); } .m-match b { font-variant-numeric: tabular-nums; } .m-match a { color: var(--act-ink); font-weight: 600; }
.m-main { display: flex; flex-wrap: wrap; align-items: start; justify-content: space-between; gap: var(--space-4) var(--space-8); }
.m-main > :first-child { flex: none; }
.m-main > .m-facts { flex: 1 1 var(--side-min); max-width: var(--facts-w); min-width: 0; }
@media (max-width: 1180px) { .m-ledger { grid-column: auto; } }
@media (max-width: 720px) { .m-main { display: grid; grid-template-columns: minmax(0, 1fr); } .m-main > .m-facts { max-width: none; } }'''

def assign_overlay():
    ov = old_overlay('money--assign')
    a = ov.index('<div class="c-options"'); b = ov.index('</div>', ov.index('</button>', ov.rindex('class="c-option"'))) + 6
    best_why = re.search(r'<button class="c-option" type="button" role="radio" aria-checked="true">.*?</button>', ov, re.S).group(0)
    best = best_why.replace('<button class="c-option"', '<button class="c-option c-option--best"', 1).replace(
        '<span class="c-option__body">', '<span class="c-option__body"><span class="c-option__tag c-option__tag--best">' + ic('i-check') + 'Gợi ý · khớp 2/3</span>', 1)
    best = re.sub(r'<span class="c-option__tag">[^<]*</span>', '', best)
    others = re.findall(r'<button class="c-option" type="button" role="radio" aria-checked="false">.*?</button>', ov, re.S)
    off = re.findall(r'<button class="c-option" type="button" role="radio" aria-checked="false" disabled>.*?</button>', ov, re.S)
    new = f'''<div class="c-options" role="radiogroup" aria-label="Gán khoản tiền vào">
        {best}
        <p class="c-options__h">Cách khác</p>
        {"".join(others)}
        <details class="c-options__off"><summary>Không chọn được ({len(off)}) · vì sao</summary>{"".join(off)}</details>
      </div>'''
    return ov[:a] + new + ov[b:]

def help_overlay():
    ov = old_overlay('money--help')
    steps = re.findall(r'<li class="c-lane"><div class="c-lane__n" aria-hidden="true">(\d)</div><div class="c-lane__body"><h3 class="c-lane__title">(.*?)</h3><p class="c-lane__detail">(.*?)</p>', ov, re.S)
    todo = '<ol class="c-todo" aria-label="Hướng dẫn ngắn">' + ''.join(
        f'<li class="c-todo__item"><span class="c-todo__n" aria-hidden="true">{n}</span><div><h3 class="c-todo__t">{t}</h3><p class="c-todo__m">{d}</p></div></li>' for n, t, d in steps) + '</ol>'
    ov = re.sub(r'<ol class="c-lanes"[\s\S]*?</ol>', todo, ov, count=1)
    return ov

build('money', 'Tiền &amp; đối chiếu', main(), 'money', style=STYLE)
build('money--assign', 'Tiền · Gán khoản chưa có mã đơn', main(assign_quiet=True), 'money', overlay=assign_overlay(), style=STYLE)
build('money--help', 'Tiền · Trợ giúp', main(), 'money', overlay=help_overlay(),
      style=STYLE + '\n.video { display: flex; align-items: center; gap: var(--space-3); text-decoration: none; color: inherit; }\n.stack { display: grid; gap: var(--space-1); }')

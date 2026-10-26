# v4.1 · Tiền group: money, money--assign, money--help.  Usage: python3 pages_money.py
# Job: "is the money real?" → the VERIFIED amount is the first read (evaluator: verified must dominate pending);
# what needs the owner sits in the one raised panel; the ledger below is rows, not a table.
import re
from pages import build, ic, sign, CUR, subnav, old_overlay

SUB = subnav('Tiền', [('Thu chi &amp; đối chiếu', 'money.html'), ('Công nợ', '#'), ('Đóng ca', '#')], 'Thu chi &amp; đối chiếu')

TXN = [  # time, payer, content, amount, match, state, note, href
  ('10:44', 'NGUYEN VAN HUNG', 'DH1043', '1.020.000 ₫', 'DH-1043', 'pend', 'Casso báo 10:44 · thường 1–3 phút', 'order-detail.html'),
  ('10:05', 'TRAN THI THU', 'DH1041 SHOPEE', '360.000 ₫', 'DH-1041', 'late', 'quá 30 phút · kiểm tra trong app MB', 'order-detail.html'),
  ('09:15', 'NHA HANG BIEN DONG', 'TT HANG KHO T9', '2.150.000 ₫', None, 'you', 'không có mã đơn', 'money--assign.html'),
  ('08:34', 'LE MINH TUAN', 'DH1036', '640.000 ₫', 'DH-1036', 'ok', 'khớp sao kê 08:35', 'order-detail.html'),
  ('08:21', 'PHAM QUOC BAO', 'DH1035', '1.250.000 ₫', 'DH-1035', 'ok', 'khớp sao kê 08:22', 'order-detail.html'),
  ('07:53', 'VO THI MAI', 'DH1030', '980.000 ₫', 'DH-1030', 'ok', 'khớp sao kê 07:54', 'order-detail.html'),
  ('07:32', 'CTY TNHH DU LICH BIEN XANH', 'DH1027 BIEN XANH', '1.690.000 ₫', 'DH-1027', 'ok', 'khớp sao kê 07:33', 'order-detail.html'),
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
          <p class="c-sub">Thứ Sáu, 02/10/2026 · tài khoản MB 0123 4567 89</p>
        </div>
        <div class="r-page-head__acts r-page-head__acts--desk">
          <a class="c-btn" href="money--help.html">{ic("i-help")}Trợ giúp</a>
          <button class="c-btn" type="button">{ic("i-cash")}Đếm tiền cuối ca</button>
        </div>
      </div>

      <div class="r-home">
        <section class="c-stat r-home__hero" aria-labelledby="h-real">
          <div class="c-stat__top">
            <h2 class="c-stat__label" id="h-real">Tiền đã chắc chắn vào MB hôm nay</h2>
            <span class="c-stat__fresh">MB · cập nhật 10:43</span>
          </div>
          <div class="c-stat__main m-main">
            <div>
              <p class="c-stat__fig">4.560.000{CUR}</p>
              <p class="c-stat__delta"><span class="c-sign c-sign--ok"><span class="c-sign__pic">{ic("i-check")}</span>Đã xác minh</span>4 khoản · khớp sao kê MB</p>
            </div>
            <ul class="c-debts m-facts" aria-label="Số dư và tiền mặt">
              <li class="c-debts__row"><span class="c-debts__k">Số dư MB</span><span class="c-debts__v">48.215.000 ₫</span><span class="c-debts__m">gồm cả tiền chưa xác minh</span></li>
              <li class="c-debts__row"><span class="c-debts__k">Tiền mặt trong ca</span><span class="c-debts__v">2.520.000 ₫</span><span class="c-debts__m">15 đơn · ca sáng · chưa tính vào MB</span></li>
            </ul>
          </div>
          <div class="c-split">
            <div class="c-split__bar" role="img" aria-label="Tiền vào MB hôm nay 8.090.000 ₫: đã xác minh 4.560.000 ₫, chờ xác minh 1.380.000 ₫, chưa gán 2.150.000 ₫"><i class="c-split__ok" style="flex:4560"></i><i class="c-split__pend" style="flex:1380"></i><i class="c-split__you" style="flex:2150"></i></div>
            <ul class="c-split__legend">
              <li class="c-split__item c-split__item--ok"><span class="c-split__k">Đã xác minh · 4 khoản</span><span class="c-split__same">= số lớn ở trên</span></li>
              <li class="c-split__item c-split__item--pend c-split__item--quiet"><a href="#txn"><span class="c-split__k">Chờ xác minh · 2 khoản</span><b class="c-split__v">1.380.000{CUR}</b></a></li>
              <li class="c-split__item c-split__item--you"><a href="money--assign.html"><span class="c-split__k">Chưa gán · 1 khoản</span><b class="c-split__v">2.150.000{CUR}</b></a></li>
            </ul>
            <p class="c-split__explain"><b>Chờ xác minh</b> = Casso đã báo có tiền, OPC đang đối chiếu với sao kê MB. <b>Đã xác minh</b> = khớp sao kê.</p>
          </div>
        </section>

        <section class="c-card r-home__todo" aria-labelledby="h-todo">
          <div class="c-card__head"><h2 class="c-card__title" id="h-todo">Cần xem <span class="c-count" aria-label="3 khoản">3</span></h2></div>
          <ol class="c-todo">
            <li class="c-todo__item c-todo__item--now"><span class="c-todo__n" aria-hidden="true">1</span>
              <div><h3 class="c-todo__t">Gán 2.150.000 ₫ vào đơn</h3><p class="c-todo__m">NHA HANG BIEN DONG · 09:15 · không có mã đơn</p></div>
              <a class="{go1}" href="money--assign.html">Gán đơn</a></li>
            <li class="c-todo__item"><span class="c-todo__n" aria-hidden="true">2</span>
              <div><h3 class="c-todo__t">DH-1041 chờ quá 30 phút</h3><p class="c-todo__m">360.000 ₫ · mở app MB xem đã nhận chưa</p></div>
              <a class="c-btn c-todo__go" href="order-detail.html">Kiểm tra</a></li>
            <li class="c-todo__item c-todo__item--wait"><span class="c-todo__n" aria-hidden="true">{ic("i-clock")}</span>
              <div><h3 class="c-todo__t">DH-1043 đang đối chiếu</h3><p class="c-todo__m">1.020.000 ₫ · OPC tự xác nhận, không cần làm gì</p></div></li>
          </ol>
        </section>

        <section class="c-card r-home__orders m-ledger" id="txn" aria-labelledby="h-txn">
          <div class="c-card__head"><h2 class="c-card__title" id="h-txn">Tiền vào MB hôm nay</h2><span class="u-money">8.090.000 ₫</span></div>
          <div class="c-tabs" role="tablist" aria-label="Lọc theo trạng thái">
            <button class="c-tabs__tab" role="tab" aria-selected="true" type="button">Tất cả <span class="c-tabs__count">7</span></button>
            <button class="c-tabs__tab" role="tab" aria-selected="false" type="button">Chờ xác minh <span class="c-tabs__count">2</span></button>
            <button class="c-tabs__tab c-tabs__tab--you" role="tab" aria-selected="false" type="button">Chưa gán <span class="c-tabs__count">1</span></button>
            <button class="c-tabs__tab" role="tab" aria-selected="false" type="button">Đã xác minh <span class="c-tabs__count">4</span></button>
          </div>
          <div role="tabpanel" aria-label="Tất cả 7 khoản"><ul class="c-orders">
            {rows()}
          </ul></div>
        </section>
      </div>'''

STYLE = '''.m-ledger { grid-column: 1 / -1; }
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
        '<span class="c-option__body">', '<span class="c-option__body"><span class="c-option__tag c-option__tag--best">' + ic('i-check') + 'Gợi ý · khớp 3/3</span>', 1)
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

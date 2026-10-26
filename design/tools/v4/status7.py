"""v7.5.2 · one status vocabulary for the whole app (eval v750 cross-screen #1). Runs after every generator, before nav7.
Seven states, one meaning and one icon each (system/maps/status.json is the spec for FE):
  ok    đã xong / đã khớp / đã xác minh        i-check  solid green      (money truth: verified)
  pass  bình thường, không cần làm gì           i-check  quiet            (Hoạt động, Đã nối, Có mã)
  pend  chờ khớp / chờ xác minh / chờ mã CQT    i-clock  amber hatch      (money truth: pending) — never for "in progress"
  wait  đang làm hoặc lượt của người khác       i-clock  grey             (Đang giao, Đã giữ hàng, Chờ khách chuyển)
  you   cần chị xem hoặc quyết                  i-alert  brand tint
  err   hỏng, sai, quá hạn, thiếu tiền          i-x      red
  unk   chưa rõ kết quả                         i-help   dashed
Usage: python3 status7.py"""
import re
from pages import SCREENS
from onboard_lib import sprite

ICON = {'ok': 'i-check', 'pass': 'i-check', 'pend': 'i-clock', 'wait': 'i-clock', 'you': 'i-alert', 'err': 'i-x', 'unk': 'i-help'}
KEEP = {'i-lock'}   # permission statements keep the lock ("Chỉ chị An")
# words decide the state when a generator picked the wrong one
RULES = [(r'^Đang dùng', 'pass'), (r'^(Đã xác minh|Khớp|Đã khớp)', 'ok'), (r'^Sẵn sàng có điều kiện', 'wait'), (r'^(Chờ xác minh|Chờ quá 30 phút|Chờ mã|Chờ cơ quan thuế)', 'pend'),
         (r'^(Đã giữ hàng|Đang |Trợ lý đang|Soạn xong|Chờ khách chuyển|Chờ tiền|Chờ điều kiện|Chưa kết nối|Chưa tính|Hạn \d|Mô phỏng|Chỉ )', 'wait'),
         (r'^(Cần |Chưa gán|Thiếu hoá đơn|Sắp hết hạn|Chưa có trong OPC)|chờ chị', 'you'),
         (r'^(Uỷ quyền|uỷ quyền)', 'pass'),
         (r'^Chưa rõ', 'unk')]
SIGN = re.compile(r'<span class="c-sign c-sign--([a-z]+)([^"]*)"([^>]*)><span class="c-sign__pic">(.*?)</span>(.*?)</span>', re.S)


def fix(m):
    kind, extra, attrs, pic, text = m.groups()
    words = re.sub(r'<[^>]+>', '', text).strip()
    for rx, k in RULES:
        if re.search(rx, words):
            kind = k
            break
    cur = re.search(r'href="#(i-[a-z0-9-]+)"', pic)
    icon = cur.group(1) if cur and cur.group(1) in KEEP else ICON.get(kind, cur.group(1) if cur else 'i-check')
    pic = re.sub(r'href="#i-[a-z0-9-]+"', f'href="#{icon}"', pic) if cur else pic
    return f'<span class="c-sign c-sign--{kind}{extra}"{attrs}><span class="c-sign__pic">{pic}</span>{text}</span>'


n = 0
for f in sorted(SCREENS.glob('*.html')):
    if f.name.startswith('_'):
        continue
    s = o = f.read_text()
    s = SIGN.sub(fix, s)
    if s != o:
        f.write_text(sprite(s)); n += 1
print(f'status7: {n} screens')

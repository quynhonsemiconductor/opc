"""v4.1 onboarding right panel (≥1180): step map on wizard steps, product proof on welcome/done.
Idempotent: removes its own <aside class="r-onboard__aside…"> before inserting. Usage: python3 onboard_aside.py [files…]"""
import re, sys, pathlib
from readiness_model import count, ITEMS
N_NEED, N_SUG, N_DONE = count('new', 'need'), count('new', 'optional'), sum(i['new'] in ('done', 'skip') for i in ITEMS)
SCREENS = pathlib.Path(__file__).resolve().parents[2] / 'apps' / 'app' / 'screens'
CK = '<svg class="c-ic" aria-hidden="true"><use href="#i-check"/></svg>'
CUR = '<span class="u-cur">₫</span>'
from onboard_lib import STEPS as _S, ABOUT
STEPS = [(t, a[0], a[1]) for t, a in zip(_S, ABOUT)]   # v7.0.0


def stepmap(now):
    rows = []
    for i, (t, m, why) in enumerate(STEPS, 1):
        k = 'done' if i < now else 'now' if i == now else 'next'
        n = CK if k == 'done' else str(i)
        cur = ' aria-current="step"' if k == 'now' else ''
        extra = f'<p class="c-stepmap__why">{why}</p>' if k == 'now' else ''
        state = '<span class="u-sr"> — xong</span>' if k == 'done' else ''
        rows.append(f'<li class="c-stepmap__s c-stepmap__s--{k}"{cur}><span class="c-stepmap__n" aria-hidden="true">{n}</span>'
                    f'<span class="c-stepmap__t">{t}{state}</span><span class="c-stepmap__m">{"xong" if k == "done" else m}</span>{extra}</li>')
    rem = sum(int(m.split()[0]) for (_, m, _) in STEPS[now - 1:])
    return (f'<aside class="r-onboard__aside r-onboard__aside--compact" aria-label="Các bước đăng ký">\n'
            f'    <nav class="c-stepmap" aria-label="Tiến độ đăng ký"><p class="c-stepmap__k">Đăng ký · còn khoảng {rem} phút · làm dở vẫn lưu</p>'
            f'<ol class="c-stepmap__list">{"".join(rows)}</ol>'
            f'<p class="c-stepmap__end">Xong {len(STEPS)} bước: làm giao dịch đầu tiên, rồi làm dần danh sách Sẵn sàng</p></nav>\n  </aside>\n  ')


def proof(caption, desk):
    cls = 'r-onboard__aside r-onboard__aside--desk' if desk else 'r-onboard__aside'
    return (f'<aside class="{cls}" aria-label="Ví dụ màn hình quầy">\n'
            f'    <figure class="r-onboard__proof"><figcaption class="r-onboard__proof-k"><span class="r-onboard__sample">Ví dụ</span>{caption}</figcaption>'
            f'<div class="c-arrived c-arrived--ok"><span class="c-arrived__pic">{CK}</span><div><span class="c-arrived__k">Đã xác minh · khớp sao kê MB</span>'
            f'<b class="c-arrived__amt">715.000{CUR}</b></div></div>'
            f'<div class="c-split__bar" role="img" aria-label="Tiền hôm nay: đã xác minh, chờ xác minh, tiền mặt"><i class="c-split__ok" style="flex:4745"></i><i class="c-split__pend" style="flex:390"></i><i class="c-split__cash" style="flex:600"></i></div>'
            f'<ul class="r-onboard__proof-legend"><li><i></i>Tiền thật đã về</li><li><i class="p"></i>Đang đối chiếu</li><li><i class="c"></i>Tiền mặt</li></ul>'
            f'<p class="r-onboard__proof-by">Tiền đọc từ sao kê ngân hàng của hộ · OPC không giữ tiền</p></figure>\n  </aside>\n  ')


def apply(path):
    s = path.read_text()
    s = re.sub(r'<aside class="r-onboard__aside[^"]*".*?</aside>\n  ', '', s, flags=re.S)
    name = path.stem
    if name == 'onboard-welcome':
        s = re.sub(r'\n\s*<figure class="r-onboard__proof".*?</figure>', '', s, count=1, flags=re.S)   # move from body
        aside = proof('Khi khách quét QR, quầy của chị hiện:', desk=False)
    elif name == 'onboard-done':   # v4.3: preview of the next screen instead of repeating the welcome specimen
        aside = ('<aside class="r-onboard__aside r-onboard__aside--desk" aria-label="Danh sách Sẵn sàng">\n'
                 '    <nav class="c-stepmap" aria-label="Sẵn sàng"><p class="c-stepmap__k">Tiếp theo · Sẵn sàng · làm dần</p><ol class="c-stepmap__list">'
                 '<li class="c-stepmap__s c-stepmap__s--now" aria-current="step"><span class="c-stepmap__n" aria-hidden="true">0/' + str(N_NEED) + '</span><span class="c-stepmap__t">Bắt buộc còn lại</span><span class="c-stepmap__m">tồn đầu kỳ, nhóm chi phí, cách giao…</span></li>'
                 '<li class="c-stepmap__s c-stepmap__s--next"><span class="c-stepmap__n" aria-hidden="true">0/' + str(N_SUG) + '</span><span class="c-stepmap__t">Tuỳ chọn</span><span class="c-stepmap__m">Zalo OA, nối ngân hàng… bỏ qua được</span></li>'
                 f'<li class="c-stepmap__s c-stepmap__s--done"><span class="c-stepmap__n" aria-hidden="true">{CK}</span><span class="c-stepmap__t">Đã xong · ' + str(N_DONE) + '</span><span class="c-stepmap__m">khi mở hộ</span></li></ol>'
                 '<p class="c-stepmap__end">Bán được ngay; nhân viên OPC có thể làm cùng chị</p></nav>\n  </aside>\n  ')
    else:
        m = re.search(r'<b>Bước (\d)/\d</b>', s)
        if not m:
            return False
        aside = stepmap(int(m.group(1)))
    s = s.replace('<footer class="r-onboard__foot">', aside + '<footer class="r-onboard__foot">', 1)
    path.write_text(s)
    return True


if __name__ == '__main__':
    files = [pathlib.Path(f) for f in sys.argv[1:]] or sorted(SCREENS.glob('onboard*.html'))
    for f in files:
        print(f.name, 'ok' if apply(f) else 'skip')

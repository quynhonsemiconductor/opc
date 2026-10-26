"""v4.1 onboarding right panel (≥1180): step map on wizard steps, product proof on welcome/done.
Idempotent: removes its own <aside class="r-onboard__aside…"> before inserting. Usage: python3 onboard_aside.py [files…]"""
import re, sys, pathlib
SCREENS = pathlib.Path(__file__).resolve().parents[4] / 'apps' / 'app' / 'screens'
CK = '<svg class="c-ic" aria-hidden="true"><use href="#i-check"/></svg>'
CUR = '<span class="u-cur">₫</span>'
STEPS = [('Số điện thoại', '1 phút', 'Để đăng nhập bằng mã Zalo — không cần nhớ mật khẩu.'),
         ('Thông tin hộ', '2 phút', 'OPC tra cổng thuế giúp chị, chị chỉ cần xác nhận.'),
         ('Xác minh chủ hộ', '2 phút', 'Để tiền QR chỉ vào đúng tài khoản của chị.'),
         ('Ngân hàng', '3 phút', 'OPC chỉ đọc tiền vào, không ai chuyển tiền đi được.'),
         ('Hàng hoá', '5 phút', 'Chụp bảng giá, AI đọc giúp — chị chỉ kiểm tra.'),
         ('Hoá đơn', '2 phút', 'Từ nay hoá đơn tự xuất mỗi lần bán.')]


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
            f'<p class="c-stepmap__end">Xong 6 bước: bán hàng, tiền QR về là thấy ngay</p></nav>\n  </aside>\n  ')


def proof(caption, desk):
    cls = 'r-onboard__aside r-onboard__aside--desk' if desk else 'r-onboard__aside'
    return (f'<aside class="{cls}" aria-label="Ví dụ màn hình quầy">\n'
            f'    <figure class="r-onboard__proof"><figcaption class="r-onboard__proof-k"><span class="r-onboard__sample">Ví dụ</span>{caption}</figcaption>'
            f'<div class="c-arrived c-arrived--ok"><span class="c-arrived__pic">{CK}</span><div><span class="c-arrived__k">Đã xác minh · khớp sao kê MB</span>'
            f'<b class="c-arrived__amt">1.020.000{CUR}</b></div></div>'
            f'<div class="c-split__bar" role="img" aria-label="Tiền hôm nay: đã xác minh, chờ xác minh, tiền mặt"><i class="c-split__ok" style="flex:4560"></i><i class="c-split__pend" style="flex:1380"></i><i class="c-split__cash" style="flex:2520"></i></div>'
            f'<ul class="r-onboard__proof-legend"><li><i></i>Tiền thật đã về</li><li><i class="p"></i>Đang đối chiếu</li><li><i class="c"></i>Tiền mặt</li></ul>'
            f'<p class="r-onboard__proof-by">Kết nối chính thức: Ngân hàng MB · Casso · Cổng thuế</p></figure>\n  </aside>\n  ')


def apply(path):
    s = path.read_text()
    s = re.sub(r'<aside class="r-onboard__aside[^"]*".*?</aside>\n  ', '', s, flags=re.S)
    name = path.stem
    if name == 'onboard-welcome':
        s = re.sub(r'\n\s*<figure class="r-onboard__proof".*?</figure>', '', s, count=1, flags=re.S)   # move from body
        aside = proof('Khi khách quét QR, quầy của chị hiện:', desk=False)
    elif name == 'onboard-done':
        aside = proof('Từ giờ, mỗi khoản QR hiện ở quầy như thế này:', desk=False).replace('class="r-onboard__aside"', 'class="r-onboard__aside r-onboard__aside--compact"', 1)
    else:
        m = re.search(r'<b>Bước (\d)/6</b>', s)
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

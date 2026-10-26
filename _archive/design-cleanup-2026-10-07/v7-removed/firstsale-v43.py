"""onboard-firstsale = the v4 counter at the QR step (counter--payment: sheet open on phone) + a guided-sale coach mark on the QR card.
Replaces the v3 r-counter / c-prod / c-route version. Idempotent. Usage: python3 firstsale.py"""
import pathlib, re
SCREENS = pathlib.Path(__file__).resolve().parents[2] / 'apps' / 'app' / 'screens'
s = (SCREENS / 'counter--payment.html').read_text()   # phone: the payment sheet is open


def ed(a, b, n=1):
    global s
    assert a in s, a[:80]
    s = s.replace(a, b, n)


s = re.sub(r'<title>.*?</title>', '<title>Bán thử · đăng ký — OPC</title>', s, count=1)
s = s.replace('DH-2053', 'đơn thử').replace('DH2053', 'BANTHU01')   # v4.3: 01/07, no stock or customers yet
s = s.replace('còn 26 · đã giữ 20', 'chưa đếm tồn').replace('còn 50 · đã giữ 30', 'chưa đếm tồn')
s = re.sub(r'<div class="r-pos__known"[\s\S]*?</div>', '', s, count=1)
# header: this is the guided test sale, not a live shift
s = re.sub(r'<div class="r-pos__title"><h1>.*?</h1><span>.*?</span></div>',
           '<div class="r-pos__title"><h1><span class="r-pos__desk">Bán thử</span><span class="r-pos__phone">Bán thử</span></h1>'
           '<span>Không tính doanh thu · bước cuối của đăng ký</span></div>', s, count=1, flags=re.S)
s = re.sub(r'<button class="c-btn r-pos__desk" type="button">Đóng ca</button>',
           '<a class="c-btn r-pos__desk" href="onboard-done.html">Bỏ qua bán thử</a>', s, count=1)
# coach mark on the QR card (step 2 of 3 of the guided sale)
m = re.search(r'<figure class="c-qrcard">.*?</figure>', s, flags=re.S)
coach = ('<div class="c-coach" role="dialog" aria-label="Hướng dẫn bán thử"><span class="c-coach__k">BÁN THỬ · 2/3</span>'
         '<p class="c-coach__text">Cho khách quét mã bên dưới bằng app ngân hàng. Tiền về là quầy báo ngay. Đơn bán thử không tính doanh thu.</p>'
         '<div class="c-coach__actions"><button class="c-btn c-btn--quiet" type="button">Bỏ qua hướng dẫn</button>'
         '<button class="c-btn c-btn--act" type="button">Tiếp</button></div></div>')
s = s.replace(m.group(0), coach.replace('class="c-coach"', 'class="c-coach c-coach--inline"', 1) + m.group(0), 1)   # above the QR card: always in view
(SCREENS / 'onboard-firstsale.html').write_text(s)
print('onboard-firstsale.html written from counter--qr.html')

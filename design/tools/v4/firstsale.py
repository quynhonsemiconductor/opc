"""onboard-firstsale = Bán nhanh at the QR step (quick-sale--qr, v7.3) + a guided-sale coach mark on the QR card.
Run after pages_sell7. Idempotent. Usage: python3 firstsale.py"""
import pathlib, re
SCREENS = pathlib.Path(__file__).resolve().parents[2] / 'apps' / 'app' / 'screens'
s = (SCREENS / 'quick-sale--qr.html').read_text()

s = re.sub(r'<title>.*?</title>', '<title>Bán thử · đăng ký — OPC</title>', s, count=1)
s = s.replace('Bán nhanh · DH-2053', 'Bán thử').replace('DH-2053', 'đơn thử').replace('DH2053', 'BANTHU01')
s = s.replace('Khách lẻ · 2 gói bò, 3 hũ muối · giá lẻ', 'Không tính doanh thu · không trừ kho · bước cuối của đăng ký')
s = s.replace('<a class="c-btn c-btn--quiet" href="quick-sale.html">Quay lại giỏ</a>', '<a class="c-btn c-btn--quiet" href="onboard-done.html">Bỏ qua bán thử</a>')
s = s.replace('href="quick-sale--done.html">Tôi đã thấy tiền về', 'href="onboard-done.html">Tôi đã thấy tiền về')
m = re.search(r'<figure class="c-qrcard">.*?</figure>', s, flags=re.S)
coach = ('<div class="c-coach c-coach--inline" role="dialog" aria-label="Hướng dẫn bán thử"><span class="c-coach__k">BÁN THỬ · 2/3</span>'
         '<p class="c-coach__text">Cho khách quét mã bên dưới bằng app ngân hàng. Tiền về là OPC báo ngay. Đơn bán thử không tính doanh thu.</p>'
         '<div class="c-coach__actions"><button class="c-btn c-btn--quiet" type="button">Bỏ qua hướng dẫn</button>'
         '<button class="c-btn" type="button">Tiếp</button></div></div>')
s = s.replace(m.group(0), coach + m.group(0), 1)
(SCREENS / 'onboard-firstsale.html').write_text(s)
print('onboard-firstsale.html written from quick-sale--qr.html')

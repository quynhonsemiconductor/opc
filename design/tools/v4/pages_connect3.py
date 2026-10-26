"""v5.1.1 · Provider intro page (GHTK): connections--info. (The directory moved to pages_connect4.py "Thêm cách nối", which also writes connections--request.)
Usage: python3 pages_connect3.py — after pages_connect2.py."""
from connect_lib import *

# ---------------------------------------------------------------- provider intro page (before connecting)
INFO = (crumb(('Kết nối', 'connections.html'), ('Thêm cách nối', 'connections--add.html'), 'GHTK')
        + dhead('Giao Hàng Tiết Kiệm (GHTK)', '<span class="c-sim">Mô phỏng</span>', 'Hãng vận chuyển · tạo vận đơn, theo dõi, thu hộ', '<a class="c-btn c-btn--act" href="connections--consent.html">Nối thử (mô phỏng)</a>')
        + '<section class="r-trustbox r-trustbox--row" aria-labelledby="rl"><h2 class="u-sr" id="rl">OPC và GHTK</h2><ul class="r-trust__list r-trust__list--row">'
          '<li class="r-trust__i r-trust__i--do"><b>Làm</b><span>tạo vận đơn khi có người bấm</span></li>'
          '<li class="r-trust__i r-trust__i--no"><b>Không làm</b><span>tự gửi lại vận đơn chưa rõ kết quả · tự trả phí</span></li>'
          '<li class="r-trust__i"><b>Phí</b><span>hiện khi tạo vận đơn, theo bảng phí của GHTK</span></li>'
          '<li class="r-trust__i"><b>Nếu không nối</b><span>giao bằng người của hộ, nhà xe hoặc nhập mã vận đơn</span></li></ul></section>'
        + '<div class="r-info__cols">'
        + card('wd', 'Làm được gì', '<dl class="c-kv"><dt>Tạo vận đơn</dt><dd>khi anh Khoa bấm bàn giao</dd><dt>Theo dõi</dt><dd>từ lúc lấy hàng tới khi giao</dd>'
               '<dt>Thu hộ</dt><dd>GHTK thu tiền khách, đối soát theo kỳ</dd></dl><p class="c-sub">Hợp khi chị gửi khách tỉnh khác, hàng nhẹ, cần thu hộ.</p>')
        + card('wn', 'Cần chuẩn bị', '<ul class="r-gate">' + row('ok', '', 'Tài khoản GHTK của hộ', 'chưa có thì OPC hướng dẫn mở')
               + row('ok', '', 'Địa chỉ lấy hàng', 'lấy từ hồ sơ hộ') + '</ul>') + '</div>')
save('connections--info', 'Kết nối · GHTK', '<div class="page">' + INFO + '</div>')
print('connect3: info')

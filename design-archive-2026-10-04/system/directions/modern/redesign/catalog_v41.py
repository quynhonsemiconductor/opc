"""v4.1 catalog section: the parts added while restructuring every screen. Idempotent (replaces its own block)."""
import pathlib, re
CAT = pathlib.Path(__file__).resolve().parents[3] / 'components' / 'catalog.html'
CK = '<svg class="c-ic" aria-hidden="true"><use href="#i-check"/></svg>'
LK = '<svg class="c-ic" aria-hidden="true"><use href="#i-lock"/></svg>'
CUR = '<span class="u-cur">₫</span>'

def sw(label, sub, state, cls, checked, extra=''):
    return (f'<li class="c-list__row"><button class="c-switch c-switch--row" type="button" role="switch" aria-checked="{checked}"{extra}>'
            f'<span class="c-switch__label">{label}<span class="c-switch__sub">{sub}</span></span>'
            f'<span class="c-switch__state c-switch__state--{cls}">{state}</span><span class="c-switch__track" aria-hidden="true"></span></button></li>')

BLOCK = f'''<!-- v41:start -->
  <section class="sec" aria-labelledby="s-v41-switch">
    <h2 id="s-v41-switch">Cài đặt · c-switch--row (Bật · Tắt · Bắt buộc · Sắp có)</h2>
    <p>Nhãn bên trái, trạng thái bằng chữ, công tắc biển. Bắt buộc: công tắc mờ, không đổi được. Sắp có: không có công tắc.</p>
    <div class="surface demo-col r-settings"><ul class="c-list">
      {sw('Giao hàng', 'Chị có đơn Zalo cần giao tận nơi.', 'Bật', 'on', 'true')}
      {sw('Thu mua nông sản', 'Bảng kê mua của nông dân.', 'Tắt', 'off', 'false')}
      {sw('Mua hàng &amp; chi phí', 'Không tắt được: doanh thu vượt 1 tỉ.', LK + 'Bắt buộc', 'lock', 'true', ' aria-disabled="true"')}
      {sw('Đặt chỗ', 'Dành cho homestay, tour.', 'Sắp có', 'soon', 'false', ' aria-disabled="true"')}
    </ul></div>
  </section>

  <section class="sec" aria-labelledby="s-v41-head">
    <h2 id="s-v41-head">Đầu trang danh sách · r-listhead</h2>
    <p>Một con số, thanh tiền thật, một ô “việc đến hạn” trung tính (liên kết). Trên điện thoại xếp dọc.</p>
    <section class="r-listhead surface" aria-label="Ví dụ đầu trang">
      <div class="r-listhead__fig"><span class="c-stat__label">Tháng 10/2026 · 19 hoá đơn</span><b class="c-figure">7.080.000{CUR}</b></div>
      <div class="r-listhead__bar"><div class="c-split__bar" role="img" aria-label="Có mã 18, chờ mã 1"><i class="c-split__ok" style="flex:18"></i><i class="c-split__pend" style="flex:1"></i></div><p class="c-sub">có mã CQT 18 · chờ mã 1</p></div>
      <a class="r-listhead__due" href="#"><span class="c-stat__label">Chờ mã CQT · 25 phút</span><span class="r-listhead__duev">HĐ 00000418 · 640.000{CUR}</span></a>
    </section>
  </section>

  <section class="sec" aria-labelledby="s-v41-feed">
    <h2 id="s-v41-feed">Nhật ký · r-feedbar, c-timeline (--ok · --pend · --ai · --you)</h2>
    <p>Sự việc đọc trước, giờ là chữ phụ. Chấm gạch = Trợ lý soạn, chờ người duyệt. Chấm mực = chính chị làm (không dùng màu biển).</p>
    <div class="surface demo-col"><ol class="c-timeline">
      <li class="c-timeline__item c-timeline__item--ok"><span class="c-timeline__time">10:47</span><span class="c-timeline__dot" aria-hidden="true"></span><div>Đã xác minh 1.020.000 ₫ · DH-1043</div></li>
      <li class="c-timeline__item c-timeline__item--ai"><span class="c-timeline__time">09:50</span><span class="c-timeline__dot" aria-hidden="true"></span><div>Soạn nháp đơn DH-1040 từ tin nhắn Zalo · chờ chị duyệt</div></li>
      <li class="c-timeline__item c-timeline__item--you"><span class="c-timeline__time">09:15</span><span class="c-timeline__dot" aria-hidden="true"></span><div>Chị Hai sửa giá Mực khô loại 1</div></li>
    </ol></div>
  </section>

  <section class="sec" aria-labelledby="s-v41-btn">
    <h2 id="s-v41-btn">Nút phụ · c-btn--quiet, c-btn--danger c-btn--quiet</h2>
    <p>Nút phụ không có viền. Huỷ cạnh nút chính: chữ đỏ, không viền. Trong onboarding nút phụ là liên kết.</p>
    <div class="surface demo-col" style="display:flex;gap:var(--space-2);flex-wrap:wrap">
      <button class="c-btn c-btn--act" type="button">Xác nhận đơn</button><button class="c-btn" type="button">In phiếu</button>
      <button class="c-btn c-btn--quiet" type="button">Kiểm tra</button><button class="c-btn c-btn--danger c-btn--quiet" type="button">Huỷ đơn</button>
    </div>
  </section>

  <section class="sec" aria-labelledby="s-v41-recap">
    <h2 id="s-v41-recap">Onboarding xong · r-onboard__recap</h2>
    <p>Các bước đã xong gập thành một dòng đã xác minh; việc nên làm tiếp hiện ngay.</p>
    <div class="surface demo-col r-onboard__body" style="max-width:none;margin:0"><details class="r-onboard__recap">
      <summary><span class="c-sign c-sign--ok"><span class="c-sign__pic">{CK}</span>6/6 bước đã xong</span><span class="u-meta">Xem lại</span></summary>
      <p class="c-say">Số điện thoại · Thông tin hộ · Xác minh chủ hộ · Ngân hàng MB · Hàng hoá · Hoá đơn</p>
    </details></div>
  </section>
<!-- v41:end -->
'''

s = CAT.read_text()
s = re.sub(r'<!-- v41:start -->.*?<!-- v41:end -->\n', '', s, flags=re.S)
s = s.replace('\n</main>', '\n' + BLOCK + '</main>', 1)
CAT.write_text(s)
print('catalog v4.1 section written')

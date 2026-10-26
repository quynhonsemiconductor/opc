# Fix list — onboarding round 1 (evaluator 7.7). Edit only the named files with Edit; same rules as feature-common.md.
1. onboard-products--review.html:
   - First group under a heading "2 món chị cần kiểm tra": the 2 unsure rows as c-field[data-check]. Each gets a
     small c-btn--quiet "Đúng rồi" beside the field and a "Xem trong ảnh" c-btn--quiet.
   - Second group "7 món AI đọc chắc chắn" as a compact c-list (name · price/unit · c-btn--quiet "Sửa"), not
     7 field pairs.
   - Primary label: "Lưu 9 món · còn 2 món chưa kiểm tra" (keep it enabled).
2. onboard-verify.html:
   - Order: (a) Chụp CCCD và khuôn mặt (checked) · (b) Nhân viên OPC đến giúp — hẹn chị Lan, Thứ Bảy 03/10/2026,
     8:00 · (c) "Xác minh bằng thẻ CCCD gắn chip" with meta "Nhân viên OPC mang máy tính đến hướng dẫn".
   - No "Cas ID", "chip CCCD" or "laptop" anywhere. The primary stays "Tiếp tục".
3. onboard-help.html: move r-help__people (the human block) ABOVE the c-answer, with the heading "Cần người thật
   giúp?". Make sure all 3 buttons are fully visible at 390 without clipping.
4. onboard-household.html:
   - Under the MST field: c-field__hint "In trên giấy đăng ký hộ kinh doanh. Không nhớ? Chạm “Tra bằng số CCCD”."
     Also add a visible c-btn--quiet "Tra bằng số CCCD".
   - Move the ngành chips ABOVE "Tên hiển thị cho khách" so they are not under the sticky footer.
5. onboard-invoice.html:
   - Replace "Hộ có doanh thu trên 1 tỷ/năm…" with "Hộ bán trên 1 tỷ đồng mỗi năm (khoảng 2,7 triệu mỗi ngày)
     phải xuất hoá đơn điện tử từ máy tính tiền. OPC làm tự động mỗi khi bán."
   - Option 1 meta: "OPC kết nối phần mềm hoá đơn giúp chị". Do not name Hilo or Casso on this screen.
6. onboard-bank.html: the second fact becomes "Kết nối qua Casso — đơn vị OPC dùng để nối với ngân hàng".
7. onboard-otp.html: add a line under the boxes: "Mở tin nhắn Zalo từ OPC Gia Lai — mã sẽ tự điền".
8. onboard-done.html: add a 6th c-lane--done "Hoá đơn điện tử · Xong 02/10/2026 · tự xuất khi bán".
9. onboard-assisted.html:
   - Show the timer once only ("Mã hết hạn sau 4:32").
   - Add a c-btn "Tạo mã mới" and a c-btn--quiet "Chuyển sang xác minh bằng giấy tờ". The second needs a
     confirmation, so append the note "(sẽ hỏi xác nhận)".
   - Show chị Hai's phone 0905 812 347.
   - Fill the right-column space with a c-card "Trên điện thoại chị Hai" · "Bước 3/6 · đang chờ quét mã" (c-sign--wait).
10. onboard-firstsale.html: nothing to change (the ring is now ink via the component).
Then re-run the machine pass for each edited file (390 --mobile --min-target 56, 1440, 1280 --stress) plus a11y, re-shoot at 390 (assisted at 1440)
into /Users/benq/Desktop/qnsc/opc/design/apps/app/shots with --prefix <file>, and reply ≤ 120 words with done/not-done per item.

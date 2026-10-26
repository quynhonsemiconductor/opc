# Kiểm toàn luồng v7.5.2 (09/10/2026) — kết quả và nguồn số duy nhất

Hai người kiểm độc lập: (A) đi trọn luồng như chị An qua liên kết thật; (B) rà số liệu trên mọi màn.
Luật v7 đúng ở mọi màn được kiểm (4 việc độc lập, trừ kho một lần, nợ không chặn đơn, không tính thuế, OPC không chuyển tiền, Agent soạn – chị gửi).

## Nguồn số duy nhất lúc 06/10 10:45 (mọi màn phải theo)
| Số | Giá trị |
|---|---|
| Doanh thu từ 01/01 | 718.400.000 ₫ (380 tr trước OPC + 338,4 tr quý III) · dưới 1 tỷ · nhịp năm ~1,06 tỷ |
| Bò một nắng | tồn 46 · giữ 20 cho DH-2052 · khả dụng 26 |
| Muối kiến vàng | tồn 80 · giữ 30 cho DH-2052 · khả dụng 50 · MH-0118 45 hũ về, chưa nhập kho (xác nhận → tồn 125) |
| DH-2052 Sunrise | đặt 09:02 qua Zalo OA · chị An xác nhận, giữ hàng 09:15 · giao trước 15:00 hôm nay · 6.250.000 ₫ |
| Phải trả HTX Cao Nguyên | 2.800.000 ₫ (còn lại MH-0109, hạn 08/10); MH-0118 thêm 1.800.000 khi xác nhận |
| Tiền mặt | 1.000.000 ₫ tiền lẻ đầu ngày; thu tiền mặt trong ngày tính khi đếm cuối ngày |
| Sunrise nợ | 8.400.000 ₫ = HĐ 00000187 5.200.000 + HĐ 00000193 3.200.000 |

## Việc phải làm (P1 trước)
- P1 số liệu: Tổng quan và Tính năng ghi 1,28 tỷ / "đã vượt 1 tỷ" → 718,4 tr; stock-count "sổ 30 hũ"; Bán nhanh "còn 24 / 92"; DH-2052 08:15/14:00/"ngày mai"; HTX 4.800.000; "thiếu 5 kg"; Công nợ "cập nhật 14:05".
- P1 luồng: Đặt hàng (purchase-new) chết; hàng trong danh sách đơn mua không mở hồ sơ; Bàn giao (delivery--pick) không dẫn tiếp; Bán nhanh không có trên thanh dưới điện thoại.
- P1 chữ cũ: "quầy" trong chú thích trạng thái và Hoá đơn; "đóng ca" ở delivery--courier.
- P2: form thêm nhà cung cấp / khách; Xuất Excel; dòng chết ở Yêu cầu; trạng thái đã khoá kỳ; ghi mã nộp thuế; thông báo doanh thu năm; báo tài khoản ngân hàng; đang giao; tách đơn khi giao thiếu.
- P3: liên kết chết trong đăng ký; manifest `flows[]` còn màn quầy.

## Bổ sung v7.6.0
| Số | Giá trị |
|---|---|
| Đơn tách khi giao thiếu | DH-2056 (12 hũ muối); DH-2055 là Quán Gió Núi (lấy chiều Thứ Tư) |
| Đơn giao không được | DH-2042 Homestay Mây Ngàn (DH-2045 là đơn đã giao, chờ xác minh 390.000 ₫) |
| Đã thu từ đơn đã giao hôm nay | 4.745.000 ₫ (DH-2049 4.550.000 + DH-2048 195.000) |
| Sổ kho bò tháng 10 | đầu tháng 70 · xuất 8 + 15 + 1 · tồn 46 · giá vốn bình quân 190.000 ₫ · giá trị 8.740.000 ₫ |
| Chi phí tháng 10 đến 06/10 | 2.950.000 ₫ (bao bì 850.000 · xăng 850.000 · điện tháng 9 1.250.000) |

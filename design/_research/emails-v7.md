# Email câu hỏi v7 (nháp, chờ chị duyệt rồi mới gửi)

Nguồn: `_research/mandatory-2026.md`, `system/E2E-SCOPE.md`, NOTES v7.1–7.5.1. Mỗi câu hỏi ghi màn hình đang chờ câu trả lời.

---

## 1. Gửi kế toán (chị Lan)

**Tiêu đề:** OPC – nhờ chị xác nhận 10 điểm thuế và sổ cho hộ kinh doanh (trước khi chạy thử)

Chào chị Lan,

OPC đang làm bản thử cho các hộ kinh doanh ở Gia Lai. Trong giai đoạn thử, OPC **không tính số thuế**. OPC chỉ gom doanh thu và chứng từ, nhắc hạn, hướng dẫn hộ tự khai trên eTax. Để các con số và quy tắc đúng, em nhờ chị xác nhận các điểm dưới đây. Mỗi điểm chị chỉ cần trả lời đúng/sai kèm căn cứ (số văn bản, điều).

1. **Mốc doanh thu không phải nộp thuế năm 2026.** Bọn em đang thấy hai con số: 200 triệu (Luật Thuế GTGT 2024) và 1 tỷ (tin năm 2026, NĐ 68/2026). Áp dụng mốc nào, từ ngày nào? *(màn Kê khai: thanh luỹ kế năm)*
2. **Mẫu tờ khai và kỳ khai.** Thông tư 40/2021 đã được thay bằng TT 18/2026, đúng không? Hộ khai theo quý thì dùng mẫu nào (01/CNKD hay mẫu mới), và hạn nộp quý III/2026 có phải 31/10 không? *(màn Hướng dẫn khai)*
3. **Thông báo doanh thu năm.** Hộ dưới mốc có phải gửi thông báo doanh thu năm không? Nếu có thì mẫu nào, hạn nộp ngày nào? *(Kê khai: "Thông báo doanh thu năm 2026")*
4. **Thông báo tài khoản ngân hàng.** Hộ phải báo những tài khoản và ví nào, theo mẫu nào, trong bao nhiêu ngày khi mở tài khoản mới? *(đăng ký bước 4; Kê khai)*
5. **Sổ theo TT 152/2025.** Hộ của bọn em (mua về bán, một kho) phải giữ những sổ nào? Sổ hàng hoá theo dõi cả số lượng lẫn giá trị phải không? *(Sổ sách; bộ chứng từ)*
6. **Giá vốn.** Dùng bình quân gia quyền di động có được không? Phí vận chuyển khi mua hàng có cộng vào giá vốn không? *(Đơn mua)*
7. **Tiền khách trả dư / trả trước.** Ghi vào sổ như thế nào? Bọn em đang coi đó là tiền của khách, chưa phải doanh thu. *(Thu chi: khách trả dư)*
8. **Trả hàng và hoá đơn điều chỉnh** (theo NĐ 254/2026, TT 91/2026):
   - a) Khách trả hàng: hộ, với tư cách người bán, lập hoá đơn điều chỉnh giảm. Có cần biên bản không?
   - b) Hộ trả hàng cho nhà cung cấp: nhà cung cấp lập hoá đơn điều chỉnh, đúng không?

   *(Đơn bán và Đơn mua: trả hàng)*
9. **Chứng từ không có hoá đơn.** Ảnh phiếu giao hàng viết tay, biên lai xăng có dùng làm chứng từ chi phí được không? Có cần bảng kê hàng mua không có hoá đơn không? *(Đơn mua: chứng từ viết tay)*
10. **Hoá đơn và chữ ký số.**
    - Hộ có doanh thu từ 1 tỷ trở lên, bán cho người tiêu dùng, thì bắt buộc dùng hoá đơn máy tính tiền từ ngày nào?
    - Chữ ký số SmartCA trên VNeID có dùng ký hoá đơn bán hàng được không?
    - Hoá đơn điện tử miễn phí 12 tháng thì hộ nào đủ điều kiện?

    *(đăng ký bước 5; Bán nhanh)*

Thêm một câu: mã số thuế của hộ là số định danh 12 số của chủ hộ, hay vẫn là MST 10 số? *(đăng ký bước 2)*

Chị trả lời dần cũng được. Câu nào chị chưa chắc, OPC sẽ tiếp tục ghi "chờ kế toán xác nhận" trên màn hình.

Cảm ơn chị.

---

## 2. Gửi CEO

**Tiêu đề:** OPC v7 – 6 quyết định cần anh/chị trước khi chạy thử

Chào anh/chị,

Bản thiết kế v7 đã đủ chuỗi từ đầu đến cuối, gồm 159 màn: Thiết lập → Mua → Kho → Bán → Giao → Hoá đơn → Thu tiền → Đối soát → Sổ → Kê khai → Bằng chứng. Để chạy thử, em cần anh/chị quyết 6 việc:

1. **Danh sách hộ chạy thử:** bao nhiêu hộ, ngành gì, doanh thu năm khoảng bao nhiêu? Con số này quyết định mốc thuế và việc có phải dùng hoá đơn máy tính tiền hay không.
2. **Mất mạng:** chỉ cho lưu nháp, đánh dấu "chưa đồng bộ" (thiết kế hiện tại), hay phải bán được cả khi không có mạng?
3. **Nhà cung cấp hoá đơn điện tử:** chọn bên nào cho bản thử? Đây là kết nối bắt buộc duy nhất. Ngân hàng và Zalo OA là tuỳ chọn.
4. **Dữ liệu và AI nước ngoài:** Agent có được gửi dữ liệu của hộ ra máy chủ AI ở nước ngoài không? Theo Luật Bảo vệ dữ liệu cá nhân 91/2025, việc này cần hộ đồng ý riêng và có hồ sơ chuyển dữ liệu ra nước ngoài.
5. **Người phụ trách hỗ trợ tại chỗ:** nhân viên OPC nào ngồi cùng hộ (đăng ký, đếm tồn, eTax)? Lịch hẹn thế nào?
6. **Tên nhà cung cấp:** em đã bỏ hẳn khỏi các màn của hộ theo quyết định của anh/chị. Tên chỉ còn ở mục Kết nối và lúc đăng ký, nơi chủ hộ tự chọn. Anh/chị xác nhận giữ như vậy?

Bản chụp các màn: `apps/app/shots/_v710-nav.png` … `_v751-onboarding.png`.

---

## 3. Gửi BA

**Tiêu đề:** OPC v7 – 5 điểm thiết kế khác BA, nhờ khảo sát và xác nhận

Chào anh/chị,

Thiết kế v7 theo BA ở phần lớn các điểm. Có 5 điểm em làm khác, hoặc cần số liệu khảo sát:

1. **Trả tiền nhà cung cấp:** BA ghi "trả đủ một lần". Thiết kế cho trả nhiều lần, mua chịu có hạn, trả trước một phần. Một lần khách trả cũng gán được cho nhiều hoá đơn, kèm bảng kê gửi khách. Nhờ xác nhận với hộ chạy thử.
2. **Trả hàng tối thiểu:** khách trả hàng và hộ trả hàng cho nhà cung cấp đều đã có màn. Hộ thực tế trả hàng bao lâu một lần?
3. **Chế biến và hạn dùng:** bản thử tắt chế biến, không theo dõi lô. Hạn dùng là tuỳ chọn, OPC báo khi sắp hết hạn. Nhờ khảo sát có bao nhiêu hộ cần chế biến hoặc theo dõi lô.
4. **Vai trò:** chủ hộ; nhân viên bán hàng (tuỳ chọn); kế toán chỉ xem và tải; người giao chỉ là tên trên đơn. Có hộ nào cần thêm vai trò không?
5. **Giao dịch đầu tiên** sau đăng ký là "Bán thử" (không tính doanh thu) hoặc "Nhập một đơn mua". Hộ thường muốn làm việc nào trước?

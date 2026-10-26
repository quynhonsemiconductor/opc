# OPC — Prototype mobile để review proposal

Ngày: 07/10/2026. Bản minh họa UX, không phải ứng dụng vận hành.

## Mở và sử dụng

Mở `index.html` bằng Chrome hoặc Edge, không cần cài thư viện. Dùng màn hình máy tính để thấy đồng thời điện thoại và phần giải thích cho DEV.

- Chọn khung iPhone Dynamic Island, iPhone tai thỏ hoặc Android camera giữa ở đầu trang. Ba khung dùng cùng chức năng responsive Web, không phải ba ứng dụng.
- Chọn **Hành trình demo** bên trái, rồi bấm trong điện thoại. Đổi hành trình sẽ đặt lại dữ liệu.
- Có thể mở từng màn hình SC-01–SC-18. Bên phải có UC, Feature, giá trị giới thiệu và giới hạn cam kết.
- **Đặt lại demo** hoặc tải lại trang để bắt đầu lại. Trên cửa sổ hẹp, chọn màn hình ở phần giải thích bên dưới điện thoại; dùng nút **Thêm** để mở các chức năng.

## Hành trình trình bày

| Hành trình | Cách đi | Điều cần người xem hiểu |
|---|---|---|
| Mua hàng và nhập kho | SC-07: sửa nháp → xác nhận đơn → nhận hàng → gắn chứng từ → ghi tiền trả | Đơn mua có trước tăng tồn. Xác nhận đơn chưa tăng kho. Chỉ hàng thực nhận mới tăng kho; tiền trả theo dõi riêng. Có thể xem đề xuất mua từ SC-02. |
| Bán hàng từ Zalo | SC-11: mở đề xuất → SC-10: kiểm tra và xác nhận → đã giao đủ → mô phỏng kết quả hóa đơn → ghi tiền mặt hoặc SC-12 nhận/liên kết giao dịch mẫu → chủ hộ đóng đơn | Agent đề xuất, chủ hộ xác nhận. Giữ hàng khác trừ kho. Giao hàng, hóa đơn và tiền có trạng thái riêng. Chủ hộ cũng có thể tạo đơn bằng tay. |
| Đóng đơn trước khi giao | SC-10: xác nhận → ghi tiền mặt → đóng đơn → SC-01 → quay lại giao hàng và xử lý hóa đơn | Đóng đơn theo xác nhận đã nhận tiền không tự hoàn tất giao hàng/hóa đơn. Việc còn chờ vẫn hiển thị. |
| Thiếu tồn | SC-10: khách hỏi 10, kho còn 6 → sửa nháp xuống 6 → xác nhận; hoặc mở đơn mua để nhập thêm trước khi xác nhận 10 | Không xác nhận vượt tồn khả dụng, không giao thiếu. Chủ hộ chọn cách xử lý. |
| Tiền về dư | SC-10: xác nhận → SC-12: mô phỏng giao dịch → kiểm tra và liên kết → chủ hộ đóng đơn | Giữ nguyên số thực nhận và ghi chú tiền dư. Không tự tăng giá trị hóa đơn hoặc hoàn tiền. |
| Tổng hợp quý và eTax | SC-15: chọn quý, mở tháng/hóa đơn → kiểm tra dữ liệu → SC-16 hướng dẫn → SC-17 ghi nhận đã gửi trên eTax và bằng chứng | Hóa đơn mua vào/bán ra hiển thị riêng. Thực hiện eTax bên ngoài, chủ hộ cập nhật trên OPC. Không minh họa tính thuế hoặc tự gửi tờ khai. |

## DEV dùng cùng tài liệu nào?

1. [Business Flow v0.3](../03_OPC_Product_Foundation/OPC_BUSINESS_FLOW_EXPLAINER.md): hiểu nghiệp vụ và điểm bắt đầu/kết thúc.
2. [Use Case Catalog v0.8](../03_OPC_Product_Foundation/OPC_USE_CASE_CATALOG.md): kiểm tra hành vi, dữ liệu, trạng thái và ngoại lệ đã chốt.
3. [Screen Plan v0.2](../03_OPC_Product_Foundation/OPC_USER_FLOWS_AND_SCREEN_PLAN.md): đối chiếu SC → UC → Feature.
4. Prototype: review bố cục và thao tác. Nếu có khác biệt, ghi nhận để PO chốt; không dùng prototype ghi đè nghiệp vụ.

## Cần chốt khi review

- Chủ hộ có tìm được việc cần làm và hiểu các trạng thái không?
- Nút xác nhận hàng/tiền có rõ, thao tác bằng tay có dễ không?
- Chọn màn hình và hành trình nào đưa vào proposal; phần nào giới thiệu là dự kiến phát triển?
- Phần thuế/provider nào cần bằng chứng trước khi cam kết? Bố cục chưa được duyệt chỉ là đề xuất UX.

## Giới hạn cần nói rõ

- Không có backend, đăng nhập/phân quyền thật, AI, Zalo, ngân hàng, hóa đơn hoặc eTax thật. Các nút provider chỉ đổi dữ liệu mẫu.
- Một sản phẩm, một đơn mua, một đơn bán và một kho để minh họa. Không chuyển đổi đơn vị. Danh mục khách/NCC chỉ là fixture.
- Dữ liệu ở bộ nhớ của trang; không lưu lâu dài. Tiến trình các quý giữ trong cùng phiên, mất khi reset/tải lại. Không nhập dữ liệu hoặc chứng từ thật.
- Có kiểm tra tồn và chống bấm lặp trong demo; chưa chứng minh concurrency, webhook idempotency, bảo mật hoặc audit bất biến của hệ thống thật.
- Số tiền hóa đơn chỉ minh họa tổng hợp dữ liệu, không phải cơ sở tính thuế đã xác minh. Chưa map trường mẫu tờ khai; chưa có công thức GTGT/TNCN. Bằng chứng eTax do chủ hộ nhập, chưa xác nhận nghĩa vụ đã hoàn thành.
- Đang chọn năm mẫu 2026. Các quy tắc thuế, sửa hóa đơn và khả năng provider vẫn cần xác minh riêng.

Không coi prototype là cam kết toàn bộ ERP. Sau review, PO chốt nội dung proposal trước; tích hợp và triển khai cần đặc tả/kế hoạch kiểm thử tiếp theo.

## Kiểm tra bản prototype

Đã kiểm tra mở 18 màn hình trong Chromium; thao tác nhập kho, xác nhận/giữ hàng, giao đủ, hóa đơn lỗi rồi có kết quả, thu tiền/đóng đơn, đóng trước giao, hủy và giải phóng giữ hàng, nhận dư và ghi chú, tổng quý và bằng chứng eTax. Đã xem hình khung Dynamic Island, tai thỏ và Android; cửa sổ rộng 390 px không tràn ngang. Đây là kiểm tra bản mô phỏng, không phải UAT tích hợp hay kiểm chứng trên thiết bị thật.

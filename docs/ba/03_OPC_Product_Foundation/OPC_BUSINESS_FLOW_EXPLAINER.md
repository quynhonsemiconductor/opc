# OPC — Ba luồng nghiệp vụ đã chốt

**Phiên bản:** 0.3  
**Ngày:** 07/10/2026  
**Product Owner:** Hiếu  
**Trạng thái:** Luồng tổng thể đã chốt; còn đầu vào kế toán/provider trước triển khai thật.

## 1. Mục tiêu và cách đọc

Tài liệu đồng bộ [Use Case Catalog v0.8](OPC_USE_CASE_CATALOG.md) và quyết định PO 07/10/2026, thay phần tương ứng ngày 06/10. Word v1.1/v1.2 giữ nguyên, chưa đồng bộ lượt này; không dùng thay baseline mới.

- **ĐÃ CHỐT:** quyết định product từ PO, dùng để tách Use Case.
- **CẦN XÁC MINH:** kế toán/provider cung cấp căn cứ; quyết định product chưa chứng minh pháp lý hoặc khả năng tích hợp.
- **LÀM SAU / ĐANG PHÁT TRIỂN:** giới hạn proposal do PO chọn; không có nghĩa đã có code.
- **VÍ DỤ:** số liệu để giải thích; ví dụ tiền 8.000đ/10.000đ là cách ghi nhận PO đã chốt.

Chủ hộ có thể nhập, kiểm tra, duyệt và cập nhật bằng tay ở mọi khâu OPC theo quyền. Agent hỗ trợ đọc dữ liệu, kiểm tra, tạo đề xuất và giải thích. Hai cách dùng cùng hồ sơ, quy tắc, trạng thái và lịch sử; không tạo giao dịch trùng.

## 2. Phạm vi và bức tranh tổng thể

Pilot là hộ kinh doanh nhỏ lẻ, tập trung Phân phối, cung cấp hàng hóa; nhập ngành nghề đã đăng ký khi onboarding. Danh sách/quy mô doanh thu còn cần khảo sát. Không chế biến/sản xuất. Một kho chứa nhiều hàng; đơn vị/quy cách do chủ hộ thiết lập, không tự quy đổi. Khách lẻ/doanh nghiệp dùng cùng luồng bán.

| Luồng | Điểm bắt đầu | Kết quả |
|---|---|---|
| 1. Procure-to-Pay — Mua hàng và kho | Mua hàng hoặc phát sinh chi phí | Đơn mua, thực nhận, tăng kho được human xác nhận; truy chứng từ và tiền chi |
| 2. Order-to-Cash — Bán hàng, hóa đơn và tiền | Zalo hoặc chủ hộ nhập yêu cầu | Chủ hộ duyệt, giữ/giao hàng; theo dõi riêng hóa đơn, công nợ và tiền thực nhận |
| 3. Record-to-Tax — Sổ sách và hướng dẫn eTax | Đơn, kho, hóa đơn, tiền và chi phí | Giải thích trường tờ khai và dữ liệu nguồn; lưu kết quả kỳ khi có căn cứ |

Mua hàng → Một kho → Đơn bán → Chủ hộ duyệt → Giữ hàng → Giao trực tiếp.

Đơn, kho, hóa đơn, tiền và chi phí cùng vào sổ/đối soát → hướng dẫn eTax → người dùng thực hiện trên eTax → lưu kết quả kỳ từ nguồn được xác minh. Hóa đơn, giao hàng và thanh toán có trạng thái riêng.

## 3. Luồng 1 — Mua hàng và kho

### 3.1 Quy trình đã chốt

| Bước | Chủ hộ | Agent/OPC | Quy tắc và Feature |
|---|---|---|---|
| 1 | Xác nhận đề xuất mua của Agent hoặc tự tạo/xác nhận đơn | Agent nhận biết ý định mua từ nguồn được phép, hỏi phần thiếu, không tự đặt hàng | Nhà cung cấp trao đổi ngoài OPC, không có bước duyệt; đơn phải có trước tăng tồn; UC-01; F03.01–F03.02 |
| 2 | Mở đơn → “Nhận hàng” → kiểm tra/sửa lượng → “Xác nhận nhập kho” | Mặc định lượng theo đơn, so thực nhận; tăng kho một lần theo số chủ hộ xác nhận | Nhận 18/20 tăng 18, thiếu 2 theo dõi riêng; UC-02; F03.03; F05.02 |
| 3 | Gắn hóa đơn/chứng từ, ghi chi phí nếu có | Điện tử qua provider; viết tay chụp ảnh + nhập tay, OCR sau; lưu nguồn | Happy path mua/bán có hóa đơn; ảnh không tự chứng minh hợp lệ thuế; UC-03/04; F09.04 |
| 4 | Mở đơn → “Ghi nhận đã trả tiền” → phương thức/số tiền/ngày → xác nhận | Agent hỗ trợ đối chiếu, không chuyển tiền | Trả đủ một lần trước hoặc sau nhận hàng; nhận hàng không chứng minh đã trả; UC-05; F03.07; F08.02/09 |

Chưa nhận hàng và chưa trả tiền: chủ hộ được sửa/hủy đơn, lưu lịch sử UC-08. Đã phát sinh hàng hoặc tiền: giữ nguyên giao dịch cũ, xử lý riêng ở refinement sau, ngoài happy path.

### 3.2 Ví dụ

Chị Lan nhận 20 thùng nước từ Minh Phát nhưng chưa nhập đơn OPC. Chị tạo đơn, kiểm đếm rồi xác nhận thực nhận. OPC mới tăng tồn theo lượng chị xác nhận. Nếu nhận 18 thì chỉ tăng 18, còn 2 theo dõi thiếu. Không tăng theo số đặt khi chưa nhận.

### 3.3 Giới hạn proposal

| Nội dung | Quyết định |
|---|---|
| Một kho; nhập mua có đơn và chủ hộ xác nhận | Luồng chính |
| Nhận 12 rồi 8 trên cùng đơn | Cho theo dõi, hiếm, không đưa proposal |
| Trả đủ một lần trước hoặc sau nhận hàng | Luồng chính; ứng trước một phần/trả nhiều lần/mua chịu làm sau |
| Chế biến hàng mua | Ngoài phạm vi |

### 3.4 Đầu vào còn thiếu

| Câu hỏi | Bên xác nhận | Trả lời |
|---|---|---|
| Mốc ghi phải trả/chi phí và bộ trường chứng từ là gì? | Kế toán | Happy path có hóa đơn; rule ghi sổ còn chờ. |
| Hàng mua của pilot có cần lô/hạn dùng không; lưu tại bước nhận nào? | PO khảo sát hộ | |

## 4. Luồng 2 — Bán hàng, hóa đơn và tiền

### 4.1 Quy trình đã chốt

| Bước | Chủ hộ | Agent/OPC | Quy tắc và Feature |
|---|---|---|---|
| 1 | Nhận yêu cầu hoặc nhập tay | Đọc Zalo, nhận diện khách/hàng, báo dữ liệu thiếu | Giữ nguồn yêu cầu; không đoán SKU/giá; F06.01–F06.03 |
| 2 | Thiết lập giá, xem tồn; tự trao đổi/báo giá/báo tồn với khách | Agent chỉ gợi ý, không tự gửi Zalo; OPC kiểm tra giá/tồn | Không giảm giá/chặn hạn mức/nợ quá hạn; F06.03–F06.08 |
| 3 | Duyệt đề xuất Agent hoặc tự tạo/xác nhận đơn | OPC kiểm tra lại tồn trước xác nhận; tạo tay không duyệt thêm | Lượng xác nhận không vượt tồn; thiếu thì sửa lượng hoặc nhập thêm trước xác nhận; UC-12 |
| 4 | Xem hàng dành cho đơn | Giữ đủ sau xác nhận, chống giữ trùng | Không giữ một phần/đơn xác nhận chờ nhập; hủy trước bàn giao giải phóng; UC-13 |
| 5 | Chuẩn bị đủ theo đơn, giao tay rồi bấm “Đã giao” | Lấy lượng từ đơn, trừ kho một lần, lưu chủ hộ/thời gian | Không nhập lại lượng/ảnh bắt buộc hoặc giao từng phần; UC-14/15 |
| 6 | Theo dõi bước hóa đơn được kích hoạt khi đã giao đủ | Gửi/nhận kết quả provider, lỗi vẫn chờ xử lý | Một hóa đơn theo đơn, kế toán/provider xác minh thực thi; UC-16 |
| 7 | Nhập/xác nhận tiền mặt hoặc xem tiền ngân hàng | Nhận giao dịch thật, khớp rule hoặc hỗ trợ tìm đơn | Chưa thu thì pending/công nợ; F08.01, F08.03–F08.07, F08.09 |
| 8 | Tự xử lý tiền dư, ghi chú giải trình | Lưu riêng hóa đơn, thực nhận và chênh lệch | Không tự hoàn/giữ tiền dư cho lần sau; F08.07; F10.02–F10.04 |
| 9 | Xác nhận đề xuất đóng khi đã có tiền thực nhận gắn đơn | Đề xuất đóng, không quyết định thay chủ hộ | Giao/hóa đơn/tiền dư không chặn đóng; UC-22 |

Tiền có thể nhận trước hoặc sau giao. Đơn đóng trước giao vẫn hiển thị và xử lý được giao/hóa đơn còn chờ; không tự đánh dấu các việc đó đã xong.

### 4.2 Một đơn — ba phần theo dõi riêng

| Phần | Đã chốt | Điểm cần nhớ |
|---|---|---|
| Giao hàng | Chủ hộ bấm “Đã giao” nghĩa là giao đủ theo đơn | Không giao thiếu/giao tiếp; không chứng minh tiền/hóa đơn đã xong |
| Hóa đơn | Giao đủ kích hoạt một hóa đơn theo đơn; lỗi vẫn chờ xử lý | Kế toán/provider xác minh thực thi và sửa sai |
| Thanh toán | Tiền mặt nhập tay; ngân hàng tích hợp thật là mục tiêu | Chưa thu thì pending; chênh lệch có số riêng và note |

Đóng đơn đã chốt: có tiền thực nhận gắn đơn → OPC đề xuất → chủ hộ xác nhận. Giao/hóa đơn/tiền dư không chặn đóng; các trạng thái đó vẫn độc lập và còn xử lý được.

### 4.3 Ví dụ

Lan mua 20 thùng nước, khách đặt 10. Agent kiểm tra và tạo đơn chờ duyệt. Chủ hộ duyệt, OPC giữ hàng trong phạm vi tồn. Chủ hộ bàn giao/giao đủ 10: kho giảm đúng thực bàn giao, giao complete, hóa đơn theo đơn được phát hành qua provider. Chưa nhận tiền thì công nợ vẫn mở.

Nếu tồn khả dụng chỉ có 6 nhưng khách hỏi 10: chủ hộ tự trao đổi, sửa đơn tối đa 6; hoặc nhập thêm/cập nhật kho rồi mới xác nhận đơn 10. Không xác nhận 10 rồi giữ/giao 6. Quy tắc này thay thế ví dụ giao thiếu ngày 06/10.

Ví dụ tiền đã chốt: hóa đơn 8.000đ, nhận chuyển khoản 10.000đ. Lưu transaction 10.000đ, liên kết hóa đơn 8.000đ, chênh lệch 2.000đ, note “chuyển dư 2.000đ”. Chủ hộ tự xử lý. Không đổi hóa đơn thành 10.000đ, ghi dư thành doanh thu hoặc tự gửi hoàn tiền.

### 4.4 Hủy và giới hạn proposal

| Trường hợp | Xử lý | Proposal |
|---|---|---|
| Khách báo hủy trước bàn giao | Chủ hộ hủy; dừng và giải phóng hàng giữ | Luồng hỗ trợ |
| Thiếu tồn trước xác nhận | Giảm lượng trong tồn hoặc nhập thêm rồi xác nhận | Không có giao từng phần hoặc đơn xác nhận chờ hàng |
| Tự giao/giao trực tiếp | Chủ hộ cập nhật tay | Luồng chính |
| Kết nối vận chuyển | Nice to have | Tiếp tục phát triển |
| Trả nhiều lần đơn bán | Hiếm, chưa xét hành trình này | Không đưa |
| Hủy sau hóa đơn | Chủ hộ làm thủ công; cần biên bản theo PO; kế toán xác nhận | Đang phát triển |
| Hóa đơn lỗi | UI pending, xử lý với provider | Không tự hoàn thành sai |

Người mua báo hủy, chủ hộ thao tác; chưa có yêu cầu tài khoản người mua. Hàng đã xuất không tự tăng lại kho chỉ vì bấm hủy; nhận hàng trả và điều kiện nhập lại còn cần đặc tả.

### 4.5 Đầu vào còn thiếu

| Câu hỏi | Bên xác nhận | Trả lời |
|---|---|---|
| Phát hành khi giao đủ cần dữ liệu/điều kiện gì; biên bản/thời hạn/quy trình sửa-hủy là gì? | Kế toán/provider | Không còn case giao thiếu. |
| Provider hỗ trợ QR, transaction ID, giao dịch thật và hóa đơn đến đâu; giá/giới hạn/điều kiện chạy thật? | Provider, PO tổng hợp | |
| Giữ có hết hạn không; sửa sau xác nhận/bàn giao/đóng xử lý thế nào? | PO ở bước refinement | Đơn tay xác nhận trực tiếp; đóng theo thực nhận gắn đơn + chủ hộ xác nhận đã chốt. |
| Tự khớp cần kiểm tra gì ngoài mã đơn; tiền thiếu hoặc không rõ đơn xử lý thế nào? | PO/kế toán/provider ở bước Use Case | |

Không hỏi lại các quyết định đã có: một kho, chủ hộ duyệt đơn Agent, ngân hàng tích hợp thật, tiền dư có note và người mua báo hủy.

## 5. Luồng 3 — Sổ sách và hướng dẫn eTax

### 5.1 Quy trình đã chốt

| Bước | Người thực hiện | OPC/Agent hỗ trợ | Kết quả và Feature |
|---|---|---|---|
| 1 | Chủ hộ nhập/xác nhận giao dịch | Nối đơn, kho, hóa đơn, tiền và chi phí | Có nguồn, ngày, actor; tránh nhiều lần ghi bán; F10.01–F10.04 |
| 2 | Chọn quý/năm, bấm tổng để xem hóa đơn theo tháng/ngày | OPC tổng riêng bán ra/mua vào theo ngày lập, truy bản gốc; Agent giải thích nguồn | Happy path có hóa đơn cho mua/bán; tiền thực thu/chi riêng; UC-26; F11.01–02 |
| 3 | Kiểm tra, sửa dữ liệu có căn cứ rồi xác nhận | Lưu lịch sử; sửa sau xác nhận báo cần kiểm tra lại | Không sửa trực tiếp hóa đơn đã phát hành hoặc kết quả eTax cũ; UC-26/28 |
| 4 | Xem hướng dẫn hoặc hỏi Agent | Mẫu đã chọn; hướng dẫn có nguồn sau kế toán xác nhận | Chưa map trường/tính GTGT/TNCN; F11.03–05; UC-27 |
| 5 | Chủ hộ điền/sửa/gửi/nộp trên eTax | Giải thích khi có yêu cầu bổ sung, không thao tác thay | Giữ lịch sử, không tự ký/gửi/nộp; UC-28 |
| 6 | Ghi nhận đã gửi và đính kèm bằng chứng; theo dõi kết quả | API nếu được xác minh; không API chủ hộ cập nhật tay có nhãn nguồn | Đã gửi → chờ cập nhật; không tự suy đã chấp nhận/nộp tiền/hoàn thành; UC-29/30 |

### 5.2 Dữ liệu cần truy lại

| Đối tượng | Nguồn |
|---|---|
| Mua/nhận hàng | Đơn mua, thực nhận human xác nhận, phiếu nhập, chứng từ bên bán |
| Bán/giao | Yêu cầu, đơn đã xác nhận, lượng giao đủ lấy từ đơn, chủ hộ/thời gian xác nhận |
| Hóa đơn | Dữ liệu gửi, mã/trạng thái provider, bản điều chỉnh và lịch sử |
| Tiền/công nợ | Transaction thực tế, mã nguồn, phương thức, đơn liên kết và note lệch |
| Trường tờ khai | Mẫu 01_CNKD_TT40_2026_9172.xlsx đã cung cấp; mapping trường để sau; ý nghĩa/rule cần kế toán xác nhận |
| Kết quả kỳ | Nguồn eTax/provider hoặc phương án đã chốt, ngày và bằng chứng |

Chọn quý của tập hóa đơn theo ngày lập đã chốt; không tự áp cho mọi bút toán sổ. Không lấy thu trừ chi làm doanh thu, không mặc định mua vào được khấu trừ. Hóa đơn điện tử qua provider; ảnh viết tay nhập thủ công, OCR sau. “Một sổ” chưa đủ trường/rule.

### 5.3 Đầu vào chờ

| Câu hỏi/đầu vào | Bên xác nhận | Trả lời |
|---|---|---|
| Mẫu sổ và quy tắc GTGT/TNCN, mẫu tờ khai đã chọn áp dụng ra sao? | Kế toán; PO tổng hợp | Mẫu đã có; chưa map trường theo yêu cầu PO. |
| Có lấy lịch sử/kết quả kỳ/yêu cầu bổ sung eTax không; nguồn và bằng chứng gì? | Provider | |
| Trạng thái sau gửi và bằng chứng đủ để xác nhận từng bước là gì? | Kế toán/provider; PO tổng hợp | Không API thì chủ hộ cập nhật tay kèm bằng chứng đã chốt; chưa chốt hoàn thành kỳ. |

Chưa chốt thuế suất, ngưỡng hay công thức. Không cam kết OPC ký/gửi/nộp thay user. Xem hướng dẫn không tự đóng kỳ.

## 6. Nguồn của các quyết định

| Chủ đề | Quyết định hiện tại | Nguồn |
|---|---|---|
| Agent và thao tác tay | Hỗ trợ; đơn Agent chờ chủ hộ duyệt; tay dùng chung hồ sơ | Chat 06/10, làm rõ câu bán hàng 1–2 gốc |
| Giữ hàng | Sau xác nhận; hủy trước bàn giao giải phóng; trừ theo thực bàn giao | Chat 06/10, làm rõ câu bán hàng 3 |
| Mua/kho | Agent đề xuất hoặc tạo tay; human xác nhận nhập theo thực nhận; trả đủ một lần trước/sau nhận; sửa/hủy khi chưa nhận/chưa trả | Chat PO 07/10; UC-01/02/05/08, thay phần tương ứng 06/10 |
| Khách/giá | Cùng luồng bán, chủ hộ setup giá | Chat 06/10, nhóm bán 1–2 |
| Giao/hóa đơn | Giao đủ bằng “Đã giao”, lượng theo đơn; trừ kho một lần, kích hoạt hóa đơn | Chat PO 07/10 thay case giao thiếu cũ |
| Đóng đơn bán | Có tiền thực nhận gắn đơn, chủ hộ xác nhận; không chặn bởi giao/hóa đơn/tiền dư | Chat PO 07/10; UC-22 |
| Ngân hàng/tiền mặt | Tích hợp thật, map provider; tiền mặt nhập tay | Câu bán 7–8 và chat 06/10 |
| Tiền dư | Ghi transaction và note, user tự xử lý | Câu bán 9 được làm rõ bằng ví dụ 8.000đ/10.000đ |
| Hủy sau hóa đơn | Chủ hộ làm, có biên bản, đang phát triển | Câu bán 10 và chat 06/10 |
| Hóa đơn lỗi | Pending, xử lý với provider | Câu bán 11 gốc |
| Thuế | Mẫu đã chọn; tổng hóa đơn quý/ngày lập, được sửa; đã gửi → chờ kết quả, không API chủ hộ cập nhật | Chat PO 07/10; UC-26–31; rule thuế còn mở |
| Chế biến | Bỏ hoàn toàn, còn ba nghiệp vụ | Quyết định PO 06/10 |

## 7. Đồng bộ và bước tiếp theo

| Tài liệu | Phiên bản | Trạng thái |
|---|---|---|
| BRD OPC Platform | 0.9 | Đồng bộ quyết định PO 07/10; giữ nguồn tỉnh làm bối cảnh |
| Capability Map | 0.6 | Giữ 15 capability; đồng bộ phạm vi mới |
| Feature Catalog | 0.4 | Giữ 94 mã và 9 Service, gồm mục lịch sử/ngoài phạm vi |
| Business Flow Explainer | 0.3 | Ba flow, ví dụ và đầu vào còn mở đồng bộ |
| Use Case Catalog | 0.8 | 33 UC, nguồn quyết định chi tiết |
| OPC_BUSINESS_FLOWS_REVIEW.docx | 1.2 | Chưa đồng bộ 07/10, không dùng thay baseline mới |

Tiếp theo: refine Use Case đã có theo từng slice, xác minh dependency/provider và thiết kế thao tác/màn hình cho phần đủ đầu vào. Chưa tạo SRS/backlog, chưa map trường tờ khai hoặc công thức thuế trong lượt này.

Slide HTML, XML bốn flow, PRD draft và bộ Sales Agent cũ chưa đồng bộ; không dùng làm căn cứ phạm vi hiện tại.

## 8. Tài liệu nguồn

- [BRD OPC Platform](BRD_OPC_PLATFORM.md)
- [Capability Map](OPC_BUSINESS_CAPABILITY_MAP.md)
- [Feature Catalog](OPC_FEATURE_CATALOG.md)
- [Word câu trả lời gốc v1.1](../05_OPC_Presentation/OPC_4_BUSINESS_FLOWS_REVIEW_v1.1.docx)
- [Word hiện tại v1.2](../05_OPC_Presentation/OPC_BUSINESS_FLOWS_REVIEW.docx)
- [Use Case Catalog v0.8](OPC_USE_CASE_CATALOG.md), mục 0, UC-01/02/05/08 và UC-09–31: quyết định PO trong chat 07/10 thay phần tương ứng ngày 06/10. Pháp lý và API cần kế toán/provider xác nhận.

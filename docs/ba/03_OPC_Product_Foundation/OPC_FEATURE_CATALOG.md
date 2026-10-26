# OPC Feature Catalog

**Phiên bản:** 0.4  
**Ngày:** 07/10/2026  
**Trạng thái:** Đồng bộ BRD v0.9, Capability Map v0.6 và Use Case Catalog v0.8; còn đầu vào kế toán/provider và refinement, chưa Dev-ready  
**Product Owner:** Hiếu  
**Nguồn chính:** [BRD OPC Platform](BRD_OPC_PLATFORM.md) và [OPC Business Capability Map](OPC_BUSINESS_CAPABILITY_MAP.md)

Phạm vi hiện tại đồng bộ BRD v0.9, Capability Map v0.6, Business Flow Explainer v0.3 và [Use Case Catalog v0.8](OPC_USE_CASE_CATALOG.md), theo quyết định PO 07/10/2026. Giữ mã Feature để trace; không lấy hành vi cũ về giao thiếu/giảm giá/chặn nợ/đóng kỳ làm đầu vào triển khai. Word, slide/demo, PRD draft và bộ Sales Agent chưa đồng bộ lượt này.

## 1. Mục đích tài liệu

Tài liệu này chuyển 15 capability đang áp dụng thành danh sách Feature và Service của OPC: 14 capability sản phẩm, 1 capability dịch vụ. Ba nghiệp vụ chính là Procure-to-Pay, Order-to-Cash và Record-to-Tax.

Tài liệu trả lời bốn câu hỏi:

1. OPC cần cung cấp những Feature nào?
2. Feature nào thuộc MVP end-to-end?
3. Feature nào chỉ làm ở mức cơ bản trong MVP?
4. Feature nào cần được phân tích tiếp thành Use Case và Workflow?

Tài liệu chưa mô tả màn hình, API, database, User Story hoặc cách tích hợp với Casso và các bên thứ ba.

## 2. Cách đọc Feature Catalog

- **Feature ID** là mã nội bộ được tạo trong tài liệu này để trace. Mã không phải yêu cầu từ tỉnh, Casso hoặc stakeholder.
- **MVP Core** là Feature bắt buộc để hoàn thành ít nhất một luồng nghiệp vụ end-to-end.
- **MVP Basic** là Feature vẫn thuộc MVP nhưng chỉ làm ở mức đủ dùng cho nhóm pilot.
- **Post-MVP** là phần chưa cần để chứng minh MVP.
- **Nguồn** cho biết Feature được tách từ capability nào.
- **Cần chốt** là quyết định business còn ảnh hưởng đến phạm vi hoặc workflow.
- **Làm sau** là chức năng PO chưa đưa vào giai đoạn đầu/proposal hiện tại; **Nice to have** là bổ sung ưu tiên thấp, chưa cam kết tích hợp. **Đang phát triển** là cách ghi trong proposal theo PO, không phải bằng chứng đã có code.
- **Ngoài phạm vi hiện tại** là không triển khai theo quyết định mới, giữ mã để trace. **Cần refinement / ngoài happy path** là nhánh chưa đủ quy tắc, không cam kết Dev-ready hoặc tự đưa vào demo chính.
- Cột **Proposal** dưới đây ghi riêng: **Luồng chính**, **Không đưa**, hoặc **Đang phát triển**. Không đưa vào proposal không tự đồng nghĩa loại khỏi mọi phân tích sản phẩm.

Capability 16 là dịch vụ triển khai. Phần này được tách thành **Service Package**, không được tính như Feature phần mềm.

Giữ mã nhóm cũ để truy lại tham chiếu. Nhóm F04 đã loại khỏi phạm vi. Mã nhóm F11 được giữ nhưng nội dung đã đổi sang hướng dẫn eTax và theo dõi kỳ; tham chiếu F11 trong tài liệu cũ cần kiểm tra lại theo phiên bản này.

## 3. Nguyên tắc xác định Feature

1. Feature phải tạo ra kết quả business mà người dùng nhận biết được.
2. Một Feature có thể dùng nhiều màn hình, workflow hoặc integration.
3. OPC sở hữu Feature và kết quả business, dù một phần thực thi có thể dùng Casso hoặc nhà cung cấp khác.
4. AI chỉ hiểu dữ liệu không cấu trúc, lập phương án và giải thích. Tiền, hàng, giá, thuế và trạng thái dùng rule xác định.
5. Hành động rủi ro phải có quyền, phê duyệt và audit.
6. Agent hỗ trợ; chủ hộ có thể thao tác tay ở mọi khâu trong OPC theo quyền. Hai cách dùng chung dữ liệu, kiểm tra, trạng thái và lịch sử, tránh tạo giao dịch trùng.
7. Agent đề xuất đơn mua/bán → chủ hộ xác nhận; chủ hộ tự tạo/xác nhận không duyệt thêm vòng. Agent không tự đặt hàng hoặc gửi Zalo. Đơn bán xác nhận không vượt tồn, giữ đủ; không giao từng phần.
8. Phần thuế giải thích cách điền tờ khai eTax và truy nguồn dữ liệu; người dùng thực hiện trên eTax. OPC lưu kết quả kỳ theo nguồn/bằng chứng được xác nhận; kết nối lấy dữ liệu eTax còn cần xác minh.
9. Pilot hộ kinh doanh nhỏ lẻ tập trung Phân phối, cung cấp hàng hóa; thu thập ngành nghề đã đăng ký khi onboarding. Danh sách/quy mô doanh thu cần khảo sát. Không có chế biến/sản xuất.
10. Đóng đơn bán khi đã có tiền thực nhận gắn đơn và chủ hộ xác nhận; không chặn bởi giao/hóa đơn/tiền dư, các việc còn chờ vẫn xử lý tiếp.
11. Thuế: chọn quý, tổng hóa đơn bán/mua riêng theo ngày lập, xổ theo tháng/ngày, sửa có lịch sử. Đã gửi → chờ kết quả; không API thì chủ hộ cập nhật kèm bằng chứng. GTGT/TNCN/mapping trường chưa chốt.

## 4. Tổng quan Feature theo Capability

| # | Capability | Loại | Số Feature/Service | Vai trò trong MVP |
|---:|---|---|---:|---|
| 1 | Business Setup and Onboarding | Product | 6 | Đưa hộ đến trạng thái sẵn sàng vận hành. |
| 2 | Master Data and Party Management | Product | 7 | Cung cấp dữ liệu chuẩn dùng chung. |
| 3 | Purchase and Expense Management | Product | 7 | Ghi nhận đầu vào, chi phí và phải trả. |
| 5 | Inventory and Warehouse Management | Product | 8 | Kiểm soát tồn, giữ hàng và biến động kho. |
| 6 | Sales and Order Management | Product | 8 | Chuyển nhu cầu khách hàng thành đơn hợp lệ. |
| 7 | Fulfilment and Delivery | Product | 6 | Chuẩn bị, bàn giao, giao và xử lý thất bại. |
| 8 | Receivables, Payables and Cash Management | Product | 9 | Theo dõi công nợ, tiền ngân hàng và tiền nhập tay. |
| 9 | Invoice and Document Management | Product | 7 | Quản lý hóa đơn, chứng từ và trạng thái. |
| 10 | Books and Reconciliation | Product | 6 | Nối dữ liệu giao dịch và chốt kỳ. |
| 11 | Tax Guidance and Period Tracking | Product | 8 | Hướng dẫn điền eTax, truy dữ liệu nguồn và theo dõi kỳ. |
| 12 | Agent Control Tower | Product | 6 | Theo dõi workflow, ngoại lệ và việc chờ duyệt. |
| 13 | Integration Management | Product | 6 | Quản lý kết nối và lỗi bên thứ ba. |
| 14 | Access, Approval and Audit | Product | 5 | Kiểm soát quyền, phê duyệt và lịch sử. |
| 15 | Business and Program Monitoring | Product | 5 | Theo dõi vận hành và kết quả pilot. |
| 16 | Implementation, Training and Customer Success | Service | 9 | Giúp hộ thiết lập, dùng thật và duy trì sử dụng. |

Tổng cộng: 94 Feature sản phẩm và 9 Service, gồm cả mục làm sau và đang phát triển; không phải tất cả đều thuộc MVP hoặc proposal. Nhóm F04 đã loại; F08.09 được bổ sung để mô tả rõ thu/chi nhập tay.

## 5. Chi tiết Product Feature

### 5.1 Business Setup and Onboarding

| ID | Feature | Kết quả người dùng | Phạm vi | Cần chốt |
|---|---|---|---|---|
| F01.01 | Hồ sơ doanh nghiệp | Chủ hộ nhập thông tin hộ, mã số thuế, ngành nghề đã đăng ký và thông tin vận hành khi onboarding. | MVP Core | Bộ trường chi tiết cần refinement; pilot Phân phối, cung cấp hàng hóa. |
| F01.02 | Thiết lập người dùng ban đầu | Tạo owner operator và người hỗ trợ đầu tiên. | MVP Core | Các vai trò thực tế của hộ pilot. |
| F01.03 | Cấu hình mô hình kinh doanh | Chọn ngành, kênh bán và cấu hình mua hàng/chi phí phù hợp hộ. | MVP Basic | Nhóm pilot và cấu hình được phép thay đổi sau khi vận hành. |
| F01.04 | Nhập dữ liệu ban đầu | Nhập khách hàng, nhà cung cấp, sản phẩm, giá và tồn đầu kỳ. | MVP Core | File mẫu, cách kiểm tra lỗi và trách nhiệm làm sạch dữ liệu. |
| F01.05 | Checklist readiness | Biết còn thiếu dữ liệu, quyền hoặc kết nối nào trước khi chạy thật. | MVP Core | Tiêu chí nào bắt buộc trước giao dịch đầu tiên. |
| F01.06 | Hướng dẫn giao dịch đầu tiên | Người dùng hoàn thành một giao dịch thật theo từng bước. | MVP Basic | Giao dịch đầu tiên là mua hàng hay bán hàng. |

### 5.2 Master Data and Party Management

| ID | Feature | Kết quả người dùng | Phạm vi | Cần chốt |
|---|---|---|---|---|
| F02.01 | Quản lý khách hàng | Lưu khách hàng, thông tin hóa đơn và địa chỉ giao hàng. | MVP Core | Quy tắc nhận diện trùng khách hàng. |
| F02.02 | Quản lý nhà cung cấp | Lưu nhà cung cấp, điều khoản mua và thông tin thanh toán. | MVP Core | Thông tin nào bắt buộc để ghi nhận chi phí và hóa đơn đầu vào. |
| F02.03 | Danh mục sản phẩm và SKU | Quản lý SKU/nhóm hàng; chủ hộ tự thiết lập field đơn vị/quy cách, không tự quy đổi thùng–chai. | MVP Core | Bộ trường và kiểm tra trùng cần refinement. |
| F02.04 | Nguồn mua hàng | Biết sản phẩm được mua từ nhà cung cấp nào và truy lại giao dịch nhập. | MVP Core | Một sản phẩm có nhiều nhà cung cấp và cách chọn nguồn mua của pilot. |
| F02.05 | Bảng giá và giá theo khách hàng | Dùng đúng giá chuẩn hoặc giá riêng đã được duyệt. | MVP Core | Số loại bảng giá của pilot. |
| F02.06 | Điều khoản và hạn mức công nợ — mã lịch sử | Không áp hạn mức/chặn nợ quá hạn trong luồng hiện tại. Theo dõi tiền/công nợ ở F06.06 và F08. | Ngoài phạm vi hiện tại | Không hỏi ngưỡng hoặc mặc định sẽ triển khai; chỉ giữ mã để trace. |
| F02.07 | Lịch sử thay đổi dữ liệu nền | Biết ai đã đổi dữ liệu quan trọng, khi nào và lý do gì. | MVP Core | Thời gian lưu và quyền xem lịch sử. |

### 5.3 Purchase and Expense Management

| ID | Feature | Kết quả người dùng | Phạm vi | Cần chốt |
|---|---|---|---|---|
| F03.01 | Nhu cầu mua hàng | Agent nhận biết ý định mua từ nguồn được phép và đề xuất, hoặc chủ hộ chủ động nhập nhu cầu. | MVP Basic | Nguồn/kênh phát hiện ý định cần refinement; không mặc định tự giám sát mọi trao đổi. |
| F03.02 | Đơn mua hàng | Agent đề xuất → chủ hộ xác nhận, hoặc chủ hộ tự tạo/xác nhận; nhà cung cấp không duyệt trên OPC. Chưa nhận và chưa trả được sửa/hủy có lịch sử. | MVP Core | Sau phát sinh hàng/tiền xử lý riêng, ngoài happy path; không xóa giao dịch cũ. |
| F03.03 | Nhận hàng theo đơn mua | Bấm “Nhận hàng”, kiểm tra/sửa lượng mặc định theo đơn, “Xác nhận nhập kho” tăng đúng thực nhận một lần. Nhận 18/20 tăng 18, thiếu 2 theo dõi riêng. | MVP Core | Đã chốt; nhận nhiều lần là nhánh hiếm, không đưa proposal. |
| F03.04 | Trả hàng và chênh lệch mua | Xử lý thiếu, thừa, hỏng hoặc trả nhà cung cấp. | MVP Basic | Các lý do và bước duyệt. |
| F03.05 | Ghi nhận chi phí không qua kho | Lưu chi phí vận hành không tạo tồn kho. | MVP Core | Nhóm chi phí dùng cho pilot. |
| F03.06 | Chứng từ đầu vào của giao dịch mua | Gắn hóa đơn hoặc chứng từ với đơn mua và chi phí. | MVP Core | Chứng từ nào được chấp nhận khi chưa có hóa đơn điện tử. |
| F03.07 | Khoản chi và phải trả nhà cung cấp | Chủ hộ ghi đã trả tiền, phương thức, số tiền/ngày và xác nhận; trả đủ một lần trước hoặc sau nhận hàng. Agent hỗ trợ đối chiếu, không chuyển tiền. | MVP Core | Rule ghi phải trả chờ kế toán; ứng trước một phần/trả nhiều lần làm sau. |

### 5.4 Production, Batch and Traceability

**Đã loại khỏi phạm vi theo quyết định PO ngày 06/10/2026.** Các mã F04.01–F04.05 không còn là Feature triển khai. Giữ số mục chỉ để truy lại tài liệu cũ; không đổi mã các nhóm còn lại.

### 5.5 Inventory and Warehouse Management

| ID | Feature | Kết quả người dùng | Phạm vi | Cần chốt |
|---|---|---|---|---|
| F05.01 | Tồn đầu kỳ | Ghi nhận lượng hàng bắt đầu sử dụng OPC. | MVP Core | Cách kiểm đếm và người xác nhận số đầu kỳ. |
| F05.02 | Sổ biến động kho | Mọi nhập, xuất, giữ, trả và điều chỉnh đều truy vết được. | MVP Core | Không. |
| F05.03 | Tồn thực tế, tồn giữ và tồn khả dụng | Hệ thống tính đúng lượng có thể bán. | MVP Core | Không. Dùng rule xác định. |
| F05.04 | Giữ và giải phóng hàng | Xác nhận đơn không vượt tồn khả dụng, giữ đủ một lần; hủy trước bàn giao giải phóng. Không giữ một phần/chờ nhập thêm sau xác nhận. | MVP Core | Hết hạn giữ/sửa đơn đã xác nhận cần refinement; không tự đặt thời hạn. |
| F05.05 | Xuất kho khi bàn giao | Chủ hộ bấm “Đã giao” đủ theo đơn; trừ lượng đơn một lần và ghi lịch sử. | MVP Core | Chi tiết thao tác đồng thời/retry cần đặc tả; không nhập lại lượng giao. |
| F05.06 | Trả hàng và nhập lại | Nhập lại hàng khi đạt điều kiện kiểm tra. | MVP Basic | Điều kiện hàng được nhập lại. |
| F05.07 | Kiểm kê và điều chỉnh | Ghi nhận chênh lệch kho và yêu cầu duyệt trước khi điều chỉnh. | MVP Basic | Tần suất và ngưỡng duyệt. |
| F05.08 | Một kho chứa nhiều hàng | Quản lý các mặt hàng trong một kho của hộ. | MVP Basic | Đã chốt một kho; không yêu cầu nhiều kho/vị trí giai đoạn đầu. |

### 5.6 Sales and Order Management

| ID | Feature | Kết quả người dùng | Phạm vi | Cần chốt |
|---|---|---|---|---|
| F06.01 | Tiếp nhận yêu cầu bán | Khách lẻ/doanh nghiệp dùng cùng luồng; nhận Zalo hoặc chủ hộ nhập tay. Người mua báo hủy, chủ hộ thao tác. | MVP Core | Các kênh kết nối khác; dữ liệu người mua cho hóa đơn do kế toán xác nhận. |
| F06.02 | AI đọc yêu cầu khách hàng | Nhận diện khách, sản phẩm, số lượng, ngày giao và thông tin còn thiếu. | MVP Core | Ngưỡng tin cậy để tự đi tiếp. |
| F06.03 | Làm rõ thông tin thiếu | Agent hỏi chủ hộ/chỉ rõ cần hỏi gì; chủ hộ tự trao đổi với khách. | MVP Core | Không tự gửi Zalo; chi tiết nội dung cần refinement. |
| F06.04 | Báo giá | Chủ hộ báo giá/báo tồn cho khách; Agent hỗ trợ từ dữ liệu chuẩn. | MVP Core | Không có quyền Agent tự gửi; chưa mặc định workflow báo giá riêng bắt buộc. |
| F06.05 | Kiểm tra giá | Áp dụng giá do chủ hộ thiết lập; không làm giảm giá hoặc approval giảm giá. | MVP Core | Số bảng giá/giá riêng theo khách cần refinement, không hỏi ngưỡng giảm giá. |
| F06.06 | Theo dõi đơn chờ thanh toán/công nợ | Đơn chưa đóng còn theo dõi chờ thanh toán; hiển thị tiền thực nhận riêng. Không chặn theo hạn mức/nợ quá hạn. | MVP Core | Mốc ghi nhận sổ chờ kế toán; không tự coi trạng thái đơn là số dư kế toán. |
| F06.07 | Tạo, xác nhận và đóng đơn bán | Agent đề xuất → chủ hộ duyệt; tạo tay → xác nhận không duyệt thêm. Có tiền thực nhận gắn đơn → đề xuất đóng → chủ hộ xác nhận. | MVP Core | Giao/hóa đơn/tiền dư không chặn đóng; việc còn chờ vẫn xử lý tiếp. Sửa sau xác nhận/đóng cần refinement; hủy sau hóa đơn đang phát triển. |
| F06.08 | Kiểm tra tồn trước xác nhận đơn | Lượng xác nhận không vượt tồn khả dụng. Thiếu thì chủ hộ giảm lượng hoặc nhập thêm trước xác nhận. | MVP Core | Không giao/giữ một phần hoặc đơn xác nhận chờ nhập thêm; kiểm tra tồn lại khi xác nhận để chống xung đột. |

### 5.7 Fulfilment and Delivery

| ID | Feature | Kết quả người dùng | Phạm vi | Cần chốt |
|---|---|---|---|---|
| F07.01 | Danh sách chuẩn bị hàng để giao | Biết đơn đã xác nhận nào cần lấy hàng, kiểm đếm và đóng gói. | MVP Core | Cách ưu tiên đơn. |
| F07.02 | Chuẩn bị theo đơn đã xác nhận | Chủ hộ chuẩn bị theo lượng đơn; không yêu cầu nhập lại lượng chuẩn bị trong luồng đơn giản. | MVP Core | Lô/hạn dùng cần khảo sát; không tự thêm quét mã/bước duyệt. |
| F07.03 | Phương thức giao và kết nối vận chuyển | Chủ hộ chủ yếu giao trực tiếp; kết nối đơn vị vận chuyển là bổ sung. | Nice to have | Proposal ghi tiếp tục phát triển phần kết nối; chưa chọn provider hoặc cam kết tích hợp. |
| F07.04 | Bàn giao và xuất kho | Bấm “Đã giao” lấy lượng từ đơn, trừ kho một lần, lưu chủ hộ/thời gian; không bắt ảnh hoặc nhập lại lượng. | MVP Core | Retry/thao tác đồng thời cần đặc tả. |
| F07.05 | Theo dõi kết quả giao | Chưa giao → đã giao đủ; không giao thiếu/giao tiếp. Theo dõi riêng tiền/hóa đơn kể cả đơn đã đóng. | MVP Core | Giao thất bại cần refinement; không tự đóng đơn chỉ vì đã giao. |
| F07.06 | Xử lý giao thất bại và hoàn hàng | Nhánh sau giao xử lý riêng, chưa mô tả hành trình chi tiết; không đưa lại giao từng phần. | Cần refinement / ngoài happy path | Hủy sau hóa đơn proposal ghi đang phát triển; chứng từ/tiền/kho cần xác minh. |

### 5.8 Receivables, Payables and Cash Management

| ID | Feature | Kết quả người dùng | Phạm vi | Cần chốt |
|---|---|---|---|---|
| F08.01 | Quản lý khoản phải thu | Theo quyết định PO, giao hàng chưa thu tiền thì ghi công nợ; nhận và phân bổ tiền thì giảm số còn nợ. | MVP Core | Kế toán xác nhận mốc giao và căn cứ ghi nhận; xử lý ứng trước còn cần chốt. |
| F08.02 | Quản lý khoản phải trả | Liên kết mua với tiền chi; chủ hộ ghi trả đủ một lần trước hoặc sau nhận hàng. | MVP Core | Mốc ghi sổ chờ kế toán; ứng trước một phần/trả nhiều lần/mua chịu làm sau. |
| F08.03 | Yêu cầu thanh toán và QR | Tạo thông tin thanh toán gắn với giao dịch. | MVP Core | Provider, ngân hàng và loại tài khoản được hỗ trợ. |
| F08.04 | Nhận giao dịch ngân hàng | Tích hợp thật để nhận giao dịch và số tiền thực tế, lưu nguồn/mã giao dịch. | MVP Core | Map khả năng provider/ngân hàng, dữ liệu và điều kiện chạy thật; mục tiêu tích hợp không phải năng lực đã kiểm chứng. |
| F08.05 | Chống giao dịch trùng | Webhook hoặc giao dịch gửi lại không tạo kết quả trùng. | MVP Core | Không. |
| F08.06 | Khớp tiền tự động | Dùng quy tắc xác định để gắn giao dịch tiền vào đúng đơn, hóa đơn hoặc công nợ; thiếu căn cứ thì chuyển người dùng xử lý. | MVP Core | Tiêu chí khớp ngoài mã đơn và giao dịch tiền; không tự giảm nợ khi chưa xác định đúng hồ sơ. |
| F08.07 | Phân bổ thủ công và ghi chú tiền chênh lệch | Chủ hộ tìm đơn, xác nhận liên kết tiền; ghi đúng tiền thực nhận và note giải trình khoản dư. Ví dụ hóa đơn 8.000đ, nhận 10.000đ, note dư 2.000đ. | MVP Core | Cách xử lý tiền thiếu/không rõ nguồn và quyền sửa note. Chủ hộ tự xử lý dư; không chốt tự hoàn hoặc giữ cho đơn sau. |
| F08.08 | Trả nhiều lần và hoàn tiền | Theo dõi các nhánh thanh toán nhiều lần hoặc hoàn khi được triển khai. | Làm sau | Trả nhiều lần là nhánh hiếm không xét proposal; hoàn sau hủy hóa đơn đang phát triển. Không bỏ qua ghi nhận tiền thực tế thiếu/dư. |
| F08.09 | Thu và chi nhập tay | Chủ hộ ghi tiền mặt hoặc giao dịch thủ công, gắn chứng từ và phân bổ theo quyền. Cùng một giao dịch không được ghi lại khi dữ liệu ngân hàng về. | MVP Core | Trường bắt buộc, quyền sửa/duyệt và cách đối chiếu. UI có thể chọn sẵn tiền mặt theo ý PO; phải nhập/xác nhận tiền thực nhận mới giảm nợ. |

### 5.9 Invoice and Document Management

| ID | Feature | Kết quả người dùng | Phạm vi | Cần chốt |
|---|---|---|---|---|
| F09.01 | Chuẩn bị dữ liệu hóa đơn bán ra | Bấm “Đã giao” đủ theo đơn kích hoạt một hóa đơn theo đơn; không có giao thiếu. | MVP Core | Kế toán/provider xác minh dữ liệu và thực thi trước chạy thật, không phải xác nhận pháp lý. |
| F09.02 | Phát hành và theo dõi hóa đơn | Hóa đơn điện tử qua provider; theo dõi thành công/chờ/lỗi. Đơn đóng không tự làm hóa đơn thành công. | MVP Core | Provider/loại hóa đơn/quyền thực thi cần xác minh; hóa đơn lỗi không chặn đóng theo thực nhận + chủ hộ xác nhận. |
| F09.03 | Gửi hóa đơn cho khách hàng | Khách nhận được hóa đơn qua kênh đã chọn. | MVP Basic | Kênh gửi và bằng chứng đã gửi. |
| F09.04 | Tiếp nhận hóa đơn và chứng từ đầu vào | Hóa đơn điện tử qua provider; chứng từ viết tay chụp ảnh và nhập tay. OCR làm sau. | MVP Core | Bộ trường/nguồn provider cần refinement; không coi ảnh là chứng từ thuế hợp lệ mặc định. |
| F09.05 | Kiểm tra hóa đơn với giao dịch | So khớp hóa đơn với đơn, giao nhận và thanh toán liên quan. | MVP Core | Mức sai lệch được chấp nhận. |
| F09.06 | Hủy, thay thế và điều chỉnh hóa đơn | Chủ hộ xử lý thủ công khi người mua báo hủy; có biên bản theo yêu cầu PO và giữ lịch sử. | Đang phát triển | Proposal ghi đang phát triển; kế toán xác nhận biên bản, thời hạn và quy trình sửa/hủy. Không sửa trực tiếp dữ liệu hóa đơn cũ. |
| F09.07 | Kho tài liệu và bằng chứng | Lưu và tìm lại hóa đơn, chứng từ và file liên quan. | MVP Basic | Loại file, dung lượng và thời gian lưu. |

### 5.10 Books and Reconciliation

| ID | Feature | Kết quả người dùng | Phạm vi | Cần chốt |
|---|---|---|---|---|
| F10.01 | Sổ giao dịch nghiệp vụ | Ghi doanh thu, chi phí, công nợ và dòng tiền theo nguồn/rule được xác nhận. | MVP Core | Mẫu sổ/mốc ghi chờ kế toán. Tập hóa đơn xem theo quý F11.02 đã chốt dùng ngày lập, không tự áp cho mọi bút toán. |
| F10.02 | Liên kết chứng từ end-to-end | Truy từ đơn, kho, hóa đơn, tiền đến bản ghi sổ và ngược lại. | MVP Core | Không. |
| F10.03 | Đối soát doanh thu và chi phí | Phát hiện giao dịch thiếu, trùng hoặc mâu thuẫn. | MVP Core | Quy tắc và mức sai lệch. |
| F10.04 | Đối soát phải thu và phải trả | Giải thích chênh lệch giữa công nợ và thanh toán. | MVP Core | Quy tắc xử lý số dư nhỏ. |
| F10.05 | Hàng đợi ngoại lệ kế toán | Kế toán hoặc người có quyền xử lý từng vấn đề có bằng chứng. | MVP Core | SLA và người chịu trách nhiệm. |
| F10.06 | Khóa và mở lại kỳ | Ngăn thay đổi dữ liệu đã chốt; mở lại phải được duyệt và audit. | MVP Core | Điều kiện khóa, mở lại và người duyệt. |

### 5.11 Tax Guidance and Period Tracking

Người dùng điền/sửa/gửi/nộp trên eTax. OPC tổng hợp hóa đơn theo quý, giải thích dữ liệu nguồn và theo dõi tiến trình. PO đã chọn mẫu 01_CNKD_TT40_2026_9172.xlsx; kế toán còn xác minh áp dụng/GTGT/TNCN. Chưa map trường, tự tính thuế/điền draft; OPC không ký/gửi/nộp thay chủ hộ.

| ID | Feature | Kết quả người dùng | Phạm vi | Cần chốt |
|---|---|---|---|---|
| F11.01 | Chọn quý và theo dõi kỳ kê khai | Chủ hộ chọn quý/năm; pilot Phân phối, cung cấp hàng hóa. | MVP Core | Nghĩa vụ/hạn thực tế cần kế toán xác minh; không tự suy chế độ thuế từ doanh thu. |
| F11.02 | Tổng hợp và kiểm tra hóa đơn quý | Tổng riêng bán ra/mua vào theo ngày lập; bấm tổng xổ theo tháng/ngày, mở hóa đơn. Happy path mua/bán có hóa đơn; tiền thực thu/chi riêng. | MVP Core | Bộ trường/cách lấy giá trị trước-sau thuế/điều chỉnh cần kế toán; không lấy thu trừ chi làm doanh thu hoặc mặc định khấu trừ. |
| F11.03 | Mẫu tờ khai và hướng dẫn đã xác nhận | Lưu mẫu PO đã chọn, phiên bản, nguồn và nội dung được xác nhận. | MVP Core | Mẫu đã có; kế toán xác minh áp dụng. Mapping trường để sau theo PO. |
| F11.04 | Giải thích trường và dữ liệu nguồn | Biết mỗi ô có nghĩa gì, cách điền, cần dữ liệu nào, hình thành từ giao dịch/chứng từ nào và tìm ở đâu trong OPC. | MVP Core | Bảng trường → dữ liệu nguồn → cách hình thành do kế toán xác nhận; chưa tự điền số hay tính thuế. |
| F11.05 | Hỗ trợ hỏi đáp khi điền eTax | Agent giải thích theo mẫu đã xác nhận và dữ liệu có nguồn; chủ hộ tự xem hướng dẫn và dữ liệu, thiếu thì được chỉ rõ cần bổ sung gì. | MVP Core | Nội dung hỏi đáp, nguồn trả lời và cách báo thiếu căn cứ. |
| F11.06 | Hỗ trợ sửa hoặc bổ sung | Cho sửa dữ liệu quý có lịch sử; sửa sau xác nhận báo cần kiểm tra lại. Không sửa trực tiếp hóa đơn phát hành hoặc kết quả kê khai cũ; chủ hộ sửa trên eTax. | MVP Core | Rule nguồn/sổ khóa cần kế toán; không tự thêm khóa dữ liệu chuẩn bị kê khai. |
| F11.07 | Theo dõi tiến trình kê khai | Chuẩn bị → kiểm tra → thực hiện eTax → đã gửi → chờ cập nhật kết quả; hiển thị nguồn và thời điểm. | MVP Core | API/provider và các trạng thái sau gửi cần xác minh; không tự suy đã chấp nhận/nộp tiền. |
| F11.08 | Ghi nhận đã gửi và lưu bằng chứng | Không có API thì chủ hộ cập nhật kèm bằng chứng, nhãn “Chủ hộ xác nhận — chưa đối chiếu qua eTax”; lưu đúng hộ/quý. | MVP Core | Bộ trường/bằng chứng đủ và điều kiện hoàn thành nghĩa vụ còn mở; không tự đóng kỳ. |

### 5.12 Agent Control Tower

| ID | Feature | Kết quả người dùng | Phạm vi | Cần chốt |
|---|---|---|---|---|
| F12.01 | Danh sách workflow | Thấy workflow đang chạy, hoàn thành, chờ hoặc bị chặn. | MVP Core | Bộ lọc ưu tiên cho mobile. |
| F12.02 | Chi tiết kế hoạch và bằng chứng của Agent | Biết Agent hiểu gì, dùng dữ liệu nào và định làm gì. | MVP Core | Mức giải thích cần hiển thị. |
| F12.03 | Hàng đợi ngoại lệ | Tập trung vấn đề cần người dùng xử lý. | MVP Core | Mức độ ưu tiên và SLA. |
| F12.04 | Điều khiển workflow và xử lý bằng tay | Chủ hộ duyệt, từ chối, sửa, dừng, tiếp tục hoặc thực hiện từng bước bằng tay trên cùng hồ sơ; dùng chung kiểm tra và lịch sử. | MVP Core | Hành động được chạy lại, quyền và cách xử lý thao tác đồng thời. |
| F12.05 | Timeout, retry và escalation | Workflow không bị treo im lặng và có hướng xử lý. | MVP Core | Chính sách theo từng loại bước. |
| F12.06 | Thông báo việc cần làm | Người dùng nhận đúng cảnh báo và mở được vào việc cần xử lý. | MVP Basic | Kênh thông báo ngoài hệ thống. |

### 5.13 Integration Management

| ID | Feature | Kết quả người dùng | Phạm vi | Cần chốt |
|---|---|---|---|---|
| F13.01 | Danh mục và thiết lập connector | Chọn và cấu hình kết nối theo use case. | MVP Core | Provider dùng cho từng use case. |
| F13.02 | Consent, quyền và vòng đời token | Biết ai đã cấp quyền, quyền gì và khi nào hết hạn. | MVP Core | Cách thu hồi quyền và dữ liệu sau thu hồi. |
| F13.03 | Trạng thái kết nối và đồng bộ | Thấy nguồn, lần cập nhật gần nhất và lỗi; biết dữ liệu được đồng bộ hay nhập tay. | MVP Core | SLA provider; nguồn eTax phải xác minh trước khi cam kết đồng bộ. |
| F13.04 | Webhook idempotency | Sự kiện gửi lại không tạo giao dịch hoặc trạng thái trùng. | MVP Core | Không. |
| F13.05 | Retry, fallback và xử lý thủ công | Kết nối lỗi không làm mất sự kiện hoặc tự hoàn thành sai. | MVP Core | Phương án fallback theo từng connector. |
| F13.06 | Theo dõi usage và chi phí | PO biết số lượt dùng và chi phí theo hộ hoặc use case. | MVP Basic | Mô hình giá và dữ liệu usage provider cung cấp. |

### 5.14 Access, Approval and Audit

| ID | Feature | Kết quả người dùng | Phạm vi | Cần chốt |
|---|---|---|---|---|
| F14.01 | Vai trò và quyền truy cập | Chỉ đúng người được xem hoặc thực hiện hành động. | MVP Core | Bộ vai trò của hộ pilot và đội hỗ trợ. |
| F14.02 | Chính sách phê duyệt | Chủ hộ xác nhận đơn Agent đề xuất; tự tạo đơn không duyệt thêm. Thiếu tồn không được duyệt để vượt tồn. | MVP Core | Quyền điều chỉnh kho/chứng từ cần refinement; không giảm giá/chặn nợ quá hạn, không tự xác nhận thuế. |
| F14.03 | Nhiệm vụ phê duyệt | Người duyệt thấy dữ liệu bắt buộc, quyết định và ghi lý do. | MVP Core | SLA và người thay thế khi quá hạn. |
| F14.04 | Audit log chỉ ghi thêm | Lưu actor, nguồn, thời gian, dữ liệu trước sau và lý do. | MVP Core | Thời gian lưu. |
| F14.05 | Timeline và xuất lịch sử | Tra cứu được toàn bộ hành trình của giao dịch hoặc workflow. | MVP Core | Định dạng xuất và quyền tải xuống. |

### 5.15 Business and Program Monitoring

| ID | Feature | Kết quả người dùng | Phạm vi | Cần chốt |
|---|---|---|---|---|
| F15.01 | Dashboard vận hành của chủ hộ | Thấy đơn, tồn, tiền, công nợ, hóa đơn, thuế và việc cần làm. | MVP Core | Bộ KPI tối thiểu trên mobile. |
| F15.02 | Theo dõi onboarding và first value | Biết hộ đã thiết lập, kết nối và tạo giao dịch thật chưa. | MVP Core | Định nghĩa first value. |
| F15.03 | Theo dõi kỳ thuế đầu tiên | Thấy tiến trình chuẩn bị/kiểm tra/thực hiện eTax/đã gửi/chờ kết quả và bằng chứng có nguồn. | MVP Core | Trạng thái sau gửi/hoàn thành còn mở; không tự đánh dấu đã nộp thuế. |
| F15.04 | Theo dõi adoption 30/90 ngày | Đo hộ còn sử dụng và Feature nào đang được dùng. | MVP Basic | Chỉ số active và mục tiêu pilot. |
| F15.05 | Báo cáo tổng hợp chương trình | PM thấy kết quả pilot mà không lộ dữ liệu chi tiết của từng hộ. | MVP Basic | Chỉ số, phân quyền và nguyên tắc ẩn dữ liệu. |

## 6. Service Package từ Capability 16

Các mục dưới đây là dịch vụ OPC phải cung cấp khi triển khai pilot. Đây không phải Feature phần mềm.

| ID | Dịch vụ | Kết quả bàn giao | Thời điểm | Cần chốt |
|---|---|---|---|---|
| S16.01 | Khảo sát readiness | Có hiện trạng, dữ liệu, thiết bị, kết nối và khoảng trống của hộ. | Trước cấu hình | Bộ câu hỏi và tiêu chí đạt. |
| S16.02 | Thiết kế cấu hình vận hành | Có cấu hình phù hợp ngành, nguồn hàng và quy trình của hộ. | Trước onboarding | Phần nào chuẩn hóa, phần nào cho phép riêng theo hộ. |
| S16.03 | Chuẩn bị và nhập dữ liệu | Dữ liệu ban đầu được làm sạch, nhập và xác nhận. | Onboarding | Ai chịu trách nhiệm chất lượng dữ liệu. |
| S16.04 | Hỗ trợ kết nối | Các connector cần thiết được thiết lập và kiểm tra. | Onboarding | Phạm vi hỗ trợ với từng provider. |
| S16.05 | Đào tạo theo vai trò | Owner, người vận hành và kế toán biết phần việc của mình. | Trước go-live | Hình thức, tài liệu và tiêu chí hoàn thành. |
| S16.06 | Hỗ trợ giao dịch thật đầu tiên | Hộ hoàn thành giao dịch end-to-end đầu tiên. | Go-live | Giao dịch chuẩn dùng để nghiệm thu. |
| S16.07 | Đồng hành kỳ thuế đầu tiên | Hộ biết cách điền eTax, kiểm tra nguồn dữ liệu và lưu kết quả kỳ trong OPC theo phương án được xác nhận. | Kỳ thuế đầu | Ranh giới hỗ trợ, trách nhiệm kế toán và cách xác nhận kết quả ngoài OPC. |
| S16.08 | Helpdesk và escalation | Vấn đề có kênh tiếp nhận, SLA, owner và cách escalation. | Sau go-live | Giờ hỗ trợ, SLA và mức độ ưu tiên. |
| S16.09 | Review 30/90 ngày và báo cáo pilot | Có dữ liệu adoption, khó khăn và đề xuất trước khi mở rộng. | Sau go-live | Chỉ số thành công và mẫu báo cáo. |

## 7. Quan hệ giữa các Feature

### 7.1 Procure-to-Pay

`Agent đề xuất nhu cầu hoặc chủ hộ tự tạo → Chủ hộ xác nhận đơn mua → Nhận hàng, kiểm tra/sửa lượng → Xác nhận nhập kho → Gắn chứng từ → Ghi khoản chi và đối chiếu`. Trả đủ một lần có thể trước hoặc sau nhận hàng. Chưa nhận/chưa trả được sửa/hủy có lịch sử.

### 7.2 Order-to-Cash

`Zalo → Agent đề xuất → chủ hộ duyệt` hoặc `chủ hộ tự tạo → xác nhận`; kiểm tra khách/giá/tồn → giữ đủ → chuẩn bị → chủ hộ bấm “Đã giao” đủ → trừ kho một lần, kích hoạt hóa đơn. Tiền có thể trước/sau giao: thực nhận gắn đơn → đề xuất đóng → chủ hộ xác nhận.

Agent không tự gửi Zalo. Không giảm giá/chặn nợ quá hạn hoặc xác nhận vượt tồn/giao từng phần. Giao/hóa đơn/tiền dư không chặn đóng; đơn đóng vẫn theo dõi và xử lý giao/hóa đơn còn chờ. Thu thực tế không đồng nghĩa doanh thu hóa đơn.

### 7.3 Record-to-Tax

`Thông tin onboarding → Chọn quý/năm → Tổng riêng hóa đơn bán/mua theo ngày lập → Xổ theo tháng/ngày, kiểm tra/sửa có lịch sử → Hướng dẫn → Chủ hộ thực hiện trên eTax → Ghi nhận đã gửi kèm bằng chứng → Chờ cập nhật kết quả`. Không API thì chủ hộ cập nhật tay có nhãn nguồn. Mẫu đã có; GTGT/TNCN/mapping trường và bước sau gửi còn mở.

### 7.4 Năng lực dùng chung

Các Feature của Agent Control Tower, Integration Management, Access, Approval and Audit và Monitoring hỗ trợ cả ba chuỗi trên. Chủ hộ có thể thao tác tay trong mọi khâu OPC theo quyền; Agent hỗ trợ trên cùng hồ sơ.

## 8. Đề xuất thứ tự phân tích và build MVP

Feature Catalog không đề xuất build toàn bộ module cùng lúc. Nên đi theo vertical slice:

1. **Slice 0 – Static onboarding demo:** trình bày hành trình thiết lập, kết nối và readiness bằng dữ liệu mô phỏng.
2. **Slice 1 – Foundation:** hồ sơ, người dùng, dữ liệu nền, quyền, audit và tồn đầu kỳ.
3. **Slice 2 – Source-to-Stock:** mua hàng, nhận hàng, chi phí, phải trả và nhập kho; không có chế biến.
4. **Slice 3 – Order-to-Cash:** Zalo → Agent đề xuất → chủ hộ duyệt, hoặc tự tạo/xác nhận; kiểm tra giá/tồn, giữ/giao đủ, hóa đơn, thực nhận gắn đơn và chủ hộ xác nhận đóng.
5. **Slice 4 – Record-to-Tax:** sổ/đối soát, chọn quý/tổng riêng hóa đơn bán/mua theo ngày lập, kiểm tra/sửa, hướng dẫn theo mẫu và ghi nhận đã gửi/chờ kết quả có nguồn; quy tắc thuế cần xác minh.
6. **Slice 5 – Pilot operations:** connector thật, dashboard chương trình, service package và đo adoption.

Mỗi slice phải dùng chung dữ liệu, quyền, audit và trạng thái. Không tạo các demo rời nhau rồi nối lại sau.

## 9. Các quyết định cần chốt

| # | Quyết định | Ảnh hưởng chính | Có chặn Feature Catalog không? |
|---:|---|---|---|
| 1 | Với một kho đã chốt, mặt hàng pilot có cần theo dõi lô/hạn dùng không? | Nhận hàng, chuẩn bị hàng và kiểm kê. | Không chặn danh sách; cần xác nhận trước thiết kế dữ liệu hàng. |
| 2 | Danh sách pilot và khoảng doanh thu theo tháng cụ thể là gì? | F01.01, F01.03 và F11. | Ngành Phân phối, cung cấp hàng hóa đã chốt; chi tiết khảo sát/xác minh còn cần. |
| 3 | Ngoài Zalo có nhận đơn từ kênh nào? | F06.01 và thiết kế integration. | Không; Zalo là kênh bắt buộc hiện tại. |
| 4 | Chi tiết giao thất bại/hoàn sau giao xử lý thế nào? | F07.03 đến F07.06. | Giao đủ bằng “Đã giao”, lấy lượng từ đơn, lưu chủ hộ/thời gian đã chốt; không hỏi lại nhập lượng/ảnh bắt buộc. |
| 5 | Bộ vai trò và ngưỡng phê duyệt của pilot là gì? | F14.01 đến F14.03 và mọi ngoại lệ. | Có, trước workflow chi tiết. |
| 6 | Mẫu sổ, quy tắc GTGT/TNCN và mẫu tờ khai đã chọn áp dụng thế nào? | F10 và F11. | Mẫu đã có; kế toán xác minh. Mapping trường để sau theo PO. |
| 7 | Provider nào cho ngân hàng/hóa đơn, có API eTax nào? | F08, F09, F11.07–F11.08 và F13. | Chặn cam kết tích hợp; fallback chủ hộ cập nhật kèm bằng chứng đã chốt. |
| 8 | Mức hoạt động khi mất mạng của responsive Web? | Các thao tác bán hàng và đồng bộ. | Có, trước kiến trúc MVP. |
| 9 | Chỉ số thành công và SLA hỗ trợ pilot? | F15 và Service Package. | Có, trước kế hoạch pilot. |
| 10 | Kế toán/provider xác nhận phát hành khi giao đủ, mốc sổ và sửa/hủy hóa đơn thế nào? | F07–F10. | Không còn giao thiếu; cần căn cứ trước chạy thật. |
| 11 | Rule tự khớp/nhận diện trùng tiền và liên kết khi thiếu mã là gì? | F08 và trạng thái đơn. | Đóng theo thực nhận gắn đơn + chủ hộ xác nhận đã chốt. Không chặn bởi giao/hóa đơn/tiền dư. |
| 12 | Hàng giữ có hết hạn không; kỳ thuế cần bằng chứng nào để đánh dấu hoàn thành? | F05.04, F11.08 và F14. | Có, trước trạng thái và quy tắc chi tiết. Chủ hộ xác nhận đơn trước giữ hàng đã chốt. |

### 9.1 Phạm vi trình bày proposal đã chốt

| Nhóm | Proposal | Phạm vi phân tích |
|---|---|---|
| Đơn mua → human xác nhận → nhập một kho | Luồng chính | Có thể nhận vật lý trước, nhưng tăng tồn phải có đơn mua. |
| Nhận mua nhiều lần | Không đưa | Vẫn theo dõi trong F03.03. |
| Trả đủ tiền mua trước hoặc sau nhận | Luồng chính | Một lần, chủ hộ ghi khoản chi; ứng trước một phần/mua chịu/trả nhiều lần làm sau. |
| Đơn chờ duyệt → giao trực tiếp → hóa đơn → thu tiền | Luồng chính | Agent hỗ trợ, chủ hộ thao tác tay; ngân hàng tích hợp thật là mục tiêu. |
| Giao một phần hoặc xác nhận đơn chờ nhập | Không thuộc luồng hiện tại | Giảm lượng theo tồn hoặc nhập thêm trước xác nhận, không giữ/giao từng phần. |
| Kết nối vận chuyển | Đang phát triển | Nice to have. |
| Trả nhiều lần đơn bán | Không đưa | Không phân tích làm hành trình chính; vẫn lưu tiền thực nhận. |
| Hủy sau có hóa đơn | Đang phát triển | Chủ hộ thao tác, cần biên bản; xác minh nghiệp vụ kế toán. |
| Tổng hóa đơn quý, hướng dẫn eTax và theo dõi tiến trình | Luồng chính | Mẫu đã có; chờ quy tắc kế toán/API. Không API dùng cập nhật tay; sau gửi chờ kết quả. |

## 10. Điều kiện chốt Feature Catalog

Feature Catalog được chốt khi:

- Mỗi capability cấp 1 có Feature hoặc Service Package tương ứng.
- Ba chuỗi Procure-to-Pay, Order-to-Cash và Record-to-Tax có đủ Feature trong phạm vi hiện tại.
- Phần thuế có hướng dẫn theo mẫu đã xác nhận, truy được dữ liệu nguồn và có phương án lưu kết quả/đóng kỳ thực hiện ngoài OPC.
- Nhóm F04 về chế biến đã loại; các Feature khác không kéo nghiệp vụ chế biến trở lại.
- Đơn Agent tạo phải được chủ hộ duyệt trước khi xác nhận/giữ hàng; thao tác tay dùng cùng quy tắc và lịch sử.
- Product Feature và dịch vụ triển khai được phân biệt rõ.
- Các quyết định về kho, giao hàng, quyền, kế toán, tờ khai, kết quả eTax và offline có đầu mối chốt.
- PO đồng ý Feature nào đi vào từng vertical slice.

Sau khi Feature Catalog được chốt, bước tiếp theo là:

1. Dùng [Use Case Catalog v0.8](OPC_USE_CASE_CATALOG.md) đã có 33 UC để refine slice ưu tiên; không tạo catalog trùng.
2. Tạo Dependency Mapping để xác định phần OPC tự xây, mua dịch vụ hoặc tích hợp provider.
3. Viết workflow nghiệp vụ và Agent workflow cho Use Case được ưu tiên.
4. Sau đó mới tách requirement, UX, User Story và UAT.

Tài liệu demo cũ: [OPC Key Use Cases and HTML Demo Scope](OPC_KEY_USE_CASES_AND_HTML_DEMO_SCOPE.md). Cần đồng bộ ba flow, quyền Agent và phạm vi thuế trước khi dùng làm đầu vào DEV.

## 11. Tài liệu nguồn

BRD v0.9, Capability Map v0.6, Flow Explainer v0.3 và Use Case Catalog v0.8 đồng bộ quyết định PO 07/10/2026. Word v1.2, PRD draft, PRD/SRS/backlog Sales Agent, demo/slide chưa cập nhật lượt này. 94 mã Feature và 9 Service được giữ, gồm mã lịch sử/ngoài phạm vi, không phải 94 Feature đều triển khai.

- [BRD OPC Platform](BRD_OPC_PLATFORM.md)
- [OPC Business Capability Map](OPC_BUSINESS_CAPABILITY_MAP.md)
- [PRD OPC Platform Draft](PRD_OPC_PLATFORM_DRAFT.md)
- [PRD OPC Sales Operations Agent](../02_OPC_Sales_Agent_Docs/01_PRD/PRD_OPC_SALES_AGENT.md)
- [Business and Agent Workflow](../02_OPC_Sales_Agent_Docs/02_Workflow/BUSINESS_AND_AGENT_WORKFLOW.md)

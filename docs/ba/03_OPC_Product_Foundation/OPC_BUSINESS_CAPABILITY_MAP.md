# OPC Business Capability Map

**Phiên bản:** 0.6  
**Ngày:** 07/10/2026  
**Trạng thái:** Đã cập nhật phạm vi theo xác nhận của PO; còn đầu vào kế toán và tích hợp cần xác minh  
**Product Owner:** Hiếu  
**Nguồn:** [BRD OPC Platform](BRD_OPC_PLATFORM.md), câu trả lời trong [bản review nghiệp vụ](../05_OPC_Presentation/OPC_4_BUSINESS_FLOWS_REVIEW_v1.1.docx) và quyết định của PO ngày 06/10/2026.

Phạm vi đồng bộ BRD v0.9, Feature Catalog v0.4, Flow Explainer v0.3 và [Use Case Catalog v0.8](OPC_USE_CASE_CATALOG.md) theo quyết định PO ngày 07/10/2026. Giữ 15 capability đang áp dụng; không thêm module mới. Word/slide chưa đồng bộ; xem mục 11.

## 1. Mục đích

Tài liệu này chuyển phạm vi business trong BRD thành bản đồ năng lực của OPC.

Tài liệu trả lời ba câu hỏi:

1. OPC phải có khả năng làm những việc gì để vận hành end-to-end một doanh nghiệp nhỏ?
2. OPC phải sở hữu những product capability nào?
3. Các capability nối với nhau như thế nào trong ba chuỗi nghiệp vụ chính?

Tài liệu chưa định nghĩa màn hình, Feature, API, User Story hoặc cách DEV triển khai.

## 2. Cách đọc capability

- **Capability cấp 0:** kết quả lớn nhất mà OPC cần cung cấp.
- **Capability cấp 1:** một nhóm năng lực business ổn định như quản lý đơn hàng hoặc quản lý kho.
- **Capability cấp 2:** các việc business cụ thể cần làm bên trong capability cấp 1.
- **Feature:** cách sản phẩm cung cấp một phần capability. Feature sẽ được xác định ở bước tiếp theo.

Ví dụ:

- Capability cấp 1: Inventory and Warehouse.
- Capability cấp 2: Giữ hàng cho đơn bán.
- Feature sau này: Stock Reservation and Release.

## 3. Capability cấp 0

**OPC giúp chủ hộ quản lý mua hàng, kho, bán hàng, giao hàng, thu chi, công nợ, hóa đơn và sổ sách; hướng dẫn điền tờ khai trên eTax và theo dõi kết quả từng kỳ.**

Nhóm pilot là hộ kinh doanh nhỏ lẻ, tập trung Phân phối, cung cấp hàng hóa. Khoảng doanh thu/danh sách cụ thể còn cần khảo sát; doanh thu trao đổi là theo tháng, không phải ngưỡng thuế được xác nhận. Ví dụ khách sạn chỉ giải thích quy trình.

Agent hỗ trợ đọc dữ liệu, kiểm tra, đề xuất và chuẩn bị giao dịch. Chủ hộ có thể thao tác tay ở mọi khâu trong OPC theo quyền. Cả hai cách dùng chung dữ liệu, quy tắc, trạng thái và lịch sử.

## 4. Ba chuỗi nghiệp vụ chính

| Chuỗi nghiệp vụ | Điểm bắt đầu | Điểm kết thúc | Kết quả business |
|---|---|---|---|
| Procure-to-Pay | Phát sinh nhu cầu mua hàng hoặc chi phí | Hàng, chi phí, chứng từ và khoản thanh toán nhà cung cấp được ghi nhận | Có đủ hàng để bán và kiểm soát được chi phí, phải trả. |
| Order-to-Cash | Zalo hoặc chủ hộ tự tạo đơn | Có thực nhận gắn đơn và chủ hộ xác nhận đóng; giao/hóa đơn tiếp tục theo dõi riêng | Xác nhận trong tồn, giữ/giao đủ; Agent hỗ trợ, không tự gửi tin. |
| Record-to-Tax | Thông tin hộ và hóa đơn/giao dịch | Tổng hóa đơn quý, hướng dẫn eTax, ghi nhận đã gửi/chờ cập nhật có nguồn | Chủ hộ kiểm tra/sửa; trạng thái sau gửi/hoàn thành cần xác minh. |

Business Onboarding, Agent Control Tower, Integration, Security và Audit hỗ trợ cả ba chuỗi. Người dùng thực hiện kê khai, sửa/bổ sung và nộp trên eTax. Khả năng lấy lịch sử, kết quả và bằng chứng từ eTax qua provider chưa được xác minh.

## 5. Bản đồ capability cấp 1

| Nhóm | Capability cấp 1 | Kết quả business | Phạm vi MVP |
|---|---|---|---|
| Nền tảng | Business Setup and Onboarding | Doanh nghiệp sẵn sàng vận hành với dữ liệu và kết nối cần thiết. | Bắt buộc |
| Nền tảng | Master Data and Party Management | Khách hàng, nhà cung cấp, sản phẩm, giá và điều khoản có dữ liệu chuẩn. | Bắt buộc |
| Mua hàng | Purchase and Expense Management | Nhu cầu mua, đơn mua, chi phí và chứng từ đầu vào được quản lý. | Bắt buộc |
| Kho | Inventory and Warehouse Management | Tồn kho và mọi biến động hàng hóa được kiểm soát và truy vết. | Bắt buộc |
| Bán hàng | Sales and Order Management | Yêu cầu bán được chuyển thành đơn hợp lệ và có thể thực hiện. | Bắt buộc |
| Thực hiện đơn | Fulfilment and Delivery | Hàng được chuẩn bị, bàn giao và giao đúng trạng thái. | Bắt buộc |
| Tiền | Receivables, Payables and Cash Management | Tiền vào, tiền ra, phải thu và phải trả được theo dõi và đối soát. | Bắt buộc |
| Chứng từ | Invoice and Document Management | Hóa đơn và chứng từ đầu vào, đầu ra được quản lý đúng trạng thái. | Bắt buộc |
| Sổ nghiệp vụ | Books and Reconciliation | Đơn, kho, tiền, hóa đơn, doanh thu và chi phí được nối và giải thích. | Bắt buộc |
| Thuế | Tax Guidance and Period Tracking | Người dùng hiểu cách điền tờ khai eTax và theo dõi được kết quả từng kỳ. | Bắt buộc; nguồn kết quả cần xác minh |
| Điều hành | Agent Control Tower | Chủ hộ kiểm soát đề xuất, workflow và thao tác tay khi cần. | Bắt buộc |
| Tích hợp | Integration Management | Kết nối third party được quản lý, giám sát và khôi phục khi lỗi. | Bắt buộc |
| Kiểm soát | Access, Approval and Audit | Quyền, phê duyệt và lịch sử hành động được kiểm soát. | Bắt buộc |
| Theo dõi | Business and Program Monitoring | Chủ hộ và chương trình thấy tình trạng vận hành và kết quả pilot. | Bắt buộc ở mức cơ bản |
| Dịch vụ | Implementation, Training and Customer Success | Hộ được thiết lập, đào tạo, hỗ trợ và duy trì sử dụng sau khi kích hoạt. | Bắt buộc |

## 6. Capability cấp 2

Giữ số mục cũ để không làm lệch tham chiếu Feature. Capability 04 đã được loại khỏi phạm vi; các capability khác không đổi mã. Còn 15 capability đang áp dụng: 14 capability sản phẩm và 1 capability dịch vụ.

### 6.1 Business Setup and Onboarding

**Kết quả:** hộ hoàn tất thiết lập và sẵn sàng tạo giao dịch thật.

- Thu thập hồ sơ hộ, mã số thuế, người vận hành và ngành nghề đã đăng ký; pilot tập trung Phân phối, cung cấp hàng hóa.
- Thiết lập vai trò và quyền truy cập.
- Chọn cấu hình ngành và chính sách ban đầu.
- Nhập hoặc tạo dữ liệu nền ban đầu.
- Kết nối ngân hàng, hóa đơn và dịch vụ cần thiết đã được xác minh; hướng dẫn sử dụng eTax và làm rõ nguồn cập nhật kết quả kỳ.
- Kiểm tra readiness trước khi vận hành.
- Hướng dẫn người dùng hoàn thành giao dịch đầu tiên.

### 6.2 Master Data and Party Management

**Kết quả:** các quy trình cùng sử dụng một nguồn dữ liệu chuẩn.

- Quản lý khách hàng và địa chỉ giao hàng.
- Quản lý nhà cung cấp.
- Quản lý sản phẩm, SKU, đơn vị tính/quy cách do chủ hộ thiết lập; không mặc định tự quy đổi thùng–chai.
- Quản lý bảng giá và giá theo khách hàng.
- Theo dõi thông tin thanh toán; hạn mức/chặn nợ quá hạn không thuộc luồng hiện tại.
- Quản lý thông tin cần dùng cho hóa đơn và thuế.
- Lưu lịch sử thay đổi dữ liệu quan trọng.

### 6.3 Purchase and Expense Management

**Kết quả:** doanh nghiệp biết mua gì, từ ai, với giá nào và đã thanh toán chưa.

- Ghi nhận nhu cầu mua hàng.
- Agent nhận biết ý định mua từ nguồn được phép và đề xuất → chủ hộ xác nhận; hoặc chủ hộ tự tạo/xác nhận đơn. Nhà cung cấp không cần tài khoản/duyệt trên OPC.
- Theo dõi trạng thái đơn mua.
- Bấm “Nhận hàng”, kiểm tra/sửa lượng mặc định theo đơn rồi “Xác nhận nhập kho”; tăng tồn một lần theo thực nhận, phần thiếu theo dõi riêng.
- Hộ linh hoạt nhập đơn trước/sau khi nhận hàng vật lý; muốn tăng tồn bắt buộc có đơn mua và chủ hộ xác nhận thực nhận.
- Theo dõi nhiều lần nhận trên cùng đơn; không đưa nhánh hiếm này vào proposal.
- Ghi nhận chi phí không qua kho.
- Nhận và kiểm tra chứng từ đầu vào.
- Tạo và theo dõi khoản phải trả nhà cung cấp.
- Xử lý trả hàng, hủy mua hoặc chênh lệch.
- Chủ hộ ghi khoản chi tiền mặt/chuyển khoản, số tiền/ngày và xác nhận; trả đủ một lần trước hoặc sau nhận hàng. Agent không chuyển tiền. Ứng trước một phần/trả nhiều lần/mua chịu làm sau.
- Chưa nhận hàng và chưa trả tiền được sửa/hủy đơn có lịch sử; đã phát sinh hàng hoặc tiền xử lý riêng, ngoài happy path.

### 6.4 Production, Batch and Traceability

**Đã loại khỏi phạm vi theo quyết định PO ngày 06/10/2026.** Không phân tích hoặc triển khai nghiệp vụ chế biến, công thức, nguyên liệu, hao hụt, tạo thành phẩm và truy xuất từ thành phẩm về nguyên liệu. Giữ mục này chỉ để truy lại mã 04 đã dùng trước đây.

### 6.5 Inventory and Warehouse Management

**Kết quả:** doanh nghiệp không bán vượt tồn và giải thích được mọi biến động kho.

Giai đoạn đầu dùng một kho chứa nhiều mặt hàng, không yêu cầu nhiều kho/vị trí.

- Ghi nhận tồn đầu kỳ của hàng hóa kinh doanh.
- Ghi nhận nhập kho từ mua hàng hoặc điều chỉnh hợp lệ.
- Tính tồn thực tế, tồn đã giữ và tồn khả dụng.
- Xác nhận đơn bán không vượt tồn khả dụng, giữ đủ theo đơn, chống giữ hai lần; không giữ một phần hoặc xác nhận đơn chờ nhập thêm.
- Đơn chờ duyệt chưa giữ hàng. Hủy trước bàn giao thì dừng xử lý và giải phóng số hàng đã giữ.
- Chính sách hết hạn giữ hàng hoặc thay đổi đơn còn cần chốt ở bước Feature; chưa tự áp dụng thời hạn.
- Chuẩn bị theo đơn; chủ hộ bấm “Đã giao” nghĩa là giao đủ, lượng lấy từ đơn đã xác nhận, không nhập lại lượng hoặc bắt ảnh giao hàng.
- Chỉ trừ tồn thực tế tại thời điểm bàn giao đã được xác nhận.
- Ghi nhận trả hàng và nhập lại khi hợp lệ.
- Kiểm kê và điều chỉnh kho có phê duyệt.
- Nhu cầu theo dõi lô hoặc hạn dùng của hàng mua ngoài cần xác nhận theo pilot; không bao gồm truy xuất chế biến.
- Truy vết lịch sử nhập, xuất, giữ và điều chỉnh.

### 6.6 Sales and Order Management

**Kết quả:** mọi yêu cầu bán hợp lệ trở thành đơn có giá, công nợ và nguồn hàng rõ ràng.

- Nhận yêu cầu từ Zalo hoặc kênh được hỗ trợ.
- Nhận diện khách hàng và sản phẩm.
- Làm rõ thông tin còn thiếu.
- Chủ hộ trao đổi, báo giá và báo tồn cho khách; Agent gợi ý nội dung, không tự gửi Zalo.
- Khách lẻ và khách doanh nghiệp dùng cùng luồng bán; thông tin hóa đơn bắt buộc vẫn cần kế toán xác nhận. Chủ hộ thiết lập giá.
- Áp dụng giá do chủ hộ thiết lập; không làm giảm giá/phê duyệt giảm giá.
- Theo dõi đơn chưa đóng là chờ thanh toán/công nợ, giữ số tiền thực nhận riêng; không kiểm tra/chặn theo hạn mức hoặc nợ quá hạn.
- Kiểm tra tồn khả dụng trước khi đề xuất đơn.
- Agent tạo đơn ở trạng thái chờ duyệt; chủ hộ duyệt thì đơn mới được xác nhận và giữ hàng.
- Hiển thị dữ liệu thiếu, không khớp hoặc ngoại lệ để chủ hộ quyết định; hỏi lại khách nếu cần thay đổi cam kết.
- Chủ hộ tự tạo/xác nhận đơn, không duyệt thêm lần nữa; sửa/hủy theo quyền và quy tắc chung.
- Khi có giao dịch đã được Agent hoặc người dùng tạo, thao tác tiếp trên cùng hồ sơ để tránh tạo trùng.
- Theo dõi trạng thái và ngoại lệ của đơn.
- Không giao một phần/giao tiếp. Thiếu tồn thì chủ hộ giảm lượng trong tồn trước xác nhận hoặc nhập thêm/cập nhật kho rồi xác nhận đủ.
- Có tiền thực nhận gắn với đơn → đề xuất đóng → chủ hộ xác nhận. Giao/hóa đơn/tiền dư không chặn đóng; đơn đóng trước giao vẫn cho xử lý các việc còn chờ.
- Người mua báo hủy; chủ hộ thao tác trên OPC, không yêu cầu người mua có tài khoản.

### 6.7 Fulfilment and Delivery

**Kết quả:** đơn được chuẩn bị và bàn giao đúng số lượng, thời điểm và người nhận.

- Tạo yêu cầu chuẩn bị hàng để giao.
- Chuẩn bị hàng theo đơn, không yêu cầu nhập lại lượng chuẩn bị trong luồng đơn giản.
- Chọn phương thức giao và đơn vị giao hàng.
- Giai đoạn đầu chủ yếu giao trực tiếp, chủ hộ ghi nhận kết quả. Tích hợp vận chuyển là Nice to have, proposal ghi tiếp tục phát triển.
- Điều phối lịch giao.
- Ghi nhận bàn giao hàng.
- Chủ hộ bấm “Đã giao” khi giao đủ; trừ kho đúng một lần theo đơn, lưu người/thời gian và kích hoạt hóa đơn.
- Giao thất bại/hoàn sau giao là nhánh cần refinement; không thêm hành trình giao từng phần.
- Không yêu cầu ảnh bắt buộc trong luồng giao tay.
- Chủ hộ có thể ghi nhận các bước bằng tay. Giao đủ chỉ hoàn thành phần giao hàng, chưa chứng minh đã thu tiền hay phát hành hóa đơn thành công.

### 6.8 Receivables, Payables and Cash Management

**Kết quả:** doanh nghiệp biết phải thu, phải trả và tiền thực tế đã đi đâu.

- Tạo và theo dõi khoản phải thu theo đơn và hóa đơn.
- Tạo và theo dõi khoản phải trả theo mua hàng và chi phí.
- Tạo yêu cầu thanh toán hoặc QR.
- Nhận giao dịch ngân hàng.
- Tích hợp ngân hàng thật là mục tiêu đã chốt; cần map dữ liệu và chức năng provider, chưa coi là đã triển khai.
- Ghi nhận thu/chi bằng tay theo quyền, gồm tiền mặt. Việc chọn sẵn phương thức tiền mặt không tự chứng minh đã nhận tiền.
- Chống ghi nhận trùng giao dịch.
- Khớp tiền tự động theo rule xác định.
- Cho phép người có quyền tìm đơn và xác nhận phân bổ tiền bằng tay; các tiêu chí tự khớp chi tiết còn cần chốt.
- Đưa giao dịch thiếu, thừa hoặc không rõ nguồn sang xử lý ngoại lệ.
- Giao chưa thu tiền thì chờ thanh toán/còn công nợ. Không lấy hành trình trả nhiều lần làm phạm vi proposal hiện tại.
- Ghi đúng tiền thực nhận và chênh lệch; chủ hộ tự xử lý, thêm ghi chú giải trình. Ví dụ hóa đơn 8.000đ, nhận 10.000đ, ghi chuyển dư 2.000đ; không sửa hóa đơn hoặc tự ghi dư thành doanh thu.
- Chi tiết tự hoàn/giữ tiền dư cho lần sau chưa được chốt; hoàn sau hủy hóa đơn thuộc nhánh đang phát triển.
- Đóng khoản phải thu hoặc phải trả khi đủ điều kiện.

### 6.9 Invoice and Document Management

**Kết quả:** mọi giao dịch cần hóa đơn hoặc chứng từ đều có trạng thái và bằng chứng rõ ràng.

- Tạo dữ liệu hóa đơn bán ra từ giao dịch đã xác nhận.
- Bấm “Đã giao” đủ theo đơn kích hoạt một hóa đơn theo đơn; kế toán/provider xác minh thực thi trước chạy thật. Quy tắc giao thiếu cũ đã bị thay thế.
- Gửi yêu cầu phát hành qua nhà cung cấp hóa đơn.
- Nhận kết quả phát hành hoặc từ chối.
- Hóa đơn lỗi vẫn chờ xử lý với provider; không dùng lỗi hóa đơn chặn đóng đơn theo tiền thực nhận và chủ hộ xác nhận. Đóng đơn không làm hóa đơn tự thành công.
- Gửi hóa đơn cho khách hàng.
- Hóa đơn điện tử qua provider; chứng từ viết tay chụp ảnh và nhập thông tin thủ công, OCR làm sau. Lưu loại/nguồn, không tự xác nhận giá trị pháp lý từ ảnh.
- Kiểm tra hóa đơn với đơn hàng, giao nhận và thanh toán.
- Xử lý hủy, thay thế hoặc điều chỉnh có phê duyệt.
- Hủy khi đã có hóa đơn xử lý thủ công và cần biên bản theo quyết định PO; proposal ghi “đang phát triển”. Loại biên bản, thời hạn sửa và quy trình hóa đơn do kế toán xác nhận.
- Lưu tài liệu và lịch sử xử lý.

### 6.10 Books and Reconciliation

**Kết quả:** dữ liệu cuối kỳ đầy đủ, khớp và có thể giải thích.

- Ghi nhận doanh thu từ giao dịch hợp lệ.
- Ghi nhận chi phí từ mua hàng và chứng từ đầu vào.
- Nối đơn hàng, kho, hóa đơn và tiền.
- Đối soát phải thu và phải trả.
- Phát hiện dữ liệu thiếu, trùng hoặc mâu thuẫn.
- Phân loại giao dịch theo quy tắc đã xác nhận.
- Tạo danh sách ngoại lệ cần kế toán hoặc người dùng xử lý.
- Khóa dữ liệu kỳ khi đủ điều kiện.
- Giải thích nguồn dữ liệu và liên kết chứng từ để người dùng kiểm tra từng trường dùng trong hướng dẫn tờ khai.
- Bộ sổ, trường dữ liệu và quy tắc ghi nhận kỳ cần kế toán xác nhận; câu trả lời “một sổ” chưa đủ để thiết kế.

### 6.11 Tax Guidance and Period Tracking

**Kết quả:** chủ hộ biết cách điền tờ khai trên eTax, kiểm tra được dữ liệu nguồn và theo dõi kết quả từng kỳ trong OPC.

- Chủ hộ chọn quý/năm; tổng hợp riêng hóa đơn bán ra và mua vào theo ngày lập. Happy path mua/bán có hóa đơn.
- Bấm số tổng để xổ hóa đơn theo tháng/ngày và mở chi tiết; thu/chi thực tế là số riêng, không lấy thu trừ chi làm doanh thu.
- Cho sửa dữ liệu chuẩn bị kê khai có lịch sử; báo cần kiểm tra lại nếu đã xác nhận, không sửa trực tiếp hóa đơn phát hành hoặc kết quả kê khai cũ.
- Dùng tờ khai mẫu do PO thu thập và kế toán xác nhận để giải thích ý nghĩa và cách điền từng trường.
- Xác định mỗi trường cần dữ liệu nào, hình thành từ giao dịch/chứng từ nào và tìm ở đâu trong OPC.
- Kiểm tra dữ liệu thiếu hoặc không khớp; Agent trả lời cụ thể theo dữ liệu có nguồn, yêu cầu người dùng bổ sung khi thiếu.
- Người dùng thực hiện điền, sửa/bổ sung, gửi và nộp trên eTax; OPC hỗ trợ giải thích và giữ lịch sử dữ liệu nguồn.
- Nếu người dùng cung cấp yêu cầu bổ sung từ eTax, hỗ trợ giải thích dữ liệu cần bổ sung. Khả năng nhận yêu cầu tự động chưa được xác minh.
- Theo dõi tiến trình OPC: chuẩn bị → kiểm tra → thực hiện eTax → đã gửi → chờ cập nhật kết quả; không coi đã gửi là đã chấp nhận/đã nộp thuế.
- Không có API thì chủ hộ cập nhật tay kèm bằng chứng và nhãn “Chủ hộ xác nhận — chưa đối chiếu qua eTax”.
- Xác minh với provider khả năng lấy lịch sử, trạng thái và bằng chứng từ eTax để hiển thị trên OPC.

PO đã chọn mẫu 01_CNKD_TT40_2026_9172.xlsx. Mẫu áp dụng, quy tắc GTGT/TNCN và trạng thái sau gửi/điều kiện hoàn thành chờ kế toán/provider; mapping trường chủ động để sau. Chưa chốt tự tính thuế/điền draft; OPC không ký/gửi/nộp thay chủ hộ. Tổng hóa đơn không tự là số thuế hoặc khoản khấu trừ.

### 6.12 Agent Control Tower

**Kết quả:** chủ hộ theo dõi trợ giúp của Agent, quyết định các bước cần duyệt và có thể tự tiếp tục công việc.

- Hiển thị workflow đang chạy, hoàn thành, chờ duyệt hoặc bị chặn.
- Hiển thị dữ liệu và lý do Agent dùng để đề xuất.
- Cho phép người dùng duyệt, từ chối, sửa hoặc dừng workflow.
- Cho phép chủ hộ thực hiện bằng tay ở từng khâu theo quyền; thao tác trên cùng giao dịch, dùng chung kiểm tra và cập nhật lịch sử.
- Agent hỗ trợ tạo đề xuất và hồ sơ chờ duyệt; không thay quyền duyệt của chủ hộ.
- Quản lý retry, timeout và escalation.
- Thông báo việc cần xử lý.
- Theo dõi SLA và ngoại lệ theo mức độ ưu tiên.

### 6.13 Integration Management

**Kết quả:** kết nối bên ngoài không làm mất kiểm soát quy trình business.

- Thiết lập và kiểm tra connector.
- Quản lý quyền truy cập và token.
- Nhận webhook và chống xử lý trùng.
- Theo dõi trạng thái, lỗi và lần đồng bộ gần nhất.
- Retry theo chính sách an toàn.
- Chuyển sang fallback hoặc xử lý thủ công khi cần.
- Theo dõi usage, giới hạn và chi phí.
- Thay provider mà không thay đổi kết quả business.

### 6.14 Access, Approval and Audit

**Kết quả:** chỉ đúng người hoặc Agent được phép mới thực hiện được hành động.

- Quản lý người dùng, vai trò và quyền.
- Tách quyền xem, đề xuất, duyệt và thực hiện.
- Yêu cầu chủ hộ duyệt đơn do Agent tạo trước khi xác nhận và giữ hàng.
- Chủ hộ xác nhận đơn Agent đề xuất; đơn tự tạo không duyệt thêm vòng. Thiếu tồn không được duyệt để vượt tồn. Quyền điều chỉnh kho/chứng từ/ngoại lệ cần refinement; không thêm approval giảm giá/nợ quá hạn hoặc thay chủ hộ xác nhận thuế.
- Lưu actor, thời gian, dữ liệu trước và sau, lý do và nguồn.
- Giữ audit log theo nguyên tắc chỉ ghi thêm.
- Cho phép tra cứu lại lịch sử của một giao dịch hoặc workflow.

### 6.15 Business and Program Monitoring

**Kết quả:** chủ hộ và chương trình biết sản phẩm có được sử dụng thật hay không.

- Theo dõi doanh thu, đơn hàng, tồn kho, công nợ, tiền và nghĩa vụ thuế.
- Theo dõi onboarding và readiness.
- Theo dõi giao dịch thật, hóa đơn đầu tiên và hoàn thành kỳ thuế.
- Phân biệt chuẩn bị/kiểm tra/thực hiện eTax/đã gửi/chờ kết quả; không tự đánh dấu hoàn thành kỳ hoặc đã nộp thuế.
- Theo dõi người dùng còn hoạt động sau 90 ngày.
- Theo dõi lỗi connector, ngoại lệ và thời gian xử lý.
- Cung cấp dữ liệu tổng hợp cho chương trình mà không lộ dữ liệu chi tiết của hộ.

### 6.16 Implementation, Training and Customer Success

**Kết quả:** hộ không chỉ được cấp tài khoản mà có thể thiết lập, vận hành giao dịch thật và tiếp tục sử dụng OPC.

- Khảo sát readiness và dữ liệu hiện có của hộ.
- Cấu hình doanh nghiệp theo ngành và mô hình vận hành.
- Chuẩn bị hoặc nhập dữ liệu ban đầu.
- Hỗ trợ thiết lập các kết nối cần thiết.
- Đào tạo trực tiếp hoặc từ xa theo vai trò người dùng.
- Hỗ trợ hoàn thành giao dịch thật đầu tiên.
- Hướng dẫn kỳ kê khai đầu tiên trên eTax và hỗ trợ ghi nhận kết quả trong OPC theo nguồn được xác nhận.
- Cung cấp helpdesk, SLA và cơ chế escalation.
- Kiểm tra mức sử dụng và khó khăn sau 30 và 90 ngày.
- Tổng hợp kết quả pilot và đề xuất điều chỉnh trước khi mở rộng.

Business Setup and Onboarding là capability của sản phẩm. Implementation, Training and Customer Success là capability dịch vụ của đơn vị cung cấp OPC.

## 7. Nguyên tắc sở hữu capability

- OPC sở hữu 15 capability đang áp dụng trong tài liệu này, gồm 14 product capability và 1 service capability. Capability 04 đã loại khỏi phạm vi; capability dịch vụ vẫn giữ mã 16.
- Capability mô tả sản phẩm phải làm được gì, chưa quyết định OPC tự code hay tích hợp dịch vụ khác.
- Sau khi Feature Catalogue được chốt, từng Feature sẽ được đánh giá theo ba lựa chọn: tự xây, mua dịch vụ hoặc tích hợp provider.
- Casso chỉ là một provider tham khảo. OPC có thể đánh giá provider khác cho ngân hàng, hóa đơn, thuế, ký số hoặc thanh toán.
- Dù dùng provider nào, OPC vẫn chịu trách nhiệm về trải nghiệm, trạng thái, lỗi, fallback, audit và kết quả end-to-end.
- Dependency Mapping là tài liệu sau Feature Catalogue, không phải điều kiện để chốt Capability Map.

## 8. Thứ tự tách Feature và Service

Product capability sẽ được chuyển thành Feature theo thứ tự:

1. Business Setup, Master Data và Access Control.
2. Purchase, Goods Receipt, Expense và Inventory.
3. Sales, Order, Inventory Reservation và Fulfilment.
4. Receivables, Payables, Invoice và Cash Matching.
5. Books, Reconciliation, Tax Guidance và Period Tracking; người dùng thực hiện kê khai/nộp trên eTax.
6. Agent Control Tower, Integration và Program Monitoring.

Service capability được chuyển thành Service Package gồm triển khai, cấu hình, nhập dữ liệu, đào tạo, hỗ trợ, SLA và theo dõi adoption.

Thứ tự trên là thứ tự phân tích và build. MVP cần hỗ trợ ba chuỗi trong phạm vi đã chốt và service package đủ để hộ vận hành. Phần thuế cần đầu vào kế toán và nguồn cập nhật kết quả kỳ; chưa cam kết có kết nối eTax tự động.

## 9. Câu hỏi cần trả lời trước khi viết Feature chi tiết

Các câu hỏi này không thay đổi capability map nhưng sẽ thay đổi Feature và workflow:

- Hàng mua ngoài có cần quản lý lô và hạn dùng không?
- Ngoài Zalo, MVP có cần nhận đơn tại quầy hoặc từ sàn thương mại điện tử không?
- Phát hành một hóa đơn theo đơn khi giao đủ cần dữ liệu/điều kiện gì; sửa/hủy cần chứng từ nào?
- Tờ khai mẫu nào áp dụng cho nhóm pilot; mỗi trường cần dữ liệu nguồn và cách giải thích nào?
- Provider có thể lấy kết quả/lịch sử eTax nào; bằng chứng đủ cho các bước sau gửi là gì? Fallback chủ hộ cập nhật đã chốt.
- Ngoài hướng dẫn, tiêu chí nào xác nhận một kỳ đã hoàn thành?
- Nhóm pilot cụ thể và khoảng doanh thu theo tháng là gì?

Việc chọn Casso hoặc provider khác không cần trả lời ở bước Capability. Câu hỏi đó được chuyển sang Dependency Mapping sau Feature Catalogue.

## 10. Điều kiện chốt Capability Map

Capability Map được chốt khi:

- Ba chuỗi Procure-to-Pay, Order-to-Cash và Record-to-Tax được mô tả theo phạm vi hiện tại.
- OPC sở hữu 15 capability đang áp dụng, gồm 14 product capability và 1 service capability; capability chế biến 04 đã loại.
- Các capability ngoài MVP được ghi rõ, không âm thầm đưa vào Feature.
- Toàn bộ chế biến/sản xuất, HR, payroll và tài sản cố định nằm ngoài MVP hiện tại.
- Các câu hỏi chi tiết về kho, kênh bán, giao hàng, tờ khai và kết quả eTax được chuyển sang Feature Catalogue hoặc xác minh với kế toán/provider.
- Nội dung triển khai, đào tạo, hỗ trợ và SLA được chuyển sang Service Package.
- PO đã xác nhận đủ cơ sở để tách Use Case và Feature.

Tài liệu tiếp theo: [OPC Feature Catalog](OPC_FEATURE_CATALOG.md).

## 11. Ảnh hưởng đến tài liệu liên quan

| Tài liệu | Trạng thái đồng bộ ngày 07/10/2026 |
|---|---|
| BRD OPC Platform v0.9 | Đã đồng bộ ba luồng, quyết định vận hành và ranh giới proposal/làm sau. |
| OPC Feature Catalog v0.4 | Giữ mã, cập nhật hành vi và phạm vi; phần hạn mức giữ lịch sử ngoài phạm vi hiện tại. |
| Business Flow Explainer v0.3; Use Case Catalog v0.8 | Đồng bộ quyết định PO 07/10 và đầu vào còn mở. |
| OPC_BUSINESS_FLOWS_REVIEW.docx v1.2 | Chưa đồng bộ quyết định 07/10 trong lượt này, không dùng thay baseline mới. |
| Slide HTML, XML sơ đồ và Word v1.1 cũ | Tài liệu lịch sử; chưa đồng bộ, không dùng làm đầu vào triển khai theo phạm vi mới. |

Không suy ra tính pháp lý hoặc khả năng tích hợp từ quyết định product. Đầu vào kế toán và provider còn mở được chuyển sang Use Case/Dependency Mapping.

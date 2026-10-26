# OPC Key Use Cases and HTML Demo Scope

**Phiên bản:** 0.1  
**Ngày:** 04/10/2026  
**Trạng thái:** Draft giao DEV làm static clickable HTML  
**Product Owner:** Hiếu  
**Nguồn chính:** [OPC Feature Catalog](OPC_FEATURE_CATALOG.md)

## 1. Mục đích

Tài liệu này chọn các Use Case quan trọng nhất để DEV dựng một bản HTML clickable phục vụ trình bày proposal.

Bản demo phải giúp người xem hiểu được:

1. OPC hỗ trợ một doanh nghiệp nhỏ vận hành end-to-end như thế nào.
2. AI Agent làm gì, business rule làm gì và con người quyết định ở đâu.
3. Dữ liệu mua hàng, chế biến, kho, bán hàng, tiền, hóa đơn và thuế nối với nhau như thế nào.
4. Casso hoặc bên thứ ba chỉ xuất hiện tại các điểm kết nối, không phải toàn bộ sản phẩm OPC.

Đây là yêu cầu cho static HTML. Đây chưa phải đặc tả để xây production MVP.

## 2. Phạm vi demo

### 2.1 Bảy Key Use Case

| ID | Key Use Case | Câu chuyện cần chứng minh | Mức ưu tiên demo |
|---|---|---|---|
| UC-01 | Thiết lập doanh nghiệp và readiness | Một hộ có thể biết cần chuẩn bị gì trước khi vận hành. | Bắt buộc |
| UC-02 | Tạo tồn từ mua hàng hoặc chế biến | OPC hỗ trợ cả hàng mua để bán lại và hàng tự chế biến. | Bắt buộc |
| UC-03 | Nhận yêu cầu từ Zalo và tạo đơn hợp lệ | Agent hiểu yêu cầu; OPC kiểm tra khách, giá, công nợ và tồn. | Bắt buộc |
| UC-04 | Soạn, giao, xuất hóa đơn và thu tiền | Một đơn được thực hiện, xuất hóa đơn, khớp tiền và đóng đúng trạng thái. | Bắt buộc |
| UC-05 | Đối soát, kê khai và nộp thuế | Dữ liệu vận hành đi đến tờ khai, thanh toán thuế và bằng chứng. | Bắt buộc |
| UC-06 | Theo dõi Agent và xử lý ngoại lệ | Con người kiểm soát workflow, approval, retry và audit. | Bắt buộc |
| UC-07 | Theo dõi kết quả pilot | Chương trình thấy hộ nào đã kích hoạt, giao dịch và hoàn thành kỳ thuế. | Nên có |

### 2.2 Nguyên tắc cắt phạm vi

- Không dựng UI cho toàn bộ 98 Feature.
- Một màn hình có thể đại diện cho nhiều Feature liên quan.
- Chỉ mô phỏng một doanh nghiệp, một kho chính và một kỳ thuế.
- Chỉ dùng Zalo Simulator cho kênh nhận đơn.
- Dùng dữ liệu tĩnh và thao tác chuyển trạng thái có kiểm soát.
- Không kết nối API thật, database thật, ngân hàng thật, hóa đơn thật hoặc cổng thuế thật.
- Không mô phỏng full ERP, MRP, payroll, HR hoặc kế toán tổng hợp đầy đủ.

## 3. Nhân vật và dữ liệu demo

### 3.1 Nhân vật

| Nhân vật | Vai trò trong demo |
|---|---|
| Owner Operator | Theo dõi doanh nghiệp, duyệt ngoại lệ và thực hiện hành động có quyền. |
| Kế toán | Kiểm tra đối soát, quy tắc thuế và tờ khai nháp. |
| Demo Admin | Reset dữ liệu và đổi kịch bản. Không được duyệt giao dịch thay Owner. |
| AI Agent | Đọc dữ liệu không cấu trúc, lập phương án và giải thích. |
| OPC Rule Engine | Tính tồn, giá, công nợ, tiền, thuế và trạng thái bằng rule xác định. |
| Connector Simulator | Mô phỏng Zalo, ngân hàng, hóa đơn, ký số và cổng thuế. |

### 3.2 Bộ dữ liệu xuyên suốt

| Loại dữ liệu | Giá trị demo |
|---|---|
| Doanh nghiệp | Đặc sản Cao Nguyên An Nhiên |
| Mô hình | Mua hàng để bán lại và tự chế biến đơn giản |
| Kho | Kho chính Gia Lai |
| Nhà cung cấp | Hợp tác xã Cao Nguyên |
| Khách hàng | Sunrise Hotel |
| Sản phẩm 1 | Bò một nắng 500g, có quản lý lô |
| Sản phẩm 2 | Muối kiến vàng 100g, mua để bán lại |
| Kênh đơn hàng | Zalo Simulator |
| Phương thức giao | Carrier Simulator |
| Hóa đơn | Invoice Connector Simulator |
| Ngân hàng | Banking Connector Simulator |
| Kỳ thuế | Kỳ demo, toàn bộ số liệu gắn nhãn `Simulated` |

### 3.3 Tin nhắn bán hàng mẫu

> Khách sạn Sunrise cần 20 gói bò một nắng 500g và 30 hũ muối kiến vàng 100g. Giao trước 15:00 ngày mai và xuất hóa đơn.

## 4. Key Use Case và flow chi tiết

### UC-01 — Thiết lập doanh nghiệp và readiness

**Mục tiêu:** đưa hộ từ trạng thái chưa thiết lập đến trạng thái sẵn sàng chạy giao dịch demo.

**Bắt đầu:** Owner chọn `Bắt đầu thiết lập`.  
**Kết thúc:** readiness đạt `Sẵn sàng có điều kiện` hoặc `Sẵn sàng`.

| Bước | Hành động người dùng | Hệ thống mô phỏng | Màn hình | Kết quả |
|---:|---|---|---|---|
| 1 | Chọn mô hình kinh doanh | Hiển thị hành trình setup phù hợp hộ vừa mua ngoài vừa chế biến. | UI-02 | Setup plan được tạo. |
| 2 | Xác nhận hồ sơ doanh nghiệp | Kiểm tra các trường bắt buộc và đánh dấu trường thiếu. | UI-03 | Hồ sơ ở trạng thái `Đủ dữ liệu`. |
| 3 | Kiểm tra dữ liệu nền | Hiển thị khách hàng, nhà cung cấp, SKU, bảng giá và tồn đầu kỳ. | UI-04 | Danh sách dữ liệu đạt hoặc cần sửa. |
| 4 | Kiểm tra kết nối | Hiển thị Zalo, ngân hàng, hóa đơn và thuế ở trạng thái `Simulated`. | UI-05 | Connector plan được xác nhận. |
| 5 | Xác nhận quyền và approval | Giải thích việc Agent đề xuất, rule kiểm tra và Owner duyệt. | UI-06 | Policy demo được chọn. |
| 6 | Chạy readiness check | Tổng hợp dữ liệu, kết nối, quyền và policy. | UI-02 | Kết quả readiness và việc tiếp theo. |

**Nhánh ngoại lệ cần click được:** thiếu bảng giá → readiness bị chặn → mở danh mục giá → chọn `Dùng dữ liệu demo` → chạy kiểm tra lại.

### UC-02 — Tạo tồn từ mua hàng hoặc chế biến

**Mục tiêu:** cho thấy một sản phẩm có thể đi vào kho từ mua hàng hoặc từ chế biến đơn giản.

**Bắt đầu:** Owner mở `Nguồn hàng và kho`.  
**Kết thúc:** tồn khả dụng và lô hàng được cập nhật.

#### Nhánh A — Mua hàng để bán lại

| Bước | Hành động người dùng | OPC xử lý | Màn hình | Kết quả |
|---:|---|---|---|---|
| 1 | Mở đơn mua mẫu | Hiển thị nhà cung cấp, SKU, số lượng, giá và ngày nhận. | UI-07 | Đơn mua `Đã xác nhận`. |
| 2 | Chọn `Xác nhận nhận hàng` | So sánh số đặt và số nhận. | UI-07 | Phiếu nhận hàng được tạo. |
| 3 | Xác nhận số lượng thực nhận | Rule Engine tạo nhập kho và khoản phải trả. | UI-08 | Tồn và công nợ nhà cung cấp tăng đúng một lần. |
| 4 | Mở nguồn chứng từ | Hiển thị hóa đơn đầu vào mô phỏng liên kết với đơn mua. | UI-08 | Chứng từ được gắn với giao dịch. |

#### Nhánh B — Tự chế biến thành phẩm

| Bước | Hành động người dùng | OPC xử lý | Màn hình | Kết quả |
|---:|---|---|---|---|
| 1 | Mở lệnh chế biến mẫu | Hiển thị nguyên liệu dự kiến và sản phẩm đầu ra. | UI-09 | Lệnh ở trạng thái `Đang thực hiện`. |
| 2 | Nhập lượng nguyên liệu thực dùng và hao hụt | Kiểm tra số lượng với tồn nguyên liệu. | UI-09 | Dữ liệu thực tế hợp lệ. |
| 3 | Xác nhận sản lượng | Tạo lô thành phẩm và nhập kho. | UI-09 | Lô thành phẩm được tạo. |
| 4 | Mở truy xuất lô | Hiển thị nguyên liệu nguồn và đơn hàng nhận lô. | UI-08 | Traceability hai chiều được chứng minh. |

**Nhánh ngoại lệ cần click được:** số nguyên liệu dùng lớn hơn tồn → hệ thống chặn, không tạo tồn âm.

### UC-03 — Nhận yêu cầu từ Zalo và tạo đơn hợp lệ

**Mục tiêu:** chứng minh Agent hiểu yêu cầu nhưng OPC chỉ tạo đơn sau khi rule đã kiểm tra.

**Bắt đầu:** Connector Simulator nhận tin nhắn mẫu.  
**Kết thúc:** đơn được xác nhận và tồn được giữ.

| Bước | Hành động/ngữ cảnh | Agent thực hiện | OPC Rule Engine thực hiện | Màn hình | Kết quả |
|---:|---|---|---|---|---|
| 1 | Tin nhắn mới xuất hiện | Trích xuất khách, SKU, số lượng, giờ giao và yêu cầu hóa đơn. | Chưa ghi đơn hoặc tồn. | UI-10 | Bản hiểu của Agent. |
| 2 | Owner mở kết quả | Hiển thị confidence và bằng chứng từ tin nhắn. | Tra cứu khách hàng và SKU chuẩn. | UI-10 | Khách và SKU được đối chiếu. |
| 3 | Chọn `Kiểm tra đơn` | Giải thích kết quả kiểm tra. | Kiểm tra bảng giá, giảm giá, công nợ và tồn khả dụng. | UI-11 | Kết quả từng rule. |
| 4 | Tất cả rule đạt | Soạn nội dung xác nhận. | Tạo Order Draft và giữ hàng trong một giao dịch xác định. | UI-11 | Đơn `Đã giữ hàng`. |
| 5 | Owner xác nhận gửi | Không tự thay đổi giá hoặc số lượng. | Revalidate phiên bản đơn và reservation. | UI-11 | Đơn `Đã xác nhận`. |

**Nhánh ngoại lệ chính:** khách có nợ quá hạn → đơn chuyển `Chờ duyệt` → mở UC-06 → Owner duyệt có lý do → OPC kiểm tra lại trước khi tiếp tục.

### UC-04 — Soạn, giao, xuất hóa đơn và thu tiền

**Mục tiêu:** đưa đơn đã xác nhận đến trạng thái đóng mà không cập nhật tiền hoặc tồn sai thời điểm.

**Bắt đầu:** đơn ở trạng thái `Đã xác nhận`.  
**Kết thúc:** giao thành công, hóa đơn được ghi nhận, tiền được khớp và đơn đóng.

| Bước | Hành động người dùng/sự kiện | OPC xử lý xác định | Màn hình | Kết quả |
|---:|---|---|---|---|
| 1 | Mở danh sách soạn hàng | Hiển thị SKU, số lượng và lô đề xuất. | UI-12 | Picking task được mở. |
| 2 | Xác nhận số lượng đã soạn | Kiểm tra với reservation. Chưa trừ tồn thực tế. | UI-12 | Hàng ở trạng thái `Đã soạn`. |
| 3 | Xác nhận bàn giao | Ghi xuất kho và consume reservation đúng một lần. | UI-12 | Đơn `Đang giao`. |
| 4 | Carrier Simulator báo giao thành công | Kiểm tra thứ tự event và cập nhật shipment. | UI-12 | Shipment `Đã giao`. |
| 5 | Chọn `Tạo hóa đơn` | Tạo dữ liệu từ giao dịch đã giao và gửi lệnh idempotent. | UI-13 | Hóa đơn mô phỏng `Đã phát hành`. |
| 6 | Hệ thống tạo khoản phải thu | Gắn số tiền và hạn thanh toán với hóa đơn. | UI-13 | Receivable `Đang mở`. |
| 7 | Banking Simulator gửi giao dịch | Chống trùng, kiểm tra số tiền và mã tham chiếu. | UI-13 | Payment `Đã khớp`. |
| 8 | OPC phân bổ tiền | Đóng phải thu và chạy close gate. | UI-11 | Đơn `Đã đóng`. |

**Nhánh ngoại lệ cần click được:** tiền về thiếu hoặc thiếu mã đơn → không tự khớp → chuyển `Cần kiểm tra` → mở UC-06.

### UC-05 — Đối soát, kê khai và nộp thuế

**Mục tiêu:** chứng minh điểm kết thúc MVP là hoàn thành một kỳ thuế có bằng chứng.

**Bắt đầu:** kỳ có dữ liệu bán, mua, kho, hóa đơn và tiền.  
**Kết thúc:** tờ khai đã gửi, thuế đã nộp, bằng chứng đã lưu và kỳ được đóng.

| Bước | Hành động người dùng | OPC xử lý | Màn hình | Kết quả |
|---:|---|---|---|---|
| 1 | Mở kỳ demo | Tổng hợp doanh thu, chi phí, hóa đơn, tiền và công nợ. | UI-14 | Readiness của kỳ. |
| 2 | Mở đối soát | Hiển thị giao dịch đã khớp và ngoại lệ còn lại. | UI-14 | Danh sách cần xử lý. |
| 3 | Xử lý ngoại lệ mẫu | Lưu quyết định và chạy lại kiểm tra. | UI-14 | Kỳ `Sẵn sàng tính`. |
| 4 | Chọn `Tính thuế` | Áp dụng bộ rule demo có phiên bản và nguồn giả lập rõ ràng. | UI-15 | Kết quả thuế `Simulated`. |
| 5 | Kế toán kiểm tra tờ khai nháp | Hiển thị dữ liệu đầu vào, công thức và chênh lệch. | UI-15 | Tờ khai `Chờ Owner duyệt`. |
| 6 | Owner duyệt và chọn `Ký và gửi` | Connector Simulator trả kết quả tiếp nhận. | UI-16 | Tờ khai `Đã tiếp nhận - Simulated`. |
| 7 | Owner chọn `Nộp thuế` | Chuyển sang Tax Payment Simulator và nhận kết quả. | UI-16 | Khoản thuế `Đã thanh toán - Simulated`. |
| 8 | Mở bằng chứng và đóng kỳ | Liên kết tờ khai, giao dịch thanh toán và audit. | UI-16 | Kỳ `Đã đóng`. |

**Cảnh báo bắt buộc:** mọi số thuế, biểu mẫu, kết quả gửi và thanh toán trong HTML đều là dữ liệu mô phỏng; không được khẳng định là quy định hoặc integration thật.

### UC-06 — Theo dõi Agent và xử lý ngoại lệ

**Mục tiêu:** chứng minh mô hình review by exception và ranh giới Agent–OPC–con người.

**Bắt đầu:** có workflow đang chạy hoặc đang chờ quyết định.  
**Kết thúc:** ngoại lệ được xử lý, workflow tiếp tục hoặc dừng có audit.

| Bước | Hành động người dùng | Hệ thống hiển thị/xử lý | Màn hình | Kết quả |
|---:|---|---|---|---|
| 1 | Mở Control Tower | Nhóm việc thành đang chạy, chờ người, chờ connector và lỗi. | UI-01 | Tổng quan vận hành. |
| 2 | Chọn case nợ quá hạn | Hiển thị tin nhắn gốc, rule result, mức nợ và đề xuất của Agent. | UI-17 | Approval detail. |
| 3 | Chọn duyệt hoặc từ chối | Bắt buộc nhập lý do; Agent không tự quyết định. | UI-17 | Decision được lưu. |
| 4 | OPC chạy revalidation | Kiểm tra lại công nợ, tồn, reservation và phiên bản đơn. | UI-18 | Workflow tiếp tục hoặc vẫn bị chặn. |
| 5 | Mở timeline | Tách nhãn `Agent proposed`, `OPC rule`, `Human approved`, `Connector simulated`. | UI-18 | Người xem hiểu trách nhiệm từng bên. |
| 6 | Mở audit | Hiển thị event chỉ đọc, trước/sau, actor, thời gian và correlation ID. | UI-19 | Bằng chứng không thể sửa. |

**Các case chuyển bằng Scenario Switcher:** nợ quá hạn, thiếu tồn, hóa đơn bị từ chối, tiền không khớp và connector timeout.

### UC-07 — Theo dõi kết quả pilot

**Mục tiêu:** cho PM/chương trình thấy pilot có sử dụng thật hay chỉ cấp tài khoản.

**Bắt đầu:** chọn vai trò `Program Viewer`.  
**Kết thúc:** xem được kết quả tổng hợp mà không mở dữ liệu giao dịch chi tiết của hộ.

| Bước | Hành động người dùng | Hệ thống hiển thị | Màn hình | Kết quả |
|---:|---|---|---|---|
| 1 | Mở Program Dashboard | Số hộ theo readiness, first transaction và first tax cycle. | UI-20 | Tổng quan pilot. |
| 2 | Chọn nhóm trạng thái | Hiển thị hộ đang bị chặn theo loại vấn đề. | UI-20 | Biết nơi cần hỗ trợ. |
| 3 | Xem adoption 30/90 ngày | Hiển thị active rate và nhóm Feature đã dùng. | UI-20 | Có dữ liệu quyết định mở rộng. |
| 4 | Mở báo cáo | Hiển thị chỉ số tổng hợp, không hiển thị chi tiết tiền/đơn của hộ. | UI-20 | Báo cáo pilot có kiểm soát dữ liệu. |

## 5. Luồng demo xuyên suốt

Trình tự mặc định khi present:

`UI-01 Dashboard → UC-01 Readiness → UC-02 Tạo tồn → UC-03 Nhận đơn Zalo → UC-06 Duyệt ngoại lệ → UC-04 Giao, hóa đơn, tiền → UC-05 Đối soát và thuế → UC-07 Kết quả pilot`

Thời lượng đề xuất:

| Phần |
|---|
| Giới thiệu dashboard và mô hình Agent |
| Onboarding và readiness |
| Nguồn hàng và tồn kho |
| Order-to-Cash và approval |
| Record-to-Tax |
| Program monitoring và kết luận |

## 6. Danh sách màn hình

| ID | Route đề xuất | Màn hình | Use Case | Ảnh cần chụp cho proposal |
|---|---|---|---|---|
| UI-01 | `#/dashboard` | Owner Operations Dashboard | UC-06 | Có |
| UI-02 | `#/setup/overview` | Onboarding và Readiness Overview | UC-01 | Có |
| UI-03 | `#/setup/business` | Hồ sơ và mô hình doanh nghiệp | UC-01 | Không |
| UI-04 | `#/setup/data` | Dữ liệu ban đầu | UC-01 | Không |
| UI-05 | `#/setup/connections` | Connection Center | UC-01 | Có |
| UI-06 | `#/setup/policy` | Vai trò và Policy | UC-01 | Không |
| UI-07 | `#/supply/purchase` | Đơn mua và nhận hàng | UC-02 | Có |
| UI-08 | `#/inventory` | Tồn kho, lô và truy xuất | UC-02 | Có |
| UI-09 | `#/supply/production` | Chế biến đơn giản | UC-02 | Có |
| UI-10 | `#/sales/inbox` | Zalo Sales Request Inbox | UC-03 | Có |
| UI-11 | `#/sales/orders/:id` | Order 360 | UC-03, UC-04 | Có |
| UI-12 | `#/fulfilment/:id` | Picking và Delivery | UC-04 | Không |
| UI-13 | `#/finance/order/:id` | Invoice, Receivable và Payment | UC-04 | Có |
| UI-14 | `#/books/period/:id` | Period Reconciliation | UC-05 | Có |
| UI-15 | `#/tax/period/:id` | Tax Calculation và Draft Return | UC-05 | Có |
| UI-16 | `#/tax/period/:id/submit` | Filing, Tax Payment và Evidence | UC-05 | Có |
| UI-17 | `#/approvals/:id` | Approval Detail | UC-06 | Có |
| UI-18 | `#/workflows/:id` | Agent Workflow Detail | UC-06 | Có |
| UI-19 | `#/audit/:entityId` | Immutable Audit Timeline | UC-06 | Không |
| UI-20 | `#/program/pilot` | Pilot and Adoption Dashboard | UC-07 | Có |

## 7. Yêu cầu tương tác HTML

### 7.1 Yêu cầu bắt buộc

- Một web app responsive, không tạo hai sản phẩm desktop và mobile riêng.
- Chạy local không cần backend hoặc tài khoản đăng nhập thật.
- Dùng hash route hoặc cơ chế tương đương để mỗi màn hình có URL riêng.
- Có `Demo Scenario Switcher`: Happy Path, Overdue Debt, Stock Shortage, Invoice Rejected, Payment Mismatch và Connector Timeout.
- Có `Reset Demo` để trả toàn bộ trạng thái về điểm bắt đầu.
- Mọi nút chính phải click được và đi đúng bước tiếp theo.
- Nút chưa hỗ trợ phải disabled và có giải thích; không dùng nút giả không phản hồi.
- Mỗi bước hiển thị rõ nguồn hành động:
  - `Agent proposed`;
  - `OPC rule checked`;
  - `Human approved`;
  - `Connector simulated`.
- Dữ liệu và trạng thái phải nhất quán giữa dashboard, đơn hàng, kho, tiền và thuế.
- Màn hình phải hỗ trợ tối thiểu desktop 1440px và mobile 390px.

### 7.2 Trạng thái demo

DEV có thể dùng một object state trong JavaScript để mô phỏng:

- `setup_status`;
- `purchase_status`;
- `batch_status`;
- `inventory_status`;
- `order_status`;
- `shipment_status`;
- `invoice_status`;
- `receivable_status`;
- `payment_status`;
- `tax_period_status`;
- `workflow_status`;
- `approval_status`.

Không yêu cầu database hoặc persistence sau khi đóng browser. Có thể dùng local storage nếu cần giữ bước demo trong cùng máy.

## 8. Trạng thái và ngoại lệ cần mô phỏng

| Đối tượng | Trạng thái tối thiểu |
|---|---|
| Readiness | Chưa bắt đầu, Đang thiết lập, Bị chặn, Sẵn sàng có điều kiện, Sẵn sàng |
| Order | Draft, Chờ duyệt, Đã giữ hàng, Đã xác nhận, Đang giao, Chờ tiền, Đã đóng, Đã hủy |
| Reservation | Active, Consumed, Released, Expired |
| Shipment | Picking, Handed Over, In Transit, Delivered, Failed, Returning |
| Invoice | Draft, Submitted, Issued Simulated, Rejected, Adjusted |
| Payment | Received, Matched, Needs Review, Allocated, Refunded |
| Tax Period | Collecting Data, Needs Review, Ready, Drafted, Approved, Filed Simulated, Paid Simulated, Closed |
| Workflow | Running, Waiting Human, Waiting Connector, Retry Scheduled, Blocked, Completed |

## 9. Yêu cầu giao diện

- Tham khảo visual pattern và onboarding pattern của SoloMatrix v4, nhưng không coi nội dung v4 là requirement đã duyệt.
- Giao diện ưu tiên mobile, từ ngữ ngắn và dễ hiểu.
- Dashboard tập trung vào `Việc cần làm`, không chỉ hiển thị biểu đồ.
- Mỗi status dùng cùng màu và wording trên toàn bộ demo.
- Mọi dữ liệu mô phỏng phải có badge `Simulated` hoặc `Demo data`.
- Approval phải hiển thị: vấn đề, bằng chứng, tác động, đề xuất, người có quyền và nút quyết định.
- Agent Workflow phải tách reasoning khỏi business result đã commit.
- Tax screen phải hiển thị nguồn dữ liệu và cảnh báo không phải tư vấn pháp lý.
- Bảng dài trên mobile chuyển thành card list; không ép bảng desktop vào màn hình nhỏ.

## 10. Ngoài phạm vi bản HTML

- Backend, database, authentication, multi-tenant thật.
- API thật với Zalo, Casso, ngân hàng, hóa đơn, ký số hoặc cổng thuế.
- Nhập OTP, mật khẩu, API key hoặc production credential.
- Tính thuế theo quy định pháp lý thật.
- Phát hành hóa đơn, gửi tờ khai hoặc chuyển tiền thật.
- Offline sync thật.
- Full CRUD cho toàn bộ master data.
- Báo cáo tài chính hoặc hệ thống kế toán đầy đủ.
- Native Android hoặc iOS.

## 11. Tiêu chí bàn giao cho DEV

Bản HTML được coi là đủ để chụp ảnh và present khi:

- Đi được trọn 7 Use Case bằng click, không cần sửa URL thủ công.
- Happy Path chạy từ onboarding đến đóng kỳ thuế.
- Ít nhất 5 ngoại lệ có thể chọn từ Scenario Switcher.
- Trạng thái kho, đơn, hóa đơn, tiền và thuế không mâu thuẫn.
- Người xem phân biệt được Agent, OPC rule, con người và connector.
- Có responsive view ở 1440px và 390px.
- Có Reset Demo.
- Không có claim về integration hoặc pháp lý chưa được xác minh.
- Có thể chụp đủ các màn hình đánh dấu `Có` trong cột proposal.

## 12. Mapping về Feature Catalog

| Use Case | Feature chính |
|---|---|
| UC-01 | F01.01–F01.06, F02.01–F02.06, F13.01–F13.03, F14.01–F14.03 |
| UC-02 | F03.02–F03.07, F04.01–F04.05, F05.01–F05.08 |
| UC-03 | F06.01–F06.08, F05.03–F05.04, F14.02–F14.03 |
| UC-04 | F07.01–F07.06, F08.01–F08.08, F09.01–F09.06 |
| UC-05 | F10.01–F10.06, F11.01–F11.08 |
| UC-06 | F12.01–F12.06, F13.04–F13.05, F14.02–F14.05 |
| UC-07 | F15.01–F15.05, S16.06–S16.09 |

## 13. Tài liệu tham chiếu

- [OPC Feature Catalog](OPC_FEATURE_CATALOG.md)
- [OPC Business Capability Map](OPC_BUSINESS_CAPABILITY_MAP.md)
- [BRD OPC Platform](BRD_OPC_PLATFORM.md)
- [Onboarding Product Flow](../02_OPC_Sales_Agent_Docs/06_Onboarding/ONBOARDING_PRODUCT_FLOW.md)
- [Sales Agent Business and Agent Workflow](../02_OPC_Sales_Agent_Docs/02_Workflow/BUSINESS_AND_AGENT_WORKFLOW.md)
- [Sales Agent Screen Inventory](../02_OPC_Sales_Agent_Docs/03_UX_UI/SCREEN_INVENTORY.md)

## 14. Nội dung có thể gửi trực tiếp cho DEV

> Hãy dựng static clickable HTML cho OPC theo tài liệu này. Bản demo gồm 7 Key Use Case, 20 route và một bộ dữ liệu xuyên suốt. Dùng responsive Web cho desktop 1440px và mobile 390px. Không cần backend, database hoặc API thật. Mọi ngân hàng, hóa đơn, Zalo và thuế phải có nhãn Simulated. Mỗi hành động phải phân biệt Agent proposed, OPC rule checked, Human approved và Connector simulated. Có Scenario Switcher, Reset Demo và trạng thái nhất quán giữa kho, đơn, giao hàng, hóa đơn, tiền và kỳ thuế. Tham khảo visual pattern của SoloMatrix v4 nhưng không sửa hoặc coi nội dung mockup cũ là requirement. Output đề xuất đặt ở folder mới `05_OPC_HTML_Demo`.

# PRD OPC Platform Draft

**Phiên bản:** 0.1  
**Ngày:** 02/10/2026  
**Trạng thái:** Product level draft, chưa Dev ready  
**Product Owner:** Hiếu  
**Điều kiện đầu vào:** Cần chốt BRD trước khi khóa release scope

## 1. Mục đích tài liệu

Tài liệu này chuyển business scope của OPC thành product direction, module và use case cấp cao.

Tài liệu chưa đi vào màn hình, workflow chi tiết, API, state machine, backlog hoặc UAT. Các tài liệu đó chỉ được tạo sau khi product scope và phase đầu được chốt.

## 2. Tóm tắt sản phẩm

OPC Platform là hệ thống vận hành dành cho hộ kinh doanh và doanh nghiệp một người. Sản phẩm giúp một operator theo dõi công việc, để Agent thực hiện việc thường xuyên trong giới hạn cho phép và đưa ngoại lệ cho con người quyết định.

Sản phẩm nối các hoạt động từ thiết lập doanh nghiệp, bán hàng, tiền, hóa đơn, chi phí, sổ sách đến thuế. Mỗi module có thể triển khai theo phase và có thể dùng connector khác nhau.

Sales Operations Agent là vertical demo đầu tiên. Casso là một integration option cho một số use case ngân hàng, hóa đơn, thuế, định danh và ký số.

## 3. Product vision

Giúp một người có thể vận hành doanh nghiệp qua một control tower đáng tin cậy, trong đó:

- dữ liệu và quy tắc xác định bảo vệ tiền, hàng, thuế và trạng thái;
- AI Agent hiểu yêu cầu, phối hợp công việc và giải thích ngoại lệ;
- con người vẫn kiểm soát quyết định rủi ro;
- mọi kết quả đều truy được về nguồn.

## 4. Định vị sản phẩm

### OPC là

- Một nền tảng vận hành theo module.
- Một lớp workflow và control tower nối dữ liệu business.
- Một môi trường để AI Agent làm việc qua công cụ được kiểm soát.
- Một hệ thống review by exception cho operator ít người.

### OPC không phải

- Một wrapper quanh Casso.
- Một chatbot chỉ trả lời câu hỏi.
- Một ERP đầy đủ trong release đầu tiên.
- Một hệ thống để AI tự quyết định tiền, thuế, giá hoặc tồn kho.
- Một dịch vụ tự kê khai, tự ký hoặc tự nộp thay chủ hộ.

## 5. Persona và Jobs To Be Done

### Chủ hộ hoặc owner operator

Khi doanh nghiệp có nhiều giao dịch và nghĩa vụ cần theo dõi, tôi muốn biết việc nào đang chạy, việc nào cần tôi quyết định và kết quả nào đã được xác nhận, để tôi vận hành mà không cần một đội lớn.

### Người kế nghiệp hoặc người vận hành trẻ

Khi tiếp nhận hoạt động của gia đình, tôi muốn có quy trình và dữ liệu rõ ràng trên điện thoại, để không phụ thuộc vào trí nhớ hoặc cách làm riêng của từng người.

### Kế toán hoặc cố vấn nghiệp vụ

Khi cần kiểm tra sổ sách và nghĩa vụ cuối kỳ, tôi muốn thấy nguồn dữ liệu, chênh lệch và quy tắc đã dùng, để tôi xác nhận hoặc sửa đúng chỗ.

### Đội triển khai

Khi đưa một hộ vào sử dụng, tôi muốn biết bước thiết lập nào đã hoàn thành và điều gì đang chặn, để hỗ trợ đúng việc và chứng minh readiness.

### PM chương trình

Khi đánh giá hiệu quả triển khai, tôi muốn thấy adoption, giao dịch, chi phí và rủi ro theo nhóm hộ, để quyết định mở rộng hay điều chỉnh.

## 6. Product journey tổng thể

| Giai đoạn | Kết quả người dùng cần |
|---|---|
| 1. Khởi tạo | Hồ sơ doanh nghiệp, vai trò và chính sách cơ bản được thiết lập. |
| 2. Kết nối | Nguồn dữ liệu và connector cần thiết được cấp quyền và kiểm tra. |
| 3. Vận hành | Bán hàng, mua hàng hoặc cung cấp dịch vụ được ghi nhận thành giao dịch business. |
| 4. Thu chi | Tiền về hoặc tiền đi được nối với giao dịch và chênh lệch được xử lý. |
| 5. Chứng từ | Hóa đơn và chứng từ được tạo, nhận, đồng bộ và kiểm tra. |
| 6. Đối soát | Doanh thu, chi phí, tiền và công nợ được nối và giải thích. |
| 7. Chốt kỳ | Dữ liệu được kiểm tra, tính toán và tạo kết quả nháp. |
| 8. Phê duyệt và thực hiện | Chủ hộ hoặc người có quyền duyệt, ký, gửi hoặc nộp. |
| 9. Theo dõi | Control Tower hiển thị kết quả, ngoại lệ, retry và audit. |

## 7. Product module

| Module | Trách nhiệm chính | Trạng thái định hướng |
|---|---|---|
| Business Setup | Hồ sơ hộ, người dùng, vai trò, chính sách và readiness. | Nền tảng chung. |
| Connection Center | Kết nối ngân hàng, hóa đơn, thuế và dịch vụ khác. | Đánh giá Casso và phương án thay thế. |
| Sales and Fulfilment | Yêu cầu bán, đơn hàng, giá, tồn kho, giao hàng và trạng thái. | Đã có domain PRD và workflow. |
| Money and Receivables | QR, phải thu, giao dịch, khớp tiền và ngoại lệ. | Một phần đã có trong Sales Agent; cần connector thật. |
| Invoice and Documents | Hóa đơn bán ra, hóa đơn đầu vào, trạng thái và lỗi. | Cần xác nhận phạm vi sản phẩm và provider. |
| Purchase and Expense | Mua hàng, chi phí và chứng từ đầu vào. | Chưa được đặc tả; cần cho vòng đời thuế. |
| Books and Reconciliation | Ghi nhận doanh thu, chi phí, tiền và chênh lệch. | OPC tự xây; cần kế toán xác nhận. |
| Tax Workspace | Dữ liệu kỳ, quy tắc, tính toán, bản nháp, gửi và bằng chứng nộp. | Cần tách rõ OPC và third party. |
| Agent Control Tower | Workflow, ngoại lệ, approval, SLA, retry và audit. | Năng lực lõi của OPC. |
| Administration and Analytics | Tenant, cấu hình, usage, cost và kết quả chương trình. | Làm theo nhu cầu rollout, không phải demo tenant switcher. |

## 8. Use case map cấp cao

| Module | Use case | Kết quả mong đợi | Casso có thể liên quan |
|---|---|---|---|
| Business Setup | Thiết lập hồ sơ doanh nghiệp | Hồ sơ và vai trò đủ để vận hành | Tra cứu mã số thuế hoặc định danh nếu được xác nhận. |
| Connection Center | Kết nối và thu hồi quyền | Connector có trạng thái, owner và bằng chứng đồng ý | Cas Link, grant, eKYC hoặc Cas ID. |
| Sales and Fulfilment | Xử lý đơn bán từ yêu cầu không cấu trúc | Đơn được kiểm tra, thực hiện và đóng đúng trạng thái | Không phải phần lõi của Casso. |
| Money and Receivables | Tạo yêu cầu thanh toán | Khách có QR hoặc thông tin thanh toán gắn với giao dịch | QR Pay hoặc dịch vụ tương đương. |
| Money and Receivables | Nhận và khớp tiền | Khoản tiền được xác minh, chống trùng và phân bổ đúng | Casso cung cấp giao dịch; OPC khớp. |
| Money and Receivables | Xử lý tiền thiếu, thừa hoặc không có mã | Ngoại lệ được operator giải quyết có audit | OPC sở hữu workflow. |
| Invoice and Documents | Phát hành và theo dõi hóa đơn bán ra | Hóa đơn có trạng thái và liên kết giao dịch | Invoice Hub hoặc provider trực tiếp. |
| Invoice and Documents | Đồng bộ hóa đơn đầu vào và đầu ra | Dữ liệu hóa đơn đủ để kiểm tra kỳ | GDT Hub nếu được xác nhận hợp lệ. |
| Purchase and Expense | Ghi nhận mua hàng và chi phí | Chi phí và chứng từ được nối với nhà cung cấp | Có thể dùng dữ liệu từ hóa đơn và ngân hàng. |
| Books and Reconciliation | Đối soát đơn, tiền, hóa đơn và sổ | Mọi chênh lệch có trạng thái và lý do | Casso chỉ cấp dữ liệu nguồn. |
| Tax Workspace | Chốt dữ liệu kỳ | Dữ liệu đủ, thiếu và chênh lệch được hiển thị | Có thể lấy dữ liệu hóa đơn từ Casso. |
| Tax Workspace | Tính thuế và tạo bản nháp | Kết quả được tạo bằng quy tắc đã xác nhận | OPC tự xây; Casso không phải bộ tính thuế. |
| Tax Workspace | Duyệt, ký và gửi tờ khai | Chủ hộ thực hiện hành động bắt buộc và nhận kết quả | Tax Return hoặc eSign chỉ dùng sau khi kiểm chứng. |
| Tax Workspace | Ghi nhận việc nộp tiền | Có bằng chứng để cập nhật trạng thái kỳ | Hiện chưa có bằng chứng Casso hỗ trợ nộp tiền. |
| Agent Control Tower | Xử lý ngoại lệ và approval | Agent đề xuất, con người quyết định, hệ thống ghi nhận | Không phụ thuộc Casso. |
| Agent Control Tower | Theo dõi lỗi connector | Lỗi, retry, fallback và SLA được quản lý | Casso cung cấp trạng thái và điều kiện vận hành. |

## 9. Phạm vi theo phase

### Phase 0 Static onboarding demo

- Giải thích product, vai trò, dữ liệu, connector và readiness.
- Dùng dữ liệu và kết nối mô phỏng.
- Đã có bộ tài liệu riêng trong folder `06_Onboarding`.

### Phase 1 Sales Operations Agent demo

- Chứng minh vertical slice từ yêu cầu khách hàng đến giao hàng, hóa đơn, thu tiền và đóng đơn.
- Dùng ERP slice tối thiểu, Agent workflow, approval và audit.
- Không đại diện cho toàn bộ OPC Platform.

### Phase 2 Money and Invoice validation

- Kiểm chứng tài khoản mục tiêu, QR, webhook, giao dịch, đối soát và hóa đơn.
- Xác định connector thật, simulator, fallback, vận hành và chi phí.
- Không mở rộng sang toàn bộ accounting hoặc tax filing nếu dữ liệu chưa đủ.

### Phase 3 Books and Tax validation

- Bổ sung purchase, expense, sổ nghiệp vụ, chốt kỳ và bộ tính thuế xác định.
- Kiểm chứng đường tạo bản nháp, gửi, nộp và bằng chứng.
- Chỉ pilot sau khi kế toán và dependency được xác nhận.

### Phase 4 Pilot and rollout

- Pilot với nhóm hộ và ngành đã chọn.
- Đo adoption, độ chính xác, thời gian, lỗi, chi phí và hỗ trợ vận hành.
- Chỉ mở rộng quy mô khi pilot đạt exit criteria.

## 10. Product requirement cấp cao

### Must have ở cấp nền tảng

- Mỗi dữ liệu và workflow phải thuộc đúng tenant hoặc hộ.
- Mỗi hành động phải biết nguồn, actor, thời gian, trạng thái và lý do.
- Agent chỉ gọi các hành động business đã được cho phép.
- Mọi thay đổi tiền, tồn kho, giá, thuế và trạng thái phải qua dịch vụ xác định.
- Hành động lặp lại phải chống tạo bản ghi hoặc chứng từ trùng.
- Hệ thống phải dừng và yêu cầu người xử lý khi dữ liệu thiếu, mâu thuẫn hoặc rủi ro.
- Connector phải có trạng thái, lần kiểm tra gần nhất, lỗi, retry và hướng khôi phục.
- Người dùng phải biết phần nào do Agent đề xuất, OPC xác nhận, con người duyệt hoặc connector trả về.
- Audit log phải chỉ ghi thêm và không cho người dùng sửa lịch sử.
- Product phải hoạt động trên responsive Web/PWA; mobile là bề mặt ưu tiên.

### Should have

- Policy có thể cấu hình theo tenant hoặc nhóm hộ.
- Có chế độ hướng dẫn cho người mới và chế độ review by exception cho người đã quen.
- Có cảnh báo về công việc chờ, connector lỗi, chênh lệch và hạn xử lý.
- Có fallback rõ khi connector không hoạt động.
- Có usage và cost view cho PO hoặc admin chương trình.

### Chưa đưa vào release đầu

- Full ERP cho mọi ngành.
- Tự động chuyển tiền, ký, gửi hoặc nộp thay chủ hộ.
- AI tự thay đổi công thức thuế hoặc chính sách business.
- Production rollout cho toàn bộ 3.000 user.
- Native mobile app riêng nếu Web/PWA chưa được chứng minh là không đủ.

## 11. Ranh giới trách nhiệm

| Thành phần | Được làm | Không được tự làm |
|---|---|---|
| OPC deterministic core | Lưu dữ liệu, tính toán, kiểm tra rule, đổi trạng thái và ghi audit. | Không dùng kết quả AI chưa được kiểm tra làm số liệu chuẩn. |
| AI Agent | Đọc dữ liệu không cấu trúc, lập kế hoạch, đề xuất và giải thích. | Không tự đoán tiền, thuế, giá, tồn kho hoặc trạng thái cuối. |
| Con người | Xác nhận thông tin, duyệt ngoại lệ, ký, gửi hoặc thực hiện bước bắt buộc. | Không được bỏ qua rule và audit bằng chỉnh dữ liệu trực tiếp. |
| Casso hoặc third party | Cung cấp connector, dữ liệu và trạng thái theo hợp đồng đã xác nhận. | Không sở hữu logic business, đối soát, tax rule hoặc workflow OPC. |
| Kế toán | Xác nhận nghiệp vụ, nguồn quy tắc và ví dụ chuẩn. | Không thay PO quyết định product scope hoặc thay DEV quyết định kiến trúc. |

## 12. Product rule

1. ERP hoặc business core là nguồn dữ liệu chuẩn cho transaction state.
2. Casso không phải nguồn chuẩn cho order, receivable, tax calculation hoặc workflow state.
3. Một webhook không đủ để kết luận tiền thật nếu chưa đáp ứng quy tắc xác minh được chốt.
4. Không tự gửi lại một hành động có thể tạo hóa đơn hoặc giao dịch trùng.
5. Việc gửi, ký, nộp hoặc chuyển tiền phải có người dùng và bằng chứng phù hợp.
6. Quy tắc thuế phải có nguồn, ngày hiệu lực, người xác nhận và bộ test.
7. Khi connector lỗi, workflow chuyển sang blocked hoặc needs review, không tự hoàn thành.
8. Thay connector không được làm thay đổi business outcome hoặc audit contract.

## 13. Nguyên tắc trải nghiệm

- Bắt đầu từ việc người dùng muốn hoàn thành, không bắt đầu từ tên API hoặc provider.
- Hiển thị một luồng xuyên suốt thay vì bắt người dùng nối nhiều module bằng trí nhớ.
- Mỗi ngoại lệ phải có vấn đề, bằng chứng, tác động và hành động tiếp theo.
- Mobile first nhưng không thu nhỏ một dashboard desktop quá nhiều thông tin.
- Hướng dẫn thiết lập phải cho biết giá trị trước khi yêu cầu nhập dữ liệu hoặc kết nối.
- Trạng thái simulated, unverified, sandbox và live phải được phân biệt rõ.
- Không dùng wording khiến người dùng hiểu AI hoặc OPC chịu trách nhiệm pháp lý thay họ.

## 14. Chỉ số thành công

### Chỉ số product cần đo

- Tỷ lệ người dùng hoàn thành onboarding và first value.
- Tỷ lệ use case hoàn thành không cần nhập lại dữ liệu.
- Tỷ lệ giao dịch được khớp tự động và tỷ lệ phải review.
- Tỷ lệ ngoại lệ được xử lý đúng hạn.
- Số lỗi trùng giao dịch, hóa đơn hoặc trạng thái.
- Thời gian từ sự kiện business đến khi operator nhận được cảnh báo.
- Tỷ lệ người dùng phân biệt đúng Agent, OPC rule, con người và connector.
- Chi phí connector trên mỗi hộ hoạt động và mỗi giao dịch thành công.
- Retention sau 30 và 90 ngày đối với pilot.

Mức mục tiêu chưa được tự đặt trong PRD này. PO cần baseline và pilot plan trước khi khóa target.

## 15. Non functional requirement cấp cao

- **Bảo mật:** secret không nằm trong client; quyền truy cập theo tenant và vai trò.
- **Riêng tư:** dữ liệu cá nhân được che, có mục đích sử dụng và thời hạn lưu.
- **Tin cậy:** idempotency, retry có kiểm soát, quarantine và phục hồi sau lỗi.
- **Audit:** log business chỉ ghi thêm và liên kết được với source event.
- **Quan sát:** đo độ trễ, lỗi, độ tươi dữ liệu và tình trạng connector.
- **Hiệu năng:** mục tiêu cụ thể sẽ được chốt theo pilot và khả năng provider.
- **Khả dụng:** có cách xử lý khi mạng yếu hoặc connector gián đoạn; mức offline còn mở.
- **Khả năng thay thế:** integration qua adapter và contract ổn định.
- **Khả năng tiếp cận:** wording đơn giản, nút và trạng thái phù hợp người dùng mobile.

## 16. Dependency

- BRD được phê duyệt.
- PM Quang xác nhận nhóm người dùng, quy mô và điểm kết thúc phase đầu.
- Kế toán xác nhận quy tắc, mẫu và dữ liệu nghiệp vụ.
- Casso xác nhận tài khoản hỗ trợ, API, sandbox, bảo mật, SLA và giá.
- DEV xác nhận kiến trúc tenant, data model, integration và recovery.
- UX kiểm tra onboarding và control tower với người dùng mục tiêu.
- Có pilot plan, support model và measurement plan.

## 17. Rủi ro product

| Rủi ro | Cách kiểm soát |
|---|---|
| Scope quá rộng | Tách vision, phase và release; không coi mọi module là Must của MVP. |
| Dùng report Casso như requirement đã duyệt | Mọi capability phải quay về use case và được xác minh. |
| AI automation vượt quá kiểm soát | Tool allowlist, deterministic validation và approval gate. |
| Dữ liệu nguồn không sạch | Readiness check, reconciliation queue và ownership rõ. |
| Connector thiếu hoặc thay đổi | Adapter, contract test, fallback và monitoring. |
| Product không phù hợp mobile thực tế | Test với thiết bị và mạng của nhóm pilot. |
| Tax scope tạo claim pháp lý | Kế toán xác nhận, nguồn theo ngày và wording giới hạn. |
| Chi phí không phù hợp 3.000 user | Mô hình low, base, high và đo usage pilot. |

## 18. Quyết định product còn mở

| Quyết định | Người chốt | Chặn bước nào |
|---|---|---|
| Persona và ngành pilot đầu tiên | PM Quang | UX, dữ liệu mẫu và pilot. |
| Điểm kết thúc release đầu tiên | PM Quang | Detailed PRD và roadmap. |
| Purchase and Expense có thuộc phase đầu | PM Quang và kế toán | Books and Tax scope. |
| Tax Workspace dừng ở tính nháp hay hỗ trợ gửi | PM Quang và kế toán | Integration và legal review. |
| Dùng connector thật ở phase nào | PM Quang và PO | Architecture và release criteria. |
| Mức offline cần hỗ trợ | PM Quang và DEV | Web/PWA architecture. |
| Cách tính tenant cho 3.000 user | PM Quang và DEV | Data model, security và cost. |
| Success target của pilot | PM Quang và PO | Go or no go decision. |

## 19. Điều kiện để tạo tài liệu chi tiết

Chưa nên sinh SRS, backlog tổng thể hoặc workflow cho tất cả module.

Có thể tạo tài liệu chi tiết khi:

- BRD được chốt.
- Module map và use case map được đồng ý.
- Phase đầu và điểm kết thúc được xác nhận.
- Các câu hỏi chặn về kế toán và Casso có owner.
- Một vertical slice được chọn để viết workflow và acceptance criteria.
- Product team thống nhất đâu là demo, pilot và production.

Khi đủ điều kiện, thứ tự tài liệu tiếp theo nên là:

1. Use Case Catalogue cho phase đã chọn.
2. Casso and Third Party Capability Mapping.
3. Business and Agent Workflow.
4. Functional and Non Functional Requirements.
5. UX flow và screen specification.
6. Backlog, UAT và handoff.

## 20. Tài liệu nguồn

- [BRD OPC Platform](BRD_OPC_PLATFORM.md)
- [PRD OPC Sales Operations Agent](../02_OPC_Sales_Agent_Docs/01_PRD/PRD_OPC_SALES_AGENT.md)
- [Business and Agent Workflow](../02_OPC_Sales_Agent_Docs/02_Workflow/BUSINESS_AND_AGENT_WORKFLOW.md)
- [Onboarding Product Flow](../02_OPC_Sales_Agent_Docs/06_Onboarding/ONBOARDING_PRODUCT_FLOW.md)
- [Casso Feasibility Scope](../02_OPC_Sales_Agent_Docs/07_Casso_Feasibility/CASSO_FEASIBILITY_SCOPE.md)
- [Casso Requirements and Flow Matrix](../02_OPC_Sales_Agent_Docs/07_Casso_Feasibility/REQUIREMENTS_AND_FLOW_MATRIX.md)
- [Report Casso cho SoloMatrix](../Casso%20cho%20SoloMatrix/index.html)
- Biên bản họp ngày 30/09/2026 do người dùng cung cấp.


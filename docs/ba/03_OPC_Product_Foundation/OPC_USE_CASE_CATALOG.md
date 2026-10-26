# OPC Use Case Catalog — Ba nghiệp vụ chính

**Phiên bản:** 0.8  
**Ngày:** 07/10/2026  
**Product Owner:** Hiếu  
**Trạng thái:** Bản phân tích để PO review; chưa phải SRS hoặc cam kết triển khai.  
**Baseline tham chiếu:** BRD 0.9; Capability Map 0.6; Feature Catalog 0.4; Business Flow Explainer 0.3.  
**Quyết định mới nhất:** PO xác nhận trong chat ngày 07/10/2026, ưu tiên hơn phần mô tả cũ bị thay thế bên dưới.

## 0. Quyết định đã chốt ngày 07/10/2026

| Nội dung | Quy tắc hiện tại |
|---|---|
| Tạo đơn | Hai cách: Agent đọc Zalo và đề xuất để chủ hộ duyệt; hoặc chủ hộ tự tạo/xác nhận đơn, không duyệt thêm lần nữa. |
| Tạo đơn mua | Agent nhận biết ý định mua từ thông tin được cung cấp và đề xuất để chủ hộ xác nhận; hoặc chủ hộ tự tạo/xác nhận trên OPC. Đặt hàng trao đổi bên ngoài; nhà cung cấp không cần tài khoản hoặc duyệt trên OPC. |
| Nhận hàng mua | Mở đơn → bấm “Nhận hàng” → kiểm tra/sửa lượng mặc định theo đơn thành số thực nhận → bấm “Xác nhận nhập kho”. Tăng tồn đúng một lần theo thực nhận; nhận 18/20 thì tăng 18, còn thiếu 2, không tự ghi đã trả tiền. |
| Trả tiền mua | Chủ hộ mở đơn → “Ghi nhận đã trả tiền” → chọn tiền mặt/chuyển khoản, nhập số tiền/ngày trả → xác nhận. Trả đủ một lần, có thể trước hoặc sau nhận hàng; không triển khai ứng trước một phần/trả nhiều lần. Agent hỗ trợ đối chiếu, không chuyển tiền. |
| Sửa/hủy đơn mua | Chưa nhận hàng và chưa trả tiền: chủ hộ được sửa/hủy, lưu lịch sử. Đã phát sinh hàng hoặc tiền: không hủy để xóa giao dịch cũ, xử lý hàng/tiền riêng ở bước refinement sau, ngoài happy path. |
| Giao tiếp khách | Agent không tự gửi tin Zalo. Chủ hộ tự trao đổi, báo giá và báo lượng hàng cho khách. |
| Tồn kho | Chủ hộ xem tồn hoặc hỏi Agent. Lượng xác nhận trên đơn không vượt tồn khả dụng lúc xác nhận. Không có đơn xác nhận chờ nhập thêm hoặc giữ một phần. |
| Thiếu tồn | Kho còn 6, khách hỏi 10: chủ hộ sửa đơn thành tối đa 6; muốn bán 10 thì nhập thêm và cập nhật kho trước xác nhận đơn 10. |
| Đơn vị tính | Chủ hộ tự thiết lập field đơn vị/quy cách. Không mặc định có tự quy đổi thùng–chai. |
| Giá và nợ | Chủ hộ thiết lập giá, không có nghiệp vụ giảm giá/phê duyệt giảm giá. Theo dõi đơn chưa đóng là còn chờ thanh toán/công nợ; giữ riêng tiền thực nhận, không tự áp hạn mức/chặn nợ quá hạn. |
| Giao tay | Chuẩn bị theo đơn; chủ hộ bấm “Đã giao” nghĩa là giao đủ theo đơn. Không nhập lại số lượng, không giao thiếu hoặc nhiều lần. |
| Kho và hóa đơn | “Đã giao” trừ kho một lần theo lượng đơn và kích hoạt bước hóa đơn. Một hóa đơn theo đơn; kế toán/provider xác minh phần thực thi. |
| Tiền và đóng đơn | Có tiền thực nhận được ghi nhận cho đơn → OPC đề xuất đóng → chủ hộ xác nhận. Giao hàng, hóa đơn và tiền dư không chặn đóng đơn, cũng không tự thành hoàn tất khi đơn đóng. |
| Tiền dư | Lưu đúng số thực nhận và note; chủ hộ tự xử lý. Không tự hoàn, đổi hóa đơn hoặc ghi dư là doanh thu. |
| Thứ tự thao tác | Thu tiền có thể trước hoặc sau giao. Đơn đã đóng vẫn hiện và xử lý được việc giao/hóa đơn còn chờ, không bị ẩn hoặc khóa việc đó. |
| Pilot thuế | Tập trung Phân phối, cung cấp hàng hóa; chủ hộ điền ngành nghề đã đăng ký khi onboarding. |
| Mẫu thuế | PO chọn file 01_CNKD_TT40_2026_9172.xlsx làm mẫu phân tích. Kế toán cần xác minh tính phù hợp và quy tắc áp dụng; chưa map trường/công thức trong lượt này. |
| Nguồn hóa đơn | Hóa đơn điện tử qua provider; chứng từ viết tay cho chụp ảnh và nhập thông tin thủ công. OCR làm sau. Không coi ảnh chụp là xác nhận chứng từ hợp lệ cho thuế. |
| Dữ liệu quý | Chủ hộ chọn quý/năm. Tổng hợp riêng hóa đơn bán ra và mua vào theo ngày lập hóa đơn; xổ danh sách theo tháng/ngày và mở chi tiết. Happy path mọi giao dịch mua/bán có hóa đơn. |
| Tổng và tiền | Doanh thu bán ra, giá trị mua vào và tiền thực thu/chi là các số riêng. Không lấy thu trừ chi làm doanh thu, không mặc định mua vào được khấu trừ thuế. |
| Sửa dữ liệu quý | Chủ hộ được sửa dữ liệu; lưu lịch sử và cảnh báo cần kiểm tra lại nếu đã xác nhận. Không sửa trực tiếp hóa đơn điện tử đã phát hành hoặc thay kết quả kê khai cũ. |
| Tiến trình kê khai | Chuẩn bị dữ liệu → chủ hộ kiểm tra → thực hiện trên eTax → ghi nhận đã gửi → chờ cập nhật kết quả. Đây là tiến trình OPC, không phải trạng thái chính thức eTax. |
| Kết quả eTax | API provider nếu được xác minh; nếu không có API, chủ hộ tự cập nhật và đính kèm bằng chứng, ghi rõ chưa đối chiếu qua eTax. Sau gửi để chờ cập nhật, không tự coi đã chấp nhận/đã nộp tiền hoặc hoàn thành nghĩa vụ. |
| Phần thuế còn mở | Cách tính GTGT/TNCN, mapping trường tờ khai và điều kiện hoàn thành kỳ chờ kế toán/provider. Không để Agent tự tính từ suy đoán. |

BRD/Capability/Feature/Flow ở các phiên bản nêu trên đã đồng bộ quyết định PO ngày 07/10, gồm mua/nhận/trả/sửa-hủy, bán/giao/đóng đơn và thuế quý. Mã Feature/UC giữ để trace; F02.06 chỉ giữ lịch sử, ngoài phạm vi hiện tại. Word, slide/demo, PRD draft và bộ Sales Agent cũ chưa đồng bộ lượt này. Đồng bộ tài liệu không có nghĩa đã Dev-ready hoặc đã xác minh kế toán/provider.

## 1. Mục đích và cách đọc

Mỗi Use Case mô tả một việc có kết quả mà chủ hộ nhận biết được: cần gì để bắt đầu, chủ hộ thực hiện gì, Agent hỗ trợ gì, OPC kiểm soát gì và hồ sơ thay đổi thế nào. Một Feature có thể tham gia nhiều Use Case; một Use Case có thể dùng nhiều Feature.

Catalog gồm **33 Use Case**: 8 mua hàng/kho, 14 bán hàng/hóa đơn/tiền, 8 sổ sách/hướng dẫn eTax và 3 hỗ trợ dùng chung. Đây không phải 33 màn hình hoặc 33 User Story.

- **UC-xx:** mã nội bộ được tạo trong catalog để trace, không phải mã từ tỉnh hoặc Casso.
- **ĐÃ CHỐT:** phạm vi/quy tắc có trong baseline; chưa chứng minh đã có code, hợp pháp hoặc provider hỗ trợ.
- **ĐỀ XUẤT:** cách tách Use Case, thứ tự thao tác và tên trạng thái để review; không tự thay phạm vi đã duyệt.
- **OPEN:** chi tiết chưa quyết định; ghi mã Q-xx ở cuối file, không lấp bằng suy đoán.
- **CẦN XÁC MINH:** cần căn cứ kế toán hoặc provider trước chạy thật.

Các luồng dưới đây là cách phân rã đề xuất từ nghiệp vụ đã chốt. Tên trạng thái là nhãn business, chưa phải enum database hoặc State Machine cuối cùng. Điều kiện hậu chỉ áp dụng khi thành công; thất bại phải giữ hồ sơ/ngoại lệ, không giả hoàn thành.

### 1.1 Maturity và Pattern

Không dùng Emerging/Advanced để ngụ ý OPC đã triển khai hoặc có mức trưởng thành kỹ thuật. Tham khảo cách catalog liên kết tình huống với mẫu thực hiện ở [Adobe Use Case Catalog](https://experienceleague.adobe.com/en/docs/blueprints-learn/architecture/industry-use-cases/use-case-catalog); nhãn dưới đây do OPC đề xuất cho nhu cầu review.

| Mức độ | Ý nghĩa |
|---|---|
| M1 — Đủ mô tả business | Kết quả và quy tắc trọng yếu đã có; vẫn cần UX, AC và kiểm thử trước DEV. |
| M2 — Chờ quy tắc | Thiếu quyết định về quyền, điều kiện, dữ liệu hoặc trạng thái; chưa Dev-ready. |
| M3 — Chờ xác minh | Phụ thuộc kế toán, mẫu biểu hoặc provider; chưa đủ căn cứ chạy thật. |

Mức độ áp dụng cho toàn Use Case, lấy theo điểm thiếu quan trọng nhất. Pattern là cách thực hiện, không phải kiến trúc đã chọn: **nhập tay có hỗ trợ**, **human xác nhận**, **đề xuất → duyệt**, **sự kiện tích hợp**, **đối soát có nguồn**, **hướng dẫn có nguồn**.

### 1.2 Ranh giới trách nhiệm chung

| Chủ hộ / người có quyền | Agent — AI reasoning | OPC — logic xác định |
|---|---|---|
| Nhập tay, kiểm tra, xác nhận thực tế; duyệt hoặc từ chối đề xuất; giải quyết ngoại lệ. | Hiểu tin nhắn/tài liệu, gợi ý liên kết, diễn giải chênh lệch và chuẩn bị phương án. Không đoán dữ liệu thiếu. | Kiểm tra dữ liệu/quyền, tính tiền và tồn theo rule, ghi giao dịch, chống trùng và chuyển trạng thái. |

Chủ hộ luôn có đường thao tác tay trong OPC theo quyền, trên **cùng hồ sơ** Agent đang hỗ trợ. Điều này không cho phép vượt rule, sửa hóa đơn đã phát hành trực tiếp hoặc tự bịa kết quả provider. Kế toán xác nhận nghiệp vụ; PO Hiếu là đầu mối thu thập quyết định, không mặc định kế toán có quyền thao tác trong app.

Khách hàng/nhà cung cấp trao đổi bên ngoài, chưa có yêu cầu portal hoặc tài khoản riêng. Agent không tự gửi tin Zalo; chủ hộ tự trao đổi với khách. Không phát hành chứng từ, chuyển tiền hoặc duyệt thay người dùng khi quyền/chính sách chưa rõ.

### 1.3 Dữ liệu và audit áp dụng cho mọi Use Case

Mọi hồ sơ phải có mã nội bộ, hộ sở hữu, nguồn nhập/tích hợp, thời gian và người thực hiện. Dữ liệu bảng bên dưới là **dữ liệu cần phân tích**, chưa phải danh sách trường DB bắt buộc đã duyệt.

Audit **chỉ ghi thêm**: UC, hồ sơ và phiên bản nguồn, actor người/Agent/system, hành động, thời gian, trước/sau, kết quả kiểm tra, quyết định/lý do, bằng chứng và ID sự kiện bên ngoài khi có. Sửa sai tạo phiên bản/bản ghi xử lý tiếp, không xóa lịch sử. Đề xuất Agent lưu căn cứ và hành động dự kiến, không yêu cầu lưu suy nghĩ nội bộ của mô hình.

Không chạy lại hành động gây tiền/hàng/chứng từ trùng. Khi kết quả bên ngoài chưa rõ, tra cứu hoặc chuyển chờ xử lý trước retry. Số lần retry, thời hạn, lưu audit và chính sách offline còn OPEN.

## 2. Danh mục và đường đi end-to-end

**Mua:** UC-01 → UC-02 → UC-03 → UC-05; UC-04 cho chi phí không qua kho; UC-06/08 cho ngoại lệ; UC-07 xem/kiểm kê kho.

**Bán:** Zalo → Agent đề xuất → chủ hộ duyệt, hoặc chủ hộ tự tạo/xác nhận. UC-11 kiểm tra giá/tồn → UC-12 xác nhận → UC-13 giữ đủ → UC-14 chuẩn bị → UC-15 “Đã giao” → UC-16 hóa đơn. Thu tiền UC-17–UC-20 có thể trước hoặc sau giao; có thực nhận cho đơn → UC-22 đề xuất đóng → chủ hộ xác nhận. Không bắt hoàn tất giao/hóa đơn mới đóng. UC-21 sửa/hủy theo quyền.

**Sổ/thuế:** thiết lập thông tin hộ/ngành nghề UC-31 → nguồn phát sinh vào UC-23/24 → chọn quý/năm, xem tổng và hóa đơn theo tháng/ngày UC-26 → chủ hộ kiểm tra → hướng dẫn UC-27 → chủ hộ thực hiện trên eTax → UC-30 ghi nhận đã gửi và bằng chứng → UC-29 theo dõi/chờ cập nhật kết quả. UC-28 cho sửa/bổ sung có lịch sử, không thay kết quả cũ. UC-25 là khóa sổ riêng, không tự tạo bước khóa dữ liệu chuẩn bị kê khai. Chưa chốt tự tính GTGT/TNCN, mapping mẫu hoặc đóng kỳ thuế.

| ID | Tên Use Case | Primary Actor / Trigger | Feature chính | Nguồn flow | Maturity / Pattern |
|---|---|---|---|---|---|
| UC-01 | Lập và xác nhận đơn mua | Chủ hộ / có ý định mua, Agent đề xuất hoặc đã nhận vật lý | F03.01, F03.02 | §3.1 bước 1; PO 07/10 | M2 / đề xuất → xác nhận hoặc nhập tay |
| UC-02 | Xác nhận thực nhận và nhập kho | Chủ hộ / hàng thực đến | F03.03, F05.02 | §3.1 bước 2 | M1 / human xác nhận |
| UC-03 | Gắn và kiểm tra chứng từ mua | Chủ hộ / nhận hóa đơn/chứng từ | F03.06, F09.04, F09.05, F09.07 | §3.1 bước 3 | M3 / đối soát có nguồn |
| UC-04 | Ghi chi phí không qua kho | Chủ hộ / phát sinh chi phí | F03.05, F03.06 | §3.1 bước 3 | M3 / nhập tay có hỗ trợ |
| UC-05 | Ghi khoản chi và đối chiếu phải trả | Chủ hộ; provider gửi dữ liệu / có khoản chi | F03.07, F08.02, F08.04, F08.09 | §3.1 bước 4 | M3 / đối soát có nguồn |
| UC-06 | Xử lý thiếu, thừa, hỏng hoặc trả hàng mua | Chủ hộ / nhận hàng lệch đơn | F03.04, F05.02 | §3.2; capability 6.3 | M2 / human xác nhận |
| UC-07 | Xem tồn, kiểm kê và điều chỉnh kho | Chủ hộ / cần kiểm tra lượng hàng | F05.03, F05.07, F05.08 | §3; capability 6.5 | M2 / human xác nhận |
| UC-08 | Thay đổi hoặc hủy đơn mua | Chủ hộ / thay đổi nhu cầu mua | F03.02 | capability 6.3 | M2 / human xác nhận |
| UC-09 | Tiếp nhận yêu cầu bán | Chủ hộ; connector Zalo kích hoạt / khách yêu cầu | F06.01, F06.02 | §4.1 bước 1 | M3 / nhập tay hoặc sự kiện |
| UC-10 | Làm rõ khách hàng và hàng cần mua | Chủ hộ / dữ liệu thiếu hoặc mơ hồ | F06.03, F02.01, F02.03 | §4.1 bước 1 | M2 / nhập tay có hỗ trợ |
| UC-11 | Kiểm tra giá, tồn và thông tin đơn chưa đóng | Chủ hộ / yêu cầu đã rõ hoặc hỏi tồn | F02.05, F05.03, F06.04–F06.05, F06.08 | §4.1 bước 2 + PO 07/10 | M1 / nhập tay có hỗ trợ |
| UC-12 | Tạo và xác nhận đơn bán | Chủ hộ / Agent đề xuất hoặc tự nhập | F06.07, F14.02, F14.03 | §4.1 bước 3 + PO 07/10 | M1 / hai cách tạo đơn |
| UC-13 | Giữ hoặc giải phóng hàng cho đơn | Chủ hộ; OPC sau xác nhận / đơn đã duyệt | F05.03, F05.04 | §4.1 bước 4 | M2 / logic xác định |
| UC-14 | Chuẩn bị hàng để giao | Chủ hộ / đơn xác nhận đã giữ đủ | F07.01, F07.02 | §4.1 bước 5 + PO 07/10 | M1 / human thực hiện |
| UC-15 | Bấm “Đã giao” và cập nhật kho | Chủ hộ / giao tay đủ theo đơn | F07.04–F07.05, F05.05 | §4.1 bước 5 + PO 07/10 | M1 / human xác nhận |
| UC-16 | Phát hành, theo dõi và gửi hóa đơn bán | Chủ hộ; provider trả kết quả / có sự kiện giao | F09.01–F09.03, F09.07 | §4.1 bước 6 | M3 / sự kiện tích hợp |
| UC-17 | Tạo yêu cầu thanh toán hoặc QR | Chủ hộ / yêu cầu khách trả tiền | F08.03 | §4.1 bước 7 | M3 / tích hợp có kiểm tra |
| UC-18 | Nhận tiền ngân hàng và khớp theo rule | Provider kích hoạt; chủ hộ giám sát / tiền về | F08.04–F08.06 | §4.1 bước 7 | M3 / sự kiện tích hợp |
| UC-19 | Ghi nhận thu tiền mặt | Chủ hộ / đã thực nhận tiền mặt | F08.09, F08.01 | §4.1 bước 7 | M2 / human xác nhận |
| UC-20 | Phân bổ tiền và ghi chú chênh lệch | Chủ hộ / chưa khớp, thiếu hoặc dư | F08.07, F10.04 | §4.1 bước 8 | M2 / đối soát có nguồn |
| UC-21 | Thay đổi hoặc hủy đơn bán | Chủ hộ / khách báo thay đổi/hủy | F06.07, F05.04; F09.06 nhánh sau | §4.4 | M2 / human xác nhận |
| UC-22 | Đề xuất và xác nhận đóng đơn khi nhận tiền | Chủ hộ / tiền thực nhận đã gắn với đơn | F06.07, F08.01, F08.07, F08.09, F15.01 | PO 07/10 thay §4.2 cũ | M1 / đề xuất → xác nhận |
| UC-23 | Ghi sổ và truy nguồn giao dịch | Chủ hộ; OPC ghi theo nguồn / giao dịch hợp lệ | F10.01, F10.02 | §5.1 bước 1 | M3 / logic xác định |
| UC-24 | Đối soát và xử lý ngoại lệ sổ sách | Chủ hộ / có dữ liệu lệch/thiếu | F10.03–F10.05 | §5.1 bước 2 | M3 / đối soát có nguồn |
| UC-25 | Khóa hoặc mở lại kỳ sổ | Chủ hộ/người có quyền / đề nghị chốt hoặc sửa kỳ | F10.06 | capability 6.10 | M2 / đề xuất → duyệt |
| UC-26 | Chọn quý, tổng hợp và kiểm tra hóa đơn | Chủ hộ / chuẩn bị quý kê khai | F11.01, F11.02; F10.02, F09.05 | §5.1 bước 2–3; PO 07/10 | M3 / logic xác định |
| UC-27 | Xem hướng dẫn và hỏi về trường tờ khai | Chủ hộ / cần điền eTax | F11.03–F11.05 | §5.1 bước 3–4 | M3 / hướng dẫn có nguồn |
| UC-28 | Xử lý yêu cầu sửa hoặc bổ sung | Chủ hộ / phát hiện sai hoặc eTax yêu cầu | F11.06 | §5.1 bước 5 | M3 / hướng dẫn có nguồn |
| UC-29 | Theo dõi tiến trình và kết quả kê khai | Chủ hộ; provider nếu có API được xác minh / xem hoặc cập nhật kết quả | F11.07, F13.03 | §5.1 bước 6; PO 07/10 | M3 / có nguồn + cập nhật tay |
| UC-30 | Ghi nhận đã gửi và lưu bằng chứng | Chủ hộ / đã thực hiện trên eTax | F11.08, F15.03 | §5.1 bước 6; PO 07/10 | M3 / human xác nhận |
| UC-31 | Chuẩn bị dữ liệu nền dùng cho giao dịch | Chủ hộ / onboarding, thêm hoặc sửa dữ liệu | F01.01, F01.03–F01.04, F02.01–F02.07, F05.01 | capability 6.1–6.2 | M2 / nhập tay có hỗ trợ |
| UC-32 | Thiết lập và kiểm tra kết nối cần dùng | Chủ hộ/người có quyền / kết nối nguồn | F13.01–F13.05 | capability 6.13 | M3 / consent + kiểm tra |
| UC-33 | Theo dõi, duyệt ngoại lệ và tiếp tục bằng tay | Chủ hộ / việc chờ, lỗi hoặc cần điều khiển | F12.01–F12.06, F14.01–F14.05, F15.01 | capability 6.12–6.15 | M2 / đề xuất → duyệt |

§ trong cột nguồn là mục của [Business Flow Explainer](OPC_BUSINESS_FLOW_EXPLAINER.md). “Capability” là mục của [Capability Map](OPC_BUSINESS_CAPABILITY_MAP.md). Feature là mã trong [Feature Catalog](OPC_FEATURE_CATALOG.md), không phải mã tính năng đã triển khai.

## 3. Mua hàng và kho — Procure-to-Pay

### UC-01 — Lập và xác nhận đơn mua

**Mục tiêu:** có hồ sơ mua hàng để nhận kho và truy tiền/chứng từ. **Actor:** chủ hộ; Agent hỗ trợ; nhà cung cấp trao đổi ngoài OPC. **Trigger:** Agent nhận biết ý định mua từ thông tin được cung cấp, chủ hộ chủ động tạo đơn, hoặc đã nhận hàng vật lý nhưng chưa có đơn. **Maturity/Pattern:** M2 / đề xuất → xác nhận hoặc nhập tay; quy tắc tạo đã chốt, chi tiết dữ liệu còn refinement. **Map:** F03.01–F03.02, F02.02–F02.04; flow §3.1 bước 1 và PO 07/10. **Scope:** luồng chính; không cần tài khoản hoặc bước duyệt của nhà cung cấp trên OPC.

**Pre-conditions:** đã có quyền và một kho; nhận diện được nhà cung cấp, SKU và đơn vị tính. Không bắt buộc đã nhận vật lý. **Dữ liệu:** nguồn nhu cầu, nhà cung cấp, hàng, số lượng, đơn vị, giá mua, thời điểm đặt/nhận; chứng từ hoặc ghi chú nếu có.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Cung cấp nhu cầu mua để xem đề xuất Agent; hoặc tự chọn nhà cung cấp, hàng và nhập lượng/giá trên OPC. | Nhận biết ý định mua từ nguồn được phép truy cập, gợi ý đơn và hỏi dữ liệu còn thiếu. Không tự cam kết đặt hàng. | Lưu đề xuất/nháp và nguồn; kiểm tra SKU, đơn vị, dữ liệu thiếu; chưa tăng tồn hoặc ghi chi. |
| 2 | Kiểm tra, sửa rồi xác nhận đề xuất; hoặc xác nhận đơn tự tạo, không duyệt thêm lần nữa. | Tóm tắt đơn và điểm chưa rõ; không xác nhận thay chủ hộ. | Tính theo giá đã xác nhận; lưu phiên bản và người xác nhận. Không chờ nhà cung cấp duyệt trên OPC. |
| 3 | Nếu hàng đã đến, chuyển sang UC-02. | Nhắc chưa được tăng tồn chỉ vì có đơn. | Liên kết đơn với hồ sơ thực nhận. |

**Post-conditions/trạng thái:** đề xuất/nháp → chủ hộ xác nhận đơn mua; tồn và thanh toán **chưa đổi**. Hai cách tạo và quyền chủ hộ xác nhận đã chốt; tên nhãn chi tiết là ĐỀ XUẤT. **Ngoại lệ:** thiếu SKU/NCC → làm rõ/UC-31, không đoán; chủ hộ không đồng ý đề xuất → chưa có đơn được xác nhận, chưa đặt hàng; hàng đến trước → tạo đơn rồi mới UC-02; gửi lại thao tác → không tạo đơn thứ hai. **Audit riêng:** nguồn nhu cầu, đề xuất/phiên bản, giá/lượng trước sau, quyết định chủ hộ. **OPEN:** Q-03; sửa/hủy theo UC-08 và quyết định Q-01. Nguồn/kênh phát hiện ý định mua cụ thể refine sau, không mặc định Agent giám sát mọi trao đổi.

### UC-02 — Xác nhận thực nhận và nhập kho

**Mục tiêu:** tăng tồn đúng hàng thực nhận. **Actor:** chủ hộ. **Trigger:** hàng đến, đã kiểm đếm. **Maturity/Pattern:** M1 / human xác nhận. **Map:** F03.03, F05.02, F05.08; flow §3.1 bước 2. **Scope:** luồng chính; nhiều lần nhận theo dõi nhưng không proposal.

**Pre-conditions:** phải có đơn mua liên kết trước khi tăng tồn; chủ hộ có quyền xác nhận; lượng/SKU/đơn vị rõ. **Dữ liệu:** đơn mua, số đặt, số đã nhận, số lần này, thời gian thực nhận, một kho, chênh lệch và bằng chứng.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Mở đơn, bấm “Nhận hàng”; kiểm đếm và kiểm tra/sửa lượng mặc định theo đơn thành số thực nhận. | Chỉ rõ phần khác số đặt, không tự xác nhận thực tế. | Đề xuất lượng theo đơn cho lần nhận đầu; kiểm tra phần đã nhận để tránh ghi lại. Chưa tăng tồn chỉ vì mở thao tác. |
| 2 | Bấm “Xác nhận nhập kho” sau khi kiểm tra số thực nhận. | Chuẩn bị tóm tắt nhập kho để kiểm tra. | Tăng tồn theo lượng được chủ hộ xác nhận đúng một lần; ghi biến động kho, không tự ghi đã thanh toán. |
| 3 | Xem phần còn thiếu nếu có. | Gợi ý việc cần làm, không tự kết thúc đơn. | Liên kết phiếu nhập với đơn và lịch sử nhận. |

**Post-conditions/trạng thái:** lần nhận chưa xác nhận → đã ghi kho; đơn chưa nhận → nhận thiếu hoặc nhận đủ theo lượng; tồn tăng đúng thực nhận. Không chứng minh đã có hóa đơn hoặc đã trả tiền. **Ngoại lệ:** nhận 18/20 → tăng 18, theo dõi 2 thiếu; chưa có đơn → UC-01, chặn tăng tồn; thừa/hỏng → UC-06; hai lần bấm/gửi lại → cùng lần nhận không tăng hai lần. **Audit riêng:** lượng thực nhận, người/thời điểm xác nhận, mã biến động kho. **OPEN:** Q-02 nếu hàng cần lô/hạn dùng, Q-03 cho quy cách.

### UC-03 — Gắn và kiểm tra chứng từ mua

**Mục tiêu:** truy được căn cứ của giao dịch mua/chi phí. **Actor:** chủ hộ; provider cung cấp dữ liệu nếu có. **Trigger:** nhận hóa đơn/chứng từ. **Maturity/Pattern:** M3 / đối soát có nguồn. **Map:** F03.06, F09.04–F09.05, F09.07; flow §3.1 bước 3. **Scope:** luồng chính, nguồn đồng bộ còn chờ xác minh.

**Pre-conditions:** có hồ sơ mua/chi phí hoặc chủ hộ xác định hồ sơ cần gắn. **Dữ liệu:** bản gốc, bên bán, số/ngày chứng từ, hàng, tiền, nguồn file/provider, giao dịch liên quan; bộ trường chi tiết chờ kế toán.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Chọn hồ sơ; nhận hóa đơn điện tử qua provider hoặc chụp chứng từ viết tay và nhập thông tin. | Giải thích thông tin cần nhập; OCR làm sau, không tự đọc ảnh trong giai đoạn đầu. | Giữ bản gốc, loại chứng từ, nguồn và dấu nhận diện trùng. |
| 2 | Kiểm tra thông tin từ provider/đã nhập và liên kết. | Chỉ chỗ lệch với đơn/nhận hàng dựa trên dữ liệu đã có. | So theo rule được xác nhận, không tự sửa cho khớp; không xác nhận giá trị pháp lý từ ảnh. |
| 3 | Xác nhận liên kết hoặc để chờ xử lý. | Tổng hợp nội dung cần hỏi bên bán/kế toán. | Cập nhật tình trạng chứng từ, không tăng kho lần nữa. |

**Post-conditions/trạng thái:** thiếu/chờ kiểm tra → đã liên kết hoặc cần xử lý; không mặc định “hợp lệ pháp lý” chỉ vì upload. **Ngoại lệ:** chưa có hóa đơn → giữ thiếu chứng từ, không xóa việc nhận hàng; dữ liệu trích sai → chủ hộ sửa bản trích, giữ bản gốc; file trùng → liên kết bản có sẵn; lệch/loại không rõ → Q-04/UC-24. **Audit riêng:** file gốc, kết quả trích, liên kết và người xác nhận. **OPEN:** Q-04, Q-13, Q-17.

### UC-04 — Ghi chi phí không qua kho

**Mục tiêu:** ghi chi phí vận hành và căn cứ mà không tạo hàng tồn. **Actor:** chủ hộ. **Trigger:** phát sinh chi phí. **Maturity/Pattern:** M3 / nhập tay có hỗ trợ. **Map:** F03.05–F03.06, F09.04, F09.07; flow §3.1 bước 3. **Scope:** luồng chính.

**Pre-conditions:** có quyền và quy tắc nhóm chi phí đã xác nhận. **Dữ liệu:** nội dung, bên nhận, ngày, số tiền, nhóm chi phí, chứng từ, tình trạng chi; chưa mặc định chi phí được dùng cho trường thuế nào.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Nhập nội dung/tiền hoặc thêm chứng từ; ảnh viết tay cần nhập thông tin thủ công. | Gợi ý nhóm từ dữ liệu đã nhập/dữ liệu provider; OCR ảnh làm sau. | Kiểm tra dữ liệu và trùng nguồn. |
| 2 | Xác nhận nhóm và thông tin. | Báo thiếu căn cứ hoặc không rõ phân loại. | Lưu hồ sơ không qua kho; không tạo phiếu nhập. |
| 3 | Ghi khoản chi ở UC-05 khi thực trả. | Dẫn tới chứng từ/tiền liên quan. | Tách chi phí khỏi bằng chứng đã trả. |

**Post-conditions/trạng thái:** nháp → chi phí đã xác nhận hoặc chờ căn cứ; kho không đổi; ghi sổ theo UC-23 khi đủ rule. **Ngoại lệ:** thiếu chứng từ/nhóm → chờ xác minh, không đoán; một khoản đã được ghi từ hóa đơn đồng bộ → dùng cùng hồ sơ. **Audit riêng:** phân loại, chứng từ, người xác nhận. **OPEN:** Q-04, Q-14.

### UC-05 — Ghi khoản chi và đối chiếu phải trả

**Mục tiêu:** biết thực chi bao nhiêu cho giao dịch mua/chi phí, không nhầm nhập kho với đã trả tiền. **Actor:** chủ hộ; provider hỗ trợ nguồn ngân hàng nếu có năng lực được xác minh. **Trigger:** chủ hộ đã trả tiền và ghi nhận trên OPC. **Maturity/Pattern:** M3 / human xác nhận + đối soát có nguồn; thao tác chính đã chốt, rule sổ/provider còn chờ. **Map:** F03.07, F08.02, F08.04–F08.05, F08.09, F10.04; flow §3.1 bước 4 và PO 07/10. **Scope:** trả đủ một lần bằng tiền mặt hoặc chuyển khoản, có thể trước hoặc sau nhận hàng. Không làm ứng trước một phần/trả nhiều lần; việc trả đủ trước nhận hàng không bị loại khỏi luồng chính. Không tự mở rộng mua chịu hoặc chính sách công nợ nhà cung cấp.

**Pre-conditions:** có giao dịch mua/chi phí và tiền thực chi có căn cứ; rule mốc phải trả cần Q-04. **Dữ liệu:** hồ sơ mua, bên nhận, số thực chi, phương thức, ngày, mã ngân hàng/phiếu chi, nguồn và chứng từ.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Mở đơn mua, bấm “Ghi nhận đã trả tiền”; chọn tiền mặt/chuyển khoản, nhập số tiền và ngày trả. | Gợi ý giao dịch ngân hàng liên quan nếu đã có dữ liệu; giải thích khác biệt. | Cho ghi trước hoặc sau nhận hàng; lưu số thực chi, phương thức, ngày và nguồn; kiểm tra trùng. |
| 2 | Kiểm tra rồi xác nhận khoản chi gắn với đơn/hóa đơn. | Trình bày căn cứ đối chiếu, không xác nhận thay chủ hộ. | Liên kết cùng hồ sơ mua và chứng từ; không tạo lệnh chuyển tiền, không thay đổi tồn kho. |
| 3 | Xem khoản tiền đã ghi và kết quả đối chiếu. | Nêu thiếu/lệch để chủ hộ xử lý. | Hiển thị khoản chi đã xác nhận; cập nhật phải trả theo rule kế toán khi có đủ căn cứ. Không tự coi đơn đã nhận đủ hàng hoặc hoàn tất mọi việc vì đã trả tiền. |

**Post-conditions/trạng thái:** chưa ghi khoản chi → chủ hộ đã xác nhận khoản chi liên kết với hồ sơ; chưa đối chiếu → đã liên kết/cần xử lý. Phải trả giảm/đóng theo rule kế toán, không tự đóng đơn mua. **Ngoại lệ:** provider không cấp chiều chi → chủ hộ nhập chuyển khoản thủ công, không giả đã đối chiếu ngân hàng; tiền thiếu/dư/không rõ hồ sơ → ngoại lệ, không mở rộng trả nhiều lần; nhập tay rồi đồng bộ → nhận diện cùng khoản, không ghi chi hai lần. **Audit riêng:** số/ngày/phương thức trả, mã giao dịch nếu có, nguồn, liên kết đơn/hóa đơn và người xác nhận. **OPEN:** Q-04, Q-12–Q-14 cho bộ trường/căn cứ/rule sổ và chống trùng; không hỏi lại quyền chủ hộ ghi khoản chi.

### UC-06 — Xử lý thiếu, thừa, hỏng hoặc trả hàng mua

**Mục tiêu:** giải thích chênh lệch mua và xử lý có chứng cứ. **Actor:** chủ hộ. **Trigger:** nhận khác đơn hoặc cần trả nhà cung cấp. **Maturity/Pattern:** M2 / human xác nhận. **Map:** F03.04, F05.02, F09.05; flow §3.2, capability 6.3. **Scope:** MVP Basic; nhận nhiều lần là nhánh hiếm không proposal.

**Pre-conditions:** có đơn và tình trạng thực nhận/kho. **Dữ liệu:** lượng đặt/nhận, loại lệch, hàng hỏng, đã ghi kho hay chưa, thỏa thuận nhà cung cấp, ảnh/chứng từ và lý do.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Ghi loại và lượng chênh lệch. | So sánh và tổng hợp căn cứ. | Không tăng tồn theo số đặt; tách phần đã xác nhận và còn tranh chấp. |
| 2 | Làm rõ với nhà cung cấp, chọn phương án. | Gợi ý giao tiếp, đổi lượng hoặc trả; không tự quyết. | Kiểm tra trạng thái kho/chứng từ liên quan. |
| 3 | Xác nhận hành động khi quy tắc tương ứng đã chốt. | Chuẩn bị hồ sơ xử lý. | Ghi biến động hợp lệ, không xóa phiếu nhập cũ. |

**Post-conditions/trạng thái:** chênh lệch mới → chờ quyết định hoặc đã xử lý; kho chỉ đổi theo hành động thực tế được xác nhận. **Ngoại lệ:** nhận thêm lần sau → UC-02 cho phần mới; hàng đã giữ cho đơn bán → không tự giảm khả dụng âm; trả/hoàn tiền chưa có rule → chờ Q-05, không giả hoàn tất. **Audit riêng:** tình trạng hàng, thỏa thuận, hành động bù và nguồn. **OPEN:** Q-02, Q-05.

### UC-07 — Xem tồn, kiểm kê và điều chỉnh kho

**Mục tiêu:** biết hàng còn bao nhiêu và giải thích chênh lệch thực tế. **Actor:** chủ hộ. **Trigger:** kiểm tra hoặc kiểm kê. **Maturity/Pattern:** M2 / human xác nhận. **Map:** F05.02–F05.03, F05.07–F05.08; capability 6.5. **Scope:** xem tồn luồng chính; kiểm kê/điều chỉnh MVP Basic.

**Pre-conditions:** một kho đã thiết lập, tồn đầu kỳ hợp lệ UC-31; điều chỉnh phải có quyền/phê duyệt. **Dữ liệu:** SKU/đơn vị, tồn thực tế đã ghi, giữ theo đơn, khả dụng, số kiểm đếm, thời điểm và lý do.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Xem tồn và lịch sử từng hàng. | Giải thích hàng đang giữ cho đơn nào. | Tính tồn/giữ/khả dụng theo rule, không lấy ước lượng AI. |
| 2 | Nhập số kiểm đếm nếu cần điều chỉnh. | Chỉ ra khác biệt và nguồn biến động. | Tạo đề nghị điều chỉnh, chưa tự ghi giảm/tăng. |
| 3 | Người có quyền duyệt theo chính sách đã chốt. | Tóm tắt ảnh hưởng các đơn liên quan. | Ghi biến động và lịch sử; xử lý xung đột trước cập nhật. |

**Post-conditions/trạng thái:** xem → kho không đổi; đề nghị → chờ duyệt → được duyệt/đã ghi hoặc bị từ chối. **Ngoại lệ:** hàng đang giữ, giao dịch kho phát sinh sau kiểm đếm → kiểm tra lại; thiếu lý do/quyền → không điều chỉnh; lặp thao tác → không tăng/giảm hai lần. **Audit riêng:** số đếm, số hệ thống, người đếm/duyệt, tác động đơn giữ. **OPEN:** Q-05, Q-18.

### UC-08 — Thay đổi hoặc hủy đơn mua

**Mục tiêu:** cập nhật nhu cầu mua mà không làm mất giao dịch đã xảy ra. **Actor:** chủ hộ. **Trigger:** thay đổi/hủy mua. **Maturity/Pattern:** M2 / human xác nhận; luồng đơn giản đã chốt, nhánh sau phát sinh cần refinement. **Map:** F03.02, F03.04, F14.04; capability 6.3, PO 07/10. **Scope:** sửa/hủy trực tiếp khi chưa nhận hàng và chưa trả tiền. Xử lý sau phát sinh hàng/tiền để refinement sau, không đưa vào happy path.

**Pre-conditions:** có đơn, biết hàng đã nhận/tiền đã chi/chứng từ đã gắn. **Dữ liệu:** phiên bản đơn, nội dung đổi, lý do, thỏa thuận bên bán và giao dịch liên quan.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Mở đơn và chọn sửa hoặc hủy. | Tổng hợp nhận hàng, kho, chứng từ, tiền. | Kiểm tra trạng thái và phiên bản hiện tại. |
| 2 | Nếu chưa nhận hàng và chưa trả tiền, kiểm tra thay đổi rồi xác nhận sửa/hủy. | Tóm tắt nội dung và ảnh hưởng, không quyết định thay chủ hộ. | Kiểm tra lại cả hai điều kiện trước ghi; lưu phiên bản/lịch sử, không xóa đơn. |
| 3 | Nếu đã phát sinh hàng hoặc tiền, xem hồ sơ liên quan để xử lý riêng. | Dẫn tới nhận hàng UC-02/06 và khoản chi UC-05, không tự hoàn tiền/trả hàng. | Không dùng thao tác hủy để xóa giao dịch cũ hoặc tự đảo tồn/tiền; quy trình nhánh này refine sau. |

**Post-conditions/trạng thái:** chưa nhận hàng và chưa trả tiền → đơn được sửa/hủy có lịch sử; tồn/tiền không đổi. Đã phát sinh hàng/tiền → giữ hồ sơ để xử lý riêng, không xóa giao dịch. **Ngoại lệ:** đã có hóa đơn → giữ chứng từ, không coi hủy đơn là hủy hóa đơn; cách xử lý chứng từ chờ kế toán/provider Q-10/Q-13. Nhận hàng hoặc ghi tiền đồng thời lúc sửa/hủy → kiểm tra lại trước ghi. **Audit riêng:** phiên bản trước/sau, người/thời điểm, lý do nếu cung cấp, kết quả kiểm tra và hồ sơ xử lý tiếp. **OPEN:** Q-05 cho hàng/tiền phát sinh; chi tiết nhánh sau phát sinh và chứng từ, không hỏi lại điều kiện sửa/hủy đơn đơn giản.

## 4. Bán hàng, hóa đơn và tiền — Order-to-Cash

### UC-09 — Tiếp nhận yêu cầu bán

**Mục tiêu:** giữ yêu cầu gốc và có nội dung để kiểm tra, chưa tự chốt bán. **Actor:** chủ hộ khi nhập tay; connector Zalo kích hoạt khi nhận tin. **Trigger:** khách lẻ hoặc doanh nghiệp yêu cầu mua. **Maturity/Pattern:** M3 / nhập tay hoặc sự kiện. **Map:** F06.01–F06.02, F13.04; flow §4.1 bước 1. **Scope:** luồng chính.

**Pre-conditions:** đúng hộ/quyền; Zalo chỉ dùng khi kết nối được xác minh, vẫn có nhập tay. **Dữ liệu:** tin gốc/mã sự kiện, người gửi, thời gian, nội dung, hàng/lượng/đơn vị/ngày giao và thông tin khách có sẵn.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Nhập yêu cầu hoặc xem tin đã nhận. | Đọc nội dung không cấu trúc. | Lưu nguồn; sự kiện trùng không sinh yêu cầu mới. |
| 2 | Kiểm tra khách/hàng/lượng Agent nhận diện. | Gợi ý từ danh mục và đánh dấu mơ hồ. | Đối chiếu mã chuẩn; không tự đoán SKU/giá. |
| 3 | Đi UC-10 nếu thiếu, UC-11 nếu đã rõ. | Nêu dữ liệu còn cần. | Chưa xác nhận đơn, chưa giữ/trừ kho. |

**Post-conditions/trạng thái:** mới nhận → cần làm rõ hoặc đủ để kiểm tra; không đồng nghĩa đã có đơn duyệt. **Ngoại lệ:** webhook lặp; file khó đọc; một tin nhắc lại đơn cũ → tìm hồ sơ liên quan, không tạo đơn mới mặc định; hết quyền Zalo → báo lỗi, không giả nhận tin. **Audit riêng:** tin gốc, kết quả nhận diện, sửa của người dùng. **OPEN:** Q-06, Q-13.

### UC-10 — Làm rõ khách hàng và hàng cần mua

**Mục tiêu:** biết đúng khách/SKU/lượng và thông tin cần thiết để xử lý. **Actor:** chủ hộ; khách trả lời ngoài OPC. **Trigger:** thiếu hoặc nhiều kết quả nhận diện. **Maturity/Pattern:** M2 / nhập tay có hỗ trợ. **Map:** F06.03, F02.01, F02.03; flow §4.1 bước 1. **Scope:** luồng hỗ trợ.

**Pre-conditions:** có yêu cầu gốc; biết điểm chưa rõ. **Dữ liệu:** lựa chọn khách/SKU, quy cách, lượng, địa chỉ/thời điểm giao, thông tin hóa đơn cần xác nhận, câu hỏi và trả lời.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Xem danh sách thiếu hoặc mơ hồ. | Soạn câu hỏi cụ thể. | Giữ các lựa chọn, chưa biến gợi ý thành dữ liệu chuẩn. |
| 2 | Tự hỏi khách hoặc xác nhận bằng hiểu biết có căn cứ. | Soạn gợi ý để chủ hộ tham khảo và hỗ trợ đọc câu trả lời. | Agent không tự gửi tin; lưu trả lời do chủ hộ cung cấp hoặc nguồn Zalo được xác minh. |
| 3 | Chọn đúng dữ liệu hoặc thêm danh mục UC-31. | Tóm tắt yêu cầu đã làm rõ. | Lưu nguồn xác nhận; kiểm tra lại dữ liệu cần thiết. |

**Post-conditions/trạng thái:** cần làm rõ → đủ để kiểm tra; còn thiếu thì giữ chờ, không tự tạo đơn hoàn chỉnh. **Ngoại lệ:** khách không trả lời → chờ/timeout Q-18; SKU không có → chủ hộ tạo hoặc chọn sản phẩm, không bịa; trùng khách → Q-03; không rõ thông tin hóa đơn → Q-10. **Audit riêng:** câu hỏi, trả lời, lựa chọn và người xác nhận. **OPEN:** Q-03, Q-06 về dữ liệu kênh, Q-10.

### UC-11 — Kiểm tra giá, tồn và thông tin đơn chưa đóng

**Mục tiêu:** chủ hộ biết còn bao nhiêu hàng, giá đang thiết lập và đơn khách còn chưa đóng. **Actor:** chủ hộ. **Trigger:** yêu cầu mua đã rõ hoặc chủ hộ hỏi tồn. **Maturity/Pattern:** M1 / nhập tay có hỗ trợ. **Map:** F02.05, F05.03, F06.04–F06.06, F06.08; F02.06 ngoài phạm vi, không dùng chặn nợ. **Nguồn:** flow §4.1 bước 2 và PO 07/10. **Scope:** luồng chính; không giảm giá, không giao thiếu, không hạn mức/nợ quá hạn.

**Pre-conditions:** SKU/đơn vị rõ, giá do chủ hộ thiết lập, tồn có nguồn. **Dữ liệu:** yêu cầu, lượng khách hỏi, giá/phiên bản, tồn thực tế, đang giữ, khả dụng và các đơn chưa đóng/tiền thực nhận đã liên kết.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Xem tồn khi tạo đơn hoặc hỏi Agent. | Trả lời từ dữ liệu kho, chỉ rõ lượng còn bán được. | Tính tồn khả dụng bằng logic xác định, hiển thị nguồn/thời điểm. |
| 2 | Tự trao đổi với khách, chọn lượng/giá trên đơn. | Báo lượng yêu cầu vượt tồn, nêu các đơn chưa đóng nếu cần. | Không tự gửi tin, giảm giá hoặc chặn do nợ quá hạn. |
| 3 | Nếu còn 6 mà khách muốn 10, sửa đơn tối đa 6 hoặc nhập thêm trước khi xác nhận 10. | Nhắc kiểm tra tồn mới, không tự chọn phương án. | Không xác nhận đơn vượt tồn; chưa giữ hàng ở bước xem/báo giá. |

**Post-conditions/trạng thái:** yêu cầu được kiểm tra → đủ điều kiện lập/xác nhận đơn hoặc chưa đủ tồn; không có trạng thái đơn xác nhận chờ hàng. Chủ hộ quyết định trao đổi và bổ sung kho qua luồng mua. **Ngoại lệ:** chưa có giá → chủ hộ thiết lập, AI không đoán; dữ liệu kho chưa cập nhật → xác nhận nguồn/nhập kho trước, không bỏ kiểm tra; tin Zalo hỏi 10 không bắt buộc đơn cuối là 10. **Audit riêng:** snapshot giá/tồn, lượng khách hỏi và lượng đơn chủ hộ chọn. **OPEN:** không còn quyết định giảm giá/chặn nợ cần hỏi; Q-18 cho offline và quyền chi tiết.

### UC-12 — Tạo và xác nhận đơn bán

**Mục tiêu:** có đơn do chủ hộ xác nhận, làm căn cứ giữ/giao hàng. **Actor:** chủ hộ. **Trigger:** lập đơn theo tin Zalo hoặc tự nhập. **Maturity/Pattern:** M1 / Agent đề xuất → chủ hộ duyệt, hoặc chủ hộ nhập tay → xác nhận. **Map:** F06.07, F14.02–F14.03, F12.04; flow §4.1 bước 3, PO 07/10. **Scope:** luồng chính.

**Pre-conditions:** khách/SKU/đơn vị/giá rõ; lượng đơn không vượt tồn khả dụng tại xác nhận; chủ hộ có quyền. **Dữ liệu:** nguồn yêu cầu, phiên bản đơn, dòng hàng/lượng/giá, nguồn tạo tay/Agent và xác nhận của chủ hộ.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Chọn một cách: xem đề xuất từ Zalo hoặc bấm “Tạo đơn” rồi nhập. | Đọc tin và chuẩn bị đề xuất nếu dùng Agent. | Đề xuất Agent chờ chủ hộ duyệt, chưa giữ/trừ kho. |
| 2 | Kiểm tra/sửa và duyệt đề xuất; hoặc xác nhận đơn tự nhập. | Báo tồn và dữ liệu thiếu, không duyệt thay. | Cùng kiểm tra giá/dữ liệu/tồn; đơn tay không có thêm vòng duyệt riêng. |
| 3 | Xem đơn xác nhận và hàng được giữ đủ UC-13. | Hiển thị việc tiếp theo. | Kiểm tra và giữ đủ tại xác nhận; không để hai đơn cùng chiếm hàng. |

**Post-conditions/trạng thái:** đề xuất Agent chờ duyệt → xác nhận; đơn tay đang nhập → xác nhận trực tiếp khi hợp lệ. Tồn thực tế chưa giảm. **Ngoại lệ:** chủ hộ từ chối → không tạo đơn xác nhận/giữ hàng, lưu nguồn/lý do; lượng vượt tồn hoặc tồn đổi khi bấm xác nhận → không hoàn tất xác nhận, chủ hộ sửa lượng hoặc nhập thêm trước; hai thao tác cùng hồ sơ → không tạo hai đơn. **Audit riêng:** phiên bản, nguồn tay/Agent, người duyệt/xác nhận và kết quả kiểm tra tồn. **OPEN:** Q-18 cho quyền/đồng bộ offline; không hỏi lại cách xác nhận đơn tay.

### UC-13 — Giữ hoặc giải phóng hàng cho đơn

**Mục tiêu:** dành đủ hàng đúng một lần cho đơn hợp lệ; ngăn các đơn cùng dùng một lượng tồn. **Actor:** chủ hộ xác nhận đơn; OPC ghi giữ theo logic xác định. **Trigger:** UC-12 xác nhận hoặc UC-21 hủy/sửa hợp lệ. **Maturity/Pattern:** M2 / logic xác định. **Map:** F05.03–F05.04, F06.08; flow §4.1 bước 4, PO 07/10. **Scope:** một kho, giữ đủ; không giữ một phần/đợi nhập.

**Pre-conditions:** lượng đơn đủ tồn khả dụng tại thời điểm xác nhận. **Dữ liệu:** đơn/phiên bản, SKU/đơn vị, tồn và lượng đang giữ; lý do giải phóng.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Xác nhận đơn theo UC-12. | Báo tồn và thiếu nếu có. | Kiểm tra tồn mới và giữ đủ cùng bước xác nhận; không dùng snapshot cũ. |
| 2 | Nếu không đủ, sửa lượng hoặc cập nhật nhập kho trước khi xác nhận lại. | Giải thích lượng còn bán được. | Không giữ phần có sẵn cho đơn vượt tồn, không tạo đơn xác nhận chờ hàng. |
| 3 | Nếu hủy trước giao, xác nhận hủy UC-21. | Nhắc hàng đang dành cho đơn. | Giải phóng giữ một lần; không tăng tồn thực tế vì giữ chưa xuất kho. |

**Post-conditions/trạng thái:** đủ hàng → đơn xác nhận và giữ đủ; không đủ → xác nhận chưa hoàn tất, không giữ một phần; hủy trước giao → đã giải phóng. Giữ chỉ giảm khả dụng, không trừ tồn thực tế. **Ngoại lệ:** hai đơn tranh hàng → chỉ đơn đủ tồn tại thao tác được xác nhận; gửi lại → không giữ hai lần; sửa đơn → kiểm tra lại lượng và hàng giữ theo phiên bản, không giữ trùng. **Audit riêng:** lượng/đơn giữ, kiểm tra tồn, thời điểm và lý do giải phóng. **OPEN:** Q-08 chỉ còn policy hết hạn/sửa sau xác nhận để refinement; không tự áp thời hạn mới.

### UC-14 — Chuẩn bị hàng để giao

**Mục tiêu:** chủ hộ lấy và chuẩn bị đủ hàng theo đơn. **Actor:** chủ hộ. **Trigger:** có đơn xác nhận/giữ đủ, giao hàng chưa hoàn thành. **Maturity/Pattern:** M1 / human thực hiện. **Map:** F07.01–F07.02, F05.03; flow §4.1 bước 5, PO 07/10. **Scope:** luồng chính, không bắt nhập lại số lượng hoặc xác nhận chuẩn bị riêng như một cửa duyệt mới.

**Pre-conditions:** đơn được xác nhận, lượng/đơn vị trên đơn rõ. Đơn đã đóng do nhận tiền vẫn được chuẩn bị/giao nếu chưa giao. **Dữ liệu:** mã đơn, danh sách hàng và số lượng lấy sẵn từ phiên bản đã xác nhận; trạng thái giao và giữ.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Mở đơn và xem danh sách cần lấy. | Hiển thị/tóm tắt hàng theo đơn. | Lấy lượng từ đơn bán đã xác nhận, không lấy lại từ tin Zalo chưa sửa. |
| 2 | Lấy hàng, kiểm đếm, đóng gói khi cần. | Nhắc thông tin đơn. | Chưa trừ tồn thực tế vì mới chuẩn bị. |
| 3 | Khi giao đủ, dùng “Đã giao” UC-15. | Hiển thị thao tác tiếp theo. | Không yêu cầu nhập lại lượng; không thêm trạng thái chuẩn bị thiếu/giao từng phần. |

**Post-conditions/trạng thái:** hàng đã chuẩn bị thực tế, giao vẫn chưa hoàn thành cho tới UC-15; chuẩn bị không tự giảm tồn/đóng đơn. **Ngoại lệ:** thực tế không đủ/hỏng → chủ hộ xử lý nguồn hàng hoặc sửa/hủy đơn đúng quyền trước giao; không dùng giao thiếu. Đơn đổi/hủy trong lúc chuẩn bị → kiểm tra phiên bản. **Audit riêng:** chỉ ghi thao tác có trên OPC; không giả ghi nhận kiểm đếm vật lý chưa được người dùng xác nhận. **OPEN:** Q-02 cho lô/hạn dùng nếu pilot cần; Q-18 cho quyền chi tiết.

### UC-15 — Bấm “Đã giao” và cập nhật kho

**Mục tiêu:** ghi nhận giao tay đủ hàng theo đơn và biết đơn đang tới bước nào. **Actor:** chủ hộ. **Trigger:** đã giao đủ cho khách. **Maturity/Pattern:** M1 / human xác nhận. **Map:** F07.04–F07.05, F05.05; F07.06/F05.06 chỉ nhánh trả hàng chưa đặc tả; flow §4.1 bước 5, PO 07/10. **Scope:** giao tay đủ một lần, không giao thiếu/giao tiếp hoặc carrier integration.

**Pre-conditions:** đơn bán đã xác nhận và có hàng giữ đủ; chưa ghi “Đã giao” cho đơn. Đóng đơn do nhận tiền không chặn thao tác này nếu giao còn chờ. **Dữ liệu:** đơn/phiên bản, SKU/đơn vị/lượng lấy sẵn, người thao tác và thời gian.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Mở đơn, xem hàng/lượng và bấm “Đã giao” sau giao đủ. | Tóm tắt đơn; không tự xác nhận giao. | Lấy lượng từ đơn bán đã xác nhận; không yêu cầu nhập lại. |
| 2 | Xem trạng thái đã giao. | Nêu kết quả cập nhật. | Trừ kho đúng toàn bộ lượng đơn, dùng hết giữ tương ứng, một lần duy nhất. |
| 3 | Theo dõi hóa đơn UC-16 và tiền nếu chưa nhận. | Nêu việc còn chờ. | Kích hoạt bước hóa đơn; không tự giả hóa đơn thành công hoặc đã thu tiền. |

**Post-conditions/trạng thái:** giao chưa hoàn thành → đã giao đủ; tồn thực tế giảm theo lượng đơn, giữ được tiêu thụ; bước hóa đơn được kích hoạt. **Ngoại lệ:** chưa giao đủ → không bấm “Đã giao”; chủ hộ tự xử lý rồi giao đủ, không có luồng nhập giao thiếu. Bấm/gửi lại → không xuất kho/hóa đơn hai lần. Hủy hoặc thay đổi đồng thời → kiểm tra phiên bản. Hàng trả về sau giao là nhánh riêng, không tự tăng kho. **Audit riêng:** chủ hộ/thời gian bấm, lượng và phiên bản đơn, biến động kho, sự kiện kích hoạt hóa đơn. **OPEN:** không còn hỏi lại giao thiếu hoặc nhập số thực giao; Q-05 cho trả hàng, Q-10/Q-13 cho hóa đơn/provider.

### UC-16 — Phát hành, theo dõi và gửi hóa đơn bán

**Mục tiêu:** có hóa đơn và biết kết quả thực tế của provider. **Actor:** chủ hộ; provider trả kết quả. **Trigger:** chủ hộ bấm “Đã giao” theo UC-15; kế toán/provider xác minh cách phát hành thật. **Maturity/Pattern:** M3 / sự kiện tích hợp. **Map:** F09.01–F09.03, F09.07, F13.04–F13.05; flow §4.1 bước 6. **Scope:** luồng chính; sửa/hủy thuộc nhánh đang phát triển.

**Pre-conditions:** đơn được duyệt, dữ liệu hóa đơn đủ, provider/quyền đã xác minh; kế toán xác nhận cách áp dụng. **Dữ liệu:** đơn/phiên bản, thông tin bên bán/mua, dòng hàng theo toàn bộ đơn, giá/thuế theo cấu hình có căn cứ, yêu cầu phát hành, mã/trạng thái/kết quả provider.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Kiểm tra dữ liệu hóa đơn khi giao. | Báo mismatch/thiếu dữ liệu. | Theo PO: một hóa đơn toàn bộ lượng đơn; không tự đoán thông tin/thuế. |
| 2 | Thực hiện phát hành theo quyền/chính sách xác nhận. | Chuẩn bị yêu cầu, giải thích trước thực hiện. | Gửi provider, nhận ID; không coi gửi thành công là phát hành xong. |
| 3 | Xem kết quả, xử lý lỗi; gửi khách theo kênh được chốt. | Tóm tắt lý do lỗi và hướng xử lý. | Cập nhật từ kết quả xác minh; giữ file/ID/bằng chứng gửi. |

**Post-conditions/trạng thái:** chưa phát hành → đang chờ → đã phát hành hoặc pending/cần xử lý nếu bị từ chối. Nhãn lỗi là đề xuất, UI pending theo PO; không coi pending là thành công. **Ngoại lệ:** thiếu dữ liệu/thuế hoặc chưa xác minh cách phát hành → chưa tự phát hành thật; retry/mất phản hồi → tra cứu kết quả cũ trước gửi mới; bấm “Đã giao” lại không tạo hóa đơn thứ hai; đã phát hành cần sửa → không sửa bản cũ, Q-10. Giao thiếu đã bỏ khỏi scope, không dùng ví dụ giao 6/hóa đơn 10. Đơn đã đóng do có tiền không ngăn xử lý hóa đơn còn chờ. **Audit riêng:** dữ liệu gửi, người/lệnh xác nhận, ID/kết quả provider, file và bằng chứng gửi khách. **OPEN:** Q-10, Q-13.

### UC-17 — Tạo yêu cầu thanh toán hoặc QR

**Mục tiêu:** khách biết cần trả bao nhiêu, vào đâu và cho đơn nào. **Actor:** chủ hộ. **Trigger:** cần yêu cầu khách thanh toán. **Maturity/Pattern:** M3 / tích hợp có kiểm tra. **Map:** F08.03, F08.01; flow §4.1 bước 7. **Scope:** luồng chính; tiền có thể trước hoặc sau giao, rule ghi sổ chờ kế toán.

**Pre-conditions:** có đơn/số cần thu được xác định và tài khoản nhận hợp lệ; năng lực QR provider xác minh. **Dữ liệu:** hồ sơ, số yêu cầu, tài khoản, nội dung chuyển/mã đơn, thời điểm và phiên bản QR.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Chọn đơn và kiểm tra số cần thu. | Giải thích số và nguồn. | Tính theo rule, không lấy số Agent đoán. |
| 2 | Tạo/kiểm tra thông tin hoặc QR. | Soạn nội dung yêu cầu. | Gắn đúng hộ, tài khoản, đơn và số tiền. |
| 3 | Gửi cho khách theo quyền/kênh đã chốt. | Hỗ trợ diễn đạt. | Lưu bản đã gửi, không ghi đã nhận tiền. |

**Post-conditions/trạng thái:** chưa có yêu cầu → đã tạo/đã gửi; payment vẫn chưa xác nhận. **Ngoại lệ:** thay giá/lượng → QR cũ cần kiểm tra lại, không tự phân bổ tiền theo bản mới; QR lỗi/không hỗ trợ → báo không khả dụng, fallback chưa cam kết; khách chuyển khác tiền → UC-20. **Audit riêng:** bản QR/nội dung, số yêu cầu, tài khoản nhận, gửi. **OPEN:** Q-11–Q-13.

### UC-18 — Nhận tiền ngân hàng và khớp theo rule

**Mục tiêu:** ghi giao dịch thật và chỉ giảm nợ khi xác định đúng hồ sơ. **Actor:** provider kích hoạt; chủ hộ giám sát. **Trigger:** webhook/nguồn đồng bộ đã xác minh có tiền vào. **Maturity/Pattern:** M3 / sự kiện tích hợp. **Map:** F08.04–F08.06, F13.03–F13.05, F08.01; flow §4.1 bước 7. **Scope:** tích hợp thật là mục tiêu, chưa chứng minh provider đáp ứng.

**Pre-conditions:** connector còn quyền; sự kiện xác thực và đúng hộ/tài khoản; bộ rule khớp đã được duyệt. **Dữ liệu:** ID nguồn/transaction, tài khoản, chiều tiền, số thực nhận, thời gian, nội dung chuyển, hồ sơ ứng viên và phân bổ đã có.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Xem giao dịch thật đã nhận. | Giải thích nguồn/nội dung. | Xác thực, lưu nguyên số tiền, chống trùng ID/sự kiện. |
| 2 | Xem kết quả khớp hoặc việc cần xử lý. | Gợi ý ứng viên khi mơ hồ, không tự xác nhận. | Chỉ tự phân bổ khi đủ rule; mã đơn đơn lẻ chưa được coi là đủ. |
| 3 | Nếu không đủ căn cứ, xử lý UC-20. | Nêu lý do không khớp. | Chỉ giảm phải thu từ phân bổ hợp lệ; không tự tăng doanh thu theo tiền dư. |

**Post-conditions/trạng thái:** chưa nhận → giao dịch đã ghi; chưa phân bổ → đã khớp theo rule hoặc chờ xác nhận; khi xác định tiền thuộc đơn thì đề xuất đóng UC-22, không tự đóng. **Ngoại lệ:** webhook lặp → không nhận/giảm nợ hai lần; không mã đơn/nhiều ứng viên/thiếu/dư → UC-20; tiền đã nhập tay → đối chiếu cùng giao dịch, không tạo thu lần hai; bank chậm → không tự ghi đã trả. **Audit riêng:** sự kiện/transaction nguồn, kiểm tra xác thực, rule/phiên bản, hồ sơ khớp và số phân bổ. **OPEN:** Q-11–Q-13.

### UC-19 — Ghi nhận thu tiền mặt

**Mục tiêu:** lưu tiền mặt thực nhận và liên kết đúng đơn. **Actor:** chủ hộ. **Trigger:** khách đã đưa tiền mặt. **Maturity/Pattern:** M2 / human xác nhận. **Map:** F08.09, F08.01, F08.07; flow §4.1 bước 7. **Scope:** luồng chính.

**Pre-conditions:** có quyền và căn cứ thực nhận; chọn được đơn hoặc đánh dấu chưa rõ hồ sơ. **Dữ liệu:** số thực nhận, ngày, người trả/nhận, đơn, phương thức, chứng từ/ghi chú và phân bổ.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Chọn đơn, nhập số đã thực nhận. | Hiển thị số theo đơn để đối chiếu. | Chọn sẵn tiền mặt không tự ghi nhận thu. |
| 2 | Xác nhận tiền thực nhận và liên kết. | Nêu chênh lệch nếu có. | Ghi tiền mặt, nguồn nhập tay và kiểm tra trùng. |
| 3 | Nếu lệch, thêm giải trình tại UC-20. | Gợi ý nội dung note dựa trên số có thật. | Giảm công nợ theo phân bổ hợp lệ, không tự coi đủ khi thiếu. |

**Post-conditions/trạng thái:** chưa ghi → tiền mặt đã xác nhận; khoản phải thu cập nhật theo rule, phần dư tách riêng; chuyển đề xuất đóng UC-22, không tự đóng. **Ngoại lệ:** chọn nhầm đơn/số → sửa có lịch sử theo quyền chưa chốt; khách nói đã trả nhưng hộ chưa nhận → không dùng UC này để giả thu; bấm lại → không tạo thu mới. **Audit riêng:** người nhận/xác nhận, số thực tế, chứng từ và phương thức. **OPEN:** Q-11–Q-12.

### UC-20 — Phân bổ tiền và ghi chú chênh lệch

**Mục tiêu:** xác định tiền thuộc hồ sơ nào và giải thích thiếu/dư. **Actor:** chủ hộ. **Trigger:** tiền chưa khớp hoặc chênh lệch. **Maturity/Pattern:** M2 / đối soát có nguồn. **Map:** F08.07, F10.04, F14.04; flow §4.1 bước 8. **Scope:** luồng chính; không thêm hành trình thanh toán nhiều lần/hoàn tự động.

**Pre-conditions:** giao dịch tiền đã có, không tạo lại tiền; có quyền xác nhận liên kết. **Dữ liệu:** transaction/phiếu thu, số thực nhận, đơn/hóa đơn ứng viên, số phải thu, phân bổ hiện có, phần dư/thiếu, căn cứ chọn và note.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Xem giao dịch và tìm đơn đúng. | Gợi ý ứng viên có căn cứ, nêu mức mơ hồ. | Hiển thị nguồn, số và phân bổ đã có; không cho phân bổ cùng tiền hai lần. |
| 2 | Xác nhận liên kết và ghi note giải trình. | Soạn note để chủ hộ sửa/xác nhận. | Giữ số giao dịch gốc; tách số đối chiếu với hồ sơ và chênh lệch. |
| 3 | Tự xử lý phần dư; phần thiếu giữ cần xử lý. | Nhắc việc còn lại, không chuyển tiền. | Không đổi hóa đơn, không tự hoàn/chuyển dư sang đơn khác hoặc ghi dư là doanh thu. |

**Post-conditions/trạng thái:** chưa khớp → đã xác nhận liên kết hoặc vẫn chờ; chênh lệch có note không tự có nghĩa đã giải quyết. Hóa đơn 8.000đ, nhận 10.000đ: lưu transaction 10.000đ, căn cứ hóa đơn 8.000đ, dư 2.000đ và note; đóng đơn theo UC-22 khi có tiền thực nhận cho đơn và chủ hộ xác nhận, không chờ chủ hộ xử lý xong khoản dư; tất toán sổ/công nợ là việc riêng, không xóa số thực nhận/chênh lệch. **Ngoại lệ:** không tìm được hồ sơ → giữ chưa phân bổ; thiếu tiền → không giả thu đủ; note thiếu căn cứ → yêu cầu bổ sung; sửa phân bổ cũ → phải có lịch sử/quyền. **Audit riêng:** liên kết, số trước/sau, note, actor, lý do; không xóa nguồn tiền. **OPEN:** Q-11–Q-12.

### UC-21 — Thay đổi hoặc hủy đơn bán

**Mục tiêu:** chủ hộ xử lý yêu cầu đổi/hủy từ khách mà không làm sai tiền/kho/hóa đơn. **Actor:** chủ hộ; khách báo ngoài OPC. **Trigger:** khách hoặc chủ hộ yêu cầu đổi/hủy. **Maturity/Pattern:** M2 / human xác nhận. **Map:** F06.07, F05.04, F07.06; F09.06/F08.08 chỉ nhánh làm sau; flow §4.4. **Scope:** trước bàn giao luồng hỗ trợ; sau hóa đơn “đang phát triển”.

**Pre-conditions:** có đơn, phiên bản hiện tại và trạng thái thực giao/hóa đơn/tiền. **Dữ liệu:** yêu cầu khách, lý do, lượng đổi/hủy, đồng ý, hàng giữ/đã xuất, tiền nhận, hóa đơn và biên bản nếu áp dụng.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Ghi yêu cầu đổi/hủy và kiểm tra đơn. | Tổng hợp ảnh hưởng hàng, hóa đơn và tiền. | Phân nhánh trước/sau bàn giao, trước/sau hóa đơn; chưa cần tài khoản khách. |
| 2 | Xác nhận phương án theo thỏa thuận/quyền. | Chuẩn bị thông tin để quyết định. | Kiểm tra lại giá/nợ/tồn nếu sửa; không áp dụng duyệt cũ cho nội dung khác. |
| 3 | Trước bàn giao: thực hiện hủy/đổi hợp lệ; sau hóa đơn: xử lý hồ sơ riêng. | Nêu việc còn chờ kế toán/provider. | Hủy hợp lệ giải phóng phần giữ chưa xuất; không tự tăng kho/hoàn tiền hoặc sửa hóa đơn cũ. |

**Post-conditions/trạng thái:** trước bàn giao → đơn hủy hoặc phiên bản mới cần xác nhận; sau bàn giao/hóa đơn → yêu cầu xử lý chờ đủ hồ sơ/rule. **Ngoại lệ:** hủy đồng thời lúc bàn giao → kiểm tra lại, không vừa xuất vừa giải phóng sai; đã nhận tiền → giữ transaction, quy trình hoàn chưa thuộc luồng chính; sau hóa đơn → cần biên bản theo PO, loại/thời hạn Q-10; hàng trả → chỉ nhập lại sau kiểm tra Q-05. **Audit riêng:** yêu cầu khách, phiên bản, lý do, giải phóng/biên bản và xử lý tiếp. **OPEN:** Q-05, Q-08, Q-10–Q-11.

### UC-22 — Đề xuất và xác nhận đóng đơn khi nhận tiền

**Mục tiêu:** chủ hộ đóng đơn sau khi OPC ghi nhận tiền thực nhận cho đơn. **Actor:** chủ hộ. **Trigger:** có tiền thực nhận được liên kết với đơn hoặc chủ hộ mở đơn để xác nhận đóng. **Maturity/Pattern:** M1 / OPC đề xuất → chủ hộ xác nhận. **Map:** F06.07, F08.01, F08.07, F08.09, F15.01; F07.05/F09.02 dùng hiển thị riêng, không làm điều kiện chặn. **Nguồn:** PO 07/10 thay phần điều kiện đóng còn mở ở flow §4.2. **Scope:** luồng chính.

**Pre-conditions:** OPC có bản ghi thực nhận của đơn: giao dịch ngân hàng có nguồn được khớp/xác nhận liên kết, hoặc tiền mặt do chủ hộ xác nhận. Chỉ tạo QR, khách nói đã chuyển hoặc có giao dịch không rõ thuộc đơn nào chưa đủ làm căn cứ. **Dữ liệu:** đơn, bản ghi tiền/nguồn/số thực nhận/liên kết, người xác nhận đóng, thời gian; giao/hóa đơn/chênh lệch hiển thị riêng.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Xem tiền thực nhận gắn với đơn. | Giải thích nguồn, số tiền và note chênh lệch. | Kiểm tra có căn cứ tiền, không tạo thêm giao dịch thu. |
| 2 | Xem đề xuất đóng đơn. | Hỗ trợ trình bày đề xuất, không tự đóng. | Đưa đề xuất khi đã ghi nhận tiền; không chặn bởi giao/hóa đơn hoặc phần dư. |
| 3 | Bấm xác nhận đóng hoặc chưa xác nhận. | Nêu kết quả thao tác. | Chủ hộ xác nhận → đóng; chưa xác nhận → vẫn mở. |

**Post-conditions/trạng thái:** đơn mở → đã đóng sau xác nhận chủ hộ. Nếu chưa đóng, vẫn trong danh sách chờ thanh toán/công nợ theo cách gọi PO; số thực nhận luôn hiện riêng, không ghi như chưa từng có tiền. Đóng không tự đánh dấu giao/hóa đơn hoàn tất, không xóa chênh lệch hoặc tự tất toán sổ bằng số giả. Tiền có thể nhận trước/sau giao, việc giao/hóa đơn còn chờ vẫn được thao tác trên đơn đã đóng.

**Ngoại lệ:** chưa có tiền thực nhận cho đơn → chưa đề xuất đóng; chỉ có tiền dư → vẫn lưu số thật/note, chủ hộ tự xử lý, không chặn đóng; ghi nhận tiền thiếu vẫn hiển thị đúng chênh lệch, không tự đánh dấu thu đủ, không thêm điều kiện giao/hóa đơn ngoài quyết định PO. Bấm đóng lại → không đóng/thu hai lần. **Audit riêng:** nguồn tiền và liên kết làm căn cứ, đề xuất, actor/thời điểm quyết định đóng; giữ timeline các việc còn chờ. **OPEN:** Q-11 chỉ còn tiêu chí tự khớp chi tiết; quyền sửa/mở lại đơn đã đóng cần refinement, không đưa thành gate mới cho luồng đóng đã chốt.

## 5. Sổ sách và hướng dẫn eTax — Record-to-Tax

### UC-23 — Ghi sổ và truy nguồn giao dịch

**Mục tiêu:** nguồn mua/bán/kho/hóa đơn/tiền được nối, không ghi trùng doanh thu. **Actor:** chủ hộ quản lý; OPC ghi theo sự kiện hợp lệ. **Trigger:** nguồn mới hoặc sửa nguồn được xác nhận. **Maturity/Pattern:** M3 / logic xác định. **Map:** F10.01–F10.02; flow §5.1 bước 1. **Scope:** luồng chính, mẫu sổ/mốc ghi chờ kế toán.

**Pre-conditions:** nguồn có mã và quyền; mẫu/rule ghi nhận được xác nhận trước ghi sổ chính thức. **Dữ liệu:** hồ sơ nguồn và phiên bản, ngày, hàng/tiền, hóa đơn, receipt/payment, loại giao dịch/kỳ theo rule được xác nhận.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Xác nhận nguồn mua/bán/chi hoặc mở giao dịch cần xem. | Gợi ý liên kết bị thiếu. | Kiểm tra nguồn hợp lệ và đã ghi chưa. |
| 2 | Kiểm tra kết quả ghi và liên kết chứng từ. | Giải thích bản ghi hình thành từ nguồn nào. | Ghi theo rule, không lấy tiền vào làm doanh thu mặc định. |
| 3 | Khi sửa nguồn, xem lịch sử/tác động kỳ. | Chỉ ra hồ sơ và kỳ bị ảnh hưởng. | Giữ phiên bản, tránh ghi hai lần cùng sự kiện; tôn trọng khóa kỳ. |

**Post-conditions/trạng thái:** nguồn chưa ghi → đã ghi sổ khi đủ rule; thiếu căn cứ → chờ xử lý. Không tự coi khoản dư 2.000đ là bán thêm. **Ngoại lệ:** mẫu “một sổ” chưa đủ → chưa đoán cột; thiếu hóa đơn hoặc chưa rõ mốc → Q-04/Q-14; sự kiện lặp → không ghi trùng; kỳ khóa → UC-25. **Audit riêng:** rule/phiên bản, bản ghi sổ và chuỗi nguồn. **OPEN:** Q-04, Q-14.

### UC-24 — Đối soát và xử lý ngoại lệ sổ sách

**Mục tiêu:** phát hiện và giải thích thiếu/trùng/lệch giữa chứng từ, đơn và tiền. **Actor:** chủ hộ; kế toán hỗ trợ kiểm tra theo quyền được chốt. **Trigger:** kiểm tra định kỳ hoặc phát hiện mismatch. **Maturity/Pattern:** M3 / đối soát có nguồn. **Map:** F10.03–F10.05, F09.05; flow §5.1 bước 2. **Scope:** luồng chính.

**Pre-conditions:** có nguồn và bộ quy tắc so sánh; không mặc định đơn, hóa đơn và tiền luôn bằng nhau. **Dữ liệu:** kỳ/phạm vi, các hồ sơ liên kết, rule sai lệch, bản gốc, số khác và tình trạng xử lý.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Chọn phạm vi và xem danh sách lệch. | Giải thích chỗ khác và nguồn liên quan. | Đối chiếu theo rule, tách lỗi với chênh lệch có giải trình. |
| 2 | Bổ sung chứng từ/sửa liên kết đúng quyền hoặc hỏi kế toán. | Soạn thông tin cần bổ sung. | Không sửa số gốc để làm bảng khớp giả. |
| 3 | Kiểm tra lại rồi xác nhận việc đã xử lý theo policy. | Tóm tắt bằng chứng xử lý. | Lưu kết quả mới và lịch sử ngoại lệ. |

**Post-conditions/trạng thái:** ngoại lệ mới → đang xử lý → đã xử lý hoặc vẫn chờ. **Ngoại lệ:** tiền dư có note không mặc định lỗi doanh thu; invoice lỗi → UC-16; thiếu dữ liệu nguồn → chưa xác nhận hết lỗi; không có rule dung sai → báo chờ căn cứ. **Audit riêng:** lỗi/rule, nguồn trước sau, quyết định xử lý. **OPEN:** Q-14, Q-18.

### UC-25 — Khóa hoặc mở lại kỳ sổ

**Mục tiêu:** bảo vệ dữ liệu đã chốt nhưng vẫn sửa có kiểm soát. **Actor:** chủ hộ/người có quyền. **Trigger:** đề nghị chốt hoặc sửa kỳ cũ. **Maturity/Pattern:** M2 / đề xuất → duyệt. **Map:** F10.06, F14.02–F14.04; capability 6.10. **Scope:** MVP Core, điều kiện chưa chốt.

**Pre-conditions:** kỳ được xác định; có quyền và bộ điều kiện khóa/mở lại đã được duyệt. **Dữ liệu:** khoảng kỳ, snapshot, ngoại lệ, yêu cầu/lý do, người duyệt và nguồn bị ảnh hưởng.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Kiểm tra dữ liệu và đề nghị khóa/mở lại. | Tổng hợp ngoại lệ và ảnh hưởng. | Kiểm tra quyền và trạng thái kỳ. |
| 2 | Người có quyền quyết định, ghi lý do. | Chuẩn bị thông tin duyệt. | Không tự mở lại vì Agent muốn sửa nguồn. |
| 3 | Sửa khi được phép, kiểm tra rồi chốt lại theo rule. | Chỉ ra dữ liệu/hướng dẫn bị ảnh hưởng. | Lưu phiên bản; không xóa bản đã dùng trước. |

**Post-conditions/trạng thái:** đang mở → đã khóa; đã khóa → được phép mở lại theo quyết định; tên nhãn ĐỀ XUẤT. **Ngoại lệ:** sự kiện đến muộn/kỳ đã kê khai → cần Q-14–Q-16, không tự sửa kỳ cũ; còn lỗi chặn → chưa tự khóa. **Audit riêng:** snapshot, quyết định/lý do, trước/sau khóa. **OPEN:** Q-14; **khóa sổ không tự xác nhận đã nộp thuế**.

### UC-26 — Chọn quý, tổng hợp và kiểm tra hóa đơn

**Mục tiêu:** xem số tổng của quý và truy được từng hóa đơn hình thành số đó trước kê khai. **Actor:** chủ hộ. **Trigger:** chuẩn bị quý kê khai. **Maturity/Pattern:** M3 / logic xác định; luồng xem đã chốt, quy tắc số liệu thuế chờ kế toán. **Map:** F11.01–F11.02, F10.02, F10.05, F09.05; flow §5.1 bước 2–3, bổ sung PO 07/10. **Scope:** pilot Phân phối, cung cấp hàng hóa; happy path giao dịch mua/bán có hóa đơn.

**Pre-conditions:** có hồ sơ hộ/ngành nghề từ onboarding UC-31 và dữ liệu hóa đơn của hộ. Xem tổng không đồng nghĩa đủ điều kiện kê khai; quy tắc kế toán và mẫu áp dụng còn cần xác minh. **Dữ liệu:** quý/năm, ngày lập, số hóa đơn/chứng từ, bên mua/bán, hàng/tiền, loại/nguồn, hồ sơ liên quan và phiên bản. Bộ trường chi tiết, cách lấy giá trị trước/sau thuế, điều chỉnh và loại trừ chờ Q-15.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Chọn quý và năm. | Giải thích phạm vi đang xem. | Lọc hóa đơn theo ngày lập thuộc quý đã chọn, đúng hộ; không dùng ngày nhận tiền để xếp quý. |
| 2 | Xem riêng tổng doanh thu bán ra và giá trị mua vào. | Giải thích nguồn của từng tổng. | Cộng từ hồ sơ hợp lệ theo bộ quy tắc được xác nhận; chống trùng. Không lấy thu trừ chi làm doanh thu hoặc coi mua vào được trừ thuế. |
| 3 | Bấm số tổng để xổ danh sách theo tháng/ngày, mở từng hóa đơn. | Dẫn tới hóa đơn và giao dịch nguồn. | Giữ liên kết tới bản gốc, nguồn provider/nhập tay và phiên bản; tiền thực thu/chi hiển thị riêng. |
| 4 | Kiểm tra, sửa dữ liệu có căn cứ và xác nhận dữ liệu đã kiểm tra. | Chỉ rõ thay đổi và phần cần kiểm tra lại. | Cho sửa có lịch sử; thay đổi sau xác nhận phải báo cần kiểm tra lại. Không sửa trực tiếp hóa đơn điện tử đã phát hành, không sửa kết quả eTax cũ. |

**Post-conditions/trạng thái:** đang chuẩn bị → chủ hộ đã kiểm tra; sửa sau xác nhận → cần kiểm tra lại. Không tự đánh dấu đã kê khai hoặc chấp nhận. **Ngoại lệ:** nguồn trùng/lệch → UC-24; thiếu hóa đơn nằm ngoài happy path hiện tại, hiển thị thiếu, không bịa dữ liệu; ảnh viết tay chưa nhập → chờ chủ hộ nhập, không OCR; chưa đủ rule → không xuất số tính thuế như đã xác minh. **Audit riêng:** quý, tập hóa đơn/phiên bản tạo tổng, bộ quy tắc, lần xác nhận và lịch sử thay đổi. **OPEN:** Q-14–Q-15; chưa map trường hoặc tính GTGT/TNCN.

### UC-27 — Xem hướng dẫn và hỏi về trường tờ khai

**Mục tiêu:** chủ hộ hiểu mỗi ô cần gì, hình thành từ nguồn nào và tự điền trên eTax. **Actor:** chủ hộ. **Trigger:** cần điền hoặc cần hiểu một trường. **Maturity/Pattern:** M3 / hướng dẫn có nguồn. **Map:** F11.03–F11.05, F10.02; flow §5.1 bước 3–4. **Scope:** luồng chính; PO đã cung cấp và chọn mẫu 01_CNKD_TT40_2026_9172.xlsx; chưa map trường.

**Pre-conditions:** mẫu đã có; kế toán còn cần xác nhận phiên bản/phương án áp dụng và bảng trường → dữ liệu nguồn → cách hình thành ở bước sau. Đây là prerequisite, không giao chủ hộ tự xác nhận quy tắc thuế. **Dữ liệu:** mẫu/nguồn/phiên bản/thời điểm áp dụng, tên trường, giải thích đã xác nhận, liên kết dữ liệu OPC theo hộ/quý và câu hỏi người dùng. Mẫu hiện có lựa chọn khai thay, không tự dùng lựa chọn đó làm cấu hình chủ hộ.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Mở đúng mẫu/kỳ và chọn trường cần hiểu. | Giải thích theo nội dung đã xác nhận. | Đối chiếu phiên bản/mô hình hộ, báo mẫu chưa có hoặc không áp dụng. |
| 2 | Xem/hỏi dữ liệu cần và nguồn từng trường. | Chỉ rõ cần lấy dữ liệu nào, từ đâu; thiếu thì nói rõ. | Chỉ cung cấp nguồn được phép xem, giữ trace tới giao dịch/chứng từ. |
| 3 | Tự điền trên eTax, quay lại hỏi nếu cần. | Hỗ trợ giải thích, không tự sinh số thuế hoặc draft. | Không ký/gửi/nộp; không coi mở hướng dẫn là hoàn tất kỳ. |

**Post-conditions/trạng thái:** hướng dẫn chưa xem → đã xem/có lần hỏi đáp; kỳ vẫn đang xử lý/chưa có kết quả. **Ngoại lệ:** Agent không đủ căn cứ → nêu thiếu và đề nghị hỏi kế toán; hỏi trường ngoài mẫu → không bịa; mẫu hết hiệu lực → không dùng bản cũ như hiện hành; không đồng nhất mọi tiền vào là doanh thu. **Audit riêng:** câu hỏi, phiên bản hướng dẫn, nguồn được dẫn và cảnh báo thiếu. **OPEN:** Q-15; không đặt tên trường/công thức/thuế suất từ suy đoán.

### UC-28 — Xử lý yêu cầu sửa hoặc bổ sung

**Mục tiêu:** người dùng sửa đúng nguồn và biết cần bổ sung gì khi phát hiện sai hoặc eTax yêu cầu. **Actor:** chủ hộ. **Trigger:** phát hiện lỗi hoặc cung cấp yêu cầu bổ sung. **Maturity/Pattern:** M3 / hướng dẫn có nguồn. **Map:** F11.06, F10.02, F10.06; flow §5.1 bước 5. **Scope:** luồng chính; nhận yêu cầu eTax tự động chưa xác minh.

**Pre-conditions:** biết hộ/kỳ/phiên bản liên quan; có nội dung yêu cầu hoặc lỗi người dùng phát hiện. **Dữ liệu:** yêu cầu/bằng chứng eTax, trường/hồ sơ sai, nguồn cũ, thông tin bổ sung, quyền sửa và phiên bản mới.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Cung cấp yêu cầu hoặc mô tả sai. | Đọc và diễn giải việc cần bổ sung. | Lưu bản gốc, không coi yêu cầu chưa xác thực là kết quả chính thức. |
| 2 | Kiểm tra và sửa nguồn có căn cứ theo quyền. | Dẫn tới giao dịch/chứng từ đúng, nêu nội dung chưa rõ. | Cho sửa dữ liệu chuẩn bị kê khai và lưu lịch sử; báo cần kiểm tra lại nếu đã xác nhận. Hóa đơn điện tử phát hành không sửa trực tiếp; nếu nguồn là sổ đã khóa, xử lý riêng theo UC-25. |
| 3 | Tự sửa/bổ sung trên eTax. | Giải thích lại từ nguồn mới đã xác nhận. | Chưa tự gửi tờ khai bổ sung; theo dõi kết quả qua UC-29/30. |

**Post-conditions/trạng thái:** phát hiện cần bổ sung → nguồn đã sửa/chờ căn cứ; nghĩa vụ/kết quả cũ không tự đổi sang hoàn thành. **Ngoại lệ:** sai nằm ở hóa đơn → nhánh đang phát triển Q-10; kỳ khóa → UC-25; yêu cầu mơ hồ → hỏi kế toán; người dùng sửa nguồn không chứng minh đã sửa trên eTax. **Audit riêng:** yêu cầu gốc, nguồn trước sau, người sửa, lần hướng dẫn lại. **OPEN:** Q-10, Q-14–Q-16.

### UC-29 — Theo dõi tiến trình và kết quả kê khai

**Mục tiêu:** chủ hộ biết đang ở bước nào và xem được căn cứ cập nhật. **Actor:** chủ hộ; provider nếu API được xác minh. **Trigger:** mở tiến trình quý hoặc có thông tin mới. **Maturity/Pattern:** M3 / có nguồn + cập nhật tay. **Map:** F11.07, F13.03–F13.05, F15.03; flow §5.1 bước 6, bổ sung PO 07/10. **Scope:** tiến trình đã chốt; API và trạng thái sau gửi còn chờ xác minh.

**Pre-conditions:** có hồ sơ quý của hộ. Đồng bộ chỉ chạy khi API/quyền/mapping được xác minh; không có API dùng phương án chủ hộ cập nhật đã được duyệt. **Dữ liệu:** hộ/quý/năm, bước đang thực hiện, nội dung kết quả gốc, ID bên ngoài nếu có, nguồn, thời điểm cập nhật, người xác nhận và bằng chứng.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Xem tiến trình: chuẩn bị dữ liệu → kiểm tra → thực hiện eTax → đã gửi → chờ cập nhật kết quả. | Giải thích bước hiện tại từ hồ sơ có thật. | Dùng nhãn tiến trình OPC, không trình bày như phản hồi chính thức eTax. |
| 2 | Xem thông tin provider nếu có; nếu không có API thì cập nhật qua UC-30. | Nêu dữ liệu còn thiếu và nguồn cập nhật. | Xác thực/chống trùng khi tích hợp; nhập tay ghi “Chủ hộ xác nhận — chưa đối chiếu qua eTax”. |
| 3 | Mở bằng chứng hoặc xử lý bổ sung qua UC-28. | Dẫn tới thông tin liên quan, không đoán kết quả. | Sau gửi vẫn chờ cập nhật; lưu nguồn/lịch sử, không tự chuyển sang đã chấp nhận, đã nộp tiền hoặc hoàn thành nghĩa vụ. |

**Post-conditions/trạng thái:** tiến trình được cập nhật có nguồn; đã gửi → chờ cập nhật kết quả. Các trạng thái tiếp theo và điều kiện hoàn thành còn OPEN. **Ngoại lệ:** không API → dùng nhập tay có nhãn nguồn, không giả đồng bộ; dữ liệu sai hộ/quý/cũ → không gắn tự động; provider lỗi → giữ kết quả cũ và thời điểm cập nhật; nguồn mâu thuẫn → hiển thị cần đối chiếu, không ghi đè lịch sử. **Audit riêng:** nguồn/kết quả gốc, bằng chứng, người cập nhật và lịch sử tiến trình. **OPEN:** Q-13, Q-16.

### UC-30 — Ghi nhận đã gửi và lưu bằng chứng

**Mục tiêu:** lưu việc chủ hộ đã thực hiện trên eTax và căn cứ để theo dõi tiếp. **Actor:** chủ hộ. **Trigger:** chủ hộ đã gửi tờ khai hoặc có thông tin/bằng chứng mới. **Maturity/Pattern:** M3 / human xác nhận; điều kiện bằng chứng chờ kế toán. **Map:** F11.08, F09.07, F15.03; flow §5.1 bước 6, bổ sung PO 07/10. **Scope:** cập nhật tay đã được duyệt nếu provider không có API; không triển khai đóng kỳ tự động.

**Pre-conditions:** có hồ sơ đúng hộ/quý; chủ hộ có nội dung và bằng chứng cần ghi nhận. **Dữ liệu:** quý/năm, việc đã làm, thời gian, nội dung kết quả, bằng chứng/ID nếu có, số tiền nếu báo đã nộp, nguồn và người cập nhật. Bộ trường bắt buộc/bằng chứng đủ và quyền mở rộng ngoài chủ hộ chờ refinement/kế toán.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Chọn quý, nhập việc đã thực hiện và đính kèm bằng chứng. | Hướng dẫn dữ liệu cần cung cấp, không tự xác nhận thay. | Gắn đúng hồ sơ, lưu bản gốc và nguồn do chủ hộ cung cấp. |
| 2 | Kiểm tra rồi xác nhận ghi nhận đã gửi hoặc lưu thông tin mới. | Tóm tắt để chủ hộ kiểm tra. | Ghi người/thời gian; cập nhật “Đã gửi” rồi “Chờ cập nhật kết quả”; không tự ghi đã nộp thuế. |
| 3 | Xem lại, bổ sung hoặc sửa nội dung nhập có căn cứ. | Dẫn tới bản trước và nội dung cần đối chiếu. | Lưu phiên bản, không xóa lịch sử; dữ liệu sửa không tự thay kết quả eTax cũ. |

**Post-conditions/trạng thái:** đã ghi nhận việc gửi/bằng chứng → chờ cập nhật kết quả; không đồng nghĩa cơ quan thuế đã chấp nhận hoặc nghĩa vụ đã hoàn thành. **Ngoại lệ:** thiếu/sai bằng chứng → yêu cầu kiểm tra, không bịa kết quả; có thông tin nộp tiền → lưu riêng nội dung/bằng chứng, không suy từ việc gửi; cần bổ sung → UC-28. **Audit riêng:** nội dung trước/sau, bằng chứng, nguồn, actor và lần xác nhận. **OPEN:** Q-16–Q-17 cho bước sau gửi/tiêu chí bằng chứng/retention; không hỏi lại việc cho cập nhật tay.

## 6. Use Case hỗ trợ dùng chung

### UC-31 — Chuẩn bị dữ liệu nền dùng cho giao dịch

**Mục tiêu:** ba luồng dùng cùng hồ sơ hộ/ngành nghề, khách/NCC/SKU/giá và tồn đầu kỳ. **Actor:** chủ hộ. **Trigger:** onboarding hoặc thêm/sửa danh mục. **Maturity/Pattern:** M2 / nhập tay có hỗ trợ. **Map:** F01.01, F01.03–F01.04, F02.01–F02.07, F05.01, F05.08; capability 6.1–6.2. **Scope:** prerequisite chung; không phải toàn bộ onboarding. Chủ hộ tự quy định field đơn vị/quy cách; không tự quy đổi thùng–chai hoặc áp hạn mức/nợ quá hạn; F02.06 giữ lịch sử ngoài phạm vi.

**Pre-conditions:** hộ/quyền/một kho đã thiết lập. **Dữ liệu:** thông tin hộ/mã số thuế/ngành nghề đã đăng ký, bản ghi hoặc file nhập, khách/NCC, thông tin hóa đơn, SKU/đơn vị/quy cách, nguồn mua, giá và tồn đã kiểm đếm. Không yêu cầu cấu hình giảm giá/hạn mức/nợ quá hạn trong luồng này.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Nhập hoặc chọn dữ liệu cần thêm/sửa; khi onboarding nhập thông tin hộ, mã số thuế và ngành nghề đã đăng ký thuộc Phân phối, cung cấp hàng hóa. | Giải thích thông tin cần nhập, gợi ý bản ghi trùng; không tự quyết định chế độ thuế. | Lưu nguồn do chủ hộ cung cấp, kiểm tra dữ liệu; không tự gộp hoặc coi ngành nghề đăng ký đã đủ xác nhận quy tắc thuế. |
| 2 | Xác nhận giá, field đơn vị/quy cách và danh mục. | Nêu thiếu thông tin hoặc ảnh hưởng. | Lưu version; không tự quy đổi đơn vị, giảm giá hay áp chính sách chặn nợ; không âm thầm đổi đơn/hóa đơn lịch sử. |
| 3 | Xác nhận tồn đầu kỳ từ kiểm đếm. | Tổng hợp số và nguồn. | Ghi đúng một lần, có audit; không lấy tồn AI ước tính. |

**Post-conditions/trạng thái:** dữ liệu chưa đủ → dùng được cho giao dịch tương ứng; bản lỗi chưa dùng. Tồn đầu kỳ có xác nhận riêng; không thay cho nhận hàng mua về sau. **Ngoại lệ:** trùng danh mục, quy cách khác nhau, sửa giá sau có đơn, nhập file lặp → cảnh báo/kiểm tra, không nhân đôi dữ liệu. **Audit riêng:** file, kết quả kiểm tra, người xác nhận, phiên bản. **OPEN:** Q-02–Q-03, Q-18.

### UC-32 — Thiết lập và kiểm tra kết nối cần dùng

**Mục tiêu:** biết connector nào có quyền, nguồn gì và có đủ dữ liệu cho Use Case nào. **Actor:** chủ hộ/người có quyền; provider hỗ trợ. **Trigger:** thiết lập, hết quyền hoặc kết nối lỗi. **Maturity/Pattern:** M3 / consent + kiểm tra. **Map:** F13.01–F13.05, F14.01; capability 6.13. **Scope:** prerequisite chung; provider lựa chọn ở Dependency Mapping.

**Pre-conditions:** provider/khả năng tích hợp được xác minh; có quyền consent/configuration. **Dữ liệu:** connector, hộ/tài khoản, phạm vi quyền, thời hạn quyền, nguồn, kết quả kiểm tra và lần đồng bộ; không ghi secret/token thô vào audit.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Chọn kết nối và xem quyền/dữ liệu cần dùng. | Giải thích điều kiện và phần provider cung cấp. | Chỉ đưa option đã có căn cứ, không coi Casso hỗ trợ tất cả. |
| 2 | Cấp quyền theo cơ chế provider. | Hướng dẫn, không lấy quyền thay người. | Kiểm tra đúng hộ/tài khoản và trạng thái quyền. |
| 3 | Kiểm tra kết nối; xử lý hết hạn/lỗi nếu có. | Tóm tắt nguyên nhân và việc cần làm. | Hiển thị kết quả/thời điểm; retry an toàn, không tự hoàn thành nghiệp vụ. |

**Post-conditions/trạng thái:** chưa kết nối → kết nối được xác minh hoặc lỗi/chờ cấp quyền; không tự chứng minh dữ liệu eTax có sẵn. **Ngoại lệ:** thu hồi quyền, API giới hạn, thiếu chiều chi hoặc kết quả hóa đơn → chặn hành động cần nguồn đó, fallback phải chốt riêng; kết nối không đồng nghĩa giao dịch thành công. **Audit riêng:** consent/phạm vi quyền, thay cấu hình, kết quả kiểm tra; không lưu bí mật. **OPEN:** Q-13, Q-16–Q-18.

### UC-33 — Theo dõi, duyệt ngoại lệ và tiếp tục bằng tay

**Mục tiêu:** chủ hộ thấy việc chờ/lỗi, quyết định và tiếp tục trên cùng hồ sơ. **Actor:** chủ hộ. **Trigger:** dashboard/workflow có việc cần xử lý hoặc chủ hộ muốn chuyển thao tác tay. **Maturity/Pattern:** M2 / đề xuất → duyệt. **Map:** F12.01–F12.06, F14.01–F14.05, F15.01; capability 6.12–6.15. **Scope:** dùng chung cả ba nghiệp vụ.

**Pre-conditions:** có quyền trên đúng hộ/hồ sơ; thấy bước hiện tại và kết quả đã có. **Dữ liệu:** run/step, hồ sơ, đề xuất/căn cứ, ngoại lệ, việc đã thực hiện, trạng thái provider, quyết định và audit.

| Bước | Chủ hộ thực hiện | Agent hỗ trợ | OPC kiểm soát |
|---:|---|---|---|
| 1 | Xem việc chờ và mở căn cứ. | Giải thích đang làm gì, thiếu gì, định làm gì. | Hiển thị trạng thái nguồn, quyền và việc đã hoàn tất. |
| 2 | Duyệt, từ chối, sửa, dừng hoặc tiếp tục bằng tay. | Chuẩn bị phương án mới, không tự duyệt. | Áp dụng UC/rule tương ứng trên cùng hồ sơ; không chạy cạnh tranh gây trùng. |
| 3 | Xem kết quả và lịch sử; xử lý lại khi an toàn. | Nêu kết quả/lỗi có nguồn. | Timeout không tự coi duyệt; retry không tạo tiền/hàng/hóa đơn lần hai. |

**Post-conditions/trạng thái:** run đang chạy/chờ người/bị chặn → tiếp tục, dừng hoặc kết thúc khi bước thật sự đủ điều kiện; dừng run không tự hủy đơn hoặc đảo giao dịch đã xong. **Ngoại lệ:** người từ chối → không thực hiện đề xuất; timeout → chờ/chuyển ngoại lệ theo policy chưa chốt; provider kết quả chưa rõ → kiểm tra trước retry; thiếu quyền → không thao tác. **Audit riêng:** quyết định, nguồn/version, hành động đã chạy và điều khiển run. **OPEN:** Q-18.

## 7. Trạng thái và quy tắc liên luồng cần giữ

Đây là **bản đồ trạng thái business để review**, không thay State Machine chi tiết. Chỉ quy tắc ghi rõ ĐÃ CHỐT được xem là quyết định hiện tại; nhãn/transition bổ sung là ĐỀ XUẤT.

| Đối tượng | Trạng thái/diễn biến được mô tả | Quy tắc đã chốt hoặc điểm mở | Use Case |
|---|---|---|---|
| Yêu cầu bán | Mới nhận → cần làm rõ → đủ để kiểm tra | Không đoán SKU/giá; không giữ hàng vì mới nhận tin. | UC-09–UC-11 |
| Đơn mua | Nháp/xác nhận; chưa nhận/nhận thiếu/nhận đủ theo dõi riêng | Có đơn trước tăng tồn; hoàn tất nhận không chứng minh đã thanh toán. Rule đóng/hủy mở. | UC-01–UC-08 |
| Lần nhận hàng | Chưa xác nhận → đã ghi kho | Human xác nhận thực nhận, tăng kho đúng một lần. | UC-02 |
| Đơn bán | Agent đề xuất → chủ hộ duyệt; hoặc chủ hộ tạo → xác nhận; mở → đóng khi có thực nhận và chủ hộ xác nhận | Không xác nhận vượt tồn khả dụng; không dùng giao/hóa đơn/tiền dư chặn đóng. | UC-12, UC-21–UC-22 |
| Hàng giữ | Chưa giữ → đang giữ → đã dùng cho bàn giao/giải phóng | Không vượt khả dụng, không giữ hai lần; hủy trước bàn giao giải phóng. Hết hạn OPEN. | UC-13, UC-15, UC-21 |
| Giao hàng | Chưa giao → đã giao đủ khi chủ hộ bấm “Đã giao” | Lượng lấy từ đơn đã xác nhận; trừ kho một lần; không giao thiếu/giao tiếp. | UC-14–UC-15 |
| Hóa đơn | Chưa phát hành → đang chờ → có kết quả; lỗi vẫn pending/cần xử lý | “Đã giao” kích hoạt hóa đơn theo đơn; kế toán/provider xác minh. Đơn đóng không làm hóa đơn tự thành công. | UC-16 |
| Tiền | Thực nhận đã ghi → chưa khớp/đã liên kết/chênh lệch | Transaction giữ số thật; note dư không sửa hóa đơn hoặc tự tăng doanh thu. | UC-18–UC-20 |
| Phải thu/phải trả | Chưa ghi/mở → cập nhật theo phân bổ → đóng nếu đủ điều kiện | Mốc và điều kiện cần kế toán/PO xác nhận; không theo trạng thái giao đơn thuần. | UC-05, UC-18–UC-24 |
| Kỳ sổ | Đang mở ↔ khóa qua quyết định được phép | Khóa/mở có duyệt và lịch sử; không đồng nghĩa hoàn tất nghĩa vụ thuế. | UC-25 |
| Hồ sơ kê khai quý | Chuẩn bị dữ liệu → chủ hộ kiểm tra → thực hiện trên eTax → đã gửi → chờ cập nhật kết quả | Được sửa dữ liệu có lịch sử, cần kiểm tra lại sau sửa. Nhập tay kết quả có nhãn nguồn; trạng thái sau gửi và điều kiện hoàn thành chưa chốt. | UC-26–UC-30 |
| Workflow run | Đang chạy/chờ người/bị chặn/dừng/kết thúc | Dừng run không hủy nghiệp vụ; handover người–Agent dùng chung hồ sơ. | UC-33 |

### 7.1 Ba ví dụ kiểm tra xuyên suốt

1. **Nhập mua:** nhận vật lý 20 thùng, chưa có đơn → UC-01 tạo đơn → UC-02 xác nhận thực nhận 18 → kho tăng 18, còn thiếu 2. Chứng từ UC-03 và tiền chi UC-05 là việc riêng. Không tự đóng đơn mua vì đã nhập kho.
2. **Bán:** khách hỏi 10 nhưng tồn khả dụng 6 → Agent báo còn 6, chủ hộ tự trao đổi và sửa đơn thành 6; hoặc nhập thêm và cập nhật kho trước xác nhận đơn 10. Đơn Agent cần chủ hộ duyệt, đơn tay xác nhận trực tiếp. Giữ đủ theo đơn; chủ hộ giao đủ và bấm “Đã giao” → giảm kho theo lượng đơn một lần, kích hoạt hóa đơn. Không có giao thiếu/chờ hàng sau xác nhận. Nếu đã có tiền và đóng trước giao, việc giao/hóa đơn vẫn xử lý tiếp.
3. **Tiền/thuế:** hóa đơn 8.000đ, transaction 10.000đ → UC-20 liên kết đúng hồ sơ, note dư 2.000đ, không đổi hóa đơn → UC-22 đề xuất đóng, chủ hộ xác nhận; không chờ xử lý dư hoặc hoàn tất giao/hóa đơn. UC-23/24 giữ trace và giải trình, không suy 10.000đ là doanh thu. UC-27 hướng dẫn từ mẫu được xác nhận; chủ hộ tự xử lý eTax; UC-30 cần bằng chứng, không đóng kỳ chỉ vì đã đọc hướng dẫn.

## 8. Coverage Feature và phần không mở rộng

Catalog mô tả nghiệp vụ, **không ép mỗi Feature thành một Use Case độc lập**. Bảng sau là map ngược để refinement; “phụ thuộc” không có nghĩa đã mô tả hết hành vi của Feature đó.

| Nhóm Feature | Use Case / vai trò | Giới hạn coverage |
|---|---|---|
| F01.01, F01.03 | UC-31 thiết lập thông tin hộ/ngành nghề; UC-26 dùng dữ liệu này | Không đại diện toàn bộ onboarding. |
| F01.02, F01.05–F01.06 | Prerequisite người dùng/quyền/readiness | Chưa viết toàn bộ onboarding trong catalog ba nghiệp vụ. |
| F01.01/03/04; F02.01–F02.07 | UC-31; UC-01/09–UC-12 dùng dữ liệu nền | Onboarding có thông tin hộ/ngành nghề; field đơn vị/quy cách do chủ hộ. F02.06 giữ lịch sử ngoài phạm vi. |
| F03.01–F03.07 | UC-01–UC-06, UC-08 | Hai cách tạo; nhận theo thực nhận; trả đủ một lần trước/sau nhận; chưa nhận/chưa trả được sửa/hủy có lịch sử. Không thêm ứng trước một phần/mua chịu/trả nhiều lần. |
| F04.* | Không có Use Case | Đã loại chế biến/sản xuất, giữ mã lịch sử. |
| F05.01–F05.08 | UC-02/06/07/13/15/21/31 | Một kho; nhập lại hàng trả và duyệt điều chỉnh còn OPEN. |
| F06.01–F06.08 | UC-09–UC-13, UC-21–UC-22 | Không buyer portal/tự gửi Zalo/giảm giá/chặn nợ/giao một phần. Tạo tay xác nhận trực tiếp, đóng theo tiền thực nhận + chủ hộ xác nhận. |
| F07.01–F07.06 | UC-14–UC-15, UC-21–UC-22 | Giao đủ một lần bằng “Đã giao”, lượng theo đơn; carrier ngoài luồng chính, hoàn sau giao cần refinement. |
| F08.01–F08.07, F08.09 | UC-05/17–UC-20/22/24 | Ghi tiền thực tế và đối soát; chiều chi provider phải xác minh. |
| F08.08 | Nhánh tham chiếu UC-20–UC-21 | Trả nhiều lần làm sau; hoàn tiền chưa có Use Case thực hiện hoàn. |
| F09.01–F09.05, F09.07 | UC-03/04/16/23/24/30 | Giao đủ kích hoạt hóa đơn; điện tử qua provider, viết tay chụp ảnh/nhập tay, OCR sau. Rule pháp lý/kế toán cần xác minh. |
| F09.06 | Nhánh tham chiếu UC-16/21/28 | Sửa/hủy/thay thế đang phát triển; chưa có quy trình pháp lý/provider cuối cùng. |
| F10.01–F10.06 | UC-23–UC-25; UC-20/26/28 dùng chung | Cần mẫu sổ/rule ghi sổ. Riêng tập hóa đơn xem theo quý ở UC-26 đã chốt dùng ngày lập; không tự áp quyết định này cho mọi bút toán sổ. |
| F11.01–F11.08 | UC-26–UC-30 | Chọn quý, tổng riêng hóa đơn bán/mua theo ngày lập, xổ theo tháng/ngày; sửa có lịch sử. Hướng dẫn eTax/theo dõi tiến trình/cập nhật tay; GTGT/TNCN/mapping trường để sau, không tự ký/gửi/nộp. |
| F12.01–F12.06 | UC-33 và hỗ trợ mọi UC | Chưa thiết kế SLA/notification channels/retry số cụ thể. |
| F13.01–F13.05 | UC-32; UC-09/16/18/29 | Chưa chọn provider; hành vi chống trùng áp dụng xuyên suốt. |
| F13.06 | Phụ thuộc quản lý usage/chi phí chương trình | Chưa có Use Case vận hành PO đo chi phí, ngoài ba luồng chủ hộ. |
| F14.01–F14.05 | UC-33; quyền/duyệt/audit dùng chung | Chưa tạo vai trò kế toán trong app mặc định; phân quyền/retention OPEN. |
| F15.01, F15.03 | UC-22/30/33 | Chỉ dashboard nghiệp vụ/kết quả kỳ; KPI chi tiết chưa chốt. |
| F15.02, F15.04–F15.05 | Phụ thuộc onboarding/adoption/report chương trình | Không mô tả đầy đủ trong catalog ba nghiệp vụ. |
| Service Package capability 16 | Hỗ trợ thu thập mẫu, cấu hình, đào tạo/pilot | Dịch vụ, không phải hành vi phần mềm tự động hoặc Use Case chủ hộ độc lập ở đây. |

Không đổi mã Feature. BRD/Capability/Feature/Flow đã đồng bộ quyết định PO 07/10, xem phiên bản ở đầu tài liệu. Word/PRD/SRS Sales Agent/demo/slide cũ chưa đồng bộ, không dùng tự bổ sung hành vi. Phần Dev-ready vẫn cần refinement, UX/AC và xác minh dependency tương ứng.

## 9. Điểm cần chốt và xác minh

Các dòng đã chốt giữ mã Q để trace và điền quyết định ngày 07/10; không hỏi lại. Dòng thiếu đầu vào vẫn để trống câu trả lời. Phân biệt quyết định business đã đủ cho luồng đơn giản với chi tiết refinement và xác minh kế toán/provider. **PO Hiếu là đầu mối duy nhất** thu thập và cập nhật quyết định; cột bên xác nhận chỉ là nguồn cần hỏi, không lập thêm người phụ trách delivery.

| Mã | Câu hỏi cần chốt | Bên xác nhận | Use Case ảnh hưởng | Trả lời |
|---|---|---|---|---|
| Q-01 | Đã chốt tạo và sửa/hủy đơn mua đơn giản. Nhánh sau phát sinh hàng/tiền refine sau, không hỏi lại điều kiện đã chốt. | PO | UC-01, UC-08 | ĐÃ CHỐT 07/10: Agent đề xuất → chủ hộ xác nhận, hoặc chủ hộ tự tạo/xác nhận; nhà cung cấp không duyệt trên OPC. Chưa nhận hàng và chưa trả tiền thì chủ hộ được sửa/hủy, lưu lịch sử. Đã phát sinh hàng hoặc tiền thì giữ giao dịch cũ, xử lý riêng, ngoài happy path. |
| Q-02 | Mặt hàng pilot có cần ghi lô/hạn dùng không? Nếu có, bắt buộc ở nhận mua, chuẩn bị hay bàn giao; không có thông tin thì chặn hay cảnh báo? | PO khảo sát hộ | UC-02, UC-06–UC-07, UC-14, UC-31 | |
| Q-03 | Còn chi tiết refinement: dùng dữ liệu nào phân biệt trùng khách/NCC/SKU? | PO khảo sát hộ | UC-01–UC-02, UC-10, UC-31 | ĐÃ CHỐT 07/10: field đơn vị/quy cách do chủ hộ tự quy định; không mặc định tự quy đổi thùng–chai. |
| Q-04 | Còn xác minh: mốc ghi chi phí/phải trả, bộ trường/căn cứ và rule đối chiếu; chi phí không qua kho dùng nhóm/chứng từ nào? Giao dịch thiếu hóa đơn ngoài happy path, không mở rộng trong lượt này. | Kế toán; PO tổng hợp | UC-03–UC-05, UC-23 | ĐÃ CHỐT 07/10: chủ hộ ghi nhận đã trả tiền trên đơn, chọn tiền mặt/chuyển khoản, nhập số tiền/ngày và xác nhận. Trả đủ một lần trước hoặc sau nhận hàng; không ứng trước một phần/trả nhiều lần. Agent chỉ hỗ trợ đối chiếu; không chuyển tiền. |
| Q-05 | Hàng thừa/hỏng/trả mua hoặc hàng khách trả cần kiểm tra và bằng chứng nào trước cập nhật kho? Ai được duyệt điều chỉnh; nếu hàng đang giữ cho đơn khác thì xử lý ảnh hưởng thế nào? | PO; kế toán cho tiền/chứng từ | UC-06–UC-08, UC-15, UC-21 | |
| Q-06 | CẦN XÁC MINH: dữ liệu Zalo thực nhận được và quyền kết nối. Chi tiết chờ khách xử lý ở refinement. | Provider; PO tổng hợp | UC-09–UC-11 | ĐÃ CHỐT 07/10: Agent không tự gửi tin. Chủ hộ tự hỏi khách, báo tồn và báo giá. |
| Q-07 | Đã chốt, không hỏi ngưỡng giảm giá hoặc chặn nợ quá hạn cho luồng hiện tại. | PO | UC-11–UC-12, UC-22, UC-31 | ĐÃ CHỐT 07/10: không làm giảm giá; đơn chưa đóng theo dõi chờ thanh toán/công nợ. Giữ số thực nhận riêng; không tự áp policy hạn mức/nợ quá hạn. |
| Q-08 | Còn refinement: thời hạn hàng giữ nếu cần, và xử lý phiên bản khi sửa đơn đã xác nhận. Không hỏi lại đơn tay/giữ một phần/chờ nhập. | PO ở bước đặc tả | UC-12–UC-14, UC-21 | ĐÃ CHỐT 07/10: Agent đề xuất → chủ hộ duyệt; chủ hộ tự tạo → xác nhận, không duyệt thêm. Xác nhận không vượt tồn khả dụng, giữ đủ; không giữ một phần hoặc đơn xác nhận chờ nhập thêm. Chưa tự đặt thời hạn giữ. |
| Q-09 | Đã chốt thao tác giao; kế toán/provider xác minh cách thực thi hóa đơn ở Q-10/Q-13. | PO | UC-14–UC-16 | ĐÃ CHỐT 07/10: giao tay đủ, bấm “Đã giao”; lượng lấy từ đơn bán đã xác nhận, không nhập lại, không giao thiếu/giao tiếp. Trừ kho một lần và kích hoạt bước hóa đơn; lưu người thao tác/thời gian, không bổ sung bước ảnh bắt buộc. |
| Q-10 | CẦN XÁC MINH: loại hóa đơn/dữ liệu thuế nào cho pilot; phát hành khi bấm “Đã giao” có điều kiện gì; lỗi, sửa/hủy sau phát hành cần hồ sơ, thời hạn và quy trình gì? Không còn case giao 6/10. | Kế toán; provider cho hành động hỗ trợ | UC-16, UC-21, UC-28 | |
| Q-11 | Còn refinement/xác minh: rule nào đủ tự khớp tiền với đơn; khi không có mã/thiếu tiền, hiển thị và xác nhận liên kết theo căn cứ nào? Không hỏi lại điều kiện đóng đơn. | PO; kế toán/provider cho căn cứ dữ liệu | UC-17–UC-22 | ĐÃ CHỐT 07/10: có thực nhận được ghi nhận cho đơn → đề xuất đóng → chủ hộ xác nhận. Giao/hóa đơn/tiền dư không chặn đóng. Dư giữ số thật/note, chủ hộ tự xử lý; đóng không tự đánh dấu giao/hóa đơn xong hay xóa chênh lệch. |
| Q-12 | Phiếu thu/chi nhập tay cần trường/chứng từ gì, ai được sửa hoặc sửa phân bổ/note? Khi đã nhập tay rồi giao dịch ngân hàng về, dùng căn cứ nào nhận ra cùng một giao dịch để không ghi tiền hai lần? | PO; kế toán/provider cho đối chiếu | UC-05, UC-18–UC-20 | |
| Q-13 | Provider nào hỗ trợ Zalo, QR, ngân hàng chiều thu/chi và hóa đơn? Có transaction ID ổn định, xác thực webhook, tra cứu kết quả cũ và trạng thái cuối không; điều kiện chạy thật, giới hạn, giá và fallback là gì? Không mặc định một provider làm tất cả. | Provider; PO tổng hợp | UC-03, UC-05, UC-09, UC-16–UC-18, UC-32 | |
| Q-14 | Mẫu sổ gồm trường nào, mốc ghi doanh thu/chi phí/phải thu/phải trả và kỳ theo ngày nào? Chênh lệch nào chặn, ai xác nhận đã xử lý; khi nào khóa/mở lại kỳ và xử lý nguồn đến muộn thế nào? | Kế toán; PO chốt quyền | UC-23–UC-26, UC-28 | |
| Q-15 | CẦN XÁC MINH Ở BƯỚC SAU: kế toán xác nhận mẫu/phiên bản áp dụng, cách lấy giá trị hóa đơn vào tổng, xử lý điều chỉnh và quy tắc GTGT/TNCN. Mapping từng trường tờ khai chưa làm theo yêu cầu PO. | Kế toán; PO tổng hợp | UC-26–UC-28 | ĐÃ CHỐT 07/10: dùng mẫu 01_CNKD_TT40_2026_9172.xlsx; pilot Phân phối, cung cấp hàng hóa, nhập ngành nghề lúc onboarding. Chọn quý/năm, phân quý theo ngày lập hóa đơn; happy path mua/bán có hóa đơn; xem tổng riêng và xổ theo tháng/ngày. Cho sửa dữ liệu quý có lịch sử, không tự đổi kết quả kê khai trước đó. Chưa chốt công thức thuế. |
| Q-16 | CẦN XÁC MINH: provider lấy được kết quả/lịch sử/yêu cầu bổ sung eTax nào? Sau gửi có trạng thái nào, bằng chứng nào đủ xác nhận từng bước, khi có bổ sung hoặc nguồn mâu thuẫn xử lý ra sao? | Provider; kế toán; PO tổng hợp | UC-28–UC-30, UC-32 | ĐÃ CHỐT 07/10: không API thì chủ hộ cập nhật tay kèm bằng chứng, ghi rõ chưa đối chiếu qua eTax. Tiến trình OPC: chuẩn bị → kiểm tra → thực hiện eTax → đã gửi → chờ cập nhật kết quả. Không tự đánh dấu đã chấp nhận/đã nộp tiền/hoàn thành kỳ. |
| Q-17 | Chứng từ và bằng chứng được lưu loại file/dung lượng/thời gian bao lâu; ai được xem, tải hoặc thay bản mới? Audit phải giữ bao lâu và xuất lịch sử theo định dạng nào? | PO; kế toán/DEV cho căn cứ | UC-03, UC-16, UC-30, UC-32–UC-33 | |
| Q-18 | Pilot có vai trò nào ngoài chủ hộ? Timeout chờ duyệt/khách/provider, số lần retry và người nhận thông báo thế nào? Khi mất mạng được nhập gì, lúc có mạng cần kiểm tra lại gì trước duyệt/giữ hàng/phát hành? | PO; PM/DEV cho offline; provider cho SLA | UC-07, UC-10–UC-13, UC-24, UC-31–UC-33 | |

### 9.1 Defect tài liệu khác missing prerequisite

| Loại | Nhận định | Cách xử lý |
|---|---|---|
| Defect tài liệu | Tự đóng vì giao đủ; cho xác nhận vượt tồn; giữ/giao từng phần; tự giảm giá/gửi Zalo; yêu cầu giao/hóa đơn xong mới đóng; lấy tiền dư làm doanh thu | Sai quyết định PO 07/10 nếu xuất hiện trong đầu vào triển khai. Năm file baseline hiện tại đã đồng bộ; không dùng tài liệu cũ chưa cập nhật thay thế. |
| Missing prerequisite | Thiếu mẫu sổ, xác minh mẫu tờ khai đã nhận, quy tắc GTGT/TNCN/hóa đơn cho pilot, năng lực provider và tiêu chí tự khớp | Mẫu tờ khai đã có, không ghi là chưa cung cấp. Còn thiếu quy tắc/xác minh, chặn phần chi tiết/chạy thật tương ứng; mapping thuế chủ động để sau theo PO. |
| Chi tiết chuyển refinement | Nhánh sau giao/hoàn, sửa đơn đã xác nhận/đóng, hết hạn giữ, timeout, quyền và offline | Không còn câu hỏi business cần chốt ngay cho luồng đơn giản; trước DEV phải chốt chi tiết ảnh hưởng hành động tương ứng. Không tự thêm rule hoặc cam kết production. |

## 10. Cách review và tiêu chí chuyển bước

1. Review **UC-01–UC-08**: số thực nhận/đơn mua/kho/chứng từ/tiền có tách đúng không.
2. Review **UC-09–UC-22**: nhập tay và Agent có cùng hồ sơ, approval đúng, giao/hóa đơn/tiền có độc lập và ngoại lệ không mất trace không.
3. Review **UC-23–UC-30**: chọn quý/tổng hóa đơn/kiểm tra/sửa và tiến trình eTax có đúng quyết định PO không. Mẫu đã nhận; chưa map trường/công thức theo yêu cầu PO. Không coi “Đã gửi” là hoàn thành nghĩa vụ.
4. Chốt từng Q-xx với nguồn trả lời; PO quyết định phần tác động phạm vi. Nâng version catalog, không xóa ID đã được tham chiếu.

**Catalog-ready để review:** mỗi UC có actor, trigger, mục tiêu, dữ liệu, pre/post, main flow tách ba trách nhiệm, trạng thái, ngoại lệ, audit, maturity/pattern và map Feature/flow. Đây là trạng thái của tài liệu này, không phải bằng chứng app đã hoàn thành.

**Dev-ready cho một UC:** quy tắc trọng yếu/quyền/dữ liệu/ngoại lệ hết điểm chặn; dependency có chứng cứ phù hợp; sau đó mới bổ sung UX, State Machine, FR/NFR, AC và UAT cho UC đó. Không cần chờ mọi UC để phân tích slice đủ đầu vào, nhưng không chạy thật phần đang chờ kế toán/provider.

Thứ tự build giữ theo BRD §9.4: static onboarding → Foundation → Source-to-Stock → Order-to-Cash → Record-to-Tax → vận hành pilot. Catalog không thay thứ tự này, không tạo backlog hoặc chọn provider trong lần này.

### 10.1 Phần tiếp theo — Review thao tác mua hàng và nhập kho

**ĐỀ XUẤT thứ tự refinement:** đi UC-01 → UC-02 → UC-03 → UC-05 trước. Đây là luồng tạo dữ liệu hàng/hóa đơn mua vào cho bán hàng và tổng hợp quý. Không mở lại các quyết định đã chốt; chưa làm mapping thuế.

**Đã có quyết định:** hàng nhận trước vẫn phải có đơn mua trước khi xác nhận tăng tồn; tăng theo số thực nhận; một kho; chủ hộ xác nhận thực tế; hóa đơn điện tử qua provider hoặc ảnh chứng từ viết tay + nhập tay, OCR sau.

**Luồng thao tác để review:** chủ hộ tạo đơn mua → ghi hàng nhận thực tế → xác nhận nhập kho → gắn hóa đơn/chứng từ → ghi khoản tiền đã trả. Chứng từ/tiền là hồ sơ liên kết riêng, không tự tăng tồn lần nữa hoặc chứng minh đã trả tiền chỉ vì nhận hàng.

**Luồng mua đơn giản đã được PO chốt:** Agent đề xuất hoặc chủ hộ tự tạo/xác nhận đơn; nhà cung cấp không duyệt trên OPC. Nhận hàng → kiểm tra/sửa số thực nhận → xác nhận nhập kho. Trả đủ một lần trước hoặc sau nhận hàng; chủ hộ ghi nhận tiền mặt/chuyển khoản, Agent không chuyển tiền. Chưa nhận hàng và chưa trả tiền được sửa/hủy có lịch sử; nhánh sau phát sinh xử lý riêng.

**Đồng bộ đã thực hiện:** BRD 0.9, Capability 0.6, Feature 0.4 và Flow 0.3 khớp quyết định mục 0. **ĐỀ XUẤT bước tiếp theo:** thiết kế luồng thao tác/màn hình theo slice đủ đầu vào, rồi đặc tả rule/AC. Kế toán/provider, lô/hạn dùng, chống trùng tiền và nhánh refinement vẫn cần đầu vào; không coi catalog đã Dev-ready. Chưa map trường thuế theo yêu cầu PO.

## 11. Tài liệu nguồn

- [BRD OPC Platform v0.9](BRD_OPC_PLATFORM.md): §7, §9.2–9.5, §11 và §16.
- [Business Capability Map v0.6](OPC_BUSINESS_CAPABILITY_MAP.md): §4, §6.1–6.3, §6.5–6.15.
- [Feature Catalog v0.4](OPC_FEATURE_CATALOG.md): §3, §5, §8–§10; giữ mã, F04 loại và F02.06 ngoài phạm vi hiện tại.
- [Business Flow Explainer v0.3](OPC_BUSINESS_FLOW_EXPLAINER.md): §3–§6, đồng bộ quyết định PO ngày 07/10/2026.
- Quyết định PO trong chat ngày 07/10/2026: hai cách tạo đơn, Agent không tự gửi tin, field đơn vị do chủ hộ, không giảm giá, giao đủ/giao tay, lượng đơn giới hạn theo tồn và đóng khi có thực nhận + chủ hộ xác nhận.
- Quyết định PO về thuế trong chat ngày 07/10/2026: pilot Phân phối, cung cấp hàng hóa; chọn quý/năm theo ngày lập hóa đơn; tổng hóa đơn bán/mua riêng và xổ theo tháng/ngày; chứng từ viết tay nhập tay kèm ảnh, OCR sau; được sửa dữ liệu quý; theo dõi đã gửi/chờ kết quả và fallback chủ hộ cập nhật khi không có API. GTGT/TNCN và mapping trường chưa chốt.
- Quyết định PO về đơn mua trong chat ngày 07/10/2026: Agent hỗ trợ nhận biết ý định mua và đề xuất; chủ hộ xác nhận hoặc tự tạo/xác nhận đơn. Nhà cung cấp trao đổi ngoài hệ thống, không cần tài khoản/duyệt trên OPC.
- Quyết định PO về nhận hàng trong chat ngày 07/10/2026: mở đơn → “Nhận hàng” → lượng mặc định theo đơn, chủ hộ kiểm tra/sửa theo thực nhận → “Xác nhận nhập kho”; nhận 18/20 tăng 18 và theo dõi thiếu 2, không tự ghi đã trả tiền.
- Quyết định PO về trả tiền mua trong chat ngày 07/10/2026: chủ hộ ghi nhận số tiền/ngày/phương thức và xác nhận, trả đủ một lần trước hoặc sau nhận hàng. Agent hỗ trợ đối chiếu, không tự chuyển tiền; chưa làm trả một phần/nhiều lần.
- Quyết định PO về sửa/hủy đơn mua trong chat ngày 07/10/2026: chưa nhận hàng và chưa trả tiền được sửa/hủy, lưu lịch sử; đã phát sinh hàng hoặc tiền thì giữ giao dịch cũ và xử lý riêng, nhánh này refine sau, ngoài happy path.
- [Mẫu tờ khai do PO cung cấp](C:/Users/ASUS/Downloads/01_CNKD_TT40_2026_9172.xlsx): sheet “Tờ khai”, B57:F61 (ngành nghề), B207:X220 (tổng theo nhóm); Header!U26:V27 (thông tin mẫu). File gốc ngoài workspace, chưa sao chép hoặc chỉnh sửa; mẫu tham khảo được PO chọn, không phải xác minh pháp lý.
- [Word review hiện tại v1.2](../05_OPC_Presentation/OPC_BUSINESS_FLOWS_REVIEW.docx): bản dùng để trình bày, phụ lục giữ câu trả lời gốc.
- [Adobe Use Case Catalog](https://experienceleague.adobe.com/en/docs/blueprints-learn/architecture/industry-use-cases/use-case-catalog): tham khảo cách tổ chức catalog/pattern; không phải nguồn yêu cầu OPC hay tiêu chuẩn pháp lý/UML bắt buộc.

Không lấy ví dụ trong tài liệu hoặc quyết định product làm xác nhận pháp lý/thuế/khả năng API. Tài liệu cũ chưa đồng bộ chỉ có giá trị lịch sử.

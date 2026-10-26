# OPC — Luồng thao tác và kế hoạch màn hình

**Phiên bản:** 0.2  
**Ngày:** 07/10/2026  
**Product Owner:** Hiếu  
**Trạng thái:** PO đã đồng ý ba nguyên tắc bố trí bên dưới. Chi tiết màn hình và prototype vẫn cần review; chưa phải SRS hoặc backlog DEV.

## 1. Mục tiêu và nguồn

Chuyển ba nghiệp vụ đã chốt thành cách chủ hộ sử dụng OPC: bắt đầu ở đâu, bấm gì, thấy dữ liệu nào và biết kết quả ra sao. Không thêm quy tắc nghiệp vụ mới.

| Nguồn hiện tại | Vai trò |
|---|---|
| [BRD v0.9](BRD_OPC_PLATFORM.md) | Phạm vi, pilot, responsive Web và thứ tự build |
| [Capability Map v0.6](OPC_BUSINESS_CAPABILITY_MAP.md) | Nhóm năng lực và ranh giới |
| [Feature Catalog v0.4](OPC_FEATURE_CATALOG.md) | Mã Feature và phạm vi |
| [Flow Explainer v0.3](OPC_BUSINESS_FLOW_EXPLAINER.md) | Ba luồng business |
| [Use Case Catalog v0.8](OPC_USE_CASE_CATALOG.md) | 33 UC, quyết định mục 0 và các câu hỏi Q-01–Q-18 |

**ĐÃ CHỐT** là hành vi từ baseline. **ĐỀ XUẤT UX** là cách bố trí, tên màn hình, nút và cách điều hướng trong tài liệu này. **CHỜ XÁC MINH** là phần chưa đủ quy tắc/kế toán/provider; chỉ thiết kế vùng hiển thị và thông báo, chưa hứa thực thi thật.

Không dùng Word/slide/mockup/Sales Agent cũ để tự bổ sung nghiệp vụ. Không map trường tờ khai hoặc tạo lại onboarding static đã có; chỉ nêu điểm nối vào ứng dụng vận hành.

### 1.1. Quyết định UX và bản minh họa

PO đã đồng ý:

- Nhận hàng, ghi tiền và gắn chứng từ là thao tác trong hồ sơ đơn, không tách thành nhiều trang bắt buộc.
- Agent hỗ trợ; chủ hộ luôn có cách thao tác bằng tay.
- Đơn đã đóng nhưng còn chờ giao hàng/hóa đơn vẫn xuất hiện trong danh sách việc cần làm.

[Prototype mobile có thể bấm](../06_OPC_Prototype/index.html) minh họa 18 màn hình bằng dữ liệu giả, với khung iPhone Dynamic Island, iPhone tai thỏ và Android camera giữa. [Hướng dẫn review cho DEV/PO](../06_OPC_Prototype/README.md) nêu hành trình demo và giới hạn. Việc tạo prototype không phê duyệt thêm quy tắc nghiệp vụ hoặc xác nhận khả năng tích hợp.

## 2. Nguyên tắc trải nghiệm

1. Một hồ sơ dùng chung: Agent đề xuất và chủ hộ tự nhập đều mở cùng đơn/giao dịch, không tạo hai hệ thống.
2. Agent hỗ trợ, không tự đặt hàng, gửi Zalo, xác nhận thực nhận hoặc chuyển tiền.
3. Việc gây thay đổi hàng/tiền có nút xác nhận rõ và kết quả có nguồn. Lưu nháp, mở màn hình hoặc chọn phương thức không tự ghi giao dịch.
4. Một đơn bán có thông tin riêng về đơn, giao hàng, hóa đơn và tiền. Không dùng một nhãn “Hoàn tất” để che các việc còn chờ.
5. Ngay trên hồ sơ có “Hỏi Agent”; đề xuất của Agent hiển thị căn cứ, phần thiếu và hành động chờ chủ hộ.
6. Responsive Web dùng cùng chức năng trên desktop/tablet/điện thoại; bố cục có thể khác, không tách codebase mobile.
7. Thiếu dữ liệu hoặc chưa rõ kết quả provider phải hiện rõ; không hiển thị số 0/thành công thay cho chưa biết.
8. Không thêm giảm giá, chặn hạn mức/nợ quá hạn, giao từng phần, OCR hoặc tự tính/ký/gửi/nộp thuế.

## 3. Điều hướng đề xuất

| Nhóm điều hướng | Nội dung |
|---|---|
| Tổng quan | Việc đang chờ, đơn cần xử lý, cảnh báo và mở Agent |
| Mua hàng | Đơn mua, nhận hàng, chứng từ và tiền trả |
| Bán hàng | Yêu cầu Zalo, đơn bán, giao hàng và đề xuất đóng |
| Hàng hóa và kho | Sản phẩm, đơn vị/quy cách, tồn thực tế/giữ/khả dụng |
| Tiền và chứng từ | Thu/chi, liên kết tiền, hóa đơn và ảnh chứng từ |
| Sổ sách và kê khai | Truy nguồn giao dịch, tổng hóa đơn quý và tiến trình eTax |
| Thiết lập | Hồ sơ hộ, danh mục, kết nối, quyền và lịch sử |

ĐỀ XUẤT UX: desktop dùng thanh bên; mobile dùng menu gọn và lối vào nhanh cho Tổng quan/Mua/Bán/Kho. Chưa chốt số tab mobile. Agent là vùng hỗ trợ dùng chung, không bắt chủ hộ phải chat trước khi thao tác.

## 4. Danh sách màn hình

18 mã SC là đề xuất nội bộ để trace, không phải 18 Feature hoặc 18 sprint. Một màn hình có thể gồm danh sách, chi tiết và form phụ. Các hành động nhận hàng, ghi tiền, gắn chứng từ là form trong hồ sơ, không bắt mở trang riêng.

| ID | Màn hình | Thông tin chính | Thao tác chính | UC | Feature chính |
|---|---|---|---|---|---|
| SC-01 | Tổng quan vận hành | Đơn/việc chờ, kết nối lỗi, việc giao/hóa đơn còn chờ kể cả đơn đóng | Mở hồ sơ, tạo đơn mua/bán, hỏi Agent | UC-33 | F12.01/03, F15.01 |
| SC-02 | Trợ giúp và đề xuất Agent | Nội dung được cung cấp, hồ sơ liên quan, căn cứ, dữ liệu thiếu | Hỏi, sửa đề xuất, mở hồ sơ để xác nhận, từ chối | UC-01/09–12/22/27/33 | F12.02/04, F06.02, F11.05 |
| SC-03 | Hồ sơ hộ và thiết lập | Thông tin hộ, MST, ngành nghề đăng ký, cấu hình một kho | Nhập/sửa theo quyền | UC-31 | F01.01/03, F05.08 |
| SC-04 | Danh mục dùng chung | Khách, NCC, SKU, đơn vị/quy cách, giá | Tạo/sửa, xem lịch sử | UC-10/31 | F01.04, F02.01–05/07 |
| SC-05 | Kết nối và nguồn dữ liệu | Connector, phạm vi dữ liệu, quyền, lần cập nhật, lỗi | Thiết lập/kiểm tra khi provider hỗ trợ | UC-32 | F13.01–05 |
| SC-06 | Danh sách đơn mua | NCC, giá trị, nhận hàng, tiền trả, chứng từ | Tạo đơn, mở đơn, lọc việc còn chờ | UC-01/08 | F03.01–03/07 |
| SC-07 | Chi tiết đơn mua | Hàng/giá/lượng, thực nhận, chứng từ, tiền chi, lịch sử | Xác nhận đơn, nhận hàng, gắn chứng từ, ghi trả tiền, sửa/hủy đủ điều kiện | UC-01–03/05/06/08 | F03.01–04/06–07, F05.02, F08.09 |
| SC-08 | Tồn kho | Thực tế, đang giữ, khả dụng theo SKU; lịch sử biến động | Xem/hỏi tồn; xem đơn liên quan; vùng kiểm kê chờ refinement | UC-07/13/31 | F05.01–04/07–08 |
| SC-09 | Danh sách đơn bán | Khách, giá trị, đơn mở/đóng, giao, tiền, hóa đơn | Tạo đơn, mở hồ sơ, lọc việc còn chờ | UC-11/12/14/22 | F06.06–08, F07.01, F15.01 |
| SC-10 | Chi tiết đơn bán | Nguồn yêu cầu, hàng/giá/tồn, giao, hóa đơn, thực nhận/chênh lệch | Duyệt đề xuất hoặc xác nhận đơn tay; đã giao; ghi thu; liên kết tiền; xác nhận đóng | UC-11–22 | F06.05–08, F05.04–05, F07.01–05, F08.03/07/09, F09.01–02 |
| SC-11 | Yêu cầu bán từ Zalo | Tin gốc, khách/SKU gợi ý, lượng yêu cầu, phần thiếu | Làm rõ, mở đề xuất đơn | UC-09/10 | F06.01–03, F13.03 |
| SC-12 | Thu chi và đối chiếu tiền | Giao dịch tiền, nguồn, liên kết hồ sơ, chênh lệch | Ghi thu/chi, tìm đơn, xác nhận liên kết, ghi note | UC-05/17–20 | F08.02–07/09 |
| SC-13 | Hóa đơn và chứng từ | Bán/mua, ngày/số, bản gốc, nguồn, trạng thái provider | Xem chi tiết, gắn hồ sơ; ảnh viết tay + nhập tay | UC-03/04/16/24 | F03.06, F09.01–07 |
| SC-14 | Sổ giao dịch và đối chiếu | Chuỗi đơn/kho/hóa đơn/tiền, dữ liệu lệch có nguồn | Mở nguồn, xử lý liên kết theo quyền; ghi chi phí; vùng khóa sổ chờ rule | UC-04/23–25 | F03.05, F10.01–06 |
| SC-15 | Tổng hợp hóa đơn theo quý | Quý/năm, tổng bán/mua riêng, tháng/ngày, tình trạng đã kiểm tra | Xổ tổng, mở hóa đơn, sửa nguồn, xác nhận đã kiểm tra | UC-26/28 | F11.01–02/06, F10.02 |
| SC-16 | Hướng dẫn kê khai | Mẫu/phiên bản, hướng dẫn có căn cứ, dữ liệu nguồn | Xem hướng dẫn, hỏi Agent, cung cấp yêu cầu bổ sung | UC-27/28 | F11.03–06 |
| SC-17 | Tiến trình kê khai quý | Chuẩn bị/kiểm tra/thực hiện eTax/đã gửi/chờ kết quả, nguồn và bằng chứng | Ghi nhận đã gửi, cập nhật tay có bằng chứng nếu không API | UC-29/30 | F11.07–08, F15.03 |
| SC-18 | Lịch sử hồ sơ | Actor, thời gian, trước/sau, kết quả, phiên bản/nguồn | Tra cứu; xuất lịch sử khi quyền/định dạng được chốt | UC-33; dùng chung mọi UC | F14.04–05 |

Đối với UC-06, UC-07 phần điều chỉnh, UC-21 sau giao và UC-25: màn hình chỉ có vị trí để tiếp tục refinement, không có nghĩa đã đủ rule để DEV thực thi. Tất cả UC đã có điểm chạm, nhưng không phải tất cả đã sẵn sàng triển khai.

## 5. Luồng mua hàng — SC-06/07

### 5.1 Tạo đơn: hai cách, cùng một hồ sơ

**Qua Agent:** SC-02 nhận nội dung ý định mua → đề xuất hàng/NCC/lượng/giá có căn cứ → chủ hộ mở SC-07, kiểm tra/sửa → “Xác nhận đơn mua”.

**Tạo tay:** SC-06 → “Tạo đơn mua” → form SC-07 → nhập NCC/hàng/lượng/đơn vị/giá → “Xác nhận đơn mua”. Không duyệt thêm lần nữa.

| Tình huống | UI và kết quả |
|---|---|
| Thiếu NCC/SKU/giá | Chỉ rõ trường thiếu; chọn/tạo dữ liệu qua SC-04, không Agent đoán |
| Chủ hộ từ chối đề xuất | Chưa có đơn được xác nhận; không đặt hàng/tăng tồn/ghi chi |
| Hàng đã tới nhưng chưa có đơn | Tạo/xác nhận đơn trước, rồi nhận hàng; không cho tăng tồn ngoài hồ sơ mua |
| Nhà cung cấp | Không có nút “Chờ NCC duyệt”; đặt hàng trao đổi bên ngoài |

ĐỀ XUẤT UX: SC-07 có bốn phần “Hàng mua”, “Nhận hàng”, “Chứng từ”, “Tiền đã trả”, kèm timeline. Hiển thị bước cần làm, không dùng wizard bắt tuần tự vì có thể trả tiền trước nhận hàng.

### 5.2 Nhận hàng

SC-07 → “Nhận hàng” → lượng mặc định theo đơn cho lần nhận đầu → chủ hộ sửa nếu thực nhận khác → xem tóm tắt → “Xác nhận nhập kho”.

- Hiện số đặt, số đã nhận và số đang xác nhận. Không tự cộng lại phần đã nhận.
- Sau xác nhận hiện số đã tăng kho, người/thời gian và liên kết biến động SC-08.
- Đặt 20, nhận 18: kho tăng 18, thiếu 2 hiển thị riêng. Nhận tiếp là nhánh hiếm, không làm demo chính.
- Bấm lại hoặc gửi lại không tăng lần hai. Chưa rõ kết quả thì tra hồ sơ trước cho thử lại.
- Lô/hạn dùng, nhận thừa/hỏng/trả mua: Q-02/Q-05 chưa chốt; không tự đặt rule hoặc nút duyệt gây thay đổi kho.

### 5.3 Gắn chứng từ

SC-07 → “Thêm chứng từ” → nhận/chọn hóa đơn điện tử từ provider, hoặc chụp/tải ảnh viết tay và nhập thông tin → xem lại → “Lưu và liên kết”. Xem lại ở SC-13.

ĐỀ XUẤT trường để review: loại/nguồn chứng từ, số/ngày, bên bán, hàng/giá trị, file gốc và hồ sơ liên quan. Trường bắt buộc/giá trị pháp lý chờ Q-04/Q-10/Q-17. Không OCR ảnh, không tự cộng cùng hóa đơn hai lần khi provider gửi lại.

### 5.4 Ghi tiền đã trả

SC-07 → “Ghi nhận đã trả tiền” → tiền mặt/chuyển khoản, số tiền/ngày → kiểm tra liên kết → “Xác nhận khoản chi”.

Ghi khoản tiền đã thực trả, không ra lệnh chuyển tiền. Trả đủ một lần trước/sau nhận hàng; nếu có dữ liệu ngân hàng thì mở khoản đã có để đối chiếu, không tạo thêm khoản. Khi provider chưa cấp chiều chi, hiển thị nhập tay/chưa đối chiếu ngân hàng. Rule chống trùng nhập tay–ngân hàng cần Q-12.

### 5.5 Sửa/hủy

Chưa nhận và chưa trả: hiện “Sửa đơn”/“Hủy đơn”, chủ hộ xác nhận; lưu lịch sử. Đã có hàng hoặc tiền: nêu giao dịch liên quan và phần xử lý riêng còn chờ refinement, không hủy để xóa chúng. Đã có hóa đơn không có nghĩa thao tác hủy đơn tự hủy hóa đơn.

## 6. Luồng bán hàng — SC-09/10/11

### 6.1 Tạo và xác nhận

**Qua Zalo:** SC-11 tin gốc → nhận diện khách/hàng → chủ hộ làm rõ → đề xuất đơn SC-10 → chủ hộ duyệt.

**Tạo tay:** SC-09 → “Tạo đơn bán” → SC-10 chọn khách/hàng/lượng/giá → “Xác nhận đơn”. Không thêm vòng duyệt.

Trước xác nhận hiển thị lượng muốn bán, giá đã thiết lập và tồn khả dụng. Chỉ xác nhận khi lượng không vượt tồn được kiểm tra lại tại thời điểm ghi. Kho có 6/khách hỏi 10: báo “Khả dụng 6”, chủ hộ sửa tối đa 6 hoặc nhập thêm rồi quay lại; không có “Duyệt bán vượt tồn”, “Giữ một phần” hoặc “Chờ nhập sau xác nhận”.

Xác nhận thành công giữ đủ hàng cho đơn; nếu có xung đột tồn thì báo không xác nhận được và cập nhật số tồn, không giả thành công. Dùng chung hồ sơ giữa Agent và người dùng. Agent gợi ý điều cần hỏi, chủ hộ tự hỏi/báo giá/báo tồn trên Zalo.

### 6.2 Bố cục chi tiết đơn bán

ĐỀ XUẤT UX: đầu SC-10 có mã đơn/khách/nguồn, tiếp theo bốn thẻ độc lập:

| Thẻ | Hiển thị | Hành động |
|---|---|---|
| Đơn | Đề xuất/đã xác nhận/mở/đóng và lịch sử | Duyệt/xác nhận; sửa/hủy theo điều kiện |
| Giao hàng | Chưa giao/đã giao đủ, lượng theo đơn, người/thời gian | “Đã giao” khi đã giao đủ |
| Hóa đơn | Chưa phát hành/đang chờ/có kết quả/lỗi theo nguồn | Mở hóa đơn/xem lỗi; retry cần policy provider |
| Tiền | Tiền thực nhận gắn đơn, nguồn, chênh lệch, ghi chú | Ghi thu, liên kết tiền, xem đề xuất đóng |

Tên trạng thái đề xuất UX, chưa phải State Machine kỹ thuật. “Đơn mở” không đồng nghĩa chưa nhận đồng tiền nào; luôn hiện số thực nhận riêng.

### 6.3 Giao đủ và hóa đơn

SC-10 → chuẩn bị đủ hàng theo đơn → giao tay → “Đã giao”. ĐỀ XUẤT UI xác nhận ghi rõ: “Xác nhận đã giao đủ [lượng theo đơn]; OPC ghi xuất kho và bắt đầu bước hóa đơn”. Không bắt nhập lại lượng/ảnh hoặc xác nhận chuẩn bị riêng.

Sau thao tác: giao đủ, kho giảm một lần, hàng giữ được tiêu thụ; bước hóa đơn có trạng thái riêng. Provider lỗi không làm giao trở lại chưa giao, không trừ kho lần hai khi xử lý hóa đơn. Retry/tra cứu kết quả cần Q-10/Q-13.

Một hóa đơn theo đơn, điều kiện thực thi do kế toán/provider xác minh. Chưa xác minh thì prototype chỉ ghi dữ liệu mô phỏng, không diễn đạt đã tích hợp thật.

### 6.4 Thu tiền và đóng đơn

**Tiền mặt:** SC-10 → “Ghi nhận thu tiền” → nhập số thực nhận/ngày → chủ hộ xác nhận → khoản tiền liên kết đơn.

**Ngân hàng:** dữ liệu provider ở SC-12 → tự khớp bằng rule đã xác minh hoặc chủ hộ tìm/xác nhận đúng đơn → SC-10 hiển thị nguồn tiền. Có QR hoặc khách báo đã chuyển không đủ xác nhận tiền về.

**Đóng:** có tiền thực nhận gắn đơn → đề xuất “Xác nhận đóng đơn” → chủ hộ xác nhận. Không tự đóng; không thêm điều kiện giao/hóa đơn/tiền dư phải xong. Không giả đủ tiền khi có chênh lệch; rule đối chiếu còn cần Q-11.

Nếu đóng trước giao, SC-09/01 vẫn hiện “Đơn đã đóng — còn chờ giao/hóa đơn” và cho mở việc cần làm. ĐỀ XUẤT bộ lọc theo việc còn chờ, không loại hết đơn đóng khỏi danh sách vận hành.

Hóa đơn 8.000đ, tiền về 10.000đ: hiện ba số riêng và note dư 2.000đ. Không đổi hóa đơn thành 10.000đ, tự hoàn/chuyển dư hoặc dùng note để coi đã xử lý khoản dư.

### 6.5 Hủy và sửa

Chủ hộ nhận yêu cầu hủy ngoài OPC, mở SC-10 xem hàng/tiền/hóa đơn trước quyết định. Hủy hợp lệ trước bàn giao giải phóng hàng giữ, không tăng kho thực tế lần nữa. Nếu đã có tiền/hóa đơn hoặc đã giao, nêu hồ sơ cần xử lý riêng, không tự hoàn tiền/nhập lại/sửa hóa đơn. Chi tiết Q-05/Q-08/Q-10, không bổ sung chức năng hiếm vào happy path.

## 7. Luồng tổng hợp quý và theo dõi eTax — SC-15/16/17

### 7.1 Chọn quý, xem dữ liệu

SC-15 → chọn quý/năm → xem riêng “Doanh thu theo hóa đơn bán ra” và “Giá trị hóa đơn mua vào”. Bấm tổng → nhóm theo tháng → danh sách theo ngày lập → mở SC-13 → truy đơn/kho/tiền liên quan.

Quý xác định bằng ngày lập hóa đơn theo quyết định PO. Cách lấy giá trị trước/sau thuế, điều chỉnh/loại trừ chờ kế toán; không tự chọn công thức. Demo số tổng phải dùng fixture minh họa có giải thích, không gọi là số đủ để nộp thuế.

Không đổi tên hai tổng thành “Tiền đã thu/chi”, không lấy bán ra trừ mua vào làm doanh thu, không coi mua vào tự là thuế được trừ. Happy path có hóa đơn cho mua/bán; dữ liệu thiếu phải nêu thiếu chứ không tạo hóa đơn giả.

### 7.2 Kiểm tra và sửa

Chủ hộ mở hóa đơn/nguồn → sửa thông tin được phép → xem lịch sử → quay lại tổng quý → kiểm tra → “Xác nhận đã kiểm tra dữ liệu”. Nút này không gửi tờ khai hoặc khóa toàn bộ kỳ.

Sửa sau xác nhận hiển thị “Dữ liệu đã thay đổi — cần kiểm tra lại”, giữ lần xác nhận trước. Không sửa trực tiếp hóa đơn điện tử đã phát hành hoặc kết quả eTax cũ. Quyền sửa sổ đã khóa, cách xử lý hóa đơn điều chỉnh cần rule riêng Q-10/Q-14.

### 7.3 Hướng dẫn

SC-16 hiển thị mẫu đã chọn, phiên bản/nguồn và phần hướng dẫn đã được kế toán xác nhận. Có liên kết quay lại tổng quý/hóa đơn và “Hỏi Agent”. Chưa có mapping trường hoặc rule GTGT/TNCN thì hiện “Chờ xác nhận nghiệp vụ”, không tạo ô thuế tự tính/draft có số suy đoán.

Chủ hộ thực hiện trên eTax ngoài OPC. Đường dẫn/thao tác mở eTax cụ thể cần xác minh trước đưa vào thiết kế chi tiết. Không dùng nút “Gửi tờ khai”/“Nộp thuế” trên OPC như thể OPC thực thi thay người dùng.

### 7.4 Theo dõi tiến trình

ĐỀ XUẤT UX tại SC-17 dùng thanh tiến trình:

**Chuẩn bị dữ liệu → Chủ hộ kiểm tra → Thực hiện trên eTax → Ghi nhận đã gửi → Chờ cập nhật kết quả.**

Đây là tiến trình OPC, không phải thông báo chính thức eTax. Mở hướng dẫn không tự chuyển thành đã gửi. Khi chủ hộ đã gửi bên ngoài: “Ghi nhận đã gửi” → nhập nội dung/ngày và đính kèm bằng chứng → xác nhận → chờ cập nhật kết quả.

Có API được xác minh thì hiển thị kết quả và nguồn provider. Không API: chủ hộ “Cập nhật thông tin” kèm bằng chứng; nhãn “Chủ hộ xác nhận — chưa đối chiếu qua eTax”. Dữ liệu báo đã nộp tiền lưu riêng bằng chứng/nội dung, không suy từ trạng thái đã gửi. Các trạng thái tiếp theo, bằng chứng đủ và hoàn thành nghĩa vụ chờ Q-16; không tự tạo nút “Hoàn tất kỳ thuế”.

## 8. Dữ liệu và phản hồi dùng chung

### 8.1 Nguồn và quyền

Trên chi tiết hồ sơ luôn truy được nguồn nhập tay/provider/Agent đề xuất, người xác nhận và thời gian cập nhật. Chọn dữ liệu trong đúng hộ; không mở hồ sơ hộ khác. Quyền ngoài chủ hộ còn Q-18, không tự tạo portal kế toán/NCC/khách.

SC-05 phân biệt: kết nối được / có quyền lấy loại dữ liệu nào / lần cập nhật cuối / lỗi. “Đã kết nối” không đồng nghĩa đã có hóa đơn, tiền hoặc API eTax. Không hiển thị token/secret trong UI hoặc audit.

### 8.2 Trạng thái UI

| Tình huống | Phản hồi đề xuất | Không được làm |
|---|---|---|
| Chưa có dữ liệu | Nêu chưa có đơn/hóa đơn/giao dịch, đưa lối vào nhập/kết nối phù hợp | Coi chưa có dữ liệu là số thuế 0 |
| Đang tải | Hiện đang tải/lần cập nhật trước nếu có | Cho số cũ trông như vừa cập nhật |
| Thiếu trường | Chỉ rõ trường/hồ sơ cần bổ sung | Agent đoán SKU/giá/thuế |
| Chờ chủ hộ | Hiện đề xuất, căn cứ, sửa/duyệt/từ chối | Agent tự duyệt |
| Chờ provider | Hiện đang chờ và nguồn yêu cầu | Ghi thành công trước có kết quả |
| Kết quả chưa rõ | Tra cứu hồ sơ/nguồn trước thử lại | Retry phát hành/ghi hàng/tiền mù gây trùng |
| Thao tác đồng thời | Báo dữ liệu đổi, tải bản mới để kiểm tra | Ghi đè bản cũ hoặc bán vượt tồn |
| Không quyền | Giải thích thao tác không được phép | Dùng Agent vượt quyền |
| Mất mạng | Hiện mất mạng/chưa đồng bộ; không giả đã xác nhận trên server | Hứa thao tác kho/tiền ngoại tuyến khi policy chưa chốt |

Offline phải được phân tích với PM/DEV theo Q-18 và yêu cầu nguồn tỉnh; tài liệu này không âm thầm loại hoặc cam kết giải pháp offline.

### 8.3 Responsive

ĐỀ XUẤT UX: desktop bảng + panel chi tiết; tablet bố cục gọn; điện thoại danh sách thẻ, chi tiết một cột, form phụ thành trang/panel toàn màn hình. Hành động chính dễ tìm, luôn có nhãn chữ; màu không phải cách duy nhất phân biệt trạng thái. Bảng hóa đơn quý xổ từng tháng, không bắt kéo ngang toàn bộ báo cáo để mở hóa đơn.

Giữ nguyên kiểm tra/xác nhận/audit trên mọi kích thước. Nút chụp ảnh phục vụ chứng từ viết tay, không tự nhận dạng nội dung. Upload type/size/retention chưa chốt Q-17.

## 9. Ví dụ walkthrough để review

| Ví dụ | Thao tác cần nhìn thấy | Kết quả kiểm tra UX |
|---|---|---|
| Mua 20 thùng, nhận 18 | SC-02/06 → SC-07 xác nhận đơn → nhận 18 → xem SC-08 | Tồn tăng 18 một lần, thiếu 2; không tự ghi tiền đã trả |
| Trả đủ tiền mua trước nhận | SC-07 ghi tiền/ngày/phương thức → nhận hàng sau | Không bắt nhận trước mới ghi chi; không coi đã trả là đã nhận |
| Bán 10 nhưng kho còn 6 | SC-11/10 → xem khả dụng → sửa lượng 6 hoặc nhập thêm | Không cho xác nhận 10/giữ một phần/chờ nhập sau xác nhận |
| Bán giao đủ | Xác nhận đơn → giữ đủ → “Đã giao” → xem hóa đơn | Lượng theo đơn, trừ kho một lần, hóa đơn chờ/lỗi không giả thành công |
| Nhận tiền và đóng trước giao | SC-12 liên kết → SC-10 xác nhận đóng → mở việc giao | Đơn đóng nhưng giao/hóa đơn còn hiện và thao tác được |
| Hóa đơn 8.000đ, nhận 10.000đ | SC-12 liên kết/note → SC-10 đóng | Giữ số thật, note 2.000đ, không bắt giải quyết dư mới đóng |
| Chuẩn bị quý | SC-15 chọn quý → xổ theo tháng/ngày → mở SC-13 | Có nguồn và ngày lập; bán/mua/tiền là số riêng |
| Sửa sau kiểm tra quý | SC-15 xác nhận → sửa nguồn → quay lại | Cần kiểm tra lại; giữ lịch sử, không sửa kết quả kê khai cũ |
| Không API eTax | SC-17 ghi nhận đã gửi + bằng chứng | Có nhãn chủ hộ xác nhận; chờ cập nhật, không tự hoàn thành kỳ |

Ví dụ là dữ liệu minh họa để review, không phải bộ UAT đầy đủ hoặc chứng minh tích hợp chạy thật.

## 10. Phần cần review và mức sẵn sàng

### 10.1 PO review cách dùng, không hỏi lại business đã chốt

| Đề xuất UX cần review | Lý do |
|---|---|
| Dùng chi tiết đơn làm nơi nhận hàng/gắn chứng từ/ghi tiền, không tách nhiều trang | Chủ hộ nhìn được một hồ sơ và ít di chuyển |
| Agent là trợ giúp dùng chung, đồng thời vẫn có nút tạo tay | Không bắt dùng chat cho mọi việc |
| Đơn bán có bốn thẻ riêng và lọc theo việc còn chờ kể cả đã đóng | Không bỏ sót giao/hóa đơn sau khi nhận tiền |
| Tổng hóa đơn quý xổ theo tháng/ngày; tiến trình eTax ở màn hình riêng có liên kết cùng quý | Tách kiểm tra dữ liệu với bằng chứng việc đã làm ngoài OPC |

### 10.2 Điểm chưa đủ để triển khai thật

| Điểm mở | Tham chiếu | Ảnh hưởng |
|---|---|---|
| Trường bắt buộc, trùng danh mục, lô/hạn dùng | Q-02/03/04 | Form hàng/nhận/chứng từ chưa đóng schema |
| Điều chỉnh/hoàn sau phát sinh, sửa đơn đã xác nhận, hết hạn giữ | Q-05/08/10 | Không build nhánh rủi ro từ placeholder UX |
| Rule khớp tiền và chống trùng nhập tay/provider | Q-11/12/13 | Chưa đủ tự động đối soát/giảm nợ thật |
| API/quyền/trạng thái phát hành/tra cứu và kết quả eTax | Q-06/10/13/16 | Không cam kết integration hoặc retry chưa kiểm chứng |
| Rule sổ, GTGT/TNCN, giá trị tổng và mẫu áp dụng | Q-14/15 | Không đưa số thuế hoặc kết luận hợp lệ chưa xác minh |
| Vai trò, bằng chứng, lưu trữ, timeout và offline | Q-17/18 | Cần chốt trước DEV hành động tương ứng |

**Lưu ý diễn đạt ở nguồn:** UC-21 còn cụm “kiểm tra lại giá/nợ/tồn nếu sửa”. Theo mục 0 và F06.06 hiện tại, nợ chỉ là thông tin theo dõi, không là rule chặn/phê duyệt. UX không đưa lại hạn mức/nợ quá hạn. Đây là điểm wording cần làm rõ, không phải quyết định business mới.

**Kết luận:** đủ làm đầu vào review UX/wireframe happy path, chưa Dev-ready toàn bộ. Chưa sửa lại BRD/Capability/Feature/UC để biến đề xuất bố cục thành yêu cầu đã duyệt.

## 11. Thứ tự thực hiện tiếp

1. PO/DEV review chi tiết màn hình ở mục 10.1 trên prototype, ưu tiên SC-07 và SC-10; ba nguyên tắc tại mục 1.1 đã được đồng ý.
2. Prototype đã có bản clickable cho Foundation → mua/kho → bán/tiền → tổng quý/tiến trình, dùng fixture có nhãn mô phỏng. Chọn hành trình và hình đưa vào proposal sau review. Static onboarding vẫn đi trước main MVP theo BRD §9.4.
3. Xác minh kế toán/provider và chốt rule còn mở song song; chưa map trường thuế khi PO chưa yêu cầu.
4. Sau đó tách đặc tả hành vi, State Machine, AC và UAT cho slice đủ đầu vào; không tạo lại backlog Sales Agent cũ như baseline mới.

Không có deadline/estimate trong tài liệu này; chưa có dữ liệu về đội DEV hoặc năng lực tích hợp để cam kết.

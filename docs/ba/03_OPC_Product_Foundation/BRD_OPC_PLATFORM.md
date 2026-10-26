# BRD OPC Platform

**Phiên bản:** 0.9  
**Ngày:** 07/10/2026  
**Trạng thái:** Phạm vi và ba luồng tổng thể đã chốt với PO; chi tiết kế toán và provider cần xác minh  
**Product Owner:** Hiếu  
**Phạm vi tài liệu:** Định nghĩa OPC ở cấp độ business, chưa phải tài liệu để DEV bắt đầu xây

Đồng bộ quyết định PO ngày 07/10/2026 với [Use Case Catalog v0.8](OPC_USE_CASE_CATALOG.md), Capability Map v0.6, Feature Catalog v0.4 và Flow Explainer v0.3. Word, slide, PRD draft và bộ Sales Agent cũ chưa đồng bộ trong lượt này. Không coi quyết định product là xác minh pháp lý hoặc năng lực provider.

## 1. Mục đích tài liệu

Tài liệu này trả lời bốn câu hỏi:

1. OPC phục vụ ai và giải quyết vấn đề gì?
2. OPC cần hỗ trợ vòng đời kinh doanh nào?
3. OPC gồm các nhóm năng lực business nào?
4. Phần nào OPC sở hữu, phần nào dùng bên thứ ba như Casso?

Tài liệu này đứng trước PRD chi tiết, use case specification, workflow, SRS và backlog.

## 2. Tóm tắt

OPC được định hướng là một nền tảng vận hành end-to-end cho hộ kinh doanh và doanh nghiệp một người có ít nhân sự. Sản phẩm kết hợp dữ liệu nghiệp vụ, quy tắc xác định, AI Agent và cơ chế con người phê duyệt.

Phạm vi hiện tại gồm ba nghiệp vụ: mua hàng và kho; bán hàng, hóa đơn và tiền; sổ sách và hướng dẫn điền tờ khai eTax. Đã bỏ chế biến. Agent hỗ trợ; chủ hộ có thể tự thao tác ở mọi khâu trên cùng hồ sơ. Đơn do Agent tạo chờ chủ hộ duyệt trước khi xác nhận và giữ hàng.

OPC không chỉ là một ứng dụng tích hợp Casso. Casso hoặc provider khác là phương án cần đánh giá cho các kết nối ngân hàng, hóa đơn và dữ liệu thuế. Không mặc định provider hỗ trợ mọi kết nối; phạm vi, điều kiện và giá phải được xác minh. OPC vẫn sở hữu trải nghiệm người dùng, dữ liệu nghiệp vụ, quy trình, đối soát, sổ sách, logic xác định, phê duyệt và audit; phần thuế hiện tại là hướng dẫn điền eTax và truy nguồn dữ liệu.

Sales Operations Agent hiện có là demo tham khảo cho luồng bán hàng trong **Slice 3 – Order-to-Cash**. Thứ tự build MVP đi từ static onboarding, nền tảng dữ liệu, nguồn hàng và kho đến bán hàng, thuế và vận hành pilot, theo mục 9.4 và Feature Catalog.

## 3. Bối cảnh business

### 3.1 Nguồn gốc chương trình

- Tỉnh Gia Lai đang chuẩn bị Chương trình Kế nghiệp số để hỗ trợ hộ kinh doanh có thế hệ kế cận chuyển đổi và vận hành theo mô hình doanh nghiệp.
- Đề bài ưu tiên người kế nghiệp từ 25 đến 40 tuổi đang trực tiếp tham gia quản lý.
- Đợt làm việc hiện tại là khảo sát và tham vấn thị trường. Tài liệu của tỉnh nói rõ đây chưa phải đấu thầu và chưa tạo cam kết mua sắm.
- Giai đoạn đánh giá Casso cũng là bước xác định tính khả thi, chưa phải cam kết tích hợp thật.

### 3.2 Quy mô cần tách rõ

| Nhóm chương trình | Số liệu trong tài liệu tỉnh | Cách hiểu hiện tại |
|---|---:|---|
| Hộ kinh doanh chuyển đổi thành doanh nghiệp | 3.000 / 32.500 | Hai số xuất hiện trong slide chương trình. Cần PM xác nhận ý nghĩa của từng số. |
| Doanh nghiệp một người hoặc khởi nghiệp tinh gọn dùng AI | 1.200 / 3.680 | Đây là nhóm được slide gọi trực tiếp là OPC. Cần PM xác nhận số mục tiêu và tổng nguồn. |
| Pilot Kế nghiệp số | 5 đến 10 hộ trong quý IV/2026 | Nêu trong bài toán đặt hàng. |
| Các khóa từ năm 2027 | 100 đến 150 hộ mỗi khóa | Chỉ mở rộng hàng nghìn hộ mỗi năm sau khi mô hình được kiểm chứng. |

Biên bản họp ngày 30/09/2026 nhắc khoảng 3.000 user. Con số này có thể thuộc nhóm chuyển đổi hộ kinh doanh, không nhất thiết là toàn bộ người dùng OPC. Không dùng con số 3.000 để tính kiến trúc hoặc chi phí trước khi PM xác nhận.

### 3.3 Người dùng và ngành ưu tiên

Đề bài của tỉnh yêu cầu giải pháp phục vụ ba chân dung:

1. Hộ cung cấp hải sản, cá mắm và đặc sản qua khách sạn, cửa hàng và kênh online.
2. Hộ cung cấp dịch vụ du lịch biển tổng hợp như ăn uống, homestay, thuyền và tour.
3. Hộ thu mua, sơ chế nông sản và bán cho doanh nghiệp hoặc bán lẻ online.

Các hộ thường có bố mẹ phụ trách sản xuất hoặc dịch vụ, còn người kế nghiệp quản lý kênh số và khách hàng. Nhu cầu chung gồm bán hàng, tiền về, hóa đơn, chi phí, công nợ, tồn kho hoặc lịch dịch vụ, sổ sách và nghĩa vụ thuế.

### 3.4 Nguyên tắc tỉnh đặt ra cho giải pháp

- Tận dụng sản phẩm thương mại đã vận hành ổn định và cấu hình theo bài toán Gia Lai. Đề bài không đặt hàng xây một ứng dụng riêng cho tỉnh.
- Tận dụng nền tảng miễn phí của Nhà nước và thị trường. Không thu phí trùng cho phần đã có sẵn.
- Giá trị có thu phí nên tập trung vào vận hành, bán hàng và dịch vụ còn thiếu.
- Đo bằng sử dụng thật như kích hoạt, hóa đơn, giao dịch và duy trì sau 90 ngày; không chỉ đếm tài khoản hoặc buổi đào tạo.
- Ưu tiên điện thoại, người ít quen công nghệ, thiết bị phổ thông và mạng yếu. Tối thiểu nghiệp vụ bán hàng cần tiếp tục hoạt động khi mất mạng và đồng bộ lại khi có mạng.
- Có hướng dẫn và hỗ trợ trực tiếp tại Gia Lai trong giai đoạn thiết lập và kỳ kê khai đầu tiên.
- Người dùng phải xuất được dữ liệu của mình để tránh bị khóa vào một nhà cung cấp.

### 3.5 Điểm cần phản biện trước khi chốt product

- Đề bài tỉnh yêu cầu dùng sản phẩm thương mại ổn định, trong khi OPC hiện mới có mockup và tài liệu MVP. OPC sẽ được trình bày là sản phẩm đang được kiểm chứng qua pilot; PM cần xác nhận cách tiếp cận này có đủ điều kiện đưa vào proposal hay không.
- OPC đã chọn responsive Web làm bề mặt chung cho máy tính, tablet và điện thoại. Cần xác nhận tiêu chí nghiệm thu của chương trình có chấp nhận cách tiếp cận này thay cho native app hay không.
- Đề bài yêu cầu giải quyết trọn vẹn ba chân dung, nhưng Sales Operations Agent hiện chỉ chứng minh một vertical slice của chân dung cung ứng cho khách sạn.
- Báo cáo Casso chỉ giúp đánh giá một số kết nối. Nó không chứng minh OPC đã đáp ứng toàn bộ bài toán của tỉnh.

### 3.6 Nhóm triển khai hiện tại

PO chọn hộ kinh doanh nhỏ lẻ mua hàng về, tập trung Phân phối, cung cấp hàng hóa và vận hành đơn giản. Khoảng doanh thu theo tháng và danh sách hộ còn cần khảo sát; không dùng doanh thu trao đổi như ngưỡng thuế đã xác nhận. Ba chân dung tỉnh ở mục 3.3 là bối cảnh nguồn, không phải tất cả thuộc proposal hiện tại.

## 4. Vấn đề cần giải quyết

### 4.1 Vấn đề của người vận hành

- Dữ liệu bán hàng, ngân hàng, hóa đơn và thuế nằm ở nhiều nơi.
- Người vận hành phải nhập lại, kiểm tra và nối dữ liệu bằng tay.
- Sai lệch tiền, hóa đơn hoặc công nợ thường được phát hiện muộn.
- Một người khó nhớ mọi việc đang chờ, ngoại lệ và hạn xử lý.
- Quy trình pháp lý và thuế khó hiểu, nhưng hệ thống không được tự suy đoán thay chuyên gia.

### 4.2 Vấn đề của chương trình triển khai

- Khó chứng minh người dùng đã thiết lập xong và đang sử dụng thật.
- Năng lực quản trị của doanh nghiệp nhỏ còn dựa nhiều vào kinh nghiệm; tài chính, vận hành, thị trường và công nghệ số chưa được quản lý đồng bộ.
- Người dùng miền núi hoặc ít quen công nghệ cần hỗ trợ tại chỗ, không chỉ được cấp tài khoản và tài liệu hướng dẫn.
- Chi phí tích hợp có thể tăng theo số tài khoản, giao dịch, hóa đơn hoặc lượt gọi API.
- Phụ thuộc bên thứ ba có thể làm gián đoạn luồng nghiệp vụ.
- Nếu không tách rõ ranh giới, stakeholder có thể hiểu nhầm khả năng của OPC hoặc Casso.

### 4.3 Hậu quả nếu không giải quyết

- Chủ hộ vẫn phải vận hành bằng nhiều công cụ rời rạc.
- Dữ liệu không đủ tin cậy để tự động hóa hoặc lập báo cáo.
- Rủi ro ghi nhận sai tiền, trùng giao dịch, thiếu chứng từ hoặc bỏ lỡ hạn xử lý tăng lên.
- OPC trở thành một lớp giao diện mỏng quanh nhà cung cấp thay vì một sản phẩm có giá trị riêng.

## 5. Người dùng và stakeholder

| Nhóm | Nhu cầu chính |
|---|---|
| Chủ hộ hoặc owner operator | Biết việc gì đang xảy ra, việc gì cần quyết định và tiền, hàng, hóa đơn, thuế đang ở trạng thái nào. |
| Người kế nghiệp từ 25 đến 40 tuổi | Thiết lập và vận hành doanh nghiệp bằng quy trình rõ ràng trên điện thoại, đồng thời phối hợp được với bố mẹ đang phụ trách sản xuất hoặc dịch vụ. |
| Kế toán hoặc cố vấn nghiệp vụ | Kiểm tra quy tắc, dữ liệu, sổ sách, kỳ thuế và ngoại lệ. |
| Khách hàng của hộ | Nhận xác nhận đơn, thanh toán và hóa đơn rõ ràng. |
| Nhà cung cấp của hộ | Gửi hàng, chứng từ và nhận thanh toán đúng. |
| Đội triển khai | Hướng dẫn thiết lập, theo dõi readiness và hỗ trợ kỳ vận hành đầu. |
| PM và chương trình | Theo dõi adoption, kết quả sử dụng, chi phí và rủi ro. |
| Bên thứ ba | Cung cấp kết nối ngân hàng, hóa đơn, thuế, định danh hoặc dịch vụ liên quan. |

## 6. Mục tiêu business

1. Giúp một người quản lý được các luồng kinh doanh quan trọng mà không phải nhập lại cùng dữ liệu nhiều lần.
2. Kết nối bán hàng, tiền, hóa đơn, sổ sách và thuế thành một dòng dữ liệu có thể truy vết.
3. Tự động hóa việc an toàn và đưa ngoại lệ cho con người quyết định.
4. Cho người vận hành thấy nguồn dữ liệu, lý do và trạng thái của mỗi hành động.
5. Giảm phụ thuộc vào một nhà cung cấp bằng kiến trúc adapter và ranh giới dữ liệu rõ ràng.
6. Tạo nền tảng để mở rộng theo module và ngành nghề, không xây toàn bộ ERP ngay từ đầu.
7. Giúp hộ truy lại dữ liệu giao dịch, hiểu cách điền tờ khai trên eTax và theo dõi kết quả từng kỳ khi có căn cứ.

Các mục tiêu định lượng sẽ được chốt sau khi có baseline về thời gian xử lý, lỗi nhập liệu, tỷ lệ đối soát và mức sử dụng hiện tại.

Pilot tạo giá trị khi hộ hoàn tất onboarding, phát sinh giao dịch thật, quản lý hóa đơn/tiền và dùng được hướng dẫn eTax có dữ liệu nguồn. Mục tiêu theo dõi kỳ hoàn thành phụ thuộc nguồn kết quả được xác minh; chỉ số duy trì sau 90 ngày và tỷ lệ đạt còn cần baseline.

## 7. Vòng đời business OPC cần hỗ trợ

1. **Thiết lập doanh nghiệp:** hồ sơ, người dùng, chính sách, dữ liệu và kết nối.
2. **Quản lý dữ liệu nền:** khách hàng, nhà cung cấp, sản phẩm, đơn vị tính, bảng giá và điều khoản thanh toán.
3. **Mua hàng và nhập kho:** tạo yêu cầu mua, ghi nhận hàng nhập, chi phí và chứng từ đầu vào.
4. **Quản lý kho:** một kho chứa nhiều hàng; theo dõi tồn thực tế, hàng giữ và lịch sử.
5. **Bán hàng và quản lý đơn:** khách lẻ hoặc doanh nghiệp dùng chung luồng; chủ hộ thiết lập giá; Agent kiểm tra và tạo đơn chờ chủ hộ duyệt, hoặc chủ hộ tự tạo tay.
6. **Chuẩn bị và giao hàng:** xác nhận trong tồn khả dụng, giữ đủ; chủ hộ giao đủ rồi bấm “Đã giao”, lượng lấy theo đơn và trừ kho một lần. Giao trực tiếp; vận chuyển tích hợp là Nice to have.
7. **Quản lý hóa đơn và chứng từ:** giao đủ kích hoạt một hóa đơn theo đơn; kế toán/provider xác minh thực thi. Điện tử qua provider, viết tay chụp ảnh/nhập tay; OCR sau.
8. **Thu và chi tiền:** tiền mặt nhập tay; chuyển khoản tích hợp ngân hàng thật là mục tiêu. Ghi tiền thực nhận và giải thích chênh lệch.
9. **Sổ nghiệp vụ và đối soát:** nối đơn, kho, tiền, hóa đơn và chi phí; không ghi tăng doanh thu vì nhận tiền dư.
10. **Chuẩn bị và hướng dẫn eTax:** chọn quý/năm, tổng riêng hóa đơn bán/mua theo ngày lập, xổ theo tháng/ngày; kiểm tra/sửa có lịch sử. Mẫu đã chọn; GTGT/TNCN/mapping trường để sau. Chủ hộ thực hiện điền/sửa/gửi/nộp trên eTax.
11. **Theo dõi kết quả kỳ:** đã gửi → chờ cập nhật; API nếu được xác minh, không API thì chủ hộ cập nhật kèm bằng chứng/nhãn nguồn. Trạng thái tiếp theo và điều kiện hoàn thành còn mở.
12. **Theo dõi và cải thiện:** xử lý ngoại lệ, audit, đo hiệu quả và cập nhật chính sách.

## 8. Bản đồ năng lực business

| Nhóm năng lực | Giá trị business | Ghi chú ownership |
|---|---|---|
| Business Onboarding | Đưa một hộ từ chưa thiết lập đến trạng thái sẵn sàng vận hành. | Cần cả hướng dẫn, readiness và connection setup. |
| Master Data and Party Management | Quản lý khách hàng, nhà cung cấp, sản phẩm, đơn vị tính, giá và điều khoản. | OPC sở hữu dữ liệu chuẩn và lịch sử thay đổi. |
| Sales and Order Management | Quản lý yêu cầu bán, báo giá, đơn hàng, công nợ và trạng thái xử lý. | OPC sở hữu; AI chỉ hiểu yêu cầu và đề xuất. |
| Inventory and Warehouse | Quản lý tồn khả dụng, giữ hàng, nhập, xuất, điều chỉnh và truy vết. | OPC dùng logic xác định; không để AI tự tính tồn. |
| Purchase and Expense | Quản lý mua hàng, nhà cung cấp, chi phí và chứng từ đầu vào. | Cần cho tồn kho, sổ sách và thuế. |
| Fulfilment and Delivery | Chuẩn bị, bàn giao và ghi nhận hàng thực giao. | Giao trực tiếp là trọng tâm; tích hợp vận chuyển là Nice to have. |
| Money, Receivables and Payables | Theo dõi phải thu, phải trả, tiền về, tiền đi và chênh lệch. | OPC sở hữu capability và kết quả đối soát. |
| Invoice and Documents | Quản lý hóa đơn bán ra, hóa đơn đầu vào và chứng từ liên quan. | OPC sở hữu capability và trạng thái chứng từ. |
| Books and Reconciliation | Nối tiền, hóa đơn, doanh thu và chi phí thành dữ liệu có thể giải thích. | OPC sở hữu quy tắc và kết quả. |
| Tax Guidance and Period Tracking | Hướng dẫn cách điền eTax, truy dữ liệu nguồn và lưu kết quả kỳ. | Người dùng thực hiện trên eTax; nguồn đồng bộ kết quả cần xác minh. |
| Agent Control Tower | Theo dõi trợ giúp Agent, duyệt đề xuất và tiếp tục bằng tay trên cùng hồ sơ. | Năng lực chung của OPC. |
| Integration Administration | Quản lý kết nối, quyền, token, lỗi, SLA và chi phí. | OPC quản lý vòng đời; bên thứ ba cung cấp dịch vụ. |
| Access, Approval and Audit | Quản lý quyền, duyệt và lịch sử chỉ ghi thêm. | Dùng chung cho Agent và thao tác tay. |
| Business and Program Monitoring | Theo dõi vận hành, onboarding và kết quả pilot. | Chỉ số và mức dữ liệu cần chốt. |
| Implementation, Training and Customer Success | Khảo sát, cấu hình, nhập dữ liệu, đào tạo, hỗ trợ và duy trì sử dụng sau kích hoạt. | Service capability bắt buộc của đơn vị cung cấp OPC. |

## 9. Phạm vi business

### 9.1 Phạm vi định nghĩa sản phẩm

- Bao phủ toàn bộ vòng đời từ thiết lập đến vận hành và chốt nghĩa vụ.
- Định nghĩa module, use case, ranh giới và thứ tự triển khai.
- Cho phép nhiều connector thay thế nhau nếu có cùng hợp đồng dữ liệu.
- Hỗ trợ AI Agent nhưng giữ dữ liệu và quyết định rủi ro trong vùng kiểm soát.

### 9.2 Phạm vi build đã có quyết định

- Static onboarding demo được làm trước main MVP.
- OPC dùng một product core và cấu hình theo ngành, không xây ba sản phẩm riêng cho ba chân dung.
- Nhóm pilot hiện tại là hộ kinh doanh nhỏ lẻ, tập trung Phân phối, cung cấp hàng hóa; thông tin ngành nghề đã đăng ký được nhập khi onboarding. Danh sách pilot và khoảng doanh thu theo tháng cần khảo sát. Ví dụ bán B2B cho khách sạn không giới hạn chân dung người dùng.
- Pilot bắt đầu với 5 đến 10 hộ. Các con số 3.000 và 1.200 chưa dùng làm cơ sở sizing production.
- Sales Operations Agent thuộc Slice 3 – Order-to-Cash, được build sau Foundation và Source-to-Stock. Demo Sales hiện có giúp minh họa luồng này, nhưng chưa phải toàn bộ MVP.
- MVP bắt đầu từ onboarding, thiết lập dữ liệu nền, kết nối nguồn dữ liệu, mua hàng và nhập tồn ban đầu.
- Sản phẩm quản lý hàng mua về, không có nghiệp vụ chế biến. Một kho chứa nhiều hàng.
- Nhận hàng có thể diễn ra trước khi nhập đơn, nhưng xác nhận tăng tồn bắt buộc có đơn mua và chủ hộ xác nhận số thực nhận.
- Đơn mua có hai cách: Agent nhận biết ý định mua từ nguồn được phép và đề xuất để chủ hộ xác nhận, hoặc chủ hộ tự tạo/xác nhận. Nhà cung cấp trao đổi bên ngoài, không cần tài khoản/duyệt trên OPC. Nhận hàng: lượng mặc định theo đơn, chủ hộ kiểm tra/sửa theo thực nhận rồi xác nhận nhập kho đúng một lần.
- Chủ hộ ghi khoản chi tiền mặt/chuyển khoản, số tiền/ngày và xác nhận; trả đủ một lần trước hoặc sau nhận hàng. Chưa làm ứng trước một phần/trả nhiều lần. Đơn mua chưa nhận và chưa trả được sửa/hủy có lịch sử; sau phát sinh hàng/tiền xử lý riêng, ngoài happy path.
- MVP gồm mua hàng, kho, bán hàng, hóa đơn, tiền, công nợ, chi phí, sổ nghiệp vụ, đối soát và hướng dẫn eTax. Phạm vi proposal và các nhánh làm sau được phân biệt tại mục 9.5.
- Người dùng điền/sửa/gửi/nộp trên eTax; OPC giải thích cách điền và truy nguồn dữ liệu. OPC không được cam kết tự tính thuế, điền số vào bản nháp hoặc gửi/nộp thay người dùng trong phạm vi hiện tại.
- Chủ hộ chọn quý/năm; OPC tổng hợp riêng hóa đơn bán ra và mua vào theo ngày lập hóa đơn, cho xổ danh sách theo tháng/ngày và mở chi tiết. Happy path mọi giao dịch mua/bán có hóa đơn. Tiền thực thu/chi theo dõi riêng; không lấy thu trừ chi làm doanh thu hoặc mặc định mua vào được khấu trừ thuế.
- Hóa đơn điện tử qua provider; chứng từ viết tay chụp ảnh và nhập thông tin thủ công, OCR làm sau. Ảnh không tự chứng minh giá trị pháp lý của chứng từ.
- Dữ liệu chuẩn bị kê khai quý được sửa có lịch sử; sửa sau xác nhận phải báo cần kiểm tra lại, không sửa trực tiếp hóa đơn đã phát hành hoặc kết quả eTax cũ. Tiến trình OPC: chuẩn bị → kiểm tra → thực hiện trên eTax → đã gửi → chờ cập nhật kết quả.
- Nếu không có API eTax, chủ hộ tự cập nhật và đính kèm bằng chứng, ghi rõ chưa đối chiếu qua eTax. API, trạng thái sau gửi và điều kiện hoàn thành nghĩa vụ còn cần xác minh; không tự coi đã gửi là đã chấp nhận/đã nộp tiền.
- Purchase, Expense, Books and Reconciliation, Tax Guidance and Period Tracking cung cấp chuỗi dữ liệu và trợ giúp cần thiết.
- Sản phẩm dùng responsive Web trên máy tính, tablet và điện thoại. Chưa làm codebase native riêng cho Android và iOS.
- Chủ hộ có thể tự thao tác mọi khâu trong OPC theo quyền; Agent hỗ trợ trên cùng dữ liệu. Đơn Agent tạo phải được chủ hộ duyệt trước xác nhận/giữ hàng.
- Đơn bán tự tạo được chủ hộ xác nhận, không duyệt thêm lần nữa. Agent không tự gửi Zalo; chủ hộ trao đổi với khách. Không làm giảm giá hoặc kiểm tra/chặn theo hạn mức, nợ quá hạn trong luồng hiện tại.
- Lượng đơn bán được xác nhận không vượt tồn khả dụng; giữ đủ hàng, không giữ/giao một phần hoặc xác nhận đơn chờ nhập thêm. Chủ hộ giao đủ và bấm “Đã giao”, lượng lấy theo đơn, trừ kho một lần và kích hoạt hóa đơn.
- Có tiền thực nhận gắn với đơn → OPC đề xuất đóng → chủ hộ xác nhận. Giao hàng, hóa đơn hoặc tiền dư không chặn đóng và cũng không tự hoàn tất theo việc đóng đơn. Đơn đóng trước giao vẫn cho xử lý giao/hóa đơn còn chờ.
- OPC được trình bày là sản phẩm đang được kiểm chứng qua pilot, chưa được gọi là sản phẩm thương mại hoàn chỉnh.
- OPC sở hữu toàn bộ product capability trong phạm vi đã chốt. Việc tự xây hay sử dụng Casso hoặc third party là quyết định triển khai, được đánh giá ở bước Dependency Mapping sau khi Feature Catalogue được chốt.
- MVP đi kèm service package gồm khảo sát readiness, cấu hình, nhập dữ liệu ban đầu, đào tạo, hỗ trợ giao dịch đầu tiên, đồng hành kỳ thuế đầu tiên, helpdesk và kiểm tra adoption sau 30 và 90 ngày.

### 9.3 Phạm vi cần đánh giá tiếp

- Kết nối ngân hàng và nhận tiền.
- Hóa đơn bán ra và dữ liệu hóa đơn đầu vào.
- Mẫu sổ và quy tắc thuế cho pilot. PO đã chọn mẫu 01_CNKD_TT40_2026_9172.xlsx; kế toán còn xác minh áp dụng, GTGT/TNCN. Mapping trường tờ khai để sau theo yêu cầu PO.
- Provider nhận giao dịch ngân hàng/hóa đơn và khả năng lấy kết quả/lịch sử từ eTax. Tích hợp ngân hàng thật là mục tiêu đã chốt, chưa phải năng lực đã kiểm chứng.
- Định danh, đồng ý chia sẻ dữ liệu, bảo mật, vận hành và chi phí.
- Mức offline và đồng bộ lại cần hỗ trợ trên responsive Web.
- Tiêu chí của chương trình đối với responsive Web thay cho native app.

Các module trên thuộc MVP end-to-end, nhưng được build và kiểm chứng theo từng vertical slice. Không build đồng thời tất cả module.

### 9.4 Thứ tự phân tích và build MVP

Thứ tự này thống nhất với mục 8 của [OPC Feature Catalog](OPC_FEATURE_CATALOG.md).

| Thứ tự | Slice | Nội dung |
|---:|---|---|
| 1 | Slice 0 – Static onboarding demo | Trình bày hành trình thiết lập, kết nối và readiness bằng dữ liệu mô phỏng. |
| 2 | Slice 1 – Foundation | Hồ sơ, người dùng, dữ liệu nền, quyền, audit và tồn đầu kỳ. |
| 3 | Slice 2 – Source-to-Stock | Đơn mua, chủ hộ xác nhận thực nhận, nhập vào một kho và lưu chứng từ/chi phí. |
| 4 | Slice 3 – Order-to-Cash | Agent đề xuất → chủ hộ duyệt, hoặc tạo tay → xác nhận; kiểm tra giá/tồn, giữ đủ, giao đủ, hóa đơn, tiền thực nhận và chủ hộ xác nhận đóng. |
| 5 | Slice 4 – Record-to-Tax | Tổng hóa đơn bán/mua theo quý, truy từng hóa đơn, kiểm tra/sửa có lịch sử; hướng dẫn eTax và theo dõi đã gửi/chờ kết quả có bằng chứng. Quy tắc tính thuế cần xác minh. |
| 6 | Slice 5 – Pilot operations | Connector thật, dashboard chương trình, service package và đo adoption. |

Mỗi slice dùng chung dữ liệu, quyền, audit và trạng thái. Control Tower và cơ chế tích hợp hỗ trợ từng slice; Slice 5 hoàn thiện việc vận hành pilot. Các dependency cần được xác minh trước khi thực hiện hành động thật tương ứng.

Hoàn thành một slice chưa đồng nghĩa hoàn thành MVP. MVP chỉ hoàn tất khi các luồng end-to-end đáp ứng phạm vi tại mục 9.2.

### 9.5 Giới hạn proposal và nhánh mở rộng

| Nội dung | Quyết định PO | Cách thể hiện trong proposal |
|---|---|---|
| Một kho; mọi nhập mua có đơn và chủ hộ xác nhận | Đã chốt | Luồng chính. |
| Nhận mua nhiều lần trên cùng đơn | Cho phép theo dõi, trường hợp hiếm | Không đưa vào proposal; vẫn giữ ở phân tích chi tiết. |
| Trả đủ tiền mua một lần trước hoặc sau nhận hàng | Đã chốt | Luồng chính; ứng trước một phần/mua chịu/trả nhiều lần làm sau. |
| Giao trực tiếp; bấm “Đã giao” đủ theo đơn | Trọng tâm giai đoạn đầu | Luồng chính; không nhập lại lượng giao. |
| Tích hợp vận chuyển | Nice to have | “Tiếp tục phát triển”; không cam kết đã kết nối. |
| Giao một phần hoặc đơn xác nhận chờ nhập thêm | Không thuộc luồng hiện tại | Sửa lượng trong tồn trước xác nhận, hoặc nhập thêm rồi mới xác nhận. |
| Một hóa đơn theo đơn khi chủ hộ xác nhận giao đủ | Quyết định product đã có | Kế toán/provider xác minh thực thi trước chạy thật; thay thế quy tắc giao thiếu cũ. |
| Trả nhiều lần cho một đơn bán | Hiếm, chưa xét trong proposal hiện tại | Không hứa hỗ trợ hành trình thu nhiều lần; vẫn ghi đúng tiền thực về. |
| Hủy sau có hóa đơn | Làm thủ công, có biên bản theo yêu cầu PO | “Đang phát triển”; kế toán xác nhận chứng từ và cách xử lý. |
| Tiền dư | Ghi đúng giao dịch và ghi chú giải trình; chủ hộ tự xử lý | Có thể giải thích nguyên tắc; chưa hứa tự hoàn hoặc tự giữ cho lần mua sau. |

Ví dụ đã chốt: hóa đơn 8.000đ, tiền vào 10.000đ. OPC lưu hóa đơn 8.000đ, giao dịch 10.000đ và ghi chú “chuyển dư 2.000đ”. Không sửa hóa đơn thành 10.000đ hoặc tự ghi phần dư là doanh thu.

## 10. Ngoài phạm vi hiện tại

- Xây một ERP đầy đủ cho mọi ngành.
- Toàn bộ chế biến/sản xuất, quản lý nguyên liệu theo mẻ, công thức, hao hụt, thành phẩm; HR, payroll, MRP hoặc tài sản cố định.
- Tự thay thế kế toán, tư vấn pháp lý hoặc cơ quan có thẩm quyền.
- Để AI tự đoán tồn kho, tiền, thuế, giá hoặc trạng thái giao dịch.
- Tự ký, tự kê khai, tự nộp tiền hoặc tự chuyển tiền thay chủ hộ khi chưa có cơ sở và quyền phù hợp.
- Cam kết dùng Casso cho mọi connector trước khi hoàn tất đánh giá khả thi.
- Production rollout theo bất kỳ con số quy mô nào trước khi xác nhận đúng nhóm người dùng và kiểm chứng pilot, vận hành, chi phí.
- Build đồng thời mọi module. Các module trong MVP được thực hiện theo từng vertical slice và tích hợp dần.

## 11. Nguyên tắc vận hành business

1. Dữ liệu nghiệp vụ chuẩn nằm trong OPC hoặc hệ thống nguồn đã được xác định.
2. Tiền, thuế, tồn kho, giá và trạng thái dùng logic xác định.
3. AI hiểu dữ liệu không cấu trúc, lập phương án và giải thích ngoại lệ.
4. Con người quyết định các hành động có rủi ro, pháp lý hoặc ảnh hưởng tài chính lớn.
5. Mọi hành động phải có nguồn, thời gian, actor và bằng chứng.
6. Connector lỗi không được làm nghiệp vụ tự chuyển sang hoàn thành.
7. Hành động gửi lại phải chống tạo giao dịch hoặc chứng từ trùng.
8. Bên thứ ba là dependency, không phải nơi sở hữu quy trình OPC.
9. OPC sở hữu toàn bộ capability đã chốt; quyết định build, buy hoặc integrate được thực hiện sau khi xác định Feature.
10. Dùng bên thứ ba không làm mất ownership của OPC đối với dữ liệu, trạng thái, lỗi, retry, fallback, audit và trải nghiệm end-to-end.
11. Đơn Agent tạo chờ chủ hộ duyệt; chưa duyệt thì chưa xác nhận và chưa giữ hàng.
12. Hủy trước bàn giao thì dừng xử lý và giải phóng hàng đã giữ; chỉ trừ tồn thực tế theo số bàn giao được xác nhận.
13. Giao đủ là hoàn thành giao hàng, không chứng minh đã nhận đủ tiền hoặc hóa đơn đã hợp lệ. Theo dõi ba phần riêng.
14. Người mua báo hủy; chủ hộ thao tác trên OPC. Chưa chốt cổng/tài khoản người mua.
15. Tiền thực nhận, hóa đơn và chênh lệch là số riêng; lưu ghi chú, actor và nguồn để giải trình. QR đúng tiền không thay chứng cứ tiền thực nhận.
16. Đóng đơn bán theo tiền thực nhận gắn đơn và chủ hộ xác nhận, không dùng giao/hóa đơn/tiền dư làm điều kiện chặn; vẫn theo dõi các việc chưa xong.
17. Chủ hộ tự thiết lập đơn vị/quy cách; không mặc định tự quy đổi thùng–chai. Thiếu tồn phải giải quyết trước xác nhận, không dùng phê duyệt để vượt tồn.

## 12. Vai trò và trách nhiệm

| Vai trò | Trách nhiệm |
|---|---|
| PO Hiếu | Chốt product scope, ưu tiên, điểm dừng và tổng hợp quyết định. |
| PM Quang | Xác nhận mục tiêu proposal, nhóm người dùng và mức cam kết business. |
| Kế toán | Xác nhận quy tắc doanh thu, chi phí, sổ sách, hóa đơn và thuế. |
| Casso hoặc bên thứ ba | Xác nhận khả năng kỹ thuật, giới hạn, vận hành và giá. |
| DEV và kiến trúc | Đánh giá cách xây, dữ liệu, bảo mật, khả năng phục hồi và thời gian. |
| UX | Kiểm tra trải nghiệm mobile first, onboarding, ngoại lệ và khả năng hiểu trạng thái. |
| QA | Xác nhận happy path, ngoại lệ, chống trùng, phân quyền và audit. |

## 13. Dependency

- Nghiệp vụ và ví dụ chuẩn từ kế toán.
- Tài liệu API, sandbox, điều kiện chạy thật và báo giá từ Casso.
- Nguồn dữ liệu sản phẩm, khách hàng, đơn hàng, tiền, hóa đơn và chi phí.
- Tờ khai/mẫu sổ từ PO và kế toán; nguồn được xác minh để nhận kết quả hoặc bằng chứng kỳ eTax.
- Chính sách bảo mật, quyền truy cập, lưu trữ và xóa dữ liệu.
- Mô hình tenant và vai trò cho quy mô triển khai thực tế.
- Kế hoạch pilot và hỗ trợ vận hành ban đầu.

## 14. Giả định cần xác nhận

- Số 3.000 trong biên bản họp thuộc nhóm chuyển đổi hộ kinh doanh, không phải mặc định là quy mô người dùng OPC.
- Số 1.200 / 3.680 trong slide tỉnh là mục tiêu và nguồn của nhóm OPC, nhưng ý nghĩa chính xác cần PM xác nhận.
- Chủ hộ hoặc người kế nghiệp là người vận hành chính trên điện thoại.
- Sales Agent có thể làm vertical demo đại diện cho cách OPC hoạt động.
- Responsive Web đáp ứng được thao tác chính trên máy tính, tablet và điện thoại.
- Cách thao tác tay và trợ giúp Agent phù hợp thực tế pilot; đơn do Agent tạo luôn cần chủ hộ duyệt.
- Provider đáp ứng dữ liệu ngân hàng/hóa đơn mục tiêu; khả năng lấy kết quả eTax chưa được xác minh.
- Kế toán có thể cung cấp bộ quy tắc và ví dụ để kiểm thử.

## 15. Rủi ro business

| Rủi ro | Ảnh hưởng | Hướng xử lý |
|---|---|---|
| Product bị định nghĩa theo Casso | Khó thay provider và thiếu giá trị riêng | Chốt module và use case trước khi map connector. |
| Phạm vi thuế làm MVP quá lớn | Không thể hoàn thành nếu build đồng thời | Build theo thứ tự tại mục 9.4; kiểm chứng từng slice và dependency trước khi chuyển sang vận hành thật. |
| OPC chưa đáp ứng điều kiện sản phẩm thương mại ổn định | Không phù hợp nguyên tắc đặt hàng của tỉnh | Làm rõ vai trò OPC và bằng chứng sản phẩm trước khi đưa vào proposal. |
| Responsive Web không được chương trình chấp nhận thay cho native app | Phải đổi kiến trúc và tăng chi phí | Xác nhận tiêu chí nghiệm thu với PM, nhưng giữ responsive Web là product direction hiện tại. |
| Nghiệp vụ thuế chưa đủ rõ | Sai kết quả hoặc claim quá mức | Kế toán xác nhận và lưu nguồn theo ngày. |
| Người dùng không tin automation | Không sử dụng hoặc quay lại làm tay | Hiện nguồn, lý do, quyền dừng và phê duyệt. |
| Kết nối bên thứ ba không ổn định | Luồng business bị kẹt | Có trạng thái lỗi, retry, fallback và audit. |
| Chi phí tăng theo usage | Mô hình tài chính không phù hợp | Tính ba kịch bản và đo usage trong pilot. |
| Nhầm demo với production | Cam kết sai với stakeholder | Gắn nhãn demo và có readiness gate riêng. |

## 16. Quyết định business còn mở

| Nội dung cần chốt | Bên xác nhận | Ảnh hưởng |
|---|---|---|
| Hai nhóm 3.000 / 32.500 và 1.200 / 3.680 được hiểu như thế nào? | PM Quang | Kế hoạch production sau pilot. Không chặn MVP 5 đến 10 hộ. |
| Provider nào hỗ trợ ngân hàng thật, QR, giao dịch và hóa đơn cho pilot? | Provider; PO tổng hợp | Map chức năng, dữ liệu, giới hạn và chi phí; chưa cam kết provider. |
| Có API lịch sử/kết quả eTax không; trạng thái sau gửi và bằng chứng đủ cho từng bước là gì? | Provider và kế toán | Fallback chủ hộ cập nhật đã chốt; không hỏi lại. Điều kiện hoàn thành kỳ còn mở. |
| Mẫu đã chọn có áp dụng cho pilot không; quy tắc GTGT/TNCN, mẫu sổ và cách lấy giá trị hóa đơn là gì? | Kế toán; PO tổng hợp | Mẫu đã có; mapping trường chủ động để sau, không tính thuế từ suy đoán. |
| Phát hành hóa đơn khi xác nhận giao đủ cần dữ liệu/điều kiện gì; sửa/hủy cần hồ sơ nào? | Kế toán/provider | Kiểm chứng thực thi; không còn case giao thiếu. |
| Mức offline hoặc degraded mode cần hỗ trợ là gì? | PM Quang và DEV | Kiến trúc mobile và đồng bộ. |
| Chương trình có chấp nhận responsive Web thay cho native Android và iOS không? | PM Quang | Tiêu chí nghiệm thu, không thay đổi product direction hiện tại. |
| Danh sách pilot và khoảng doanh thu theo tháng cụ thể là gì? | PO và PM Quang | Nhóm Phân phối, cung cấp hàng hóa đã chốt; còn khảo sát quy mô thực tế. |

## 17. Điều kiện để BRD được chốt

BRD được xem là đủ để chuyển sang PRD chi tiết khi:

- Nhóm pilot là hộ kinh doanh nhỏ lẻ; ngành, danh sách và quy mô thực tế được PM xác nhận. Mốc 5–10 hộ là tham chiếu chương trình.
- Vòng đời business và module map được chấp thuận.
- Thứ tự build tại mục 9.4 được chấp thuận; Sales Agent thuộc Slice 3 – Order-to-Cash, không phải toàn bộ MVP.
- Ba luồng và ranh giới proposal tại mục 9.5 được chấp thuận; phần thuế hướng dẫn eTax và lưu kết quả theo nguồn được xác minh.
- Ownership của OPC đối với product capability và ranh giới quyết định giữa AI với con người được đồng ý.
- Service capability về triển khai, đào tạo và customer success được đồng ý.
- Các dependency về kế toán, Casso và pilot có owner và hạn xử lý.
- Không còn mâu thuẫn lớn giữa mục tiêu product và proposal Casso.

## 18. Tài liệu nguồn

- [OPC Business Capability Map](OPC_BUSINESS_CAPABILITY_MAP.md)
- [OPC Feature Catalog](OPC_FEATURE_CATALOG.md)
- [PRD OPC Sales Operations Agent](../02_OPC_Sales_Agent_Docs/01_PRD/PRD_OPC_SALES_AGENT.md)
- [Business and Agent Workflow](../02_OPC_Sales_Agent_Docs/02_Workflow/BUSINESS_AND_AGENT_WORKFLOW.md)
- [Onboarding Product Flow](../02_OPC_Sales_Agent_Docs/06_Onboarding/ONBOARDING_PRODUCT_FLOW.md)
- [Casso Feasibility Scope](../02_OPC_Sales_Agent_Docs/07_Casso_Feasibility/CASSO_FEASIBILITY_SCOPE.md)
- [Casso Requirements and Flow Matrix](../02_OPC_Sales_Agent_Docs/07_Casso_Feasibility/REQUIREMENTS_AND_FLOW_MATRIX.md)
- [Report Casso cho SoloMatrix](../Casso%20cho%20SoloMatrix/index.html)
- [Thư mời và Bài toán đặt hàng Kế nghiệp số Gia Lai](../01_B%C3%A0i%20to%C3%A1n/Thu_moi_va_Bai_toan_dat_hang_-_Ke_nghiep_so_Gia_Lai.docx)
- [Phát triển Kinh tế tư nhân tỉnh Gia Lai giai đoạn 2026-2030](../01_B%C3%A0i%20to%C3%A1n/KTTN%2010-08-2026%20H%E1%BB%99i%20DNT.pptx)
- Biên bản họp ngày 30/09/2026 do người dùng cung cấp.
- [Use Case Catalog v0.8](OPC_USE_CASE_CATALOG.md), mục 0 và UC-01/02/05/08/09–22/26–31: quyết định PO ngày 07/10/2026 là nguồn cập nhật mới nhất; thay phần tương ứng ngày 06/10. Không thay xác minh kế toán/provider.
- [Business Flow Explainer](OPC_BUSINESS_FLOW_EXPLAINER.md) và bản Word hiện tại tại `05_OPC_Presentation/OPC_BUSINESS_FLOWS_REVIEW.docx`.

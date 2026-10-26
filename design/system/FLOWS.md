# OPC — Bản đồ luồng nghiệp vụ (v1, 04/10/2026)

**Mục đích:** một bản duy nhất mô tả OPC vận hành thế nào, để design, BA và dev cùng nhìn một luồng. Mỗi bước ghi:
ai làm · OPC kiểm tra gì · trạng thái sau bước · dùng danh mục kết nối nào (số theo `SCOPE-MVP.md` §8) và **làm tay**
thế nào khi chưa kết nối · màn hình.
**Căn cứ:** BA (BRD 0.6, Capability Map 0.3, Feature Catalog 0.1, Key Use Cases 0.1), báo cáo Casso của CEO (mã
R-…/OPC-…/N-…), quyết định trong `SCOPE-MVP.md` §7–§8. Chỗ nào còn chờ trả lời ghi **[Câu 1]**, **[Câu 2]**.

**Các luồng:** ① Bán tại quầy · ② Đơn B2B từ mọi kênh · ③ Mua & nhận hàng · ④ Chế biến & kho · ⑤ Chốt kỳ & thuế ·
⓪ Onboarding & Readiness · Phụ lục: trạng thái chung, đối chiếu màn hình.

---

## 0. Nguyên tắc dùng chung cho mọi luồng

1. **Quầy là một đơn B2B làm gọn**: cùng khách, đơn, hàng & lô, tồn, tiền, hoá đơn, công nợ, sổ. Một danh sách đơn
   cho mọi kênh.
2. **Ba vai tách bạch** ở mọi bước (nhãn hiển thị cho người dùng):
   **Trợ lý đề xuất** (đọc dữ liệu không cấu trúc, soạn, giải thích) · **OPC kiểm tra** (quy tắc xác định: giá, tồn,
   công nợ, tiền, thuế, trạng thái) · **Chị duyệt / Người làm** (quyết định có rủi ro) · **Kết nối** (ngân hàng, hoá
   đơn, cổng thuế…; trong demo là **Mô phỏng**). Trợ lý không bao giờ tự đổi số liệu hay trạng thái cuối.
3. **Trừ kho đúng một lần, lúc bàn giao.** Giữ hàng (B2B) không trừ kho; bán chỉ được trên **tồn khả dụng** =
   tồn thực − đã giữ.
4. **Tiền có 3 trạng thái** ở mọi kênh: *Chờ khách chuyển* → *Đã nhận · chờ xác minh* (webhook ngân hàng chưa ký) →
   *Đã xác minh* (khớp sao kê hoặc chủ hộ xác nhận). Không bao giờ coi tiền là thật chỉ vì có thông báo.
5. **Không làm thay chủ hộ** (N-06, N-07): người bấm phát hành hoá đơn, chuyển tiền, gửi tờ khai, nộp thuế luôn là
   người trong hộ. OPC không giữ tiền, không chi hộ, không giữ mật khẩu eTax.
6. **Mọi kết nối có đường làm tay** — không luồng nào bị kẹt vì chưa có nhà cung cấp hoặc kết nối lỗi.
7. **Gửi lại không tạo trùng**: mọi bước tạo hoá đơn, giao dịch, tờ khai có khoá chống trùng; quá giờ chờ thì
   *Chưa rõ kết quả*, kiểm tra rồi mới làm tiếp, không tự gửi lại.
8. **Mất mạng vẫn bán được** tại quầy; việc cần mạng thì xếp hàng chờ và nói rõ lý do.
9. **Mọi hành động có dấu vết**: ai, lúc nào, nguồn, trước/sau, lý do — nhật ký chỉ ghi thêm.

### 0.1 Dữ liệu demo (từ bộ của BA, design bổ sung)

| Loại | Giá trị |
|---|---|
| Hộ | **Đặc sản Cao Nguyên An Nhiên** · MST 5901234567 · Pleiku, Gia Lai · doanh thu 2026 lũy kế 1.284.500.000 ₫ (đã vượt 1 tỷ) |
| Người | **Chị Phạm Thị An** — chủ hộ · **Anh Nguyễn Minh Khoa** (con, 29) — người vận hành · **Hạnh** — thu ngân · **Anh Hùng** — người giao (chỉ dùng link) · **Chị Lan** — kế toán dịch vụ (uỷ quyền có hạn) |
| Kho | Kho chính Gia Lai (một kho) |
| Nhà cung cấp | **HTX Cao Nguyên** — thịt bò tươi, muối kiến vàng đóng hũ · công nợ 30 ngày |
| Khách B2B | **Sunrise Hotel** (MST 5900987654) · người đặt: chị Mai, bộ phận bếp · giá riêng khách sạn · hạn mức 15.000.000 ₫ · thanh toán 15 ngày · đang nợ 8.400.000 ₫, **quá hạn 12 ngày** |
| Khách khác | Nhà hàng Phố Núi (B2B, trả theo đơn) · khách lẻ tại quầy |
| Sản phẩm 1 | **Bò một nắng 500g** — tự chế biến, quản lý lô, hạn dùng 60 ngày · giá lẻ 260.000 ₫ · giá khách sạn 230.000 ₫ · tồn 46 gói (lô BMN-0405: 26 gói, lô BMN-0410: 20 gói) |
| Sản phẩm 2 | **Muối kiến vàng 100g** — mua về bán lại từ HTX · giá lẻ 65.000 ₫ · giá khách sạn 55.000 ₫ · tồn 80 hũ |
| Nguyên liệu | Thịt bò tươi (kg) · gia vị ướp (gói) |
| Kênh | Zalo OA "Đặc sản An Nhiên" · thêm thủ công · Quầy |
| Kết nối | Ngân hàng MB (tài khoản tổ chức mang tên hộ) · hoá đơn: Hilo (quầy), X Invoice (B2B) · trong demo mọi kết nối là **Mô phỏng** |
| Kỳ thuế | **Đang đối chiếu: Quý III/2026** (07–09) · hạn khai 31/10/2026 · doanh thu kỳ 338.400.000 ₫ (design bổ sung, vì "hôm nay" của demo là 06/10/2026) · **Đang thu dữ liệu: Quý IV/2026** · hạn khai 31/01/2027 (Chủ nhật — hạn thực tế theo quy tắc lùi sang ngày làm việc, kế toán xác nhận) |
| Số chứng từ | Hoá đơn quầy (Hilo, máy tính tiền) dãy 0000xxxx riêng; hoá đơn B2B (X Invoice) dãy 00000187, 00000193 (Sunrise, 09–10/09), 00000199 (Phố Núi DH-2031, 25/09), 00000201 (Homestay DH-2036, 28/09) |
| Đơn mẫu B2B | Sunrise: 20 gói bò × 230.000 = 4.600.000 ₫ · 30 hũ muối × 55.000 = 1.650.000 ₫ · **6.250.000 ₫** · giao trước 15:00 ngày mai · xuất hoá đơn |
| Đơn mẫu quầy | Khách lẻ: 2 gói bò × 260.000 + 3 hũ muối × 65.000 = **715.000 ₫** · QR |

---

## ① Bán tại quầy

**Mục tiêu:** bán nhanh cho khách đứng trước mặt, tiền và hoá đơn đúng, không bán vào hàng đã giữ cho đơn khác.
**Bắt đầu:** người bán mở Quầy. **Kết thúc:** đơn *Đã đóng* (tiền đã xác minh) hoặc *Đã giao · chờ xác minh tiền*.

| # | Bước | Ai | OPC kiểm tra | Trạng thái sau | Kết nối · làm tay | Màn hình |
|---:|---|---|---|---|---|---|
| 1 | Chọn món, số lượng (cân kg nếu có) | Người bán | Chỉ bán trên **tồn khả dụng**; hiện "còn 26 · đã giữ 20" | Đơn *Đang bán* | — | Quầy (`counter`) |
| 2 | (Tuỳ chọn) chọn khách quen | Người bán | Có hồ sơ → dùng **giá riêng** và **hạn mức công nợ** của khách | — | — | Quầy · chọn khách |
| 3 | Chọn cách trả: QR · tiền mặt · ghi nợ | Người bán | Ghi nợ: chỉ khách có hồ sơ, trong hạn mức, không nợ quá hạn → nếu vi phạm: **chờ duyệt** | — | — | Quầy · `c-seg` |
| 4a | QR: hiện mã theo đơn | OPC | Mã đơn gắn vào QR | Tiền *Chờ khách chuyển* | #2 Thu tiền · **làm tay:** QR tĩnh của hộ, khớp tay | `counter--qr` |
| 4b | Tiền mặt: nhập khách đưa | Người bán | Tính tiền thối | Tiền *Đã xác minh* (tiền mặt) | — | `counter--cash` |
| 5 | Ngân hàng báo tiền về | Kết nối | Khớp theo mã đơn; đủ / thiếu / thừa | Tiền *Đã nhận · chờ xác minh* | #1 Ngân hàng · **làm tay:** người bán xác nhận đã thấy tiền trong app ngân hàng | `counter--received` |
| 6 | Bấm **Thu tiền** = bàn giao | Người bán | Tiền chờ xác minh: chỉ giao nếu đơn **dưới ngưỡng chủ hộ đặt** (mặc định 2.000.000 ₫); trên ngưỡng → chờ xác minh hoặc chủ hộ xác nhận | **Trừ kho** (tự chọn lô gần hết hạn trước) · đơn *Đã giao* | — | Quầy |
| 7 | Hoá đơn máy tính tiền tự phát hành | OPC, theo lần bấm của người bán (quyền "phát hành tại quầy") | Tổng hoá đơn = tổng đơn; ghi người bấm | Hoá đơn *Có mã CQT* (Hilo cấp ngay) | #4 Hoá đơn · **làm tay:** lập trên cổng nhà cung cấp, ghi nhận lại | `counter--verified`, phiếu (`receipt`) |
| 8 | Tiền được xác minh | OPC | Khớp sao kê hoặc chủ hộ xác nhận | Đơn *Đã đóng* | #1 | Tiền & đối chiếu |
| 9 | Đóng ca | Người bán | Đếm tiền mặt, chênh lệch phải có lý do; QR chưa xác minh liệt kê riêng | Ca *Đã đóng* | — | Đóng ca (mới) |

**Ngoại lệ**
- **Bán vào hàng đã giữ** (ví dụ chỉ còn hàng đã giữ cho Sunrise): người bán thấy cảnh báo; chủ hộ/quản lý tại chỗ
  duyệt (mã PIN) hoặc vào Cần xử lý. Duyệt xong, đơn Sunrise bị đánh dấu "thiếu hàng" để xử lý.
- **Tiền thiếu/thừa:** thiếu → QR bổ sung; thừa → OPC soạn lệnh hoàn, chủ hộ tự chuyển qua app ngân hàng (#3).
- **Khách đổi sang tiền mặt** khi đang chờ QR: huỷ QR, chuyển bước 4b.
- **Không có mạng:** bán tiền mặt và QR tĩnh; đơn và hoá đơn **xếp hàng trên máy**, đồng bộ khi có mạng; hiện
  "Chờ đồng bộ n đơn". Không xác minh QR được khi mất mạng → đơn trên ngưỡng không giao trước.
- **Hoá đơn không phát hành được / quá giờ chờ:** đơn vẫn xong; hoá đơn *Chưa rõ kết quả* → vào Cần xử lý → Lỗi;
  không tự gửi lại.
- **Hộ đặt quyền phát hành tắt cho một thu ngân:** hoá đơn của người đó chờ chủ hộ/quản lý trong Cần xử lý.
- **Trả hàng tại quầy:** từ đơn đã đóng → nhập lại kho nếu đạt, hoàn tiền (chủ hộ tự chuyển), hoá đơn điều chỉnh
  qua cổng nhà cung cấp rồi ghi nhận [luồng trả hàng chi tiết ở bản sau].

**Nhất quán với luồng ②:** cùng giá riêng và hạn mức của khách; cùng quy tắc "giao trước khi tiền được xác minh"
(khách lẻ = ngưỡng chủ hộ; khách B2B = hạn mức công nợ); cùng cách chọn lô; cùng Cần xử lý.

---

## ② Đơn B2B từ mọi kênh (Order-to-Cash)

**Mục tiêu:** biến một yêu cầu không cấu trúc thành đơn hợp lệ, giao đúng, xuất hoá đơn, thu đủ tiền rồi đóng.
**Bắt đầu:** có yêu cầu mới. **Kết thúc:** đơn *Đã đóng* (phải thu đã đóng bằng tiền đã xác minh).

### ②a Nhận yêu cầu và tạo đơn hợp lệ (UC-03)

| # | Bước | Ai | OPC kiểm tra | Trạng thái sau | Kết nối · làm tay | Màn hình |
|---:|---|---|---|---|---|---|
| 1 | Yêu cầu đến: tin Zalo OA, hoặc **thêm thủ công** (dán/chia sẻ tin nhắn từ app khác, ảnh đơn viết tay, PDF đơn đặt hàng, ghi âm cuộc gọi, tự gõ), hoặc đơn định kỳ đến hạn | Khách / người trong hộ | Ghi nguồn, giờ nhận | Yêu cầu *Mới* | #11 Kênh trò chuyện (Zalo OA) · **làm tay:** thêm thủ công | Hộp yêu cầu (mới) |
| 2 | Đọc yêu cầu | **Trợ lý đề xuất** | — | Bản hiểu: khách, món, số lượng, ngày giờ giao, có xuất hoá đơn không, **điều còn thiếu**, độ tin cậy, bằng chứng (trích tin gốc) | #15 AI | Hộp yêu cầu · chi tiết |
| 3 | Đối chiếu dữ liệu chuẩn | **OPC kiểm tra** | Khách có hồ sơ? Món khớp SKU? Đơn vị quy đổi đúng? | Đã khớp / cần làm rõ | — | như trên |
| 4 | Làm rõ nếu thiếu (ví dụ "giao ở cổng nào?") | Trợ lý soạn câu hỏi · người trong hộ bấm gửi | Không tạo đơn khi còn thiếu thông tin bắt buộc | *Chờ khách trả lời* | #11 · **làm tay:** gọi điện, ghi lại | như trên |
| 5 | Chạy kiểm tra đơn | **OPC kiểm tra** | **Giá** (bảng giá riêng; giảm giá vượt quyền?) · **Tồn khả dụng** · **Công nợ** (hạn mức, nợ quá hạn) · ngày giao khả thi | Từng quy tắc: đạt / không đạt | — | Order 360 · kết quả kiểm tra |
| 6a | Tất cả đạt → tạo đơn và **giữ hàng** | OPC | Giữ trong một giao dịch; đơn nháp giữ 24 giờ | Đơn *Nháp · đã giữ hàng* · giữ hàng *Đang giữ* | — | Order 360 |
| 6b | Có quy tắc không đạt → **chờ duyệt** | OPC | Chưa giữ hàng, chưa báo khách | Đơn *Chờ duyệt* | — | **Cần xử lý → Cần chị quyết** → chi tiết duyệt |
| 7 | Duyệt (có lý do bắt buộc) hoặc từ chối | **Chị duyệt** (người có quyền theo ngưỡng) | Sau khi duyệt, **kiểm tra lại** tồn, công nợ, phiên bản đơn | Quay lại 6a, hoặc *Đã huỷ* | — | Chi tiết duyệt |
| 8 | Gửi xác nhận cho khách | Trợ lý soạn · người trong hộ bấm gửi | Không đổi giá/số lượng so với đơn đã kiểm tra | Đơn *Đã xác nhận* · giữ hàng tới ngày giao | #11 · **làm tay:** gọi điện hoặc nhắn tay, đánh dấu đã báo | Order 360 |

### ②b Soạn, giao, hoá đơn, thu tiền, đóng (UC-04)

| # | Bước | Ai | OPC kiểm tra | Trạng thái sau | Kết nối · làm tay | Màn hình |
|---:|---|---|---|---|---|---|
| 9 | Danh sách soạn hàng | OPC | Đề xuất lô (gần hết hạn trước) | Giao hàng *Chờ soạn* | — | Soạn & giao (mới) |
| 10 | Xác nhận đã soạn (số lượng, lô thực tế) | Người trong hộ | So với hàng đã giữ; **chưa trừ kho** | *Đã soạn* | — | Soạn & giao |
| 11 | Chọn **cách giao** (mặc định theo khách): khách tự lấy · nhân viên của hộ · gửi nhà xe · đơn vị vận chuyển không kết nối · có kết nối | Người trong hộ | Có thu hộ (COD) không, ai thu | — | #13 Giao hàng · **làm tay:** 4 cách không kết nối | Soạn & giao |
| 12 | **Bàn giao** cho người giao | Người trong hộ | **Trừ kho đúng một lần**, dùng hết phần đã giữ | *Đã bàn giao* → *Đang giao* | #13 (tạo vận đơn) · **làm tay:** ghi người nhận bàn giao | Soạn & giao |
| 13 | Kết quả giao: đã giao / một phần / thất bại | Người giao (link, ảnh, tên người nhận) · nhà xe (ảnh phiếu) · đơn vị vận chuyển (tự động) | Thứ tự sự kiện hợp lệ; giao một phần → phần còn lại thành đơn chờ hoặc huỷ (chủ hộ chọn) | *Đã giao* / *Giao một phần* / *Thất bại* | #13 · **làm tay:** chủ hộ nhập kết quả | Soạn & giao · link cho người giao (mới) |
| 14 | **Đề xuất hoá đơn** theo **số đã giao** | OPC | Dữ liệu từ giao dịch đã giao; mẫu số 2; người mua theo hồ sơ khách | Hoá đơn *Nháp chờ duyệt* | — | Order 360 · hoá đơn |
| 15 | **Phát hành** | **Chị duyệt** (bấm phát hành) | Chống trùng; cần chữ ký số của hộ **[Câu 2]** | *Chờ mã CQT* → *Có mã CQT* / *Bị từ chối* / *Chưa rõ kết quả* | #4 Hoá đơn, #8 Chữ ký số · **làm tay:** lập trên cổng nhà cung cấp, ghi nhận | `invoice-detail` |
| 16 | Tạo **khoản phải thu** | OPC | Số tiền, hạn thanh toán theo điều khoản khách (15 ngày) | Phải thu *Đang mở* | — | Công nợ (mới) |
| 17 | Gửi hoá đơn + thông tin trả tiền (QR theo hoá đơn) | Trợ lý soạn · người trong hộ gửi | — | — | #11, #2 · **làm tay:** gửi file | Order 360 |
| 18 | Tiền về (một khoản có thể trả **nhiều hoá đơn** — bảng kê) | Kết nối | Chống trùng; khớp theo mã, rồi số tiền + tên; **không đoán** khi nhiều ứng viên | Tiền *Đã nhận · chờ xác minh* | #1 · **làm tay:** chủ hộ gán | Tiền & đối chiếu · gán tiền (sửa: gán nhiều hoá đơn) |
| 19 | Phân bổ và xác minh | OPC (+ chủ hộ khi cần) | Đủ → đóng phải thu; thiếu → còn lại *Trả một phần*; thừa → chờ quyết (giữ làm trả trước / hoàn) | Phải thu *Đã đóng* · tiền *Đã xác minh* | #1 | như trên |
| 20 | **Đóng đơn** | OPC | Đã giao + hoá đơn có mã + phải thu đã đóng | Đơn *Đã đóng* | — | Order 360 |

**Ngoại lệ (đều chọn được trong Scenario Switcher của demo)**
- **Khách nợ quá hạn / vượt hạn mức** → bước 6b, duyệt có lý do, kiểm tra lại (`approvals.html` + 3 trạng thái).
- **Thiếu hàng** → đề xuất: giao một phần, hẹn ngày, đổi món, hoặc tạo lệnh chế biến (luồng ④); chủ hộ chọn.
- **Hoá đơn bị từ chối** → lý do của nhà cung cấp (nếu có) → sửa dữ liệu → phát hành lại; không sửa được qua API
  thì hướng dẫn trên cổng nhà cung cấp rồi ghi nhận.
- **Tiền không khớp** (thiếu mã, thiếu tiền, một khoản cho nhiều đơn) → Tiền & đối chiếu → gán tay có kiểm tra.
- **Kết nối quá giờ** (hoá đơn, giao hàng) → *Chờ kết nối*, OPC hỏi lại theo lịch; quá lâu → *Lỗi*, đề xuất làm tay.
- **Khách đổi đơn sau khi xác nhận** → đơn mới phiên bản 2 → kiểm tra lại từ bước 5; giữ hàng cập nhật.
- **Giao thất bại** → giao lại (lần 2) hoặc hoàn về kho (nhập lại khi đạt kiểm tra).
- **Thu hộ (COD):** nhân viên thu → nộp lại và đối chiếu như đóng ca; đơn vị vận chuyển thu → phải thu từ đơn vị đó,
  đối chiếu khi họ chuyển trả.
- **Mất mạng:** tạo được yêu cầu và đơn nháp; xác nhận đơn và giữ hàng cần mạng (phải kiểm tra lại tồn và công nợ).

**Nhất quán với luồng ①:** trừ kho lúc bàn giao (quầy = lúc bấm Thu tiền); cùng ba trạng thái tiền; cùng Cần xử lý;
cùng danh sách đơn (nguồn: Quầy / Zalo OA / thủ công / định kỳ).
**Khác luồng ①, có chủ đích:** hoá đơn B2B do chủ hộ bấm phát hành sau khi giao (OPC-09); quầy phát hành ngay lúc
bán (hoá đơn máy tính tiền, Câu 3 đã chốt).

---

## ③ Mua hàng & nhận hàng (Procure-to-Pay, UC-02 nhánh A)

**Mục tiêu:** có hàng để bán, chi phí và công nợ nhà cung cấp đúng, chứng từ đầu vào gắn với giao dịch.
**Bắt đầu:** cần mua (tồn thấp, hoặc người trong hộ tạo). **Kết thúc:** phải trả *Đã đóng* bằng lần chuyển tiền
chủ hộ tự bấm.

| # | Bước | Ai | OPC kiểm tra | Trạng thái sau | Kết nối · làm tay | Màn hình |
|---:|---|---|---|---|---|---|
| 1 | Nhu cầu mua: OPC gợi ý khi tồn dưới mức tối thiểu, hoặc người trong hộ tạo | OPC / người trong hộ | Mức tồn tối thiểu, hàng đang về | Nhu cầu *Mới* | — | Hàng hoá · tồn kho (mới) |
| 2 | Lập **đơn mua**: nhà cung cấp, món, số lượng, giá, ngày nhận | Người trong hộ (Trợ lý có thể soạn từ tin nhắn/ảnh báo giá) | Giá so với lần mua trước (lệch nhiều → nhắc) | Đơn mua *Nháp* | #11 (gửi NCC) · **làm tay:** gọi điện | Đơn mua (mới) |
| 3 | Xác nhận đơn mua (gửi cho NCC) | Chủ hộ / quản lý | Ngưỡng duyệt chi | *Đã xác nhận* | — | Đơn mua |
| 4 | **Nhận hàng**: đếm số thực nhận (kg, hũ), chất lượng | Người trong hộ | So với số đặt: đủ / thiếu / thừa / hỏng | Phiếu nhận *Nháp* | — | Nhận hàng (mới) |
| 5 | Chênh lệch → quyết định | **Chị duyệt** | Thiếu: nhận phần có, phần còn lại chờ hoặc huỷ · hỏng: trả NCC | — | — | Cần xử lý → chi tiết duyệt |
| 6 | Xác nhận nhận hàng | Người trong hộ | **Nhập kho đúng một lần** (theo lô nếu là nguyên liệu cần truy xuất) · tạo **phải trả** | Tồn tăng · phải trả *Đang mở* | — | Nhận hàng |
| 7 | Gắn **chứng từ đầu vào**: hoá đơn của NCC (từ cổng thuế hoặc ảnh/PDF), hoặc **bảng kê mua hàng** khi NCC không có hoá đơn | Trợ lý đọc ảnh/PDF · OPC khớp | Khớp với đơn mua và phiếu nhận (số lượng, giá, MST NCC) | Chứng từ *Đã khớp* / *Lệch* | #5 Cổng thuế (tuỳ chọn theo hộ) · **làm tay:** chụp ảnh | Nhận hàng · chứng từ |
| 8 | Đến hạn trả NCC → OPC soạn đề nghị chuyển tiền | OPC | Số tiền = phải trả còn lại | Đề nghị *Chờ chị chuyển* | — | Công nợ phải trả (mới) |
| 9 | **Chủ hộ tự chuyển** qua app ngân hàng (mở sẵn số TK, số tiền, nội dung) | **Chủ hộ** | — | — | #3 Chi tiền (deeplink) · **làm tay:** chép thông tin | như trên |
| 10 | Ngân hàng báo tiền ra → khớp | OPC | Khớp số tiền + nội dung; không khớp → chờ chủ hộ gán | Phải trả *Đã đóng* | #1 · **làm tay:** chủ hộ đánh dấu đã trả kèm ảnh biên lai | Tiền & đối chiếu |

**Chi phí không qua kho** (điện, xăng, bao bì nhỏ, thuê mặt bằng): chụp hoá đơn/biên lai → Trợ lý đọc → chủ hộ xác
nhận nhóm chi phí → ghi sổ; trả ngay hoặc thành phải trả. Cùng màn chứng từ, không cần đơn mua.

**Ngoại lệ:** NCC giao nhiều lần cho một đơn mua (nhận từng đợt) · NCC hộ nông dân không có hoá đơn → bảng kê thu
mua (căn cứ do kế toán xác nhận) · giá thực tế khác đơn mua → duyệt · trả hàng NCC → xuất kho trả, giảm phải trả.

**Nhất quán:** tồn tăng chỉ khi xác nhận nhận hàng (đối xứng với "trừ kho khi bàn giao"); chứng từ đầu vào dùng
cho sổ chi phí (luồng ⑤); tiền ra luôn do chủ hộ bấm.

---

## ④ Chế biến & kho (Produce-to-Stock, UC-02 nhánh B; tồn kho, lô, truy xuất)

**Mục tiêu:** tạo thành phẩm theo lô từ nguyên liệu, tồn luôn giải thích được, truy xuất được hai chiều.
**Bắt đầu:** cần thêm thành phẩm (tồn thấp, hoặc đơn B2B thiếu hàng). **Kết thúc:** lô thành phẩm nhập kho, truy
xuất được về nguyên liệu và tới khách đã nhận.

| # | Bước | Ai | OPC kiểm tra | Trạng thái sau | Kết nối · làm tay | Màn hình |
|---:|---|---|---|---|---|---|
| 1 | Lập **lệnh chế biến**: thành phẩm (40 gói bò một nắng), nguyên liệu dự kiến (OPC gợi ý theo lần trước: 34 kg thịt bò tươi, 2 gói gia vị) | Người trong hộ | Nguyên liệu khả dụng đủ? | Lệnh *Nháp* | — | Chế biến (mới) |
| 2 | Bắt đầu: **xuất nguyên liệu** (chọn lô nguyên liệu) | Người trong hộ | Không xuất quá tồn — **chặn, không tạo tồn âm** | Nguyên liệu trừ kho · lệnh *Đang làm* | — | Chế biến |
| 3 | Ghi **lượng thực dùng và hao hụt** | Người trong hộ | Hao hụt vượt mức thường (theo các lần trước) → nhắc, cần lý do | — | — | Chế biến |
| 4 | Xác nhận **sản lượng** | Người trong hộ | Tạo **lô thành phẩm** (BMN-0412), ngày chế biến, **hạn dùng** (60 ngày) | Lô *Mới* · thành phẩm nhập kho · lệnh *Xong* | — | Chế biến · lô |
| 5 | (Tuỳ chọn) in tem lô / mã QR truy xuất | Người trong hộ | Chỉ công khai khi chủ hộ bấm đăng (trang truy xuất là tuỳ chọn) | — | — | Lô · truy xuất |

**Tồn kho & lô (dùng chung cho mọi luồng)**
- Mỗi món có: **tồn thực · đã giữ · khả dụng**, theo lô nếu cần truy xuất. Sổ biến động kho ghi mọi nhập, xuất, giữ,
  nhả giữ, trả, điều chỉnh — ai, lúc nào, vì sao.
- **Chọn lô khi bán/soạn:** gần hết hạn trước, tự động; người trong hộ đổi được khi soạn B2B.
- **Truy xuất hai chiều:** từ lô thành phẩm → lô nguyên liệu → đơn mua/NCC; và từ lô → các đơn/khách đã nhận (khách
  lẻ tại quầy gộp thành "khách lẻ tại quầy, n gói").
- **Kiểm kê:** đếm thực tế → chênh lệch → **chủ hộ duyệt** có lý do → điều chỉnh tồn (không sửa tồn trực tiếp).
- **Hàng sắp hết hạn:** nhắc trước 7 ngày; đề xuất bán trước tại quầy.

**Ngoại lệ:** nguyên liệu không đủ → chặn bước 2, gợi ý lập đơn mua (luồng ③) · hao hụt bất thường → duyệt · lô có
vấn đề chất lượng → **khoá lô** (không bán, không giao), xem danh sách khách đã nhận để báo.

**Nhất quán:** một sổ kho cho mọi luồng; lô thành phẩm từ chế biến và hàng mua từ luồng ③ cùng vào một tồn; đơn
B2B thiếu hàng (②, ngoại lệ) có thể sinh lệnh chế biến; chế biến đơn giản — **không** định mức, không MRP.

---

## ⑤ Chốt kỳ & thuế (Record-to-Tax, UC-05)

**Mục tiêu:** dữ liệu kỳ đầy đủ và khớp, số thuế tính bằng quy tắc đã xác nhận, tờ khai được gửi, thuế được nộp,
bằng chứng được lưu, kỳ được đóng.
**Bắt đầu:** gần hạn kỳ (OPC nhắc trước 10 ngày, OPC-19). **Kết thúc:** kỳ *Đã đóng* (có mã tiếp nhận tờ khai và
mã biên nhận nộp tiền).

| # | Bước | Ai | OPC kiểm tra | Trạng thái sau | Kết nối · làm tay | Màn hình |
|---:|---|---|---|---|---|---|
| 1 | Sổ ghi liên tục từ mọi luồng: doanh thu (đơn đã giao + hoá đơn), chi phí (chứng từ đầu vào), tiền, công nợ | OPC | Mọi bút toán truy được về đơn / hoá đơn / giao dịch ngân hàng | Kỳ *Đang thu dữ liệu* | — | Sổ sách (mới) |
| 2 | **Readiness của kỳ**: thiếu gì, lệch gì | OPC | Đơn đã giao chưa có hoá đơn · hoá đơn chưa có mã · tiền chưa gán · chứng từ đầu vào thiếu · tồn chưa kiểm kê · doanh thu sàn đã bị khấu trừ thuế | Danh sách việc | #5 Cổng thuế (đối chiếu hoá đơn ra/vào) | Đối chiếu kỳ (mới) |
| 3 | Xử lý từng việc | Người trong hộ / kế toán | Lưu quyết định, chạy lại kiểm tra | Kỳ *Sẵn sàng tính* | — | Đối chiếu kỳ → mở từng việc |
| 4 | **Khoá kỳ** | Chủ hộ / kế toán | Sau khoá, sửa dữ liệu kỳ phải **mở lại kỳ** (duyệt, có lý do, có dấu vết) | Kỳ *Đã khoá* | — | Đối chiếu kỳ |
| 5 | **Tính thuế** | OPC | Bộ quy tắc có phiên bản, nguồn văn bản, ngày hiệu lực, người xác nhận; nhóm ngành (phân phối / sản xuất…) theo doanh thu; trừ phần sàn đã khấu trừ; ngưỡng 1 tỷ | Kết quả thuế (giải thích được từng dòng) | — | Thuế (mới) |
| 6 | **Tờ khai nháp** đúng mẫu | OPC | Dữ liệu đầu vào, công thức, chênh lệch so với kỳ trước | Tờ khai *Chờ kế toán xem* | — | Thuế · tờ khai |
| 7 | Kế toán xem (nếu hộ có uỷ quyền) | Kế toán | Ghi chú, yêu cầu sửa | *Chờ chủ hộ duyệt* | — | như trên |
| 8 | **Chủ hộ duyệt** (bước duyệt cứng, không tự chạy) | **Chủ hộ** | Cảnh báo: đây là số OPC tính, không phải tư vấn pháp lý | *Đã duyệt* | — | như trên |
| 9a | **Gửi tờ khai — có đối tác:** "Chị ký và gửi" (ký số từ xa, xác nhận OTP của chị) | **Chủ hộ** | Chống gửi trùng | *Đã gửi* → *Đã tiếp nhận* | #6 Gửi tờ khai, #8 Chữ ký số · **[Câu 1]** · trong demo: **Mô phỏng** | Thuế · nộp |
| 9b | **Gửi tờ khai — chưa có đối tác:** xuất file → "Mở eTax" + 4 bước hướng dẫn → chụp thông báo tiếp nhận | **Chủ hộ** | Trợ lý đọc ảnh, OPC kiểm tra mã số thuế, kỳ, số tiền khớp | *Đã tiếp nhận* | **làm tay** | Thuế · nộp |
| 10 | **Nộp tiền thuế:** mở eTax Mobile hoặc app ngân hàng (thông tin điền sẵn khi được) → chủ hộ tự nộp → chụp/nhập **mã biên nhận** | **Chủ hộ** | Số tiền khớp tờ khai; kỳ chỉ thành "đã nộp" khi có mã biên nhận (OPC-21) | *Đã nộp* | #7 Nộp thuế (deeplink) · **làm tay:** nhập mã biên nhận | Thuế · nộp |
| 11 | **Bằng chứng & đóng kỳ** | OPC | Lưu tờ khai, thông báo tiếp nhận, biên nhận nộp tiền, dấu vết duyệt | Kỳ *Đã đóng* | — | Thuế · bằng chứng |

**Ngoại lệ:** dữ liệu thiếu sát hạn → OPC nhắc theo mốc (10 ngày, 3 ngày, 1 ngày) và đề xuất gọi hỗ trợ · tờ khai bị
từ chối → lý do → sửa → gửi lại (khai bổ sung) · số tiền nộp lệch → không đóng kỳ, chờ quyết · vượt ngưỡng 1 tỷ
giữa kỳ → nhắc đăng ký hoá đơn điện tử trong 30 ngày (mẫu 01/ĐKTĐ-HĐĐT).

**Nhất quán:** kỳ chỉ đóng khi các luồng ①–④ đã sạch (mọi đơn có hoá đơn, mọi tiền đã gán, chứng từ đủ); tiền thuế
và tờ khai luôn do chủ hộ bấm; mọi số thuế trong demo có nhãn **Mô phỏng**.

---

## ⓪ Onboarding & Readiness (UC-01)

**Mục tiêu:** hộ thấy giá trị nhanh, rồi làm dần tới *Sẵn sàng* với hỗ trợ của OPC. **Kết thúc:** readiness *Sẵn sàng
có điều kiện* (giao dịch thật được, còn việc nên làm) hoặc *Sẵn sàng*.

### Phần A — Mở hộ (5 bước, khoảng 10 phút, ưu tiên điện thoại) · v6.0.0

> Khi mở hộ chưa nối gì của hộ: mã đăng nhập do tài khoản gửi tin của chính OPC gửi (Zalo rồi SMS), ảnh giấy đăng ký do AI của OPC đọc. Ngân hàng, hoá đơn, chữ ký số, mua hàng, chế biến, thuế là các **cổng đúng lúc** trong Sẵn sàng.
> Tra cứu cổng thuế cho hộ kinh doanh chưa được chứng minh: luồng không dựa vào nó (xem NOTES, 4 câu cần hỏi).

| # | Bước | Chị làm | OPC làm | Màn hình |
|---:|---|---|---|---|
| 1 | Số điện thoại | Nhập số, nhập mã 6 số | Gửi mã qua Zalo hoặc SMS bằng tài khoản của OPC; nhớ máy 90 ngày | `onboard-phone`, `onboard-otp` |
| 2 | Hộ kinh doanh | Chụp giấy đăng ký, hoặc nhập mã số thuế / số căn cước; kiểm tra; nhập doanh thu từ đầu năm và ngày bắt đầu | AI đọc ảnh; dòng chưa chắc có ô riêng; nói thẳng khi chưa tra được cổng thuế | `onboard-household`, `--read`, `--open`, `--notfound` |
| 3 | Cách bán và việc OPC làm | Chọn cách bán, hàng từ đâu; xem 12 việc và cách gợi ý sẵn | Xếp việc: Cần để bắt đầu / Nên có / Khi cần | `onboard-model`, `onboard-features`, `onboard-feature` |
| 4 | Xác minh chủ hộ | App Cas ID (máy có NFC), hoặc nhân viên OPC, hoặc để sau | Mã 5 phút; không tự quét trên cùng điện thoại | `onboard-verify`, `--app`, `--failed` |
| 5 | Hàng đầu tiên | Chụp bảng giá, bán thử một đơn | Coach từng bước | `onboard-products`, `onboard-firstsale`, `onboard-done` |

Giá trị đầu tiên = đơn bán thử đầu tiên. Chưa xác minh: vẫn bán tiền mặt, chưa nối được ngân hàng và hoá đơn. Chế độ nhân viên (`onboard-assisted`) là cùng luồng.

### Phần B — Readiness: danh sách việc làm dần (sinh theo mô hình ở bước 3)

| Mục | Quầy | B2B | Chế biến | Cách nhập / kết nối |
|---|---|---|---|---|
| Hàng hoá & bảng giá | Bắt buộc | Bắt buộc + **giá riêng theo khách** | Bắt buộc | ảnh bảng giá (AI đọc), Excel, nhân viên nhập giúp (#17) |
| Tồn đầu kỳ | Nên có | **Bắt buộc** (để giữ hàng) | **Bắt buộc, theo lô** | đếm + nhập, Excel |
| Khách hàng, điều khoản, hạn mức | Tuỳ chọn | **Bắt buộc** | — | MST → tự điền (#10), Excel |
| Nhà cung cấp | Tuỳ chọn | Nên có | **Bắt buộc** | MST → tự điền |
| Hoá đơn | Máy tính tiền (Hilo) | Có mã (X Invoice) + **chữ ký số** **[Câu 2]** | — | #4, #8 |
| Kênh bán | — | Zalo OA (nên có) | — | #11 |
| Cách giao mặc định | — | **Bắt buộc** | — | #13 hoặc làm tay |
| Người dùng & vai trò | Nên có | **Bắt buộc** | Nên có | mời qua số điện thoại |
| Ngưỡng duyệt | Mặc định | Xem lại | Mặc định | mặc định sẵn, chỉnh được |
| Thuế: nhóm ngành, kỳ khai | Bắt buộc | Bắt buộc | Bắt buộc | gợi ý từ ngành nghề đăng ký |
| Cài OPC như ứng dụng (dùng được khi mất mạng) | Nên có | Nên có | Nên có | hướng dẫn cài PWA |
| Đồng ý dữ liệu & quyền riêng tư | Bắt buộc | Bắt buộc | Bắt buộc | — |

Một hộ thuộc nhiều cột thì gộp lại; mục bắt buộc ở bất kỳ cột nào là bắt buộc.

**Trạng thái readiness** (tính tự động): *Chưa bắt đầu* · *Đang thiết lập* · *Bị chặn* (mục bắt buộc lỗi, ví dụ thiếu
bảng giá) · *Sẵn sàng có điều kiện* (đủ bắt buộc, còn nên có) · *Sẵn sàng*. Trang chủ hiện "còn 3 việc"; nhân viên
hỗ trợ xem **cùng một danh sách** khi ngồi cùng hộ (chế độ hỗ trợ, `onboard-assisted`).

**Ngoại lệ (UC-01):** thiếu bảng giá → *Bị chặn* → mở Hàng hoá & bảng giá → "Dùng dữ liệu mẫu" (chỉ demo) hoặc chụp
bảng giá → kiểm tra lại. Kết nối lỗi → mục chuyển *Lỗi* kèm đường làm tay; không chặn các mục khác.

---

## Phụ lục A — Bảng trạng thái chung (hiển thị · BA · máy trạng thái của CEO)

Chữ ở cột "Hiển thị" là chữ người dùng thấy; mỗi trạng thái luôn có màu + hình + chữ, giống nhau ở mọi màn.

| Đối tượng | Hiển thị (tiếng Việt) | BA (Key UC §8) | CEO (báo cáo Casso §6.2) |
|---|---|---|---|
| **Đơn** | Nháp · Chờ duyệt · Đã giữ hàng · Đã xác nhận · Đang soạn · Đang giao · Chờ tiền · Đã đóng · Đã huỷ | Draft, Chờ duyệt, Đã giữ hàng, Đã xác nhận, Đang giao, Chờ tiền, Đã đóng, Đã hủy | CHO_THANH_TOAN, HET_HAN… (đơn QR) |
| **Giữ hàng** | Đang giữ (đến …) · Đã dùng · Đã nhả · Hết hạn giữ | Active, Consumed, Released, Expired | — |
| **Tiền vào** | Chờ khách chuyển · **Đã nhận · chờ xác minh** · Đã xác minh · Thiếu / Thừa · Chưa gán · Đã hoàn | Received, Matched, Needs Review, Allocated, Refunded | DA_NHAN_TIEN, LECH_TIEN, DA_XAC_MINH |
| **Phải thu / phải trả** | Đang mở · Trả một phần · Quá hạn n ngày · Đã đóng | Receivable Đang mở | — |
| **Hoá đơn** | Nháp chờ duyệt · Chờ mã CQT · Có mã CQT · Bị từ chối · **Chưa rõ kết quả** · Đã điều chỉnh / thay thế | Draft, Submitted, Issued, Rejected, Adjusted | CHO_DUYET_HD, DA_PHAT_HANH, CO_MA_THUE, HD_HONG, CHUA_RO |
| **Giao hàng** | Chờ soạn · Đã soạn · Đã bàn giao · Đang giao · Đã giao · Giao một phần · Thất bại · Đang hoàn về | Picking, Handed Over, In Transit, Delivered, Failed, Returning | — |
| **Đơn mua / nhận hàng** | Nháp · Đã xác nhận · Nhận một phần · Đã nhận · Đã huỷ | (F03) | — |
| **Lô** | Mới · Đang bán · Sắp hết hạn · Đã khoá · Hết | (F04) | — |
| **Lệnh chế biến** | Nháp · Đang làm · Xong · Đã huỷ | Đang thực hiện | — |
| **Kỳ thuế** | Đang thu dữ liệu · Cần xem · Sẵn sàng tính · Đã khoá · Đã có tờ khai nháp · Đã duyệt · Đã tiếp nhận · Đã nộp · Đã đóng | Collecting Data, Needs Review, Ready, Drafted, Approved, Filed, Paid, Closed | KY_THUE + mã biên nhận |
| **Quy trình (Control Tower)** | Đang chạy · Cần chị quyết · Chờ kết nối · Sẽ thử lại lúc … · Bị chặn · Xong | Running, Waiting Human, Waiting Connector, Retry Scheduled, Blocked, Completed | — |
| **Kết nối** | Chưa kết nối · Đang kết nối · Hoạt động · Cần đăng nhập lại · Sắp hết hạn đồng ý · Lỗi · Tạm dừng · Mô phỏng | (F13) | GRANT_LOGIN_REQUIRED, USER_PERMISSION_REVOKED |
| **Readiness** | Chưa bắt đầu · Đang thiết lập · Bị chặn · Sẵn sàng có điều kiện · Sẵn sàng | như BA | — |

---

## Phụ lục B — Đối chiếu màn hình: 66 màn hiện có ↔ 20 màn BA cần

**Giữ, chỉ đổi dữ liệu sang An Nhiên và áp các quyết định mới**
- Quầy (12 màn): thêm "còn · đã giữ" trên ô món; chọn khách quen (giá riêng, ghi nợ); đóng ca (mới).
- Tiền & đối chiếu, gán tiền: **gán một khoản cho nhiều hoá đơn**; thêm tiền ra (đề nghị chuyển, chủ hộ tự chuyển).
- Hoá đơn, chi tiết hoá đơn, phiếu: mẫu số 2; trạng thái *Chưa rõ kết quả*; luồng sửa qua cổng nhà cung cấp.
- Đơn hàng + 9 trạng thái: cột nguồn (Quầy / Zalo OA / thủ công / định kỳ); trạng thái đơn theo Phụ lục A.
- Nhật ký (`audit`) = **UI-19**: thêm trước/sau, mã tra cứu sự kiện, lọc theo đối tượng.
- Cài đặt (hiển thị, tính năng, người dùng): vai trò mới (Người giao, kế toán có hạn), quyền "phát hành tại quầy".
- Onboarding (21 màn) = Phần A của ⓪; màn "Xong" → **Readiness**.

**Sửa lớn**
- Trang chủ = **UI-01**: Việc cần làm + một dòng "OPC đang chạy n việc · n lỗi" + readiness khi chưa sẵn sàng.
- Cần xử lý (`approvals`) = **UI-01/UI-17/UI-18**: 5 tab + chi tiết quy trình + chi tiết duyệt (`approvals.html` + 3 trạng thái, v4.2).
- Chi tiết đơn (`order-detail`) → **UI-11 Order 360**: kết quả từng quy tắc, giữ hàng, giao hàng, hoá đơn, phải thu,
  dòng thời gian bốn vai.

**Làm mới** (theo thứ tự cho demo)
1. Hộp yêu cầu bán (**UI-10**) — mọi nguồn, Trợ lý đọc, đối chiếu khách/món.
2. Soạn & giao (**UI-12**) + link xác nhận cho người giao.
3. Công nợ: phải thu (bảng kê, nhắc nợ) và phải trả.
4. Đơn mua & nhận hàng (**UI-07**), chi phí không qua kho.
5. Tồn kho, lô, truy xuất (**UI-08**), kiểm kê.
6. Chế biến (**UI-09**).
7. Sổ sách + đối chiếu kỳ (**UI-14**).
8. Thuế: tính & tờ khai nháp (**UI-15**), gửi/nộp & bằng chứng (**UI-16**) — hai mức trên cùng màn.
9. Readiness (**UI-02**), mô hình kinh doanh (**UI-03**), dữ liệu nền (**UI-04**), Kết nối theo 17 danh mục (**UI-05**),
   vai trò & ngưỡng duyệt (**UI-06**).
10. Hàng hoá & bảng giá (danh sách, giá riêng theo khách).
11. Pilot dashboard (**UI-20**) — vai trò xem của chương trình, chỉ số tổng hợp, không lộ dữ liệu hộ.
12. Mẫu offline dùng chung; Scenario Switcher + Reset (cho bản demo của bạn).


## Luồng kết nối (v4.8.0)
`Kết nối` là mục cấp 1 (chấm đỏ khi có lỗi). Nối **một lần theo tài khoản nhà cung cấp** (Zalo OA, MB qua Casso, Hilo, X Invoice, Cas ID); mỗi tài khoản làm được
nhiều **việc**, bật/tắt riêng, có đồng ý riêng (xin thêm khi bật việc mới). Các luồng nghiệp vụ chỉ xin **việc** (12 việc, gom từ 17 nhóm kết nối); OPC tìm cách đang bật, không có thì dùng đường làm tay.
Màn (từ v5.1): **Đã nối** (thẻ theo tài khoản) · **Việc OPC làm** (12 việc, 3 nhóm) · **Nhật ký**; "Thêm cách nối" mở từ Việc OPC làm. Thêm mới: chọn việc → chọn cách → đồng ý (chỉ chủ hộ: phạm vi, thời hạn, OTP) → đọc thử → "Dùng để làm gì?". Sửa: tài khoản → bật/tắt việc, Nối lại, Ngắt kết nối (hộp xác nhận nêu hậu quả).
Lỗi: thẻ đỏ + Cần xử lý; "Chưa rõ kết quả" không bao giờ tự gửi lại. Nhà cung cấp chưa làm: "Báo tôi", không có nút nối giả.

### Nhiều nhà cung cấp cùng một việc (v4.9.0)
Thêm cách nối: **theo việc** (tìm, liên kết nhảy tới việc, "Sắp có" là nhãn bấm để Báo tôi) → **trang nhà cung cấp** (làm gì, không làm gì, phí, cần chuẩn bị) → nối → "Dùng để làm gì?".
Nhóm có nhiều lựa chọn (Giao hàng…) có **trang nhóm**: các cách giao đang dùng, mặc định, cách chọn hãng (Trợ lý đề xuất, người bàn giao chọn; quy tắc tự động sau này) và bảng giá ví dụ khi bàn giao.
Khi hộ nối nhiều (10–20 tài khoản): **Cần chị xem** lên đầu, lọc Lỗi / Sắp hết hạn, danh sách gọn theo nhóm.

### Kết nối theo cách giữ khoá (v5.0.0)
| Cách | Bước | Ai | Màn hình |
|---|---|---|---|
| Qua Casso | Xem cần chuẩn bị → mở trang Casso → nhập ở đó → về OPC, đọc thử | chủ hộ (OTP) | connections--casso · --guide-casso · --testing |
| Dán khoá | Lấy khoá ở nhà cung cấp → dán vào OPC → Thử kết nối → dán địa chỉ nhận báo tiền vào nhà cung cấp → lưu | chủ hộ | connections--key · --key--error · --guide |
| Quản lý | Thử lại · Đổi khoá (khoá cũ chạy tới khi khoá mới qua thử) · Gỡ (nêu hậu quả, nhắc xoá khoá ở nhà cung cấp) | chủ hộ | connections--manage · --rotate · --remove |
| Nền tảng | Thêm nhà cung cấp (chọn cách nối + ô hộ phải nhập) · Ẩn hoặc gỡ (lý do bắt buộc, nêu số hộ và nhà cung cấp ảnh hưởng) | QNSC | platform-providers · platform-provider · --remove · --new |
Nguyên tắc: khoá không bao giờ hiện lại đầy đủ; mỗi lần đổi/gỡ ghi nhật ký; Casso là đường chung — gỡ Casso dừng 11 nhà cung cấp.

### Việc OPC làm (v5.1.0)
Đăng ký bước 3/5 `onboard-features`: OPC liệt kê 12 việc theo mô hình đã chọn ở bước 3; 4 việc "Cần để bắt đầu" có sẵn một cách nối gợi ý, chị Đổi được (`onboard-feature`) hoặc nhờ nhân viên OPC nối giúp. Việc nào chưa nối thì chỉ khoá luồng phụ thuộc (tiền chuyển khoản, đơn sỉ, hoá đơn có mã), không khoá cả app. Sau khi vào app: Kết nối › Việc OPC làm (`connections--category`) là cửa chính; mỗi việc mở `connections--feature`; "Tất cả nhà cung cấp" là tra cứu phụ.

### Sẵn sàng theo chuỗi (v6.0.0)
`readiness--new` / `readiness` chia 33 việc theo 5 chuỗi: Hộ và người · Bán và thu · Mua và trả · Chế biến và kho · Thuế và sổ (`tools/v4/readiness_model.py`). Mỗi chuỗi: việc **bắt buộc** còn mở (kèm việc nó khoá: nhận chuyển khoản, đơn sỉ, hoá đơn có mã, lệnh chế biến, thuế tạm tính), "Nên có" luôn hiện, "Làm sau" và "Đã xong" gập nhưng tên vẫn thấy. Cổng chỉ khoá luồng phụ thuộc, không khoá cả app. Kỳ khai tự tính theo doanh thu lũy kế (quý khi vượt 500 triệu); ngưỡng 1 tỷ cho hoá đơn máy tính tiền. Các mốc pháp lý cần kế toán xác nhận.

### Mở hộ v7 (6 bước) — thay Phần A cũ
1 Số điện thoại + đồng ý dữ liệu · 2 Hộ kinh doanh (chụp giấy / chưa có → đăng ký ở xã) · 3 Cách bán (bán cho ai, hàng từ đâu, thuê người, thực phẩm) + Việc OPC làm · 4 VNeID và eTax, cách khai thuế, tài khoản dùng kinh doanh · 5 Hoá đơn điện tử (cách xuất, đăng ký 01/ĐKTĐ-HĐĐT, chữ ký số) · 6 Số đầu kỳ (hàng, giá, tồn đã đếm, tiền, công nợ) → giao dịch đầu tiên. Xác minh chủ hộ và nối ngân hàng: tuỳ chọn, mở từ Sẵn sàng. Màn hình: onboard-consent, -household(--read/--notfound/--unregistered), -model, -features, -feature, -gov, -tax, -bankacc, -invoice(--register), -products(--review), -opening, -done.

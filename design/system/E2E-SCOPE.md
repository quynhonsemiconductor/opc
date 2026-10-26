# OPC end-to-end scope (v7, 08/10/2026) — what MUST exist vs what can be skipped

Source of truth for v7 design. Supersedes the scope tables in SCOPE-MVP.md §8 and FLOWS ⓪ where they disagree.
Built from: BA v0.8 (07/10), OPC v6, and research in `_research/` (law 2025–2026, KiotViet/Sapo/MISA/Odoo/Shopify/Square/QuickBooks/Xero).
Rule: **Bắt buộc** = without it one end-to-end chain breaks, or the law requires it (added even if BA left it out). **Tuỳ chọn** = shown in the UI with "Bỏ qua", never blocks a chain.
Two different things: a **bắt buộc feature** (OPC must have it: sổ, kê khai, đối soát…) vs a **bắt buộc connection** (the household must connect an outside system). A connection is bắt buộc only when the chain cannot be done correctly and legally by hand. Today that is only the e-invoice provider (an e-invoice can only be issued through a registered provider). Zalo OA and the bank speed things up but the chain runs without them (nhập tay, xác nhận theo sao kê) → **tuỳ chọn, nên có**. OTP and owner notifications are OPC's own platform services — nothing for the household to connect.

## The chain
Thiết lập → Mua → Nhận hàng → Kho → Bán → Giao → Hoá đơn → Thu tiền → Đối soát → Sổ → Kỳ khai (eTax) → Bằng chứng. Every record keeps source, actor, time; audit is append-only; data can be exported.

## 1 · Thiết lập (Foundation)
| Item | Level | Note |
|---|---|---|
| Đăng nhập bằng số điện thoại + mã | Bắt buộc · dịch vụ của OPC (SMS, Zalo của OPC nếu có) | Platform service — the household connects nothing |
| Hồ sơ hộ: tên, mã số thuế, ngành nghề đăng ký, địa chỉ | Bắt buộc | Photo of giấy đăng ký read by the Agent, owner confirms; lookup only cross-checks |
| Một kho | Bắt buộc | |
| Danh mục: khách, nhà cung cấp, hàng (đơn vị/quy cách dạng số), bảng giá | Bắt buộc | Quy đổi đơn vị: tuỳ chọn (later) |
| Tồn đầu kỳ (đếm, xác nhận một lần) | Bắt buộc | **BA thiếu chi tiết** — added |
| Số dư đầu kỳ: tiền mặt, tiền gửi, công nợ phải thu/phải trả | Bắt buộc | **BA thiếu** — books cannot balance without it |
| Doanh thu từ đầu năm trước ngày dùng OPC | Bắt buộc (khi bắt đầu giữa năm) | **BA thiếu** — needed for the 1 tỷ mark and the annual revenue notice; asked in Sổ & kê khai, not at signup |
| Người dùng: chủ hộ | Bắt buộc | Nhân viên bán, kế toán chỉ xem/xuất: tuỳ chọn |
| Nhật ký chỉ ghi thêm, xuất dữ liệu (CSV/Excel/PDF/XML) | Bắt buộc | Province requires export; lưu chứng từ 10 năm |
| Đồng ý xử lý dữ liệu (Luật 91/2025) | Bắt buộc | |
| Xác minh chủ hộ (eKYC) | Tuỳ chọn | Only if a provider demands it when connecting a bank |

## 2 · Mua hàng và kho (Procure-to-Pay)
| Item | Level | Note |
|---|---|---|
| Đơn mua (tay hoặc Agent đề xuất → chủ hộ xác nhận) | Bắt buộc | BA |
| Nhận hàng theo thực nhận, nhận nhiều lần, thiếu/thừa | Bắt buộc | BA + nhận lần hai |
| Chứng từ mua: hoá đơn điện tử (tải lên XML/PDF) hoặc ảnh giấy + nhập tay | Bắt buộc | Lấy tự động từ cổng thuế: **tuỳ chọn** (kết nối, legal check N-15) |
| Trả tiền nhà cung cấp: nhiều lần, mua chịu, số còn nợ | Bắt buộc | **BA sai** ("trả đủ một lần") — research: distribution buys on credit |
| Mở app ngân hàng với VietQR điền sẵn | Tuỳ chọn | OPC never moves money |
| Chi phí không qua kho (điện, nước, thuê, vận chuyển…) | Bắt buộc | |
| Trả hàng cho nhà cung cấp | Bắt buộc (tối thiểu) | **BA để ngoài happy path** — added |
| Tồn thực tế / đang giữ / khả dụng, lịch sử | Bắt buộc | |
| Kiểm kho + điều chỉnh có lý do, chủ hộ duyệt | Bắt buộc | **BA thiếu chi tiết** |
| Hạn dùng + cảnh báo cận hạn | Tuỳ chọn theo mặt hàng | Lô: không làm |
| Chế biến | Tuỳ chọn (tắt trong pilot) | BA bỏ |

## 3 · Bán hàng, hoá đơn và tiền (Order-to-Cash)
| Item | Level | Note |
|---|---|---|
| Nhận yêu cầu: nhập tay (dán tin, ảnh, gõ) | Bắt buộc | Agent đọc, soạn; không tự gửi |
| Nối Zalo OA để yêu cầu tự vào | Tuỳ chọn, nên có | Không có Zalo OA vẫn bán được |
| Đơn bán: xác nhận trong tồn khả dụng, giữ hàng | Bắt buộc | BA |
| Sửa đơn giá trên dòng | Bắt buộc | Replaces a discount engine |
| Giao: "Đã giao" = giao đủ, trừ kho một lần | Bắt buộc | Phần lấy sau = đơn mới. Giao qua hãng: tuỳ chọn |
| Hoá đơn điện tử: một hoá đơn mỗi đơn, phát hành khi "Đã giao" | Bắt buộc · **kết nối bắt buộc duy nhất: nhà cung cấp hoá đơn điện tử** (khi hộ phải hoặc cần xuất hoá đơn: từ 1 tỷ, hoặc khách sỉ đòi hoá đơn) | Khách lẻ không bắt MST; điều chỉnh/thay thế (04/SS) làm ở nhà cung cấp, OPC giữ liên kết; bán không hoá đơn được ghi (hộ dưới 1 tỷ) |
| Hoá đơn máy tính tiền | Bắt buộc với hộ từ 1 tỷ bán lẻ trực tiếp | Nghị định 70/2025 |
| Thu tiền: tiền mặt, chuyển khoản (chủ hộ xác nhận theo sao kê) | Bắt buộc | |
| Nối ngân hàng để tiền về tự khớp, QR theo đơn | Tuỳ chọn, nên có | Hộ phải báo tài khoản cho cơ quan thuế dù có nối hay không |
| Khớp tiền: QR/tài khoản ảo theo đơn; "Tiền chưa gán"; một khoản cho nhiều đơn; trả một phần | Bắt buộc | **BA thiếu** (một khoản nhiều đơn "hiếm") |
| Tiền dư → ghi chú + "khách trả trước" (gợi ý trừ lần sau) | Bắt buộc | |
| Chống trùng tiền mặt ↔ ngân hàng | Bắt buộc | |
| Công nợ phải thu + bảng kê theo khách | Bắt buộc | Hạn mức mềm (chỉ cảnh báo): tuỳ chọn |
| Đóng đơn khi tiền đã khớp; việc còn chờ vẫn hiện | Bắt buộc | BA |
| Khách trả hàng (tồn +, nợ − hoặc hoàn, nhắc hoá đơn điều chỉnh) | Bắt buộc (tối thiểu) | **BA thiếu** |
| Bán nhanh (tạo + giao + thu một chạm) | Tuỳ chọn | Bắt buộc nếu hộ bán lẻ tại chỗ |
| Báo tin cho khách qua ZNS | Tuỳ chọn | Cần mẫu được Zalo duyệt, đồng ý của khách |

## 4 · Sổ sách và kê khai (Record-to-Tax)
| Item | Level | Note |
|---|---|---|
| Sổ quỹ tiền mặt, sổ tiền gửi | Bắt buộc | **BA thiếu** |
| Sổ theo Thông tư 152/2025 (doanh thu; chi phí khi cần; nhập–xuất–tồn), xuất được | Bắt buộc | Chờ kế toán xác nhận danh mục sổ |
| Đối soát cuối kỳ: đơn ↔ hoá đơn ↔ tiền ↔ kho | Bắt buộc | |
| Khoá kỳ; sửa sau khoá = điều chỉnh có dấu vết | Bắt buộc | BA để "chờ rule" — added minimal rule |
| Tổng hoá đơn bán ra / mua vào theo quý (ngày hoá đơn) + doanh thu luỹ kế năm so với 1 tỷ | Bắt buộc | |
| Hướng dẫn kê khai (mẫu do kế toán xác nhận), nhãn "không phải tư vấn thuế" | Bắt buộc | Không có số thuế trong pilot |
| Tiến trình: chuẩn bị → kiểm tra → làm trên eTax → đã gửi (thông báo tiếp nhận) → chờ chấp nhận | Bắt buộc | eTax: không có API → chủ hộ ghi kèm bằng chứng |
| Báo doanh thu năm (hộ dưới 1 tỷ) | Bắt buộc (chờ kế toán xác nhận hạn) | **Cả BA lẫn OPC thiếu** |
| Báo tài khoản ngân hàng/ví dùng kinh doanh cho cơ quan thuế | Bắt buộc (chờ kế toán xác nhận) | **Cả BA lẫn OPC thiếu** |
| Nộp tiền thuế (khi có) | Bắt buộc · làm ngoài OPC | Ghi mã biên nhận |
| Số thuế ước tính | Tuỳ chọn, tắt trong pilot | Bật khi kế toán xác nhận bộ quy tắc có phiên bản |

## 5 · Vận hành chung
| Item | Level | Note |
|---|---|---|
| Tổng quan / Cần xử lý: việc chờ, lỗi, kết nối lỗi, đơn đóng còn chờ | Bắt buộc | |
| Agent: đề xuất có căn cứ, chủ hộ duyệt; "Hỏi Agent" trên hồ sơ | Bắt buộc | AI: dữ liệu khách tối thiểu (Luật 91/2025) |
| Thông báo cho chủ hộ | Bắt buộc · dịch vụ của OPC (SMS; Zalo của OPC nếu chủ hộ quan tâm OA) | Household connects nothing; web push: phụ |
| Thời gian chờ, thử lại không trùng, tra kết quả trước khi gửi lại | Bắt buộc | |
| Mất mạng | Bắt buộc ở mức tối thiểu: xem + nháp + "chưa đồng bộ" | Bán tiền mặt khi mất mạng: chờ CEO |
| Dashboard chương trình (tỉnh) | Bắt buộc cho pilot | BA F15 |

## Integrations, final list (Kết nối)
Bắt buộc (household connects): **Hoá đơn điện tử bán ra** — only when the hộ must or needs to issue invoices.
OPC lo sẵn (household connects nothing): gửi mã đăng nhập, thông báo cho chủ hộ.
Tuỳ chọn, nên có: **Zalo OA** (yêu cầu tự vào), **Ngân hàng — tiền vào** (tự khớp tiền, QR theo đơn).
Tuỳ chọn: Hoá đơn mua vào từ cổng thuế · Ngân hàng — tiền ra (đối soát chi) · Mở app ngân hàng (VietQR) · Giao hàng qua hãng · ZNS báo khách · Xác minh chủ hộ · Xuất cho phần mềm kế toán.
Bỏ khỏi OPC: chữ ký số do OPC (nhà cung cấp hoá đơn ký), nộp tờ khai qua T-VAN, sàn thương mại điện tử (sau pilot).

## Thuế và kế toán: chức năng bắt buộc, không phải kết nối
All Record-to-Tax items above marked Bắt buộc are mandatory OPC features because the law requires them of every hộ (sổ theo Thông tư 152/2025, lưu chứng từ 10 năm, kê khai/thông báo doanh thu, báo tài khoản dùng kinh doanh). None of them needs a connection: eTax has no API for OPC; the owner files and pays on eTax and OPC records the proof. Only **số thuế ước tính** is optional (off until an accountant confirms the rules).

## Onboarding v7 — mandatory then optional (from `_research/mandatory-2026.md`)
Mandatory = law or the chain needs it. Each mandatory item can be "nhân viên OPC làm cùng"; none needs a household connection except the e-invoice provider.

| # | Bước bắt buộc | Vì sao | Kết nối |
|---|---|---|---|
| 1 | Số điện thoại + mã | đăng nhập | OPC lo |
| 2 | Hộ đã đăng ký kinh doanh chưa → có: chụp giấy đăng ký (tên hộ, ngành nghề, địa điểm, chủ hộ, MST = số định danh chủ hộ); chưa: hướng dẫn đăng ký ở xã, OPC chỉ mở phần chuẩn bị | NĐ 168/2025 | — |
| 3 | Chủ hộ: VNeID mức 2 và tài khoản eTax đã có chưa (chỉ hỏi, OPC không giữ mật khẩu) | eTax phải liên kết VNeID trước 31/12/2026; cần để kê khai | — (state platforms, owner uses directly) |
| 4 | Cách bán, hàng từ đâu, có thuê người làm không, có kinh doanh thực phẩm không | sinh danh sách nghĩa vụ: hoá đơn máy tính tiền, BHXH, giấy ATTP | — |
| 5 | Thuế: doanh thu năm ước tính + kỳ khai/phương pháp chị đã khai (OPC gợi ý theo bộ quy tắc, chị xác nhận) | tự khai từ 2026; xác định nhóm, kỳ khai, có bắt buộc hoá đơn không | — |
| 6 | Tài khoản ngân hàng/ví dùng kinh doanh + đã báo cơ quan thuế chưa | bắt buộc báo tài khoản | — (nối feed: tuỳ chọn) |
| 7 | Hoá đơn điện tử khi bắt buộc: chọn hoá đơn miễn phí của cơ quan thuế (nếu đủ điều kiện) / nhà cung cấp / đã có; chữ ký số (SmartCA trên VNeID / đã có / không cần với máy tính tiền); đăng ký 01/ĐKTĐ-HĐĐT | luật hoá đơn 2026 | **bắt buộc: nhà cung cấp hoá đơn** |
| 8 | Số đầu kỳ: hàng và giá, tồn đã đếm, tiền mặt, tiền gửi, công nợ phải thu/phải trả (hoặc "bắt đầu từ 0") | sổ TT 152/2025 cân được | — |
| 9 | Đồng ý xử lý dữ liệu + thông báo cho khách | Luật 91/2025 | — |
| 10 | Giao dịch đầu tiên có hướng dẫn | first value | — |

Optional, shown with "Bỏ qua": Zalo OA (yêu cầu tự vào) · nối ngân hàng (tiền tự khớp, QR theo đơn) · hoá đơn mua vào từ cổng thuế · mời nhân viên bán · mời kế toán (chỉ xem/xuất) · khách, nhà cung cấp chi tiết · thông báo qua Zalo của OPC · cài app lên màn hình chính · giao qua hãng · ZNS báo khách · lộ trình lên doanh nghiệp (ưu đãi 3 năm TNDN, tư vấn miễn phí).

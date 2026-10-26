# Research brief — OPC vs BA (08/10/2026)

OPC = responsive web app (phone first) that runs a Vietnamese hộ kinh doanh end to end: mua hàng → kho → bán → giao → hoá đơn → tiền → sổ → thuế.
Pilot: 5–10 hộ ở Gia Lai, quý IV/2026, chương trình "Kế nghiệp số" của tỉnh (người kế nghiệp 25–40 tuổi, bố mẹ lớn tuổi; thiết bị phổ thông, mạng yếu).
The province asks: dùng nền tảng có sẵn, ưu tiên điện thoại, tối thiểu bán hàng phải chạy khi mất mạng, xuất được dữ liệu, có hỗ trợ tại chỗ.

There are two candidate designs. The owner does NOT assume either is right; the goal is the design that is correct, realistic for a Vietnamese household business in 2026, legally safe, and end-to-end.
- **OPC (current design)** — what we drew.
- **BA (PO decisions 07/10/2026)** — the new business analysis.

| # | Topic | OPC now | BA |
|---|---|---|---|
| T1 | Chế biến (simple processing) | Supports it: lệnh chế biến, công thức, hao hụt, lô thành phẩm (demo: bò một nắng tự làm) | Removed. Pilot = hộ mua về bán, phân phối/cung cấp hàng hoá, one warehouse |
| T2 | Tax | OPC computes estimated tax (Mô phỏng) by rate × revenue per industry group, drafts the tờ khai, owner approves; filing via eTax or T-VAN; payment receipt recorded; period closes when 3 proofs | OPC never computes tax. It totals sale and purchase invoices per quarter by invoice date, shows a guide for the chosen form (01_CNKD TT40 2026), the owner files on eTax, then records "đã gửi" + evidence; status "chờ cập nhật". No tax numbers until an accountant confirms rules |
| T3 | Onboarding asks revenue year-to-date to watch thresholds (500 triệu quarterly, 1 tỷ invoice) | Yes | No: "không tự suy chế độ thuế từ doanh thu" |
| T4 | Credit limit, overdue blocking, discount | Customer credit limit + overdue check; owner can override with a reason; discount policy setting | None. Debt is information only; no discount feature |
| T5 | Partial stock / partial delivery | Hold per lot, delivery picking, partial handling | Confirm only within available stock (ask 10, have 6 → edit to 6 or buy first). One button "Đã giao" = delivered in full, stock out once. No partial, no backorder |
| T6 | Order lifecycle / close | Linear stepper: request → check → approve → hold → pick → deliver → invoice → money → close | Four independent tracks (order, delivery, invoice, money). Owner closes when money received is linked; delivery/invoice don't block close; closed orders with pending delivery/invoice stay in to-do |
| T7 | Invoice timing | Counter: cash-register invoice at payment; B2B: after delivery, owner issues | One invoice per order, triggered by "Đã giao" |
| T8 | Quầy (fast counter POS) + Đóng ca | 13 counter screens, shift close, cash-register invoice | No counter: khách lẻ and doanh nghiệp use the same order flow |
| T9 | Offline | Counter sells cash offline, queue invoices | Do not promise stock/money actions offline until policy decided; show "chưa đồng bộ" |
| T10 | Agent messaging customers on Zalo | Agent drafts; staff presses send; reminders via ZNS | Agent never sends Zalo; owner talks to customers outside OPC |
| T11 | Paying suppliers | Payables with due dates; "OPC soạn lệnh chuyển khoản, chủ hộ tự bấm" | Owner records "đã trả" (cash/transfer, amount, date), paid in full once, before or after receipt; no transfer order; installments/credit purchase later |
| T12 | Documents | AI reads photo of supplier invoice | Electronic invoices via provider; handwritten = photo + manual entry; OCR later; photo ≠ legal proof |
| T13 | Units | (not designed) | Owner sets unit/packaging field; no automatic thùng↔chai conversion |
| T14 | Lot / expiry | Lots + expiry on goods | Open question (Q-02) |
| T15 | Roles | Owner, operator, cashier, deliverer (link), accountant (time-boxed) | Only owner confirmed; other roles open (Q-18); accountant does not operate in app by default |
| T16 | Navigation | Hôm nay · Quầy · Cần xử lý · Bán · Hàng hoá · Tiền · Sổ & thuế · Kết nối (top level) · Cài đặt | Tổng quan · Mua hàng · Bán hàng · Hàng hoá và kho · Tiền và chứng từ · Sổ sách và kê khai · Thiết lập (Kết nối inside Thiết lập) |
| T17 | Purchase flow | Purchases list + separate receive page; receive with lots; options "HTX giao bù" | Purchase order record with 4 sections (hàng mua, nhận hàng, chứng từ, tiền đã trả). Received 18/20 → stock +18, 2 short tracked; order required before stock increases |

Return format (per topic you were given): **Reality** (what Vietnamese hộ kinh doanh actually do, with numbers if any) · **Law / platform constraints 2026** (cite document number + date, link) · **What leading products do** (KiotViet, Sapo, MISA eShop/AMIS HKD, Viettel Tendoo/ VNPT, Odoo, Shopify/QuickBooks/Xero where relevant, with links) · **Verdict**: OPC / BA / hybrid, and the exact recommended design in 2–4 bullets · **Confidence** high/medium/low and what is still unverified. Cite sources inline (URL). Never invent a law number; if you cannot confirm, say so. Write in Vietnamese. Max ~250 words per topic.

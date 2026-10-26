# OPC — MVP scope and information architecture (design input, 2026-10-02)

Status: **provisional**. The CEO's module list was merged with the gap analysis from 2026-10-02. Five questions
are still open (§6) and defaults are assumed. Change this file when they are answered, then re-run the IA
evaluation.

Rule for the whole MVP: **wide but thin.** Every area exists, at the thinnest depth that is legally correct and
usable by a one-person household. Depth beyond that is a **feature switch** per household, off by default
unless the household's profile needs it.

## 1. Roles and surfaces
| Role | Surface | Sees |
|---|---|---|
| Owner (chủ hộ) | `app`, phone first | 5 owner groups (§2). Approves everything OPC or the assistant drafts |
| Manager / staff (Phúc, thu ngân) | `app` | Same groups, filtered by permission (e.g. a cashier sees Bán + Đóng ca only) |
| Delegated accountant | `app`, accountant view (`data-density="compact"`) | Sổ & thuế, Hoá đơn vào/ra, Công nợ, Báo cáo across the households that delegated to them; time-boxed |
| Programme officer | `gov` | Activation milestones, anonymised aggregates; no household data |
| QNSC support / ops | `console` (F2) | Agent Control Tower, assisted onboarding, connector health, audit search |
| Buyer (public) | `site` | QR trace pages a household published |

## 2. Owner information architecture (app) — v2.1 after the IA evaluation
**Desktop sidebar:** Hôm nay · **Quầy bán hàng** · Bán · Tiền · Hàng hoá · Sổ & thuế · Cần xử lý; footer Cài đặt ·
Trợ giúp. Group pages start with `c-subnav`; feature switches (⚙) only add or remove sub-nav items.
**Phone tabs:** Hôm nay (count = Cần xử lý) · Quầy · Bán · Tiền · Thêm. "Thêm" lists only what has no tab:
Cần xử lý (pinned) · Hàng hoá · Sổ & thuế · Hỏi Trợ lý · Thông báo · Cài đặt · Trợ giúp.

| Group | Sub-nav | Entry points that are not in the menu |
|---|---|---|
| Hôm nay | — (money truth, Cần xử lý top 3, ca đang mở → **Đóng ca**) | |
| Quầy | — (focus mode) | **Trả hàng** action in the counter header |
| Bán | Đơn hàng · Giao hàng ⚙ · Đặt chỗ ⚙ · Khách hàng | Order detail: **Trả hàng / hoàn tiền**, history |
| Tiền | Thu chi & đối chiếu · Công nợ (phải thu; phải trả ⚙) · Đóng ca | |
| Hàng hoá | Danh sách & giá · Tồn kho · Nhập hàng & chi phí ⚙ · Nhà cung cấp ⚙ · Thu mua nông sản ⚙ | Item page: **price and stock history** |
| Sổ & thuế | Hoá đơn (bán ra; mua vào ⚙) · Sổ sách · Thuế & tờ khai · Báo cáo | |
| Cần xử lý | — (tabs: Chờ chị duyệt · Cảnh báo · Đã xử lý) | Approve shows a receipt and offers **Hoàn tác** for 10 s |
| Cài đặt | Hộ · Người dùng · Kết nối · Tính năng · Dữ liệu · **Nhật ký hoạt động** | Also reachable from the avatar menu |
| Top bar | Search · **Trợ lý** (assistant Q&A) · **Thông báo** (bell → notification centre) · avatar menu (Tài khoản, Người dùng, Đăng xuất) | Accountant: the household switcher (`c-hh`) lists the delegated households |

Công nợ has one home: **Tiền → Công nợ**. The Khách hàng list shows each customer's debt total and links there.
When a switch is OFF, its group still shows one quiet row, e.g. Hàng hoá → "Nhập hàng & chi phí — bật trong Cài đặt → Tính năng", so the owner is never left without a way in.
Nhật ký hoạt động filters by person, by kind of change (Giá & hàng hoá · Tiền · Đơn hàng · Người dùng & quyền) and by date.
Deferred switches (Đặt chỗ, Thu mua nông sản, Truy xuất) show "Sắp có" and are disabled until their screens exist.
Wording: say "đối chiếu" instead of "đối soát". On first use on a page, write "mã cơ quan thuế (CQT)".
Deferred for the pilot: **screens** for Đặt chỗ, Thu mua nông sản and Truy xuất nguồn gốc. Their switches stay,
but are hidden until a household needs them and the CEO answers open question 4.

## 3. Capability map (CEO list + gaps), MVP depth
| Area | MVP (thin) | Switch / later | Designed? |
|---|---|---|---|
| Onboarding & dữ liệu nền | Phone/OTP, MST lookup, L1 verify, bank link, products by AI photo/voice/template, invoice setup, first sale; import customers/suppliers/opening stock from photo/Excel | — | ✅ main flow + errors; import ❌ |
| Khách hàng, NCC, sản phẩm, bảng giá | One contact book (khách / NCC flag), giá lẻ + giá sỉ per customer | NCC ⚙ with purchasing | ❌ |
| Quầy + thu QR + xác minh (gap #1) | Counter, VietQR, 3 money states, delivery limit, cash, công nợ | offline in native F3 | ✅ |
| Kết nối ngân hàng + đồng ý 180 ngày (gap #2) | Link, name match, renew consent, freshness | more banks | partial (onboarding) |
| Mua hàng, chi phí, nhập kho | Photo of invoice/receipt → AI draft phiếu nhập + chi phí → approve; bảng kê thu mua for farmers ⚙ | **⚙ default ON only for households > 1 tỷ** or on profit-based PIT | ❌ |
| Tồn kho | Per item, low-stock alert, stock count with reason; one location; lots/expiry only for traceable food | multi-location later | partial (alerts) |
| Báo giá, đơn hàng, công nợ | Báo giá = draft order sent by Zalo; confirm → auto hold stock; due date + reminder | — | ✅ orders; báo giá ❌ |
| Soạn, giao, giao thất bại | "Cần giao hôm nay"; chờ giao → đang giao → đã giao / không giao được (lý do · giao lại · huỷ trả kho). No picking lists, no carrier API | ⚙ Giao hàng | ❌ |
| Đặt chỗ (gap #8, tourism) | Rooms/tours as resources, hold → confirm → check-in, deposit by QR | ⚙ Đặt chỗ | ❌ |
| Thu, chi, phải thu, phải trả | Phiếu thu/chi tied to order or expense; bank + cash; đóng ca with cash count | phải trả ⚙ | partial (money, AR) |
| Huỷ, trả hàng, hoàn tiền, điều chỉnh hoá đơn (gap #10) | Cancel/return with reason, refund record, guided invoice adjust/replace on the provider portal | — | ❌ |
| Hoá đơn đầu vào, đầu ra | Out: done. In: photo/manual; GDT Hub sync opt-in (cost, legal basis) | ⚙ with purchasing | ✅ out; in ❌ |
| Sổ nghiệp vụ & đối soát | Books per TT 152/2025 generated from transactions (S1a for most; more books only when required); bank reconciliation; 2-way invoice ↔ phiếu nhập | — | partial |
| Thuế | Compute → draft return (structured/XML) → **owner files on eTax** (guided) → OPC records the receipt code as evidence. **No filing or payment on the owner's behalf** (programme rules N-06/N-07) | Casso filing only after testing | partial (home card) |
| Cần xử lý + Nhật ký (owner side of the Control Tower) | One approval inbox for every draft (assistant, bank, system) with evidence; audit log of every change by person / assistant / system | full Control Tower in console F2 | ❌ |
| Người dùng & quyền (gap #4) | Owner, manager, cashier, accountant (time-boxed delegation), devices, L0–L2 gates | — | ❌ |
| Dữ liệu & quyền riêng tư (gap #5) | Consents (eKYC separate), retention, export, erasure request | — | ❌ |
| Thông báo & nhắc hạn (gap #6) | Zalo ZNS + in-app: tax deadlines, debt reminders, 180-day consent, invoice errors | — | partial |
| Truy xuất nguồn gốc (gap #7) | Publish a lot page with QR (explicit publish) | ⚙ | ❌ |
| Đóng ca (gap #11) | Count cash, difference with reason, hand-over | — | ❌ |
| Trợ lý (gap #12) | Q&A with read-only tools; never decides numbers | — | partial (help, home card) |
| Báo cáo (gap #14) | Doanh thu, lãi lỗ đơn giản, hàng bán chạy, công nợ | — | ❌ |
| Hỗ trợ (gap #13) | Assisted onboarding, help pages, "Gọi hỗ trợ" | console F2 | partial |
| B2G (gap #3) | Milestones per household (installed, first invoice, active at 90 days) in `gov`; consent-based | — | ❌ (gov app) |

Not in MVP: formal quotations module, picking lists, warehouse transfers, multi-warehouse, PO, 3-way match,
tiered price lists, carrier integrations, automatic tax payment, multi-agent dashboard for owners.

## 4. Feature switches (Cài đặt → Tính năng)
| Switch | Default | Turns on |
|---|---|---|
| Mua hàng & chi phí (+ NCC, phải trả, hoá đơn mua vào) | ON if revenue > 1 tỷ or profit-based PIT, else OFF (recommended ON when a cost book is required) | Hàng → Nhập hàng; Tiền → Phải trả; Sổ → Hoá đơn mua vào |
| Giao hàng | OFF (ON if the household chose wholesale or delivery at onboarding) | Bán → Giao hàng |
| Đặt chỗ | OFF (ON for tourism) | Bán → Đặt chỗ |
| Thu mua nông sản | OFF (ON for agriculture) | Hàng → Thu mua (bảng kê) |
| Truy xuất nguồn gốc | OFF | Lot pages + QR |
| Nhiều người dùng | ON | Người dùng & quyền |

## 5. Golden thread (must be perfect first)
Bán (quầy/đơn) → Thu (QR/tiền mặt/công nợ) → Xác minh → Hoá đơn ra → Sổ tự ghi → Đối soát → Tạm tính thuế →
Tờ khai (owner files) → Bằng chứng. Every screen shows where an item is on this thread.

## 6. Open questions (defaults assumed)
1. Share of households above / below 1 tỷ. **Default: most are below**, so purchasing is OFF by default.
2. Segment mix (retail / wholesale + delivery / tourism / agriculture). **Default: mixed**, so switches are
   chosen at onboarding by ngành.
3. B2G reporting needs and who pays. **Default: province pays per milestone.**
4. Are booking and traceability in the pilot? **Default: designed now, switched on per household.**
5. Tax filing path. **Default: the owner files on eTax and OPC prepares the return and keeps the evidence**
   (N-06/N-07).

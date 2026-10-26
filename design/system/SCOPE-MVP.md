# OPC — MVP scope and information architecture (design input, 2026-10-02)

Status: **provisional** — **read §7 first (decisions 2026-10-04 after the BA docs); it overrides earlier sections where they differ.** The CEO's module list was merged with the gap analysis from 2026-10-02. Five questions
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
| Area | MVP (thin) | Switch / later | Designed? (2026-10-04) |
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
| Cần xử lý + Nhật ký (owner side of the Control Tower) | One approval inbox for every draft (assistant, bank, system) with evidence; audit log of every change by person / assistant / system | full Control Tower in console F2 | ✅ approvals, audit |
| Người dùng & quyền (gap #4) | Owner, manager, cashier, accountant (time-boxed delegation), devices, L0–L2 gates | — | ✅ settings-users (+ OTP) |
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

## 7. Decisions 2026-10-04 — after the BA set (BRD 0.6, Capability Map 0.3, Feature Catalog 0.1, Key Use Cases 0.1) and the CEO's Casso test (29/09)
These replace the defaults above where they differ. Sources: BA docs in `opc/docs/ba/`, CEO report `Casso cho SoloMatrix`
(requirement codes R-…/OPC-…, anti-scope N-…). **Q** = still needs CEO/BA (see the end).

**Scope and surface**
1. MVP = **Quầy (counter) + B2B** as the BA describes, across the four chains: Procure-to-Pay, Produce-to-Stock,
   Order-to-Cash, Record-to-Tax. Purchase, simple production, lots and two-way traceability are **on by default**
   (BA: MVP Core), no longer behind switches. Đặt chỗ, Thu mua nông sản stay "Sắp có" (pilot = specialty household).
2. **Web first** (responsive/PWA); native is the next phase. **Phone is the primary surface** (R-A2, BA §7.1) → 390 is
   the first size we grade; the ≥1180 two-column onboarding stays as the desktop layout.
3. **Offline is required on web too** (R-A2-06, OPC-43). Works offline: counter sale, cash, static-QR fallback,
   draft orders, cached catalogue/prices/stock. Queued with a reason: QR verification, invoices with a tax code,
   tax, connections. B2B orders can be drafted offline; confirming needs a re-check online. A "Chờ đồng bộ n" pill and
   a "Đang dự phòng · QR tĩnh" state (CEO B19).
4. Demo data = **BA set**: Đặc sản Cao Nguyên An Nhiên · Kho chính Gia Lai · HTX Cao Nguyên · Sunrise Hotel ·
   Bò một nắng 500g (lots) · Muối kiến vàng 100g. Gaps filled by design, BA reviews.
5. Users are mixed (successor 25–40, elderly owner, staff, accountant): roles, not personas, decide what a screen
   shows; every screen is checked with a successor (Đầy đủ, shortcuts) and an older owner (Gọn, text lg/xl).

**One business model for counter and B2B** — the counter is a B2B order with every step collapsed into one moment
6. Same objects for every channel: customer (walk-in or a profile), order, item + lot, stock (on hand / reserved /
   available), payment (3 money states), invoice, receivable, book entry. One order list for all channels.
7. **Stock leaves the shelf once, at hand-over** (BA F05.05): the counter hands over at payment; B2B at hand-over to
   the deliverer. B2B reserves at confirmation (draft holds 24 h, confirmed holds to the delivery date).
8. The counter sells **available** stock only ("còn 26 · đã giữ 20"); selling into reserved stock needs the owner's
   approval. Lots are picked automatically, nearest expiry first, so traceability covers walk-in sales.
9. One customer book and one credit limit: a known customer can buy on credit at the counter under the same rule.
10. One rule for "goods before verified money": walk-in = the owner's threshold; B2B = the customer's credit limit.
11. Payments: one transfer can settle **many invoices** (hotels pay by statement); the assign dialog becomes
    one-to-many. Partial payments and overpayments stay in review, never guessed.

**Sales channels — one inbox, many sources**
11b. A sales request is one object whatever its source; the assistant reads text, voice, photos (handwritten orders)
     and PDFs (a hotel's purchase order) into the same draft, then the same rule checks run. MVP sources: **Zalo OA**
     (connector; BA: required channel) and **manual add** — paste or share a chat, photo, voice note, or type it in
     (covers phone calls, personal Zalo, walk-ins, sales visits). Later, each as a connector: Messenger/Facebook Page,
     email, web order form, marketplaces, **standing orders** (a hotel's weekly order as a template). Note: personal
     Zalo chats have no official API — only Zalo OA does — so most hotel chats arrive by share/forward. **Q5.**
     Three kinds of source, one order model:
     (a) **chat** — Zalo, Messenger/Facebook Page, Instagram, TikTok inbox, phone, email, livestream comments ("chốt đơn")
         → the assistant drafts the order; the household collects the money and delivers;
     (b) **platform orders** — Shopee, TikTok Shop, Lazada, own web shop (Haravan/Sapo), ShopeeFood/GrabFood → the order
         arrives complete; the **platform collects the money and pays out later minus fees** (a receivable from the
         platform, settled by its payout report), often ships it, handles returns; and the platform **withholds and
         files VAT/PIT for the household per transaction** (current rule, to be checked against the decree) → the tax
         module must count that revenue as already taxed, never twice; stock is shared, so platforms need stock sync;
     (c) **in person** — counter, market stall/fair, sales visits, resellers (cộng tác viên bán hộ, with commission).
     MVP: (a) via Zalo OA + manual add, (c) counter. (b) is post-MVP as connectors, but the model (source, who
     collected the money, fee, who shipped, tax withheld) exists from day one; a platform payout file can be imported.

**Invoices**
12. Counter: the cash-register invoice is issued when the **seller presses "Thu tiền"** (a person's action, no
    separate approval; N-06 satisfied — no agent issues anything). B2B: the invoice is **proposed after delivery and
    issued by the owner** (OPC-09). Invoices follow the **delivered** quantity on partial delivery.
13. Household invoices are **hoá đơn bán hàng (mẫu số 2)**. An invoice with a tax code needs the household's digital
    certificate → "Chữ ký số" is a readiness item. Cancel/replace/adjust is not possible via API → guided flow on the
    provider's portal, then "ghi nhận kết quả". Timeout on issue → "Chưa rõ kết quả", never auto-retry.

**Delivery — flexible, one state chain**
14. Per order (default per customer): Khách tự lấy · Nhân viên của hộ (link to confirm, no account needed; photo +
    receiver) · Gửi nhà xe (manual, photo of the slip) · Đơn vị vận chuyển không kết nối (tracking no.) · Đơn vị vận
    chuyển có kết nối (status by connector; simulator in the demo). States: Chờ soạn → Đã soạn → Đã bàn giao → Đang
    giao → Đã giao / Giao một phần / Thất bại → Giao lại / Hoàn về kho.
15. COD in MVP: staff-collected cash is handed in and checked like closing a shift; carrier COD becomes a
    receivable from the carrier.

**Money out, tax, identity**
16. Money out (suppliers, refunds): OPC prepares, a **bank-app deeplink** opens with the details filled in, the owner
    presses send (N-06, N-07). No Pay Out / Payment Initiation.
17. Tax: OPC computes, drafts the return, shows readiness and evidence. **Paying tax always happens in eTax Mobile or a
    bank app**, then OPC records the receipt number (OPC-19/20/21, N-06; no third-party payment path). Filing inside
    OPC ("Chị ký và gửi") is shown only when a provider is proven; otherwise "Mở eTax" + photo of the acknowledgement.
    One screen supports both. **Q1.**
18. eKYC: Cas ID path + assisted path (OPC staff on site) + a web eKYC provider port (R-A2-02 "no app install").

**Control and onboarding**
19. Control Tower for the owner = **Cần xử lý, extended**: tabs Cần chị quyết · Đang chạy · Chờ kết nối · Lỗi · Xong
    hôm nay; a workflow detail (timeline labelled Trợ lý đề xuất · OPC kiểm tra · Chị duyệt · Kết nối) and an approval
    detail (problem · evidence · impact · proposal · who may approve · reason required · re-check after). Home shows
    one summary line. Technical views (retry policy, correlation id) stay in `console`. Screens: `approvals.html`, `--running`, `--error`, `--detail` (v4.2).
20. Roles: Chủ hộ · Người vận hành · Thu ngân · Kế toán (time-boxed) · Người giao (link only). Approval policy is per
    household with defaults: discount > 10 %, overdue or over-limit customer, selling reserved stock, stock adjustment,
    refund, B2B invoice, tax return.
21. Onboarding = current self-serve wizard + BA readiness: business model (mua về bán / tự chế biến / cả hai), base data
    (customers, suppliers, price lists, opening stock), connections, digital certificate, approval policy, then a
    **Readiness** screen (Chưa bắt đầu · Đang thiết lập · Bị chặn · Sẵn sàng có điều kiện · Sẵn sàng). OTP is skipped in the demo only.
22. Wording to users: "Mô phỏng" (not Simulated) · "đối chiếu" (not đối soát) · the four source labels in Vietnamese.

**Still open — needs CEO/BA (design proceeds on the default)**
- **Q1** CEO + BA: accept the change to UC-05 (tax paid outside OPC; in-OPC filing only with a proven provider).
- **Q2** Accountant: a household over 1 tỷ at the counter — cash-register invoice or invoice with a tax code? Default:
  cash-register invoice; both are supported per household.
- ~~Q3~~ decided (owner, 2026-10-04): the "Thu tiền" press is a person issuing the invoice (N-06). Setting "Cho phép
  phát hành hoá đơn tại quầy" per person: on by default for every seller role (Chủ hộ, Người vận hành, Thu ngân) because a
  cash-register invoice must be made at the sale; the owner can switch it off per person — that person's invoices then wait
  in Cần xử lý for the owner/manager. Every invoice records who pressed.
- ~~Q5~~ decided (owner, 2026-10-04): **Zalo OA** is the MVP chat channel (customers message the household's OA);
  manual add stays for every other source; platforms stay post-MVP with the model ready; B2B payment per order and
  by statement are both supported.
- ~~Q4~~ decided: design extends the BA demo data itself (prices, opening stock, Sunrise limit and debt, tax period, users); BA may review.

## 8. Connector categories (2026-10-04) — every category exists from day one; providers arrive phase by phase
Rule: the business flow talks to a **category**, never to a provider. Each category has the same contract in the UI:
states (Chưa kết nối · Đang kết nối · Hoạt động · Cần đăng nhập lại · Sắp hết hạn đồng ý · Lỗi · Tạm dừng · Mô phỏng),
data freshness, consent and its expiry, cost note, and a **manual path** ("Làm tay") so no flow is blocked when no
provider is connected. A household may connect several providers in one category (two bank accounts, several shops).
Surface (v5.1): **Kết nối → Việc OPC làm** — the 17 categories are grouped into 12 features the owner sees (Nhận tiền chuyển khoản = cat 1+2; Hoá đơn bán ra = 4; Chữ ký số = 8; Xác minh chủ hộ = 9; Nhận yêu cầu = 11; Báo tin = 14; Hoá đơn mua vào = 5; Giao hàng = 13; Bán trên sàn = 12; Kê khai và nộp thuế = 6+7; Sổ sách và xuất = 16+17; **Trả tiền nhà cung cấp = 3 (v6)**; 10 Tra cứu and 15 AI are inside other features / internal). Mapping and tiers: `tools/v4/capabilities.py`, `system/connector-catalog.md`. Readiness marks which features this household needs; Readiness marks which categories this household needs; failures show
in Cần xử lý → Chờ kết nối / Lỗi. Matches BA F13.01–F13.06. Architecture ports (ADR 0012) cover 1–10; 11–17 need ports.

| # | Category | OPC needs | Providers to evaluate (examples) | Phase 1 (proposed) | Manual path |
|---|---|---|---|---|---|
| 1 | Ngân hàng (tài khoản, giao dịch) | link the household's organisation account, transactions, balance, 180-day consent | Casso Cas; banks' open APIs (MB, BIDV, VietinBank…) | Casso (MB VietQR) | owner confirms in the bank app |
| 2 | Thu tiền | dynamic QR per order/invoice, virtual account per B2B customer, card POS, wallets | Casso QR Pay/VA, payOS, VNPAY, MoMo, ZaloPay, SmartPOS | Casso QR Pay | static QR, cash |
| 3 | Chi tiền | prefilled transfer the owner sends (suppliers, refunds) | bank deeplinks via Casso Deeplink / VietQR | Deeplink | copy account + amount |
| 4 | Hoá đơn bán ra | cash-register + invoices with a tax code, status, no duplicates | Hilo, X Invoice, S-Invoice, Bkav, VNPT, MISA meInvoice, EasyInvoice (direct or via Casso Invoice Hub) | Casso → Hilo (counter), X Invoice (B2B) | issue on the provider portal, record it |
| 5 | Hoá đơn mua vào, dữ liệu cổng thuế | inbound/outbound invoices for books | Casso GDT Hub | opt-in per household, after the legal check (N-15) | photo/PDF upload, OCR |
| 6 | Gửi tờ khai | file the return, get the acknowledgement | T-VAN: Casso TVAN, TS24, Thái Sơn, VNPT, Viettel | — (manual) | export file → eTax → photo of the acknowledgement |
| 7 | Nộp thuế | pay to the state budget, get the receipt | eTax Mobile deeplink; banks' NSNN payment | eTax Mobile deeplink | pay anywhere, enter the receipt number |
| 8 | Chữ ký số | remote signing for invoices with a code and returns | CAS CERT (Cas ID), VNPT SmartCA, Viettel MySign, MISA eSign, FPT.CA | open (Q) | provider's own app |
| 9 | Định danh (eKYC) | owner identity (chip ID + face) on web | Cas ID, VNPT eKYC, FPT.AI | Cas ID + assisted | OPC staff on site |
| 10 | Tra cứu | tax-code / industry / account-name lookup | Casso IDKit, X Invoice MST API, VietQR lookup | IDKit | type it in |
| 11 | Kênh trò chuyện | read requests, reply/confirm | Zalo OA, Messenger/Facebook Page, Instagram, TikTok messages, email inbox | Zalo OA | share/paste, photo, voice, type |
| 12 | Sàn & cửa hàng online | orders, payouts and fees, returns, stock sync, tax withheld | Shopee, TikTok Shop, Lazada, Haravan, Sapo, WooCommerce, ShopeeFood, GrabFood | — | import the payout file |
| 13 | Giao hàng | create shipment, status, COD reconciliation | GHN, GHTK, Viettel Post, J&T, Ahamove, Grab Express, Lalamove | simulator (demo) | own staff link, bus, tracking number |
| 14 | Thông báo gửi đi | to owner and customers | Zalo ZNS, SMS brandname, email, web push | ZNS + SMS fallback | — |
| 15 | Trí tuệ nhân tạo (đọc chữ, giọng nói, ảnh) | read requests, documents, receipts | per ADR 0010 (provider-agnostic) | per ADR 0010 | type it in |
| 16 | Xuất dữ liệu / kế toán | data portability (BRD §3.4), hand-off to an accountant | Excel/CSV, MISA/Fast import formats | Excel/CSV | — |
| 17 | Nhập dữ liệu nền | customers, suppliers, products, opening stock | Excel, Google Sheets, photo (AI) | Excel + photo | type it in |
Categories 15 is internal (no owner login) but appears under Dữ liệu & quyền riêng tư as a data processor.

# OPC — Design Brief (v1, 2026-10-02)

> **2026-10-04:** scope, users, demo data and business rules were updated after the BA docs — see `SCOPE-MVP.md` §7.
> Where this brief disagrees (counter as job #1, Cô Hai data, tax filed only on eTax), §7 wins.

Product: **OPC** ("Doanh nghiệp một người ứng dụng AI") — sales, payments, invoices, stock, books and tax
for Vietnamese household businesses (hộ kinh doanh). Architecture: `opc/docs/ARCHITECTURE.md`.
This phase: **web app `app`** (owner, staff, delegated accountant), desktop + phone browser. Native apps
come later and will reuse this design system. Own brand (no logo/colour yet); "by QNSC" endorsement only.

Output: 5–6 style tiles → 2–3 finalists rendered on **Home (Tổng quan)** and **Counter (Quầy bán hàng)** with
identical content → GATE.

## 1. Users
- **Owner** of a household business in the Gia Lai programme (coastal Quy Nhơn/Nhơn Lý, highlands Pleiku):
  dried seafood & specialties, tourism (homestay, boats, food), coffee/macadamia buying. Often 45–65,
  phone-first, Zalo daily, paper notebook for years, afraid of getting tax wrong.
- **Successor** (25–40, son/daughter) — runs the laptop at the counter, does invoices and tax. Primary web user.
- **Staff / family** selling at the counter. **Delegated accountant** managing several households.
- Motivation: 2026 self-declared tax; households > 1 tỷ/yr must issue e-invoices from a cash register;
  the province pays OPC per *activated* household. Trust and "not getting it wrong" beat delight.

## 2. Contexts
| Context | Device | Doing |
|---|---|---|
| Counter, tourist rush (weekend, summer, Tết) | Laptop 1366–1440 or tablet 1024; also phone browser 390 | Sell fast, take QR or cash, issue invoice automatically |
| Morning / quiet hours | Laptop or phone browser | Check money, match unmatched transfers, confirm hotel/restaurant orders, restock |
| Evening / month-end | Laptop | Books, tax estimate, filing preparation, consents and connections |
Network can be weak; bank/provider connections (via Casso) can lag or fail — the UI must show freshness.

## 3. Jobs, in priority order
1. **Sell at the counter fast** (mouse, keyboard, touch). Weight-based items (kg) are common. Payment by
   VietQR or cash; the cash-register e-invoice is issued automatically after payment.
2. **Know the money today and whether it is real**: received vs **pending verification** (bank webhooks
   are unsigned — a QR payment shows "chờ xác minh" until confirmed), cash vs transfer, receivables.
3. **Handle what needs me now**: verify payments, assign transfers without an order code, invoices without a
   tax-authority code, channel orders to confirm, low stock, connection/consent renewals, tax deadline.
4. **Keep books and tax right without being an accountant**: revenue vs 1 tỷ threshold, quarterly estimate.

Design consequence: **Home is a "needs-me-now + is-my-money-real" surface**, not a KPI wall. Counter
optimises the 4-line cart → QR → done loop and must make the payment state impossible to misread.

## 4. Hard constraints
- Vietnamese UI, full diacritics; fonts **must** include the Vietnamese subset
  (`~/.claude/skills/uiux-studio/library/fonts.md`); body line-height ≥ 1.4.
- Money `1.020.000 ₫` (dot thousands, symbol after), tabular figures; weights `0,5 kg` (comma decimal);
  dates `02/10/2026`, times `10:42`.
- Body ≥ 16px, meta ≥ 14px, nothing < 13px; contrast WCAG AA; status = colour + label (+ icon).
- Targets ≥ 44px; **Counter uses the touch context (≥ 56px)**.
- Responsive: 1440, 1280, 1024 **and 390 (phone browser)** — not a desktop squeezed: on 390 the Counter
  becomes product list + sticky cart bar → payment sheet; Home stacks needs-me-now first.
- Money states must be explicit: **Chờ khách chuyển → Đã nhận · chờ xác minh → Đã xác minh**; unmatched
  transfers never auto-assigned; invoice states **Chờ mã CQT → Có mã CQT / Lỗi / Chưa rõ kết quả**.
- Show data freshness of connections ("MB · cập nhật 2 phút trước"); offline/degraded banner pattern.
- AI assistant ("Trợ lý") is a plain, useful entry with suggested questions — never a sparkle hero.
- Keyboard on Counter: `/` search, `+`/`−` qty, `F9` charge, `Esc` cancel (shown as small kbd hints).

## 5. Anti-slop list
Copy of `references/anti-slop.md`, plus: green+gold "agriculture" palette by default; bank-app blue as the
brand by default; stock photos of smiling shopkeepers; Tết red/gold clichés; seafood/wave clip-art.

## 6. Detail checklist
`references/detail-checklist.md` + `references/content-checklist.md` + consistency section.

## 7. Screen content (identical across directions)

Household: **Hải sản khô Cô Hai** — thôn Lý Hưng, Nhơn Lý, Quy Nhơn, Gia Lai. Owner **Trần Thị Hai**;
signed-in user **Nguyễn Văn Phúc** (con, Quản lý). Verification L1. Clock: **Thứ Sáu, 02/10/2026, 10:45**.
Shift: **Ca sáng · mở 07:00 · Phúc**. Connections: **MB (qua Casso) · cập nhật 2 phút trước** ·
**Hoá đơn Hilo · hoạt động** · **Cổng thuế · chưa bật**. Notifications: 4 unread.

### 7.1 App shell
Nav: Tổng quan · **Quầy bán hàng** (primary) · Đơn hàng (3) · Tiền & đối soát (3) · Hoá đơn · Hàng hoá & kho ·
Khách hàng & công nợ · Sổ sách & thuế · Kết nối · Cài đặt. Global: household switcher (for accountants),
search `Tìm đơn, món, khách… /`, Trợ lý, notifications, user avatar "P".

### 7.2 Home — "Tổng quan"
- Title line: `Thứ Sáu, 02/10/2026` · `Ca sáng đang mở từ 07:00 · Phúc`
- Actions: **Mở quầy bán hàng** (primary), Tạo đơn, Ghi khoản chi.
- **Tiền hôm nay**: Doanh thu **8.460.000 ₫** · 23 đơn · +19% so với hôm qua (7.120.000 ₫).
  QR/chuyển khoản 5.940.000 ₫ (đã xác minh 4.560.000 ₫ · **chờ xác minh 1.380.000 ₫**) · Tiền mặt 2.520.000 ₫.
- **Cần xử lý** (urgency order, one action each):
  1. 2 khoản QR chờ xác minh — DH-1043 1.020.000 ₫ (10:42), DH-1041 360.000 ₫ (10:05) → `Đối chiếu`
  2. Chuyển khoản không có mã đơn — 2.150.000 ₫ từ NHA HANG BIEN DONG, 09:15, nội dung "TT HANG KHO T9";
     gợi ý: khớp công nợ Nhà hàng Biển Đông 2.150.000 ₫ → `Gán vào đơn`
  3. Đơn Zalo chờ xác nhận — Khách sạn Hải Âu: 3 kg cá cơm sấy, 2 kg tôm khô loại 1 · 3.420.000 ₫ · giao 15:00 → `Xác nhận`
  4. Hoá đơn 00000418 chưa có mã CQT sau 25 phút (640.000 ₫, Hilo chậm) → `Kiểm tra`
  5. Sắp hết — Mực khô loại 1 còn 3,2 kg (ngưỡng 5 kg) · Tôm khô loại 1 hũ 500 g còn 6 hũ → `Tạo phiếu nhập`
  6. Liên kết MB cần đồng ý lại trước 17/10/2026 (quy định 180 ngày) → `Gia hạn`
- **Thuế & ngưỡng**: Doanh thu 2026 **1.284.500.000 ₫** — đã vượt 1 tỷ ngày 14/08/2026 → đang dùng hoá đơn
  máy tính tiền (Hilo). Khai thuế quý III/2026: hạn **31/10/2026** (còn 29 ngày) · tạm tính **6.184.500 ₫**
  (doanh thu quý 412.300.000 ₫ × 1,5% — GTGT 1% + TNCN 0,5%, nhóm phân phối hàng hoá).
- **Doanh thu 7 ngày** (bars; today in progress): T7 26/9 9.820.000 · CN 11.240.000 · T2 6.310.000 ·
  T3 5.980.000 · T4 6.750.000 · T5 7.120.000 · T6 02/10 8.460.000 (đang bán). Tổng 55.680.000 ₫.
- **Công nợ phải thu**: 5.570.000 ₫ — Khách sạn Hải Âu 3.420.000 ₫ (đơn chờ) · Nhà hàng Biển Đông 2.150.000 ₫ (có thể đã trả, xem khoản 2).
- **Đơn gần đây** (table):
  | Mã | Giờ | Khách | Kênh | Món | Tổng | Thanh toán | Trạng thái |
  |---|---|---|---|---|---|---|---|
  | DH-1043 | 10:42 | Khách lẻ | Tại quầy | 4 | 1.020.000 ₫ | QR | Chờ xác minh |
  | DH-1042 | 10:31 | Khách lẻ | Tại quầy | 2 | 245.000 ₫ | Tiền mặt | Hoàn tất · HĐ có mã |
  | DH-1041 | 10:05 | Chị Thu | Shopee | 3 | 360.000 ₫ | QR | Chờ xác minh |
  | DH-1040 | 09:48 | Khách sạn Hải Âu | Zalo | 2 | 3.420.000 ₫ | Công nợ | Chờ xác nhận |
  | DH-1039 | 09:20 | Khách lẻ | Tại quầy | 1 | 95.000 ₫ | Tiền mặt | Hoàn tất · HĐ có mã |
  | DH-1038 | 08:55 | Nhà hàng Biển Đông | Điện thoại | 5 | 2.150.000 ₫ | Chuyển khoản | Chờ gán tiền |
- **Trợ lý**: "Tuần này món nào bán chạy nhất?" · "Quý III phải nộp thuế bao nhiêu?"

### 7.3 Counter — "Quầy bán hàng"
- Header: `Ca sáng · mở 07:00 · Phúc` · connection freshness · `Đóng ca`.
- Search `Tìm món hoặc quét mã… /`; categories: Tất cả · Mực & cá · Tôm & ruốc · Đặc sản · Quà tặng.
- Products (name · price · stock hint · in-cart):
  Mực khô loại 1 — 1.250.000 ₫/kg · còn 3,2 kg · **trong giỏ 0,5 kg** · Cá thu một nắng — 380.000 ₫/kg ·
  Cá bò một nắng — 320.000 ₫/kg · Cá cơm sấy giòn hũ 250 g — 95.000 ₫ · **×2** · Tôm khô loại 1 hũ 500 g —
  420.000 ₫ · còn 6 · Ruốc biển hũ 200 g — 65.000 ₫ · Mực rim me hũ 300 g — 120.000 ₫ · Chả cá Quy Nhơn
  500 g — 85.000 ₫ · **×1** · Nem chợ Huyện (chục) — 50.000 ₫ · Bánh tráng nước dừa (xấp 10) — 40.000 ₫ ·
  **×3** · Muối ớt xanh hũ — 30.000 ₫ · Túi giấy quà tặng — 5.000 ₫.
- Ticket `DH-1043` · Khách lẻ (change → search/MST lookup):
  Mực khô loại 1 0,5 kg × 1.250.000 = 625.000 · Cá cơm sấy giòn ×2 = 190.000 · Bánh tráng nước dừa ×3 =
  120.000 · Chả cá Quy Nhơn ×1 = 85.000 → **Khách phải trả 1.020.000 ₫** (HKD sales invoice: no VAT line).
- Payment: **QR chuyển khoản** (selected) · Tiền mặt · Công nợ. QR state shown: VietQR MB, amount 1.020.000 ₫,
  mã đơn DH1043, **"Đang chờ khách chuyển…"**; next state copy: "Đã nhận 1.020.000 ₫ · chờ xác minh — giao
  hàng được (dưới mức 2.000.000 ₫ bạn đặt)". Cash alternative: Khách đưa quick amounts + Tiền thối.
- Invoice: "Hoá đơn máy tính tiền — tự phát hành sau khi thu tiền" (mandatory, cannot be turned off) ·
  toggle "Khách lấy hoá đơn công ty" (MST lookup) · toggle "In phiếu".
- Primary: **Xác nhận đã thu 1.020.000 ₫** is disabled while QR is pending (auto-advances on payment);
  secondary: `Đổi sang tiền mặt`, `Lưu tạm`, `Huỷ đơn`. Kbd: `/` `+` `−` `F9` `Esc`.
- Phone 390: product list + sticky bar "4 món · 1.020.000 ₫ · Thu tiền" → full-height payment sheet.

## 8. Verified fonts
See `library/fonts.md` (Vietnamese subset checked 2026-09-30). Do not use: DM Sans, Instrument Sans/Serif,
Figtree, Sora, Schibsted Grotesk, Red Hat Display, Bodoni Moda.


## 9. Directions (DNA recombination — each mixes ≥3 sources, one local element, one wildcard)

### A — "Sổ Tay" (`a-so-tay`)
- Idea: the household's paper notebook, made precise and trustworthy
- Attributes: metaphor: paper ledger (users' own world) · layout: ruled lines + columns, no cards (Stripe restraint) · type: serif display for money (Source Serif 4 / Newsreader, from Square's editorial serif) + humanist sans UI (IBM Plex Sans / Public Sans) · colour: near-white paper, blue-black ink, ONE vermilion 'con dấu' seal accent (local) — errors use a different orange/brown + icon · shape: 0–4px radius, hairlines · density: medium
- Signature move: the verification STAMP: a verified payment gets a seal-like stamp 'ĐÃ XÁC MINH'; pending shows a dashed empty stamp outline — money truth is visible at a glance
- Risk: can feel formal/old-fashioned; serif money must stay legible at 16px
- Anchor refs: refs/square-retail.png, refs/stripe.png

### B — "Bảng Giá Chợ" (`b-bang-gia`)
- Idea: the market price board — bold, big, readable from a metre away
- Attributes: metaphor: hand-painted market price boards (local) · layout: chunky blocks and zones, big product tiles (Shopify POS / Toast POS hardware UIs) · type: heavy condensed display for prices (Big Shoulders Display or Barlow Condensed — both Vietnamese) + Be Vietnam Pro body · colour: ink black + white + ONE saturated warm accent that is not red (e.g. marigold, sea-salt cyan — your call) · shape: 12–16px radius, 2px strokes · density: low, large targets
- Signature move: the PRICE TAG component: products and money amounts sit on tag shapes (notch + hole) like real shop tags; the running total is the biggest tag
- Risk: can look loud/childish; must stay professional for tax and invoices
- Anchor refs: refs/shopify-pos.png, refs/kiotviet.png

### C — "Biển Lặng" (`c-bien-lang`)
- Idea: a calm, precise professional tool with coastal warmth
- Attributes: metaphor: calm sea / nautical chart · layout: quiet left sidebar, action row, cards with hairline borders (Mercury demo, Linear restraint) · type: neutral grotesk (Onest or Hanken Grotesk) + mono figures (Geist Mono or JetBrains Mono) · colour: warm sand/stone neutrals, deep sea-teal ink, one coral accent used sparingly (local coast) · shape: 10–12px radius, 1px borders · density: medium-compact
- Signature move: the TIDE LINE: a thin 3-step progression line (Chờ chuyển → Đã nhận → Đã xác minh) shown wherever money appears, like a tide marker; chart gridlines borrow nautical-chart contour hairlines
- Risk: closest to 'good generic SaaS' — must earn identity through the tide line and colour
- Anchor refs: refs/mercury-demo.png, refs/linear.png

### D — "Biên Lai" (`d-bien-lai`)
- Idea: everything is a receipt — the thing every shop already trusts
- Attributes: metaphor: thermal receipt / POS printout (local: hoá đơn) · layout: narrow receipt strips with perforated edges and tear-off stubs, stacked like a spike of receipts; monospaced columns · type: mono for figures and codes (IBM Plex Mono or JetBrains Mono) + a sturdy sans for text (Public Sans or Work Sans) · colour: thermal-paper off-white, print black, ONE faded thermal-blue or purple-ink accent · shape: square edges, zigzag perforations · density: medium
- Signature move: the RECEIPT SLIP: each money/invoice item is a slip with a stub; status is a printed rubber-stamp line ('ĐÃ XÁC MINH 10:43'); the to-do list is a spike of slips
- Risk: monospace everywhere hurts readability — mono only for figures/codes
- Anchor refs: refs/square-retail.png, refs/payos.vn.png

### E — "Trò Chuyện" (`e-tro-chuyen`)
- Idea: the app talks to you like a helpful family member
- Attributes: metaphor: a conversation (Zalo habits — local) · layout: plain-language sentence summaries above numbers; to-dos as message cards with quick-reply buttons; assistant woven in, not a separate hero · type: bold friendly sans (Bricolage Grotesque or Plus Jakarta Sans) with very large headline numbers (Wise) · colour: black text, white, ONE fresh bright accent for money (lime/leaf from Wise — not agriculture green+gold) · shape: 16–20px radius, soft · density: low
- Signature move: SENTENCE-FIRST numbers: every block starts with a sentence ('Hôm nay nhà mình bán được 8,46 triệu, hơn hôm qua 1,34 triệu') before the figures; quick-reply chips act on to-dos
- Risk: challenges the 'serious tool' taste; risk of feeling casual for tax
- Anchor refs: refs/wise.com-vn.png, refs/payos.vn.png

### F — "Biển Chỉ Dẫn" (`f-chi-dan`)
- Idea: airport/expressway wayfinding — you always know what to do next
- Attributes: metaphor: transit wayfinding signage (wildcard domain) · layout: strong panels, numbered 'lanes' by urgency (1, 2, 3 as huge numerals), arrow-led actions, pictograms · type: DIN-like grotesk (Barlow or Archivo) for headers/numbers + Barlow/Public Sans body · colour: high contrast — black/near-black panels with signal yellow for 'act now', white text; local touch from Vietnamese expressway green/blue signs used for secondary categories · shape: 4–6px radius, rectangular panels · density: medium
- Signature move: URGENCY LANES: to-dos are numbered lanes with big numerals and an arrow action, like gate signs; money states use pictogram + word, readable from across the counter
- Risk: dark panels can feel heavy in daylight; keep the canvas light
- Anchor refs: refs/linear.png (structure only); wayfinding from your knowledge


## 10. Feature content v1.1 (2026-10-02) — states + Tiền & đối soát, Đơn hàng, Hoá đơn
All numbers reconcile with §7: doanh thu 8.460.000 ₫ = QR đã xác minh 4.560.000 + QR chờ xác minh 1.380.000 + tiền mặt 2.520.000.

### 10.1 Today's 23 orders (DH-1021 … DH-1043)
| Mã | Giờ | Khách | Kênh | Món | Tổng | Thanh toán | Trạng thái | Hoá đơn |
|---|---|---|---|---|---|---|---|---|
| DH-1043 | 10:42 | Khách lẻ | Tại quầy | 4 | 1.020.000 | QR | Chờ xác minh (nhận 10:44) | — (phát hành khi xác minh) |
| DH-1042 | 10:31 | Khách lẻ | Tại quầy | 2 | 245.000 | Tiền mặt | Hoàn tất | 00000421 · có mã |
| DH-1041 | 10:05 | Chị Thu | Shopee | 3 | 360.000 | QR | Chờ xác minh **quá 30 phút** | — |
| DH-1040 | 09:48 | Khách sạn Hải Âu | Zalo | 2 | 3.420.000 | Công nợ | Chờ xác nhận (giao 15:00) | — |
| DH-1039 | 09:20 | Khách lẻ | Tại quầy | 1 | 95.000 | Tiền mặt | Hoàn tất | 00000420 · có mã |
| DH-1038 | 08:55 | Nhà hàng Biển Đông | Điện thoại | 5 | 2.150.000 | Chuyển khoản | Chờ gán tiền | — |
| DH-1037 | 08:41 | Khách lẻ | Tại quầy | 2 | 195.000 | Tiền mặt | Hoàn tất | 00000419 · có mã |
| DH-1036 | 08:33 | Anh Tuấn | Tại quầy | 3 | 640.000 | QR | Hoàn tất | **00000418 · chờ mã CQT** (Hilo lỗi, gửi lại 10:20) |
| DH-1035 | 08:20 | Khách lẻ | Tại quầy | 2 | 1.250.000 | QR | Hoàn tất | 00000417 · có mã |
| DH-1034 | 08:12 | Khách lẻ | Tại quầy | 1 | 40.000 | Tiền mặt | Hoàn tất | 00000416 |
| DH-1033 | 08:09 | Khách lẻ | Tại quầy | 2 | 160.000 | Tiền mặt | Hoàn tất | 00000415 |
| DH-1032 | 08:03 | Khách lẻ | Tại quầy | 1 | 95.000 | Tiền mặt | Hoàn tất | 00000414 |
| DH-1031 | 07:58 | Khách lẻ | Tại quầy | 3 | 230.000 | Tiền mặt | Hoàn tất | 00000413 |
| DH-1030 | 07:52 | Chị Mai | Tại quầy | 4 | 980.000 | QR | Hoàn tất | 00000412 |
| DH-1029 | 07:46 | Khách lẻ | Tại quầy | 1 | 50.000 | Tiền mặt | Hoàn tất | 00000411 |
| DH-1028 | 07:40 | Khách lẻ | Tại quầy | 1 | 120.000 | Tiền mặt | Hoàn tất | 00000410 |
| DH-1027 | 07:31 | Công ty TNHH Du lịch Biển Xanh | Tại quầy | 6 | 1.690.000 | QR | Hoàn tất | 00000409 · **HĐ công ty**, MST 4101523687 |
| DH-1026 | 07:29 | Khách lẻ | Tại quầy | 1 | 380.000 | Tiền mặt | Hoàn tất | 00000408 |
| DH-1025 | 07:26 | Khách lẻ | Tại quầy | 1 | 65.000 | Tiền mặt | Hoàn tất | 00000407 |
| DH-1024 | 07:22 | Khách lẻ | Tại quầy | 2 | 190.000 | Tiền mặt | Hoàn tất | 00000406 |
| DH-1023 | 07:18 | Khách lẻ | Tại quầy | 1 | 420.000 | Tiền mặt | Hoàn tất | 00000405 |
| DH-1022 | 07:12 | Khách lẻ | Tại quầy | 1 | 85.000 | Tiền mặt | Hoàn tất | 00000404 |
| DH-1021 | 07:05 | Khách lẻ | Tại quầy | 2 | 150.000 | Tiền mặt | Hoàn tất | 00000403 |
Totals: 23 đơn · đã thu 8.460.000 ₫ (QR 5.940.000 incl. 1.380.000 chờ xác minh · tiền mặt 2.520.000, 15 đơn) · chưa thu 5.570.000 ₫ (DH-1038, DH-1040).
Channels: Tại quầy 20 · Zalo 1 · Shopee 1 · Điện thoại 1. Nav badge "Đơn hàng (3)" = Cần xem: DH-1041 (QR quá 30 phút), DH-1040 (chờ xác nhận), DH-1038 (chờ gán tiền).

### 10.2 Tiền & đối soát — MB account via Casso, today
Header facts: Số dư MB **48.215.000 ₫** · cập nhật 10:43 · TK 0123 4567 89 · chủ TK HO KINH DOANH TRAN THI HAI.
Bank credits today (7):
| Giờ | Người chuyển (raw) | Nội dung (raw) | Số tiền | Khớp với | Trạng thái |
|---|---|---|---|---|---|
| 10:44 | NGUYEN VAN HUNG | DH1043 | 1.020.000 | DH-1043 | Chờ xác minh (Casso báo 10:44, đang đối chiếu sao kê, thường 1–3 phút) |
| 10:05 | TRAN THI THU | DH1041 SHOPEE | 360.000 | DH-1041 | Chờ xác minh **quá 30 phút** → kiểm tra trong app MB |
| 09:15 | NHA HANG BIEN DONG | TT HANG KHO T9 | 2.150.000 | — | **Chưa gán** (không có mã đơn) |
| 08:34 | LE MINH TUAN | DH1036 | 640.000 | DH-1036 | Đã xác minh 08:35 |
| 08:21 | PHAM QUOC BAO | DH1035 | 1.250.000 | DH-1035 | Đã xác minh 08:22 |
| 07:53 | VO THI MAI | DH1030 | 980.000 | DH-1030 | Đã xác minh 07:54 |
| 07:32 | CTY TNHH DU LICH BIEN XANH | DH1027 BIEN XANH | 1.690.000 | DH-1027 | Đã xác minh 07:33 |
Tabs: Cần xem (3) · Chờ xác minh (2) · Chưa gán (1) · Đã khớp (4) · Tất cả (7). Cash card: Tiền mặt trong ca 2.520.000 ₫ · 15 đơn · "Đếm tiền cuối ca".
Explain once on the page: "Chờ xác minh = Casso đã báo có tiền; OPC đang đối chiếu với sao kê MB. Đã xác minh = khớp sao kê."

### 10.3 Gán vào đơn (dialog over Tiền & đối soát) — for the 09:15 credit 2.150.000 ₫
Facts: MB · NHA HANG BIEN DONG · nội dung "TT HANG KHO T9" · 09:15 · mã GD FT26275091542.
Options (radio cards, none committed until the button):
1. **DH-1038 · Nhà hàng Biển Đông** — đơn điện thoại 08:55 · 5 món · 2.150.000 ₫ · ✓ đúng số tiền · ✓ đúng tên khách · ✓ chuyển sau khi đặt 20 phút · ✗ nội dung ghi "T9" (tháng 9) → tag "Gợi ý", pre-selected? **No** — selected by the user (show as checked in the drawn state).
2. Ghi có cho Nhà hàng Biển Đông (trả trước đơn sau) — số dư có 2.150.000 ₫.
3. Tiền khác, không phải bán hàng — ghi vào sổ là thu khác (không tính doanh thu).
4. (disabled) DH-1040 · Khách sạn Hải Âu · 3.420.000 ₫ — ✗ khác số tiền · ✗ khác tên.
Footer note: "Gán xong: DH-1038 hoàn tất, phát hành hoá đơn 00000423, công nợ Biển Đông còn 0 ₫." Buttons: Huỷ · **Gán vào DH-1038** (act).

### 10.4 Hoá đơn — cash-register e-invoices (Hilo via Casso)
Facts: Hoá đơn máy tính tiền · ký hiệu **2C26MCH** · Hilo · hoạt động · Tháng 10/2026: 19 hoá đơn · 7.080.000 ₫ (= tiền đã xác minh + tiền mặt).
Tabs: Cần xem (1) · Chờ mã CQT (1) · Có mã (18) · Lỗi (0) · Tất cả (19).
Rows: 00000421 (DH-1042, 10:31) … 00000403 (DH-1021, 07:05), numbers/amounts per 10.1. Mã CQT format example: `M1-26-QN7K2-00000000421`. 00000418 (DH-1036, 640.000 ₫, Anh Tuấn): **Chờ mã CQT** — Hilo báo lỗi 08:34, OPC gửi lại 10:20, chờ 25 phút → actions Gửi lại · Xem. 00000409 = HĐ công ty (Công ty TNHH Du lịch Biển Xanh, MST 4101523687).
Note under the banner: "Hoá đơn chờ mã vẫn đưa khách được; mã CQT sẽ gắn vào khi Hilo trả về."

### 10.5 Counter states (desktop 1440/1280/1024, same cart DH-1043 = 1.020.000 ₫ unless noted)
- **received**: QR status "Đã nhận 1.020.000 ₫ lúc 10:44 · chờ xác minh" (pend); ladder current = station 2; caption "Giao hàng được — đơn dưới mức 2.000.000 ₫ bạn đặt. OPC tự xác nhận khi MB khớp sao kê (thường 1–3 phút)."; confirm still locked; the one act button: **Giao hàng · bán đơn tiếp** (N) — the pending order moves to Tiền & đối soát.
- **verified** (10:47): QR status "Đã xác minh 10:47 · MB"; ladder station 3 current (solid green); confirm `--done` "Đã xác minh 1.020.000 ₫ · đang in phiếu"; invoice line "Hoá đơn 00000422 · chờ mã CQT" (sign pend → expected within a minute); steppers disabled; act **Đơn mới DH-1044** (N).
- **cash**: method Tiền mặt; c-field--money "Khách đưa" 1.100.000; quick amounts 1.020.000 (đủ) · 1.050.000 · 1.100.000 · 1.200.000 · 1.500.000 · 2.000.000; c-change "Tiền thối 80.000 ₫"; confirm enabled (act) "Đã thu 1.020.000 ₫ tiền mặt · thối 80.000 ₫" F9.
- **offline** (bank link down): c-banner--err in the pay column "Mất kết nối MB (qua Casso) lúc 10:45 — QR tạm tắt. Thu tiền mặt hoặc ghi công nợ; OPC thử lại mỗi phút." QR option aria-disabled "QR tạm tắt", Tiền mặt selected (same cash fields as above, Khách đưa empty, hint "Gõ số tiền khách đưa"); header connection shows MB as error.
- **empty**: new order DH-1044, no lines; ticket shows c-empty "Chưa có món — chọn món bên trái hoặc quét mã"; total 0 ₫; pay column: method row visible, QR area c-empty--flush "Mã QR hiện khi giỏ có món"; confirm locked reason "Thêm món để thu tiền"; no product tile has data-incart.
- **phone sheets**: counter--payment--received and counter--payment--verified = the 390 sheet with the same changes.

### 10.6 Home states
- **offline**: c-banner--err at the top of content "Mất kết nối MB (qua Casso) lúc 10:45 · Tiền QR mới sẽ hiện khi có lại kết nối. Vẫn bán được bằng tiền mặt; OPC thử lại mỗi phút." [Thử lại ngay]. Money hero connection → "số liệu đến 10:44" (one statement, no repeat of the banner); QR figures labelled "đến 10:44"; nav-foot MB connection err.
- **first-run** (new household, nothing sold yet): title "Chào chị Hai — còn 3 bước để bán hàng với OPC". Lanes as setup steps: ✓ Xác minh chủ hộ (L1, xong 01/10/2026, `--done`) · **1 Liên kết tài khoản MB để nhận tiền QR** (now) [Liên kết ngân hàng] · 2 Thêm hàng hoá — 0 món [Thêm món] [Nhập từ Excel] · 3 Kết nối hoá đơn điện tử (Hilo) [Kết nối]. Money card: c-empty "Chưa có tiền hôm nay — bán đơn đầu tiên ở Quầy sau khi thêm hàng." Tax card: "Nhập doanh thu năm 2026 đến nay để OPC tính ngưỡng 1 tỷ" [Nhập doanh thu]. No orders/7-day/debt cards. Badges in nav: none.

## 11. Onboarding v1.3 (2026-10-02) — self-serve on phone + assisted, AI only for hard steps
**Who:** Trần Thị Hai, 58, registers on her own Android phone (Chrome, 390×844), reading glasses, uses Zalo daily,
has never filled a web form alone. Her son Phúc may help remotely. Pilot field staff: **Nguyễn Thị Lan — Tổ hỗ trợ
OPC xã Nhơn Lý** (Zalo 0905 112 233). Support: "Zalo OPC Gia Lai".
**Principles (design consequences):** one task per screen; title says the task in plain words; at most 2 inputs
per screen; big primary at the bottom (thumb); "Bước n/6" + segment bar; every screen has **"?" Hỏi** (help sheet)
and a way to a human (Gọi chị Lan / Nhắn Zalo / Nhờ người thân làm giúp — sends a link); "Để sau" wherever a step
is not blocking; progress is saved after every step ("Đã lưu — làm tiếp lúc nào cũng được"); no jargon (no "eKYC",
"OTP", "API": say "mã xác nhận", "xác minh chủ hộ"); explain WHY before asking for something sensitive.
AI never acts alone: it reads/suggests, the owner reviews, uncertain values are marked "AI chưa chắc — kiểm tra".

Steps: 1 Số điện thoại · 2 Thông tin hộ · 3 Xác minh chủ hộ · 4 Ngân hàng · 5 Hàng hoá · 6 Hoá đơn → bán thử → xong.

### 11.1 Screens and content (phone 390 first; desktop shows the same column centred, max 560px)
1. **onboard-welcome** — OPC by QNSC mark; title "Bán hàng, nhận tiền, làm hoá đơn — trên một điện thoại";
   3 lines with pictograms: "Thu tiền QR, biết ngay tiền thật hay chưa" · "Hoá đơn tự làm khi bán" · "Thuế tự tính
   theo quý"; "Khoảng 15 phút · làm dở vẫn lưu". Primary **Bắt đầu**; secondary "Đã có tài khoản · Đăng nhập";
   card "Có nhân viên OPC bên cạnh? **Làm cùng nhân viên**". Footer: "Cần giúp? Nhắn Zalo OPC Gia Lai".
2. **onboard-phone** (Bước 1/6) — "Số điện thoại của chị/anh"; field (tel, big) value `0905 812 347`; hint "OPC gửi
   mã xác nhận qua Zalo. Không mất phí."; primary **Gửi mã qua Zalo**.
3. **onboard-otp** (1/6) — "Nhập mã 6 số OPC vừa gửi qua Zalo"; 6 boxes `4 8 2 · 9 1 _` (5 filled, focus on 6th);
   "Gửi lại sau 0:42"; link "Không nhận được? Gửi qua tin nhắn SMS"; mini note "Mở Zalo → tin nhắn từ OPC Gia Lai".
4. **onboard-household** (2/6) — "Thông tin hộ kinh doanh"; field "Mã số thuế của hộ" `4101678912` with result card
   (c-kv): Tên trên giấy phép **HỘ KINH DOANH TRẦN THỊ HAI** · Địa chỉ thôn Lý Hưng, Nhơn Lý, Quy Nhơn, Gia Lai ·
   Ngành bán lẻ thực phẩm · source "Cổng thuế · tra lúc 10:02"; field "Tên hiển thị cho khách" `Hải sản khô Cô Hai`;
   ngành chips (one choice): **Hải sản khô** · Tạp hoá · Ăn uống · Nông sản · Khác; link "Chưa có mã số thuế?".
5. **onboard-verify** (3/6) — "Xác minh chủ hộ"; why (c-say): "Để tiền QR chỉ vào đúng tài khoản của chị, và hoá
   đơn đúng tên hộ."; 3 option cards with pictogram: (a) **Chụp CCCD và khuôn mặt** — khoảng 2 phút, trên điện thoại
   này · tag "Nhanh nhất" (checked); (b) **Nhân viên OPC xác minh tại quầy** — hẹn chị Lan · Thứ Bảy 03/10/2026, 8:00;
   (c) **Dùng app Cas ID đọc chip CCCD** — chắc chắn nhất · cần thêm một máy (laptop) để quét mã. Privacy note
   (c-banner--ok style is not right — use c-kv/c-say): "OPC không lưu ảnh khuôn mặt. Chỉ lưu họ tên và số CCCD (mã hoá)."
6. **onboard-verify--camera** (3/6) — camera view (dark viewfinder is allowed here) with card-shaped frame
   (corners), step chips "Mặt trước · Mặt sau · Khuôn mặt" (1 of 3), hint "Đặt CCCD nằm gọn trong khung, đủ sáng,
   không loá"; shutter button; "Chụp lại" disabled; small "Đang dùng camera sau". (Vendor SDK draws the real camera;
   this is the OPC frame around it.)
7. **onboard-bank** (4/6) — "Liên kết tài khoản MB để nhận tiền QR"; 3 facts with ✓: "OPC chỉ thấy tiền vào, không
   chuyển tiền đi được" · "Kết nối qua Casso — đối tác kết nối ngân hàng của OPC" (do not claim licences we have not verified) · "Ngân hàng sẽ hỏi chị đồng ý chia sẻ, mỗi 180 ngày hỏi lại một lần"; primary **Mở trang liên
   kết MB** (opens Casso hosted page); secondary "Ngân hàng khác"; "Để sau (chưa nhận được tiền QR)".
8. **onboard-bank--done** (4/6) — success: c-banner--ok "Đã liên kết MB"; c-kv: Tài khoản 0123 4567 89 · Chủ tài
   khoản HO KINH DOANH TRAN THI HAI · **✓ Tên khớp với chủ hộ đã xác minh**; primary **Tiếp tục**.
9. **onboard-products** (5/6) — "Thêm hàng hoá chị bán"; 4 big option cards: **Chụp bảng giá** — AI đọc giúp,
   chị kiểm tra lại (tag "Dễ nhất", checked) · **Nói tên và giá** — ví dụ "mực khô một triệu hai trăm năm mươi một
   ký" · **Chọn từ mẫu Hải sản khô** — 24 món hay bán, sửa giá cho đúng · **Nhập từ Excel** — trên máy tính; "Để sau".
10. **onboard-products--review** (5/6) — "AI đọc được 9 món — chị kiểm tra giá trước khi lưu"; photo thumbnail
    "bảng giá viết tay · chụp 10:12"; list of 9 rows (name · price · unit), each editable: Mực khô loại 1
    1.250.000/kg · Cá thu một nắng 380.000/kg · **Cá bò một nắng 3?0.000/kg → field shows 320.000 with "AI chưa chắc
    — kiểm tra"** · Cá cơm sấy giòn hũ 250 g 95.000/hũ · Tôm khô loại 1 hũ 500 g 420.000/hũ · Ruốc biển hũ 200 g
    65.000/hũ · Mực rim me hũ 300 g 120.000/hũ · Chả cá Quy Nhơn 500 g 85.000/cái · **Nem chợ Huyện 50.000 / đơn vị
    "chục?" — AI chưa chắc**; summary "7 món chắc chắn · 2 món cần kiểm tra"; primary **Lưu 9 món** (stays enabled;
    unsure ones saved as entered); secondary "Chụp thêm ảnh".
11. **onboard-invoice** (6/6) — "Hoá đơn điện tử"; c-say "Hộ có doanh thu trên 1 tỷ/năm phải xuất hoá đơn điện tử
    từ máy tính tiền. OPC làm tự động mỗi khi bán."; question as 2 option cards: **Doanh thu năm nay trên 1 tỷ** →
    kết nối Hilo (qua Casso) ngay · **Dưới 1 tỷ** → để sau, OPC nhắc khi gần tới 1 tỷ; primary **Kết nối hoá đơn**.
12. **onboard-firstsale** — the counter (phone) with a coach mark: spotlight on "Mực khô loại 1" row + bubble
    "Bán thử · 1/3 — Chạm vào một món để thêm vào giỏ. Đơn bán thử không tính doanh thu." [Tiếp] · "Bỏ qua hướng dẫn".
13. **onboard-done** — "Xong! Hải sản khô Cô Hai đã sẵn sàng bán hàng"; checklist (c-lane--done ×5 with dates);
    "Nên làm thêm" (2 normal lanes): Mời con/nhân viên cùng dùng [Mời] · Đặt mức giao hàng khi tiền chờ xác minh
    (mặc định 2.000.000 ₫) [Đặt]; primary **Mở quầy bán hàng**.
14. **onboard-help** (sheet over onboard-products) — "Hỏi về bước này"; suggested questions (chips): "Bảng giá viết
    tay có đọc được không?" (selected) · "Sai giá thì sửa ở đâu?" · "Có mất phí không?"; AI answer card: label
    "Trợ lý OPC · trả lời tự động" — "Đọc được chữ viết tay rõ ràng. Món nào AI chưa chắc sẽ có khung xanh nét đứt để
    chị kiểm tra. Chị luôn sửa được giá sau ở mục Hàng hoá."; "Câu trả lời có giúp được không? Có · Không"; human
    block: **Gọi chị Lan** (hỗ trợ xã Nhơn Lý) · Nhắn Zalo OPC Gia Lai · **Nhờ người thân làm giúp** (gửi đường link
    qua Zalo; người thân làm xong, chị chỉ xác nhận).
15. **onboard-assisted** (desktop 1440, staff laptop) — "Hỗ trợ đăng ký · Hải sản khô Cô Hai"; staff line "Nguyễn
    Thị Lan · Tổ hỗ trợ OPC Nhơn Lý · mọi thao tác được ghi lại"; left: step checklist (1–2 done, 3 now, 4–6 next);
    right: "Xác minh chủ hộ bằng chip CCCD" — QR for Cas ID (use qr-demo.svg), instructions for chị Hai "Mở app Cas
    ID → Quét mã → Đặt CCCD sau điện thoại", status c-qr__status "Đang chờ chị Hai quét…" (wait); secondary
    "Xác minh bằng giấy tờ tại chỗ (nhân viên đối chiếu)"; note "Mã hết hạn sau 4:32".

## 12. List tools v1.4 (2026-10-02) — search, date range, filters, sort, pagination
Applies to Đơn hàng (owner) and Hoá đơn (accountant view). Data from §10.1/§10.4 plus earlier days:
7 ngày (26/9–02/10): 168 đơn · đã thu 55.680.000 ₫ (matches the 7-day card). Tháng 9/2026: 642 đơn.
1. **orders.html (update)** — replace the current filter row with `r-listbar`: search "Tìm mã đơn, khách, SĐT…" ·
   date preset c-seg **Hôm nay** (selected) · 7 ngày · Tháng này · Tự chọn · `Lọc` button · sort menu button "Mới nhất".
   No chips (nothing filtered). Keep tabs and table as is.
2. **orders--filtered.html** — date "7 ngày" + filters Kênh: Zalo, Shopee + Thanh toán: Chưa thu → chips row
   "Thời gian: 26/9 – 02/10 ×" · "Kênh: Zalo, Shopee ×" · "Chưa thu ×" · Xoá lọc · result "4 đơn · 9.870.000 ₫".
   Rows (4): DH-1040 02/10 09:48 Khách sạn Hải Âu · Zalo · 3.420.000 · Công nợ · Chờ xác nhận ·
   DH-0987 01/10 16:20 Chị Ngọc · Shopee · 540.000 · QR · Chờ khách chuyển · DH-0911 29/9 11:05 Nhà nghỉ Biển Xanh ·
   Zalo · 2.760.000 · Công nợ · Chờ thanh toán (hẹn 05/10) · DH-0866 27/9 08:40 Khách sạn Hải Âu · Zalo · 3.150.000 ·
   Công nợ · **Quá hạn 2 ngày**. Sum 9.870.000. Tab "Tất cả" selected (filters drive the list). Lọc button shows count 3.
3. **orders--filters.html** — filter dialog open over orders (desktop dialog / phone full screen): groups
   Thời gian (Hôm nay · 7 ngày ✓ · Tháng này · Tự chọn) · Kênh (Tại quầy · Zalo ✓ · Shopee ✓ · Điện thoại) ·
   Thanh toán (Đã thu · Chờ xác minh · Chưa thu ✓) · Trạng thái đơn (Chờ xác nhận · Hoàn tất · Đã huỷ) · Hoá đơn
   (Có mã · Chờ mã · Chưa có). Footer: "Xoá lọc" · **Xem 4 đơn** (act, live count).
4. **orders--daterange.html** — "Tự chọn" open: c-dialog "Chọn khoảng ngày" with c-cal Tháng 9/2026, start 26/9,
   end 02/10 (today), future disabled; quick row "Từ 26/09/2026 → Đến 02/10/2026"; footer Huỷ · **Áp dụng** (act).
5. **orders--search.html** — query "hải âu" typed; suggestions c-menu: Khách: Khách sạn Hải Âu (8 đơn · công nợ
   3.420.000 ₫) · Đơn: DH-1040 (02/10 · 3.420.000 ₫), DH-0866 (27/9 · 3.150.000 ₫) · "Tìm “hải âu” trong tất cả
   thời gian". Matched text highlighted with `mark`.
6. **orders--noresult.html** — query "DH-0999", date "Hôm nay": c-empty "Không có đơn DH-0999 hôm nay" body "Đơn có
   thể ở ngày khác." actions **Tìm trong tất cả thời gian** · Xoá tìm kiếm.
7. **invoices--accountant.html** — accountant context: `data-density="compact"` on main; household switcher shows
   "Cô Hai · Nhơn Lý" (accountant serves several households: note "Kế toán: Lê Văn Minh · 6 hộ"); date "Tháng này"
   → Tháng 9/2026 via chips "Tháng 9/2026 ×"; table 25 rows/page of September invoices 00000175 … 00000151 (generate
   plausible rows: times, buyers mostly "Khách lẻ", amounts 40.000–1.690.000, all Có mã except 00000163 "Lỗi — sai MST,
   đã sửa và gửi lại"); c-pager "Hiển thị 1–25 / 212 hoá đơn" page 1 of 9; export button "Xuất Excel" (plain).

## 13. Remaining states + detail screens v1.5 (2026-10-02)
### 13.1 Onboarding errors (phone 390; copy the base step; one fix action each, a person always reachable)
- **onboard-otp--wrong** — boxes `4 8 2 9 1 7` invalid (c-otp[data-invalid]); c-banner--err "Mã chưa đúng" body
  "Còn 2 lần thử. Mã mới nhất là tin nhắn cuối cùng từ OPC Gia Lai trên Zalo."; primary **Gửi mã mới**; link "Gửi qua SMS".
- **onboard-household--notfound** — MST `4101678913` field invalid, hint "Không tìm thấy mã số thuế này trên Cổng
  thuế"; c-banner--pend "Có thể gõ nhầm một số — kiểm tra lại giấy đăng ký hộ kinh doanh"; buttons **Tra bằng số
  CCCD** (act) · "Chưa có mã số thuế — OPC giúp đăng ký" · Gọi chị Lan.
- **onboard-verify--camera-denied** — c-empty (i-camera) "OPC chưa được dùng camera"; numbered steps (c-lanes,
  plain): 1 Chạm biểu tượng ổ khoá cạnh địa chỉ trang · 2 Chọn Quyền → Máy ảnh → Cho phép · 3 Quay lại và chạm
  "Thử lại"; primary **Thử lại**; secondary "Chọn cách khác: nhân viên OPC đến giúp".
- **onboard-verify--failed** — c-banner--err "Chưa xác minh được" body "Ảnh mặt trước bị loá ở góc phải, nên không
  đọc được số CCCD." (reason in plain words); what still works: "Chị vẫn thêm hàng và bán tiền mặt được — chỉ QR và
  hoá đơn cần xác minh."; primary **Chụp lại** · option card "Nhân viên OPC xác minh tại quầy — hẹn Thứ Bảy 03/10";
  "Lần thử 2/3".
- **onboard-bank--mismatch** — c-banner--err "Tên tài khoản không khớp chủ hộ"; c-kv: Tài khoản MB 0987 6543 21 ·
  Chủ tài khoản **NGUYEN VAN PHUC** · Chủ hộ đã xác minh **TRAN THI HAI**; body "Tiền QR phải vào tài khoản đứng tên
  chủ hộ hoặc tên hộ kinh doanh."; primary **Liên kết tài khoản khác**; secondary "Gửi OPC xem xét (có giấy uỷ quyền)".
- **onboard-products--unreadable** — c-empty "AI chưa đọc được ảnh này" with the reason "Ảnh bị mờ và tối";
  tips (r-onboard__facts): đặt bảng giá trên mặt phẳng · đủ sáng · chụp thẳng, không nghiêng; primary **Chụp lại**;
  secondary options: "Nói tên và giá" · "Chọn từ mẫu Hải sản khô".
### 13.2 Loading (skeleton in the real layout)
- **home--loading** — shell rendered; money hero, lanes (3 blocks), tax and orders as c-skel; c-skel-note "Đang tải…
  · số liệu trước đó 10:43"; nav badges hidden.
- **orders--loading** — listbar usable (search, date), tabs counts as c-skel, table rows as 6 skeleton rows.
### 13.3 Order detail — **order-detail.html** = DH-1040 (Khách sạn Hải Âu · Zalo · công nợ · chờ xác nhận)
r-detail: back "Đơn hàng"; title "DH-1040" + c-sign--you "Chờ xác nhận · giao 15:00"; actions **Xác nhận đơn** (act) ·
In phiếu · Huỷ đơn (danger). Main: customer card (c-kv: Khách sạn Hải Âu · anh Quang 0914 223 456 · 18 Nguyễn Huệ,
Quy Nhơn · công nợ hiện tại 3.150.000 ₫ (DH-0866 quá hạn 2 ngày)); lines: Cá cơm sấy giòn 3 kg × 680.000 = 2.040.000 ·
Tôm khô loại 1 2 kg × 690.000 = 1.380.000 → Tổng 3.420.000 ₫; payment: Công nợ · hạn trả 09/10/2026 · c-moneyline
step 1. Side: c-timeline: 09:48 Khách đặt qua Zalo (tin nhắn "3kg cá cơm, 2kg tôm khô, giao 3h chiều") · 09:50 OPC
tạo đơn từ tin nhắn (Trợ lý · Phúc kiểm tra) · now: chờ chị xác nhận; note "Sau khi xác nhận: trừ kho, nhắc giao
lúc 14:30, hoá đơn phát hành khi thu tiền".
### 13.4 Invoice detail — **invoice-detail.html** = 00000418 (DH-1036, Anh Tuấn, 640.000 ₫, chờ mã CQT)
r-detail: back "Hoá đơn"; title "Hoá đơn 00000418" + c-sign--pend "Chờ mã CQT · 25 phút"; actions **Gửi lại** (act) ·
Tải PDF · Gửi cho khách qua Zalo. c-banner--pend "Hilo báo lỗi lúc 08:34 (máy chủ CQT bận). OPC đã gửi lại 10:20. Hoá
đơn vẫn hợp lệ để đưa khách." Main: c-doc preview: HOÁ ĐƠN BÁN HÀNG (máy tính tiền) · ký hiệu 2C26MCH · số 00000418 ·
02/10/2026 08:34; Người bán HỘ KINH DOANH TRẦN THỊ HAI · MST 4101678912 · address; Người mua: Anh Tuấn (khách lẻ);
lines: Mực khô loại 1 0,4 kg × 1.250.000 = 500.000 · Cá cơm sấy giòn hũ 250 g 1 × 95.000 · Muối ớt xanh hũ 1 × 30.000 ·
Túi giấy quà tặng 3 × 5.000 = 15.000 → 640.000 ₫ (bằng chữ: Sáu trăm bốn mươi nghìn đồng); foot "Mã CQT: đang chờ
cấp · Tra cứu tại hoadondientu.gdt.gov.vn". Side: c-timeline 10:20 OPC gửi lại (pend) · 08:34 Hilo báo lỗi (err) ·
08:34 Phát hành từ đơn DH-1036 · 08:33 Đã xác minh 640.000 ₫ QR (ok).

## 14. Information architecture v2 (2026-10-02) — see SCOPE-MVP.md
**Two levels.** The sidebar holds 6 groups + Quầy. Each group page has a sub-navigation row (`c-subnav`) with its
pages, and feature switches only add or remove sub-nav items, so the sidebar never grows.
- **Sidebar (desktop):**
  - Hôm nay · **Quầy bán hàng** (outlined, arrow) · Bán (3) · Tiền (3) · Hàng · Sổ & thuế · Cần xử lý (6)
  - Footer: Cài đặt · Trợ giúp & hỗ trợ + connection lines.
- **Sub-nav per group** (for Cô Hai: revenue > 1 tỷ, so purchasing is ON; delivery is ON because of Zalo
  orders; booking, farm purchase and traceability are OFF):
  - Bán: Đơn hàng · Giao hàng · Khách hàng
  - Tiền: Thu chi & đối soát · Công nợ · Đóng ca
  - Hàng: Hàng hoá & giá · Tồn kho · Nhập hàng & chi phí · Nhà cung cấp
  - Sổ & thuế: Hoá đơn · Sổ sách · Thuế & tờ khai · Báo cáo
  - Cần xử lý: Việc chờ duyệt (6) · Nhật ký
  - Cài đặt: Hộ kinh doanh · Người dùng & quyền · Kết nối · Tính năng · Dữ liệu & quyền riêng tư
- **Phone tab bar (v2.1):** Hôm nay (6) · Quầy (yellow) · Bán (3) · Tiền (3) · Thêm. "Thêm" lists only what has no tab:
  Cần xử lý (pinned) · Hàng hoá · Sổ & thuế · Hỏi Trợ lý · Thông báo · Cài đặt · Trợ giúp.
- **v2.1 renames:** "Hàng" becomes "Hàng hoá"; "đối soát" becomes "đối chiếu". Nhật ký moves to Cài đặt ("Nhật ký hoạt động").

### 14.1 approvals.html — Cần xử lý → Việc chờ duyệt (the owner side of the Agent Control Tower)
Title "Việc chờ duyệt"; c-say "OPC và Trợ lý chỉ soạn sẵn — chị duyệt thì mới thành thật."; tabs: **Chờ chị duyệt
(4)** · Cảnh báo (2) · Đã xử lý hôm nay (7). Each card: source chip (Trợ lý · Ngân hàng · Hệ thống), what, evidence
link, "Sau khi duyệt: …", actions (only the first card has the yellow primary):
1. Trợ lý · 09:50 — **Đơn Zalo DH-1040 · Khách sạn Hải Âu · 3.420.000 ₫** — "Tạo từ tin nhắn: “3kg cá cơm, 2kg tôm
   khô, giao 3h chiều”" [Xem tin nhắn] — Sau khi duyệt: giữ hàng, nhắc giao 14:30, công nợ khách thành 6.570.000 ₫
   — **Xác nhận đơn** · Sửa · Từ chối.
2. Ngân hàng · 09:15 — **Gán 2.150.000 ₫ vào DH-1038** (NHA HANG BIEN DONG · "TT HANG KHO T9") — gợi ý: đúng số
   tiền, đúng tên — Gán · Chọn đơn khác.
3. Trợ lý · 08:05 — **Phiếu nhập NH-0052 từ ảnh hoá đơn · Cơ sở Mực khô Tam Quan · 19.600.000 ₫** — Mực khô loại 1
   20 kg × 980.000 ₫; 1 dòng AI chưa chắc (đơn vị) — Sau khi duyệt: cộng 20 kg vào kho, ghi chi phí, công nợ NCC
   19.600.000 ₫ — Kiểm tra & duyệt · Từ chối.
4. Hệ thống · 01/10 — **Nháp tờ khai thuế quý III/2026 · 6.184.500 ₫ · hạn 31/10/2026** — Sau khi duyệt: OPC tạo
   tệp tờ khai, chị nộp trên eTax (có hướng dẫn), rồi chụp mã xác nhận để OPC lưu — Xem nháp tờ khai.
Cảnh báo tab (not drawn): HĐ 00000418 chờ mã CQT; DH-0866 quá hạn 2 ngày (Trợ lý soạn sẵn tin nhắc nợ).

### 14.2 audit.html — Cần xử lý → Nhật ký
Filter chips: Tất cả · Chị Hai · Phúc · Trợ lý · Hệ thống · Ngân hàng; date "Hôm nay". c-timeline (newest first),
each entry: time · actor · action · object link · before → after where relevant · device:
10:47 Hệ thống · Đã xác minh 1.020.000 ₫ · DH-1043 · khớp sao kê MB
10:44 Phúc · Giao hàng trước DH-1043 (chờ xác minh, dưới mức 2.000.000 ₫) · điện thoại của Phúc
10:20 Hệ thống · Gửi lại hoá đơn 00000418 lên Hilo
09:50 Trợ lý · Soạn nháp đơn DH-1040 từ tin nhắn Zalo · chờ chị duyệt
09:15 Ngân hàng · Nhận 2.150.000 ₫ không có mã đơn · vào hàng chờ gán
08:12 Chị Hai · Sửa giá Cá bò một nắng: 320.000 ₫ → 330.000 ₫/kg · điện thoại của chị Hai
08:05 Trợ lý · Đọc ảnh hoá đơn Cơ sở Mực khô Tam Quan → nháp phiếu nhập NH-0052
07:00 Phúc · Mở ca sáng · tiền đầu ca 500.000 ₫
Note: "Nhật ký không sửa hoặc xoá được. Kế toán và cán bộ chỉ xem phần được chị cho phép."

### 14.3 settings-users.html — Cài đặt → Người dùng & quyền
Members (c-list or table): Trần Thị Hai — Chủ hộ · toàn quyền · đã xác minh L1 · Nguyễn Văn Phúc — Quản lý · mọi việc
trừ đổi tài khoản ngân hàng và người dùng · Lê Thị Hoa — Thu ngân · Quầy và Đóng ca · ca sáng · Lê Văn Minh — Kế toán
(uỷ quyền) · Sổ & thuế, Hoá đơn, Công nợ · chỉ xem và lập nháp · **đến 31/12/2026**. Primary **Mời người dùng**.
Permission matrix (compact): rows Bán · Tiền · Hàng · Sổ & thuế · Duyệt · Cài đặt; columns Chủ hộ / Quản lý / Thu ngân
/ Kế toán; cells ✓ / Xem / Nháp / —. Devices: 3 đang đăng nhập (Điện thoại chị Hai · Điện thoại Phúc · Laptop quầy)
with "Đăng xuất".
### 14.4 settings-features.html — Cài đặt → Tính năng
c-say "Bật thêm khi chị cần. Tắt thì menu gọn hơn; dữ liệu không mất." Switch rows (label · why · what it adds):
Mua hàng & chi phí — **bật, bắt buộc** (doanh thu 2026 là 1.284.500.000 ₫, trên 1 tỷ) → Nhập hàng, Nhà cung cấp, Phải
trả, Hoá đơn mua vào · Giao hàng — bật → Bán · Giao hàng · Đặt chỗ — tắt (homestay, tour) · Thu mua nông sản — tắt
(bảng kê mua của nông dân không có hoá đơn) · Truy xuất nguồn gốc — tắt (mã QR trên bao bì đặc sản) · Nhiều người
dùng — bật.
### 14.5 home--more.html — phone "Thêm" sheet over Hôm nay
Sheet title "Tất cả"; Cần xử lý (6) row first (yellow count); then groups with items: Bán (Đơn hàng, Giao hàng,
Khách hàng) · Tiền (Thu chi & đối soát, Công nợ, Đóng ca) · Hàng (Hàng hoá & giá, Tồn kho, Nhập hàng & chi phí, Nhà cung
cấp) · Sổ & thuế (Hoá đơn, Sổ sách, Thuế & tờ khai, Báo cáo) · Cài đặt · Trợ giúp & hỗ trợ (Gọi chị Lan). Items are
44px rows with icon + label (+ count).

## 15. Pro layer v3.1 (2026-10-02) — support, productivity, trust (style A-Pro)
### 15.1 Support (everyone)
- **home--assistant**: Trợ lý drawer open over Hôm nay. Context line "Đang xem: Tổng quan · hôm nay". Suggested chips
  for this screen: "Vì sao hôm nay tăng 19%?" (asked) · "Khoản nào cần đối chiếu trước?" · "Quý III nộp bao nhiêu
  thuế?". Answer (c-answer): "Doanh thu tăng 1.340.000 ₫ so với hôm qua, chủ yếu từ DH-1027 của Công ty TNHH Du lịch
  Biển Xanh (1.690.000 ₫) — khách mới, mua 6 món." Sources: "Đơn hôm nay (23) · Sao kê MB đến 10:44". Action
  suggestion: "Lưu Biển Xanh làm khách quen" → [Đề xuất · cần chị duyệt] (goes to Cần xử lý). Composer: input "Hỏi Trợ
  lý…" + mic + send. Note "Trợ lý chỉ đọc số liệu và soạn đề xuất; không tự làm thay chị."
- **money--help**: help drawer over Tiền & đối chiếu. Title "Trợ giúp · Tiền & đối chiếu". Short guide steps (3):
  "Chờ xác minh là gì" · "Khi nào giao hàng được" · "Khoản chưa gán làm sao". A 30-second video card (thumbnail as
  c-card with play icon, "Video 0:30 · chị Lan hướng dẫn"). "Xem lại hướng dẫn trên màn này" (tour). People:
  **Gọi lại cho tôi** (pick time: Trong 15 phút · Chiều nay 14:00 · Mai 8:00) · Nhắn Zalo OPC Gia Lai · Gọi chị Lan.
- **home--notifications**: drawer "Thông báo" with tabs Tất cả (4 chưa đọc) · Tiền · Hoá đơn · Hệ thống; items
  (newest first): 10:47 Đã xác minh 1.020.000 ₫ · DH-1043 (money, unread) · 10:44 Có tiền mới 1.020.000 ₫ chờ xác minh
  (money, unread) · 10:20 Hoá đơn 00000418 đang chờ mã CQT (warn, unread) · 09:15 Chuyển khoản 2.150.000 ₫ chưa có mã
  đơn (warn, unread) · Hôm qua 17:05 Liên kết MB cần đồng ý lại trước 17/10 (system) · Hôm qua 08:00 Nhắc: khai thuế
  quý III hạn 31/10 (system). Actions: "Đánh dấu đã đọc tất cả" · "Cài đặt thông báo".
- **settings-display**: Cài đặt → Hiển thị (add "Hiển thị" to the settings sub-nav). Cỡ chữ (c-sizepick: Vừa ·
  **Lớn** (checked) · Rất lớn, each showing "Aa 1.020.000 ₫"); Chế độ (c-seg): **Gọn** — ít cột, ít thẻ, cho chủ hộ
  · Đầy đủ — mọi công cụ, cho quản lý & kế toán; Tương phản cao (switch, off); Chuyển động: Bình thường · Giảm (seg);
  live preview card at the side (a lane + money sign at the chosen size). Note "Mỗi người dùng một cài đặt riêng".
- **home--simple**: Hôm nay in Gọn mode + text size Lớn (`<html data-textsize="lg">`, `<body data-view="simple">`):
  only Tiền hôm nay + Cần xử lý (top 3) + "Mở quầy" big; tax/orders/7-day/debt/assistant cards hidden (`u-pro`).
- **Global (all shell screens)**: top bar gets `c-sync` "Đã lưu · 10:45"; search shows `⌘K` hint and a mic button;
  icon buttons get `data-tip`.
### 15.2 Productivity (Phúc, accountant — `u-pro`, hidden in Gọn)
- **home--command**: palette open with query "dh-104": Đơn — DH-1043 (1.020.000 ₫ · chờ xác minh), DH-1042, DH-1041,
  DH-1040 (chờ xác nhận); Hành động — Tạo đơn (N) · Mở quầy (Q) · Ghi khoản chi; Đi tới — Thuế & tờ khai · Nhật ký.
  Footer: ↑↓ chọn · Enter mở · Esc đóng · ⌘K mở lại.
- **orders--peek**: orders list with a wide drawer for DH-1040 (quick view: customer, lines, money line, timeline,
  actions Xác nhận đơn / Mở trang đơn ↗); footer hint "↑↓ đơn trước/sau".
- **orders--bulk**: "Chưa thu" saved view selected (a c-filter chip "★ Đơn chưa thu" + "Lưu chế độ xem" quiet),
  checkboxes column, 2 rows selected (DH-1040, DH-1038) → c-bulkbar "Đã chọn 2 đơn · 5.570.000 ₫" actions: **Gửi nhắc
  nợ qua Zalo** (act) · In phiếu · Xuất Excel · ✕; a c-toast after a previous action: "Đã xuất 23 đơn ra Excel ·
  Tải lại" (ok).
- **Home**: Tiền hôm nay gets c-trend "↑ 19%" + c-spark (7 days: 9.82, 11.24, 6.31, 5.98, 6.75, 7.12, 8.46 triệu) and a
  quiet "Vì sao tăng?" (opens the assistant). Detail pages get `c-crumbs` (Bán / Đơn hàng / DH-1040).
### 15.3 Trust & brand
- **Counter**: every product tile gets `c-prod__img` with a category drawing (mực, cá, tôm, hũ, bánh, túi) until the
  owner adds a photo; one tile ("Mực khô loại 1") shows a photo placeholder state "Thêm ảnh".
- **receipt**: the printed slip / PDF for DH-1043 (80mm): shop "Hải sản khô Cô Hai" · thôn Lý Hưng, Nhơn Lý · MST
  4101678912 · 02/10/2026 10:47 · lines · Tổng 1.020.000 ₫ · Đã thanh toán QR · Hoá đơn 00000422 · Mã tra cứu
  M1-26-QN7K2-00000000422 · QR tra cứu · "Cảm ơn quý khách — hẹn gặp lại!". Beside it: actions In · Tải PDF · Gửi Zalo
  cho khách, and a c-msgcard preview of the Zalo message the customer receives (from "Hải sản khô Cô Hai · qua OPC",
  body: đơn, số tiền, hoá đơn, buttons "Xem hoá đơn" · "Lưu số cửa hàng").
- **settings-users--otp**: OTP confirm dialog when inviting the accountant: "Xác nhận mời Lê Văn Minh làm Kế toán
  đến 31/12/2026" · c-otp · "Mã gửi qua Zalo tới 0905 812 347" · trust line with i-shield "OPC không bao giờ tự chuyển
  tiền hay nộp thuế thay chị" · Huỷ · **Xác nhận mời**.

# OPC app — design notes (maker self-check, references/maker-checklist.md)

## v4.2 · Round 1 — approvals (Control Tower), sales-inbox, order-detail (Order 360) · 2026-10-05
1. Machine: probe 0 at 1440/1024/390 + stress, keys ok (dialog traps focus via inert: 7 of 38 stops), axe 0, text lg/xl clean.
2. Squint: approvals → selected job title, then the decision panel (primary "Duyệt đơn"); sales-inbox → the original
   message, then "Trợ lý hiểu là" lines and the total; order-detail → title + state pill + 6.250.000 ₫, then the journey bar.
3. Anti-slop: no gradients/illustrations; one accent; status = colour + icon + word. Watch: many small pills on list rows.
4. Detail: list rows align left with the detail panel; tables stack on phone (c-table--stack).
5. Content: real names/amounts from FLOWS.md §0.1; Vietnamese wording; "Mô phỏng" not used yet (demo labels come with the demo build).
6. Weakest area (maker's guess): the journey bar on Order 360 is visually quiet at 1440 (small meta labels); the
   sales-inbox detail is long before the primary action on phone.

## v4.2 · Round 1 — delivery (board), delivery--pick, delivery--courier · 2026-10-05
- Inventory. **delivery** — purpose: today's shipments and who moves them; first read: what is waiting to be picked
  and what failed; primary: "Soạn hàng" on the most urgent card; data: order, customer, lines, due, method (4 kinds),
  deliverer, COD, state; states: empty day, failed delivery, carrier status (Mô phỏng). Pattern **board** because
  shipments move through 4 stages (Chờ soạn → Đã soạn → Đang giao → Đã giao) and the household moves them; a status
  column alone would hide the flow. Phone: one stage at a time with stage tabs (r-board rule).
  **delivery--pick** — purpose: pick the reserved lines by lot and hand over; first read: "1/2 món xong"; primary:
  "Bàn giao cho anh Hùng" (locked until complete or partial chosen); pattern detail/checklist.
  **delivery--courier** — purpose: the deliverer records the outcome without an account; first read: customer +
  address; primary: "Đã giao xong" with photo + receiver + COD method; pattern short wizard (one screen).
- Machine: probe 0 at 1440/1024/390 + stress, keys ok, axe 0, text lg/xl clean.
- Squint/anti-slop: board uses the skill's r-board skinned with OPC tokens; one filled primary per view (the most
  urgent card); carrier states labelled "Mô phỏng". Weakest: card density in "Đang giao" (3 states + 2 actions).
- Evaluator: delivery 7.6 (no stage load, money twice, failed card not raised) → round 2 8.0; pick 8.3; courier 8.0 → 8.0 (either/or proof, one instruction per method).

## v4.2 · Round 1 — receivables, receivables--payables, receivable-detail, receivable-detail--assign · 2026-10-05
- Inventory. **receivables** — purpose: who owes how much, what is overdue, what to do; first read: 17.700.000 ₫ and
  the overdue tile (Sunrise 8.400.000 ₫); primary: "Xem & nhắc" on the overdue row; data: customer, terms, limit,
  open amount, state (due/overdue), last reminder; also carriers/bus companies holding COD as receivables.
  Pattern **datatable** because many counterparties with comparable attributes, scanned and sorted (same family as
  orders and invoices: r-listhead + 5 columns). **payables** — same table, money out: the owner sends via the bank
  app (N-06/N-07). **receivable-detail** — pattern detail: one customer's statement (open invoices, upcoming invoice
  not counted yet, paid), reminder history and the assistant's draft; primary "Gửi bảng kê & nhắc nợ".
  **--assign** — pattern match: one transfer without an order code → several invoices, suggestion = exact sum.
- Consistency checks done: Sunrise debt 8.400.000 (2 overdue invoices 5.200.000 + 3.200.000) matches the credit check
  in approvals; DH-2052 counted only after its invoice (FLOWS ② step 16); DH-2049 paid by QR at delivery (board updated);
  COD from the bus company and GHTK appear as receivables (SCOPE §7 #15). Tabs carry no amounts (say once).
- Machine: probe 0 at 1440/1024/390 + stress, keys ok (dialog inert: 5 of 28), axe 0, text lg/xl clean.
- Weakest (maker): phone stacked rows are still busy (amount, state chip and button compete).
- Evaluator: r1 8.0/7.6/8.2/7.6 → r2 8.0/8.0/8.2/8.0. Fixed: say-once tiles, payables bar + single accent, assign focus + math vs money truth, 'Chưa tính' chip, folded history reachable.

## v4.2 · Round 1 — purchases, purchase-receive, purchases--expense · 2026-10-05
- Inventory. **purchases** — purpose: what was bought, what is coming, what needs the owner; first read: MH-0118
  "Nhận thiếu 5 kg · chờ chị"; primary: "Tạo đơn mua" (page) / "Xem & xác nhận" (row); data: PO, supplier, lines,
  value, state; tabs Đơn mua · Chi phí. Pattern **datatable** (same family as orders/invoices/debts).
  **purchase-receive** — purpose: count what arrived, decide on the shortfall, match the supplier invoice; first read:
  35/40 kg; primary "Xác nhận nhận hàng" (stock in once + payable 11.200.000 ₫); pattern **detail/checklist**
  (mirror of picking). **purchases--expense** — expense without stock from a photo; pattern **form** (dialog).
- Consistency: stock rises only at receipt confirmation; payable created then (payables now shows MH-0118 as
  "Chưa tính", total 6.050.000 ₫); production at 07:30 used lot TB-1005 (MH-0114, 05/10), not the new receipt;
  MH-0109 value = 120 hũ × 28.000 + 60 gói × 24.000; beef 280.000 ₫/kg everywhere. Nav "Hàng hoá" → purchases.html.
- Machine: probe 0 (1440/1024/390 + stress), keys ok, axe 0, text lg/xl clean.
- Weakest (maker): desktop receive page is dense on the right (document check) — first read is still the shortfall.
- Eval r1: 7.4 / 8.0 / 7.4 / 7.5 → r2: 8.0 / 8.2 / 8.0 / 8.0 (all criteria ≥ 8). Deferred (r2 refine notes): sticky confirm on 390 receive, mute figures inside the invoice preview, routine status chips → grey (system-wide, with the old-screen migration).

## v4.2.4 · Tồn kho, lô, truy xuất, kiểm kê (UI-08) · 2026-10-05 — inventory + pattern
Data (FLOWS §0.1 + ③④, today Thứ Ba 06/10): Bò một nắng 46 gói = BMN-0405 26 (20 giữ cho DH-2052, hạn 15/11)
+ BMN-0410 20 (hạn 30/11); LCB-0412 đang làm (+40 gói ~16:00). Muối MKV-0921 80 hũ (30 giữ). Thịt bò tươi 6 kg
(TB-0998 đông lạnh, phần còn lại của 40 kg MH-0105 sau khi LCB-0405 dùng 34 kg) — dưới mức 20 kg; 35 kg MH-0118
chờ xác nhận. Gia vị ướp GV-0908 54 gói. Lot BMN-0405 = LCB-0405 16/09: 34 kg TB-0998 + 2 gói GV-0908 → 40 gói;
went to Phố Núi DH-2031 3 · quầy 11 (4 to 3 known customers) · 26 in stock → 40 = 14 + 26.
- **stock** — purpose: can I sell / do I need to buy, per item; first read: the tinted raw-beef row (below minimum,
  35 kg waiting for the owner's receipt); primary "Kiểm kê"; columns thực · đã giữ · khả dụng (held links the order),
  lots inline as links. Pattern **datatable** because: few items, the same comparable numbers per row; lots are
  children shown inside the row rather than a second table.
- **stock-lot** — purpose: where this lot came from and where it went (two-way trace) + its append-only ledger;
  first read: 26 gói (20 giữ · 6 bán được) · hạn 15/11; no primary (a reading page; the only state change, lock, is
  destructive so it is a quiet danger button). Pattern **detail** because one object, facts + history; trace is a new
  recipe `r-trace` (Từ đâu | Tới đâu, balance line "40 = 14 + 26" from OPC kiểm tra).
- **stock-lot--lock** — confirm dialog: consequences first (6 stop selling, the 20 held for DH-2052 move to
  BMN-0410 → bò bán được 0 tới ~16:00, who received it and that the assistant drafts the notices), reason required
  (empty), "Khoá lô" locked until a reason. Reversible (Mở khoá with a reason).
- **stock-count** — purpose: count, see differences, send for approval (FLOWS ④: never edit stock directly);
  first read: 2 lines lệch; primary "Gửi chị An duyệt" locked with its reason (1 line without reason). Pattern
  **form/checklist** (mirror of r-pick) because the job is going line by line with a number in hand; selling continues.
- Machine: probe 0 (1440/1024/390 + stress), keys ok (dialog traps 4 stops), axe 0, text lg/xl clean.
  System fix found while building: `td.c-table__who` was `display:grid`, so tall rows broke the cell height and
  hairline (all 18 datatable screens) → children are blocks, td stays a table-cell. Phone: stock folds thực/giữ into
  the item cell, khả dụng on the right; the needs-you tint covers the whole stacked row.
- Maker self-check — weakest: lot page has no primary by design (reading page); count reason segment is a 4-way
  choice that wraps on phone at xl.
- Eval r1: 7.2 / 7.6 / 7.8 / 7.2 → r2: 8.0 / 8.0 / 8.4 / 8.0 (all criteria 8+). Deferred refine notes: healthy-state
  pills duplicate the figure (system-wide, with migration); signed qty in the ledger margin; in/out glyphs on trace heads.

## v4.2.5 · Chế biến (UI-09) · 2026-10-05 — inventory + pattern
Data: LCB-0412 (hôm nay, anh Khoa) đang làm từ 07:30 — đã xuất 34 kg TB-1005 + 2 gói GV-0908, dự kiến 40 gói ~16:00
→ lô BMN-0412, hạn 05/12. LCB-0413 (Thứ Năm 08/10) nháp: cần 34 kg, khả dụng 6 kg → thiếu 28 kg; đủ khi chị xác nhận
MH-0118 (35 kg). Recipe from the last 3 runs: 34 kg + 2 gói → 39–40 gói. Lot code = order number (LCB-0405 → BMN-0405).
- **production** — purpose: what is being made and what is blocked; first read: tinted LCB-0413 "thiếu 28 kg";
  primary "Lập lệnh chế biến". Pattern **datatable** because: a short list of comparable orders (same family as
  purchases). Hàng hoá sub-nav gains "Chế biến".
- **production-new** — purpose: plan a run; OPC computes materials from past runs and blocks starting on shortage
  (never negative stock); first read: the materials check "thiếu 28 kg"; primary "Lưu lệnh nháp", "Bắt đầu" locked
  with its reason. Pattern **form** because: one short object; the check is beside the inputs.
- **production-detail** — running order; first read: "Đang làm · xong khoảng 16:00"; primary "Ghi kết quả". Pattern
  **detail** (c-journey + materials issued + expected lot + timeline), same as Order 360.
- **production-detail--finish** — 16:05: expected vs actual sheet (reuses `r-count`), yield 38 < usual 39–40 →
  reason required (empty); new lot preview; primary "Nhập kho 38 gói" locked with its reason. Shell clock shows 16:05.
- Machine: probe 0 (1440/1024/390 + stress), axe 0, text lg/xl clean. System: on phone a banner's action drops under
  its text (was squeezing the text column). Consistency edits: purchases low-stock banner now names LCB-0413 (34 kg,
  covered once MH-0118 is confirmed) instead of suggesting another PO; Control Tower production detail links here.
- Maker self-check — weakest: production list has only a status column (few attributes); finish state shell clock
  is rewritten to 16:05 by `at()`.
- Eval: r1 group 7.8 → r2 7.4/7.5/7.1/7.7 → r3 7.8/8.0/7.8/8.2 → r4 8.2/8.4/8.2/8.2 (pass). Deferred: row-action
  weight scale for all datatables, inline unlock hint under locked primaries, progress rule for in-flight runs.
  r4 misread the finish primary (it is "Nhập kho 38 gói", locked) — not acted on.

## v4.2.6 · Sổ sách + đối chiếu kỳ (UI-14) · 2026-10-05 — inventory + pattern
Period: today is 06/10, so the period being reconciled is **Quý III/2026** (hạn 31/10, còn 25 ngày); Q IV is
"Đang thu dữ liệu". FLOWS §0.1 updated. Three sources (CEO B09): doanh thu theo đơn đã giao 338.400.000 · hoá đơn
bán ra trong OPC 337.100.000 (thiếu DH-2036 1.300.000 — invoice exists on X Invoice, not pulled) · hoá đơn có mã
trên cổng thuế 337.760.000 (thiếu HĐ quầy 00001172 640.000 — "Chưa rõ kết quả") · tiền: đã thu 327.850.000 + phải
thu 8.400.000 (Sunrise) + chưa gán 2.150.000 = 338.400.000. Cổng thuế is not connected → chị Lan uploaded the list
05/10 (manual path).
- **period** — purpose: is Q III clean enough to lock; first read: "Cần xem · 5 việc" + three-source figures;
  primary (bottom gate) "Gửi chị An khoá kỳ" locked "còn 5 việc" (anh Khoa is operator; lock = chủ hộ/kế toán).
  Pattern **detail/checklist** because one object (the period) with a finite to-do list; recipes `r-recon` (source
  rows with the gap) + `r-gate` (to-dos with figure + one action each).
- **period--item** — drawer: one exception handled in place (input invoice on the tax portal, not in the books):
  options with the assistant's pick, "Lưu quyết định" re-runs the checks (result line says "còn 4 việc").
- **period--ready** — 07/10: all sources match, 5 decisions with who/when, primary "Gửi chị An khoá kỳ" enabled;
  result line explains what locking means and that "Tính thuế" comes next.
- **books** — purpose: the household's books built from orders/invoices/bank (never typed); first read: Doanh thu
  tháng 9 figure + rows needing attention; primary "Xuất sổ". Pattern **datatable**; tabs Doanh thu · Chi phí · Tiền
  · Kho; the template (S1a, TT 152/2025) is labelled "chưa đối chiếu văn bản gốc" (CEO B24).
- Machine: probe 0 (1440/1024/390 + stress), axe 0, drawer traps 5 stops, text lg/xl clean. Order: to-dos first (the
  job), three sources second (the evidence); gate in flow (not sticky) so it never covers the list.
- Maker self-check — weakest: three-source row labels wrap at 1440 in the narrower main column; books tabs Chi phí /
  Tiền / Kho are not drawn (same table shape).
- Eval: r1 7.6/7.8/7.8/7.6 → r2 8.0/8.2/8.0/7.6 → r3 8.0/8.4/8.0/8.0 (pass). Deferred: hide repeated OK marks on
  mostly-clean lists (system), outcome-delta emphasis standard, "mở lại kỳ" affordance near the lock.

## v4.2.7 · Thuế: tính, tờ khai nháp, gửi/nộp, bằng chứng (UI-15/16) · 2026-10-05 — inventory + pattern
Follows Câu 1 option B (SCOPE Q1): payment always outside OPC (eTax Mobile / bank app) and OPC records the receipt;
filing in OPC only with a proven provider — in the demo "Ký và gửi qua OPC" is **Mô phỏng**; the manual eTax path is
always available. Owner's view (shell user = chị An) because approval/filing/payment are hers (N-06/N-07).
Numbers (bộ quy tắc demo-2026.3, % trên doanh thu theo nhóm ngành, **nguồn giả lập**, chưa ai xác nhận): Q III
338.400.000 = chế biến (bò một nắng) 266.400.000 × (3% GTGT + 1,5% TNCN) = 11.988.000 + phân phối (muối, mua về bán
lại) 72.000.000 × (1% + 0,5%) = 1.080.000 → **13.068.000 ₫** (GTGT 8.712.000 · TNCN 4.356.000). Q II 12.009.000.
Timeline 07/10: 08:55 chị An khoá kỳ · 08:56 OPC tính · 10:20 chị Lan xem · 11:02 chị An duyệt · 11:06 tiếp nhận
(Mô phỏng) · 11:24 chị An nộp trên eTax Mobile, nhập mã · MB shows 13.068.000 out → khớp · 11:25 kỳ Đã đóng.
- **tax** — purpose: see how the tax was computed and approve it; first read: 13.068.000 ₫ (Mô phỏng) + "Chờ chị
  duyệt"; primary "Duyệt số thuế". Pattern **detail** (journey + explainable calc table + rule set in the rail).
- **tax--return** — the draft return as a document (`c-doc`), watermark NHÁP · MÔ PHỎNG; reading view, no primary.
- **tax-file** — purpose: file the approved return; two levels on one screen (choice): Tự gửi trên eTax (selected,
  4 steps, primary "Chụp thông báo tiếp nhận") · Ký và gửi qua OPC (Mô phỏng, needs T-VAN + remote signature).
- **tax-file--signed** — accepted (Mô phỏng); step 2 pay: prefilled facts, primary "Mở eTax Mobile", receipt field
  empty; the period becomes "Đã nộp" only with a receipt code (OPC-21).
- **tax-evidence** — period closed; evidence pack (return, acknowledgement, receipt matched to the MB outflow,
  approvals, reconciliation); primary "Tải bộ bằng chứng". Patterns **form/wizard-short** (file) and **detail**.
- Machine: probe 0 (1440/1024/390 + stress), axe 0, text lg/xl clean. Phone: calc rows label GTGT/TNCN/Cộng inline,
  total row collapses to label + figure. Watermark kept unrotated (no overflow).
- Maker self-check — weakest: tax-file packs choice + 4 steps + result in one card; tiểu mục codes are demo values.
- Eval: r1 8.0/7.8/8.2/8.0/8.0 → r2 8.0/7.8/8.0/8.0/8.2 → r3 8.0/8.0/8.0/8.0/8.2 (pass). Deferred: tabular right-aligned
  r-pay values, one "Xem" pattern for evidence rows, stronger recommended-path affordance on tax-file.

## v4.2.8 · Thiết lập: Sẵn sàng, Hộ & mô hình, Dữ liệu nền, Kết nối, Vai trò & duyệt (UI-02..06) · 2026-10-05
Lives under Cài đặt with a new sub-nav: Sẵn sàng · Hộ & mô hình · Dữ liệu nền · Kết nối · Vai trò & duyệt · Tính
năng · Hiển thị · Nhật ký (nav "Cài đặt" → readiness.html on new screens). An Nhiên is live, so readiness is
**Sẵn sàng có điều kiện**: all required items done, 3 recommended open — cổng thuế not connected (Q III list uploaded
by hand), counter device not installed as an app (offline), tax rule set not confirmed by chị Lan. Plus 1 connection
error (X Invoice timeout 10:12, DH-2047 "Chưa rõ kết quả") which does not block other items. Data cross-checks:
3 customers (Sunrise 15 ngày/15.000.000, Phố Núi trả theo đơn → 7 ngày, Homestay Mây Ngàn 15 ngày), suppliers HTX
Cao Nguyên, Bao bì Phú Mỹ, Điện lực Gia Lai; 2 products + 2 materials; lots as in stock.
- **readiness** — purpose: what is still missing to run safely, per the household's model; first read: "Sẵn sàng có
  điều kiện · 3 việc nên làm"; primary = the next recommended task. Pattern **checklist** (reuses `r-gate`: tone +
  type icon, one action each) grouped by area; done areas collapse. Assisted mode link (OPC staff sees the same list).
- **setup-business** — profile from the tax-code lookup ("OPC tra") + the business model (how you sell / where goods
  come from) and its consequence on the readiness plan; primary "Lưu". Pattern **form** (two short questions).
- **setup-data** — base data sets with counts and checks (đạt / cần sửa / nên có), import paths (Excel, ảnh, tay);
  primary "Nhập dữ liệu". Pattern **datatable**.
- **connections** — 17 categories grouped (Tiền · Hoá đơn & thuế · Định danh & tra cứu · Bán & giao · Hệ thống), each
  provider + state + freshness/consent + manual path; first read: the one error; primary "Thêm kết nối". **datatable**.
- **setup-policy** (owner view) — who does what (5 roles incl. Người giao link-only, Kế toán delegated with expiry) +
  approval rules with thresholds, the three roles explained (Trợ lý đề xuất · OPC kiểm tra · Người duyệt); changes need
  the owner's OTP; primary "Lưu chính sách". Pattern **form/list**.
- Machine: probe 0 (1440/1024/390 + stress), axe 0, text lg/xl clean (readiness area summaries wrap instead of
  truncating). Maker self-check — weakest: connections is a long 17-row table; the model checkboxes reuse c-option
  with a new box part.
- Eval: r1 8.0/7.8/7.8/8.2/8.0 → r2 8.0/8.0/8.0/8.2/8.0 (pass). Deferred: collapse "Đã đủ" to a count, unify row-action
  weights (Xem/Sửa/Bật), per-person permission editing path, connections filter by state on phone.

## v4.2.9 · Hàng hoá & bảng giá (BA F02.03–F02.05) · 2026-10-05 — inventory + pattern
Data: Bò một nắng 500g (gói, tự chế biến, lô, hạn 60 ngày, nhóm thuế chế biến) lẻ 260.000 / khách sạn 230.000;
Muối kiến vàng 100g (hũ, mua về bán, nhóm phân phối) 65.000 / 55.000; 2 nguyên liệu không bán. Two price lists:
**Giá lẻ** (mặc định: quầy + khách chưa gán, e.g. Homestay Mây Ngàn DH-2036 = 5 × 260.000 = 1.300.000) and **Giá khách
sạn & nhà hàng** (Sunrise Hotel, Nhà hàng Phố Núi — DH-2031 3 × 230.000 = 690.000). F02.05: only approved prices are
used → a price change is drafted by anh Khoa and approved by chị An (new policy rule, setup-policy now 8 rules);
orders already confirmed keep their price (DH-2052 stays 230.000).
- **products** — purpose: what we sell and at which prices; first read: the two products with both prices side by
  side; primary "Thêm món". Pattern **datatable** (price lists as columns).
- **product-detail** — one item: prices per list, unit/source/lot rule/shelf life/tax group, production recipe link,
  append-only price history; primary "Đổi giá". Pattern **detail**.
- **pricelist** — one price list: who uses it, items vs retail, effective date, scheduled change; primary "Đổi giá
  trong bảng". Pattern **datatable**.
- **pricelist--edit** — drawer: new price from a date, OPC checks (orders already confirmed keep the old price, not
  above retail, customers on the list), assistant drafts the customer notice; primary "Gửi chị An duyệt".
- Machine: probe 0 (1440/1024/390 + stress), axe 0, drawer traps 6 stops, text lg/xl clean; phone labels each price.
- Maker self-check — weakest: products list is short (2 items) so the page looks sparse at 1440; the tab "Nguyên
  liệu" points at stock.
- Eval: r1 7.8/8.0/7.8/8.7 → r2 8.0/8.0/8.0/8.5 (pass). Deferred: short tables at 1440 (max-width or two-up),
  live block state for the retail check, item thumbnails (photo of the pack).

## v4.2.10 · Pilot dashboard (BA UI-20, UC-07, F15.02–F15.05) · 2026-10-05 — inventory + pattern
Viewer: **PM Quang · Xem chương trình** (Program Viewer) — no household nav, no money/order/customer details; the
program sees each household's *stage and flags only* (consent given on joining). Pilot "Kế nghiệp số Gia Lai · đợt 1":
8 hộ = 2 hộ sớm (từ 01/07: An Nhiên, Gạo Ia Ly) + 6 hộ đợt 1 (vào 15/09–01/10). Funnel (BRD §6 success definition):
tham gia 8 → onboarding xong 6 → giao dịch thật 6 → hoá đơn 5 → kỳ thuế hoàn thành 1 (An Nhiên Q III; đợt 1's first
period is Q IV) → còn dùng sau 90 ngày 2/2 eligible. Need help (4 hộ): Mật ong Đak Đoa bị chặn (thiếu bảng giá, 6
ngày, inactive) · Măng khô K'Bang (TK ngân hàng cá nhân) · Cà phê Chư Sê (chưa có chữ ký số, Câu 2) · Gạo Ia Ly (kỳ
Q III còn 2 việc, hạn 31/10). Active 7 ngày 7/8. Aggregates only, groups under 3 households are merged.
- **program** — purpose: is the pilot really used, where to help; first read: the funnel; primary "Xuất báo cáo".
  Pattern **dashboard** (funnel + need-help by issue type + adoption by feature) because the viewer compares stages.
- **program--help** — the "Cần hỗ trợ" group opened: households × stage × issue × who supports × days (no data
  values). Pattern **datatable**.
- **program-report** — the controlled aggregate report (definitions, privacy rule, findings, proposals); document.
- Machine: probe 0 (1440/1024/390 + stress), axe 0, text lg/xl clean. Program shell: own nav (Tổng quan pilot · Hộ
  tham gia · Báo cáo · Dữ liệu được xem · Trợ giúp), no household switcher, no assistant, avatar Q.
- Maker self-check — weakest: funnel denominators differ for the last two stages (2 eligible) — marked with a
  hatched bar + the base in the sub-line.
- Eval: r1 7.8/7.8/7.8 → r2 8.0/8.0/8.0 (pass). Deferred: ▲/▼ on stat deltas, neutral hue for "Chờ chương trình",
  sticky report TOC, chevrons on need-help cards.

## v4.2.11 · Offline dùng chung + Scenario Switcher (FLOWS §0 nguyên tắc 8; BA UC-06 switcher) · 2026-10-05
**Offline pattern** (device has no internet, not a connector error) shown on picking DH-2052 in the store room
(weak wifi), 10:51–11:04. Three behaviours in one screen: (1) work continues and is **saved on the device** (ticks,
counts, cash sales); (2) actions that only need sending are **queued in order** with a duplicate-safe key (Soạn
xong, Zalo message) and can be cancelled while queued; (3) actions that need the server to stay correct are
**locked with the reason** — Bàn giao "cần mạng để trừ kho đúng một lần". Shell chip "Mất mạng · 2 việc chờ".
Reconnect: OPC sends in order, re-checks each; a conflict stops the chain and asks — here lot BMN-0405 was locked by
chị An at 10:52 (stock-lot--lock) while the device was offline → muối accepted, bò rejected, Zalo held; primary
"Soạn lại 20 gói từ BMN-0410" (còn 20).
- **delivery--pick--offline** (detail + banner) · **delivery--pick--queue** (drawer: queued items, order, rule) ·
  **delivery--pick--back** (reconnect result with one conflict).
**Scenario Switcher** — `demo.html`, a demo console outside the product (dashed "DEMO" frame, never in production
builds): the BA end-to-end path (UI-01 → UI-20) as steps, the exception cases (nợ quá hạn, thiếu tồn, hoá đơn chưa rõ
kết quả/bị từ chối, tiền không khớp, kết nối timeout, mất mạng, khoá lô), role to view as, simulated connector states,
demo clock, and Reset. `demo--reset` = confirm dialog (demo data only; type-to-confirm not needed, but names what is
lost). Pattern **dashboard/console** because it is a launcher of states, not a product screen.
- Machine: probe 0 (1440/1024/390 + stress), axe 0, drawer/dialog traps (4/3 stops), text lg/xl clean.
- Maker self-check — weakest: on phone the offline state relies on the banner (the shell chip is desktop-only); the
  demo console is a plain launcher (fine: it is not product UI).
- Eval: offline r1 7.8/8.0/8.0 → r2 8.0×3; demo r1 7.6/8.0 → r2 7.6 (6 controls hidden in a closed disclosure) → r3 8.0.
  Deferred: phone offline indicator in the top bar, guarded "Huỷ" in the queue, one control idiom for demo levers.

## v4.3 · Màn cũ sang dữ liệu An Nhiên (Quầy, Hôm nay, Tiền, Đơn hàng, Hoá đơn/Nhật ký, Cài đặt) · 2026-10-05
- Shell: `home43.py` rewrites screens/home.html (the shell every build() uses) → An Nhiên, anh Khoa, nav Hàng hoá →
  products, Sổ & thuế → period, Cài đặt → readiness; counts 3. `run_all.sh` rebuilds everything in order.
- Quầy (`src43.py` + states.py): 2 products as big tiles with "còn · đã giữ"; known-customer chips; DH-2053 = 2 gói bò
  + 3 hũ muối = 715.000 ₫ (FLOWS §0.1); "Thu tiền = phát hành hoá đơn máy tính tiền" (Q3); new `counter--debt` (Sunrise
  at the counter → hotel prices, debt needs chị An because overdue); `counter--offline` is now device offline
  (pending tone, QR off, invoice queued) instead of "MB lost".
- Hôm nay (UI-01): revenue 7.235.000 ₫ (5 đơn đã giao) split verified 4.745.000 / pending 390.000 / chưa thu 2.100.000;
  "OPC đang chạy 3 việc · 1 lỗi"; 3 to-dos (soạn DH-2052, MH-0118, DH-2047); Kỳ Quý III, khách còn nợ 17.700.000,
  Sẵn sàng có điều kiện. Overlays (Thêm, Thông báo, ⌘K, Trợ lý) and states (offline = device, firstrun = chị An).
- Tiền: 4 MB transfers today 5.720.000 (verified 4.745.000 · pending 390.000 · unassigned 585.000 → DH-2050); assign
  dialog gains "Chia cho nhiều đơn hoặc hoá đơn" (one-to-many).
- Đơn hàng (`orders43.py`): 8 orders today across Quầy / Zalo OA / Thêm tay / Định kỳ (source column), states per
  Phụ lục A; peek = DH-2052; bulk reminder = Phố Núi (Chị Hoa excluded: thu hộ at GHTK).
- Hoá đơn / phiếu / Nhật ký (`pages_books43.py`, replaces pages_books/pages_detail): mẫu số 2, two series (Hilo
  2C26MAN counter, X Invoice 2C26TAN), "Chưa rõ kết quả" never auto-resent, corrections via provider portal; accountant
  view = chị Lan, Tháng 9 matching the Q III reconciliation; audit (UI-19) with before → after, source, event id.
- Cài đặt (`settings43.py`): new sub-nav; users An / Khoa / Hạnh / Lan (+ Hùng link-only).
- Consistency fixes: DH-2054 (bus to Quy Nhơn) → DH-2043 (DH-2054 is the next counter order); "Chị Hoa (Shopee)" →
  Zalo OA (no marketplace in the model). Machine: probe 0 on all non-onboarding screens, axe 0, text lg/xl clean.
- Only onboarding (21) still shows Cô Hai → next task (Onboarding ⓪ redesign).
- Eval: r1 (8 screens) all ≥ 8.2 except money 7.9 → money hero = match state, actionable first → 8.0; home then 7.82
  (mirrored money figures) → summary in words, figures on Tiền → 8.0; counter 7.82 → idle hairline / in-cart raised → 8.0.
  Deferred: source as its own column in orders, actor colour tags in audit, idle tile shown in at least one counter state.

## v4.3.1 · Onboarding ⓪ · 2026-10-05
- `onboard43.py` snapshots the hand-edited onboarding screens once (src_v43/onboard_v42/) and rewrites them: An Nhiên
  data, 6-step counter, new `onboard-model`, done → `readiness--new`; `onboard_aside.py` step map + done preview.
  FLOWS ⓪ phần A note added (products stay in phase A because the test sale needs them; invoices → phase B).
- Eval: r1 8.0/8.4/7.8/8.4/7.8/8.4/8.0/8.0 → r2 model 8.0, products--review 8.0 (pass). Deferred: split the plan
  summary into three weights, phone tally on done, quieter stacked secondary buttons.

## v4.3.2 · Đóng ca + nộp tiền thu hộ (COD) · 2026-10-05 — inventory + pattern
Shift: ca sáng 07:00–14:00, cashier Hạnh (shell user = Hạnh), close at 14:02. Expected cash = đầu ca 500.000 + bán
tiền mặt 2 đơn 845.000 (DH-2055 5 hũ muối 325.000, DH-2057 2 gói bò 520.000) + thu hộ nộp về 1.150.000 (anh Hùng,
DH-2051 Phố Núi) − chi tiền mặt 50.000 (cước xe khách DH-2043) = **2.445.000 ₫**; counted by denomination 2.425.000 →
**thiếu 20.000 ₫** → reason required (under the 50.000 ₫ threshold: no approval, chị An is told). QR at the counter: 2
khoản 1.105.000 verified (DH-2053 715.000, DH-2056 390.000). Cash-register invoices 4, all with code. Other COD: nhà xe
Đức Long DH-2043 1.300.000 (bus leaves 16:30 → not this shift), GHTK DH-2046 260.000 (paid by transfer at the weekly
settlement). After close: keep 500.000 for the afternoon shift, hand 1.925.000 to chị An (she confirms on her phone).
- **shift-close** — purpose: close the drawer honestly; first read: phải có 2.445.000 vs đếm được 2.425.000 → thiếu
  20.000; primary "Đóng ca" locked with its reason. Pattern **form/checklist** (r-recon for the expected amount,
  denomination count, reason) because the job is a count and one decision.
- **shift-close--cod** — dialog at 12:40: anh Hùng hands over COD; count vs expected; primary "Đã nhận".
- **shift-close--done** — the shift report after close + chị An's confirmation of the hand-over. Pattern **detail**.
- Machine: probe 0 (1440/1024/390 + stress), axe 0, dialog traps 4 stops, text lg/xl clean. Links: Đóng ca from Quầy header, Hôm nay, Tiền sub-nav.
- Eval: r1 8.0/7.5/7.8 → r2 8.0/8.0/8.0. Deferred: matched-count collapsed state, decision dot variant in timelines, quieter rail figures.

## v4.4 · Menu trái mở rộng tại chỗ (phương án A) · 2026-10-05 — inventory + pattern
- Problem (audit of 123 screens): 7 rail items hid 20+ destinations behind sub-navs only visible after entering a
  section; dead links (Khách hàng, Nhà cung cấp, Trợ giúp, Giao hàng on 5 screens); one item counted in 2–3 badges;
  Nhật ký in two places; menu not shaped by business model or role; Cần xử lý last.
- Pattern: **expandable section rail** (Shopify admin / Linear sidebar) because the household needs to see every
  destination without guessing a parent, while the rail stays short: 7 sections; the current section is always open
  with its children (counts on children); other sections collapsed with a peek chevron and the summed count. On
  desktop/tablet the rail replaces the in-page sub-nav (hidden ≥ 721 px); on phone the sub-nav stays and "Thêm" shows
  the whole tree. Order by frequency: Hôm nay · Quầy · Cần xử lý · Bán · Hàng hoá · Tiền · Sổ & thuế; footer Cài đặt ·
  Trợ giúp. Counts once: Cần xử lý (2 cần quyết · 1 lỗi), Bán › Yêu cầu 3, Tiền › Thu chi & đối chiếu 2.
- Shaped by model (items appear only with the matching choice: Chế biến ← tự chế biến; Giao hàng, Khách hàng ← khách
  sỉ; Nhập hàng, Nhà cung cấp ← mua về bán) and by role (Thu ngân: Hôm nay · Quầy · Đơn hàng · Đóng ca; Kế toán: Sổ &
  thuế · Công nợ; Người giao: link only; Program viewer: own shell). Nhật ký lives in Sổ & thuế only.
- New destinations to close dead links: customers, customer-detail (Sunrise), suppliers, help.
- Eval: r1 nav 8.2 ×5, customer-detail 8.5, suppliers 8.0, help 8.2, customers 7.8 → r2 customers 8.0, suppliers 8.0. Deferred: err-tinted row rail vs you, '0 ₫' instead of '—', tfoot totals, one-child sections flat for roles, Calm hairline instead of boxed right panels.

## v4.4.1 · Tinh chỉnh menu + bảng (deferred from v4.4 eval) · 2026-10-05 — inventory + pattern
- Row tone by severity: a "needs you" row whose sign is err (overdue debt, failed connector, blocking shortage) gets the
  err edge + err tint (`c-table__row--err`, also auto via `:has(.c-sign--err)`) because the owner scans for the worst
  row first and blue/red must not look alike (receivables, receivable-detail, customers, connections, production-new).
- No balance = muted "0 ₫", not "—" (a dash reads as missing data): customers, suppliers. Quantities keep "—".
- List totals in `tfoot` where the page sub states a sum (customers 14.700.000 ₫, suppliers 6.050.000 ₫) so the figure
  sits where the eye ends; the sub keeps the count only.
- Role rails: a section left with one child renders flat with the child's name (cashier: Đơn hàng, Đóng ca; accountant:
  Công nợ) because a one-child disclosure is an orphan indent.
- Eval v4.4.1: customers, suppliers, receivables, receivable-detail, connections, shift-close, invoices--accountant all 8.0. Deferred: tighter table row height (system-wide), foot-note scope labels, faint link colour on needs-you rows.

## v4.5 · Anti-slop budgets — baseline (budget.mjs, 1440 first viewport, 2026-10-05)
- Skill: new `references/budgets.md` + `scripts/budget.mjs` (colour · icons · reading · lines & spacing · type),
  wired into evalpack facts + evaluator caps. Baseline OPC: 126/127 screens over budget —
  type 124 · reading 40 · icons 39 · spacing 27 · colour 17 (phone 390: type 125 · spacing 55 · colour 40).
- Root cause of type (system): 12 font tokens 14·15·16·17·18·19·20·22·24·28·34·44 (five within ×1.12) and
  weights 400·500·600·650·700·750·800·900. Proposal `tools/v4/proposal_v45.py` (sandbox `design/_proposal-v45/`):
  14·16·18·24·32·44, weights 400/600/700, wrapped titles lh 1.35, nested bold capped at 700 →
  type fails 124 → 0, spacing 27 → 21, probe 0 issues at 1440/1024/390-stress. NOT applied — waiting for approval.
- Per-screen work after the system change (content, not tokens):
  - reading (40): period 322 words, readiness 344, connections 330, program 305, order-detail 285, sales-inbox 278 …
  - icons (39): mostly status signs in lists (orders 8/100w) and counter dialogs; home--more 17.8/100w; delivery 17.
  - colour/tinted (17): counter payment/received states and onboarding result screens (large green/red areas).
  - spacing: r-order__opts / c-cashpad__field padding < 8px; rules on shift-close 18, demo 18, period 14.
- v4.5 applied (owner OK). Added rhythm checks to budget.mjs (stackGap, headAlign, ragged) after the owner caught
  period/order-detail. Eval g45 with caps: 7.0/7.4/7.6/7.2/7.8 — next: content pass per screen (cuts listed in
  _packs/v45 eval: period r-gate icons + sub-lines; order-detail Giao hàng as kv, timeline one line; orders drop
  icons on chip cells and labelled controls; home Cần làm one line, no leading icons; customer-detail one overdue colour).
- v4.5.1 g1 done (all ≥ 8.0, budgets pass). Deferred from eval: rail deviation as the loud value (period), bold current journey label, equal-width gate buttons, home money bar green vs revenue, credit bar label once. Next content groups by budget fails: reading (34), icons (24), colour/tinted (17), spacing (22).
- v4.5.2 g2 done. budget.mjs: new 'panel' kind (drawer/sheet ≥440px), collapsed <details> no longer counted. Deferred: connections action cell right edge, sticky Lưu chính sách, policy editable vs fixed rows. Remaining budget fails: icons 21 · spacing 18 · colour 17 · reading 13 (mostly counter/onboarding dialogs + home states).
- v4.5.3 g3 done. budget.mjs: controls + first action alert excluded from tint; icon-only buttons excluded from icon count; tinted offenders listed; input wrappers not 'cramped'. Deferred: process-step dot tone vs money tones; cart total as the largest figure.
- v4.5.4 done: 0/127 over budget. budget.mjs: iconRate only from 100 words; structured cards not 'cramped'; panel detection by layout size; animation wait capped at 800 ms and skips infinite animations (an earlier version hung on spinners — that was the long wait). Deferred: borderless count inputs, delta as the hero on shift-close, board column sums quieter.
- v4.5.5 done: 0/127 over budget at 390/1024/1440. budget.mjs: phone full-height sheets = panel; selection + sticky/fixed chrome not content tint; heading lh thresholds by size. Deferred: onboard desktop lower-right void, 'Sửa' links more visible; ~70 screens not re-scored by the Evaluator since v4.5 (machine + budgets clean).
- v4.5.6: all 127 screens scored since v4.5; home--more 7.8 (generic menu tree). Evaluator variance ±0.5 between rounds for the same screen. Deferred: borderless count inputs, 'Sửa' links more visible, onboarding desktop void.
- v4.5.7: every screen >= 8.0 on its latest round. Remaining polish (not blocking): sheet group rule tint, Quầy CTA vs current place, borderless count inputs, 'Sửa' links, onboarding desktop void. Evaluator variance ±0.5.
- v4.5.8: polish done. Two evaluators disagree by up to 0.5 on the same screen (home--more 8.0 → 7.5, onboard-done 8.0 → 7.6); Identity 7 keeps recurring on template-like screens (menu tree, onboarding steps, settings lists). Treat 7.5-8.0 as the noise band; next real gain is a user GATE decision on taste (show sheets to chị), not more evaluator rounds.
- v4.5.9: lesson — removing an element from a grid row (icon) can collapse the text into the icon column; probe only catches overflow/clipping, not sliver text. budget.mjs now has 'narrow'. Rule: after any bulk removal of icons/markup, run budget.mjs --all at 390 and 1440 and LOOK at 3 affected screens.
- v4.6.0: connector flow done (list + 6). Missing optional states: consent granted receipt, OTP wrong, consent expiring (MB 28/12). FLOWS.md/SCOPE should mention Kết nối as top-level + the flow (todo when CEO answers Câu 2).
- Rail count/chevron options compared in design/_explorations/rail-options.html (A current, B hover-chevron, C one right slot). Awaiting choice.
- v4.7.1: owner judged C+ ugly in the real UI. Lesson: mock-ups of one state (comparison sheet) hid the ragged x of floating counts; check the rule across all labels before adopting.
- v4.8.0: open questions for BA — (1) Casso: one login for Cas/QR Pay/GDT Hub or separate activations? (2) Zalo: one authorisation for messaging + ZNS or separate? (3) OTP channel if Zalo not connected yet (proposal: SMS). Design tolerates both answers (jobs are per account, scopes per job).
- v4.9.0: decisions I took for the owner — MVP delivery = default + assistant suggestion + human choice; aggregator vs direct carriers still a business decision (design holds both); cost/balance lines deferred. Open BA questions unchanged (Casso login, Zalo authorisation, OTP channel).

## v5.0.0 (2026-10-07)
- Decision: Zalo cá nhân removed from providers, sales copy and FLOWS (Zalo has an OA API only). Pasting a message into the Hộp yêu cầu stays as manual input.
- Decision: three custody modes (Casso / OAuth / pasted key) — OPC never sees passwords typed on Cas Link.
- **Unverified (check before release):** every guide step for payOS, Casso and S-Invoice is written from general knowledge, not from the portals; payOS field names (Client ID, API Key, Checksum Key) and signed webhooks; GHTK/GHN key fields; Shopee/TikTok Shop partner approval; Meta app review for Messenger; list of banks Casso supports beyond MB.
- Open: does one Casso login cover Cas / QR Pay / GDT Hub? (changes `mode` rows). Which CA for digital signatures (Câu 2)?
- Deferred polish: Client ID could note why it is not secret; the phone registry stacks labels plainly; connections--casso's "Mở trang nối" links to the GDT testing screen as a stand-in.
- Evaluator: guide-casso 7.7 and platform-provider--new 7.8 were tweaked after their last score.

## v5.1.0 (2026-10-07)
- Decision: features first (11 việc, 3 tiers) in onboarding (new step 4/7) and in Kết nối; providers are the choices. The 17-category table is replaced by the 11-feature view (mapping in connector-catalog.md).
- Decision: "require" = lock the dependent flow until a way is connected, not the whole app. Confirm with the CEO whether some việc should hard-block go-live.
- Decision (demo): identity + receive are due now; invoice + sign are due before the first wholesale order (because the model has khách sỉ).
- Open: tier rules for other business models are described, not drawn. Chữ ký số has no selectable way yet (Câu 2).
- Evaluator: onboard-features 7.7, onboard-feature 7.8, connections--feature 7.6, readiness--new 7.6 were fixed after their score, not re-scored.

## v5.1.1 (2026-10-07)
- Owner principle: OPC shows its own features and voice; it does not advertise other apps/providers. Rule: provider names are plain text and appear only where the owner chooses or manages them (Kết nối, chooser, hand-off page) or where the law needs it; never a logo/monogram in household screens; shared chrome never names a provider (`brand.py`).
- Round-2 scores 7.2–7.9 (none pass 8.0). The owner's requirement is met on every screen; the shortfall is Identity 7 (no signature move) plus density on readiness--new and connections. Candidate work: a distinct OPC voice element for the features list; demote the credential block on connections--manage; drop the decorative flow glyphs on onboard-bank.
- Non-Kết nối screens still name Hilo / X Invoice where they are the issuer of a specific invoice (invoices list, order detail): kept, it is data not promotion.

## v5.1.2 (2026-10-07) clean-up
- Eval packs before v500 and older screenshots are in `opc/_archive/design-cleanup-2026-10-07/`; manifest `eval.pack` values before v5 point there. Delete the archive when no longer needed.
- `tools/v4/README.md` is the only build guide now; `run_all.sh` is the order.

## v6.0.0 (2026-10-07) onboarding v6
- Principle: real, not BA-assumed. Platform-level services (OTP sender, photo reading) work before anything of the household is connected; household connections are gates just in time.
- **Unproven / to confirm** (4 questions drafted for the accountant, Casso, tax office): MST of a hộ (10 digits vs CCCD), which source returns hộ data, legal thresholds (500 triệu quarterly, 1 tỷ invoice, 3 tỷ costs, bank account notification), VNeID level 2 vs digital signature.
- OTP channel order Zalo → SMS is a default; prices not found, get quotes. Email only as recovery.
- Identity: Cas ID needs NFC and another phone to scan; VNPT eKYC / FPT.AI (camera on web) are untested alternatives. "Để sau" is allowed.
- Round 2: household 8.4, read 8.1, open 7.7, notfound 8.1, model 8.1; features 8.0, verify 8.2, app 8.0, failed 8.0, done 7.8; readiness--new 8.0, readiness 8.0, bank 7.6, assisted 8.0, products 7.8. Small fixes after (done title, bank "Để sau" button, verify disabled button) not re-scored.
- Open polish: onboard-products options all equal weight; onboard-bank rank; onboard-assisted expired state.

## v7.0.0 (2026-10-08) onboarding v7
- Principle: onboarding holds every mandatory item (law or chain); optional items visible with skip. Only mandatory connection: e-invoice provider (when the hộ must or needs to issue invoices).
- To confirm with the accountant before go-live: tax threshold (200 triệu vs 1 tỷ), filing period rule, bank-account notification form, TT 152/2025 book list, whether SmartCA-on-VNeID signs commercial invoices, free state e-invoice eligibility (NĐ 254/2026 Đ.11).
- Still pending in other screens (Đợt 1–5 of v7): menu per BA, removal of production/lots/credit-limit blocking, purchase record with partial payments, order 4 tracks, quarter summary, eTax progress.
- Round 2 scores: consent 7.7, unregistered 7.6, features 7.1, gov 7.8, bankacc 7.8, invoice--register 7.8, opening 7.6, done 7.6, readiness--new 7.8, verify 7.5.

## v7.1.0 (2026-10-08) đợt 1
- Menu follows the ERP chain (BA Screen Plan §3, research T16). Kết nối sits in Thiết lập; its error count shows on the collapsed group and on Tổng quan.
- Demo story now: An Nhiên buys bò một nắng 500g from Cơ sở Krông Pa (Gia Lai) and muối kiến vàng from HTX Cao Nguyên; no processing, no lots; expiry dates optional.
- Still old (to be rebuilt): counter/quầy + shift close (→ Bán nhanh, đợt 3), order-detail stepper + delivery picking with lots (đợt 3), purchases + purchase-receive with thịt bò (đợt 2), tax pages with computed tax (đợt 5), customers/receivables with credit limits (đợt 4).

## v7.2.0 (2026-10-09) đợt 2 Mua hàng
- Purchase order is optional for the household; "Hàng đã về, chưa có đơn" creates the record at receipt (KiotViet/QuickBooks pattern).
- Cost of goods: moving weighted average (bình quân gia quyền di động) is the proposed default; purchase shipping into stock value is optional. Both wait for the accountant (TT 152/2025 sổ hàng hoá quantity + value not yet verified from the full text).
- Open: segmented control (`c-seg`) selected state is subtle (evaluator, cross-screen). It is a shared component → fix in a system pass, not per screen.

## v7.3.0 (2026-10-09) đợt 3 Bán hàng
- Cash at the counter is no longer a shift: it is counted in Thu chi và đối chiếu (đợt 4 redraws that screen). Role "Thu ngân" is now "Nhân viên bán hàng".
- Walk-in customers who later want an invoice: issue from the order the same day. Cash-register e-invoice applies at the legal revenue threshold — accountant to confirm.
- Still old until đợt 4: customers / customer-detail / receivables / receivable-detail show credit limits and overdue as before (information only, to be checked), money.html.
- Open (evaluator): confirm step for "Giao thiếu"; on phone keep the Tiền track and primary action above the fold.

## v7.4.0 (2026-10-09) đợt 4 Tiền
- "Tiền khách trả trước" is a liability (customer money held), not revenue — accountant to confirm how TT 152 books show it.
- Open (evaluator, cross-screen): on phone the right "why/context" panel falls below the fold → consider an inline disclosure; demote "Agent soạn tin" buttons to tertiary; link Nhật ký from every money decision.

## v7.5.0 (2026-10-09) đợt 5 Sổ và kê khai
- Demo numbers: revenue before OPC 380.000.000 ₫ (onboard-tax) + Q3 338.400.000 ₫ = 718.400.000 ₫; run-rate ~1,06 tỷ vs the 760 triệu estimate at registration → OPC raises it (threshold + cash-register invoice).
- Provider names (Hilo, X Invoice) still appear as plain text on invoices, approvals--error, help, audit and home connection errors — places where the owner manages invoices; review with CEO if even that should go.
- Open (evaluator): one chip vocabulary across screens; one primary per screen; mobile variant of Diễn biến; numbered link between reconcile tasks and the 3-source panel.

## v7.5.1 (2026-10-09)
- CEO decision: provider names never appear on household screens (only where the owner picks/manages a provider: Kết nối, registration). Enforced by `relink.py` BRAND; add new names there.
- Open: one chip vocabulary across screens (evaluator v750) — not done; needs a token-level status map.

## v7.5.3 (2026-10-09) end-to-end audit
- Source of truth for demo numbers: design/_research/audit-e2e-v752.md. Change a number there first, then in facts7.py / the v7 generators.
- Still open (P3): ~40 secondary href="#" in older list screens (customers rows, books exports, setup-data, notifications); offline states for the new record screens; accountant/staff views of v7 screens; usability test with real households.

## v7.6.0 (2026-10-10)
- Open (eval v760): delivery board on phone is the weakest fit (columns become tabs); home has three meter styles (today bar, year meter, reconciliation strip) — unify later; customers / receivables keep the v4 layout (numbers now correct).

## v7.7.0 (2026-10-10)
- Detail pages are demo records (one customer, one order, one product): rows of other records link to the same detail screen. FE uses real ids.
- Offline queue: offline screens link to the existing queue drawer (delivery--pick--queue); a general sync-queue screen is open.
- Open: usability test with real households; accountant answers (emails in design/_research/emails-v7.md).

"""v4.2 hand-written handoff parts (the TODOs handoff.mjs leaves) for Control Tower, sales inbox and Order 360.
Replaces everything above the generated block; the generated block is kept. Usage: python3 handoff_v42.py"""
import pathlib, re
H = pathlib.Path(__file__).resolve().parents[2] / 'apps' / 'app' / 'handoff'

DOCS = {

'onboard-consent': """# Handoff — Mở hộ v7 (6 bước)

- Steps (onboard_lib.STEPS): 1 Số điện thoại + đồng ý dữ liệu · 2 Hộ kinh doanh · 3 Cách bán + Việc OPC làm · 4 Thuế và tài khoản · 5 Hoá đơn · 6 Số đầu kỳ → giao dịch đầu tiên.
- Consent: the mandatory box only; "cho Agent đọc tin nhắn" is optional and unchecked by default (Luật 91/2025).
- Hộ chưa có giấy đăng ký: `onboard-household--unregistered` — selling and invoices stay locked; products and prices can be prepared.
- Step 4 only asks whether VNeID level 2 and eTax exist; OPC never stores those passwords. Revenue before OPC + filing period are a suggestion from a versioned rule set "chờ kế toán xác nhận".
- Step 5 is the only mandatory connection (e-invoice provider, or the free state e-invoice if eligible). Waiting for the tax office's acceptance never blocks the next step.
- Step 6 confirms counted opening stock, cash, bank and debts once (or "Bắt đầu từ 0"); later changes go through an adjustment with a reason.
- Identity (onboard-verify*) and bank connection (onboard-bank*) are optional gates from Sẵn sàng (no step bar).
""",

'onboard-features': """# Handoff — Đăng ký bước 3/5: Việc OPC làm (màn thứ hai của bước 3)

- **Who:** chủ hộ. **First read:** 4 việc cần nối để bắt đầu. **Primary:** "Tiếp tục".
- Danh sách 12 việc sinh từ mô hình (màn trước), chia Cần để bắt đầu / Nên có / Khi cần (`tools/v4/capabilities.py`). Mỗi việc cần có sẵn một cách nối gợi ý + "Đổi" (`onboard-feature`), hoặc nhờ nhân viên OPC nối giúp. Chữ ký số: chờ chương trình chọn (chưa có cách để chọn).
- "Cần" nghĩa là khoá luồng phụ thuộc (tiền chuyển khoản, đơn sỉ, hoá đơn có mã), không khoá cả app.
- `onboard-feature` = chọn cách cho một việc: cách chọn được, "Sắp có" (bấm để OPC báo), nhân viên OPC nối giúp. Nút chính nêu tên cách đang chọn.
""",

'connections--category': """# Handoff — Kết nối › Việc OPC làm

- **Who:** chủ hộ, người vận hành (xem). **First read:** việc nào đang lỗi hoặc chờ (vạch đỏ bên trái). Thay bảng 17 nhóm cũ bằng 12 việc, 3 nhóm.
- Mỗi dòng: việc + nó làm gì | cách đang dùng + trạng thái bằng chữ | Xem / Chọn cách. `connections--feature` = một việc (cách đang dùng, thêm cách nữa, OPC làm gì, nếu không có cách nào).
- "Thêm cách nối" (`connections--add`) liệt kê cách nối theo từng việc, chữ thường, không logo; nhà cung cấp không là tiêu đề.
""",

'connections--key': """# Handoff — Nối bằng khoá (payOS) và các màn quản lý khoá

- **Who:** chủ hộ only (nhập, đổi, gỡ khoá). **First read:** khoá được giữ thế nào. **Primary:** "Thử kết nối" (chưa lưu gì cho tới khi qua thử).
- Ba cách giữ khoá (`mode` trong `tools/v4/providers.py`): **Nối qua Casso** (`connections--casso`: nhập mật khẩu ở trang Cas Link, OPC chỉ giữ grant), **Cho phép** (OAuth, chủ hộ OTP), **Dán khoá** (màn này). Khoá dán vào kho bí mật, sau khi lưu chỉ hiện 4 số cuối, không hiện lại.
- Form: Client ID (không bí mật), API Key và Checksum Key (che, nút Hiện), địa chỉ nhận báo tiền (chỉ đọc, nút Chép). Lỗi: `data-invalid` trên ô sai + banner "Chưa lưu gì".
- Quản lý (`connections--manage`): Thử lại · Đổi khoá (`--rotate`: khoá cũ chạy tới khi khoá mới qua thử; nút khoá tới khi dán đủ) · Gỡ (`--remove`: nêu hậu quả, nhắc xoá khoá ở nhà cung cấp). Mỗi lần ghi nhật ký.
- Hướng dẫn (`connections--guide`, `--guide-casso`): bước "Ở <nơi>", lỗi thường gặp, "Nhờ chị Thu". Nội dung cổng bên thứ ba CẦN KIỂM LẠI (xem NOTES).
- Trạng thái khoẻ hiển thị bằng chữ; biểu tượng chỉ cho việc cần chủ hộ.
""",

'platform-providers': """# Handoff — Bảng điều khiển nền tảng (QNSC): nhà cung cấp

- **Who:** quản trị QNSC (vai trò riêng, chỉ thấy số hộ, không thấy dữ liệu của hộ). **First read:** 4 nhà cung cấp cần xem. **Primary:** "Thêm nhà cung cấp".
- Bảng: nhà cung cấp · cách nối · trạng thái (kèm lý do chặn từ `GATE`) · số hộ đang nối · khoá nền tảng. Dòng cần xem có vạch bên. Phone: mỗi dòng xếp chồng, nhãn cột in trước giá trị (`data-l`).
- `platform-provider` (Casso): khoá QNSC, nơi Casso gọi về, nhà cung cấp đi qua, "Nếu gỡ Casso" (6 hộ, 11 nhà cung cấp). `--remove`: Ẩn (hộ đang nối vẫn chạy) hay Gỡ hẳn (ngắt, xoá khoá, không hoàn tác); lý do bắt buộc, nút khoá tới khi có lý do. `--new`: chọn cách nối + ô hộ phải nhập, xem trước "Hộ sẽ thấy", nút Lưu dính dưới.
- Danh mục là dữ liệu: thêm = thêm một dòng; ẩn = `visible:false`.
""",
'connections': """# Handoff — Kết nối (top-level) + luồng kết nối

- **Who:** chủ hộ (đồng ý), người vận hành (xem, làm tay). **First read:** kết nối nào đang lỗi (chấm đỏ trên menu, dòng đỏ trong bảng).
- Thẻ theo tài khoản (nối một lần, nhiều việc, bật/tắt từng việc) · `connections--category` = Việc OPC làm (12 việc) · `connections--add` thêm cách nối theo việc (danh mục nhà cung cấp là dữ liệu, 71 dòng) · tài khoản → `connections--account`; lỗi → `connections--detail`; chưa kết nối → `connections--provider`.
- Luồng: chi tiết → chọn nhà cung cấp → đồng ý (chỉ chủ hộ: phạm vi, 180 ngày, OTP Zalo) → đọc thử → `connections--unknown` nếu không trả lời → nhật ký.
- Quy tắc: OPC không tự gửi lại khi chưa rõ kết quả; mọi kết nối có đường làm tay; OPC không chuyển tiền, không nộp thuế. Nút Đồng ý khoá tới khi đủ 6 số.
""",

'customers': """# Handoff — Khách hàng (Bán › Khách hàng)

- **Who:** owner / operator. **Purpose:** see who owes what and open the one that needs action. **Primary:** "Thêm khách"
  (MST lookup fills name + address). Rows: name (row link) + type/channel, price list, terms + credit limit, owed, sign.
- Only customers with a profile can buy on credit, inside their limit and with nothing overdue (policy in Vai trò & duyệt).
- Tablet ≤1180: Bảng giá / Điều khoản columns drop (terms resurface as a sub-line), action column drops (row is the link).
""",
'customer-detail': """# Handoff — Khách hàng · chi tiết (Sunrise Hotel)

- Head: name + debt sign, the owed figure, limit + terms. Primary "Tạo đơn"; secondary "Nhắc nợ" (→ receivable-detail).
- Credit meter (used / limit) with the consequence line (overdue → credit orders need owner approval). Profile & terms
  (MST, orderer, delivery address, price list, invoice email, recurring order). Recent orders and open invoices.
- Right: conversation trail (Zalo OA reminders by the assistant, orders, owner approvals) — read-only.
""",
'suppliers': """# Handoff — Nhà cung cấp (Hàng hoá › Nhà cung cấp)

- Suppliers with terms, payable and status; the row needing the owner (short receipt) links to purchase-detail--receive.
- OPC never pays: money out is always made by the owner in her bank app; OPC matches the transfer afterwards.
""",
'help': """# Handoff — Trợ giúp & hỗ trợ

- Ask the assistant first (primary; answers about the current screen, never acts for the user); then people: call /
  Zalo OPC Gia Lai (chị Thu), book an on-site visit. 30-second guides deep-link to the screen. Right: live connection
  status (from Kết nối). Bug report attaches a screenshot; support sees the screen, never passwords.
""",

'onboard-model': """# Handoff — Đăng ký · Cách bán (bước 3/5)

- **Purpose:** decide which readiness items this household gets (FLOWS ⓪). Two multi-select questions: how you sell
  (quầy · khách sỉ/khách sạn · online) and where goods come from (mua về bán · tự chế biến); each option states what it
  adds to the plan; chosen = tint + hairline, the accent stays on the primary.
- Running summary right above "Tiếp tục": total items · required before wholesale · recommended · already done.
  Changing later = Cài đặt › Hộ & mô hình (recomputes Sẵn sàng, no data lost). "Chưa chắc" → staff help.
- Phase A (5 steps, v6.0.0): Số điện thoại · Hộ kinh doanh · Cách bán và việc OPC làm · Xác minh chủ hộ · Hàng đầu tiên → bán thử → Xong → `readiness--new`. Bank, invoices, e-signature are gates in Sẵn sàng.
""",
'readiness--new': """# Handoff — Sẵn sàng · hộ mới (sau đăng ký)

- Same page as `readiness` in state *Đang thiết lập*: counter usable; required items (before wholesale orders) with one
  verb each; recommended; done (collapsed). An item waiting on someone else (e.g. digital-signature provider, Câu 2)
  shows "Chờ quyết định" and no action. Primary = the first required item. Assisted mode: OPC staff sees the same list.
""",

'delivery--pick--offline': """# Handoff — Mẫu mất mạng dùng chung (FLOWS §0 nguyên tắc 8)

- **Device offline ≠ connector error.** Shell chip `c-health--off` (pending tone) "Mất mạng · n việc chờ"; banner
  `r-offbar` at the top of the content with "Xem n việc chờ". On phone the banner is the indicator.
- Three behaviours, decided per action (not per screen):
  1. **Works offline, saved on device:** picking ticks, counts, stock take, cash sales at the counter (only on the
     last-known available stock).
  2. **Queued** (`r-qchip` on the object, `r-queue` drawer): Soạn xong, messages, document photos — ordered, each with
     a client-generated idempotency key, cancellable while queued.
  3. **Needs the server, locked with the reason:** hand-over (stock leaves once), QR, invoices with a code, approvals,
     money out. Never fake success.
- Reconnect: send in order, re-check each on the server; the first item that needs a decision stops the chain
  (later items held). Example `delivery--pick--back`: lot locked while offline → part accepted, part rejected, message
  held; primary = the fix. Everything logged; nothing deducted twice. PWA install recommended on counter devices.
- `delivery--pick--queue` = the drawer; `delivery--pick--back` = the reconnect result.
""",
'demo': """# Handoff — Bảng điều khiển demo (demo build only)

- Not part of the product: render only when the build flag `DEMO=1` (and route `/demo`); dashed "DEMO · không có
  trong sản phẩm" frame. A floating "Demo" pill may open it from any screen in the demo build.
- Levers (sticky): view-as role (owner, operator, cashier, accountant, programme viewer), demo clock (named
  snapshots), simulated connector states per connector (Hoạt động · Không trả lời · Lỗi · Chưa kết nối · Mất mạng).
- Path: the BA end-to-end flow as 10 deep links (UI-01 start). Scenarios: 8 exception cases, each a deep link with a
  preset (role + clock + connector states). Reset (`demo--reset`) restores the seed data set (FLOWS §0.1) and default
  connector states; it never touches real data (the demo build has no real connectors).
""",

'program': """# Handoff — Pilot dashboard (Program Viewer)

- **Who:** programme manager (role Program Viewer). Own shell: Tổng quan pilot · Hộ tham gia · Báo cáo · Dữ liệu được
  xem · Trợ giúp; no household switcher, no assistant, no write actions on household data.
- **Data rule (F15.05):** aggregates only; households appear with stage and flags, never money/orders/customers/
  invoices; groups under 3 households are merged; households consent to this level on joining (TrustLine on every page).
- **program:** stats with last-period movement; funnel along the BRD success definition on one base (joined → set up →
  real sale → invoice); smaller-base steps (one tax period done, still used after 90 days) in a separate labelled group
  with hatched shorter bars; need-help by issue type (each links to the household row); adoption by feature (30 days).
  **Primary:** "Xuất báo cáo". Recomputed nightly.
- **program--help:** households grouped Cần hỗ trợ / Ổn × stage × issue × who supports × days; read-only.
- **program-report:** KPI table with definitions and base rows, findings, proposals (S16.09 30/90-day review); "Tải PDF".
""",

'products': """# Handoff — Hàng hoá · Danh sách & giá

- **Purpose:** what we sell and at which approved prices. **First read:** items with every price list as a column
  (default marked "mặc định"). **Primary:** "Thêm món" (secondary: photograph a price list — the assistant reads it,
  the owner reviews each line).
- Rule above the grid: counter + customers without a list → retail; customers assigned to a list → that list;
  confirmed orders keep the price at confirmation. Item facts: unit/barcode, source (bought / own production with
  recipe), lot + shelf life, tax group, available stock (muted). Materials live in Tồn kho.
- `product-detail`: prices per list (default leads), facts incl. recipe, append-only price history with approver.
  **Primary:** "Đổi giá".
""",
'pricelist': """# Handoff — Bảng giá riêng (khách sạn & nhà hàng)

- **Purpose:** one customer price list. Items vs retail with the delta emphasised, effective date, customers on the
  list (rail). **Primary:** "Gán thêm khách"; row action "Đổi giá".
- `pricelist--edit` (drawer): new price + effective date + reason; OPC checks: not above retail (blocks sending when
  violated), confirmed orders keep the old price (list them), affected customers; optional customer notice drafted by
  the assistant, sent only after approval. **Primary:** "Gửi chị An duyệt" — the price is not used until approved
  (BA F02.05; policy rule "Đổi bảng giá → chị An duyệt").
""",

'readiness': """# Handoff — Sẵn sàng (readiness) · v6.0.0

- **Purpose:** everything a hộ kinh doanh needs to run end to end, by chain: Hộ và người · Bán và thu · Mua và trả · Chế biến và kho · Thuế và sổ (33 việc, `readiness_model.py`). **First read:** state + "còn n việc".
- Each chain: open **bắt buộc** items with the flow each one locks (never the whole app), "Nên có" always visible, "Làm sau" and "Đã xong" folded with their names. Failing connection = error edge, never blocks other items.
- Rules, not fixed lists: tiers come from the model chosen at step 3 and from doanh thu lũy kế (quý khi vượt 500 triệu, hoá đơn máy tính tiền từ 1 tỷ — to be confirmed by an accountant). Assisted mode shows the same list.
""",
'setup-business': """# Handoff — Hộ & mô hình kinh doanh

- Profile filled from the tax-code lookup (connector #10; manual: type it in); OPC never edits registered data —
  fix at the tax office, then "Tra lại". Two questions (multi-select): how you sell (quầy · khách sỉ/khách sạn ·
  online/sàn) and where goods come from (mua về bán · tự chế biến); each option shows its consequence on the plan and
  tax group. **Primary:** "Lưu" = recompute readiness; no data is deleted when an option is turned off.
""",
'setup-data': """# Handoff — Dữ liệu nền

- Data sets (customers + terms/limits, products & price lists incl. per-customer prices, materials, suppliers, opening
  stock by lot, opening receivables/payables) with count and check (pass · cần sửa · nên có). **Primary:** "Nhập dữ
  liệu": photo (assistant reads, owner reviews each line — recommended), Excel template (row-level errors), tax-code
  lookup, OPC staff entry (logged).
""",
'setup-policy': """# Handoff — Vai trò & ngưỡng duyệt (owner)

- Roster first: Chủ hộ · Người vận hành · Thu ngân (Thu tiền = issue the counter invoice) · Người giao (link only, no
  account) · Kế toán (delegated with an end date; view + drafts, never approves or files).
- Approval rules: rule · who decides · threshold (range-validated). Locked rules (lock period, approve tax, file, pay,
  move money) cannot be delegated (N-06/N-07). Templates Mặc định / Chặt hơn. Saving needs the owner's OTP; every
  change goes to the audit log with before/after. The rail explains the roles: Trợ lý đề xuất · OPC kiểm tra · Người
  duyệt · Kết nối.
""",


'period': """# Handoff — Đối chiếu kỳ (Quý III/2026)

- **Purpose:** is the period clean enough to lock. **First read:** "Cần xem · 5 việc" + the to-do list; the rail
  answers "do the sources match?" on the same screen. **Primary (head):** "Gửi chị An khoá kỳ", locked "còn n việc";
  enabled in `period--ready`. Lock belongs to the owner or the accountant; the operator sends the request.
- To-dos (FLOWS ⑤ step 2): delivered order without invoice · invoice without tax-authority code ("Chưa rõ kết quả":
  ask the provider, never re-issue) · money not assigned · input invoice on the tax portal not in the books ·
  expense without invoice (accountant decides). Each has its figure and one action; done checks collapse.
- Three sources (base = revenue from delivered orders): invoices in OPC · coded invoices on the tax portal (manual
  upload by the accountant while the portal is not connected) · money (received + receivable + unassigned). Each gap
  links to the to-do that clears it. OPC re-runs checks nightly and after every decision.
- Lock = period data frozen; changes after that need "mở lại kỳ" with approval and reason. Next: Tính thuế (UI-15).
- `period--item` (drawer): one exception decided in place; options with the assistant's pick; "Lưu quyết định"
  re-runs the checks. `period--ready`: all match, decisions listed with who/when.
""",
'books': """# Handoff — Sổ sách (sổ doanh thu)

- **Purpose:** the household's books, built from orders, invoices and bank records — never typed. **First read:**
  month revenue figure; rows needing attention tinted. **Primary:** "Xuất sổ".
- Tabs Doanh thu · Chi phí · Tiền · Kho (same table shape). Rows: date · document + description · amount · invoice
  state (clean rows quiet "có mã" in the ok tone; exceptions with chip + tint). Counter invoices may be grouped per day.
- Template: S1a per TT 152/2025 — shown as "kế toán chưa đối chiếu với văn bản gốc" until the accountant verifies
  (CEO B24); the exported file carries the same note. To change a line: fix the source record or post an
  adjustment with a reason (append-only).
""",

'production': """# Handoff — Hàng hoá · Chế biến

- **Purpose:** what is being made, what is blocked. **First read:** tinted LCB-0413 "Thiếu 28 kg thịt bò".
  **Primary:** "Lập lệnh chế biến". Live rows (blocked, running) have bordered actions; done rows quiet.
- **Why datatable:** a short list of comparable orders. Columns: Lệnh · Ngày · Gói ra / dự kiến ("– / 40" until
  finished; dash grey) · Lô (lot code = order number: LCB-0412 → BMN-0412) · one status token.
- States (FLOWS Phụ lục A): Nháp · Đang làm · Xong · Đã huỷ. Simple production only — no BOM/MRP; OPC learns the
  usual inputs and yield from the last runs.
""",
'production-new': """# Handoff — Lệnh chế biến (nháp) LCB-0413

- **Purpose:** plan a run; see at once whether it can start. **First read:** materials check — "Thiếu 28 kg".
  **Primary:** "Bắt đầu" (locked with its reason while short); "Lưu lệnh nháp" secondary.
- OPC computes materials from the last 3 runs (label "OPC kiểm tra"); never issues more than available (no negative
  stock). The cure sits under the shortage: incoming receipt waiting for the owner (link to purchase-detail--receive), else
  "Tạo đơn mua phần thiếu".
- Start = issue materials, deducted once; finished goods enter stock only when the result is recorded.
- Rail (quiet): the lot that will come out (code, expiry = production date + shelf life).
""",
'production-detail': """# Handoff — Lệnh chế biến đang làm / ghi kết quả

- **Running (`production-detail`):** head figure = expected output "40 gói" with the usual band (39–40 from 34 kg)
  — the finish step checks against it; journey owns "now", timeline holds history; materials issued table.
  **Primary:** "Ghi kết quả".
- **Finish (`--finish`, 16:05):** actual vs expected sheet (reuses `r-count`): yield, raw used (unused part goes back
  to stock), seasoning. Yield outside the usual band → "OPC kiểm tra" asks for a reason (Sấy quá khô · Bỏ phần hỏng ·
  Cân sai · Khác), empty by default; primary "Nhập kho 38 gói" locked with its reason. Result: new lot BMN-0412,
  expiry 05/12, sellable at once; optional print of lot labels (public trace page only if the owner turns it on).
""",

'stock': """# Handoff — Hàng hoá · Tồn kho

- **Purpose:** can I sell, do I need to buy — per item. **First read:** the tinted raw-beef row (6 kg, below 20 kg,
  35 kg waiting for the owner's receipt). **Primary:** "Kiểm kê". Row action on the exception: "Nhận hàng".
- **Why datatable:** few items, the same comparable numbers per row; lots are children shown inside the row.
- Columns: tồn thực · đã giữ cho đơn (links the order) · **khả dụng** (truth column = thực − giữ). Counter and new
  orders sell only on khả dụng; FEFO picks the nearest-expiry lot. Stock leaves once, at hand-over.
- Quiet line: no lot expiring in 7 days (else a pending banner with "bán trước tại quầy"). Phone: thực/giữ fold
  into the item cell, khả dụng right; healthy "Xem lô" actions hidden (the lot links stay).
""",
'stock-lot': """# Handoff — Lô hàng · truy xuất hai chiều

- **Purpose:** where this lot came from and where it went; its stock ledger. **First read:** 26 gói (20 giữ · 6 bán
  được) · hạn 15/11. **No primary** (reading page); "Khoá lô" is a quiet danger button → `stock-lot--lock`.
- Balance line from OPC kiểm tra first: made = reached customers + in stock; if it does not balance, show the gap as
  an error sign and link the stock take.
- Từ đâu: supplier → PO → raw lots (qty used) → production order (yield). Tới đâu: orders/customers (counter sales
  grouped "khách lẻ tại quầy, n gói", known customers counted) → still in stock.
- Ledger: append-only, newest first; holds are listed but do not change on-hand. Adjustments only via stock take.
- Lock dialog: worst consequence first (who already received it; assistant drafts notices, owner sends), then
  in-stock effects (stop selling; held units move to another lot if available, else the order shows "thiếu hàng"),
  reason required (empty), reversible with a reason. Anyone with stock rights can lock; owner is notified.
""",
'stock-count': """# Handoff — Kiểm kê

- **Purpose:** count, see differences, send them for approval — stock is never edited directly. **First read:**
  "2 dòng lệch". **Primary:** "Gửi chị An duyệt", locked with its reason until every difference has a reason.
- Selling continues during the count: OPC snapshots book quantities at start and nets out sales made meanwhile.
- Per line: counted input (decimal for kg) · difference (loud) · reason (Hỏng · Hao hụt · Đếm sai · Khác) + note;
  the assistant may suggest a reason from history (label "Trợ lý gợi ý"). Matched lines recede.
- Result line: approval writes n adjustments to the ledger, value at cost. Desktop pins the gate; phone keeps it in
  flow (tab bar owns the bottom). Approval appears in Cần xử lý for the owner.
""",

'purchases': """# Handoff — Mua hàng · Đơn mua (v7.2.0)

- **Purpose:** what was bought, what is still coming, what is owed, what needs the owner. **First read:** the tinted rows
  (MH-0118 về 45/50, MH-0122 Agent proposal). **Primary:** "Tạo đơn mua"; quiet "Hàng đã về, chưa có đơn" (PO optional).
- Columns are independent tracks: Nhận hàng · Chứng từ · Tiền · Giá trị. Filters: Cần chị · Đang về · Còn nợ · Lệch chứng từ.
- Tabs Đơn mua · Chi phí · Trả hàng. `purchases--expense`: expense outside stock from a photo; never part of cost of goods.
""",
'purchase-detail': """# Handoff — Hồ sơ đơn mua (v7.2.0)

- **One record, 4 sections** (Hàng mua · Nhận hàng · Chứng từ · Tiền đã trả) + Diễn biến (append-only timeline).
  Header shows `r-tracks` (Nhận hàng · Chứng từ · Tiền), each with its own state: wait / pend / you / ok / err. Never a stepper.
- **Receiving** (`--receive`): counted quantity per line (`r-qty`), optional expiry, receiver. Short → wait for the rest
  (receive again on the same PO) or close short. Confirm = stock in once by the counted quantity; result line shows stock
  before → after and the payable (by received quantity) with due date. Over-delivery: count above ordered → owner accepts
  the extra (new line, priced) or returns it.
- **After confirm** (`--received`): success banner, editable the same day (then a correction entry, never a silent edit).
- **Documents:** supplier e-invoice (mailbox or photo) matched with PO and receipt. Mismatch → the seller issues the
  adjustment invoice; the household never edits the seller's invoice; Agent drafts the message, the owner sends.
- **Money** (`--pay`): many payments per PO, before or after receipt; buying on credit with due date; one payment may
  cover several POs of the same supplier (đợt 4). OPC records only; optional supplier VietQR opens the owner's bank app;
  the bank feed (if connected) matches it.
- **New** (`purchase-new`): Đặt hàng trước | Hàng đã về, chưa có đơn; terms Trả khi nhận | Mua chịu | Trả trước một phần.
  Agent may propose (reason + supplier quote shown); nothing is sent before the owner approves.
- **Return** (`purchase-return`): from a received PO; stock out (not a sale), reason, photo of the signed return note;
  supplier offsets the next PO, refunds, or replaces; seller issues the adjustment invoice (rule to confirm with the accountant).
- Cost of goods: moving weighted average (proposal, accountant to confirm).
""",

'money--split': """# Handoff — Gán tiền (v7.4.0): một lần trả nhiều hoá đơn · trả dư · có thể trùng

- Source: bank feed (if connected) or the owner's confirmation. OPC proposes, the owner confirms; OPC never moves money.
- **Split** (`money--split`): transfer + suggested allocation table (oldest invoice first; editable inputs; footer total must equal
  the transfer). Underpaid → oldest first, rest stays as debt. Result line names the invoices/orders that close.
- **Overpay** (`money--overpay`): extra → "tiền khách trả trước" (customer credit, not revenue, offsets the next order on
  confirmation) or refund by the owner through her bank app (OPC records the payout).
- **Duplicate** (`money--duplicate`): same sender, amount, memo, < 10 min, one copy missing from the statement → owner picks;
  "Bỏ" hides from Thu chi but keeps it in Nhật ký; "Để sau" keeps it in Cần xem.
- **Cash** (`money--cash`): count once a day, total only; expected = opening float + cash sales − cash expenses; a difference
  needs a reason and owner approval; deliverer COD hand-ins are logged with person + time.
""",
'customer-statement': """# Handoff — Bảng kê công nợ (v7.4.0)

- Per customer and period: invoices with due date and remaining amount, total, customer credit, orders not yet invoiced.
- Agent drafts the Zalo OA message with PDF + QR of the household account (memo = customer code); the owner sends.
""",
'tax': """# Handoff — Kê khai (v7.5.0)

- **Never show a computed tax amount in the pilot.** Show: quarter revenue (with / without invoice, link to the reconcile item),
  year-to-date vs revenue thresholds from versioned rule data (`ruleSet`, status "chờ kế toán xác nhận"; conflicting values shown),
  other mandatory notices (bank accounts, annual revenue) with state, and tracks Đối soát kỳ · Kế toán xem · Nộp trên eTax · Cơ quan thuế.
- `tax--return`: 6-step guide for eTax (VNeID level 2; choose form; copy revenue — copy buttons; eTax computes; sign; save notice).
  Banner "không phải tư vấn thuế". Download the evidence pack.
- `tax-file`: the owner uploads the eTax notices; **tiếp nhận** (received, transaction code) and **chấp nhận** (accepted) are separate
  states; reminder after 3 days without acceptance. `tax-file--signed`: accepted; edits after lock = amendment; tax payment is
  recorded only from the owner's payment document.
- `tax-evidence`: books (TT 152/2025 forms, PDF + Excel), e-invoices XML+PDF, bank statement, purchase documents (incl. photos),
  lock record, eTax notices, append-only change log; kept 10 years; accountant = view/download.
""",
'receivables': """# Handoff — Tiền · Công nợ (phải thu / phải trả)

- **Purpose:** who owes how much and what is overdue; who must be paid and when. **First read:** the total and the
  drill-in tile (overdue customer / next payable). **Primary:** "Xem & nhắc" on the overdue row; on Phải trả the only
  accent is "Trả 4.800.000 ₫" (bank-app deeplink, the owner confirms — N-06/N-07).
- **Why datatable:** many counterparties with comparable attributes, scanned and sorted; same family as Đơn hàng and
  Hoá đơn (r-listhead + ≤ 5 columns, stacks on phone).
- Rules (FLOWS ②b 16–19, ③ 8–10): a receivable exists only after an invoice is issued (delivered-not-invoiced shows
  as "Chưa tính"); carriers and bus companies holding COD are receivables tagged "thu hộ"; paying is never done by OPC.

## States
`receivables` (Phải thu) · `receivables--payables` (Phải trả). Not drawn: nothing owed, payment not confirmed by the
bank after 1 day ("Chờ xác nhận", owner marks it with a receipt), filters by age bucket.
""",
'receivable-detail': """# Handoff — Công nợ của một khách (bảng kê, nhắc nợ, gán tiền)

- **Purpose:** chase overdue politely and apply payments correctly. **First read:** owed now 8.400.000 ₫ (2 overdue
  invoices). **Primary:** "Gửi bảng kê & nhắc nợ" under the assistant's draft (the person presses send).
- Data: open invoices (amount, due, days overdue) · "Chưa tính" upcoming invoice · paid history (folded) · reminder
  timeline (assistant via Zalo OA, owner's promises from approval reasons).
- `--assign`: a transfer without an order code → choose invoices (suggestion = exact sum, oldest first); "đủ" is
  arithmetic; the money stays "chờ xác minh" until the bank statement matches; alternatives: prepayment for a coming
  invoice, customer credit, not this customer. Never auto-assigned.
""",

'delivery': """# Handoff — Bán · Giao hàng hôm nay (board)

- **Purpose:** get today's orders picked, handed over and delivered with proof; cash collected accounted for.
  **First read:** the urgent card ("Gấp · trước 15:00") and the raised failed card. **Primary:** "Soạn hàng" on the
  most urgent card (one filled button per view).
- **Why board:** shipments move through 4 stages and the household moves them; a status column would hide the flow.
  Phone: one stage at a time with stage tabs. Drag is not required — every move is a button on the card.
- Flow: `FLOWS.md` ②b steps 9–13. Methods: own staff · pickup · bus parcel · carrier (not connected / connected); COD.

## Data & content
| Field | Source | Format | Empty | Truncation |
|---|---|---|---|---|
| Column, count, COD subtotal | shipments by stage for the day | header | "không thu hộ" | — |
| Card | order code, customer, lines, due/time, method + deliverer/carrier + tracking, COD, state | `r-board__card` | — | wraps |
| Carrier state | connector #13 status; in the demo labelled `c-sim` "Mô phỏng" | `c-sign` + `c-sim` | — | — |

## States
Board (today). Not drawn: empty day, all done, carrier error, partial delivery card, bus parcel waiting at the depot.

## Interactions
Soạn → `delivery--pick`; Bàn giao (from Đã soạn) deducts stock once and sends the deliverer a link; failed card:
Giao lại (new attempt) or Hoàn về kho (re-stock after check). Date switch "Hôm nay".

## Accessibility
Each column is a region labelled by its heading; cards are articles labelled by the customer; state is words + icon.

## Open questions
Which carriers to connect first (category #13) — CEO, not blocking.
""",
'delivery--pick': """# Handoff — Soạn hàng → bàn giao

- **Purpose:** pick the held lines (shelf + nearest expiry hint, no lots) and hand over. **First read:** "1/2 món xong". **Primary:** "Bàn giao
  cho anh Hùng" — `aria-disabled` with the reason on the button until every line is complete; secondary "Giao thiếu · N" (add a confirm step)
  edits the order to what is delivered and creates a new order for the rest; the invoice follows delivered quantities.
- Hand-over sends the deliverer link; **stock leaves once** when the deliverer reports delivered (Đã giao).
""",
'delivery--courier': """# Handoff — Link giao hàng (người giao, không cần tài khoản)

- **Purpose:** the deliverer records the outcome on his phone from a Zalo link (signed, single-order, expires after
  delivery). **First read:** customer + address; the COD amount is the largest figure. **Primary:** "Đã giao xong",
  locked until a photo **or** the receiver's name exists. Problems are a second tier: Giao một phần · Không giao được.
- COD: cash (handed in at day end, reconciled like closing a shift) or the household's QR (money goes straight to the
  household's account). No app shell, no navigation, one job.
""",

'approvals': """# Handoff — Cần xử lý (Control Tower của chủ hộ)

- **Purpose:** every job OPC and the assistant are running for the household, and the ones that need a person.
  **First read:** the selected job's title and the decision panel. **Primary action:** the decision (Duyệt đơn).
- **Why split (list + detail):** a stream of jobs, each needs reading before acting (triage one by one); jobs are not
  compared side by side, so not a table. Phone: list → `approvals--detail` page.
- Flow: `system/FLOWS.md` ② (and every flow's exceptions). Rules: `SCOPE-MVP.md` §7 #19.

## Data & content
| Field | Source | Format | Empty | Truncation |
|---|---|---|---|---|
| Tabs + counts | workflow state: waiting_human · running · waiting_connector · error (retry_scheduled/blocked) · completed today | count | 0 hides the count | — |
| Row state, time, title, situation, source | workflow: state, updated_at, subject (order/purchase/invoice…), summary, source channel/actor | `c-sign`, HH:MM | — | title 2 lines |
| Timeline steps | workflow events with `actor_kind` = assistant · rule · person · connector | role label + time + what + detail | — | — |
| Rule checks | rule results per check (khách, giá, tồn, công nợ) | pass/fail chips | — | — |
| Decision | approval task: problem, impact figure, assistant proposal, allowed approvers, required reason | — | reason starts empty (placeholder only) | — |

## States
`approvals` (Cần chị quyết) · `approvals--running` · `approvals--error` (invoice outcome unknown) · `approvals--detail`
(phone). Not drawn yet: Chờ kết nối tab, Xong hôm nay tab, empty ("Không có việc nào cần chị"), approval of a short
goods receipt (HTX), blocked after re-check.

## Interactions
- Duyệt / Từ chối need a reason (min 5 characters); after approval OPC **re-validates** (stock, credit, order version)
  and the job either continues or returns as blocked with the new reason. Undo is not offered for approvals.
- Error (outcome unknown): no automatic resend; OPC re-polls on a schedule (shown as a chip). "Phát hành lại" stays
  `aria-disabled` until the owner confirms on the provider portal that no invoice exists.
- Keyboard: tabs are a tablist (arrow keys); rows are links; ↑/↓ moves the selection on desktop (to build).

## Accessibility
Main landmark; list `aria-label`; selected row `aria-current="true"`; rule chips carry "đạt / không đạt" text; the
decision is a `group` labelled by its question.

## Open questions
Câu 1/2 (tax filing, invoice type) do not affect this page. Counts in the nav = Cần chị quyết + Lỗi.
""",
'sales-inbox': """# Handoff — Bán · Yêu cầu (một hộp cho mọi nguồn)

- **Purpose:** turn messy requests (Zalo OA, pasted chats, photos, voice, files, standing orders) into a valid order
  without retyping. **First read:** the original message, then "Trợ lý hiểu là". **Primary action:** "Kiểm tra giá,
  tồn, công nợ" (or "Gửi qua Zalo OA" when something is missing).
- **Why split:** a stream of requests read one by one. Phone: list → detail page (to draw).
- Flow: `FLOWS.md` ②a. Channels: `SCOPE-MVP.md` §7 #11b; connector categories §8 (#11 chat, #15 AI).

## Data & content
| Field | Source | Format | Empty | Truncation |
|---|---|---|---|---|
| Source + time + who added | request: channel (zalo_oa / manual_paste / photo / voice / file / standing), received_at, added_by | icon + text | — | — |
| Original | request payload (text, image, audio transcript, file) | quote; uncertain spans marked | — | full |
| Lines | assistant extraction: said_text → matched SKU, qty + unit, price (customer price list) | table, stacks on phone | "Chưa rõ" | — |
| Customer, delivery, invoice, missing | extraction + customer profile | `c-kv` | "Chưa có hồ sơ" | — |

## States
`sales-inbox` (all matched) · `sales-inbox--unclear` (ambiguous quantity → question) · `sales-inbox--add` (manual add).
Not drawn: reading in progress, voice transcript view, unknown customer → create profile, duplicate request, ignored.

## Interactions
"Kiểm tra" runs the rule checks: all pass → draft order + reservation → Order 360; any fail → job in Cần xử lý (the
Sunrise demo fails on credit, hence the link to approvals). Nothing is created before the checks. "Gửi qua Zalo OA"
sends the assistant's question only after a person presses it; customers who never messaged the OA cannot receive
it → call or personal Zalo, then "Tự sửa".

## Accessibility
Table region focusable with a label; uncertain line has text "Chưa rõ", not colour only; dialog traps focus (inert).

## Open questions
Which pilot hotels already use the household's Zalo OA (affects how many requests arrive by manual add).
""",
'order-detail': """# Handoff — Đơn bán (v7.3.0)

- **One record**: Hàng bán · Giao hàng · Hoá đơn · Tiền + Diễn biến. Header `r-tracks` Đơn · Giao · Hoá đơn · Tiền; each track
  moves on its own (an invoice error never touches stock or money). Never a stepper.
- **Confirm** only within available stock (otherwise Cần xử lý: sửa số lượng / chờ hàng về); confirm holds the goods.
- **Đã giao** = delivered in full → stock out once (preview before → after) + one e-invoice for the order (buyer company + MST
  captured on the order; walk-in buyer: name / MST / personal ID optional). Short delivery = order edited to what was
  delivered + a new order for the rest.
- `--invoice-error`: tax authority rejected (no code yet) → fix the field, resend the same invoice; no adjustment invoice.
- `--return`: household is the seller → OPC drafts the adjustment invoice, the owner signs/sends via the e-invoice provider;
  restock only when "Còn tốt"; receivable reduced or refund. Rule awaits the accountant.
- Credit and overdue debt are shown as information, never a gate. The order closes when money is linked.
""",
'quick-sale': """# Handoff — Bán nhanh (v7.3.0, replaces Quầy + Đóng ca)

- Walk-in sale: search/quick-add goods, steppers, retail price list, pay by QR (household account) / cash / debt, optional
  "Khách cần hoá đơn". Result line before the primary: order number, stock out once, money recorded when matched.
- `--qr`: VietQR of the household's own account with the order code as content; bank connected → OPC matches automatically;
  not connected → the owner checks her bank app and taps "Tôi đã thấy tiền về". OPC never moves money.
- `--done`: one order, all four tracks closed at once; Bán tiếp · In phiếu · Khách cần hoá đơn (issue from the order same day).
- Cash is counted in Thu chi và đối chiếu (no shift close). onboard-firstsale reuses `--qr` as a test sale (no revenue, no stock).
""",
}
POINTER = lambda base: f"""# Handoff — state of `{base}`

This is a state of `{base}.html`; intent, data, interactions and accessibility are in `{base}.md`.
"""
STATES = {'tax--return': 'tax', 'tax-file': 'tax', 'tax-file--signed': 'tax', 'tax-evidence': 'tax', 'money--overpay': 'money--split', 'money--duplicate': 'money--split', 'money--cash': 'money--split', 'purchase-detail--doc': 'purchase-detail', 'order-detail--invoice': 'order-detail', 'order-detail--invoice-error': 'order-detail', 'order-detail--return': 'order-detail', 'quick-sale--qr': 'quick-sale', 'quick-sale--done': 'quick-sale', 'purchase-detail--receive': 'purchase-detail', 'purchase-detail--received': 'purchase-detail', 'purchase-detail--pay': 'purchase-detail', 'purchase-new': 'purchase-detail', 'purchase-return': 'purchase-detail', 'onboard-household--unregistered': 'onboard-consent', 'onboard-gov': 'onboard-consent', 'onboard-tax': 'onboard-consent', 'onboard-bankacc': 'onboard-consent', 'onboard-invoice--register': 'onboard-consent', 'onboard-opening': 'onboard-consent', 'onboard-feature': 'onboard-features', 'connections--feature': 'connections--category', 'connections--casso': 'connections--key', 'connections--key--error': 'connections--key', 'connections--guide': 'connections--key', 'connections--guide-casso': 'connections--key', 'connections--manage': 'connections--key', 'connections--rotate': 'connections--key', 'connections--remove': 'connections--key', 'platform-provider': 'platform-providers', 'platform-provider--remove': 'platform-providers', 'platform-provider--new': 'platform-providers', 'connections--info': 'connections', 'connections--request': 'connections', 'connections--delivery': 'connections', 'connections--many': 'connections', 'connections--add': 'connections', 'connections--category': 'connections', 'connections--use': 'connections', 'connections--account': 'connections', 'connections--disconnect': 'connections', 'connections--detail': 'connections', 'connections--provider': 'connections', 'connections--consent': 'connections', 'connections--testing': 'connections', 'connections--unknown': 'connections', 'connections--log': 'connections', 'delivery--pick--queue': 'delivery--pick--offline', 'delivery--pick--back': 'delivery--pick--offline', 'demo--reset': 'demo', 'program--help': 'program', 'program-report': 'program', 'product-detail': 'products', 'pricelist--edit': 'pricelist', 'tax--return': 'tax', 'tax-file--signed': 'tax-file', 'period--item': 'period', 'period--ready': 'period', 'production-detail--finish': 'production-detail', 'stock-lot--lock': 'stock-lot', 'purchases--expense': 'purchases', 'receivables--payables': 'receivables', 'receivable-detail--assign': 'receivable-detail', 'approvals--running': 'approvals', 'approvals--error': 'approvals', 'approvals--detail': 'approvals',
          'sales-inbox--unclear': 'sales-inbox', 'sales-inbox--add': 'sales-inbox', 'order-detail--invoice': 'order-detail'}

for name, text in list(DOCS.items()) + [(k, POINTER(v)) for k, v in STATES.items()]:
    p = H / f'{name}.md'
    s = p.read_text() if p.exists() else ''
    i = s.find('<!-- handoff.mjs:start')
    gen = s[i:] if i >= 0 else ''
    p.write_text(text.rstrip() + '\n\n' + gen)
    print('ok', name)

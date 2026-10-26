# Handoff — Bán · Giao hàng hôm nay (board)

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

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/delivery.html` · Bán · Giao hàng hôm nay (bảng 4 chặng) · status v7-v4-calm
- Page pattern: **board**
- States: `delivery--courier.html`, `delivery--pick--back.html`, `delivery--pick--offline.html`, `delivery--pick--queue.html`, `delivery--pick.html`
- Component spec: `bridge/opc-shadcn/delivery.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×818
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×746
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×723
- **390**: header 0,0 390×65 · main 0,65 390×1242 · Bán hàng 0,97 390×45 · Điều hướng nhanh 0,779 390×65

### Responsive behaviour (components that appear/disappear)
- `c-nav`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-brand`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-search`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-kbd`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-health`: 1440 shown · 1280 shown · 1024 hidden · 390 hidden
- `c-avatar`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-subnav`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown
- `c-banner`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown
- `r-mob-only`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown
- `c-tabs`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown
- `c-tabbar`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown

### Components used (at 1440)
- `c-avatar` ×1
- `c-banner` ×1 · --err
- `c-brand` ×1
- `c-btn` ×8 · --quiet --act
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×33 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sign` ×6 · --err --wait --ok
- `c-sim` ×2
- `c-sub` ×1
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-tabs` ×1
- `r-board` ×1
- `r-mob-only` ×1
- `r-page-head` ×1
- `r-shell` ×1

### Outline
- h1 Giao hàng hôm nay
- h2 Chờ soạn 2không thu hộ
- h3 Sunrise Hotel
- h3 Quán Gió Núi
- h2 Đã soạn 1thu hộ 1.300.000 ₫
- h3 Chị Thảo (Quy Nhơn)
- h2 Đang giao 3thu hộ 1.150.000 ₫
- h3 Homestay Mây Ngàn
- h3 Nhà hàng Phố Núi
- h3 Anh Nam (đặt qua Facebook)
- h2 Đã giao hôm nay 3thu 4.745.000 ₫
- h3 Sunrise Hotel
- h3 Khách lẻ
- h3 Chị Hoa (Zalo OA)

### Navigation out of this screen
- `home.html`
- `approvals.html`
- `purchases.html`
- `suppliers.html`
- `purchases--expense.html`
- `orders.html`
- `sales-inbox.html`
- `delivery.html`
- `customers.html`
- `products.html`
- `stock.html`
- `stock-count.html`
- `money.html`
- `receivables.html`
- `invoices.html`
- `period.html`
- `tax.html`
- `books.html`
- `audit.html`
- `readiness.html`
- `setup-business.html`
- `setup-data.html`
- `setup-policy.html`
- `connections.html`
- `settings-features.html`
- `settings-display.html`
- `help.html`
- `home--assistant.html`
- `home--notifications.html`
- `delivery--pick.html`
- `order-detail--delivering.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

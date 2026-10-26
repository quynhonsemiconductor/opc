# Handoff — Hàng hoá · Tồn kho

- **Purpose:** can I sell, do I need to buy — per item. **First read:** the tinted raw-beef row (6 kg, below 20 kg,
  35 kg waiting for the owner's receipt). **Primary:** "Kiểm kê". Row action on the exception: "Nhận hàng".
- **Why datatable:** few items, the same comparable numbers per row; lots are children shown inside the row.
- Columns: tồn thực · đã giữ cho đơn (links the order) · **khả dụng** (truth column = thực − giữ). Counter and new
  orders sell only on khả dụng; FEFO picks the nearest-expiry lot. Stock leaves once, at hand-over.
- Quiet line: no lot expiring in 7 days (else a pending banner with "bán trước tại quầy"). Phone: thực/giữ fold
  into the item cell, khả dụng right; healthy "Xem lô" actions hidden (the lot links stay).

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/stock.html` · Hàng hoá · Tồn kho (thực · giữ · khả dụng) · status v4-calm
- Page pattern: **datatable**
- States: none drawn
- Component spec: `bridge/opc-shadcn/stock.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×436 · Tồn kho theo món 284,261 1124×208
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×475 · Tồn kho theo món 284,261 964×247
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×513 · Tồn kho theo món 276,299 724×247
- **390**: header 0,0 390×65 · main 0,65 390×864 · Kho hàng 0,97 390×45 · Tồn kho theo món 16,425 358×360 · Điều hướng nhanh 0,779 390×65

### Responsive behaviour (components that appear/disappear)
- `c-nav`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-brand`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-search`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-kbd`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-health`: 1440 shown · 1280 shown · 1024 hidden · 390 hidden
- `c-avatar`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-subnav`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown
- `c-tabbar`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown

### Components used (at 1440)
- `c-avatar` ×1
- `c-brand` ×1
- `c-btn` ×5 · --quiet --act
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×27 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sign` ×3 · --ok --you
- `c-sub` ×2
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-table` ×1 · --stack
- `r-page-head` ×1
- `r-shell` ×1
- `r-stock` ×1

### Outline
- h1 Tồn kho

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
- `books--stock.html`
- `order-detail.html`
- `purchase-detail--receive.html`
- `product-detail.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

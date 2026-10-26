# Handoff — Nhận hàng theo đơn mua

- **Purpose:** count what arrived, decide on a shortfall, match the supplier's invoice. **First read:** 35/40 kg
  (tinted). **Primary:** "Xác nhận nhận hàng" with its result preview (stock in once by lot, payable amount and due).
- Shortfall options: receive and wait for the rest (PO stays open) · receive and close the PO; note to supplier.
- Supplier invoice (photo/PDF or from the tax portal when enabled): checks supplier, unit price, quantity; a mismatch
  is an error banner with "Nhắn HTX" (ask for an adjustment invoice); the document stays "Lệch" until resolved.
- Not drawn: over-delivery, damaged goods returned to the supplier, receipt without a PO, supplier without an invoice
  (bảng kê thu mua — rule to be confirmed by the accountant).

<!-- handoff.mjs:start — generated 2026-10-08, do not edit inside this block -->
## Generated facts
- Screen: `../screens/purchase-receive.html` · Nhập hàng · Nhận MH-0118 (thiếu 5 kg, chứng từ lệch) · status v4-calm
- Page pattern: **detail**
- States: none drawn
- Component spec: `bridge/opc-shadcn/purchase-receive.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×916 · Đường dẫn 284,105 1124×44 · aside 966,251 442×444
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×916 · Đường dẫn 284,105 964×44 · aside 870,251 378×497
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1261 · Đường dẫn 276,105 724×44 · aside 276,975 724×320
- **390**: header 0,0 390×65 · main 0,65 390×1663 · Mua hàng 0,97 390×45 · Đường dẫn 16,166 358×44 · aside 16,1161 358×423 · Điều hướng nhanh 0,779 390×65

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
- `c-banner` ×1 · --err
- `c-brand` ×1
- `c-btn` ×4 · --quiet --act
- `c-card` ×1
- `c-crumbs` ×1
- `c-decide` ×1
- `c-field` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×30 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-option` ×2 · --best
- `c-options` ×1
- `c-quote` ×1
- `c-rules` ×1
- `c-search` ×1
- `c-sign` ×1 · --you
- `c-sub` ×1
- `c-subnav` ×1
- `c-tabbar` ×1
- `r-pick` ×1
- `r-shell` ×1

### Outline
- h1 Nhận hàng MH-0118 · HTX Cao Nguyên Thiếu 5 kg
- h2 Hàng thực nhận
- h2 Chứng từ đầu vào

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
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

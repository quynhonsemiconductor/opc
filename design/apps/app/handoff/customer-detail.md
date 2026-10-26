# Handoff — Khách hàng · chi tiết (Sunrise Hotel)

- Head: name + debt sign, the owed figure, limit + terms. Primary "Tạo đơn"; secondary "Nhắc nợ" (→ receivable-detail).
- Credit meter (used / limit) with the consequence line (overdue → credit orders need owner approval). Profile & terms
  (MST, orderer, delivery address, price list, invoice email, recurring order). Recent orders and open invoices.
- Right: conversation trail (Zalo OA reminders by the assistant, orders, owner approvals) — read-only.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/customer-detail.html` · Khách hàng · Sunrise Hotel
- Page pattern: **v4.4 rail destinations**
- States: none drawn
- Component spec: `bridge/opc-shadcn/customer-detail.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×866 · Đường dẫn 284,105 1124×44 · aside 966,263 442×418
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×890 · Đường dẫn 284,105 964×44 · aside 870,263 378×439
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1342 · Đường dẫn 276,105 724×44 · aside 276,957 724×418
- **390**: header 0,0 390×65 · main 0,65 390×1775 · Bán hàng 0,97 390×45 · Đường dẫn 16,166 358×44 · aside 16,1320 358×376 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×3 · --quiet --act
- `c-card` ×2
- `c-crumbs` ×1
- `c-figure` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×30 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-kv` ×1
- `c-link` ×1
- `c-nav` ×1
- `c-orders` ×1
- `c-search` ×1
- `c-sign` ×5 · --err --wait --ok
- `c-sub` ×2
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-timeline` ×1 · --quiet
- `r-shell` ×1

### Outline
- h1 Sunrise Hotel Nợ quá hạn 12 ngày
- h2 Thông tin & điều khoản
- h2 Đơn gần đây
- h2 Trao đổi gần đây

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
- `receivable-detail.html`
- `sales-inbox--add.html`
- `pricelist.html`
- `orders--search.html`
- `order-detail.html`
- `invoice-detail.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

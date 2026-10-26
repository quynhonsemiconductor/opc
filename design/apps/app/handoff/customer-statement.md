# Handoff — Bảng kê công nợ (v7.4.0)

- Per customer and period: invoices with due date and remaining amount, total, customer credit, orders not yet invoiced.
- Agent drafts the Zalo OA message with PDF + QR of the household account (memo = customer code); the owner sends.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/customer-statement.html` · Công nợ · bảng kê Sunrise · status v7-money
- Page pattern: **detail**
- States: none drawn
- Component spec: `bridge/opc-shadcn/customer-statement.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×636 · Đường dẫn 284,105 1124×44 · Bảng kê 284,308 662×247 · aside 966,243 442×249
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×636 · Đường dẫn 284,105 964×44 · Bảng kê 284,308 566×247 · aside 870,243 378×249
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×857 · Đường dẫn 276,105 724×44 · Bảng kê 276,308 724×247 · aside 276,689 724×201
- **390**: header 0,0 390×65 · main 0,65 390×1107 · Đường dẫn 16,97 358×44 · Bảng kê 16,371 358×245 · aside 16,767 358×261 · Điều hướng nhanh 0,779 390×65

### Responsive behaviour (components that appear/disappear)
- `c-nav`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-brand`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-search`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-kbd`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-health`: 1440 shown · 1280 shown · 1024 hidden · 390 hidden
- `c-avatar`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `r-jump7`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown
- `c-tabbar`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown

### Components used (at 1440)
- `c-avatar` ×1
- `c-brand` ×1
- `c-btn` ×3 · --quiet --act
- `c-card` ×1
- `c-crumbs` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×25 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-kv` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sub` ×2
- `c-tabbar` ×1
- `c-table` ×1
- `r-jump7` ×1
- `r-lines` ×1 · --alloc
- `r-page-head` ×1
- `r-shell` ×1

### Outline
- h1 Bảng kê công nợ · Sunrise Hotel
- h2 Hoá đơn trong kỳ
- h2 Khách Sunrise Hotel

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

# Handoff — Công nợ của một khách (bảng kê, nhắc nợ, gán tiền)

- **Purpose:** chase overdue politely and apply payments correctly. **First read:** owed now 8.400.000 ₫ (2 overdue
  invoices). **Primary:** "Gửi bảng kê & nhắc nợ" under the assistant's draft (the person presses send).
- Data: open invoices (amount, due, days overdue) · "Chưa tính" upcoming invoice · paid history (folded) · reminder
  timeline (assistant via Zalo OA, owner's promises from approval reasons).
- `--assign`: a transfer without an order code → choose invoices (suggestion = exact sum, oldest first); "đủ" is
  arithmetic; the money stays "chờ xác minh" until the bank statement matches; alternatives: prepayment for a coming
  invoice, customer credit, not this customer. Never auto-assigned.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/receivable-detail.html` · Công nợ · Sunrise Hotel (bảng kê, nhắc nợ) · status v4-calm
- Page pattern: **detail**
- States: `receivable-detail--assign.html`
- Component spec: `bridge/opc-shadcn/receivable-detail.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×954 · Đường dẫn 284,105 1124×44 · Hoá đơn còn nợ 284,328 662×168 · aside 966,263 442×725
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×1023 · Đường dẫn 284,105 964×44 · Hoá đơn còn nợ 284,328 566×168 · aside 870,263 378×794
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1157 · Đường dẫn 276,105 724×44 · Hoá đơn còn nợ 276,328 724×168 · aside 276,615 724×576
- **390**: header 0,0 390×65 · main 0,65 390×1637 · Tiền 0,97 390×45 · Đường dẫn 16,166 358×44 · Hoá đơn còn nợ 16,497 358×204 · aside 16,851 358×707 · Điều hướng nhanh 0,779 390×65

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
- `c-card` ×1
- `c-crumbs` ×1
- `c-figure` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×30 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-quote` ×1
- `c-search` ×1
- `c-sign` ×6 · --err --wait --ok
- `c-sub` ×2
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-table` ×2 · --stack
- `c-timeline` ×1
- `r-paid` ×1
- `r-shell` ×1
- `r-upcoming` ×1

### Outline
- h1 Sunrise Hotel · công nợ Quá hạn 12 ngày
- h2 Hoá đơn còn nợ
- h2 Nhắc nợ

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
- `receivable-detail--assign.html`
- `customer-statement.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

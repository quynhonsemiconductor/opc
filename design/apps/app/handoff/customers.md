# Handoff — Khách hàng (Bán › Khách hàng)

- **Who:** owner / operator. **Purpose:** see who owes what and open the one that needs action. **Primary:** "Thêm khách"
  (MST lookup fills name + address). Rows: name (row link) + type/channel, price list, terms + credit limit, owed, sign.
- Only customers with a profile can buy on credit, inside their limit and with nothing overdue (policy in Vai trò & duyệt).
- Tablet ≤1180: Bảng giá / Điều khoản columns drop (terms resurface as a sub-line), action column drops (row is the link).

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/customers.html` · Bán · Khách hàng
- Page pattern: **v4.4 rail destinations**
- States: none drawn
- Component spec: `bridge/opc-shadcn/customers.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×741 · Khách hàng 284,265 1124×509
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×885 · Khách hàng 284,265 964×653
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×762 · Khách hàng 276,285 724×510
- **390**: header 0,0 390×65 · main 0,65 390×1285 · Bán hàng 0,97 390×45 · Khách hàng 16,435 358×771 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×8 · --quiet --act
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×31 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sign` ×6 · --err --wait --you --pass
- `c-sub` ×1
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-table` ×1 · --stack
- `r-page-head` ×1
- `r-shell` ×1
- `r-trust` ×1 · --gate

### Outline
- h1 Khách hàng

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
- `customer-detail.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

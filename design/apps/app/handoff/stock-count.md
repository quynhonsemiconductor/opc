# Handoff — Kiểm kê

- **Purpose:** count, see differences, send them for approval — stock is never edited directly. **First read:**
  "2 dòng lệch". **Primary:** "Gửi chị An duyệt", locked with its reason until every difference has a reason.
- Selling continues during the count: OPC snapshots book quantities at start and nets out sales made meanwhile.
- Per line: counted input (decimal for kg) · difference (loud) · reason (Hỏng · Hao hụt · Đếm sai · Khác) + note;
  the assistant may suggest a reason from history (label "Trợ lý gợi ý"). Matched lines recede.
- Result line: approval writes n adjustments to the ledger, value at cost. Desktop pins the gate; phone keeps it in
  flow (tab bar owns the bottom). Approval appears in Cần xử lý for the owner.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/stock-count.html` · Tồn kho · Kiểm kê (lệch → gửi duyệt) · status v4-calm
- Page pattern: **form**
- States: none drawn
- Component spec: `bridge/opc-shadcn/stock-count.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×693 · Đường dẫn 284,105 1124×44
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×693 · Đường dẫn 284,105 964×44
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×743 · Đường dẫn 276,105 724×44
- **390**: header 0,0 390×65 · main 0,65 390×1170 · Kho hàng 0,97 390×45 · Đường dẫn 16,166 358×44 · Điều hướng nhanh 0,779 390×65

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
- `c-card` ×1
- `c-crumbs` ×1
- `c-field` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×27 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-seg` ×1
- `c-sign` ×1 · --wait
- `c-sub` ×1
- `c-subnav` ×1
- `c-tabbar` ×1
- `r-count` ×1
- `r-shell` ×1

### Outline
- h1 Kiểm kho · Kho chính Đang đếm
- h2 1 món lệch so với sổ

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

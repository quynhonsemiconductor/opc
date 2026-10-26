# Handoff — Hàng hoá · Danh sách & giá

- **Purpose:** what we sell and at which approved prices. **First read:** items with every price list as a column
  (default marked "mặc định"). **Primary:** "Thêm món" (secondary: photograph a price list — the assistant reads it,
  the owner reviews each line).
- Rule above the grid: counter + customers without a list → retail; customers assigned to a list → that list;
  confirmed orders keep the price at confirmation. Item facts: unit/barcode, source (bought / own production with
  recipe), lot + shelf life, tax group, available stock (muted). Materials live in Tồn kho.
- `product-detail`: prices per list (default leads), facts incl. recipe, append-only price history with approver.
  **Primary:** "Đổi giá".

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/products.html` · Hàng hoá · Danh sách & giá · status v4-calm
- Page pattern: **datatable**
- States: none drawn
- Component spec: `bridge/opc-shadcn/products.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×470 · Món bán và giá 284,330 1124×173
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×498 · Món bán và giá 284,350 964×181
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×554 · Món bán và giá 276,406 724×181
- **390**: header 0,0 390×65 · main 0,65 390×877 · Kho hàng 0,97 390×45 · Món bán và giá 16,516 358×282 · Điều hướng nhanh 0,779 390×65

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
- `c-ic` ×25 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sub` ×1
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-table` ×1 · --stack
- `c-tabs` ×1
- `r-page-head` ×1
- `r-prices` ×1
- `r-shell` ×1
- `r-trust` ×1 · --gate

### Outline
- h1 Danh sách & giá

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
- `onboard-products.html`
- `product-detail.html`
- `pricelist.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

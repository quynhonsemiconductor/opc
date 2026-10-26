# Handoff — Mua hàng · Đơn mua (v7.2.0)

- **Purpose:** what was bought, what is still coming, what is owed, what needs the owner. **First read:** the tinted rows
  (MH-0118 về 45/50, MH-0122 Agent proposal). **Primary:** "Tạo đơn mua"; quiet "Hàng đã về, chưa có đơn" (PO optional).
- Columns are independent tracks: Nhận hàng · Chứng từ · Tiền · Giá trị. Filters: Cần chị · Đang về · Còn nợ · Lệch chứng từ.
- Tabs Đơn mua · Chi phí · Trả hàng. `purchases--expense`: expense outside stock from a photo; never part of cost of goods.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/purchases.html` · Mua hàng · Đơn mua (nhận hàng, chứng từ, tiền tách riêng) · status v7-buy
- Page pattern: **datatable**
- States: `purchases--expense.html`
- Component spec: `bridge/opc-shadcn/purchases.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×739 · Đơn mua 284,346 1124×376
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×887 · Đơn mua 284,346 964×524
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×943 · Đơn mua 276,402 724×524
- **390**: header 0,0 390×65 · main 0,65 390×1374 · Đơn mua 16,454 358×777 · Điều hướng nhanh 0,779 390×65

### Responsive behaviour (components that appear/disappear)
- `c-nav`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-brand`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-search`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-kbd`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-health`: 1440 shown · 1280 shown · 1024 hidden · 390 hidden
- `c-avatar`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-tabbar`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown

### Components used (at 1440)
- `c-avatar` ×1
- `c-brand` ×1
- `c-btn` ×8 · --quiet --act
- `c-filter` ×5
- `c-filters` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×26 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sign` ×2 · --you
- `c-sub` ×2
- `c-tabbar` ×1
- `c-table` ×1 · --stack
- `c-tabs` ×1
- `r-buy` ×1
- `r-page-head` ×1
- `r-shell` ×1

### Outline
- h1 Mua hàng

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
- `purchase-new.html`
- `purchase-return.html`
- `purchase-detail--receive.html`
- `purchase-detail.html`
- `purchase-detail--pay.html`
- `purchase-detail--doc.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

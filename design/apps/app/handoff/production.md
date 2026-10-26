# Handoff — Hàng hoá · Chế biến

- **Purpose:** what is being made, what is blocked. **First read:** tinted LCB-0413 "Thiếu 28 kg thịt bò".
  **Primary:** "Lập lệnh chế biến". Live rows (blocked, running) have bordered actions; done rows quiet.
- **Why datatable:** a short list of comparable orders. Columns: Lệnh · Ngày · Gói ra / dự kiến ("– / 40" until
  finished; dash grey) · Lô (lot code = order number: LCB-0412 → BMN-0412) · one status token.
- States (FLOWS Phụ lục A): Nháp · Đang làm · Xong · Đã huỷ. Simple production only — no BOM/MRP; OPC learns the
  usual inputs and yield from the last runs.

<!-- handoff.mjs:start — generated 2026-10-08, do not edit inside this block -->
## Generated facts
- Screen: `../screens/production.html` · Hàng hoá · Chế biến (lệnh) · status v4-calm
- Page pattern: **datatable**
- States: none drawn
- Component spec: `bridge/opc-shadcn/production.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×461 · Lệnh chế biến 284,195 1124×299
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×461 · Lệnh chế biến 284,195 964×299
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×549 · Lệnh chế biến 276,195 724×387
- **390**: header 0,0 390×65 · main 0,65 390×817 · Hàng hoá 0,97 390×45 · Lệnh chế biến 16,307 358×431 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×6 · --quiet --act
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×29 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sign` ×4 · --you --wait --ok
- `c-sub` ×1
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-table` ×1 · --stack
- `r-dash` ×2
- `r-page-head` ×1
- `r-shell` ×1

### Outline
- h1 Chế biến

### Navigation out of this screen
- `home.html`
- `counter.html`
- `approvals.html`
- `orders.html`
- `sales-inbox.html`
- `delivery.html`
- `customers.html`
- `products.html`
- `stock.html`
- `production.html`
- `purchases.html`
- `suppliers.html`
- `money.html`
- `receivables.html`
- `shift-close.html`
- `period.html`
- `books.html`
- `invoices.html`
- `audit.html`
- `connections.html`
- `readiness.html`
- `setup-business.html`
- `setup-data.html`
- `setup-policy.html`
- `settings-features.html`
- `settings-display.html`
- `help.html`
- `home--assistant.html`
- `home--notifications.html`
- `production-new.html`
- `production-detail.html`
- `stock-lot.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

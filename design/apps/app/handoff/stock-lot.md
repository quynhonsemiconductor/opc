# Handoff — Lô hàng · truy xuất hai chiều

- **Purpose:** where this lot came from and where it went; its stock ledger. **First read:** 26 gói (20 giữ · 6 bán
  được) · hạn 15/11. **No primary** (reading page); "Khoá lô" is a quiet danger button → `stock-lot--lock`.
- Balance line from OPC kiểm tra first: made = reached customers + in stock; if it does not balance, show the gap as
  an error sign and link the stock take.
- Từ đâu: supplier → PO → raw lots (qty used) → production order (yield). Tới đâu: orders/customers (counter sales
  grouped "khách lẻ tại quầy, n gói", known customers counted) → still in stock.
- Ledger: append-only, newest first; holds are listed but do not change on-hand. Adjustments only via stock take.
- Lock dialog: worst consequence first (who already received it; assistant drafts notices, owner sends), then
  in-stock effects (stop selling; held units move to another lot if available, else the order shows "thiếu hàng"),
  reason required (empty), reversible with a reason. Anyone with stock rights can lock; owner is notified.

<!-- handoff.mjs:start — generated 2026-10-08, do not edit inside this block -->
## Generated facts
- Screen: `../screens/stock-lot.html` · Tồn kho · Lô BMN-0405 (truy xuất hai chiều + sổ kho) · status v4-calm
- Page pattern: **detail**
- States: `stock-lot--lock.html`
- Component spec: `bridge/opc-shadcn/stock-lot.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×885 · Đường dẫn 284,105 1124×44 · aside 966,263 442×616
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×885 · Đường dẫn 284,105 964×44 · aside 870,263 378×616
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1572 · Đường dẫn 276,105 724×44 · aside 276,1012 724×592
- **390**: header 0,0 390×65 · main 0,65 390×1879 · Hàng hoá 0,97 390×45 · Đường dẫn 16,166 358×44 · aside 16,1253 358×547 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×3 · --quiet --danger
- `c-card` ×1
- `c-crumbs` ×1
- `c-figure` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×28 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sign` ×2 · --ok
- `c-sub` ×2
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-tag` ×1
- `c-timeline` ×1 · --quiet
- `r-shell` ×1
- `r-trace` ×1

### Outline
- h1 Lô BMN-0405 · Bò một nắng 500g Đang bán
- h2 Truy xuất
- h3 Từ đâu
- h3 Tới đâu
- h2 Sổ kho của lô

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
- `stock-lot--lock.html`
- `order-detail.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

# Handoff — Bán nhanh (v7.3.0, replaces Quầy + Đóng ca)

- Walk-in sale: search/quick-add goods, steppers, retail price list, pay by QR (household account) / cash / debt, optional
  "Khách cần hoá đơn". Result line before the primary: order number, stock out once, money recorded when matched.
- `--qr`: VietQR of the household's own account with the order code as content; bank connected → OPC matches automatically;
  not connected → the owner checks her bank app and taps "Tôi đã thấy tiền về". OPC never moves money.
- `--done`: one order, all four tracks closed at once; Bán tiếp · In phiếu · Khách cần hoá đơn (issue from the order same day).
- Cash is counted in Thu chi và đối chiếu (no shift close). onboard-firstsale reuses `--qr` as a test sale (no revenue, no stock).

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/quick-sale.html` · Bán nhanh · giỏ hàng khách lẻ · status v7-sell
- Page pattern: **detail**
- States: `quick-sale--done.html`, `quick-sale--offline.html`, `quick-sale--qr.html`, `quick-sale--staff.html`
- Component spec: `bridge/opc-shadcn/quick-sale.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×933 · aside 966,195 442×195
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×933 · aside 870,195 378×219
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1104 · aside 276,966 724×171
- **390**: header 0,0 390×65 · main 0,65 390×1370 · aside 16,1082 358×210 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×5 · --quiet --act
- `c-card` ×3
- `c-check` ×1
- `c-field` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×28 · --s
- `c-icon-btn` ×6
- `c-kbd` ×1
- `c-kv` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-seg` ×1
- `c-sub` ×2
- `c-tabbar` ×1
- `r-chkrow` ×1
- `r-page-head` ×1
- `r-pick` ×1
- `r-recv` ×1
- `r-shell` ×1
- `r-step` ×2

### Outline
- h1 Bán nhanh
- h2 Khách lẻ
- h2 Giỏ hàng
- h2 Thanh toán
- h2 Hôm nay

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
- `quick-sale--qr.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

# Handoff — Sẵn sàng (readiness) · v6.0.0

- **Purpose:** everything a hộ kinh doanh needs to run end to end, by chain: Hộ và người · Bán và thu · Mua và trả · Chế biến và kho · Thuế và sổ (33 việc, `readiness_model.py`). **First read:** state + "còn n việc".
- Each chain: open **bắt buộc** items with the flow each one locks (never the whole app), "Nên có" always visible, "Làm sau" and "Đã xong" folded with their names. Failing connection = error edge, never blocks other items.
- Rules, not fixed lists: tiers come from the model chosen at step 3 and from doanh thu lũy kế (quý khi vượt 500 triệu, hoá đơn máy tính tiền từ 1 tỷ — to be confirmed by an accountant). Assisted mode shows the same list.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/readiness.html` · Cài đặt · Sẵn sàng (readiness theo mô hình) · status v4-calm
- Page pattern: **checklist**
- States: `readiness--new.html`
- Component spec: `bridge/opc-shadcn/readiness.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×1453 · aside 966,195 442×301
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×1477 · aside 870,195 378×301
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1750 · aside 276,1506 724×277
- **390**: header 0,0 390×65 · main 0,65 390×2174 · Thiết lập 0,97 390×45 · aside 16,1845 358×250 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×14 · --quiet --act
- `c-card` ×4
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×25 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-meter` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sign` ×1 · --wait
- `c-sub` ×5
- `c-subnav` ×1
- `c-tabbar` ×1
- `r-gate` ×9
- `r-page-head` ×1
- `r-shell` ×1

### Outline
- h1 Sẵn sàng Sẵn sàng có điều kiện
- h2 Hộ và dữ liệu nền
- h3 Tuỳ chọn · bỏ qua được
- h2 Mua hàng và kho
- h3 Tuỳ chọn · bỏ qua được
- h2 Bán hàng, hoá đơn và tiền
- h3 Tuỳ chọn · bỏ qua được
- h2 Sổ sách và kê khai
- h2 Danh sách này từ đâu
- h2 Nhân viên OPC hỗ trợ

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
- `connections--category.html`
- `purchase-detail--pay.html`
- `onboard-invoice.html`
- `onboard-assisted.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

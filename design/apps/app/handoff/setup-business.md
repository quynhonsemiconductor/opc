# Handoff — Hộ & mô hình kinh doanh

- Profile filled from the tax-code lookup (connector #10; manual: type it in); OPC never edits registered data —
  fix at the tax office, then "Tra lại". Two questions (multi-select): how you sell (quầy · khách sỉ/khách sạn ·
  online/sàn) and where goods come from (mua về bán · tự chế biến); each option shows its consequence on the plan and
  tax group. **Primary:** "Lưu" = recompute readiness; no data is deleted when an option is turned off.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/setup-business.html` · Cài đặt · Hộ & mô hình kinh doanh · status v4-calm
- Page pattern: **form**
- States: none drawn
- Component spec: `bridge/opc-shadcn/setup-business.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×799 · aside 966,195 442×455
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×799 · aside 870,195 378×527
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1230 · aside 276,852 724×411
- **390**: header 0,0 390×65 · main 0,65 390×1721 · Thiết lập 0,97 390×45 · aside 16,1075 358×567 · Điều hướng nhanh 0,779 390×65

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
- `c-card` ×2
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×29 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-kv` ×1
- `c-nav` ×1
- `c-option` ×5 · --on
- `c-options` ×2
- `c-search` ×1
- `c-sign` ×1 · --ok
- `c-sub` ×2
- `c-subnav` ×1
- `c-tabbar` ×1
- `r-model` ×2
- `r-page-head` ×1
- `r-shell` ×1
- `r-trust` ×1 · --gate

### Outline
- h1 Hộ & mô hình kinh doanh Đủ dữ liệu
- h2 Chị bán thế nào?
- h2 Hàng từ đâu?
- h2 Hồ sơ hộ

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

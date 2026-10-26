# Handoff — Lệnh chế biến đang làm / ghi kết quả

- **Running (`production-detail`):** head figure = expected output "40 gói" with the usual band (39–40 from 34 kg)
  — the finish step checks against it; journey owns "now", timeline holds history; materials issued table.
  **Primary:** "Ghi kết quả".
- **Finish (`--finish`, 16:05):** actual vs expected sheet (reuses `r-count`): yield, raw used (unused part goes back
  to stock), seasoning. Yield outside the usual band → "OPC kiểm tra" asks for a reason (Sấy quá khô · Bỏ phần hỏng ·
  Cân sai · Khác), empty by default; primary "Nhập kho 38 gói" locked with its reason. Result: new lot BMN-0412,
  expiry 05/12, sellable at once; optional print of lot labels (public trace page only if the owner turns it on).

<!-- handoff.mjs:start — generated 2026-10-08, do not edit inside this block -->
## Generated facts
- Screen: `../screens/production-detail.html` · Chế biến · LCB-0412 đang làm · status v4-calm
- Page pattern: **detail**
- States: `production-detail--finish.html`
- Component spec: `bridge/opc-shadcn/production-detail.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×730 · Đường dẫn 284,105 1124×44 · Nguyên liệu đã xuất 284,420 662×168 · aside 966,354 442×311
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×730 · Đường dẫn 284,105 964×44 · Nguyên liệu đã xuất 284,420 566×168 · aside 870,354 378×332
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1036 · Đường dẫn 276,105 724×44 · Nguyên liệu đã xuất 276,420 724×168 · aside 276,759 724×311
- **390**: header 0,0 390×65 · main 0,65 390×1336 · Hàng hoá 0,97 390×45 · Đường dẫn 16,166 358×44 · Nguyên liệu đã xuất 16,586 358×136 · aside 16,988 358×269 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×2 · --quiet --act
- `c-card` ×2
- `c-crumbs` ×1
- `c-figure` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×26 · --s
- `c-icon-btn` ×2
- `c-journey` ×1
- `c-kbd` ×1
- `c-kv` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sign` ×1 · --wait
- `c-sub` ×3
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-table` ×1 · --stack
- `c-timeline` ×1
- `r-shell` ×1

### Outline
- h1 LCB-0412 · Bò một nắng 500g Đang làm
- h2 Nguyên liệu đã xuất
- h2 Thành phẩm dự kiến
- h2 Diễn biến

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
- `production-detail--finish.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

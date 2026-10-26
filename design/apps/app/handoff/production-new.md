# Handoff — Lệnh chế biến (nháp) LCB-0413

- **Purpose:** plan a run; see at once whether it can start. **First read:** materials check — "Thiếu 28 kg".
  **Primary:** "Bắt đầu" (locked with its reason while short); "Lưu lệnh nháp" secondary.
- OPC computes materials from the last 3 runs (label "OPC kiểm tra"); never issues more than available (no negative
  stock). The cure sits under the shortage: incoming receipt waiting for the owner (link to purchase-detail--receive), else
  "Tạo đơn mua phần thiếu".
- Start = issue materials, deducted once; finished goods enter stock only when the result is recorded.
- Rail (quiet): the lot that will come out (code, expiry = production date + shelf life).

<!-- handoff.mjs:start — generated 2026-10-08, do not edit inside this block -->
## Generated facts
- Screen: `../screens/production-new.html` · Chế biến · Lệnh mới (OPC tính nguyên liệu, chặn khi thiếu) · status v4-calm
- Page pattern: **form**
- States: none drawn
- Component spec: `bridge/opc-shadcn/production-new.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×895 · Đường dẫn 284,105 1124×44 · Nguyên liệu cần 284,587 662×226 · aside 966,251 442×223
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×895 · Đường dẫn 284,105 964×44 · Nguyên liệu cần 284,587 566×226 · aside 870,251 378×271
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1093 · Đường dẫn 276,105 724×44 · Nguyên liệu cần 276,587 724×226 · aside 276,927 724×199
- **390**: header 0,0 390×65 · main 0,65 390×1665 · Hàng hoá 0,97 390×45 · Đường dẫn 16,166 358×44 · Nguyên liệu cần 16,887 358×276 · aside 16,1350 358×237 · Điều hướng nhanh 0,779 390×65

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
- `c-card` ×2
- `c-crumbs` ×1
- `c-field` ×4
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×33 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-kv` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sign` ×3 · --pend --err --ok
- `c-sub` ×1
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-table` ×1 · --stack
- `c-tag` ×1
- `r-form2` ×1
- `r-mat` ×1
- `r-shell` ×1

### Outline
- h1 Lệnh chế biến LCB-0413 Nháp
- h2 Làm gì
- h2 Nguyên liệu
- h2 Sẽ ra

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
- `purchase-receive.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

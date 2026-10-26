# Handoff — Soạn hàng → bàn giao

- **Purpose:** pick the held lines (shelf + nearest expiry hint, no lots) and hand over. **First read:** "1/2 món xong". **Primary:** "Bàn giao
  cho anh Hùng" — `aria-disabled` with the reason on the button until every line is complete; secondary "Giao thiếu · N" (add a confirm step)
  edits the order to what is delivered and creates a new order for the rest; the invoice follows delivered quantities.
- Hand-over sends the deliverer link; **stock leaves once** when the deliverer reports delivered (Đã giao).

<!-- handoff.mjs:start — generated 2026-10-06, do not edit inside this block -->
## Generated facts
- Screen: `../screens/delivery--pick.html` · Giao hàng · Soạn DH-2052 → bàn giao · status v4-calm
- Page pattern: **detail**
- States: `delivery--pick--back.html`, `delivery--pick--offline.html`, `delivery--pick--queue.html`
- Component spec: `bridge/opc-shadcn/delivery--pick.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×736 · Đường dẫn 284,105 1124×44 · aside 966,251 442×217
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×736 · Đường dẫn 284,105 964×44 · aside 870,251 378×217
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×882 · Đường dẫn 276,105 724×44 · aside 276,747 724×169
- **390**: header 0,0 390×65 · main 0,65 390×1308 · Bán 0,97 390×45 · Đường dẫn 16,166 358×44 · aside 16,1066 358×180 · Điều hướng nhanh 0,779 390×65

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
- `c-crumbs` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×26 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-kv` ×2
- `c-nav` ×1
- `c-search` ×1
- `c-sub` ×3
- `c-subnav` ×1
- `c-tabbar` ×1
- `r-pick` ×1
- `r-shell` ×1

### Outline
- h1 Soạn DH-2052 · Sunrise Hotel
- h2 Lấy hàng · 1/2 món xong
- h2 Bàn giao
- h2 Đã giữ cho đơn này

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
- `readiness.html`
- `setup-business.html`
- `setup-data.html`
- `connections.html`
- `setup-policy.html`
- `settings-features.html`
- `settings-display.html`
- `help.html`
- `home--assistant.html`
- `home--notifications.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

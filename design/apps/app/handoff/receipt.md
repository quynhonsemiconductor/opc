# Handoff — receipt (v3.1 Pro layer)

<!-- v41:start -->
## v4.1 (current)
> Layout and parts follow DESIGN.md §3 (v4.1). Primary = sea `--act`, one per view; money states use the truth palette. If any older note below disagrees with this block, this block wins.

- **Purpose:** Print or send the receipt for a paid order.
- **First read:** 1.020.000 ₫ + verified pill "Đã xác minh · QR".
- **Primary action:** "In phiếu"; PDF / Zalo outline.
- **Layout:** Receipt facsimile | Zalo message preview (links in brand ink).
<!-- v41:end -->


Content: BRIEF §15. Rules: DESIGN.md §5 (Help and support · Display preferences · Power tools · Feedback · Trust). Component spec: `bridge/opc-shadcn/receipt.md`.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/receipt.html` · Phiếu in & tin Zalo cho khách · status v4-calm
- Page pattern: **detail**
- States: none drawn
- Component spec: `bridge/opc-shadcn/receipt.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×746 · Đường dẫn 284,105 1124×44 · header 471,283 288×101
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×784 · Đường dẫn 284,105 964×44 · header 423,321 288×101
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1296 · Đường dẫn 276,105 724×44 · header 494,381 288×101
- **390**: header 0,0 390×65 · main 0,65 390×1480 · Đường dẫn 16,97 358×44 · header 51,427 288×101 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×4 · --quiet --act
- `c-card` ×1
- `c-crumbs` ×1
- `c-figure` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×25 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-kv` ×1
- `c-msgcard` ×1
- `c-nav` ×1
- `c-receipt` ×1
- `c-search` ×1
- `c-sign` ×1 · --ok
- `c-sub` ×2
- `c-tabbar` ×1
- `r-shell` ×1

### Outline
- h1 Phiếu DH-2053 Đã xác minh · QR
- h2 Tin Zalo khách sẽ nhận

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
- `invoice-detail.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

<!-- v43:start -->
## v4.3 · data & decisions

Counter receipt with the cash-register invoice number and lookup code; Zalo message only to customers following the OA.
<!-- v43:end -->

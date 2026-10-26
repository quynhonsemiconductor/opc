# Handoff — Đơn bán (v7.3.0)

- **One record**: Hàng bán · Giao hàng · Hoá đơn · Tiền + Diễn biến. Header `r-tracks` Đơn · Giao · Hoá đơn · Tiền; each track
  moves on its own (an invoice error never touches stock or money). Never a stepper.
- **Confirm** only within available stock (otherwise Cần xử lý: sửa số lượng / chờ hàng về); confirm holds the goods.
- **Đã giao** = delivered in full → stock out once (preview before → after) + one e-invoice for the order (buyer company + MST
  captured on the order; walk-in buyer: name / MST / personal ID optional). Short delivery = order edited to what was
  delivered + a new order for the rest.
- `--invoice-error`: tax authority rejected (no code yet) → fix the field, resend the same invoice; no adjustment invoice.
- `--return`: household is the seller → OPC drafts the adjustment invoice, the owner signs/sends via the e-invoice provider;
  restock only when "Còn tốt"; receivable reduced or refund. Rule awaits the accountant.
- Credit and overdue debt are shown as information, never a gate. The order closes when money is linked.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/order-detail.html` · Đơn bán DH-2052 · đã xác nhận, giữ hàng, chờ giao · status v7-sell
- Page pattern: **detail**
- States: `order-detail--delivering.html`, `order-detail--invoice-error.html`, `order-detail--invoice.html`, `order-detail--return.html`, `order-detail--split.html`
- Component spec: `bridge/opc-shadcn/order-detail.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×1108 · Đường dẫn 284,105 1124×44 · {label} 284,447 662×195 · aside 966,376 442×335
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×1156 · Đường dẫn 284,105 964×44 · {label} 284,447 566×195 · aside 870,376 378×335
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1536 · Đường dẫn 276,105 724×44 · {label} 276,520 724×195 · aside 276,1234 724×335
- **390**: header 0,0 390×65 · main 0,65 390×2048 · Đường dẫn 16,97 358×44 · {label} 16,638 358×178 · aside 16,1676 358×293 · Điều hướng nhanh 0,779 390×65

### Responsive behaviour (components that appear/disappear)
- `c-nav`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-brand`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-search`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-kbd`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-health`: 1440 shown · 1280 shown · 1024 hidden · 390 hidden
- `c-avatar`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `r-jump7`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown
- `c-tabbar`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown

### Components used (at 1440)
- `c-avatar` ×1
- `c-brand` ×1
- `c-btn` ×4 · --quiet --act
- `c-card` ×4
- `c-crumbs` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×25 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-kv` ×3
- `c-nav` ×1
- `c-search` ×1
- `c-sub` ×3
- `c-tabbar` ×1
- `c-table` ×1
- `c-timeline` ×1
- `r-jump7` ×1
- `r-lines` ×1
- `r-shell` ×1
- `r-tracks` ×1

### Outline
- h1 DH-2052 · Sunrise Hotel
- h2 Hàng bán
- h2 Giao hàng
- h2 Hoá đơn
- h2 Tiền
- h2 Diễn biến

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
- `delivery--pick.html`
- `order-detail--delivering.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

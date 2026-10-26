# Handoff — Hồ sơ đơn mua (v7.2.0)

- **One record, 4 sections** (Hàng mua · Nhận hàng · Chứng từ · Tiền đã trả) + Diễn biến (append-only timeline).
  Header shows `r-tracks` (Nhận hàng · Chứng từ · Tiền), each with its own state: wait / pend / you / ok / err. Never a stepper.
- **Receiving** (`--receive`): counted quantity per line (`r-qty`), optional expiry, receiver. Short → wait for the rest
  (receive again on the same PO) or close short. Confirm = stock in once by the counted quantity; result line shows stock
  before → after and the payable (by received quantity) with due date. Over-delivery: count above ordered → owner accepts
  the extra (new line, priced) or returns it.
- **After confirm** (`--received`): success banner, editable the same day (then a correction entry, never a silent edit).
- **Documents:** supplier e-invoice (mailbox or photo) matched with PO and receipt. Mismatch → the seller issues the
  adjustment invoice; the household never edits the seller's invoice; Agent drafts the message, the owner sends.
- **Money** (`--pay`): many payments per PO, before or after receipt; buying on credit with due date; one payment may
  cover several POs of the same supplier (đợt 4). OPC records only; optional supplier VietQR opens the owner's bank app;
  the bank feed (if connected) matches it.
- **New** (`purchase-new`): Đặt hàng trước | Hàng đã về, chưa có đơn; terms Trả khi nhận | Mua chịu | Trả trước một phần.
  Agent may propose (reason + supplier quote shown); nothing is sent before the owner approves.
- **Return** (`purchase-return`): from a received PO; stock out (not a sale), reason, photo of the signed return note;
  supplier offsets the next PO, refunds, or replaces; seller issues the adjustment invoice (rule to confirm with the accountant).
- Cost of goods: moving weighted average (proposal, accountant to confirm).

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/purchase-detail.html` · Đơn mua MH-0121 · đã đặt, trả trước một nửa · status v7-buy
- Page pattern: **detail**
- States: `purchase-detail--doc.html`, `purchase-detail--pay.html`, `purchase-detail--placed.html`, `purchase-detail--receive--offline.html`, `purchase-detail--receive.html`, `purchase-detail--received.html`
- Component spec: `bridge/opc-shadcn/purchase-detail.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×1014 · Đường dẫn 284,105 1124×44 · {label} 284,417 662×143 · aside 966,352 442×272
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×1014 · Đường dẫn 284,105 964×44 · {label} 284,417 566×143 · aside 870,352 378×335
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1329 · Đường dẫn 276,105 724×44 · {label} 276,441 724×143 · aside 276,1091 724×272
- **390**: header 0,0 390×65 · main 0,65 390×1631 · Đường dẫn 16,97 358×44 · {label} 16,594 358×111 · aside 16,1322 358×230 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×5 · --quiet --act
- `c-card` ×4
- `c-crumbs` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×25 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-kv` ×1
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
- h1 MH-0121 · Cơ sở Krông Pa
- h2 Hàng mua
- h2 Nhận hàng
- h2 Chứng từ
- h2 Tiền đã trả
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
- `purchase-detail--receive.html`
- `purchase-detail--pay.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

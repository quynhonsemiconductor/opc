# Handoff — Tiền · Công nợ (phải thu / phải trả)

- **Purpose:** who owes how much and what is overdue; who must be paid and when. **First read:** the total and the
  drill-in tile (overdue customer / next payable). **Primary:** "Xem & nhắc" on the overdue row; on Phải trả the only
  accent is "Trả 4.800.000 ₫" (bank-app deeplink, the owner confirms — N-06/N-07).
- **Why datatable:** many counterparties with comparable attributes, scanned and sorted; same family as Đơn hàng and
  Hoá đơn (r-listhead + ≤ 5 columns, stacks on phone).
- Rules (FLOWS ②b 16–19, ③ 8–10): a receivable exists only after an invoice is issued (delivered-not-invoiced shows
  as "Chưa tính"); carriers and bus companies holding COD are receivables tagged "thu hộ"; paying is never done by OPC.

## States
`receivables` (Phải thu) · `receivables--payables` (Phải trả). Not drawn: nothing owed, payment not confirmed by the
bank after 1 day ("Chờ xác nhận", owner marks it with a receipt), filters by age bucket.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/receivables.html` · Tiền · Công nợ phải thu · status v4-calm
- Page pattern: **datatable**
- States: `receivables--payables.html`
- Component spec: `bridge/opc-shadcn/receivables.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×770 · Phải thu 17.700.000 ₫: trong hạn 9.300.000 ₫, quá hạn 8.400.000 ₫ 284,260 1124×97 · Khách đang nợ 284,376 1124×364
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×774 · Phải thu 17.700.000 ₫: trong hạn 9.300.000 ₫, quá hạn 8.400.000 ₫ 284,260 964×97 · Khách đang nợ 284,376 964×368
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×866 · Phải thu 17.700.000 ₫: trong hạn 9.300.000 ₫, quá hạn 8.400.000 ₫ 276,260 724×151 · Khách đang nợ 276,431 724×368
- **390**: header 0,0 390×65 · main 0,65 390×1222 · Tiền 0,97 390×45 · Phải thu 17.700.000 ₫: trong hạn 9.300.000 ₫, quá hạn 8.400.000 ₫ 16,308 358×192 · Khách đang nợ 16,516 358×534 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×6 · --quiet
- `c-figure` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×31 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sign` ×6 · --err --wait
- `c-sub` ×3
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-table` ×1 · --stack
- `c-tabs` ×1
- `c-tag` ×2
- `r-listhead` ×1
- `r-page-head` ×1
- `r-shell` ×1
- `r-upcoming` ×1

### Outline
- h1 Công nợ

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
- `receivables--payables.html`
- `receivable-detail.html`
- `customer-statement.html`
- `money--overpay.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

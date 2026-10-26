# Handoff — Hoá đơn (invoices)

<!-- v41:start -->
## v4.1 (current)
> Layout and parts follow DESIGN.md §3 (v4.1). Primary = sea `--act`, one per view; money states use the truth palette. If any older note below disagrees with this block, this block wins.

- **Purpose:** This period's e-invoices and the one that needs attention.
- **First read:** "7.080.000 ₫" for the month; truth bar có mã 18 · chờ mã 1.
- **Primary action:** "Gửi lại" in the amber banner for HĐ 00000418.
- **Layout:** `r-listhead` (due tile is a neutral link "HĐ 00000418 · 640.000 ₫") → banner → tabs → 5-column table; CQT code shows its tail "…0421" (full code for SR + title).
- **Also:** invoices--accountant: compact density, 25 per page, rejected = `c-split__err`.
<!-- v41:end -->


- Visual reference: `../screens/invoices.html`. Content: BRIEF §10.4. Component spec: `bridge/opc-shadcn/invoices.md`.

## Data
- **Invoice Hub via Casso:** number, symbol, order, issue time, buyer (MST for company invoices), total, type,
  CQT state + code.
- **Status:** poll, because INVOICE webhooks were not observed (ADR 0012).
- **Mã CQT format:** e.g. `M1-26-QN7K2-00000000421`.

## States
- **Drawn:** one waiting for its tax code.
- **Not drawn:**
  - error (Hilo rejected: c-banner--err + reason + "Sửa và gửi lại")
  - invoice detail / PDF preview
  - empty month

## Interactions
- "Gửi lại" re-submits (idempotent per invoice number) and shows c-banner--ok.
- "Xem" opens the detail.
- A waiting invoice is still valid to hand to the customer (copy on the page).

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/invoices.html` · Hoá đơn · status v4-calm
- Page pattern: **data-table**
- States: `invoices--accountant.html`
- Component spec: `bridge/opc-shadcn/invoices.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×980 · Hoá đơn trong kỳ 284,195 1124×93 · Danh sách hoá đơn 284,469 1124×494 · Hoá đơn tháng 10 284,469 1124×494
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×1044 · Hoá đơn trong kỳ 284,251 964×93 · Danh sách hoá đơn 284,525 964×502 · Hoá đơn tháng 10 284,525 964×502
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1137 · Hoá đơn trong kỳ 276,275 724×103 · Danh sách hoá đơn 276,582 724×514 · Hoá đơn tháng 10 276,582 724×514
- **390**: header 0,0 390×65 · main 0,65 390×1756 · Tiền 0,97 390×45 · Hoá đơn trong kỳ 16,349 358×189 · Danh sách hoá đơn 16,833 358×759 · Hoá đơn tháng 10 16,833 358×759 · Điều hướng nhanh 0,779 390×65

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
- `c-banner` ×1 · --pend
- `c-brand` ×1
- `c-btn` ×10 · --quiet
- `c-card` ×1
- `c-figure` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×33 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sign` ×7 · --unk --pass
- `c-sub` ×3
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-table` ×1 · --stack
- `c-tabs` ×1
- `r-listcard` ×1
- `r-listhead` ×1
- `r-page-head` ×1
- `r-shell` ×1

### Outline
- h1 Hoá đơn

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
- `tax-evidence.html`
- `approvals--error.html`
- `invoice-detail.html`
- `receipt.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

<!-- v43:start -->
## v4.3 · data & decisions

Mẫu số 2 (hoá đơn bán hàng). Two series: Hilo cash-register (counter) and X Invoice with code (B2B). 'Chưa rõ kết quả' never auto-resent; corrections/replacements on the provider portal, OPC records and links.
<!-- v43:end -->

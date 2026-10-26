# Handoff — invoices--accountant

Accountant view of Hoá đơn: `data-density="compact"`, month filter, 25 per page, `c-pager`, export Excel (server-side, async for > 1.000 rows). Content: BRIEF §12 #7. See `invoices.md`.

<!-- handoff.mjs:start — generated 2026-10-05, do not edit inside this block -->
## Generated facts
- Screen: `../screens/invoices--accountant.html` · Hoá đơn · kế toán (compact, phân trang) · status v4-calm
- Page pattern: **data-table**
- States: none drawn
- Component spec: `bridge/opc-shadcn/invoices--accountant.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×797 · Hoá đơn trong kỳ 284,197 1124×93 · Danh sách hoá đơn tháng 9 284,335 1124×494 · Hoá đơn tháng 9 284,335 1124×494
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×805 · Hoá đơn trong kỳ 284,197 964×93 · Danh sách hoá đơn tháng 9 284,335 964×502 · Hoá đơn tháng 9 284,335 964×502
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×882 · Hoá đơn trong kỳ 276,257 724×103 · Danh sách hoá đơn tháng 9 276,405 724×510 · Hoá đơn tháng 9 276,405 724×510
- **390**: header 0,0 390×65 · main 0,65 390×1448 · Sổ & thuế 0,97 390×45 · Hoá đơn trong kỳ 16,329 358×227 · Danh sách hoá đơn tháng 9 16,602 358×784 · Hoá đơn tháng 9 16,602 358×784 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×9 · --quiet --act
- `c-card` ×1
- `c-figure` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×23 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sign` ×7 · --unk --pass --you
- `c-sub` ×2
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-table` ×1 · --stack
- `c-tabs` ×1
- `r-listcard` ×1
- `r-listhead` ×1
- `r-page-head` ×1
- `r-shell` ×1

### Outline
- h1 Hoá đơn · Tháng 9/2026

### Navigation out of this screen
- `receivables.html`
- `period.html`
- `books.html`
- `invoices.html`
- `audit.html`
- `help.html`
- `home--assistant.html`
- `home--notifications.html`
- `receipt.html`
- `invoice-detail.html`
- `home.html`
- `counter.html`
- `orders.html`
- `money.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

<!-- v43:start -->
## v4.3 · data & decisions

Delegated accountant (time-boxed) sees the month list, exports, drafts — cannot issue.
<!-- v43:end -->

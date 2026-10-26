# Handoff — Cần xử lý → Nhật ký (audit)

<!-- v41:start -->
## v4.1 (current)
> Layout and parts follow DESIGN.md §3 (v4.1). Primary = sea `--act`, one per view; money states use the truth palette. If any older note below disagrees with this block, this block wins.

- **Purpose:** What happened today, by whom.
- **First read:** Day heading + the feed; the event text leads, the time is meta (tabular).
- **Primary action:** None (read view).
- **Layout:** `r-feedbar`: time segment + "Ai làm: Tất cả" menu on one row, then "Việc" chips; dot key; `c-timeline` (ok · pend · ai = assistant draft, hatched · you = ink · system = hollow).
<!-- v41:end -->


- **What it shows:** append-only entries from the audit module. Each entry has the actor (person / Trợ lý /
  Hệ thống / Ngân hàng), the action, the object link, before → after values, the device and the time.
- **Filters:** by actor and by date. The accountant and the officer see only what the owner has granted.
- **Rules:** entries cannot be edited or deleted. Export goes through Dữ liệu & quyền riêng tư.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/audit.html` · Cần xử lý · nhật ký · status v4-calm
- Page pattern: **feed**
- States: none drawn
- Component spec: `bridge/opc-shadcn/audit.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×1268 · Nhật ký hôm nay 284,297 1124×954
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×1332 · Nhật ký hôm nay 284,361 964×954
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1412 · Nhật ký hôm nay 276,417 724×954
- **390**: header 0,0 390×65 · main 0,65 390×2215 · Sổ và kê khai 0,97 390×45 · Nhật ký hôm nay 16,606 358×1445 · Điều hướng nhanh 0,779 390×65

### Responsive behaviour (components that appear/disappear)
- `c-nav`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-brand`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-kbd`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-health`: 1440 shown · 1280 shown · 1024 hidden · 390 hidden
- `c-avatar`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-subnav`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown
- `c-tabbar`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown

### Components used (at 1440)
- `c-avatar` ×1
- `c-brand` ×1
- `c-btn` ×2 · --quiet
- `c-card` ×1
- `c-filter` ×5
- `c-filters` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×25 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-search` ×2
- `c-seg` ×1
- `c-sub` ×2
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-timeline` ×1
- `r-audit` ×1
- `r-page-head` ×1
- `r-shell` ×1

### Outline
- h1 Nhật ký

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
- `receipt.html`
- `order-detail.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

<!-- v43:start -->
## v4.3 · data & decisions

UI-19: append-only; each event = time · who (role) · what · before → after · source/device · event id; filter by time, actor type, object search.
<!-- v43:end -->

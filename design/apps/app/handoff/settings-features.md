# Handoff — Cài đặt → Tính năng

<!-- v41:start -->
## v4.1 (current)
> Layout and parts follow DESIGN.md §3 (v4.1). Primary = sea `--act`, one per view; money states use the truth palette. If any older note below disagrees with this block, this block wins.

- **Purpose:** Turn modules on/off; see what is coming.
- **First read:** Group "Đang dùng · 3".
- **Primary action:** Switches (`c-switch--row` with state pill).
- **Layout:** Groups "Đang dùng" and "Sắp có" (recede, no switch); "Bắt buộc" shows only the lock pill.
<!-- v41:end -->

- **Switches:** the values and rules come from SCOPE-MVP §4.
- **Locked switches:** a switch locked by a rule (purchasing when revenue > 1 tỷ) has `aria-disabled` and shows
  the reason.
- **Turning a switch off** hides menu items and keeps the data. **Turning it on** may start a short setup (for
  example, suppliers for purchasing).

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/settings-features.html` · Cài đặt · tính năng · status v4-calm
- Page pattern: **settings**
- States: none drawn
- Component spec: `bridge/opc-shadcn/settings-features.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×978
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×978
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×984
- **390**: header 0,0 390×65 · main 0,65 390×1456 · Cài đặt 0,97 390×93 · Điều hướng nhanh 0,779 390×65

### Responsive behaviour (components that appear/disappear)
- `c-nav`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-brand`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-search`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-kbd`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-health`: 1440 shown · 1280 shown · 1024 hidden · 390 hidden
- `c-btn`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-avatar`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-subnav`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown
- `c-tabbar`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown

### Components used (at 1440)
- `c-avatar` ×1
- `c-brand` ×1
- `c-btn` ×1 · --quiet
- `c-card` ×2
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×25 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-list` ×2
- `c-nav` ×1
- `c-search` ×1
- `c-sub` ×1
- `c-subnav` ×1 · --wrap
- `c-switch` ×6 · --row
- `c-tabbar` ×1
- `r-page-head` ×1
- `r-settings` ×1
- `r-shell` ×1

### Outline
- h1 Tính năng
- h2 Đang dùng · 3
- h2 Sắp có · 3

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
- `home--more.html`

### Tokens referenced by the layout
--space-4
<!-- handoff.mjs:end -->

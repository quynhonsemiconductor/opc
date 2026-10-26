# Handoff — onboard-firstsale

Part of the onboarding flow: see `onboarding.md`. Content: BRIEF §11. Component spec: `bridge/opc-shadcn/onboard-firstsale.md`.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/onboard-firstsale.html` · Onboarding · bán thử · status v4-calm
- Page pattern: **wizard**
- States: none drawn
- Component spec: `bridge/opc-shadcn/onboard-firstsale.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×831 · Hướng dẫn bán thử 284,195 662×158 · aside 966,195 442×500
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×831 · Hướng dẫn bán thử 284,195 566×158 · aside 870,195 378×500
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1351 · Hướng dẫn bán thử 276,195 724×158 · aside 276,884 724×500
- **390**: header 0,0 390×65 · main 0,65 390×1598 · Hướng dẫn bán thử 16,215 358×209 · aside 16,1090 358×429 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×6 · --quiet --act
- `c-coach` ×1 · --inline
- `c-decide` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×24 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-qrcard` ×1
- `c-search` ×1
- `c-sub` ×2
- `c-tabbar` ×1
- `r-page-head` ×1
- `r-pick` ×1
- `r-shell` ×1

### Outline
- h1 Bán thử
- h2 Giỏ hàng

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
- `onboard-done.html`
- `quick-sale.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

<!-- v43:start -->
## v4.3 · data & decisions

Guided test sale on the real counter at day 0: no stock counted yet, no customers yet; does not count as revenue.
<!-- v43:end -->

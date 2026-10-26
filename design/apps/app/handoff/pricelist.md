# Handoff — Bảng giá riêng (khách sạn & nhà hàng)

- **Purpose:** one customer price list. Items vs retail with the delta emphasised, effective date, customers on the
  list (rail). **Primary:** "Gán thêm khách"; row action "Đổi giá".
- `pricelist--edit` (drawer): new price + effective date + reason; OPC checks: not above retail (blocks sending when
  violated), confirmed orders keep the old price (list them), affected customers; optional customer notice drafted by
  the assistant, sent only after approval. **Primary:** "Gửi chị An duyệt" — the price is not used until approved
  (BA F02.05; policy rule "Đổi bảng giá → chị An duyệt").

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/pricelist.html` · Hàng hoá · Bảng giá khách sạn & nhà hàng · status v4-calm
- Page pattern: **datatable**
- States: `pricelist--edit.html`
- Component spec: `bridge/opc-shadcn/pricelist.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×480 · Giá trong bảng 284,260 662×169 · aside 966,260 442×253
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×480 · Giá trong bảng 284,260 566×211 · aside 870,260 378×253
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×669 · Giá trong bảng 276,260 724×169 · aside 276,449 724×253
- **390**: header 0,0 390×65 · main 0,65 390×921 · Kho hàng 0,97 390×45 · Giá trong bảng 16,368 358×250 · aside 16,634 358×208 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×4 · --quiet --act
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×24 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sub` ×2
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-table` ×1 · --stack
- `c-tabs` ×1
- `r-page-head` ×1
- `r-plist` ×1
- `r-shell` ×1

### Outline
- h1 Giá khách sạn & nhà hàng
- h2 Khách dùng bảng này

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
- `pricelist.html`
- `pricelist--edit.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

# Handoff — Chi tiết hoá đơn (invoice-detail) · 00000418

<!-- v41:start -->
## v4.1 (current)
> Layout and parts follow DESIGN.md §3 (v4.1). Primary = sea `--act`, one per view; money states use the truth palette. If any older note below disagrees with this block, this block wins.

- **Purpose:** Why an invoice has no tax code yet, and resend it.
- **First read:** Number + 640.000 ₫ under the title; amber "chờ mã CQT · 25 phút".
- **Primary action:** "Gửi lại ngay"; PDF / Zalo outline.
- **Layout:** `r-detail__head--calm` → banner → invoice facsimile | Diễn biến (event text leads, time is meta).
<!-- v41:end -->


- Content: BRIEF §13.4. Primary: **Gửi lại ngay**. The banner states that the invoice is still valid and when OPC
  retries on its own (10:50).
- **Preview:** `c-doc` mirrors the legal layout: title, ký hiệu, số, seller with MST, buyer, lines, total in figures
  and words, and the CQT footer with the lookup site.
- **Timeline:** shows the issue, the Hilo error, the resend and the payment verification.
- **Actions:**
  - Tải PDF is produced server-side.
  - Gửi cho khách qua Zalo uses ZNS or a share link.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/invoice-detail.html` · Chi tiết hoá đơn 00000418 · status v4-calm
- Page pattern: **detail**
- States: none drawn
- Component spec: `bridge/opc-shadcn/invoice-detail.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×875 · Đường dẫn 284,105 1124×44 · header 309,293 612×92 · Hàng hoá trên hoá đơn 309,570 612×143 · aside 966,263 442×517
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×913 · Đường dẫn 284,105 964×44 · header 309,331 516×92 · Hàng hoá trên hoá đơn 309,608 516×143 · aside 870,301 378×541
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1464 · Đường dẫn 276,105 724×44 · header 301,391 674×92 · Hàng hoá trên hoá đơn 301,668 674×143 · aside 276,1026 724×472
- **390**: header 0,0 390×65 · main 0,65 390×1880 · Tiền 0,97 390×45 · Đường dẫn 16,166 358×44 · header 33,527 324×163 · Hàng hoá trên hoá đơn 33,923 324×146 · aside 16,1335 358×466 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×3 · --quiet --act
- `c-crumbs` ×1
- `c-doc` ×1
- `c-figure` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×25 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sign` ×1 · --ok
- `c-sub` ×3
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-table` ×1 · --stack
- `c-timeline` ×1 · --quiet
- `r-shell` ×1

### Outline
- h1 Hoá đơn 00000231 Có mã CQT
- h2 Hoá đơn bán hàng
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
- `tax-evidence.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

<!-- v43:start -->
## v4.3 · data & decisions

Document view of an issued invoice (code from the tax authority), send via Zalo OA, PDF; timeline with the four roles.
<!-- v43:end -->

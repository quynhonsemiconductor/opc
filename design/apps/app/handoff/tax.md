# Handoff — Kê khai (v7.5.0)

- **Never show a computed tax amount in the pilot.** Show: quarter revenue (with / without invoice, link to the reconcile item),
  year-to-date vs revenue thresholds from versioned rule data (`ruleSet`, status "chờ kế toán xác nhận"; conflicting values shown),
  other mandatory notices (bank accounts, annual revenue) with state, and tracks Đối soát kỳ · Kế toán xem · Nộp trên eTax · Cơ quan thuế.
- `tax--return`: 6-step guide for eTax (VNeID level 2; choose form; copy revenue — copy buttons; eTax computes; sign; save notice).
  Banner "không phải tư vấn thuế". Download the evidence pack.
- `tax-file`: the owner uploads the eTax notices; **tiếp nhận** (received, transaction code) and **chấp nhận** (accepted) are separate
  states; reminder after 3 days without acceptance. `tax-file--signed`: accepted; edits after lock = amendment; tax payment is
  recorded only from the owner's payment document.
- `tax-evidence`: books (TT 152/2025 forms, PDF + Excel), e-invoices XML+PDF, bank statement, purchase documents (incl. photos),
  lock record, eTax notices, append-only change log; kept 10 years; accountant = view/download.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/tax.html` · Kê khai · Quý III/2026 (doanh thu, luỹ kế so với mốc, thông báo; không tính thuế) · status v7-books
- Page pattern: **detail**
- States: `tax--accountant.html`, `tax--return.html`
- Component spec: `bridge/opc-shadcn/tax.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×1110 · Đường dẫn 284,105 1124×44 · aside 966,344 442×335
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×1134 · Đường dẫn 284,105 964×44 · aside 870,344 378×335
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1538 · Đường dẫn 276,105 724×44 · aside 276,1236 724×335
- **390**: header 0,0 390×65 · main 0,65 390×2103 · Đường dẫn 16,97 358×44 · aside 16,1732 358×293 · Điều hướng nhanh 0,779 390×65

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
- `c-banner` ×1
- `c-brand` ×1
- `c-btn` ×4 · --quiet --act
- `c-card` ×3
- `c-crumbs` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×27 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-kv` ×1
- `c-meter` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sub` ×2
- `c-tabbar` ×1
- `c-timeline` ×1
- `r-jump7` ×1
- `r-page-head` ×1
- `r-pick` ×1
- `r-shell` ×1
- `r-tracks` ×1

### Outline
- h1 Quý III/2026
- h2 Doanh thu quý III
- h2 Luỹ kế năm so với mốc
- h2 Thông báo khác
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
- `period--item.html`
- `tax-notice-bank.html`
- `tax-notice-year.html`
- `tax--return.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

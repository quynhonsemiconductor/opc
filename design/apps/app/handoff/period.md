# Handoff — Đối chiếu kỳ (Quý III/2026)

- **Purpose:** is the period clean enough to lock. **First read:** "Cần xem · 5 việc" + the to-do list; the rail
  answers "do the sources match?" on the same screen. **Primary (head):** "Gửi chị An khoá kỳ", locked "còn n việc";
  enabled in `period--ready`. Lock belongs to the owner or the accountant; the operator sends the request.
- To-dos (FLOWS ⑤ step 2): delivered order without invoice · invoice without tax-authority code ("Chưa rõ kết quả":
  ask the provider, never re-issue) · money not assigned · input invoice on the tax portal not in the books ·
  expense without invoice (accountant decides). Each has its figure and one action; done checks collapse.
- Three sources (base = revenue from delivered orders): invoices in OPC · coded invoices on the tax portal (manual
  upload by the accountant while the portal is not connected) · money (received + receivable + unassigned). Each gap
  links to the to-do that clears it. OPC re-runs checks nightly and after every decision.
- Lock = period data frozen; changes after that need "mở lại kỳ" with approval and reason. Next: Tính thuế (UI-15).
- `period--item` (drawer): one exception decided in place; options with the assistant's pick; "Lưu quyết định"
  re-runs the checks. `period--ready`: all match, decisions listed with who/when.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/period.html` · Sổ & thuế · Đối chiếu Quý III/2026 (ba nguồn + việc trước khi khoá) · status v4-calm
- Page pattern: **detail**
- States: `period--item.html`, `period--locked.html`, `period--ready.html`
- Component spec: `bridge/opc-shadcn/period.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×912 · aside 966,264 442×681
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×931 · aside 870,264 378×700
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1527 · aside 276,879 724×681
- **390**: header 0,0 390×65 · main 0,65 390×2102 · Sổ và kê khai 0,97 390×45 · aside 16,1385 358×639 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×8 · --quiet --act
- `c-card` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×29 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sign` ×4 · --you --err --ok
- `c-sub` ×1
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-tabs` ×1
- `c-timeline` ×1 · --quiet
- `r-gate` ×2
- `r-recon` ×1
- `r-shell` ×1

### Outline
- h1 Quý III/2026 · đối chiếu Cần xem
- h2 Trước khi khoá kỳ · 5 việc
- h2 Ba nguồn có khớp không
- h2 Diễn biến kỳ

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
- `tax-file--signed.html`
- `order-detail--invoice.html`
- `connections--detail.html`
- `money--assign.html`
- `period--item.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

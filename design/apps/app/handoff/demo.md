# Handoff — Bảng điều khiển demo (demo build only)

- Not part of the product: render only when the build flag `DEMO=1` (and route `/demo`); dashed "DEMO · không có
  trong sản phẩm" frame. A floating "Demo" pill may open it from any screen in the demo build.
- Levers (sticky): view-as role (owner, operator, cashier, accountant, programme viewer), demo clock (named
  snapshots), simulated connector states per connector (Hoạt động · Không trả lời · Lỗi · Chưa kết nối · Mất mạng).
- Path: the BA end-to-end flow as 10 deep links (UI-01 start). Scenarios: 8 exception cases, each a deep link with a
  preset (role + clock + connector states). Reset (`demo--reset`) restores the seed data set (FLOWS §0.1) and default
  connector states; it never touches real data (the demo build has no real connectors).

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/demo.html` · Demo · bảng điều khiển (không thuộc sản phẩm) · status v4-calm
- Page pattern: **dashboard**
- States: `demo--reset.html`
- Component spec: `bridge/opc-shadcn/demo.md`

### Regions per size
- **1440**: main 160,0 1120×1266 · header 180,24 1080×213
- **1280**: main 80,0 1120×1266 · header 100,24 1080×213
- **1024**: main 0,0 1024×1401 · header 20,24 984×213
- **390**: main 0,0 390×3075 · header 20,24 350×336

### Responsive behaviour (components that appear/disappear)
- no component changes visibility between sizes (layout reflows only)

### Components used (at 1440)
- `c-btn` ×8 · --act
- `c-ic` ×6
- `c-seg` ×2
- `c-sub` ×1
- `c-tag` ×16
- `r-demo` ×1

### Outline
- h1 Bảng điều khiển demo
- h2 Đặt trước khi trình bày
- h2 Luồng xuyên suốt · 10 bước · bắt đầu ở đây
- h2 Kịch bản ngoại lệ · nhảy thẳng vào

### Navigation out of this screen
- `approvals.html`
- `demo--reset.html`
- `readiness.html`
- `purchase-detail--receive.html`
- `sales-inbox.html`
- `approvals--detail.html`
- `delivery--pick.html`
- `order-detail--invoice.html`
- `period.html`
- `tax.html`
- `program.html`
- `stock.html`
- `approvals--error.html`
- `receivable-detail--assign.html`
- `connections.html`
- `delivery--pick--offline.html`
- `tax-evidence.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

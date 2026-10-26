# Handoff — Đăng ký · Cách bán (bước 3/5)

- **Purpose:** decide which readiness items this household gets (FLOWS ⓪). Two multi-select questions: how you sell
  (quầy · khách sỉ/khách sạn · online) and where goods come from (mua về bán · tự chế biến); each option states what it
  adds to the plan; chosen = tint + hairline, the accent stays on the primary.
- Running summary right above "Tiếp tục": total items · required before wholesale · recommended · already done.
  Changing later = Cài đặt › Hộ & mô hình (recomputes Sẵn sàng, no data lost). "Chưa chắc" → staff help.
- Phase A (5 steps, v6.0.0): Số điện thoại · Hộ kinh doanh · Cách bán và việc OPC làm · Xác minh chủ hộ · Hàng đầu tiên → bán thử → Xong → `readiness--new`. Bank, invoices, e-signature are gates in Sẵn sàng.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/onboard-model.html` · Đăng ký · Cách bán (3/6) · status v4-calm
- Page pattern: **wizard**
- States: none drawn
- Component spec: `bridge/opc-shadcn/onboard-model.md`

### Regions per size
- **1440**: header 0,0 1440×73 · main 216,113 560×1035 · Các bước đăng ký 824,113 400×414 · footer 216,672 560×228
- **1280**: header 0,0 1280×73 · main 136,113 560×1035 · Các bước đăng ký 744,113 400×414 · footer 136,572 560×228
- **1024**: header 0,0 1024×73 · main 232,73 560×1075 · Các bước đăng ký 232,1148 560×150 · footer 0,540 1024×228
- **390**: header 0,0 390×73 · main 0,73 390×1136 · footer 0,615 390×229

### Responsive behaviour (components that appear/disappear)
- `c-stepmap`: 1440 shown · 1280 shown · 1024 shown · 390 hidden

### Components used (at 1440)
- `c-btn` ×1 · --act --block
- `c-ic` ×7
- `c-icon-btn` ×1 · --outline
- `c-option` ×9 · --big --on
- `c-options` ×4
- `c-stepmap` ×1
- `c-steps` ×1
- `r-model` ×2
- `r-onboard` ×1
- `r-yn` ×2

### Outline
- h1 Chị bán thế nào?
- h2 Bán cho ai
- h2 Hàng từ đâu

### Navigation out of this screen
- `onboard-household--read.html`
- `onboard-help.html`
- `onboard-features.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

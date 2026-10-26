# Handoff — Pilot dashboard (Program Viewer)

- **Who:** programme manager (role Program Viewer). Own shell: Tổng quan pilot · Hộ tham gia · Báo cáo · Dữ liệu được
  xem · Trợ giúp; no household switcher, no assistant, no write actions on household data.
- **Data rule (F15.05):** aggregates only; households appear with stage and flags, never money/orders/customers/
  invoices; groups under 3 households are merged; households consent to this level on joining (TrustLine on every page).
- **program:** stats with last-period movement; funnel along the BRD success definition on one base (joined → set up →
  real sale → invoice); smaller-base steps (one tax period done, still used after 90 days) in a separate labelled group
  with hatched shorter bars; need-help by issue type (each links to the household row); adoption by feature (30 days).
  **Primary:** "Xuất báo cáo". Recomputed nightly.
- **program--help:** households grouped Cần hỗ trợ / Ổn × stage × issue × who supports × days; read-only.
- **program-report:** KPI table with definitions and base rows, findings, proposals (S16.09 30/90-day review); "Tải PDF".

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/program.html` · Chương trình · Pilot dashboard (Program Viewer) · status v4-calm
- Page pattern: **dashboard**
- States: `program--help.html`
- Component spec: `bridge/opc-shadcn/program.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×1064 · aside 966,414 442×525
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×1064 · aside 870,414 378×525
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1718 · aside 276,1226 724×525
- **390**: header 0,0 390×65 · main 0,65 390×2088 · aside 16,1526 358×483 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×2 · --act --quiet
- `c-card` ×2
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×12
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-link` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sub` ×1
- `c-tabbar` ×1
- `c-work` ×4
- `c-works` ×1
- `r-adopt` ×1
- `r-funnel` ×2 · --part
- `r-page-head` ×1
- `r-pstats` ×1
- `r-shell` ×1 · --program
- `r-trust` ×1 · --gate

### Outline
- h1 Pilot Kế nghiệp số · đợt 1
- h2 Hộ qua từng bước
- h3 Trên 2 hộ đã đủ thời gian (hộ sớm)
- h2 Đang dùng gì · 30 ngày
- h2 Cần hỗ trợ · 4 hộ

### Navigation out of this screen
- `program.html`
- `program--help.html`
- `program-report.html`
- `home--notifications.html`
- `program--help.html#h1`
- `program--help.html#h2`
- `program--help.html#h3`
- `program--help.html#h4`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

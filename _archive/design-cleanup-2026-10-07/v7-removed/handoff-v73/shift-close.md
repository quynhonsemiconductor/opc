# Handoff — Đóng ca (cash drawer close) + nộp tiền thu hộ

- **Who:** the cashier of the shift (role Thu ngân). **Purpose:** close the drawer honestly. **First read:** "Phải có
  trong két" vs "Đếm được" and the over/short chip. **Primary:** "Đóng ca", locked with its reason until a difference
  has a reason.
- Expected cash = opening float + cash sales + COD handed in by the household's deliverer − cash expenses (with
  receipts) — all computed by OPC from orders and expense slips of the shift (OPC kiểm tra). Count by denomination.
- Difference policy (setup-policy): under the threshold (default 50.000 ₫) a reason is enough and the owner is told;
  at or above, the owner approves. Result line: float kept for the next shift + amount handed to the owner.
- COD: the deliverer's cash enters the drawer when the cashier confirms (`shift-close--cod`: count vs expected; "Đếm
  lệch" records a difference); bus-company and carrier COD are not in the drawer — they stay receivables until paid.
- After close (`shift-close--done`): shift locked (reopen needs owner approval and a reason); the owner confirms the
  hand-over on her phone; printable report; full trail in Nhật ký.

<!-- handoff.mjs:start — generated 2026-10-08, do not edit inside this block -->
## Generated facts
- Screen: `../screens/shift-close.html` · Tiền · Đóng ca sáng (đếm két, lệch cần lý do) · status v4-calm
- Page pattern: **form**
- States: `shift-close--cod.html`, `shift-close--done.html`
- Component spec: `bridge/opc-shadcn/shift-close.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×1343 · aside 966,199 442×644
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×1633 · aside 870,199 378×711
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1959 · aside 276,1396 724×596
- **390**: header 0,0 390×65 · main 0,65 390×2635 · Tiền 0,97 390×45 · aside 16,1884 358×672 · Điều hướng nhanh 0,779 390×65

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
- `c-card` ×1
- `c-field` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×18 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-kv` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-seg` ×1
- `c-sign` ×5 · --you --err --pass --wait
- `c-sub` ×3
- `c-subnav` ×1
- `c-tabbar` ×1
- `r-den` ×1
- `r-plist` ×1
- `r-recon` ×1
- `r-shell` ×1

### Outline
- h1 Đóng ca sáng Thiếu 20.000 ₫
- h2 Tiền mặt trong két
- h3 Đếm theo mệnh giá
- h2 Trong ca
- h2 Tiền thu hộ

### Navigation out of this screen
- `home.html`
- `orders.html`
- `help.html`
- `home--assistant.html`
- `home--notifications.html`
- `money.html`
- `receivables.html`
- `invoices.html`
- `purchases.html`
- `stock.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

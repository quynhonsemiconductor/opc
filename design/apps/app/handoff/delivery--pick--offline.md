# Handoff — Mẫu mất mạng dùng chung (FLOWS §0 nguyên tắc 8)

- **Device offline ≠ connector error.** Shell chip `c-health--off` (pending tone) "Mất mạng · n việc chờ"; banner
  `r-offbar` at the top of the content with "Xem n việc chờ". On phone the banner is the indicator.
- Three behaviours, decided per action (not per screen):
  1. **Works offline, saved on device:** picking ticks, counts, stock take, cash sales at the counter (only on the
     last-known available stock).
  2. **Queued** (`r-qchip` on the object, `r-queue` drawer): Soạn xong, messages, document photos — ordered, each with
     a client-generated idempotency key, cancellable while queued.
  3. **Needs the server, locked with the reason:** hand-over (stock leaves once), QR, invoices with a code, approvals,
     money out. Never fake success.
- Reconnect: send in order, re-check each on the server; the first item that needs a decision stops the chain
  (later items held). Example `delivery--pick--back`: lot locked while offline → part accepted, part rejected, message
  held; primary = the fix. Everything logged; nothing deducted twice. PWA install recommended on counter devices.
- `delivery--pick--queue` = the drawer; `delivery--pick--back` = the reconnect result.

<!-- handoff.mjs:start — generated 2026-10-05, do not edit inside this block -->
## Generated facts
- Screen: `../screens/delivery--pick--offline.html` · Offline · soạn hàng khi mất mạng · status v4-calm
- Page pattern: **detail**
- States: none drawn

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×817 · Bán 284,105 1124×45 · Đường dẫn 284,265 1124×44 · aside 966,375 442×329
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×841 · Bán 284,105 964×45 · Đường dẫn 284,289 964×44 · aside 870,399 378×373
- **1024**: Điều hướng chính 0,0 224×768 · header 224,0 800×73 · main 224,73 800×1123 · Bán 248,105 752×45 · Đường dẫn 248,289 752×44 · aside 248,873 752×283
- **390**: header 0,0 390×65 · main 0,65 390×1674 · Bán 0,97 390×45 · Đường dẫn 16,383 358×44 · aside 16,1219 358×392 · Điều hướng nhanh 0,779 390×65

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
- `c-banner` ×1
- `c-brand` ×1
- `c-btn` ×3 · --quiet --act
- `c-card` ×2
- `c-crumbs` ×1
- `c-health` ×1 · --off
- `c-hh` ×2 · --bar
- `c-ic` ×29 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-kv` ×2
- `c-nav` ×1
- `c-search` ×1
- `c-sign` ×1 · --wait
- `c-sub` ×1
- `c-subnav` ×1
- `c-tabbar` ×1
- `r-offbar` ×1
- `r-offrules` ×1
- `r-pick` ×1
- `r-qchip` ×1
- `r-shell` ×1

### Outline
- h1 Soạn DH-2052 · Sunrise Hotel Soạn xong · chờ gửi
- h2 Lấy hàng
- h2 Bàn giao
- h2 Trên máy này

### Navigation out of this screen
- `home.html`
- `counter.html`
- `orders.html`
- `money.html`
- `purchases.html`
- `invoices.html`
- `approvals.html`
- `settings-users.html`
- `home--assistant.html`
- `home--notifications.html`
- `sales-inbox.html`
- `delivery.html`
- `delivery--pick--queue.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

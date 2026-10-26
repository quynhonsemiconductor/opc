# Handoff — Nối bằng khoá (payOS) và các màn quản lý khoá

- **Who:** chủ hộ only (nhập, đổi, gỡ khoá). **First read:** khoá được giữ thế nào. **Primary:** "Thử kết nối" (chưa lưu gì cho tới khi qua thử).
- Ba cách giữ khoá (`mode` trong `tools/v4/providers.py`): **Nối qua Casso** (`connections--casso`: nhập mật khẩu ở trang Cas Link, OPC chỉ giữ grant), **Cho phép** (OAuth, chủ hộ OTP), **Dán khoá** (màn này). Khoá dán vào kho bí mật, sau khi lưu chỉ hiện 4 số cuối, không hiện lại.
- Form: Client ID (không bí mật), API Key và Checksum Key (che, nút Hiện), địa chỉ nhận báo tiền (chỉ đọc, nút Chép). Lỗi: `data-invalid` trên ô sai + banner "Chưa lưu gì".
- Quản lý (`connections--manage`): Thử lại · Đổi khoá (`--rotate`: khoá cũ chạy tới khi khoá mới qua thử; nút khoá tới khi dán đủ) · Gỡ (`--remove`: nêu hậu quả, nhắc xoá khoá ở nhà cung cấp). Mỗi lần ghi nhật ký.
- Hướng dẫn (`connections--guide`, `--guide-casso`): bước "Ở <nơi>", lỗi thường gặp, "Nhờ chị Thu". Nội dung cổng bên thứ ba CẦN KIỂM LẠI (xem NOTES).
- Trạng thái khoẻ hiển thị bằng chữ; biểu tượng chỉ cho việc cần chủ hộ.

<!-- handoff.mjs:start — generated 2026-10-07, do not edit inside this block -->
## Generated facts
- Screen: `../screens/connections--key.html` · Kết nối · Dán khoá (payOS)
- Page pattern: **connector flow**
- Note: Khoá cất kín, chỉ 4 số cuối, địa chỉ nhận báo tiền.
- States: `connections--key--error.html`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×804 · Đường dẫn 284,105 1124×44 · aside 966,251 442×365
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×804 · Đường dẫn 284,105 964×44 · aside 870,251 378×365
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1189 · Đường dẫn 276,105 724×44 · aside 276,857 724×365
- **390**: header 0,0 390×65 · main 0,65 390×1287 · Đường dẫn 16,97 358×44 · aside 16,885 358×323 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×5 · --quiet --act
- `c-card` ×2
- `c-crumbs` ×1
- `c-field` ×4
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×26 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-link` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sign` ×1 · --pend
- `c-sub` ×1
- `c-tabbar` ×1
- `r-gate` ×1
- `r-keys` ×2
- `r-shell` ×1

### Outline
- h1 Nối payOS Chỉ chị An
- h2 Khoá từ payOS
- h2 Dán vào payOS · nơi nhận báo tiền
- h2 Khoá của chị được giữ thế nào

### Navigation out of this screen
- `home.html`
- `counter.html`
- `approvals.html`
- `orders.html`
- `sales-inbox.html`
- `delivery.html`
- `customers.html`
- `products.html`
- `stock.html`
- `production.html`
- `purchases.html`
- `suppliers.html`
- `money.html`
- `receivables.html`
- `shift-close.html`
- `period.html`
- `books.html`
- `invoices.html`
- `audit.html`
- `connections.html`
- `readiness.html`
- `setup-business.html`
- `setup-data.html`
- `setup-policy.html`
- `settings-features.html`
- `settings-display.html`
- `help.html`
- `home--assistant.html`
- `home--notifications.html`
- `connections--add.html`
- `connections--guide.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

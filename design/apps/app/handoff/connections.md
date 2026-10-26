# Handoff — Kết nối (top-level) + luồng kết nối

- **Who:** chủ hộ (đồng ý), người vận hành (xem, làm tay). **First read:** kết nối nào đang lỗi (chấm đỏ trên menu, dòng đỏ trong bảng).
- Thẻ theo tài khoản (nối một lần, nhiều việc, bật/tắt từng việc) · `connections--category` = Việc OPC làm (12 việc) · `connections--add` thêm cách nối theo việc (danh mục nhà cung cấp là dữ liệu, 71 dòng) · tài khoản → `connections--account`; lỗi → `connections--detail`; chưa kết nối → `connections--provider`.
- Luồng: chi tiết → chọn nhà cung cấp → đồng ý (chỉ chủ hộ: phạm vi, 180 ngày, OTP Zalo) → đọc thử → `connections--unknown` nếu không trả lời → nhật ký.
- Quy tắc: OPC không tự gửi lại khi chưa rõ kết quả; mọi kết nối có đường làm tay; OPC không chuyển tiền, không nộp thuế. Nút Đồng ý khoá tới khi đủ 6 số.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/connections.html` · Cài đặt · Kết nối (17 nhóm) · status v4-calm
- Page pattern: **datatable**
- States: `connections--account.html`, `connections--add.html`, `connections--casso.html`, `connections--category.html`, `connections--consent.html`, `connections--delivery.html`, `connections--detail.html`, `connections--disconnect.html`, `connections--feature.html`, `connections--guide-casso.html`, `connections--guide.html`, `connections--info.html`, `connections--key--error.html`, `connections--key.html`, `connections--log.html`, `connections--manage.html`, `connections--many.html`, `connections--provider.html`, `connections--remove.html`, `connections--request.html`, `connections--rotate.html`, `connections--testing.html`, `connections--unknown.html`, `connections--use.html`
- Component spec: `bridge/opc-shadcn/connections.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×982
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×982
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1382
- **390**: header 0,0 390×65 · main 0,65 390×1990 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×4 · --quiet --act
- `c-card` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×30 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sign` ×6 · --pass --err --ok
- `c-sub` ×1
- `c-tabbar` ×1
- `c-tabs` ×1
- `r-acct` ×6 · --ok --err
- `r-gate` ×1
- `r-page-head` ×1
- `r-shell` ×1

### Outline
- h1 Kết nối
- h2 Chưa có cách nối · đang làm tay

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
- `connections--category.html`
- `connections--log.html`
- `connections--account.html`
- `connections--detail.html`
- `connections--manage.html`
- `connections--provider.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

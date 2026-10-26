# Handoff — Đăng ký bước 3/5: Việc OPC làm (màn thứ hai của bước 3)

- **Who:** chủ hộ. **First read:** 4 việc cần nối để bắt đầu. **Primary:** "Tiếp tục".
- Danh sách 12 việc sinh từ mô hình (màn trước), chia Cần để bắt đầu / Nên có / Khi cần (`tools/v4/capabilities.py`). Mỗi việc cần có sẵn một cách nối gợi ý + "Đổi" (`onboard-feature`), hoặc nhờ nhân viên OPC nối giúp. Chữ ký số: chờ chương trình chọn (chưa có cách để chọn).
- "Cần" nghĩa là khoá luồng phụ thuộc (tiền chuyển khoản, đơn sỉ, hoá đơn có mã), không khoá cả app.
- `onboard-feature` = chọn cách cho một việc: cách chọn được, "Sắp có" (bấm để OPC báo), nhân viên OPC nối giúp. Nút chính nêu tên cách đang chọn.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/onboard-features.html` · Đăng ký · Việc OPC làm (3/6)
- Page pattern: **onboarding step**
- Note: Features first: 11 việc OPC làm, 4 cần nối để bắt đầu; cách nối gợi ý sẵn, Đổi được.
- States: none drawn
- Component spec: `bridge/opc-shadcn/onboard-features.md`

### Regions per size
- **1440**: header 0,0 1440×73 · main 216,113 560×604 · Các bước đăng ký 824,113 400×414 · footer 216,717 560×164
- **1280**: header 0,0 1280×73 · main 136,113 560×604 · Các bước đăng ký 744,113 400×414 · footer 136,636 560×164
- **1024**: header 0,0 1024×73 · main 232,73 560×644 · Các bước đăng ký 232,717 560×150 · footer 0,604 1024×164
- **390**: header 0,0 390×73 · main 0,73 390×721 · footer 0,699 390×145

### Responsive behaviour (components that appear/disappear)
- `c-stepmap`: 1440 shown · 1280 shown · 1024 shown · 390 hidden

### Components used (at 1440)
- `c-btn` ×2 · --act --block
- `c-ic` ×5
- `c-icon-btn` ×1 · --outline
- `c-say` ×1
- `c-stepmap` ×1
- `c-steps` ×1
- `r-feat` ×3
- `r-onboard` ×1

### Outline
- h1 Việc OPC làm cho chị
- h2 Cần nối · 1
- h2 OPC lo sẵn · 2

### Navigation out of this screen
- `onboard-model.html`
- `onboard-help.html`
- `onboard-feature.html`
- `onboard-gov.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

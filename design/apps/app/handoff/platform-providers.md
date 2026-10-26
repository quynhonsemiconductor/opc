# Handoff — Bảng điều khiển nền tảng (QNSC): nhà cung cấp

- **Who:** quản trị QNSC (vai trò riêng, chỉ thấy số hộ, không thấy dữ liệu của hộ). **First read:** 4 nhà cung cấp cần xem. **Primary:** "Thêm nhà cung cấp".
- Bảng: nhà cung cấp · cách nối · trạng thái (kèm lý do chặn từ `GATE`) · số hộ đang nối · khoá nền tảng. Dòng cần xem có vạch bên. Phone: mỗi dòng xếp chồng, nhãn cột in trước giá trị (`data-l`).
- `platform-provider` (Casso): khoá QNSC, nơi Casso gọi về, nhà cung cấp đi qua, "Nếu gỡ Casso" (6 hộ, 11 nhà cung cấp). `--remove`: Ẩn (hộ đang nối vẫn chạy) hay Gỡ hẳn (ngắt, xoá khoá, không hoàn tác); lý do bắt buộc, nút khoá tới khi có lý do. `--new`: chọn cách nối + ô hộ phải nhập, xem trước "Hộ sẽ thấy", nút Lưu dính dưới.
- Danh mục là dữ liệu: thêm = thêm một dòng; ẩn = `visible:false`.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/platform-providers.html` · Nền tảng · Nhà cung cấp
- Page pattern: **platform console**
- Note: Sổ đăng ký nhà cung cấp của QNSC (chỉ số hộ).
- States: none drawn
- Component spec: `bridge/opc-shadcn/platform-providers.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×1537 · Nhà cung cấp 284,351 1124×1169
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×1576 · Nhà cung cấp 284,351 964×1208
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1832 · Nhà cung cấp 276,351 724×1464
- **390**: header 0,0 390×65 · main 0,65 390×3379 · Nhà cung cấp 16,407 358×2851 · Điều hướng nhanh 0,779 390×65

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
- `c-btn` ×1 · --act
- `c-filter` ×5
- `c-filters` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×26
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-search` ×1
- `c-sign` ×14 · --pass --wait
- `c-sub` ×2
- `c-tabbar` ×1
- `c-table` ×1 · --stack
- `r-page-head` ×1
- `r-reg` ×1
- `r-shell` ×1 · --program
- `r-trust` ×1 · --gate

### Outline
- h1 Nhà cung cấp

### Navigation out of this screen
- `platform-providers.html`
- `program.html`
- `home--notifications.html`
- `platform-provider--new.html`
- `platform-provider.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

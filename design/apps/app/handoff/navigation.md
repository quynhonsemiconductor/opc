# Handoff — Navigation and information architecture (v7.1.0)

- Source of truth: `tools/v4/navtree.py` (SECTIONS / FOOT / ROLES). Older notes (v2.0) are gone.
- **Desktop rail** (`c-nav`, source `tools/v4/navtree.py`, applied by `nav7.py`): Tổng quan (Hôm nay, Cần xử lý) · Mua hàng (Đơn mua, Nhà cung cấp, Chi phí) · Bán hàng (Yêu cầu, Đơn bán, Giao hàng, Khách hàng) · Kho hàng (Hàng và giá, Tồn kho, Kiểm kho) · Tiền (Thu chi và đối chiếu, Công nợ, Hoá đơn) · Sổ và kê khai (Kỳ và đối soát, Kê khai, Sổ sách, Nhật ký). Footer: Thiết lập (Sẵn sàng, Hộ kinh doanh, Dữ liệu nền, Người dùng và quyền, **Kết nối** with a red count, Tính năng, Hiển thị) · Trợ giúp và hỗ trợ.
- **Kết nối** tabs: Đã nối · Việc OPC làm · Nhật ký. "Thêm cách nối" (ways grouped by feature) opens from Việc OPC làm; the QNSC console (`platform-*`) has its own rail.
- **Phone:** `c-tabbar` Tổng quan · Mua · Bán · Kho · Thêm (BA). "Thêm" opens `home--more` (full-screen list of every destination, current page first).
- **Roles** (`ROLES`): cashier sees Hôm nay, Quầy, Đơn hàng, Đóng ca; accountant sees Sổ & thuế and Công nợ; a lone child shows flat under its own name.
- **Routes:** group-first URLs (`/ban/don-hang`, `/tien/doi-soat`, `/so-thue/hoa-don`, `/can-xu-ly`, `/ket-noi`). Each child is a route, not a client-side tab.
- **Feature switches** (Cài đặt → Tính năng) show or hide children; the rail never reorders. Turning a switch off keeps the data.
- **Never show a disabled menu:** hide what a role cannot open.

## Provider names (v7.5.1, CEO decision)
Never render a provider's name or mark on household screens. Use the role: "bên hoá đơn điện tử", "hoá đơn máy tính tiền", "ngân hàng MB",
"đơn vị giao hàng". Provider names appear only where the owner picks or manages a provider: Kết nối (connections*) and registration
(onboard*). Handoff docs may name providers for integration; the UI copy may not.

## Status chips and tracks (v7.5.2)
Every `c-sign` chip, `r-tracks` track and gate row uses one of 7 states from `system/maps/status.json`:
ok (đã xong/khớp) · pass (bình thường) · pend (chờ khớp/xác minh/cơ quan) · wait (đang làm / lượt người khác) · you (cần chị) · err (hỏng/quá hạn/thiếu) · unk (chưa rõ).
FE: implement as one `<StatusBadge state>` with the icon fixed by state; the label is free text. Never pick colour or icon per screen.

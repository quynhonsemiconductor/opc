# Handoff — Navigation and information architecture (v2.0)

- Source: `system/SCOPE-MVP.md` §2 and BRIEF §14.
- **Desktop:** `c-nav` lists Hôm nay · Quầy · Bán · Tiền · Hàng · Sổ & thuế · Cần xử lý, with Cài đặt and Trợ giúp
  in the footer. Each group page starts with `c-subnav`.
- **Phone:** `c-tabbar` with Hôm nay · Quầy · Đơn · Tiền · Thêm. "Thêm" opens `home--more` (full-screen dialog
  with a `c-menulist` of every destination; Cần xử lý first).
- **Routes:** use group-first URLs (`/ban/don-hang`, `/tien/doi-soat`, `/so-thue/hoa-don`, `/can-xu-ly`,
  `/cai-dat/tinh-nang`). Each sub-nav item is a route, not a client-side tab.
- **Feature switches** (Cài đặt → Tính năng) only show or hide sub-nav items and menulist rows; the sidebar
  never changes. Turning a switch off keeps the data.
- **Permissions:** hide what a role cannot open (a cashier sees Hôm nay · Quầy · Tiền → Đóng ca); never show a
  disabled menu.
- **Counts:** nav and tab counts come from one server count of "needs the owner"
  (Bán 3 · Tiền 3 · Cần xử lý 6).

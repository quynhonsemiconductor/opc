# Handoff — Đơn hàng (orders)

- Visual reference: `../screens/orders.html`. Content: BRIEF §10.1. Component spec: `bridge/opc-shadcn/orders.md`.
- **Purpose:** today's orders, and which ones need the owner.
- **First read:** the one-line summary "Đã thu · chưa thu".
- **Primary action:** none is yellow. Rows that need the owner carry the yellow edge (`c-table__row--you`).

## Layout
- **1440:**
  1. r-page-head (Tạo đơn, Mở quầy)
  2. c-say summary
  3. c-tabs: Cần xem 3 · Chờ xác minh 2 · Chưa thu 2 · Hoàn tất 19 · Hôm nay 23 (selected) · Tất cả
  4. Filter row: channel `c-filters` + `c-search`
  5. Table of the 12 most recent orders, then "Xem thêm 11 đơn"
- **1024:** the Giờ / Kênh / Món columns hide.
- **390:** channel chips hidden (search only); rows stack. Channel and time move into the customer line
  (`c-table__phone`). The tabs fade at the edge to show they scroll.

## Data
- **Orders API (today, local tz):** code, time, customer, channel, items, total, payment method, payment state,
  order state, invoice number + tax-code state.
- **Tab counts:** come from the server.
- "Cần xem" = pending QR over 30 min, orders awaiting confirmation, transfers awaiting assignment.

## States
- **Not drawn:**
  - empty day
  - loading
  - order detail (next screen to design)
  - search with no result (c-empty)

## Interactions
- Row click opens the order detail (not drawn).
- `/` focuses search.
- Tabs and filters combine. Pagination is "Xem thêm".

## List tools (v1.4)
- **`r-listbar`:** search (combobox with suggestions after 2 characters, grouped Khách / Đơn, matches highlighted)
  · date preset (Hôm nay default · 7 ngày · Tháng này · Tự chọn → c-cal dialog, future dates disabled) · Lọc
  (count badge) · sort menu (Mới nhất / Tổng tiền lớn nhất / Cần xem trước).
- **Filter panel:** a dialog (full screen on phone) with groups Thời gian, Kênh, Thanh toán, Trạng thái đơn and
  Hoá đơn. Its footer button shows the live count ("Xem 4 đơn").
- **Active filters:** shown as `c-chip` with ×, plus "Xoá lọc" and the result count and total.
- **No result:** c-empty with "Tìm trong tất cả thời gian" / "Xoá tìm kiếm".
- **URL** keeps q, date, filters, sort and page. Owners use "Xem thêm" (+12).
- The page has no yellow action. Rows that need the owner use the row marker; yellow is used only inside dialogs
  (Áp dụng / Xem n đơn) and on the no-result action.

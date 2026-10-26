# Handoff — Đơn hàng (orders)

<!-- v41:start -->
## v4.1 (current)
> Layout and parts follow DESIGN.md §3 (v4.1). Primary = sea `--act`, one per view; money states use the truth palette. If any older note below disagrees with this block, this block wins.

- **Purpose:** Today's orders and which ones need the owner.
- **First read:** "Đã thu hôm nay 8.460.000 ₫" — the only figure; truth bar under it.
- **Primary action:** None in the head; "Chưa thu · 2 đơn · 1 quá hạn / 5.570.000 ₫ ›" is a neutral link tile to the filtered list (pairwise pick A, 8.2).
- **Layout:** `r-listhead` → tabs (Cần xem · Chờ xác minh · Chưa thu · Hoàn tất · Hôm nay · Tất cả) → search/filters → 5-column table: Khách·đơn (`c-table__who`), Thanh toán, Trạng thái (labelled pill), Hoá đơn, Tổng. 390: rows stack.
- **Also:** 9 states share this head (search, filters, daterange, filtered, noresult, bulk, bulk--preview, peek, loading).
<!-- v41:end -->


- Visual reference: `../screens/orders.html`. Content: BRIEF §10.1. Component spec: `bridge/opc-shadcn/orders.md`.

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

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/orders.html` · Đơn hàng · status v7-v4-calm
- Page pattern: **data-table**
- States: `orders--bulk--preview.html`, `orders--bulk.html`, `orders--daterange.html`, `orders--filtered.html`, `orders--filters.html`, `orders--loading.html`, `orders--noresult.html`, `orders--peek.html`, `orders--search.html`
- Component spec: `bridge/opc-shadcn/orders.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×1029 · Tiền của đơn hôm nay 284,211 1124×93 · Danh sách đơn hàng 284,449 1124×553 · Bảng — vuốt hoặc cuộn ngang để xem thêm cột 284,449 1124×553
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×1029 · Tiền của đơn hôm nay 284,211 964×93 · Danh sách đơn hàng 284,449 964×553 · Bảng — vuốt hoặc cuộn ngang để xem thêm cột 284,449 964×553
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1147 · Tiền của đơn hôm nay 276,267 724×103 · Danh sách đơn hàng 276,567 724×553 · Bảng — vuốt hoặc cuộn ngang để xem thêm cột 276,567 724×553
- **390**: header 0,0 390×65 · main 0,65 390×1702 · Bán hàng 0,97 390×45 · Tiền của đơn hôm nay 16,344 358×189 · Danh sách đơn hàng 16,726 358×837 · Bảng — vuốt hoặc cuộn ngang để xem thêm cột 16,726 358×837 · Điều hướng nhanh 0,779 390×65

### Responsive behaviour (components that appear/disappear)
- `c-nav`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-brand`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-kbd`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-health`: 1440 shown · 1280 shown · 1024 hidden · 390 hidden
- `c-avatar`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-subnav`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown
- `c-seg`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `r-phone-only`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown
- `c-tabbar`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown

### Components used (at 1440)
- `c-avatar` ×1
- `c-brand` ×1
- `c-btn` ×6 · --quiet --block
- `c-card` ×1
- `c-figure` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×60 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-menu` ×2
- `c-menu-anchor` ×2 · --end
- `c-nav` ×1
- `c-search` ×2
- `c-seg` ×1
- `c-sign` ×32 · --ok --pass --wait --unk --pend
- `c-sub` ×2
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-table` ×1 · --stack
- `c-tabs` ×1
- `r-listbar` ×1
- `r-listcard` ×1
- `r-listhead` ×1
- `r-page-head` ×1
- `r-phone-only` ×8
- `r-shell` ×1

### Outline
- h1 Đơn bán

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
- `quick-sale.html`
- `home--more.html`

### Tokens referenced by the layout
--space-4
<!-- handoff.mjs:end -->

<!-- v43:start -->
## v4.3 · data & decisions

One list for every channel; source shown per order (Quầy · Zalo OA · Thêm tay · Định kỳ); states per FLOWS Phụ lục A; 'Đã thu' head = received (verified + pending); chưa thu = delivered and unpaid.
<!-- v43:end -->

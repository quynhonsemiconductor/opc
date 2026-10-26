# Handoff — Bán · Yêu cầu (một hộp cho mọi nguồn)

- **Purpose:** turn messy requests (Zalo OA, pasted chats, photos, voice, files, standing orders) into a valid order
  without retyping. **First read:** the original message, then "Trợ lý hiểu là". **Primary action:** "Kiểm tra giá,
  tồn, công nợ" (or "Gửi qua Zalo OA" when something is missing).
- **Why split:** a stream of requests read one by one. Phone: list → detail page (to draw).
- Flow: `FLOWS.md` ②a. Channels: `SCOPE-MVP.md` §7 #11b; connector categories §8 (#11 chat, #15 AI).

## Data & content
| Field | Source | Format | Empty | Truncation |
|---|---|---|---|---|
| Source + time + who added | request: channel (zalo_oa / manual_paste / photo / voice / file / standing), received_at, added_by | icon + text | — | — |
| Original | request payload (text, image, audio transcript, file) | quote; uncertain spans marked | — | full |
| Lines | assistant extraction: said_text → matched SKU, qty + unit, price (customer price list) | table, stacks on phone | "Chưa rõ" | — |
| Customer, delivery, invoice, missing | extraction + customer profile | `c-kv` | "Chưa có hồ sơ" | — |

## States
`sales-inbox` (all matched) · `sales-inbox--unclear` (ambiguous quantity → question) · `sales-inbox--add` (manual add).
Not drawn: reading in progress, voice transcript view, unknown customer → create profile, duplicate request, ignored.

## Interactions
"Kiểm tra" runs the rule checks: all pass → draft order + reservation → Order 360; any fail → job in Cần xử lý (the
Sunrise demo fails on credit, hence the link to approvals). Nothing is created before the checks. "Gửi qua Zalo OA"
sends the assistant's question only after a person presses it; customers who never messaged the OA cannot receive
it → call or personal Zalo, then "Tự sửa".

## Accessibility
Table region focusable with a label; uncertain line has text "Chưa rõ", not colour only; dialog traps focus (inert).

## Open questions
Which pilot hotels already use the household's Zalo OA (affects how many requests arrive by manual add).

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/sales-inbox.html` · Bán · Yêu cầu (hộp yêu cầu mọi nguồn) · status v4-calm
- Page pattern: **split**
- States: `sales-inbox--add.html`, `sales-inbox--unclear.html`
- Component spec: `bridge/opc-shadcn/sales-inbox.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×916 · Danh sách yêu cầu 284,276 478×410 · Món Trợ lý đọc được 807,500 580×219
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×1022 · Danh sách yêu cầu 284,276 409×410 · Món Trợ lý đọc được 738,524 489×301
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1189 · Danh sách yêu cầu 276,276 304×410 · Món Trợ lý đọc được 625,548 354×323
- **390**: header 0,0 390×65 · main 0,65 390×873 · Bán hàng 0,97 390×45 · Danh sách yêu cầu 16,384 358×410 · Điều hướng nhanh 0,779 390×65

### Responsive behaviour (components that appear/disappear)
- `c-nav`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-brand`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-search`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-kbd`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-health`: 1440 shown · 1280 shown · 1024 hidden · 390 hidden
- `c-avatar`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-subnav`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown
- `c-quote`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-table`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-match`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-kv`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-tabbar`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown

### Components used (at 1440)
- `c-avatar` ×1
- `c-brand` ×1
- `c-btn` ×5 · --quiet --act
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×30 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-kv` ×1
- `c-match` ×2
- `c-nav` ×1
- `c-quote` ×1
- `c-search` ×1
- `c-sign` ×3 · --ok --you --wait
- `c-sub` ×1
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-table` ×1 · --stack
- `c-tabs` ×1
- `c-work` ×3
- `c-works` ×1
- `r-page-head` ×1
- `r-shell` ×1
- `r-tower` ×1 · --list

### Outline
- h1 Yêu cầu bán
- h2 Sunrise Hotel · chị Mai (bếp)
- h3 Trợ lý hiểu là

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
- `sales-inbox--add.html`
- `sales-inbox--unclear.html`
- `order-detail.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

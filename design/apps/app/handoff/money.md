# Handoff — Tiền & đối soát (money) + state money--assign

<!-- v41:start -->
## v4.1 (current)
> Layout and parts follow DESIGN.md §3 (v4.1). Primary = sea `--act`, one per view; money states use the truth palette. If any older note below disagrees with this block, this block wins.

- **Purpose:** Show which money is real; resolve what needs the owner.
- **First read:** The verified amount (72px hero, "Đã xác minh · 4 khoản · khớp sao kê MB"). The legend item for verified says "= số lớn ở trên" (said once).
- **Primary action:** "Gán đơn" on Cần xem #1 (opens money--assign). #2/#3 are quiet.
- **Layout:** 1440: hero + facts (Số dư MB, Tiền mặt trong ca) | flat "Cần xem" panel; truth bar + legend links (Chờ xác minh → list, Chưa gán → assign); ledger rows with tabs. 1024: facts wrap under the hero. 390: one column, hero → Cần xem → ledger.
- **Also:** money--assign: dialog with the best match (`c-option--best`, "Nên chọn"), "Cách khác", folded "Không chọn được"; footer previews the result; focus trapped.
<!-- v41:end -->


- Visual reference: `../screens/money.html`, `money--assign.html`. Component spec: `bridge/opc-shadcn/money*.md`. Content: BRIEF §10.2–10.3.

## Data
| Field | Source |
|---|---|
| Balance | Casso Balance Hook (timestamped) |
| Credits | Casso Transactions. Raw sender and content are shown **exactly as received** |
| Matching | order code in the transfer content (DH1043 → DH-1043) |
| Status | `received_unverified` (Casso reported) → `verified` (matched against the MB statement by polling, since webhooks are unsigned, ADR 0012) |
| Age warning | "quá 30 phút" when `received_unverified` is older than 30 min |

## States
- **Drawn:** default (tab Cần xem); `money--assign` (dialog open, option 1 chosen).
- **Not drawn:**
  - empty ("Chưa có tiền vào hôm nay")
  - offline (c-banner--err on top; figures "đến hh:mm")
  - after assignment (c-banner--ok "Đã gán 2.150.000 ₫ vào DH-1038" + Hoàn tác for 10 s)

## Interactions
- Tabs filter the table. The state-panel arrows jump to the matching tab.
- "Kiểm tra" on a pending credit older than 30 min opens the transfer detail with the advice to check the MB
  app or ask the customer.
- **Dialog (APG dialog-modal):**
  - Opens from "Gán vào đơn"; focus goes to the title, Esc closes.
  - The options are a radiogroup. The candidates come from the API with match reasons (amount, name, time,
    content); disabled candidates show why.
  - Nothing is committed until "Gán vào DH-1038". The footer note previews the result.
  - Option 3 (tiền khác) excludes the credit from revenue.

## Open questions
- Who may assign money (owner only, or staff too)? Is an audit log entry required? (Yes per ADR 0005 outbox.)
- Is undo allowed after the invoice is issued? (Proposal: undo only within 10 s, before issuing.)

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/money.html` · Tiền & đối soát · status v4-calm
- Page pattern: **matching**
- States: `money--assign.html`, `money--cash.html`, `money--duplicate.html`, `money--help.html`, `money--overpay.html`, `money--split.html`
- Component spec: `bridge/opc-shadcn/money.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×1135
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×1146
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1561
- **390**: header 0,0 390×65 · main 0,65 390×2079 · Tiền 0,97 390×45 · Điều hướng nhanh 0,779 390×65

### Responsive behaviour (components that appear/disappear)
- `c-nav`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-brand`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-search`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-kbd`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-health`: 1440 shown · 1280 shown · 1024 hidden · 390 hidden
- `c-avatar`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-subnav`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown
- `c-tabbar`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown

### Components used (at 1440)
- `c-avatar` ×1
- `c-brand` ×1
- `c-btn` ×7 · --quiet --act
- `c-card` ×2
- `c-count` ×1
- `c-debts` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×29 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-nav` ×1
- `c-orders` ×1
- `c-search` ×1
- `c-sign` ×5 · --ok --you --pend
- `c-split` ×1
- `c-stat` ×1
- `c-sub` ×1
- `c-subnav` ×1
- `c-tabbar` ×1
- `c-tabs` ×1
- `c-todo` ×1
- `r-home` ×1
- `r-page-head` ×1
- `r-shell` ×1

### Outline
- h1 Tiền & đối chiếu
- h2 Đã khớp sao kê MB hôm nay
- h2 Cần xem 4
- h3 Gán 585.000 ₫ vào đơn
- h3 DH-2045 chờ quá 30 phút
- h3 Sunrise vừa chuyển 8.400.000 ₫
- h3 195.000 ₫ có thể trùng
- h2 Tiền vào MB hôm nay

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
- `money--help.html`
- `money--assign.html`
- `money--cash.html`
- `order-detail.html`
- `money--split.html`
- `money--duplicate.html`
- `home--more.html`

### Tokens referenced by the layout
--space-2 --act-ink --space-4 --space-8 --side-min --facts-w
<!-- handoff.mjs:end -->

<!-- v43:start -->
## v4.3 · data & decisions

Hero = match state ('Đã khớp sao kê MB hôm nay', n/m khoản). Ledger lists what needs action first (unassigned, pending > 30 min). Assign dialog: suggestion with ✓/✗ reasons, one-to-many ('Chia cho nhiều đơn hoặc hoá đơn'), prepayment credit, non-sales income.
<!-- v43:end -->

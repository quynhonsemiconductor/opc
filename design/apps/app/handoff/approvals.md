# Handoff — Cần xử lý (Control Tower của chủ hộ)

- **Purpose:** every job OPC and the assistant are running for the household, and the ones that need a person.
  **First read:** the selected job's title and the decision panel. **Primary action:** the decision (Duyệt đơn).
- **Why split (list + detail):** a stream of jobs, each needs reading before acting (triage one by one); jobs are not
  compared side by side, so not a table. Phone: list → `approvals--detail` page.
- Flow: `system/FLOWS.md` ② (and every flow's exceptions). Rules: `SCOPE-MVP.md` §7 #19.

## Data & content
| Field | Source | Format | Empty | Truncation |
|---|---|---|---|---|
| Tabs + counts | workflow state: waiting_human · running · waiting_connector · error (retry_scheduled/blocked) · completed today | count | 0 hides the count | — |
| Row state, time, title, situation, source | workflow: state, updated_at, subject (order/purchase/invoice…), summary, source channel/actor | `c-sign`, HH:MM | — | title 2 lines |
| Timeline steps | workflow events with `actor_kind` = assistant · rule · person · connector | role label + time + what + detail | — | — |
| Rule checks | rule results per check (khách, giá, tồn, công nợ) | pass/fail chips | — | — |
| Decision | approval task: problem, impact figure, assistant proposal, allowed approvers, required reason | — | reason starts empty (placeholder only) | — |

## States
`approvals` (Cần chị quyết) · `approvals--running` · `approvals--error` (invoice outcome unknown) · `approvals--detail`
(phone). Not drawn yet: Chờ kết nối tab, Xong hôm nay tab, empty ("Không có việc nào cần chị"), approval of a short
goods receipt (HTX), blocked after re-check.

## Interactions
- Duyệt / Từ chối need a reason (min 5 characters); after approval OPC **re-validates** (stock, credit, order version)
  and the job either continues or returns as blocked with the new reason. Undo is not offered for approvals.
- Error (outcome unknown): no automatic resend; OPC re-polls on a schedule (shown as a chip). "Phát hành lại" stays
  `aria-disabled` until the owner confirms on the provider portal that no invoice exists.
- Keyboard: tabs are a tablist (arrow keys); rows are links; ↑/↓ moves the selection on desktop (to build).

## Accessibility
Main landmark; list `aria-label`; selected row `aria-current="true"`; rule chips carry "đạt / không đạt" text; the
decision is a `group` labelled by its question.

## Open questions
Câu 1/2 (tax filing, invoice type) do not affect this page. Counts in the nav = Cần chị quyết + Lỗi.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/approvals.html` · Cần xử lý · Control Tower (Cần chị quyết) · status v4-calm
- Page pattern: **split**
- States: `approvals--detail.html`, `approvals--error.html`, `approvals--running.html`
- Component spec: `bridge/opc-shadcn/approvals.md`

### Regions per size
- **1440**: Điều hướng chính 0,0 252×900 · header 252,0 1188×73 · main 252,73 1188×1127 · Danh sách việc 284,276 478×258
- **1280**: Điều hướng chính 0,0 252×800 · header 252,0 1028×73 · main 252,73 1028×1268 · Danh sách việc 284,276 409×258
- **1024**: Điều hướng chính 0,0 252×768 · header 252,0 772×73 · main 252,73 772×1626 · Danh sách việc 276,276 304×278
- **390**: header 0,0 390×65 · main 0,65 390×592 · Danh sách việc 16,255 358×258 · Điều hướng nhanh 0,779 390×65

### Responsive behaviour (components that appear/disappear)
- `c-nav`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-brand`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-search`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-kbd`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-health`: 1440 shown · 1280 shown · 1024 hidden · 390 hidden
- `c-btn`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-avatar`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-timeline`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-rules`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-decide`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-kv`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-tabbar`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown

### Components used (at 1440)
- `c-avatar` ×1
- `c-brand` ×1
- `c-btn` ×4 · --quiet --act
- `c-decide` ×1
- `c-health` ×1
- `c-hh` ×2 · --bar
- `c-ic` ×29 · --s
- `c-icon-btn` ×2
- `c-kbd` ×1
- `c-kv` ×1
- `c-nav` ×1
- `c-rules` ×1
- `c-search` ×1
- `c-sign` ×2 · --you
- `c-sub` ×1
- `c-tabbar` ×1
- `c-tabs` ×1
- `c-timeline` ×1
- `c-work` ×2
- `c-works` ×1
- `r-page-head` ×1
- `r-shell` ×1
- `r-tower` ×1 · --list

### Outline
- h1 Cần xử lý
- h2 Nhà hàng Phố Núi · 6.900.000 ₫

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
- `approvals--detail.html`
- `home--more.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

# Handoff — Tiền & đối soát (money) + state money--assign

- Visual reference: `../screens/money.html`, `money--assign.html`. Component spec: `bridge/opc-shadcn/money*.md`. Content: BRIEF §10.2–10.3.
- **Purpose:** show which money is real, and resolve the credits that need the owner.
- **First read:** the money-by-state panel (Đã xác minh · Chờ xác minh · Chưa gán).
- **Primary action:** "Gán vào đơn" on the unmatched credit (the one yellow button). The state-panel arrows are
  navigation only (`c-msign__go--quiet`).

## Layout
| Width | Layout |
|---|---|
| 1440 / 1280 | `AppShell`. r-page-head (title, MB connection line, "Đếm tiền cuối ca") → row of cards: Số dư MB (balance + c-kv account facts) · Tiền vào MB hôm nay (c-msigns) · Tiền mặt trong ca → c-say definition line → c-card with c-tabs + c-table |
| 1024 | Cards wrap to 2 columns; optional table columns hide |
| 390 | Single column: money-by-state first; account facts hidden; table stacks (time + amount, then sender/content, then status + action) |

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

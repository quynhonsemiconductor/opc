# Handoff — Tổng quan (home)

- Visual reference: `../screens/home.html` · shots: `../shots/home-*.png` · component spec: `bridge/opc-shadcn/home.md`
- **Purpose:** answer "is today's money real?" and "what do I do first?"
- **First read:** the 72px revenue figure, then lane 1.
- **Primary action:** lane 1's yellow button (Đối chiếu). On desktop the page also has "Mở quầy bán hàng".

## Layout
| Width | Layout |
|---|---|
| 1440 / 1280 | `AppShell` (sidebar 252px). Grid 1.6fr / 1fr: Money (full width) → Cần xử lý \| Thuế, Công nợ → Đơn gần đây (full) → 7 ngày \| Trợ lý |
| 1024 | Sidebar 224px; grid 1.25fr / 1fr; lanes switch to their narrow layout (container ≤ 560px); the Giờ / Kênh / Món columns hide |
| 390 | No sidebar; `PhoneTabBar` at the bottom. Single column: Money → Cần xử lý → Thuế → Công nợ → 7 ngày → Đơn → Trợ lý. Page actions hidden (Quầy is in the tab bar; Tạo đơn / Ghi khoản chi sit under Thêm). The money sign panel is replaced by a one-line legend |

## Data & content
| Field | Source | Format | Empty |
|---|---|---|---|
| Doanh thu hôm nay, đơn count, % vs hôm qua | orders aggregate (tenant, today, local tz) | `8.460.000 ₫` · `23 đơn` · `↑ +19%` | `0 ₫ · chưa có đơn` |
| Verified / pending / cash split | payments by state (`verified`, `received_unverified`, cash) | money | each 0 ₫ |
| Connection lines | Casso link status + last sync; Hilo; tax portal | "MB (qua Casso) · cập nhật 2 phút trước" | "chưa kết nối" (`ConnectionStatus off`) |
| Lanes 1–3, Việc khác 4–6 | tasks API ranked server-side (money first, then orders, invoices, stock, consents) | one fact each: title · amount · hint | empty state (not drawn) |
| Thuế | tax module: year revenue vs 1 tỷ threshold, quarter estimate, due date | `1.284.500.000 ₫`, `31/10/2026` | — |
| Đơn gần đây | last 6 orders | code · time · customer · channel · items · total + MoneyLine · state | — |
| Công nợ | receivables by customer | money + link to related lane | "Không có công nợ" |

## States
- **Default:** drawn.
- **Drawn in v1.2:**
  - `home--offline.html`: one c-banner--err at the top; figures say "đến 10:44"
  - `home--firstrun.html`: setup lanes; the done step uses `Lane--done`; money is c-empty
- **Changed in v1.2:** "Mở quầy bán hàng" is a plain button, because Quầy is always in the nav and the one yellow
  action is lane 1's. The state arrows are quiet.
- **Not drawn:**
  - no tasks (c-empty "Không có việc cần xử lý")
  - loading skeleton
  - staff permission

## Interactions
- The pending `MoneySign` go-arrow jumps to lane 1.
- Lane "Chi tiết" (phone) expands the hidden detail.
- Search: `/` focuses search.
- Lane actions open their task flows (not drawn).

## Accessibility
- Landmarks: nav, header, main.
- Lanes are an `<ol>`; numerals are `aria-hidden` because order is semantic.
- `MoneyLine` and `TruthBar` use `role="img"` with an aria-label.
- Status is always shown as a word.

## Open questions
- Ranking rules for lanes (product): is a large unverified QR always lane 1?
- The owner's delivery limit (2.000.000 ₫) is a setting. Where is it edited?

# Handoff — Quầy bán hàng (counter) + states counter--cart, counter--payment

- Visual reference: `../screens/counter.html`, `counter--cart.html` (phone), `counter--payment.html` (phone).
  Component spec: `bridge/opc-shadcn/counter*.md`.
- **Purpose:** sell a cart and take payment fast, with a payment state that cannot be misread.
- **First read:** the total `1.020.000 ₫` and the "ĐANG Ở ĐÂY" station.
- **Primary action:** "Thu tiền" (phone). On desktop, payment confirmation is automatic.

## Layout
- **Context:** the whole page runs in `data-density="touch"` (56px targets).
- **Focus mode:** `CounterShell` header (menu, ← Tổng quan, title, connections, Đóng ca). No sidebar.

| Width | Layout |
|---|---|
| 1440 | products \| `OrderTicket` 400px \| `PaymentPanel` 420px; each column scrolls on its own; the payment column fits 900px height |
| 1280 | 380 / 400 |
| 1024 | products (2 columns) \| one sticky 440px side column (ticket above payment); the total repeats in the payment footer |
| 390 | product rows with 56px + buttons; fixed `PhoneCartBar`: "Sửa giỏ" → `counter--cart`, "Thu tiền" → `counter--payment` (both are a `Drawer`) |

## Data & content
| Field | Source | Format |
|---|---|---|
| Products | catalog + stock (low-stock threshold) | name · price `/kg` · stock line |
| Cart lines | local cart state (offline-safe, ADR 0008) | weight `0,5 kg`, qty `×2`, line total |
| VietQR | Casso QR Pay; content `DH1043` | amount, bank |
| Payment state | Casso transaction webhook **plus polling** (webhooks are unsigned, ADR 0012) | `awaiting_customer` → `received_unverified` → `verified` |
| Invoice | cash-register e-invoice, issued automatically after payment (Hilo via Casso) | fixed notice + optional company invoice / print |

## States
Changed in v1.2: all main states are drawn.

| File | State | What changes |
|---|---|---|
| `counter.html` | awaiting customer | — |
| `counter--received.html` | received, unverified | Ladder on station 2. The delivery rule is in the caption. The confirm stays locked; the one act button is "Giao hàng trước · bán đơn tiếp" (N), and the order moves to Tiền & đối soát |
| `counter--verified.html` | verified 10:47 | `MoneyConfirm--done` (light green), invoice 00000422 · chờ mã CQT, steppers disabled; act "Đơn mới DH-1044" (N) |
| `counter--cash.html` | cash | Field "Khách đưa" + quick amounts; `ChangeDue` "Tiền thối 80.000 ₫"; confirm enabled (F9) |
| `counter--offline.html` | bank link down 10:45 | c-banner--err; QR option `aria-disabled`; cash preselected |
| `counter--empty.html` | DH-1044, no lines | c-empty in the ticket; confirm locked "Thêm món để thu tiền" |
| `counter--cart.html` | phone cart sheet | — |
| `counter--payment.html` | phone payment sheet | — |
| `counter--payment--received.html` / `--verified.html` | phone sheets | Same changes as the desktop states |

Not drawn yet:
- công nợ (customer picker)
- out-of-stock tap (`ProductButton disabled` is in the catalog)
- customer short of money in cash (`ChangeDue--short` is in the catalog)

## Interactions
- **Keys:** `/` search · `+` / `−` quantity · `F9` take payment · `Esc` cancel.
- **Confirmation:** the confirm button stays locked (`aria-disabled`, reason "Tự xác nhận khi ngân hàng
  báo") until the bank reports. There is no manual override in v1 (product decision).
- **Huỷ đơn:** destructive. It needs a confirmation dialog (not drawn) and sits apart from Lưu tạm.

## Accessibility
- The QR status line is `aria-live="polite"`.
- The ladder is an `<ol>` with `aria-current="step"`.
- Stepper buttons have item-specific labels ("Bớt mực khô").
- The QR image has alt text with the amount and content.

## Open questions
- Whether to allow manual "đã nhận" for a bank that is down (risk) — product/finance.
- Weighed items: scale integration, or manual entry only?

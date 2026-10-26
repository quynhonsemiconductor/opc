# Handoff — Quầy bán hàng (counter) + 11 states · v4.0 "Modern · Calm"

- Visual reference: `../screens/counter.html` and every `counter--*.html`. Component spec per file:
  `bridge/opc-shadcn/counter*.md`. Components: `../../../system/components/catalog.html` (sections "Món ở Quầy",
  "Đơn đang bán", "Thu tiền QR", "Thu tiền mặt", "Phản hồi").
- The states are **generated** by `tools/v4/states.py` from `tools/v4/src/counter.html` and
  `src/counter--qr.html`; edit the templates, then re-run.
- **Purpose:** sell a cart and take payment fast, with a payment state that cannot be misread.
- **First read:** the total `1.020.000 ₫` in the order panel; during payment, the current step of `PaymentSteps`.
- **Primary action:** one per state — Thu tiền (F9) → (QR waits automatically) → Giao hàng · bán đơn tiếp (N) → Đơn mới (N).

## Layout (changed in v4.0)
- `data-density="touch"` on the whole page (56px targets). `CounterLayout` header: ← Tổng quan · title + shift ·
  `ConnectionPill` · Đóng ca. No sidebar.

| Width | Layout |
|---|---|
| 1440 / 1280 | products (search, `FilterBar`, `TileGrid` auto-fill 196px) \| `OrderPanel` 440px |
| 1024 | products \| `OrderPanel` 400px; total shrinks to 36px |
| 390 | tiles become rows with a 44px round add; fixed dark `PhoneCartPill` (total + Thu tiền) opens `OrderPanel` as `Sheet side="bottom"` (`r-pos--sheet`) |

- `OrderPanel` order of parts: head (DH-1043 · 4 món, customer picker, ✕ Huỷ) → `OrderLine`s (scroll) → foot:
  `SegmentedChoice` (QR · Tiền mặt · Công nợ) → total (largest figure on screen) → Lưu tạm | **Thu tiền F9** →
  invoice note. Payment is **step 2 in the same panel** (`OrderPanel--pay`, ← back to the lines).

## Data & content
| Field | Source | Format |
|---|---|---|
| Products | catalog + stock (low-stock threshold) | name · price + `/kg` · `còn 3,2 kg` (amber + icon when low) |
| Cart lines | local cart (offline-safe, ADR 0008) | `0,5 kg × 1.250.000 ₫`, line total |
| VietQR | Casso QR Pay, content `DH1043` | QR 196px + amount 36px + `VietQR · MB · nội dung DH1043` |
| Payment state | Casso webhook **plus polling** (webhooks unsigned, ADR 0012) | `awaiting_customer` → `received_unverified` → `verified` |
| Payer | bank transaction | `từ NGUYEN VAN HUNG · nội dung DH1043` |
| Delivery rule | owner setting (default 2.000.000 ₫) | "Giao hàng được — đơn dưới mức 2.000.000 ₫ bạn đặt" |
| Invoice | cash-register e-invoice issued after payment (Hilo) | note under the action; "Hoá đơn chờ mã CQT" after verification |

## States
| File | State | What changes |
|---|---|---|
| `counter.html` | cart, choosing | 4 lines, QR selected, Thu tiền enabled |
| `counter--qr.html` | awaiting customer | `QrCard` → `PaymentSteps` (step 1 now, pulse) → `WaitBar` "OPC tự chuyển bước — không cần bấm" → "Khách đổi sang trả tiền mặt" |
| `counter--received.html` | received, unverified | **Money moment:** `MoneyArrived` (amber hatch) replaces the QR, step 2 now, `InlineNote` delivery rule; primary "Giao hàng · bán đơn tiếp" (N); desktop toast "Đã nhận 1.020.000 ₫ · giao hàng được" |
| `counter--verified.html` | verified 10:47 | `MoneyArrived--ok` (check draws), steps 1–2 done, 3 now; "Hoá đơn chờ mã CQT"; primary "Đơn mới DH-1044", secondary "In lại phiếu"; toast |
| `counter--cash.html` | cash | `CashPad` 1.100.000 + `QuickAmounts` (first = "vừa đủ") → `ChangeDue` 80.000 ₫; primary "Đã thu tiền mặt · thối 80.000 ₫" (F9) |
| `counter--offline.html` | bank down 10:45 | `ConnectionPill--err`; `Banner--err` in the panel; QR option struck "QR tạm tắt" (aria-disabled); cash preselected, empty; commit locked "Nhập số tiền khách đưa để thu" |
| `counter--empty.html` | new order DH-1044 | `OrderEmpty`; no tile in cart; both commits locked "Thêm món để thu tiền"; toast "DH-1043 đã xong" |
| `counter--undo.html` | item removed | line gone, total 935.000 ₫; toast "Đã bỏ Chả cá Quy Nhơn · 85.000 ₫" + **Hoàn tác** (6 s) |
| `counter--cart.html` | phone: order sheet | sheet over products; the just-added tile pops once |
| `counter--payment.html`, `--payment--received.html`, `--payment--verified.html` | phone payment sheets | same as desktop states; **no toast** while the sheet is open (the panel announces itself) |

Not drawn yet: công nợ (customer picker), out-of-stock tap, customer short of money (`ChangeDue--short` exists),
Huỷ đơn confirmation dialog.

## Interactions & motion
- **Keys:** `/` search · `+` / `−` quantity of the selected line · `F9` Thu tiền · `N` next order · `Esc` huỷ.
- **Add item:** tile gets `data-incart` + qty badge; `data-justadded` pop (320 ms spring) on the tile and badge.
- **Money arrived:** `MoneyArrived` enters with a 480 ms spring; `--ok` draws the check after 200 ms. Optional
  sound/vibration is a setting (not drawn). All motion off with `prefers-reduced-motion`.
- **No manual "confirm" for QR** in v1 (product decision): the system moves the steps; cash has its own commit.
- **Remove line:** immediate, with undo toast (never a confirm dialog for one line).

## Accessibility
- `PaymentSteps` is an `<ol>` with `aria-current="step"` and the words "Đang ở đây".
- `WaitBar` is `role=status` polite; `MoneyArrived` is `role=status` **assertive** (the cashier may not be looking).
- Toast region `aria-live="polite"`; the undo button is a real button (≥ 44px).
- Disabled commits use `aria-disabled` and say what unlocks them. The struck QR option has an aria-label with the reason.
- Stepper buttons have item-specific labels ("Bớt mực khô"). QR image alt has amount and content.

## Open questions
- Manual "đã nhận" when the bank is down (risk) — product/finance.
- Weighed items: scale integration or manual entry?
- Sound on money arrived: default on or off?

<!-- handoff.mjs:start — generated 2026-10-08, do not edit inside this block -->
## Generated facts
- Screen: `../screens/counter.html` · Quầy bán hàng · status v4-calm
- Page pattern: **pos**
- States: `counter--cart.html`, `counter--cash.html`, `counter--debt.html`, `counter--empty.html`, `counter--offline.html`, `counter--payment--received.html`, `counter--payment--verified.html`, `counter--payment.html`, `counter--qr.html`, `counter--received.html`, `counter--undo.html`, `counter--verified.html`
- Component spec: `bridge/opc-shadcn/counter.md`

### Regions per size
- **1440**: header 0,0 1440×77 · Chọn món 0,77 1000×823 · aside 1000,77 440×823
- **1280**: header 0,0 1280×77 · Chọn món 0,77 840×723 · aside 840,77 440×723
- **1024**: header 0,0 1024×77 · Chọn món 0,77 624×691 · aside 624,77 400×691
- **390**: header 0,0 390×73 · Chọn món 0,73 390×560

### Responsive behaviour (components that appear/disappear)
- `c-kbd`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `r-order`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-oline`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-stepper`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `c-seg`: 1440 shown · 1280 shown · 1024 shown · 390 hidden
- `r-cartbar`: 1440 hidden · 1280 hidden · 1024 hidden · 390 shown

### Components used (at 1440)
- `c-btn` ×5 · --xl --act
- `c-chip` ×3
- `c-health` ×1
- `c-ic` ×16 · --s
- `c-icon-btn` ×3 · --outline
- `c-kbd` ×7
- `c-oline` ×2
- `c-search` ×1
- `c-seg` ×1
- `c-stepper` ×2
- `c-tile` ×2 · --big
- `c-tiles` ×1 · --few
- `r-cartbar` ×1
- `r-order` ×1
- `r-pos` ×1

### Outline
- h1 Quầy bán hàngQuầy
- h2 DH-2053

### Navigation out of this screen
- `home.html`
- `shift-close.html`
- `counter--qr.html`
- `counter--cart.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

<!-- v43:start -->
## v4.3 · data & decisions

Data An Nhiên: 2 products as big tiles with 'còn · đã giữ' (sell only on available stock; FEFO lot shown on the line); known-customer chips switch to the customer's price list; 'Thu tiền' = issue the cash-register invoice (Hilo). States: counter--debt (known customer, overdue → owner approves the debt; or pay now), counter--offline = device offline (pending tone, QR off, cash ok, invoice queued, never duplicated).
<!-- v43:end -->

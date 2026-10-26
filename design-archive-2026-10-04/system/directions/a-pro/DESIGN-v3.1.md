# OPC — DESIGN.md

> Source of truth for every OPC screen (web now, native later). Direction: **F "Biển Chỉ Dẫn"**
> (wayfinding), chosen 2026-10-02, with calming polish borrowed from A "Sổ Tay". Version 3.1.0.
> Raw values live in `tokens.css`; component styling lives in `components/components.css` (c-*) and
> `components/recipes.css` (r-*). Screens contain layout only. The living library is `components/catalog.html`.

## 1. Point of view (v3.0 "A-Pro · Sổ Cái")
OPC answers two questions first: **"what do I do first?"** and **"is this money real?"** It looks like a calm,
premium ledger: Mercury/Stripe-grade restraint (hairlines, tiered surfaces, soft elevation, refined type),
with OPC's own signature motifs used as accents:
- the **numbered lane** (lane 1 has the yellow numeral)
- the **payment ladder** "ĐANG Ở ĐÂY"
- **fill = certainty** (outline → blue hatched/dashed → solid green)
- the **"ĐÃ XÁC MINH" stamp**

Motion explains cause → effect. Older owners get large type and calm screens (Gọn mode); Phúc and the
accountant get power tools (Đầy đủ mode). Direction F's semantics are kept; its material (2px black borders,
square corners, heavy condensed type) was retired on 2026-10-02 as "looks like a 2D pixel game". A copy is in
`directions/f-final/`.

## 2. Tokens
### Colour roles
| Role | Token | Use / never use |
|---|---|---|
| Page canvas / surface / sunk | `--canvas` #f7f7f5 · `--surface` #fff · `--surface-sunk` | canvas behind, white cards, sunk for hover/selected |
| Ink / secondary / meta | `--ink` #15181b · `--ink-2` · `--ink-3` #4f565e (≥ 7:1) | meta never lighter than ink-3 |
| Lines | `--line` (hairline rows, card edges) · `--line-quiet` (controls) · `--line-strong` (grey outline) · `--line-ink` (focus, current marker) | black lines only for focus and the current marker |
| **Primary action** | `--panel` ink fill + white text | ONE per view (`c-btn--act`, `c-confirm`) |
| **Do-now marker** | `--act` #f5b800 | lane-1 numeral, "needs you" counts and edges, the counter icon. Not a button fill |
| Verified | `--ok` | solid fill / green check; never decoration |
| Pending | `--pend` + `--pend-hatch` | always dashed + hatched |
| Error | `--err` | errors only |
### Type
- **Be Vietnam Pro** (UI and body, 400/500/600): a Vietnamese-designed face with excellent diacritics.
- **Newsreader** (page, card and dialog titles, 600): gives the ledger voice.
- **IBM Plex Mono** (codes: DH-1043, 00000418, mã CQT, account numbers).
- Scale as before (14 floor, 16 body). Figures use weight 600, `tabular-nums` and -0.03em tracking on large sizes.
### Space, radius, elevation, motion
- **Radius:** 6 / 10 / 14 / pill.
- **Elevation:**
  - `--elev-1` for things you can act on (buttons, lanes, products, approval cards, inputs)
  - `--elev-2` on hover and for the current first item
  - `--elev-3` for overlays
  - Plain information cards have **no shadow**, only a hairline and a ledger rule under the head.
- **Motion:** `--dur-1..4` = 120/200/320/480ms, `--ease`, `--ease-spring`. Signature moments: ladder fill +
  check draw, the stamp, add-to-cart fly + bump, approve collapse + undo toast (pauses on hover/focus), live-update
  flash (`.is-updated` + `aria-live`), count-up of today's revenue. Tooltips use `[data-tip]` (350ms delay);
  glossary terms use `.c-term` (tap opens a sheet). `prefers-reduced-motion` turns all of it off.

## 3. Layout grammar
- **IA v2 (SCOPE-MVP.md):** sidebar = Hôm nay · Quầy · Bán · Tiền · Hàng · Sổ & thuế · Cần xử lý (+ Cài đặt, Trợ giúp); every group page starts with `c-subnav`. Phone tabs: Hôm nay · Quầy · Đơn · Tiền · Thêm (sheet with every destination).
- **Shell (`r-shell`):** a 252px sidebar (`c-nav`; 224px at ≤1180) beside a 68px top bar and the content.
  The top bar holds search, Trợ lý, notifications and the account.
  - **≤720px:** the sidebar is hidden. The top bar shows the household (`c-hh--bar`), search and the
    account, and a fixed `c-tabbar` sits at the bottom (Tổng quan · Quầy · Đơn hàng · Tiền · Thêm).
    Content gets 128px of bottom padding so the tab bar never covers it.
- **Breakpoints:**

| Width | What changes |
|---|---|
| 1440 / 1280 | full layout |
| 1180 | sidebar 224px; optional table columns hide; money signs lose their sub-line |
| 720 | phone layout |
| 390 | reference phone |

- **Home grid:** 1.6fr / 1fr.
  - Desktop order: Money hero (full width) → Cần xử lý | Thuế, Công nợ → Đơn gần đây → 7 ngày | Trợ lý.
  - Phone order: Money first (figure, pending line, truth bar + legend; the sign panel moves to the Tiền tab), then Cần xử lý. Page actions are hidden on phone: Quầy is in the tab bar, Tạo đơn / Ghi khoản chi sit under Thêm.
- **Counter focus mode (`r-counter`):** its own 72px header (menu, ← Tổng quan, title, connections,
  Đóng ca) with no sidebar.

  | Width | Layout |
  |---|---|
  | 1440 | products \| ticket 400 \| pay 420 |
  | 1280 | 380 / 400 |
  | 1024 | products \| one sticky 440 side column (ticket over pay), total pinned in the pay footer |
  | phone | product rows + `r-cart-bar` (Sửa giỏ → cart `c-sheet` with steppers; Thu tiền → payment `c-sheet`) |

- **Density contexts:** `data-density="touch"` gives 56px targets and is used on the counter and the
  payment sheet. `data-density="compact"` gives 40px rows and is reserved for accountant tables. Contexts
  change tokens, never components.

## 4. Components
See `components/catalog.html` for every variant and state, and `components/registry.json` for names,
WAI-ARIA APG patterns and shadcn mappings.

| Component | Anatomy · variants · states | Do / don't |
|---|---|---|
| `c-btn` | icon? + label + kbd? · `--act` `--quiet` `--danger` `--wrap` `--block` · hover, focus-visible (3px ink ring + yellow halo), active, disabled (dashed), `aria-busy` | Do: one `--act` per view. Do: lane actions end with →. Don't: grey-only disabled; say why |
| `c-confirm` | pic + label + reason (+ kbd) · `aria-disabled` = locked (hatched, lock) · `--done` (light green, a fact, not a call to act) | Use it to confirm money. While locked it must say what unlocks it ("Tự xác nhận khi ngân hàng báo") |
| `c-sign` | pictogram + word · `--wait` `--pend` `--ok` `--you` `--err` `--unk` | Every status. Never colour alone, never a dot alone |
| `c-moneyline` | 3 squares · `data-step` 1–3 | Next to amounts in lists and tables; `role="img"` + aria-label "Bước n/3: …" |
| `c-lane` | numeral · kicker · title · amount (+ hint) · detail · actions (+ more) · `--now` · `--done` (first-run steps) | Max 3 lanes; more goes to `c-later`. Say each fact once. Only `--now` is filled |
| `c-later` | `<details>` hairline list, grey numerals | Non-urgent work ("không gấp hôm nay"). No box |
| `c-msign` | pictogram block · word + sub · amount · go → (`__go--quiet` = navigation only) · `--ok` `--pend` `--cash` | Money by state. The yellow go appears only when it is the page's one action (Home); elsewhere use `__go--quiet` |
| `c-route` | 3 stations · `aria-current="step"` + "ĐANG Ở ĐÂY" · caption · passed stations are muted automatically | The payment ladder. The pending station is the largest. The caption states what happens next and the owner's delivery rule |
| `c-qr` | QR · meta · live status (`--pend`, `--ok`) · `--compact` | Status is `aria-live="polite"` |
| `c-table` | `__scroll` wrapper · `--stack` (rows become 2-line items ≤720) · cell roles main/end/wide/hide/opt · `__phone` / `__desk` parts · `__row--you` | Wide data scrolls inside the card, never the page |
| `c-prod` | badge (in cart) · name · price/unit · stock (`--low`) · add (phone) · `data-incart`, disabled | Tile on desktop, row with a 56px + on phone |
| `c-stepper` | − value + | Weight shows the unit ("0,5 kg") |
| `c-seg` | radiogroup | Payment method |
| `c-switch` | role=switch, label + sub · disabled | Optional invoice / print choices only |
| `c-sheet` | grip · head (k + title) · body · foot | Phone dialogs. The title is the amount |
| `c-banner` | pic · title · body · actions · `--err` (role=alert) `--pend` `--ok` | A section/page message. Only when the user can act on it or must know it; never for marketing. Error banners say since when and what still works |
| `c-empty` | pic · title · body (+ one action) · `--center` `--flush` | Every empty list/card says why it is empty and the one next step |
| `c-tabs` | tab + count · `aria-selected` · `--you` (dark count = needs the owner) | State views of a list (Cần xem · Chờ xác minh · …). Max one `--you` tab |
| `c-dialog` | panel · head (k + title + close) · body · foot (+ note) | Desktop modal; ≤720 becomes a full-screen sheet. See §5 Dialogs |
| `c-option` | radio · title · meta · why (✓ matches / ✗ misses) · amount · tag | Choose one candidate (gán tiền vào đơn). Show the reasons; never pre-commit |
| `c-field` | label · control (input + suffix) · hint · `--money` · `data-invalid` | Every typed value has a visible label. Money input is right-aligned Barlow |
| `c-change` | k · v · `--short` | Change due at the counter: the highest-contrast panel on the cash screen |
| `c-kv` | dt/dd · `__raw` for bank strings | Facts of a transaction or invoice |
| `c-steps` | label "Bước n/6 · task" + segment bar (done green · now ink) | Every onboarding screen. Never more than 6 steps |
| `c-otp` | 6 boxes, first has `autocomplete="one-time-code"` · `data-invalid` | Confirmation code; paste fills all boxes |
| `c-option--big` | radio · pictogram · title · meta · tag | "Choose how" screens (verify, add products, invoice) |
| `c-field[data-check]` | dashed blue control + hint "AI chưa chắc — …" | A value suggested by AI that the owner must check. Never block saving on it |
| `c-answer` | who ("Trợ lý OPC · trả lời tự động", hatched mark = not confirmed by a person) · question · text · feedback | Automatic answers. Not a chat bubble; always next to a way to reach a person |
| `c-coach` + `c-coach-anchor` | spotlight ring (yellow) + bubble (k "BÁN THỬ · 1/3", text, Bỏ qua / Tiếp) | Guided first sale only. Max 3 steps; always skippable |
| `c-camera` | dark viewfinder · card frame with yellow corners (`--face` oval) · hint · shutter | Frame around the vendor capture SDK. The one place a large dark block is allowed |
| `r-listbar` | search · date preset (`c-seg`: Hôm nay / 7 ngày / Tháng này / Tự chọn) · Lọc (`c-btn__count`) · sort menu → active `c-chips` | Every list. Phone: date preset gets its own row; Lọc opens the full-screen filter dialog (`r-filter`) |
| `c-chip` | key · value · × (aria-label "Bỏ lọc …") · `c-chips__clear` · `c-chips__result` | Every active filter is visible and removable; the result count + total sit on the same row |
| `c-menu` | groups · items (icon · label + sub · aside) · `aria-checked` for sort · `mark` for matched text | Sort menu (APG menu with menuitemradio) and search suggestions (APG combobox + listbox) |
| `c-cal` | head (prev · month · next) · weekday row · days (`--today`, `--start`, `--end`, `--range`, `--out`, disabled future) | "Tự chọn" date range inside a c-dialog |
| `c-pager` | info "Hiển thị 26–50 / 212" · prev · pages · gap · next | Only in `data-density="compact"` (accountant). Owners get "Xem thêm" (load more) |
| `c-skel` (+ `c-skel-note`) | line · title · figure · block, shimmer (off with reduced motion) | Loading = the real layout in grey blocks plus "Đang tải… · số liệu trước đó 10:43". Container `aria-busy="true"`. Never a full-page spinner |
| `c-timeline` | time · dot (ok / pend / err / you) · what · who | Order and invoice history, assisted-mode audit. Newest first |
| `c-doc` | head (title + số/ký hiệu) · parties · lines table · total · foot (mã CQT, tra cứu) | A preview of the legal document, shown paper-like and distinct from app cards |
| `c-subnav` | links (`aria-current="page"`) · count | Pages inside a group (two-level IA). Feature switches add or remove items here, never in the sidebar |
| `c-menulist` | group heading · rows (icon · label + sub · count) · `--you` | Phone "Thêm" sheet and settings index |
| `c-task` | source (Trợ lý = hatched mark · Ngân hàng · Hệ thống) · time · title + amount · evidence · "Sau khi duyệt" · actions | Every approval in Cần xử lý. Always show the evidence and the consequence before the button |
| `c-drawer` (`--wide`, `--docked`) | head (k + title + close) · body · foot | Assistant, help, notifications, quick view. Desktop: right panel; phone: full sheet. Esc closes, focus returns |
| `c-command` | input (combobox) · grouped listbox (Đơn · Hành động · Đi tới) · key hints | ⌘K or "/" from anywhere. One ranked list of places, actions and objects. `u-pro` hint for the owner |
| `c-toast` (`--err`) + `c-toasts` | pic · text · action (Hoàn tác / Thử lại) · time bar | Success fades after 10 s and pauses on hover/focus. **Errors never auto-dismiss.** Region is `aria-live` |
| `c-sync` (`--saving`, `--offline`) | dot + words | Always in the top bar: "Đã lưu · 10:45" / "Đang lưu…" / "Mất mạng — đã lưu trên máy" |
| `c-notice` (`--unread`, `--money`, `--warn`, `--err`) | pic · title · time · text | Notification centre rows; each links to the thing |
| `c-check` + `c-bulkbar` | 44px checkbox · bar: count · total · actions | Selecting rows shows the bar; one primary in it. Phone: bar sits above the tab bar |
| `c-crumbs` | links + current | Detail pages (Bán / Đơn hàng / DH-1040) |
| `c-spark`, `c-trend` (`--down`) | sparkline (area + line + end dot) · arrow chip | Trends beside key figures. A trend is neutral ink, never "verified" green |
| `c-prod__img` (`--sea`, `--warm`) | photo or category drawing | Products are recognised by picture first; a drawing stands in until the owner adds a photo |
| `c-receipt`, `c-msgcard` | slip: shop · lines · total · lookup code + QR · thanks / Zalo card: from · body · buttons | What the household's customer sees. Treat as brand surfaces |
| `c-sizepick`, `[data-textsize]`, `[data-view="simple"]`, `.u-pro` | — | Display preferences per user. Gọn hides `u-pro` power features; text size scales every font token |
| `c-stamp` (`--pend`, `--animate`) | rotated outlined label | "ĐÃ XÁC MINH" moment and the verified mark on receipts and invoices |
| `[data-tip]`, `.c-term` | tooltip after 350 ms · dotted term opens a glossary sheet on tap | Every icon-only button has a tooltip; every jargon word is a term |
| Others | `c-card`, `c-say`, `c-nav`, `c-hh`, `c-conn`, `c-search`, `c-icon-btn`, `c-avatar`, `c-filter`, `c-picker`, `c-list`, `c-truthbar`, `c-meter`, `c-daybars`, `c-tabbar`, `c-kbd`, `c-brand`, `c-ic` | See the catalog |

Not drawn yet (design with *Add a component* when the first screen needs them): toast, skeleton, select,
date picker, pagination.

## 5. Patterns
- **Money states (the core contract).** These map to backend states and must never be merged:
  1. Chờ khách chuyển — `--wait`, outline
  2. Đã nhận · chờ xác minh — `--pend`, hatched, dashed
  3. Đã xác minh — `--ok`, solid

  Invoices follow the same pattern: Chờ mã CQT is `--pend`, Có mã CQT is `--ok`. A QR payment is never
  shown as done before verification.
- **Delivery rule.** Goods may be handed over at step 2 only below the owner's limit (2.000.000 ₫ in the
  demo). The rule is stated in the `c-route__caption`.
- **Confirmations.**
  - Money confirmation is automatic when the bank reports. The manual button stays locked with a reason.
  - Destructive actions (Huỷ đơn) use `c-btn--danger`, sit apart from Lưu tạm and need a second step
    (dialog not drawn yet).
- **Lists.** Use hairline rows (`c-list`, `c-later`) unless a row is an action with its own button (`c-lane`).
- **Search, filter, pagination.**
  - **Search:** matches code, customer, phone and MST, with suggestions after 2 characters.
  - **No results:** show `c-empty` that repeats the query and offers "Xoá lọc" / "Tìm trong tất cả thời gian".
  - **Date preset:** the default is "Hôm nay" for owners and "Tháng này" for accountants. A custom range opens `c-cal`.
  - **Filters and sort:** filters live in one panel (dialog, full-screen on phone). Active filters always show as
    chips with the result count and total. Sorting uses a menu; the default is "Mới nhất", or "Cần xem trước" on
    the Cần xem tab.
  - **Paging:** owners load more 12 at a time ("Xem thêm 11 đơn"). Accountant tables page 25 per page with `c-pager`.
  - **URL state:** the URL keeps search, filters, sort and page, so back/forward and sharing work.
- **Owner sentence.** Every key figure gets one plain sentence above it (`c-say`) that says what it means
  and what to do.
- **Connections** (`c-conn`) are always visible where money or invoices appear: bank (via Casso), Hilo,
  tax portal. Off = hollow square, error = red.
- **Keyboard (counter):** / search · + − quantity · F9 take payment · Esc cancel.
- **Dialogs (`c-dialog`).**
  - Opened from a button; focus moves to the dialog title. Focus is trapped while open and returns to the
    trigger on close. Esc and the ✕ close without changes.
  - The primary action names its result ("Gán vào DH-1038"), never "OK". Destructive actions use
    `c-btn--danger` and say what is lost.
  - After a money action, show a `c-banner--ok` with "Hoàn tác" for 10 seconds.
- **Empty / error / offline.**
  - Empty uses `c-empty` with one next step.
  - Bank/Casso offline: a `c-banner--err` at the top of the affected area, saying since when, what still works
    (cash, công nợ) and that OPC retries. QR choices show as unavailable (`c-seg__opt[aria-disabled]`).
    Amounts show "chưa cập nhật từ 10:30", never a silent stale number.
  - First run: Home lanes become the setup steps (`c-lane--done` for finished ones).
- **Help and support (v3.1).**
  - "?" opens the help drawer for the current screen, with 3 short steps, a 30-second video, "Xem lại hướng dẫn"
    and people. **Gọi lại cho tôi** books a call (15 phút · chiều nay · mai); Zalo and Gọi chị Lan are also there.
  - The assistant drawer knows the screen. It suggests questions, answers with sources, and sends any action it
    proposes to Cần xử lý. It never acts by itself.
- **Display preferences.**
  - Text size Vừa / Lớn / Rất lớn and the Gọn / Đầy đủ mode are stored per user.
  - Default: owner Gọn + Lớn, manager and accountant Đầy đủ + Vừa.
- **Power tools (Đầy đủ only):**
  - ⌘K palette.
  - Quick view drawer from any list row (↑↓ moves between rows).
  - Selection + bulk bar (Gửi nhắc nợ qua Zalo, In phiếu, Xuất Excel).
  - Saved views as chips.
  - Breadcrumbs, and "?" for keyboard shortcuts.
- **Feedback.** Every save shows `c-sync` and every action a `c-toast`. Optimistic updates roll back with an error
  toast. Live changes flash once (`.is-updated`) and are announced via `aria-live`.
- **Trust.**
  - Sensitive actions (inviting users, changing the bank, delegating) need an OTP sent over Zalo.
  - The promise "OPC không bao giờ tự chuyển tiền hay nộp thuế thay chị" appears wherever money or tax is
    authorised.
- **Loading:** skeleton in the real layout (`c-skel`). Keep the last known figures visible and greyed where available (money must never flash 0 ₫).
- **Onboarding (r-onboard).**
  - One task per screen. The title states the task in plain words. At most 2 inputs per screen.
  - Every screen has the primary at the bottom, "Bước n/6", "?" Hỏi (help sheet), and a way to reach a
    person: Gọi chị Lan / Nhắn Zalo / Nhờ người thân làm giúp.
  - Non-blocking steps offer "Để sau". "Đã lưu" is shown after each step.
  - Explain why before asking for anything sensitive (CCCD, bank). No jargon: "mã xác nhận", not "OTP";
    "xác minh chủ hộ", not "eKYC".
  - AI reads and suggests, the owner reviews, and uncertain values use `c-field[data-check]`. AI never saves on
    its own.
  - Assisted mode runs on the staff laptop, with the staff identity always visible and every action logged.

## 6. Content rules
- **Language:** Vietnamese with full diacritics. Write "Hoá đơn" (the programme's spelling). Bank strings
  are shown as received (NHA HANG BIEN DONG).
- **Formats:**

  | What | Example |
  |---|---|
  | Money | `1.020.000 ₫` (dot thousands, space, ₫ after) |
  | Weight | `0,5 kg` (decimal comma) |
  | Date | Thứ Sáu, 02/10/2026 |
  | Time | 10:42 |
  | Order code | DH-1043 (DH1043 in transfer content) |

- **Voice:** an assistant who knows the shop. Short, concrete, says the next step ("đối chiếu trước khi
  giao hàng lớn"). No exclamation marks, no blame.
- **Verbs on buttons:** Đối chiếu, Gán vào đơn, Xác nhận, Thu tiền, Kiểm tra, Gia hạn, Tạo phiếu nhập.

## 7. Accessibility
- **Contrast:** AA everywhere (text ≥ 4.5:1; meta `--ink-3` ≈ 7:1).
- **Targets:** at least 44px by default and 56px in the touch context. Inline text links are exempt (WCAG 2.5.8).
- **Focus:** `:focus-visible` shows a 3px ink outline plus a yellow halo.
- **Status semantics:** status is always shown with colour + pictogram + word. Live payment status uses
  `aria-live="polite"`. Decorative icons are `aria-hidden`.
- **Machine checks:** probe at 1440, 1024, 390 (mobile) and 1280 (stress); axe reports 0 violations.
  Retest with `--text-scale 1.3` before handoff.
- **Reduced motion** is respected.

## 8. Never do
- Yellow as a button fill or decoration; it marks "do now". Green for anything except "verified/done".
- Plain blue fill for pending (it must be hatched + dashed), or a pending payment shown as "done".
- Black 2px borders, square corners, heavy condensed type (the retired F material). Shadows on plain information cards.
- Large dark blocks, except the primary button, `c-change` and the camera viewfinder.
- Text under 14px, light grey text, or status shown by a coloured dot alone.
- More than one yellow action in a view (lane-1 numeral and `__row--you` edges are markers, not actions; the page-head "Mở quầy" is plain because Quầy is always in the nav); more than 3 lanes; repeating a fact inside a lane.
- Shadows, gradients (except the pending hatch), glassmorphism, pill buttons, emoji, seafood/wave clip-art,
  green+gold "agri" palettes, Tết clichés.
- Restyling a `c-*` class inside a screen. Use a variant, a context, a recipe, or a documented snowflake.

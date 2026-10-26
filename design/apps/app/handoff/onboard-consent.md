# Handoff — Mở hộ v7 (6 bước)

- Steps (onboard_lib.STEPS): 1 Số điện thoại + đồng ý dữ liệu · 2 Hộ kinh doanh · 3 Cách bán + Việc OPC làm · 4 Thuế và tài khoản · 5 Hoá đơn · 6 Số đầu kỳ → giao dịch đầu tiên.
- Consent: the mandatory box only; "cho Agent đọc tin nhắn" is optional and unchecked by default (Luật 91/2025).
- Hộ chưa có giấy đăng ký: `onboard-household--unregistered` — selling and invoices stay locked; products and prices can be prepared.
- Step 4 only asks whether VNeID level 2 and eTax exist; OPC never stores those passwords. Revenue before OPC + filing period are a suggestion from a versioned rule set "chờ kế toán xác nhận".
- Step 5 is the only mandatory connection (e-invoice provider, or the free state e-invoice if eligible). Waiting for the tax office's acceptance never blocks the next step.
- Step 6 confirms counted opening stock, cash, bank and debts once (or "Bắt đầu từ 0"); later changes go through an adjustment with a reason.
- Identity (onboard-verify*) and bank connection (onboard-bank*) are optional gates from Sẵn sàng (no step bar).

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/onboard-consent.html` · Đăng ký · Đồng ý dữ liệu (1/6)
- Page pattern: **wizard**
- Note: Đồng ý rõ ràng theo Luật 91/2025; quyền xuất/xoá.
- States: none drawn
- Component spec: `bridge/opc-shadcn/onboard-consent.md`

### Regions per size
- **1440**: header 0,0 1440×73 · main 216,113 560×631 · Các bước đăng ký 824,113 400×414 · footer 216,736 560×164
- **1280**: header 0,0 1280×73 · main 136,113 560×631 · Các bước đăng ký 744,113 400×414 · footer 136,636 560×164
- **1024**: header 0,0 1024×73 · main 232,73 560×691 · Các bước đăng ký 232,764 560×129 · footer 0,604 1024×164
- **390**: header 0,0 390×73 · main 0,73 390×815 · footer 0,627 390×217

### Responsive behaviour (components that appear/disappear)
- `c-stepmap`: 1440 shown · 1280 shown · 1024 shown · 390 hidden

### Components used (at 1440)
- `c-btn` ×1 · --act --block
- `c-ic` ×7
- `c-icon-btn` ×1 · --outline
- `c-option` ×2 · --big --on
- `c-options` ×1
- `c-say` ×1
- `c-stepmap` ×1
- `c-steps` ×1
- `r-gate` ×1
- `r-model` ×1
- `r-onboard` ×1

### Outline
- h1 OPC dùng dữ liệu của hộ thế nào

### Navigation out of this screen
- `onboard-otp.html`
- `onboard-help.html`
- `onboard-household.html`
- `help.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

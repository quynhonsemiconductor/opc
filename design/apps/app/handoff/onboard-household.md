# Handoff — onboard-household

Part of the onboarding flow: see `onboarding.md`. Content: BRIEF §11. Component spec: `bridge/opc-shadcn/onboard-household.md`.

<!-- handoff.mjs:start — generated 2026-10-10, do not edit inside this block -->
## Generated facts
- Screen: `../screens/onboard-household.html` · Đăng ký · Hộ kinh doanh (2/6) · status v4-calm
- Page pattern: **wizard**
- Note: Chụp giấy đăng ký hoặc nhập mã; không giả định tra cổng thuế chắc chắn.
- States: `onboard-household--notfound.html`, `onboard-household--read.html`, `onboard-household--unregistered.html`
- Component spec: `bridge/opc-shadcn/onboard-household.md`

### Regions per size
- **1440**: header 0,0 1440×73 · main 216,225 560×360 · Các bước đăng ký 824,225 400×414 · footer 216,584 560×164
- **1280**: header 0,0 1280×73 · main 136,175 560×360 · Các bước đăng ký 744,175 400×414 · footer 136,534 560×164
- **1024**: header 0,0 1024×73 · main 232,73 560×420 · Các bước đăng ký 232,493 560×150 · footer 0,604 1024×164
- **390**: header 0,0 390×73 · main 0,73 390×447 · footer 0,520 390×145

### Responsive behaviour (components that appear/disappear)
- `c-stepmap`: 1440 shown · 1280 shown · 1024 shown · 390 hidden

### Components used (at 1440)
- `c-btn` ×1 · --act --block
- `c-ic` ×3
- `c-icon-btn` ×1 · --outline
- `c-option` ×2 · --big
- `c-options` ×1
- `c-say` ×1
- `c-stepmap` ×1
- `c-steps` ×1
- `r-onboard` ×1

### Outline
- h1 Hộ của chị đã có giấy đăng ký kinh doanh chưa?

### Navigation out of this screen
- `onboard-consent.html`
- `onboard-help.html`
- `onboard-household--read.html`
- `onboard-household--notfound.html`

### Tokens referenced by the layout
none
<!-- handoff.mjs:end -->

<!-- v43:start -->
## v4.3 · data & decisions

Tax-code lookup returns the registered household; owner confirms or edits the display name and main goods; 'Không phải hộ của tôi' → retry.
<!-- v43:end -->

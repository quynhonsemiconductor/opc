<!-- uiux-studio · OPC web — paste into the FE repo's AGENTS.md (Kiro, Codex, Cursor, Copilot) or CLAUDE.md. -->
## Implementing UI from the OPC design (v5.1.1 "Modern · Calm")

**Source of truth**: `opc/design/` (uiux-studio project). Read before any UI work, in this order:
1. `system/DESIGN.md` — rules, tokens, layout grammar (§3), components (§4), patterns, content, a11y, "never do".
2. `apps/app/handoff/<screen>.md` — layout per size, data, states, behaviour.
3. `apps/app/handoff/bridge/opc-shadcn/<screen>.md` — which shadcn component + props for every element.
4. `apps/app/handoff/<screen>.inventory.json` — component tree with boxes.

`apps/app/screens/*.html` are a **visual reference, not code to copy**. `handoff/annotated/*.html` show component
boundaries (`data-component`, `data-variant`, `data-part`, `data-state`). Click-through: `apps/app/prototype.html`
(66 screens/states, 9 flows). Living library: `system/components/catalog.html`.

**Stack** (ADR 0007): React 19 + Vite SPA · TanStack Router/Query · Tailwind v4 · shadcn/ui (Radix). Map: `system/maps/opc-shadcn.json`.
Theme: import `system/tokens/tailwind.theme.css` (OPC utilities, generated from `system/tokens.css`) and
`apps/app/handoff/bridge/opc-shadcn/theme.css` (shadcn variables: `--primary` = sea #0b6b93, `--ring` = sea) — never hand-copy values.
Native later: `system/tokens/*.tokens.json` (W3C DTCG, per context) feed Style Dictionary / SwiftUI / Compose.

### Rules
1. Build from shadcn as mapped in the bridge spec. Anything `custom` in `system/components/registry.json` becomes
   ONE shared component in `src/components/opc/` — never inline per page. The custom set (21):
   - Money truth: `MoneyTruthBar` (c-split + `__you`/`__err`), `c-bars`, `c-paysteps`, `c-waitbar`, `c-arrived`,
     `c-change`, `r-listhead`.
   - Lists/queues: `c-todo` (+ `--wait`), `c-orders`, `c-oline`, `c-debts`, `c-timeline__item--ai`.
   - Layout: `r-settings`, `r-detail__head--calm`.
   - Onboarding: `c-stepmap`, `r-onboard__aside`, `r-onboard__proof`, `r-onboard__flow`.
   Build `MoneyTruthBar` first — Home, Tiền, Đơn hàng, Hoá đơn, Counter and onboarding all reuse it.
2. No raw values in feature code. Colour roles are strict (DESIGN.md §2): `--act` (sea) = primary action / current
   place / today only; `--truth-ok` / `--truth-pend` (+ hatch, dashed) / `--truth-cash` = money state only; red =
   errors only. Status is never colour alone (always a label or icon).
3. Contexts are providers, not page CSS: `data-density="touch"` (counter, onboarding, 56px targets),
   `data-density="compact"` (accountant tables), `data-textsize="lg|xl"` (user setting — every layout must still fit).
4. Behaviour follows the WAI-ARIA APG pattern named in the registry. Dialogs: Radix Dialog traps focus — the mock-ups
   mark the page behind `inert` only to simulate this. Switches: `role="switch"`; "Bắt buộc" = disabled, no switch
   shown; "Sắp có" = badge only, no switch. Scrollable tables are focusable regions with a label.
5. One primary per view; secondary = outline; quiet = no border (`c-btn--quiet`); destructive next to a primary =
   ghost red. On phone, button labels wrap — never widen the page.
6. Say each figure once (a figure shown as the hero is not repeated in a legend/tile on the same view).
7. Implement every state in the handoff (empty, loading, error, offline, disabled, long content, text size lg/xl).
8. Demo content through a fixture route (`/__design/<screen>`) so the visual check compares design, not data.

### Onboarding layout (decision 2026-10-04)
Web is the product now; native iOS/Android get their own native-first onboarding later. So web onboarding is
designed laptop-first: **≥1180 two columns** (form ≤560 | panel ≤400: step map, or the sample proof card tagged
"Ví dụ" on welcome/done); **<1180** one column with the panel as a compact strip. Forward action sticky at all sizes.

### Definition of done for a screen (dev server up)
```
node ~/.kiro/skills/uiux-studio/scripts/verify.mjs <abs>/opc/design/apps/app <screen> http://localhost:5173/__design/<screen> --qa
```
PASS at 1440/1280/1024/390, no component over its drift threshold, no serious/critical a11y violations. An
intentional difference is recorded in the handoff ("deviation: … because …") with design sign-off; otherwise fix
the code, not the threshold.

### Known open items (design side)
- settings-features 7.8 and onboard-phone 7.8 are just under the 8.0 bar; all other evaluated screens ≥ 8.0.
- Not yet designed: native apps, dark theme.
- Restructured screens carry a "v4.1 (current)" block at the top of their handoff; it overrides older layout text
  further down (data/API sections stay valid). Generator: `tools/v4/handoff_v41.py`.
- Design generators (re-run in this order after editing screens): `pages_*.py` → `onboard_aside.py` → `inert.py`
  → `handoff.mjs` / `inventory.mjs --annotate` / `bridge.mjs` / `proto.mjs` / `digest.mjs`.

## Navigation (v4.4)
- One `NAV` config (sections → children → count source) drives the desktop rail, the phone "Thêm" sheet and the phone
  sub-nav. Source of truth for the mockups: `tools/v4/navtree.py` (SECTIONS, FOOT, ROLES).
- Filter by business model (feature flags from Hộ & mô hình / Tính năng): Chế biến ← tự chế biến; Giao hàng, Khách hàng ←
  khách sỉ; Nhập hàng, Nhà cung cấp ← mua về bán. Filter by role: Thu ngân, Kế toán (see ROLES); deliverer has no shell.
- The section containing the current route is open; others collapsed (Collapsible, 44px trigger). Counts come from the
  child that owns the work; a collapsed parent shows the sum. Hide the in-page SectionNav ≥721px.


## Connections data model (v4.8.0)
Three layers, never collapsed into one table:
1. **ProviderAccount** `(household, provider, display_name, credential, status, expires_at)` — connected once by the owner (Zalo OA "Đặc sản An Nhiên", MB qua Casso, Hilo, X Invoice, Cas ID). Several accounts of one provider allowed (named).
2. **JobGrant** `(account, job/category, scopes, enabled, consented_by, consented_at, expires_at)` — what OPC may do with the account (Zalo OA: nhận đơn · trả lời khách · gửi ZNS). Scope is stored per (account, job), never only per account, so one job cannot inherit another's scope. Adding a job asks only for the new scope (incremental consent). Prerequisites per job (ZNS: approved template, balance).
3. **Category** (17) — what flows request. A flow asks for a category; the router returns the enabled JobGrants (default + fallback). No enabled grant → the manual path.
UI: `Kết nối` (top-level) → Đã nối (accounts + jobs as chips + gaps) · Việc OPC làm (11 features, 3 tiers) · Nhật ký; "Thêm cách nối" (ways grouped by feature) opens from Việc OPC làm. Open questions: whether Casso products share one login; whether Zalo grants messaging and ZNS in one authorisation.

### Catalog and scale (v4.9.0)
The provider list is data — see `system/connector-catalog.md` (entry schema, status values, category policies: fan-in / accumulate / choose-per-action / rules).
Delivery MVP: default carrier + assistant suggests + the person at hand-over chooses (quote preview); automatic rules later. Screens: `connections--add` (directory v2),
`connections--info` (provider page), `connections--request`, `connections--delivery` (category hub, template for every multi-provider category), `connections--many` (Đã nối with 14 accounts).

## v5.0.0 · Credentials and provider registry (FE/BE notes)
- `GET /providers` returns the catalog rows (see system/connector-catalog.md, `mode`, `status`, `visible`); the directory, pills and platform registry only render this list. Adding a provider = adding a row; hiding = `visible:false`.
- `POST /accounts {providerId, fields}` for `key` mode: store in a secrets vault (KMS-encrypted), return `{id, masked:{apiKey:"••••9f3c"}}`. Never return the secret again. `POST /accounts/:id/rotate` tests the new key first and swaps atomically. `DELETE /accounts/:id` also deletes the secret.
- `casso` mode: no secret stored; keep `grantId` and listen to the `GRANT` webhook. Casso's webhook is unsigned — verify money before writing the ledger.
- Webhook endpoint per household per provider (`/w/{household}/{provider}`) with a per-account secret; payOS-style signed webhooks are verified with the checksum key.
- Platform console is a separate role (QNSC admin): sees counts only, never households' data; hide/remove needs a reason and writes the audit log.

## v5.1.0 · Features first
- `GET /features` returns the 11 features for the household: `{id, tier, when, why, recommendedWay, choices[], manualPath, state, way}`; tier is computed from the business model (rules in capabilities.py). Providers are listed only as `choices`.
- `POST /features/:id/way {providerId | "assisted"}` stores the household's choice before any credential; the connect flow then runs by the provider's custody mode.
- A `need` feature without a way locks only its dependent flows (feature flags `canTakeTransfer`, `canAcceptWholesale`, `canIssueCodedInvoice`); the response to a locked action names the feature to connect.
- Onboarding is 5 steps (`STEPS` in onboard_lib.py / onboard43.py): phone, hộ (photo or MST/CCCD + doanh thu lũy kế), cách bán + việc OPC làm, xác minh chủ hộ, hàng đầu tiên. Nothing of the household is connected; bank/invoice/e-signature/purchasing/production/tax are gates from `GET /readiness` (33 items by chain, see readiness_model.py).

# tools/v4 — screen generators (design side only)

Python 3, no dependencies. They rewrite `apps/app/screens/*.html` from pristine inputs, so re-runs are idempotent.
**Run `sh run_all.sh`** (order matters; `inert.py` is always last). After it: probe / a11y / `budget.mjs --all` at 390, 1024, 1440, then
`handoff.mjs` → `handoff_v42.py` → `inventory.mjs --annotate` → `bridge.mjs` → `proto.mjs` → `digest.mjs` → `status.mjs --mark` (see `apps/app/IMPLEMENT.md`).

## Order in run_all.sh
1. Inputs → shells: `home43`, `src43`, `states`, `home_states`, `orders43`, `settings43` (read `src/`, `src_v31/`, `src_v40/`, `src_v43/` snapshots — do not delete them).
2. Pages: `pages_money/orders/queue/settings/books43`, then the v4.2+ pages (`pages_control … pages_partners`). v7: `pages_buy7` (Mua hàng: list, purchase record + receive/received/pay, new, return, expense) replaced `pages_purchase`; `pages_sell7` (Bán hàng: order record states, Bán nhanh) replaced `pages_order360`, `pages_shift` and `states.py` (counter); shared helpers `erp_lib.py`; `pages_money7` (Tiền: split, overpay, duplicate, cash count, customer statement); `pages_books7` (Kê khai: quarter overview, eTax guide, filing progress, evidence — no computed tax) replaced `pages_tax`; `pages_production` removed (no chế biến in pilot).
3. Kết nối: `pages_connect` (flow screens) → `pages_connect2` (Đã nối, account, use, X Invoice detail) → `pages_connect3` (GHTK info) → `pages_connect3b` (Giao hàng, many accounts)
   → `pages_connect4` (Thêm cách nối + request, casso hand-off, keys, guides, manage, platform console) → `pages_connect5` (Việc OPC làm + feature page). A later script overwrites nothing from an earlier one.
4. Onboarding (6 steps): `onboard43` → `onboard_features` (step 3 plan) → `onboard_flow` (steps 1, 2, 4, 5, done, bank gate) → `firstsale` (built on quick-sale--qr) → `onboard_aside`. Shared helpers: `onboard_lib.py`. Sẵn sàng: `pages_readiness.py` from `readiness_model.py`.
5. Last: `relink.py` (counter → quick-sale, shift-close → money, labels; BRAND: no provider names on household screens) → `status7.py` (one status vocabulary, `system/maps/status.json`) → `nav7.py` → … → `inert.py` → `tracks7.py` (order lists: Giao · Hoá đơn · Tiền) → `facts7.py` → `links7.py` (no dead links) → `offline7.py` → `role7.py` → `nav7.py` again (role rails) · `facts7.py` (demo numbers = design/_research/audit-e2e-v752.md; runs last because earlier passes change markup) (rail + phone sub-nav + tab bar from `navtree.py` on every household screen) → `brand.py` (OPC voice in shared chrome) → `quiet_icons.py` → `inert.py`.

## Data
- `providers.py` — every provider (mode, status, source). `capabilities.py` — the 11 features (tier, choices, demo state). Screens render from these; removing a provider = removing a row.
- `navtree.py` — the ERP menu (SECTIONS, FOOT, PREFIX page→section, ALIAS); applied by `nav7.py`. `connect_lib.py` — shared helpers for the Kết nối screens.

## Other
- `catalog_v4.py`, `catalog_v41.py`, `catalog_v42.py`, `catalog_v42b.py` — catalog sections (registry + `system/components/catalog.html`); new recipes are not in the catalog yet.
- `handoff_v42.py` — hand-written handoff parts (DOCS) + state pointers (STATES); run after `handoff.mjs`.
- One-off scripts (lanes_to_todo, retire_catalog, css_fold, css_prune, handoff_v41, proposal_v45) were archived on 2026-10-07 to `opc/_archive/design-cleanup-2026-10-07/tools-v4/`.

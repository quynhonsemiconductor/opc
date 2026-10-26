# Design changelog

Every change to tokens, components or screens gets an entry. Version: MAJOR = direction/structure change,
MINOR = new component or screen, PATCH = adjustment to an existing one.

## 0.1.0 — 2026-10-01
- Project initialised.

## 0.2.0 — 2026-10-02 — direction chosen
- GATE: direction **F Biển Chỉ Dẫn** chosen (with calming polish borrowed from A Sổ Tay). Rejected: A (8.0, runner-up), D, B, E, C. Exploration kept in `directions/`.
- Next: lock (DESIGN.md, components, catalog, layout-only screens) → 1.0.0.

## 1.0.0 — 2026-10-02 — system locked (direction F)
- tokens.css: F tokens in 3 tiers; contexts `data-density="touch|compact"`; layout tokens; native placeholders.
- components.css: 37 components (c-btn, c-confirm, c-sign, c-moneyline, c-lane, c-later, c-list, c-msign, c-route, c-qr, c-prod, c-stepper, c-table, c-seg, c-switch, c-sheet, c-tabbar, …); recipes.css: 10 recipes (r-shell, r-money-hero, r-counter, r-ticket, r-pay, r-invoice, r-cart-bar, …).
- Calming polish (from A): only lane 1 has a filled numeral; lanes 2–3 ink on white; non-urgent work is a hairline list (c-later); counts are outlined, not dark.
- Fixes from the finalist evaluator: lane hints wrap (2 lines) on phone; household switcher "Cô Hai · Nhơn Lý"; lane 1 says each fact once; delivery rule merged into the ladder caption (c-route__caption); phone cart bar separated (3px rule + canvas gap).
- registry.json with APG patterns + shadcn mapping; catalog.html; DESIGN.md; assets/qr-demo.svg, assets/icons.svg.

## 1.1.0 — 2026-10-02 — components for states and list screens
- New: c-banner (--err/--pend/--ok), c-empty, c-tabs, c-dialog (desktop modal → phone full-screen), c-options/c-option, c-field (--money, invalid, disabled), c-change (--short), c-kv; c-lane--done; c-seg__opt disabled; c-table__row--you. Token: --scrim.
- DESIGN.md §4 rows + §5 Dialogs, Empty/error/offline. BRIEF §10 feature content.

## 1.2.0 — 2026-10-02 — round-1 evaluator fixes (MINOR: new variants/parts)
- c-msign__go--quiet (navigation arrow; yellow stays the one action); c-confirm--done is now light green (calm); c-route mutes passed stations; c-tabs fade on phone; c-table__phone / __desk parts; c-table__scroll contains sr-only text.
- Content: invoice for the DH-1038 assignment is 00000423 (00000422 = DH-1043); offline scenario starts 10:45 with data to 10:44.

## 1.3.0 — 2026-10-02 — onboarding & guidance
- New: c-steps, c-otp, c-option--big (+ __pic), c-field[data-check] (AI chưa chắc), c-answer, c-coach + c-coach-anchor (spotlight), c-camera (--face); recipes r-onboard, r-help. c-field input now meets the target size. DESIGN.md §4 rows + §5 Onboarding. BRIEF §11.
- apps/app/screens/_onboard-template.html: shared skeleton (sprite extended: phone, camera, id, bank, mic, photo, file, help, shield, family).

## 1.4.0 — 2026-10-02 — list tools + onboarding fixes
- New: c-chips/c-chip, c-menu (+ anchor), c-cal, c-pager, c-btn__count, c-say--icon; recipes r-listbar, r-filter. c-seg options shrink (minmax 0). Compact density keeps 44px targets. Coach ring is ink (yellow stays for the bubble action). DESIGN.md §4 rows + §5 Search, filter, pagination. BRIEF §12.

## 1.5.0 — 2026-10-02 — loading, history, documents
- New: c-skel (+ c-skel-note), c-timeline, c-doc, c-option--action, c-table total row; recipe r-detail. BRIEF §13.

## 2.0.0 — 2026-10-02 — information architecture v2 (MAJOR: navigation structure)
- SCOPE-MVP.md: the MVP is wide but thin (CEO list + gaps), with feature switches and defaults assumed.
- Two-level navigation: the sidebar has 6 groups + Quầy; `c-subnav` on group pages; phone tabs are Hôm nay · Quầy · Đơn · Tiền · Thêm. All screens migrated by script; the diff shows changes only in the navigation.
- New: c-subnav, c-menulist, c-task. BRIEF §14.

## 2.1.0 — 2026-10-02 — IA evaluation fixes (7.1)
- Phone tabs Hôm nay (Cần xử lý count) · Quầy · Bán · Tiền · Thêm. The Thêm sheet lists only what has no tab.
- Renames: Hàng → Hàng hoá, đối soát → đối chiếu. Nhật ký moved to Cài đặt and gained approval entries. Cần xử lý has no sub-nav.
- Shorter settings sub-nav labels. Date preset moves into the filter dialog on phone. Home: "Đóng ca" sits next to the open shift.
- SCOPE-MVP §2 rewritten (entry points: returns, price history, assistant, notifications, avatar menu, accountant switcher; booking, farm purchase and traceability screens deferred).

## 2.1.1 — 2026-10-02 — IA round 3 polish (8.3 PASS)
- c-menulist rows are taller with spaced sub-lines. Thêm sub-lines name "Lịch sử giá" and "Thuế & tờ khai". Nhật ký gains filters by kind of change. "Sắp có" wording. SCOPE: a quiet entry row when a switch is OFF.

## 3.0.0 — 2026-10-02 — restyle to A-Pro "Sổ Cái" (MAJOR: material)
- tokens.css: Be Vietnam Pro + Newsreader + IBM Plex Mono; recalibrated neutrals; radius 6/10/14/pill; strokes 1px; elevation and motion tokens.
- components.css / recipes.css: A-Pro material layer (merged from directions/a-pro/skin.css; the 0% diff against the preview is verified). Primary action = ink; yellow = do-now marker. The tooltip `[data-tip]` and glossary `.c-term` are added. c-field shrinks in narrow columns.
- The F material is archived in directions/f-final/. All 53 screens are restyled with no screen edits.

## 3.1.0 — 2026-10-02 — Pro layer (support, productivity, trust)
- New: c-drawer, c-command, c-toast(s), c-sync, c-notice(s), c-check, c-bulkbar, c-crumbs, c-spark, c-trend, c-prod__img, c-receipt, c-msgcard, c-sizepick, c-search__mic; text-size contexts `[data-textsize]`; Gọn mode `[data-view="simple"] .u-pro`; motion utilities (u-bump, c-stamp--animate, ladder transitions).
- All shell screens: sync chip, mic + ⌘K in search, tooltips on icon buttons; the bell and Trợ lý link to their drawers. Counter: category thumbnails. Fix: the counter category row no longer collapses.
- 3.1.1: evaluator fixes (7.2 → 7.8): Gọn mode hides power tools (`u-pro` on ⌘K, Excel export, bulk select) and can be locked by the owner; the assistant answer offers "Hỏi người thật"; new state orders--bulk--preview (recipients, message, already-paid warning, undo); the OTP confirm stays disabled until all 6 digits are in, and shows resend and expiry; the focus halo is blue-grey, never yellow.

## 4.0.0 — 2026-10-03 — direction "Modern · Calm" (MAJOR: direction + structure)
- GATE: the user found A-Pro "still old, not modern/professional" (refs: Apple iOS 26/macOS, Stripe/Ramp/Attio,
  Revolut/Cake/MoMo). Explored in `directions/modern/`: a reskin "Ocean" (bank-blue gradient hero) and an
  "Ink & Lime" variant, then a structural redesign of Home + Counter in two finishes. Evaluator: Ocean Home 6.8 →
  7.2 (fail), Counter 7.8 → 8.0; **Calm** Home 8.0 + Counter 8.0 (pass) and won the pairwise comparison. User chose Calm.
- tokens.css rewritten: sans only (Be Vietnam Pro; Newsreader and IBM Plex Mono removed), deep-sea `--act`
  #0b6b93 (primary / current / today), amber pending, new `--truth-*`, `--canvas-quiet`, `--act-soft/-ring/-ink`,
  `--pend-ink`, `--err-ink`, radius 8/12/16/20. v3.1 tokens archived in `directions/a-pro/tokens-v3.1-system.css`.
- Icons: every sprite replaced by Lucide (ISC), same ids; `assets/icons/lucide-map.json` + `lucide-extra.json`.
- components.css / recipes.css: v4 layer appended (tokens only, no hex). New components: c-stat, c-bars, c-split,
  c-health, c-off, c-count, c-link, c-sub, c-figure, c-todo, c-orders, c-debts, c-tiles/c-tile, c-oline, c-oempty,
  c-qrcard, c-paysteps, c-waitbar, c-arrived, c-note, c-cashpad, c-quick, c-btn--xl, c-skel--bar/--row/--w1–5;
  new variants: c-seg disabled option, c-health--err, c-change--none, c-toast--pend/--ok + undo, c-sign--err ink.
  Recipes: r-home, r-pos (--sheet), r-order (--pay), r-cartbar. Retired (still styled for old screens): c-lane,
  c-msign, c-route, c-prod, c-truthbar, c-daybars, c-spark, c-stamp, r-money-hero, r-counter, r-ticket, r-pay.
- Screens: Home + 8 states and Counter + 10 states rebuilt (generated by `directions/modern/redesign/states.py`
  and `home_states.py`); new `counter--qr`, `counter--undo`. Money-arrived moment, add-item pop, undo toast.
  The other 44 screens take the v4 tokens/components without edits (structure unchanged — next round).
- Fixes found while locking: error-pill and offline contrast (`--err-ink`), household name and chart labels wrap
  under large text, chart never widens the page, orders fall back to two lines with large text at ≤1180;
  status warnings cleared (orders--loading skeleton widths → classes, raw checkboxes/command input → system classes).
- Catalog v4 sections (and its empty icon sprite fixed); registry +29 entries; opc-shadcn map +30 entries,
  theme vars for truth/act/ink tokens; inventories + bridge specs regenerated for all 66 screens.
- Verified: probe 0 issues on all 66 screens at 1440 and 390 (Home/Counter also 1024 + stress); axe 0
  violations; text size lg/xl swept at 390/1024/1440. Backup of v3.1: `../design-backup-v3.1-2026-10-02/`.
- Final evaluator: CORE 7.8 → fixes (Home nav now identical to every other screen: + "Cần xử lý 6", "Trợ giúp & hỗ trợ";
  to-do #2–3 buttons quiet so only #1 is filled) → **CORE 8.0 PASS**. Other 44 screens: readiness 6.0 (tokenised,
  not yet restructured) — next round.

## 4.1.0 — 2026-10-04 — every screen on Calm (MINOR: new components, no token changes)
- Restructured the 44 remaining screens to the v4 layout grammar, group by group: Tiền, Đơn hàng, Sổ & thuế,
  Cần xử lý, Cài đặt, Onboarding (DESIGN.md §3). Generators: `directions/modern/redesign/pages*.py`.
- New: `c-switch--row` (+ state pill), `r-listhead`, `r-feedbar`, `r-settings`, `c-option--best`, `c-table__who`,
  `r-detail__head--calm`, `c-split__you` / `__err` / `__same`, `c-timeline__item--ai`, `c-todo__item--wait`,
  `r-onboard__recap`; token `--read-w` (880) for queues and feeds. Registry, shadcn map updated.
- Onboarding in Calm: no boxed card on desktop; sea progress; option/chip selection in sea; hairline groups;
  helper actions as links; sticky forward action at every size.
- Fixes found by the evaluator rounds (3 rounds, 5 + 4 + 2 independent evaluators):
  - Focus escaped all 16 open dialogs (keys probe) → page behind marked `inert` (`redesign/inert.py`).
  - `c-btn--quiet` had its border re-added by the v4 `.c-btn` base → re-asserted; destructive actions next to a
    primary are `c-btn--danger c-btn--quiet`.
  - Tiền hero facts were clipped by the Cần xem panel at 1440 (overflow, invisible to probe) → wrap.
  - Home bars: "Hôm nay" label was ellipsised to "Hô…" at 1440 → today column ≥ its label.
  - Say once: the Tiền legend no longer repeats the hero; order rows drop the unlabelled 3-bar glyph; the invoice
    "due" item is a neutral link, not a second hero figure; receipts carry the verified pill.
  - Feeds: event text leads, time is meta; "you did this" dot is neutral ink (sea is not a truth state).
  - Settings: coming-soon rows show no switch; required rows dim the switch.
  - Phone: long button labels, status signs, coach kicker, size-picker samples and list names wrap instead of
    widening the page; scrollable tables are focusable regions with a label.
- Machine pass on all 65 screens: probe 0 at 1440/1024/390 + stress, axe 0, keyboard escapes 0, text size lg/xl
  clean at 390/1024/1440.

## 4.1.7 — 2026-10-04 — clean-up (no visual change except 6 screens moved off retired parts)
- Archive: explorations (`directions/`), old evaluator packs, progress sheets, the v3.1 backup and an old token
  export moved to `../design-archive-2026-10-04/` (README inside; manifests renamed `*.archived.json`).
- Generators moved to `design/tools/v4/` (README: what each writes, inputs, run order); v3.1 overlay inputs copied to
  `tools/v4/src_v31/`. Re-running every generator reproduces all 68 screen files byte-for-byte.
- Retired for good: `c-lane(s)`, `c-later`, `c-msign(s)`, `c-route`, `c-prod(s)`, `c-truthbar`, `c-daybars`,
  `c-spark`, `c-trend`, `c-stamp`, `c-term`, `c-sheet`, `c-coach-anchor`, `r-money-hero`, `r-counter`, `r-ticket`,
  `r-pay`, `r-due`, `r-invoice`, `r-cart-bar` — CSS, catalog demos, registry (143 → 120), shadcn map entries.
- CSS: rules for classes no screen or catalog uses removed (404 rules), declarations overridden by the same selector
  later removed (492); components.css 1.918 → 1.524 lines, recipes.css 637 → 463. Tokens: 14 unused removed.
  Pixel diff of 132 full-page shots + catalog: identical except the 6 screens below.
- `c-split__legend` wraps in a narrow panel (auto-fit); `c-coach--inline` (coach above its target, no scrim).
- DESIGN.md §4: retired rows and the "Retired in v4" note removed; v4.1 components added; patterns updated.

## 4.2.0 — 2026-10-05 — BA scope: Control Tower, sales inbox, Order 360 (MINOR: new components)
- Inputs: BA docs (BRD 0.6, Capability Map 0.3, Feature Catalog 0.1, Key Use Cases 0.1), CEO Casso report; decisions in
  `SCOPE-MVP.md` §7–§8; business flows in `FLOWS.md` (6 flows + shared states + screen map).
- New components: `c-works`/`c-work`, `c-timeline__src` (+ item `--now`, `--next`), `c-rules`, `c-decide` (+ `__fig`,
  `__auto`), `c-quote`, `c-match` (`--unsure`), `c-journey`; recipe `r-tower` (list | detail, phone list only).
  `.c-btn[aria-disabled]` for gated risky paths; table footer total one size up. Catalog §v4.2, registry, shadcn map.
- Fix: `.r-shell__content` is one `minmax(0,1fr)` column, so a wide child (tabs) can no longer widen the page
  (pixel-identical on existing screens).
- 4.2.1 (2026-10-05) delivery: the skill's page-pattern recipes `r-board` and `r-split` added (`pattern.mjs --add`)
  and skinned with OPC tokens; `r-board__sum`, `r-board__card--you`, `r-pick`, `c-sim` ("Mô phỏng"), `r-courier`;
  `.c-btn--act[aria-disabled]` = locked primary with its reason on the button. Catalog §v4.2b, registry, shadcn map.
- 4.2.2 (2026-10-05) debts: `r-alloc` (one transfer → several invoices, arithmetic "đủ" kept apart from money truth),
  `c-tag` (neutral, e.g. "thu hộ"), `r-upcoming` ("Chưa tính"), `r-paid` (folded history), `.r-alloc__row:focus-within`,
  `.c-check input:focus-visible` visible ring, `.r-upcoming .c-sign` wraps. Catalog §v4.2c, registry, shadcn map.
- 4.2.3 (2026-10-05) purchases: `c-decide__result` (outcome right above the primary), `r-capture` (document thumbnail + assistant read + editable guess), `c-table__row--you` gets a tinted fill (system-wide), `c-table__row--muted` (not counted yet), `r-pick__qty--short`. Catalog block v42d; registry + shadcn map.
- 4.2.4 (2026-10-05) stock: `r-stock` (khả dụng = truth column, `__avail--low`), `r-trace` (two-way lot trace, OPC balance line first), `r-lock` (worst consequence first), `r-count` (count sheet, matched lines recede, gate pinned on desktop), `c-timeline--quiet`, `r-pick__chk--warn`. Fix: `td.c-table__who` no longer `display:grid` (tall rows kept height/hairline on 18 screens); needs-you tint covers the whole stacked row on phone. Catalog block v42e; registry + shadcn map.
- 4.2.5 (2026-10-05) production: `r-form2`, `r-mat` (+ `__have`, `__cure`), `r-dash`, `r-rail--quiet` (+ `r-rail__lot`), `r-detail__meta`; `r-count` reused for actual vs expected. System: on phone a banner's action drops under its text; signs never wrap inside table cells. Lesson kept: never `display:grid` a `td` (broke row height twice). Catalog block v42f; registry + shadcn map.
- 4.2.6 (2026-10-05) period close: `r-gate` (to-dos before locking; tone + type icon, state word leads the meta), `r-recon` (sources vs base, gap → to-do link), `r-book` (ledger, quiet ok signature, template caveat line, zebra), `r-drawer__fig`. Catalog block v42g; registry + shadcn map.
- 4.2.7 (2026-10-05) tax: `r-taxcalc`, `r-trust` (+ `--gate`; one amber disclosure per view), `r-return` (+ `__mark` stamp), `r-howto`, `r-pay`, `r-gate__i--match`. Catalog block v42h; registry + shadcn map.
- 4.2.8 (2026-10-05) setup: `c-sign--pass` (quiet healthy state, system-wide), `r-gate--err`, `r-ready__area`, `r-model` (+ `__plan`, `c-option__box`), `r-import`, `r-conn`, `r-policy` (+ `__r--lock`), `r-roles`, `r-roster`. Catalog block v42i; registry + shadcn map.
- 4.2.9 (2026-10-05) products & price lists: `r-prices` (+ `__def`, `__rule`, `__delta`, `__stock`, `__ok`), `r-plist` (+ `__main`). Catalog block v42j; registry + shadcn map.
- 4.2.10 (2026-10-05) programme: `r-shell--program`, `r-pstats`, `r-funnel` (+ `--part`, `__h`), `r-adopt`, `r-issue__n`, `r-preport` (+ `__toc`); `:target` highlight for deep-linked rows. Catalog block v42k; registry + shadcn map.
- 4.2.11 (2026-10-05) offline + demo: `c-health--off` (offline = pending tone; red only for conflicts), `r-offbar`, `r-qchip`, `r-offrules`, `r-queue` (+ `--done`), `r-pick__chk--err`, `r-pick__l--err`; demo console `r-demo` (demo build only). Catalog block v42l; registry + shadcn map.
- 4.3.0 (2026-10-05) An Nhiên migration: `c-tiles--few`, `c-tile--big` (idle hairline / in-cart raised), `r-pos__known`, `r-order__custok`, `r-home__run`, `r-home__moneyline`, `r-audit`; `c-doc__foot` wraps long codes. Shell (screens/home.html) is An Nhiên; `run_all.sh` rebuilds every generated screen in order. Catalog block v43a; registry + shadcn map.
- 4.3.1 (2026-10-05) onboarding: `r-model__sum`, `r-sure`, `r-gate__i--nice`, `r-onboard__aside--desk` (hidden < 1180); model choice chosen state = tint + hairline. Registry + shadcn map.
- 4.3.2 (2026-10-05) shift close: `r-den` (denomination count), `r-shift` (expected vs counted, reason gate, hand-over), `r-plist__row`. Catalog block v43b; registry + shadcn map.
- 4.4.0 (2026-10-05) navigation: `c-nav` expandable sections (`__grp`, `__row`, `__peek` 44px disclosure, `__sub`, `__subitem`, `__item--here`, `__list--foot`, `--sheet`); rail replaces the in-page sub-nav ≥721px; rail 252px on tablet. `c-table__optline`, `c-table__cell--act` (hidden 721–1180), money cells never wrap, stacked phone rows drop per-cell hairlines. `r-help`. Catalog block v44.
- 4.4.1 (2026-10-05) c-table severity: `row--err` (and you-row with an err sign) = red edge + tint; `c-table__zero` "0 ₫"; `c-table__foot-note`; stacked phone tfoot; row-name links quiet until hover. c-nav role rails flatten a lone child. Catalog block v441.
- 4.5.0 (2026-10-05) type budget + rhythm: font tokens 14·16·18·24·32·44 (was 12 sizes), weights 400/600/700 (500 → 400 or 600, 650 → 600/700, 750–900 → 700; nested b/strong 700); wrapped titles lh 1.35; `.page` is a grid with `--page-gap` (was block, 0 gap on 73 screens); crumbs 8px above title; figure ≥ 12px under title; `r-detail__head--calm` = title 1fr + actions auto on the title line at the right edge; `r-page-head` actions on the title line, title on `--fs-h1`; `c-table tfoot th` keeps the top rule only; `c-dialog__k` 4px above the title. Applied by `tools/v4/proposal_v45.py --apply` + recipes v4.5 block.
- 4.5.1 (2026-10-06) icons/reading budget rules in the system: `r-gate` rows without the leading icon chip (3-col grid ≥721px); `c-table td .c-sign--ok/--pass` words only; rail reconciliation rows grouped by space; `.r-gate__foot .c-decide__result` unboxed. DESIGN.md §Type gains the icon rule.
- 4.5.2 (2026-10-06) `r-gate` phone grid fixed (old 32px pic track no longer applies ≤720px; empty `__amt` collapses); `c-table td .c-sign--pass` neutral ink; table names lh 1.35; `r-roster` balanced columns. DESIGN.md: colour + reading rules.
- 4.5.3 (2026-10-06) colour/icons: `c-arrived` (+`--ok`) surface + 4px tone edge (icon circle kept); `c-banner--ok` surface + ok edge; `c-note`, `c-waitbar`, `c-coach--inline` neutral; `c-paysteps` 16px dots without icons; `r-order__opts p.c-switch` stacks (verified invoice line); `c-arrived__m`, `c-tile__meta` ink-2; table cells/labels lh. DESIGN.md: tint rule.
- 4.5.4 (2026-10-06) last budget pass: `r-trace` dot node + line (no icon chip per row); `r-board__col` borderless, board settled signs words only; `r-den` rows with one right-aligned money edge, zero rows recede; table `c-sign--wait` words only; `c-dialog__k` 8px; sign/label line-heights for diacritics.
- 4.5.5 (2026-10-06) phone budgets + icon rule: `small` 14px/1.4 (UA default was 13.3px); wrapped buttons/options/titles lh 1.35; phone `c-work--you` and stacked you-rows use the edge, no fill; passed `c-rules__r` quiet; `r-onboard__fig`; compact onboarding step map hidden ≤720px. New build step `tools/v4/quiet_icons.py` (labelled buttons without verb icons; keeps chevron/lock/icon-only).
- 4.5.6 (2026-10-06) re-score fixes: onboarding step map = quiet left-ruled rail (no card), `c-stepmap__n` fits "0/6"; `c-banner--err/--pend` surface + tone edge; onboard-done one primary; date-range continuous track; `c-empty` reason + one primary + text link; late figure in err ink in `--err` rows; `tfoot` total larger; OTP active cell + focus ring; phone "Thêm" tree marks the current section.
- 4.5.7 (2026-10-06) phone "Thêm" sheet: shows the page you came from (`aria-current` on Hôm nay: fill + 3px tick + act ink), 2px rule per expanded group. Fixed: `home_states.py` had stripped the Bán section icon from the tree (per-row icon removal was meant only for the command palette).
- 4.5.8 (2026-10-07) polish list: borderless count inputs until focus; row-action cells on one right edge; sticky page head on setup-policy; roster sub-line stacks; "Sửa" links underlined act-ink in onboarding; delivery board sums quieter; phone content bottom padding; sheet group rule tinted + CTA spacing; onboarding rail closing margin.
- 4.5.9 (2026-10-07) owner-reported bugs: (1) `c-menu__item` without a leading icon used the 24px icon column for its text (orders--search, home--command results broke one word per line) → `:not(:has(> .c-ic))` single-column grid; (2) rail counts share one column (rows without a disclosure button reserve its width; child counts align to the parents'); (3) date-range dialog 460px with a full-width calendar; (4) phone titles 24px (a 32px title broke into 4 lines); bulk bar actions wrap; toast rides at the top while the bulk bar is open; demo rows wrap. budget.mjs: new `narrow` check (text squeezed to ≤ 1.5 words per line) + selftest fixture.
- 4.6.0 (2026-10-07) Connector flow + rail: **Kết nối** is a top-level rail item (flat, with an error count `c-nav__count--err`), no longer under Cài đặt. Six new screens: `connections--detail`, `--provider`, `--consent` (owner-only, scope + 180 days + OTP), `--testing`, `--unknown` ("Chưa rõ kết quả": no auto-resend), `--log`. List buttons now link to them. Date-range dialog: equal fields, hint below both, start/end in the action colour, continuous range track.
- 4.6.1 (2026-10-07) rail rows: hover / focus / current section is one surface over the whole row (label + count + chevron); the chevron no longer sits outside the highlight.
- 4.7.0 (2026-10-07) rail counts "C+": a group row = label + its count, chevron at the far right; a leaf row = label, count on the chevron axis; whole row is one hover/current surface. Chosen from three options after a web/precedent review (Linear: don't compete for attention; SetProduct: a badge annotates its parent, dot-only when the count doesn't matter — here the count does).
- 4.7.1 (2026-10-07) rail counts: back to two right-hand columns [count][chevron] (C+ of 4.7.0 made numbers float at ragged x after the labels). Count pill turns white on hover/current so it stays visible; whole row is one hover surface.
- 4.8.0 (2026-10-07) Kết nối redesigned (provider-led front door): `connections` = health + one card per connected ACCOUNT with its jobs as chips + "Chưa có cách nối"; `connections--add` provider directory (states: Đã nối / Nối / Mô phỏng / Báo tôi); `connections--category` = the 17-category table as secondary view; `connections--use` "Dùng để làm gì?"; `connections--account` per-job switches, consent, Nối lại / Ngắt; `connections--disconnect` consequences dialog; `connections--detail` = X Invoice account in error. New recipes `r-acct`, `r-dir`, `r-use__acts`.
- 4.9.0 (2026-10-07) Kết nối at scale: directory v2 (search, status chips, "Gợi ý cho hộ của chị", "Sắp có" folded per group, request a provider), provider page before connecting (`connections--info`), category hub `connections--delivery` (ways to deliver, how the carrier is chosen, ranked quote preview), `connections--many` (14 accounts: "Cần chị xem" first, chips, grouped compact rows). New recipes `r-car`, `r-crow`, `r-quote`, `r-trustbox`, `r-dir__more`. `system/connector-catalog.md`: providers are data.
- 5.0.0 (2026-10-07) Provider catalog as data (`tools/v4/providers.py`, 71 rows: mode = casso / oauth / key / link / assist, status, source tag). New recipes: `r-dir__nb` (tile name + how it connects), `r-dir__pills` ("Sắp có"), `r-guide` (numbered steps with where-tag), `r-keys` (field stack), `r-opt--danger`, `r-save--bar` (sticky save), `r-reg` (registry table with phone labels). Healthy account state = words (`.r-acct__st .c-sign--pass` hides its icon).
- 5.1.0 (2026-10-07) `tools/v4/capabilities.py` = the 11 features (tier, when, why, recommended way, choices, manual path, demo state). Recipes: `r-feat` (feature row: name+what | way+state | action, fixed columns), `r-feat__i--err` (gutter marker), `r-feat__more`. Onboarding step bar is 7 segments (`onboard43.py`).
- 5.1.1 (2026-10-07) Household screens show no provider marks (`.r-acct__logo` hidden; account/directory/delivery rows are text-only grids), `r-jump` (jump links), `brand.py` rewrites shared chrome to OPC voice.
- 5.1.2 (2026-10-07) docs only: step limit 7 (DESIGN), SCOPE §8 feature mapping, connector-catalog `auth.mode`, FLOWS 7-step onboarding.
- 6.0.0 (2026-10-07) `onboard_lib.py`, `onboard_flow.py`, `readiness_model.py`, `pages_readiness.py`; capabilities: 12 việc (+pay); providers: +bank-link. Step limit 5.
- 7.0.0 (2026-10-08) `onboard_lib.py` is the single source of STEPS (6) + ABOUT; capabilities tiers need/opc/optional; providers +`opc` mode (OPC lo sẵn); readiness_model v7 (25 items, 4 chains, states incl. skip); recipes `r-yn`, `r-open`, `r-ready__opt`, `r-ready__next`, `r-onb-hero`. Step limit 6.
- 7.1.0 (2026-10-08) navtree v7 (ERP sections, `('err', n)` child counts, PREFIX map page→section), `nav7.py` post-pass (rail + sub-nav + tab bar on every household screen).
- 7.2.0 (2026-10-09) recipes: `r-tracks` (independent tracks of one record; phone = one compact row each), `r-qty` (counted quantity inside r-pick), `r-recv` (field gap). navtree: detail pages prefer the base list child over its `--` variant.
- 7.3.0 (2026-10-09) recipes: Bán nhanh (`r-quick__goods`, `r-quick__total`, `r-step`, `r-chkrow`), card spacing after `c-kv`. navtree PREFIX quick-sale → Bán hàng. New post-pass `relink.py`.
- 7.4.0 (2026-10-09) recipes: spacing after `c-quote` / `r-pick` / `r-capture`. navtree PREFIX customer-statement → Tiền; Thu chi count 4.
- 7.5.0 (2026-10-09) recipes: `r-guide7` (numbered guide steps). Generators: pages_books7 replaces pages_tax.
- 7.5.1 (2026-10-09) components: `c-seg__opt[aria-checked=true]` white face + 2px ring. recipes: `r-jump7`, `r-lines` (+`--alloc`), `r-skip`, `r-gate__ic`, `r-feat__open`, option title icon, onboarding signature (`.r-onboard .c-steps__seg--done/now`, stepmap). DESIGN: money-truth signature extended to progress (done = verified green, now = pending amber).
- 7.5.2 (2026-10-09) Status vocabulary: `maps/status.json` (7 states), DESIGN.md section; `status7.py` post-pass.
- 7.6.0 (2026-10-10) recipes: `r-phone-only` (order lists), `r-ledger` (books on phone), compact `r-listhead` on phone, `r-board__head` line height. Post-pass `tracks7.py`.
- 7.7.0 (2026-10-10) recipes: `r-mob-only`. nav7: role tab bars (cashier: Tổng quan · Bán · Thêm; accountant: Sổ · Tiền · Thêm). Post-passes links7, offline7, role7.

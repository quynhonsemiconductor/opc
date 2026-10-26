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

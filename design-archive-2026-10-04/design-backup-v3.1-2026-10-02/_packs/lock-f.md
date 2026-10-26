# Context pack — OPC · Maker · Phase 5 LOCK (direction F Biển Chỉ Dẫn)

## 1. Product in 5 lines
OPC: web app (laptop + phone browser) for Vietnamese household businesses ("Hải sản khô Cô Hai", Nhơn Lý,
Quy Nhơn; owner 58, successor son Phúc 29). Home = "needs-me-now + is-my-money-real"; Counter = cart → QR →
done, payment state impossible to misread. Brief: /Users/benq/Desktop/qnsc/opc/design/system/BRIEF.md (§3, §4, §7 only).

## 2. Decision (GATE, 2026-10-02)
User chose **F Biển Chỉ Dẫn** with **calming polish borrowed from A Sổ Tay**. Source files (round-3, passed 8.0):
`/Users/benq/Desktop/qnsc/opc/design/system/directions/f-chi-dan/` — tokens.css, base.css, home.html, counter.html,
counter--payment.html, NOTES.md (read NOTES first). Look at A only for the hairline-list feel:
`directions/a-so-tay/shots/home-1440.png` (one Read, max).
Tech (ADR 0007): React 19 + Vite SPA, Tailwind v4, **shadcn/ui headless** — components must map cleanly to shadcn/Radix
primitives (Button, Dialog/Sheet, Switch, ToggleGroup, Table, Input, Badge, Tabs) + `custom` where no primitive exists.

## 3. Hard constraints (unchanged)
Vietnamese with full diacritics; Barlow + Public Sans (Vietnamese subset). Money `1.020.000 ₫`, tabular figures.
Body ≥ 16px, meta ≥ 14px, nothing < 14px. AA contrast. Status = colour + label + pictogram. Targets ≥ 44px
(56px in the counter touch context). Colour jobs: yellow = act now ONLY; green = verified/done; blue hatched+dashed =
pending (bank/CQT); red = error only; cash neutral.

## 4. What to produce (all paths absolute under /Users/benq/Desktop/qnsc/opc/design/)
Conventions: read `~/.claude/skills/uiux-studio/references/consistency.md` and `references/design-md-template.md`
(both short). Component tokens are NOT declared on `:root`; components read them with a semantic fallback,
e.g. `min-height: var(--btn-h, var(--target))`. Contexts use `data-density="touch|compact"` (rename F's
`data-context`). Keep `data-platform="ios|android"` placeholders for later native.

1. `system/tokens.css` — replace the starter with F's tokens (fonts `@import` first), 3 tiers, contexts touch/compact
   (dark theme not required now — leave a commented stub).
2. `system/components/components.css` — every reusable piece of F's base.css as `c-*` (base / `--variant` /
   `__part`), tokens only, all states (hover, focus-visible, active, disabled/aria-disabled, loading where relevant).
   Expected set (merge/rename as you judge, ≤ 6 variants each): c-btn (primary=act, secondary, quiet, danger, locked),
   c-icon-btn, c-sign (status sign: ok, pend, wait, err, cash, cqt), c-moneyline (3-stop), c-lane (now/today/week),
   c-card, c-nav (sidebar) + c-tabbar (phone bottom nav), c-table, c-input, c-switch, c-seg, c-prod (product row/tile,
   in-cart state, stepper), c-ladder ("ĐANG Ở ĐÂY" route), c-qr, c-sheet (phone bottom sheet), c-confirm-locked if not
   a btn variant. Replace F's old `.c-hide`/`.sr` with one `.u-sr` utility.
3. `system/components/recipes.css` — product compositions as `r-*` (e.g. r-money-hero, r-pay-panel, r-ticket, r-cart-bar).
4. `system/components/registry.json` — every c-*/r-* with name, WAI-ARIA APG pattern, variants, parts (keep the
   existing $description; replace the 4 starter entries).
5. `system/components/catalog.html` — every component in every variant and state, Vietnamese real labels, sections
   with headings; links ../tokens.css, components.css, recipes.css.
6. `system/DESIGN.md` — from the template: tokens, layout grammar (shell, grid, breakpoints 1440/1280/1024/390,
   counter focus mode), components (anatomy, use/don't), patterns (lanes, money states, confirmations, empty/error),
   content rules (voice = owner sentence, money/date format), a11y, never-do list. ≤ 1,800 words.
7. `apps/app/screens/home.html`, `counter.html`, `counter--payment.html` — LAYOUT ONLY: link
   `../../../system/tokens.css`, `../../../system/components/components.css`, `../../../system/components/recipes.css`,
   `../app-tokens.css`; a `<style>` block may hold only grid/flex/placement — never colour, font, border or any `c-*`
   restyle. Same content as F round 3.

## 5. Polish to apply while locking (evaluator + Director)
Calming: solid filled numeral block ONLY for lane 1 (yellow); lanes 2–3 = ink outline numeral on white; 4–6 grey
text numeral. Lists and ledgers use 1px hairlines (A's feel) instead of boxed cards where a card adds nothing.
Fewer dark blocks overall. Then F's open fixes:
1. home@390: lane hints wrap to 2 lines max (no ellipsis truncation).
2. Sidebar workspace name → "Cô Hai · Nhơn Lý" (no wrap).
3. Lane 1 repeats facts — say each fact once (headline, amount, action).
4. Counter payment column crowded — merge the 2,000,000 ₫ rule note into the ladder caption.
5. counter@390: clear separation between product list and the sticky Giỏ summary bar.

## 6. Machine pass (no images until clean)
`cd ~/.claude/skills/uiux-studio/scripts`; for each screen + catalog: `node probe.mjs <html> --size 1440x900 --min-font 14`,
`--size 1024x768`, `--size 390x844 --mobile`, `--size 1280x800 --stress`; counter files also `--min-target 56`;
`node a11y.mjs <html>`; then `node status.mjs /Users/benq/Desktop/qnsc/opc/design/apps/app` and
`node status.mjs /Users/benq/Desktop/qnsc/opc/design/system` — fix every ERROR (local overrides, raw controls,
undefined components, registry gaps). Then ONE look: `node shots.mjs <html> <apps/app/shots> --sizes 1440x900,390x844 --scale 0.5`
per screen + `node sheet.mjs` of them; Read the sheet once; at most 1 refinement round with Edit.
Do NOT edit directions/, BRIEF.md, manifests or anything outside the files listed in §4.

## 7. Reply (≤ 150 words)
Files written; component list (count + names); polish items done/not done; probe/axe/status results;
honest weakest point; subagent_tokens if known.

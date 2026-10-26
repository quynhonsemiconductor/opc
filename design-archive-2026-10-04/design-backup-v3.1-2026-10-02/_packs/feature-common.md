# Context pack — OPC · Maker · Feature screens on the LOCKED system v1.1.0 (direction F "Biển Chỉ Dẫn")

## 1. Product in 5 lines
OPC: web app (laptop + phone browser) for Vietnamese household businesses ("Hải sản khô Cô Hai", Nhơn Lý;
owner Trần Thị Hai 58, son Phúc 29 runs the laptop). Two questions rule every screen: "what do I do first?"
and "is this money real?". Money states never merge: Chờ khách chuyển → Đã nhận · chờ xác minh → Đã xác minh.

## 2. Read first (only these)
- /Users/benq/Desktop/qnsc/opc/design/system/DESIGN.md (whole file — the rules)
- /Users/benq/Desktop/qnsc/opc/design/system/BRIEF.md **§10 only** (exact content; use it verbatim)
- /Users/benq/Desktop/qnsc/opc/design/system/components/components.css and recipes.css (class names; skim)
- The existing screen(s) named in your task in /Users/benq/Desktop/qnsc/opc/design/apps/app/screens/ — copy
  their head, icon sprite and shell markup; do not re-invent them.

## 3. Hard rules
- Screens are LAYOUT ONLY. Link exactly: `../../../system/tokens.css`, `../../../system/components/components.css`,
  `../../../system/components/recipes.css`, `../app-tokens.css`. A `<style>` block may hold only grid/flex/
  placement/display using tokens (`var(--space-*)`, layout tokens) — never colour, font, border, px values, or
  any rule that targets a `c-*`/`r-*` class. Use `style="width:…%"`/`flex:` only for data-driven bars.
- Use only existing c-*/r-* classes. If something is missing, DO NOT invent CSS — use the closest component and
  list the gap in your reply ("PROPOSE: …").
- Vietnamese with full diacritics; money `1.020.000 ₫`; times `10:44`; status = sign/pictogram + word.
- One yellow (`--act`) action per view. Counter/sheets use `<body data-density="touch">`.
- Write files in chunks: create with the first ≤ 250 lines, then append with Edit. For a state of an existing
  screen, `cp` the base screen with Bash and change only what differs using Edit.

## 4. Machine pass (no images until clean)
`cd ~/.claude/skills/uiux-studio/scripts`, for every file you made:
`node probe.mjs <abs html> --size 1440x900 --min-font 14` · `--size 1024x768` · `--size 390x844 --mobile` ·
`--size 1280x800 --stress` (touch screens also `--min-target 56`); `node a11y.mjs <abs html>`;
then `node status.mjs /Users/benq/Desktop/qnsc/opc/design/apps/app` must show no ERROR and no hard-coded values
for your files. Then ONE look: `node shots.mjs <html> /Users/benq/Desktop/qnsc/opc/design/apps/app/shots
--sizes 1440x900 --prefix <screen>` and `--sizes 390x844 --mobile --prefix <screen>` per file, one `node sheet.mjs`
of them, Read it once; at most one refinement round with Edit.
Do NOT edit tokens, components, recipes, catalog, DESIGN.md, BRIEF.md or manifests.

## 5. Reply (≤ 150 words)
Files written; components used; PROPOSE list (missing pieces); probe/axe/status results; weakest point;
subagent_tokens if known.

## 6. Your task

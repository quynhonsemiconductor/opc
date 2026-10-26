# Context pack — OPC · Maker · Finalist screens (Home + Counter)

## 1. Product in 5 lines
OPC: web app (laptop + phone browser) for Vietnamese household businesses — "Hải sản khô Cô Hai", Nhơn Lý,
Quy Nhơn; owner 58, successor son Phúc 29 runs the laptop. Jobs in order: sell at the counter fast (VietQR /
cash, cash-register e-invoice issued automatically), know if today's money is real (QR payments stay
"chờ xác minh" until verified), handle what needs them now, keep tax right. Trust > delight.

## 2. Hard constraints
Full brief: /Users/benq/Desktop/qnsc/opc/design/system/BRIEF.md — **use §7.1–§7.3 content verbatim**
(every row, number, state) and obey §4. Fonts with Vietnamese subset only. Body ≥ 16px, meta ≥ 14px, nothing
< 13px, AA contrast, status = colour + label + icon, targets ≥ 44px; Counter in a touch context (≥ 56px).
Sizes: 1440×900, 1280×800, 1024×768, **390×844 phone browser** (Home stacks "Cần xử lý" first; Counter =
product list + sticky cart bar "4 món · 1.020.000 ₫ · Thu tiền"; put the payment sheet in a separate file
`counter--payment.html` at 390 only).
Money truth everywhere: Chờ khách chuyển → Đã nhận · chờ xác minh → Đã xác minh; never show a total as
"real" without its pending part. Anti-slop: ~/.claude/skills/uiux-studio/references/anti-slop.md.

## 3. Direction (your starting point — evolve it, don't restart it)
Your tile: /Users/benq/Desktop/qnsc/opc/design/system/directions/a-so-tay/tile.html and NOTES.md (read both).
**A — "Sổ Tay"**: the household's paper notebook made precise. Ruled lines and columns, not cards; Source
Serif 4 for money/headings, Public Sans for UI; blue-black ink, vermilion seal ONLY for the verified stamp.
Signature: verified money gets the "ĐÃ XÁC MINH" seal; pending shows a dashed empty seal outline.
Evaluator risks to fix: the stamp must be legible at 16px+ and on 390px (no tiny rotated 13px caps — make it
larger, rotation subtle or none); error brown must be clearly different from the seal vermilion (pick a
distinct hue + icon); serif money must not feel formal/slow next to a dense counter — the Counter can use the
sans for product tiles and keep serif for totals. Borrow from the receipt tile: the Counter ticket is a printed
receipt slip with a timestamped stamp line ("ĐÃ XÁC MINH 10:43"), perforation only at its top/bottom edge.
Borrowed for both finalists:
- The 3-step money line (Chờ chuyển → Đã nhận → Đã xác minh) as a thin marker next to money amounts
  (idea from another tile), drawn in YOUR direction's language.
- One plain-language sentence above key money figures in the owner's voice, e.g. "1.380.000 ₫ chưa xác
  minh — đối chiếu trước khi giao hàng lớn". Exact figures always stay visible under the sentence.

## 4. Rules
- Write only in /Users/benq/Desktop/qnsc/opc/design/system/directions/a-so-tay/: `tokens.css` (all tokens as CSS
  custom properties, 3 tiers: --p-* primitives → semantic → component tokens NOT declared on :root),
  `base.css` (shared shell/components for this direction), `home.html`, `counter.html`,
  `counter--payment.html`, `shots/`, update `NOTES.md` (per round: what changed).
- Machine pass first, no images: `cd ~/.claude/skills/uiux-studio/scripts` then for each file
  `node probe.mjs <abs> --size W x H` at 1440x900, 1024x768, and `--size 390x844 --mobile`;
  `node probe.mjs <abs> --size 1280x800 --stress`; counter with `--min-target 56`; `node a11y.mjs <abs>`.
  Fix everything reported (overflow, clipping, tiny text, fonts, small targets, contrast).
- Then look ONCE per round with one contact sheet: `node shots.mjs <abs html> <abs shots dir> --sizes
  1440x900,1024x768,390x844 --scale 0.5` for home and counter, then `node sheet.mjs <abs>/shots/_round.png
  <the six @0.5 pngs> --cols 3 --width 1800` and Read only that sheet. Crop with `--selector` if a detail
  needs full resolution. Edit, never rewrite whole files.
- Also save full-res shots for the evaluator: `node shots.mjs <home.html> <shots> --sizes 1440x900,1280x800,1024x768,390x844`
  and the same for counter.html; `counter--payment.html` at 390x844 with `--mobile`.
- A separate evaluator will grade you; do not self-score above what you can defend. After the first build
  reply (≤ 150 words): files, what you kept/changed from the tile, how money truth reads, known weak spots,
  subagent_tokens if known. You will then receive evaluator fixes — apply them with Edit.

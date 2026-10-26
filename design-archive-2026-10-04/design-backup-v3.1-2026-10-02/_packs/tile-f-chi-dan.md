# Context pack — OPC · Maker · Style tile (one per agent)

## 1. Product in 5 lines
OPC: web app for Vietnamese household businesses (dried seafood shop in Nhơn Lý, Quy Nhơn — owner 58,
successor son 29 runs the laptop) to sell at the counter, take VietQR/cash, auto-issue cash-register
e-invoices, see money and tax. Users fear getting money/tax wrong; trust > delight. Home = "needs-me-now
+ is-my-money-real"; Counter = cart → QR → done, payment state impossible to misread.

## 2. Hard constraints
Vietnamese with full diacritics; ONLY fonts with the Vietnamese subset (list:
~/.claude/skills/uiux-studio/library/fonts.md). Money `1.020.000 ₫`, weights `0,5 kg`, tabular figures.
Body ≥ 16px, meta ≥ 14px, nothing < 13px, AA contrast, status = colour + label (+ icon), targets ≥ 44px.
Money states: Chờ khách chuyển → Đã nhận · chờ xác minh → Đã xác minh. Invoice: Chờ mã CQT → Có mã CQT.
Own brand (name "OPC", small "by QNSC" allowed). Anti-slop list: ~/.claude/skills/uiux-studio/references/anti-slop.md
(plus: no green+gold agriculture palette, no bank-blue by default, no seafood/wave clip-art, no Tết clichés).

## 3. Direction
Given in section 5 (name, idea, attributes with sources, signature move, risk). Execute it with conviction —
a tile is a point of view, not a palette swap. Reference screenshots are in
/Users/benq/Desktop/qnsc/opc/design/system/refs/ (DNA cards in refs/dna/ and
~/.claude/skills/uiux-studio/library/dna/) — read only the 1–2 named for your direction.

## 4. Rules
- Template: ~/.claude/skills/uiux-studio/templates/style-tile.html (fixed 1200×800). Write ONLY
  /Users/benq/Desktop/qnsc/opc/design/system/directions/<id>/tile.html (+ tokens inline in :root of the tile)
  and directions/<id>/NOTES.md (5 lines: idea, fonts+why, colours+why, signature, self-score honestly).
- The tile must show: name + 3 words, 2 anchor refs, type specimen in Vietnamese (display, body,
  numerals `1.020.000 ₫`), colour roles, components in states (primary/secondary/disabled button, input,
  status labels for: Chờ xác minh · Đã xác minh · Chờ mã CQT · Lỗi), and the **content slice** below,
  and the **signature move** labelled.
- Content slice (verbatim): **Tiền hôm nay** — Doanh thu 8.460.000 ₫ · 23 đơn · +19% so với hôm qua
  (7.120.000 ₫); QR/chuyển khoản 5.940.000 ₫ (đã xác minh 4.560.000 ₫ · chờ xác minh 1.380.000 ₫) ·
  Tiền mặt 2.520.000 ₫. Then two **Cần xử lý** rows: "2 khoản QR chờ xác minh — DH-1043 1.020.000 ₫ (10:42),
  DH-1041 360.000 ₫ (10:05) → Đối chiếu" and "Chuyển khoản không có mã đơn — 2.150.000 ₫ từ NHA HANG BIEN DONG,
  09:15 · gợi ý: công nợ Nhà hàng Biển Đông → Gán vào đơn".
- Machine checks before looking: `cd ~/.claude/skills/uiux-studio/scripts && node probe.mjs <abs tile.html>
  --size 1200x800` (fix overflow/clipping/tiny text/fallback fonts). Then ONE look:
  `node shots.mjs <abs tile.html> <abs dir>/shots --sizes 1200x800 --prefix tile` and Read the PNG.
  At most 2 refinement rounds, using Edit (never rewrite). Do not look at other directions.
- Reply: files written, fonts, accent colour, the signature in one line, honest weakest point,
  subagent_tokens if known. Max 120 words.

## 5. Your direction
**F — "Biển Chỉ Dẫn"** (id `f-chi-dan`)
- Idea: airport/expressway wayfinding — you always know what to do next
- Attributes: metaphor: transit wayfinding signage (wildcard domain) · layout: strong panels, numbered 'lanes' by urgency (1, 2, 3 as huge numerals), arrow-led actions, pictograms · type: DIN-like grotesk (Barlow or Archivo) for headers/numbers + Barlow/Public Sans body · colour: high contrast — black/near-black panels with signal yellow for 'act now', white text; local touch from Vietnamese expressway green/blue signs used for secondary categories · shape: 4–6px radius, rectangular panels · density: medium
- Signature move: URGENCY LANES: to-dos are numbered lanes with big numerals and an arrow action, like gate signs; money states use pictogram + word, readable from across the counter
- Risk to manage: dark panels can feel heavy in daylight; keep the canvas light
- Anchor refs to read: refs/linear.png (structure only); wayfinding from your knowledge

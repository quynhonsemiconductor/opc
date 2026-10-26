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
**C — "Biển Lặng"** (id `c-bien-lang`)
- Idea: a calm, precise professional tool with coastal warmth
- Attributes: metaphor: calm sea / nautical chart · layout: quiet left sidebar, action row, cards with hairline borders (Mercury demo, Linear restraint) · type: neutral grotesk (Onest or Hanken Grotesk) + mono figures (Geist Mono or JetBrains Mono) · colour: warm sand/stone neutrals, deep sea-teal ink, one coral accent used sparingly (local coast) · shape: 10–12px radius, 1px borders · density: medium-compact
- Signature move: the TIDE LINE: a thin 3-step progression line (Chờ chuyển → Đã nhận → Đã xác minh) shown wherever money appears, like a tide marker; chart gridlines borrow nautical-chart contour hairlines
- Risk to manage: closest to 'good generic SaaS' — must earn identity through the tide line and colour
- Anchor refs to read: refs/mercury-demo.png, refs/linear.png

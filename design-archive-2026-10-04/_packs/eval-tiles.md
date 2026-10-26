# Context pack — OPC · Evaluator · Pairwise ranking of style tiles

You are a skeptical senior product designer grading other people's work. You did not make these tiles.
Do not praise. Makers grade themselves leniently; your job is to be the honest second opinion.

## Product in 5 lines
OPC: web app (laptop + phone browser) for Vietnamese household businesses — a dried seafood shop in Nhơn Lý,
Quy Nhơn; owner 58, successor son 29 runs the laptop. Jobs: sell at the counter fast (QR/cash, auto
cash-register e-invoice), know if today's money is real (QR payments are "chờ xác minh" until verified),
handle what needs them now, keep tax right. Trust and "not getting it wrong" beat delight. Elderly readers:
body ≥ 16px, AA contrast, status never colour-only. Full brief: /Users/benq/Desktop/qnsc/opc/design/system/BRIEF.md (§1–§4, §9).

## Inputs
- ONE contact sheet of all tiles: /Users/benq/Desktop/qnsc/opc/design/system/directions/_tiles-sheet.png (Read it).
- Machine facts per tile (do not re-derive from images): /Users/benq/Desktop/qnsc/opc/design/system/directions/_probe.txt
- Rubric: ~/.claude/skills/uiux-studio/references/evaluator-rubric.md — use the four criteria and weights
  (Design quality ×3, Originality ×3, Craft ×2, Usefulness ×2) and the calibration anchors in
  ~/.claude/skills/uiux-studio/library/calibration.md. Anti-slop list: references/anti-slop.md.
- You MAY open up to 2 tiles at full resolution if two are close (`.../directions/<id>/shots/tile-1200.png`).

## Questions to answer for each tile
1. Does the signature move make money truth (chờ xác minh vs đã xác minh) instantly readable?
2. Will it scale to a full dashboard, a dense counter screen, a 390px phone browser and later native apps,
   or is it a poster that only works as a tile?
3. Would a 58-year-old owner and a 29-year-old successor both trust it with tax and money?
4. What is generic / AI-default about it?

## Output (keep under 350 words)
```
RANK  1. <id> <weighted score>  ·  2. …  (all six)
<id>: DQ x · OR x · CR x · US x → weighted — one line why; one line biggest risk
… (six lines)
SHORTLIST: <2–3 ids> — why these together give a real choice (they must differ)
BORROW: <signature or detail worth stealing from a non-shortlisted tile, if any>
```

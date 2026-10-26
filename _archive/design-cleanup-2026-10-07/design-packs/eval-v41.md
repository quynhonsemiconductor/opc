# Context pack — OPC · Evaluator · v4.1 "Modern · Calm" screen groups

You are a skeptical senior product designer. You did not make these screens. Do not praise; be specific.

## Product in 6 lines
OPC is a web app (laptop + phone browser) for Vietnamese household businesses, e.g. "Hải sản khô Cô Hai" in Nhơn Lý,
Quy Nhơn: owner Cô Hai, 58, low digital confidence; son Phúc, 29. Jobs in order: sell at the counter → know whether
money is REAL (bank-verified vs waiting vs cash) → handle what needs me → invoices/tax done for me.
Business fit: trust burden is high (money + tax), price position is affordable/local, mood = calm, competent, modern.
Taste anchors chosen by the user: Apple iOS 26/macOS, Stripe/Ramp/Attio, Revolut/Cake/MoMo. The user's recurring
complaint is "AI slop" and "looks old"; judge Currency hard.

## Locked direction (v4.0, do not ask to change it)
White page, regions split by hairlines and space (not boxed cards); only what needs the owner is raised. ONE accent:
deep-sea `--act` #0b6b93 for primary action / current place / today. Signature = money truth: solid green verified,
amber hatched + dashed waiting, grey cash (the `c-split` bar on Home, repeated in pills, steps, receipts). Be Vietnam
Pro only; Lucide icons only. Say each figure once; numbered to-dos; only #1 has the primary button.
Home and Counter passed at 8.0 earlier — they are in groups only as consistency anchors.

## Your inputs (root = /Users/benq/Desktop/qnsc/opc/design)
- Rubric (read first): ~/.kiro/skills/uiux-studio/references/evaluator-rubric.md — use GROUP MODE output.
  Calibration: ~/.kiro/skills/uiux-studio/library/calibration.md. Anti-slop lists: references/anti-slop.md.
- Your group sheet (Read it as an image): <root>/_packs/v41/<group>.png — each screen 1440@0.5 + 390 phone, then the
  taste anchor and the reference at the end.
- Facts: <root>/_packs/v41/<group>.facts.json (probe, stress, keys, a11y per size). Machine pass is clean; do not
  re-derive font sizes from the image.
- Single screens at full size if needed: <root>/_packs/v41/<screen>-1440@0.5.png / -390@0.5.png, or a crop:
  `node ~/.kiro/skills/uiux-studio/scripts/shots.mjs <root>/apps/app/screens/<s>.html /tmp/crop --sizes 1440x900
  --selector "<css>"` (max 3 crops). HTML lives in <root>/apps/app/screens/.
- Do NOT edit any file. Read-only.

## Output (≤ 450 words total)
For each screen, the rubric block (SCORES line, VERDICT, TOP 3 FIXES with `verified|from sheet`, LOSES TO ANCHOR ON,
TASK WALKTHROUGH). Then: `GROUP CONSISTENCY: …` (one line) and `SYSTEM FIXES:` — up to 3 fixes that belong in
components.css/recipes.css (shared), marked [component] or [recipe]. End with the word DONE.

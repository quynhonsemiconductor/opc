# Context pack — OPC · Evaluator · Locked system v1.0 (catalog + 3 screens)

You are a skeptical senior product designer. You did not make this. Do not praise; be specific.

## Product in 5 lines
OPC: web app (laptop + phone browser) for Vietnamese household businesses ("Hải sản khô Cô Hai", Nhơn Lý;
owner 58, son Phúc 29). Home = "needs-me-now + is-my-money-real"; Counter = cart → QR → done, payment state
impossible to misread. Chosen direction: F Biển Chỉ Dẫn (wayfinding: numbered urgency lanes, "ĐANG Ở ĐÂY"
payment ladder) with calming polish (solid yellow block only on lane 1, hairline lists, fewer dark blocks).
The finalist version passed at 8.0; this lock must not regress and must be implementable in shadcn/ui + Tailwind v4.

## Inputs (root = /Users/benq/Desktop/qnsc/opc/design)
- Build and Read ONE contact sheet: `cd ~/.claude/skills/uiux-studio/scripts && node shots.mjs <html> <root>/apps/app/shots
  --sizes 1440x900,390x844 --scale 0.5` for apps/app/screens/{home,counter,counter--payment}.html (payment: 390 only) and
  `node shots.mjs <root>/system/components/catalog.html <root>/system/shots --sizes 1440x900 --full --scale 0.5`;
  then `node sheet.mjs <root>/apps/app/shots/_eval-lock.png <the pngs> --cols 3 --width 2100`.
- Finalist baseline (compare against, one Read): <root>/system/directions/_final-desktop.png and _final-phone.png.
- Machine facts (use these, do not re-derive sizes from images): `node probe.mjs <screen> --size 1280x800 --stress --min-font 14`,
  `node probe.mjs <counter.html> --size 1024x768 --min-target 56`, `node a11y.mjs <each screen>`,
  `node status.mjs <root>/apps/app`.
- Max 2 full-res crops via `shots.mjs --selector`.
- Rubric: ~/.claude/skills/uiux-studio/references/evaluator-rubric.md (DQ×3, OR×3, CR×2, US×2; pass ≥ 8.0, no
  criterion < 7) + library/calibration.md + references/anti-slop.md.

## Questions
1. Did the calming polish land without losing F's signature (lanes, ladder, fill level = certainty)?
2. Regression vs the finalist baseline? Name it.
3. Catalog: is every component shown in every state (hover/focus/disabled/locked/pending/error)? Gaps?
4. Implementability: anything that cannot map to shadcn/Radix + Tailwind tokens without a snowflake?
5. Task walkthrough Counter (4-item cart → QR → pending → hand over) and Home ("is today's money real, what first?").

## Output (≤ 350 words)
```
LOCK v1.0  DQ x · OR x · CR x · US x → weighted  PASS|FAIL
REGRESSIONS vs finalist: …
TOP 5 FIXES (screen|catalog@size → what → why; mark [component] if the fix belongs in components.css)
CATALOG GAPS: …
IMPLEMENTABILITY: …
TASK WALKTHROUGH: Counter n steps · hesitation …; Home …
```

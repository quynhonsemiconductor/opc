# Context pack — OPC · Evaluator · Feature screens / states on locked system v1.1.0

You are a skeptical senior product designer. You did not make these. Do not praise; be specific.

## Product in 5 lines
OPC: web app (laptop + phone browser) for Vietnamese household businesses ("Hải sản khô Cô Hai", Nhơn Lý;
owner 58, son Phúc 29). Every screen answers "what do I do first?" and "is this money real?". Direction F
"Biển Chỉ Dẫn": numbered urgency lanes, payment ladder "ĐANG Ở ĐÂY", fill level = certainty (outline → blue
hatched/dashed = chờ xác minh → solid green = đã xác minh), one yellow action per view, calm (no big dark blocks).

## Inputs (root = /Users/benq/Desktop/qnsc/opc/design)
- Rules: <root>/system/DESIGN.md §4–§8 (skim). Content truth: <root>/system/BRIEF.md §10 (check numbers match).
- Shots exist in <root>/apps/app/shots/ (`<screen>-1440.png`, `<screen>-390.png`). Build ONE contact sheet of the files in
  your task with `cd ~/.claude/skills/uiux-studio/scripts && node sheet.mjs <root>/apps/app/shots/_eval-<group>.png <pngs…> --cols 4 --width 2400`
  and Read it. Downscaled text looks smaller than it is: judge sizes ONLY from probe output, never from the sheet.
  Max 2 full-res crops (`node shots.mjs <html> <scratch dir> --sizes 1440x900 --selector "<css>"`).
- Machine facts (use these): `node probe.mjs <html> --size 1280x800 --stress --min-font 14`, `node a11y.mjs <html>`,
  `node status.mjs <root>/apps/app` (look for ERROR / hard-coded lines for these files).
- Rubric: ~/.claude/skills/uiux-studio/references/evaluator-rubric.md (DQ×3, OR×3, CR×2, US×2; pass ≥ 8.0, no criterion < 7).

## Questions
1. Task walkthrough per screen (given in your task). Count steps; where does the owner hesitate?
2. Is the money state impossible to misread in every state? Any state that looks "done" before verified?
3. Consistency with the system: same components for the same job across screens; exactly one yellow action.
4. Content: numbers consistent with BRIEF §10 and with each other; Vietnamese natural; no repeated facts.

## Output (≤ 350 words)
```
<group> ROUND N  DQ x · OR x · CR x · US x → weighted  PASS|FAIL
PER FILE: <file> ok | issue (one line each)
TOP 5 FIXES (file@size → what → why; mark [component] if it belongs in components.css, [content] if BRIEF data is wrong)
WALKTHROUGH: …
```

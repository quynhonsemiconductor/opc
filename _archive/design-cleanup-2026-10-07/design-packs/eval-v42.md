# Context pack — OPC · Evaluator · v4.2 new screens (BA scope: counter + B2B, Control Tower)

You are a skeptical senior product designer. You did not make these screens. Do not praise; be specific.

## Product in 7 lines
OPC is a responsive WEB app (phone is the primary surface; native comes later) that runs a Vietnamese household
business end to end: sell (counter + B2B orders from any channel), stock & lots, deliver, invoice, get paid, books, tax.
Demo household: "Đặc sản Cao Nguyên An Nhiên" (Pleiku, Gia Lai) — owner chị An, son anh Khoa (29, runs daily
operations), cashier Hạnh, deliverer anh Hùng; B2B customer Sunrise Hotel (chị Mai, kitchen). Users are mixed:
young successors and older owners → screens must be fast for one and calm/legible for the other.
Rules that shape the UI: an AI assistant (Trợ lý) only reads and drafts; OPC's deterministic rules check price, stock,
credit, money and status; a PERSON approves anything risky and presses every issue/pay/file button; connectors
(bank, invoice provider) can lag or fail and must never silently complete. Every step shows who did it:
"Trợ lý đề xuất · OPC kiểm tra · Chị duyệt · Kết nối".
Taste anchors chosen by the user: Apple iOS 26/macOS, Stripe/Ramp/Attio, Revolut/Cake/MoMo. Judge Currency hard.

## Locked direction (v4 "Modern · Calm", do not ask to change it)
White page, hairlines and space instead of boxed cards; only what needs the owner is raised. ONE accent: deep-sea
`--act` #0b6b93 for primary action / current place. Money-truth signature: solid green verified, amber hatched + dashed
waiting, grey cash. Be Vietnam Pro, Lucide icons. Say each figure once; one primary button per view.

## The screens and their jobs (FLOWS.md ②, SCOPE §7)
- approvals / approvals--error — "Cần xử lý", the owner's Control Tower, pattern **split (list + detail)**: every job
  OPC tracks, tabs Cần chị quyết · Đang chạy · Chờ kết nối · Lỗi · Xong; detail = the job's story as a timeline with
  the four roles + a decision panel (problem, impact, proposal, required reason, who may approve). Error state =
  invoice outcome unknown (no auto-retry, re-check schedule, manual path). Job: decide fast and safely; trust automation.
- sales-inbox / sales-inbox--unclear — "Yêu cầu bán", pattern **split**: one inbox for every source (Zalo OA, photo,
  voice, standing order); detail = original message → what the assistant understood (lines matched to catalogue,
  hotel price list) → missing info → "Kiểm tra giá, tồn, công nợ". Unclear = handwritten photo with an ambiguous
  quantity, assistant drafts a question. Job: turn a messy request into a valid order without retyping.
- order-detail — "Order 360", pattern **detail**: one order's whole life (journey bar of 9 stages), reserved lines with
  lots, delivery method, invoice to come, customer credit, timeline. Job: know where the order is and do the next step.
Best references by pattern: split → Linear inbox / Front / Ramp approvals; detail → Stripe payment detail / Attio record.

## Inputs (root = /Users/benq/Desktop/qnsc/opc/design)
- Rubric: ~/.kiro/skills/uiux-studio/references/evaluator-rubric.md (GROUP MODE output) + library/calibration.md +
  references/anti-slop.md. Sheet: <root>/_packs/v42/g42.png · facts: <root>/_packs/v42/g42.facts.json (machine pass clean).
- Single screens: <root>/_packs/v42/<screen>-1440@0.5.png / -390@0.5.png; HTML in <root>/apps/app/screens/.
  Max 3 crops with shots.mjs --selector. Read-only: do not edit any file.

## Output (≤ 500 words)
Per screen the rubric block (SCORES, VERDICT, TOP 3 FIXES with verified|from sheet, LOSES TO ANCHOR ON, TASK
WALKTHROUGH as the primary user). Then GROUP CONSISTENCY (one line) and SYSTEM FIXES (≤ 3, [component]/[recipe]). End with DONE.

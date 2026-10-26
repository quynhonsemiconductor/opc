# Context for the Evaluator — OPC v5.1.0 "Features first"
Owner request: in onboarding and across Kết nối, show the MAIN FEATURES OPC supports (not providers). The household chooses which provider to use per feature (flexible);
features that need a provider to start are "Cần để bắt đầu" (required), the rest "Nên có" (suggested) / "Khi cần". 11 features group the 17 connector categories.
Interpretation of "require": the dependent flow is locked until a way is connected (e.g. no transfer payments, no wholesale orders) — the whole app is not blocked; cash at the counter works.
Screens: onboarding step 4/7 `onboard-features` (plan with OPC-suggested way, "Đổi"), `onboard-feature` (choose a way for one feature, "Nhờ nhân viên OPC nối giúp", "Sắp có" pills),
Kết nối tab "Việc OPC làm" `connections--category` (tiers, way in use, state), `connections--feature` (one feature), `readiness--new` (rows reworded feature-first).
Design system "Modern · Calm" v4; Vietnamese; fewer words/icons; healthy states are words; one primary per view. Rubric: ~/.claude/skills/uiux-studio/references/evaluator-rubric.md (group mode). Pass >= 8.0, no criterion < 7.
Inputs: m1/m1.png, m1/m1.facts.json. Verify claims on the real screens in apps/app/screens/. Return per-screen scores, the single most valuable fix, PASS/NEEDS_CHANGES, under 400 words.

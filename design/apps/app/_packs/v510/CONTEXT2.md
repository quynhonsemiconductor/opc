# Round 2 context — OPC v5.1.1 "OPC leads, providers are plain text"
Owner's point: the OPC app must show OPC's own features and brand, not advertise other apps or providers. Changes since round 1:
- No provider logos/monograms anywhere in household screens; provider names are plain text where the owner chooses or manages them (Kết nối, chooser, hand-off page).
- Kết nối tabs: Đã nối · Việc OPC làm · Nhật ký. The 71-provider directory is now "Thêm cách nối" (connections--add), grouped by FEATURE, reached from Việc OPC làm; it is no longer a tab and no longer provider-led.
- Hub rows (connections--category) lead with the feature and its state; the provider is a small grey note. Onboarding plan says "OPC chọn sẵn: <way>" in regular weight.
- Shared chrome (health tooltip, onboarding proof/bank page) no longer names Casso / Hilo / X Invoice outside Kết nối (brand.py).
Rubric: ~/.claude/skills/uiux-studio/references/evaluator-rubric.md (group mode), pass >= 8.0, no criterion < 7. Also judge: does OPC's own voice lead, and are third parties never the headline?
Inputs: <group>/<group>.png + .facts.json. Real screens: apps/app/screens/*.html. Verify every claim. Return per-screen scores, the one most valuable fix, PASS/NEEDS_CHANGES; under 350 words.

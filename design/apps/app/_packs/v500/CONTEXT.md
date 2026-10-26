# Context for the Evaluator — OPC v5.0.0 "Kết nối: full catalog + credentials"

OPC = responsive web app (phone first) running a Vietnamese household business. Users: chị An (owner, older), anh Khoa (operator). Design system "Modern · Calm" v4
(`system/DESIGN.md`, tokens, components). Language: Vietnamese; fewer words, fewer icons, aligned columns, clear hierarchy, no "AI slop".

What was asked (CEO): one connections page that SHOWS EVERY provider option (he may remove some later if a partnership fails), with add / manage / remove,
how a token or API key is handled, and a guide per provider. Zalo personal accounts are not connectable (Zalo has an OA API only) and are excluded.

Design decisions to judge (not to re-litigate the business):
- Three credential custody modes: **Nối qua Casso** (secret typed on Casso's Cas Link page, OPC never sees it), **Cho phép** (OAuth-style consent), **Dán khoá** (key pasted into OPC, kept masked, 4 last chars, rotate/remove), plus "Mở app" and "Cần đăng ký".
- Directory (`connections--add`): 71 providers in 9 purpose groups; connectable ones are tiles, "Sắp có" ones are pills (press = "Báo tôi"); never a fake connect button.
- Platform console (QNSC) `platform-*`: registry of providers, platform keys for Casso, hide vs remove with a required reason (starts empty). Shows counts only, never households.
- Healthy states are words (icon only marks what needs the owner). One primary button per view. OPC never signs, files, pays or moves money.
- Guide steps for third-party portals are written from general knowledge (flagged in NOTES; the mock says they may differ).

Rubric: `~/.claude/skills/uiux-studio/references/evaluator-rubric.md` (group mode). Pass ≥ 8.0, no criterion < 7. Budgets and probe/a11y facts are in `<group>.facts.json`.
Inputs per group: `<group>.png` contact sheet (desktop + phone per screen, then the anchor and a reference) and `<group>.facts.json`. You may open the real screens in
`apps/app/screens/*.html` and screenshot them. Verify every claim you make against the screen.
Return: per screen the scores (Design quality, Craft, Originality, Functionality — as in the rubric), the 3 most important fixes, and PASS or NEEDS_CHANGES.

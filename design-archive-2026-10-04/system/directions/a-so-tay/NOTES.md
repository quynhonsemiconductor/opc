- Idea: the household's paper ledger made precise. Ruled hairlines and right-aligned money columns, no cards; totals get the bookkeeper's double underline.
- Fonts: Source Serif 4 for money and headings (editorial serif like Square's, real tabular lining figures, still legible at 16–20px) + Public Sans for UI (neutral humanist sans). Both have the Vietnamese subset.
- Colours: paper #faf8f3, blue-black ink #172033, muted ink #4e5563, rule line #d8d2c4. ONE vermilion seal #b8321a, used only for "đã xác minh". Errors use earth brown #8f4a0e on #f5e8d4 with a ⚠ icon. The primary button is ink, so the seal stays rare.
- Signature: the verification STAMP. Verified money gets a slightly rotated double-ruled vermilion seal "ĐÃ XÁC MINH"; pending money gets an empty dashed outline "chờ xác minh". It is used inline in the ledger column.
- Self-score 7/10: ledger restraint and the stamp read well. Weak points: the brown error and the vermilion seal sit close in hue; the uppercase stamp at 13px is on the small side; the bottom of the meta column is underused; the overall feel leans formal.

## Finalist round 1 (02/10/2026) — Home + Counter
Files: tokens.css (3 tiers: --p-* → semantic on :root → component tokens on .btn/.stamp/.trail/.tag/.ledger/.slip/.ptile/.nav-item), base.css, home.html, counter.html, counter--payment.html, shots/.
- Seal fixed: "ĐÃ XÁC MINH" is now 16px bold caps (18px in .stamp-lg), 36–44px tall, tilt −1.5° (was 13px, −3°). Verified line carries the sync time: "ĐÃ XÁC MINH | 10:43" (MB last update, 2 min before 10:45). Pending = same-size dashed empty outline, sentence case, clock icon, no tilt.
- Error/attention is now turmeric #7a5300 on #f7eecf with a triangle icon (hue ~40°, clearly yellow-brown against the vermilion seal). A real "Lỗi" is a solid turmeric block with an octagon icon.
- Money trail (borrowed): three ruled boxes beside amounts — dashed = waiting, ink = done, vermilion = verified. Expanded as labelled steps on the payment panel.
- Owner-voice sentence (borrowed), serif italic, above key figures: Tiền hôm nay, Thuế, Thu tiền. Exact figures stay underneath.
- Doanh thu 8.460.000 ₫ always shows "trong đó 1.380.000 ₫ còn chờ xác minh"; today's 7-day bar has a hatched pending part.
- Counter: sans for product tiles (ruled grid cells), serif only for totals. Ticket = white receipt slip, zigzag only at top/bottom, with the stamp line at the foot. 3 panes at ≥1240 (products · slip · payment), 2 at 1024, list + sticky bar on 390 → counter--payment.html sheet. Touch targets 56px.
- Probe/a11y: 0 issues at 1440/1024/390 and on 1280 stress; axe 0 violations.
- Known weak: counter's full app nav is behind a menu (focused mode); payment pane needs scrolling at 900px for the cash block; 7-day day labels add dates not in the brief (T7 26/9 …).

## Round 2 (evaluator round 1: 7.3 FAIL)
- Home: date H1 cut to 24px and the header rule is now a hairline. Money now reads first: the "Tiền hôm nay" title is 30px, the hero figure 56px, and the owner sentence 20px. At 390 a money brief (sentence, 8.460.000 ₫, 1.380.000 ₫ chờ xác minh with trail, 23 đơn) now sits above "Mở quầy bán hàng". The phone header name truncates (with a title attribute); the avatar is 36px inside a 44px target.
- Demoted 7-day, Trợ lý, Công nợ and Đơn gần đây with `.sec-minor`: hairline head, 20px title, lighter bars and amounts. Stamp is now 18px/40px with a 20px icon; trail boxes are 13px.
- Counter: --text-min raised to 14 (kbd, badges). The ticket is wider at 1440 (448px) with 18–20px lines, 16px meta and a 40px total. In-cart tiles use the same 4px left ink bar as the selected ticket line (no box).
- Counter 390: the sticky bar now shows a line summary of the cart. In-cart rows are paper-coloured with a left bar and quantity badge.
- Payment 390: the bank details collapse to the amount plus "VietQR · MB · nội dung DH1043". Under the pending stamp: "Đã nhận · chờ xác minh — giao hàng được vì dưới mức 2.000.000 ₫ bạn đặt". The disabled "Xác nhận đã thu" now says what unlocks it (lock icon). "Huỷ đơn" is turmeric with a trash icon, set apart from "Lưu tạm". The receipt slip is collapsed. The hesitation copy is above the fold at 390x844. The desktop counter got the same copy and button changes.
- Machine pass: probe 0 issues at all sizes and stress, min-font 14 clean; axe 0 violations.

## Round 3 (evaluator round 2: 7.8 FAIL — last round)
- Payment 390: the sticky footer now holds only the state line (trail + "Chờ khách chuyển · nút tự mở khi MB báo tiền vào"), a rule and the disabled primary. Secondary actions are one row, "Đổi sang tiền mặt · Lưu tạm · Khác…"; "Huỷ đơn…" sits inside the Khác… menu with destructive styling (the "…" means a confirm dialog). The cash block is now a closed details. Steps are quieter. The hesitation copy and the action row are above the fold at 390x844, and the body has bottom padding so nothing hides under the footer.
- Home 1440: Cần xử lý item 1 is now a featured row (raised paper, ink bar, 20px serif title, 20px amounts). Items 2–6 are quieter (500 weight, grey numbers, rule-border buttons). Minor sections are demoted further: 18px grey headings, 10px bars, grey table cells.
- Counter 1440: one line of copy per block (say, next state, unlock, VAT note, invoice meta, stamp line). The QR side is collapsed to amount + "VietQR · MB · nội dung DH1043". The pending stamp is 20px/52px. The kbd row is quieter. Same Khác… menu as the sheet; the cash block is collapsed.
- Counter 390: the cart bar summary is one ellipsised line, "Mực khô 0,5 kg · Cá cơm ×2 · +2 món" (full text in title), and the bar is about 84px. Product rows are 56px with no empty gaps.
- Home 390: header shows "Cô Hai". The date is a 16px sans line. Money figure is 48px with the pending part under it, then the owner sentence at body size, then 23 đơn.
- Machine pass: probe 0 issues (incl. stress at 1280 and 390, min-font 14), axe 0 violations.

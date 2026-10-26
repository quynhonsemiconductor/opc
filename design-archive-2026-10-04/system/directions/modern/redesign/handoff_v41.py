"""Prepend a 'v4.1 (current)' block to hand-written handoffs whose intent text predates the v4.1 restructure.
Idempotent (replaces its own block). Data / API sections below stay valid; layout text below is historical."""
import pathlib, re
H = pathlib.Path(__file__).resolve().parents[4] / 'apps' / 'app' / 'handoff'
COMMON = ('Layout and parts follow DESIGN.md §3 (v4.1). Primary = sea `--act`, one per view; money states use the '
          'truth palette. The "Layout" / "Primary action" text further down is v3 history — where it mentions yellow '
          'buttons, c-msign, c-lane or c-truthbar, this block wins. Data and API sections below are still valid.')
V = {
 'money': ('Show which money is real; resolve what needs the owner.',
   'The verified amount (72px hero, "Đã xác minh · 4 khoản · khớp sao kê MB"). The legend item for verified says "= số lớn ở trên" (said once).',
   '"Gán đơn" on Cần xem #1 (opens money--assign). #2/#3 are quiet.',
   '1440: hero + facts (Số dư MB, Tiền mặt trong ca) | flat "Cần xem" panel; truth bar + legend links (Chờ xác minh → list, Chưa gán → assign); ledger rows with tabs. 1024: facts wrap under the hero. 390: one column, hero → Cần xem → ledger.',
   'money--assign: dialog with the best match (`c-option--best`, "Nên chọn"), "Cách khác", folded "Không chọn được"; footer previews the result; focus trapped.'),
 'orders': ('Today\'s orders and which ones need the owner.',
   '"Đã thu hôm nay 8.460.000 ₫" — the only figure; truth bar under it.',
   'None in the head; "Chưa thu · 2 đơn · 1 quá hạn / 5.570.000 ₫ ›" is a neutral link tile to the filtered list (pairwise pick A, 8.2).',
   '`r-listhead` → tabs (Cần xem · Chờ xác minh · Chưa thu · Hoàn tất · Hôm nay · Tất cả) → search/filters → 5-column table: Khách·đơn (`c-table__who`), Thanh toán, Trạng thái (labelled pill), Hoá đơn, Tổng. 390: rows stack.',
   '9 states share this head (search, filters, daterange, filtered, noresult, bulk, bulk--preview, peek, loading).'),
 'order-detail': ('One order: status, money, customer, what happens next.',
   'Title DH-1040 + total 3.420.000 ₫ under it.',
   '"Xác nhận đơn"; "In phiếu" outline; "Huỷ đơn" ghost red.',
   '`r-detail__head--calm` → debt banner (amber) → facts | Diễn biến timeline at ≥1180; lines table; Thanh toán. 390: actions grid (primary full row).', ''),
 'invoices': ('This period\'s e-invoices and the one that needs attention.',
   '"7.080.000 ₫" for the month; truth bar có mã 18 · chờ mã 1.',
   '"Gửi lại" in the amber banner for HĐ 00000418.',
   '`r-listhead` (due tile is a neutral link "HĐ 00000418 · 640.000 ₫") → banner → tabs → 5-column table; CQT code shows its tail "…0421" (full code for SR + title).',
   'invoices--accountant: compact density, 25 per page, rejected = `c-split__err`.'),
 'invoice-detail': ('Why an invoice has no tax code yet, and resend it.', 'Number + 640.000 ₫ under the title; amber "chờ mã CQT · 25 phút".',
   '"Gửi lại ngay"; PDF / Zalo outline.', '`r-detail__head--calm` → banner → invoice facsimile | Diễn biến (event text leads, time is meta).', ''),
 'receipt': ('Print or send the receipt for a paid order.', '1.020.000 ₫ + verified pill "Đã xác minh · QR".',
   '"In phiếu"; PDF / Zalo outline.', 'Receipt facsimile | Zalo message preview (links in brand ink).', ''),
 'approvals': ('Approve what the assistant or staff prepared.', 'Task #1 (flat raised panel) with "Sau khi duyệt" consequence line.',
   '"Duyệt" on #1 only.', 'Queue at `--read-w` (880): `c-task` hairline rows; tabs by type.', ''),
 'audit': ('What happened today, by whom.', 'Day heading + the feed; the event text leads, the time is meta (tabular).',
   'None (read view).', '`r-feedbar`: time segment + "Ai làm: Tất cả" menu on one row, then "Việc" chips; dot key; `c-timeline` (ok · pend · ai = assistant draft, hatched · you = ink · system = hollow).', ''),
 'settings-display': ('Text size, mode, contrast — preview live.', 'Size picker (`c-sizepick`, selected = sea) + live preview.',
   'None (auto-saves: "Tự lưu · áp dụng ngay").', '`r-settings` groups (hairline + space) | preview.', ''),
 'settings-features': ('Turn modules on/off; see what is coming.', 'Group "Đang dùng · 3".',
   'Switches (`c-switch--row` with state pill).', 'Groups "Đang dùng" and "Sắp có" (recede, no switch); "Bắt buộc" shows only the lock pill.', ''),
 'settings-users': ('Who uses the shop and what each can do.', 'Member rows with role and verification.',
   '"Mời người dùng".', '`r-settings` groups: members; "Ai làm được gì" matrix (scroll region, focusable). --otp: confirm dialog, focus trapped.', ''),
 'onboarding': ('Sign up in ~15 minutes, 6 steps, autosaved.', 'Per step: the title question; on ≥1180 the right panel (step map, or the sample proof card on welcome/done).',
   'The sticky forward button (one per step); helpers are links.',
   '≥1180 two columns (form ≤560 | panel ≤400). <1180 one column + compact strip (current step, why, minutes left). Household is one question "Đây có đúng hộ của chị?" with OPC-prefilled rows; welcome shows the sample proof ("Ví dụ"); bank shows MB → Casso → Quầy OPC read-only; products--review folds the 7 sure items; done folds the recap and leads with reviewing 2 AI-uncertain prices.',
   'Generators: `system/directions/modern/redesign/onboard_aside.py` (panel) then `inert.py` (help dialog).'),
}
TAG = ('<!-- v41:start -->', '<!-- v41:end -->')
for name, (purpose, first, primary, layout, extra) in V.items():
    p = H / f'{name}.md'
    if not p.exists():
        print('missing', name); continue
    s = re.sub(r'\n?<!-- v41:start -->.*?<!-- v41:end -->\n', '\n', p.read_text(), flags=re.S)
    block = (f'{TAG[0]}\n## v4.1 (current)\n> {COMMON}\n\n- **Purpose:** {purpose}\n- **First read:** {first}\n'
             f'- **Primary action:** {primary}\n- **Layout:** {layout}\n' + (f'- **Also:** {extra}\n' if extra else '') + f'{TAG[1]}\n')
    lines = s.split('\n', 1)
    p.write_text(lines[0] + '\n\n' + block + (lines[1] if len(lines) > 1 else ''))
    print('ok', name)

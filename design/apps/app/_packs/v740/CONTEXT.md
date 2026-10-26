# v7.4.0 · Tiền (đợt 4) — context for the evaluator

Product: OPC, phone-first web app for Vietnamese household businesses that buy goods to resell. Demo An Nhiên, Pleiku; owner chị An; business bank account MB 0901 2345 678 (notified to tax). Today 06/10/2026.
Rules these screens must show:
- OPC never moves money. It reads the bank feed (if connected) or the owner's confirmation, proposes a match, the owner confirms. "Chờ xác minh" = bank notification seen, not yet in the statement.
- One transfer may pay several invoices (oldest first, editable). Underpayment leaves the rest as debt.
- Overpayment → "tiền khách trả trước" (customer credit, not revenue, offsets the next order) or refund by the owner.
- Possible duplicate (same sender, amount, memo, < 10 min, one copy missing from the statement) → owner decides; nothing deleted silently; everything logged.
- Cash: counted once a day (no shift close); total is enough, no denominations; difference needs a reason + owner approval.
- Customer statement (bảng kê): Agent drafts, owner sends via Zalo OA; includes QR of the household account.
- Credit limit is information only, never blocks an order (customer-detail).
- Handwritten delivery note: photo + manual entry (no OCR in pilot), matched against PO and receipt; the photo is evidence, not an invoice.
Score each screen 0–10 on: task clarity, business correctness, hierarchy, consistency with the rest of OPC, phone fit, copy (Vietnamese, plain). Target ≥ 8.0, no criterion < 7.

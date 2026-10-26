# Handoff — Gán tiền (v7.4.0): một lần trả nhiều hoá đơn · trả dư · có thể trùng

- Source: bank feed (if connected) or the owner's confirmation. OPC proposes, the owner confirms; OPC never moves money.
- **Split** (`money--split`): transfer + suggested allocation table (oldest invoice first; editable inputs; footer total must equal
  the transfer). Underpaid → oldest first, rest stays as debt. Result line names the invoices/orders that close.
- **Overpay** (`money--overpay`): extra → "tiền khách trả trước" (customer credit, not revenue, offsets the next order on
  confirmation) or refund by the owner through her bank app (OPC records the payout).
- **Duplicate** (`money--duplicate`): same sender, amount, memo, < 10 min, one copy missing from the statement → owner picks;
  "Bỏ" hides from Thu chi but keeps it in Nhật ký; "Để sau" keeps it in Cần xem.
- **Cash** (`money--cash`): count once a day, total only; expected = opening float + cash sales − cash expenses; a difference
  needs a reason and owner approval; deliverer COD hand-ins are logged with person + time.


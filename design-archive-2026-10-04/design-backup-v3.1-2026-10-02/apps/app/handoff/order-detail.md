# Handoff — Chi tiết đơn (order-detail) · DH-1040

- Content: BRIEF §13.3. Recipe `r-detail`. Primary: **Xác nhận đơn**.
- The banner above the content shows the debt **after** this order (6.570.000 ₫, of which 3.150.000 ₫ is overdue),
  so confirming is an informed decision. Debt limits per customer are an open question.
- **Main column:** customer facts (c-kv), the lines table with a total row (`c-table__row--sum`), the payment line
  with c-moneyline. **Side column:** c-timeline of order events (the Zalo message, created by the assistant and
  checked by Phúc) and the post-confirm note.
- **Huỷ đơn** is destructive: confirm with a dialog (not drawn).
- **In phiếu:** prints a delivery slip.

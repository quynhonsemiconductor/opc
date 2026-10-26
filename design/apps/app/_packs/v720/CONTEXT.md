# v7.2.0 · Mua hàng (đợt 2) — context for the evaluator

Product: OPC, phone-first web app for Vietnamese household businesses (hộ kinh doanh) that buy goods to resell. Demo: An Nhiên, Pleiku; today 06/10/2026 10:45.
Users: owner chị An (decides), operator anh Khoa (counts goods). Design system "Modern · Calm" v4.

Business rules these screens must show (research: Odoo / QuickBooks / KiotViet patterns + VN invoice rules):
- One purchase record = 4 sections: Hàng mua · Nhận hàng · Chứng từ · Tiền đã trả, plus a timeline (Diễn biến).
- Receiving, documents and money are independent tracks (`r-tracks`), never one stepper.
- Stock rises once, by the counted quantity, when the owner confirms. Short delivery → choose: wait for the rest (receive again on the same order) or close short.
- Payments: several per order, before or after receipt; buying on credit has a due date. OPC never moves money (optional QR of the supplier opens the owner's bank app).
- Supplier invoice differs from received goods → the seller issues the adjustment invoice; the household keeps evidence. Legal detail awaits the accountant.
- Agent may propose a purchase; the owner approves before anything is sent.
- Return to supplier: stock out (not a sale), supplier owes back / offset next purchase.
- Expenses outside stock never go into cost of goods.

Screens: purchases (list) · purchase-detail (MH-0121 ordered, half prepaid) · purchase-detail--receive (MH-0118 counted 45/50, invoice says 50) · purchase-detail--received (after confirm, 5 still open) · purchase-detail--pay (MH-0109 second partial payment) · purchase-new (Agent proposal MH-0122) · purchase-return (TH-0003, 1 bag torn) · purchases--expense (expense photo dialog).

Score each screen 0–10 on: task clarity, business correctness, hierarchy, consistency with the rest of OPC, phone fit, copy (Vietnamese, plain). Target ≥ 8.0, no criterion < 7.

# v7.3.0 · Bán hàng (đợt 3) — context for the evaluator

Product: OPC, phone-first web app for Vietnamese household businesses (buy goods to resell). Demo An Nhiên, Pleiku; owner chị An, deliverer anh Hùng.
Business rules these screens must show (BA verdicts + Vietnamese invoice rules):
- One sales order = sections (Hàng bán · Giao hàng · Hoá đơn · Tiền) + Diễn biến; 4 independent tracks Đơn · Giao · Hoá đơn · Tiền (`r-tracks`), never one stepper.
- Confirm only within available stock; goods are held at confirm; stock goes out ONCE when "Đã giao" (delivered in full). Leftover = a new order.
- One e-invoice per order, issued at "Đã giao"; buyer info (company + MST) captured on the order. An invoice rejected by the tax authority (no code yet) is fixed and resent — no adjustment invoice needed; only the invoice track turns red.
- Customer return: household is the seller → household issues the adjustment invoice (rule awaits accountant); stock back in if good; receivable reduced.
- Credit is information only (never blocks an order). Agent drafts, owner confirms.
- "Bán nhanh" replaces the old counter + shift close: walk-in sale, handed over and paid at once → still one order record; QR to the household's own account; OPC never moves money; cash counted in Thu chi và đối chiếu.
- onboard-firstsale: guided test sale built on Bán nhanh QR step (not revenue).

Screens: order-detail · order-detail--invoice (delivered + invoiced) · --invoice-error · --return · quick-sale · quick-sale--qr · quick-sale--done · delivery--pick · onboard-firstsale.
Score each 0–10 on: task clarity, business correctness, hierarchy, consistency with the rest of OPC, phone fit, copy (Vietnamese, plain). Target ≥ 8.0, no criterion < 7.

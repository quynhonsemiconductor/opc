# Handoff — Cần xử lý → Việc chờ duyệt (approvals)

- **Purpose:** the owner side of the Agent Control Tower. Everything the assistant, the bank feed or the system
  drafts waits here until the owner approves it (principle: "OPC drafts; the owner approves").
- **Card (`c-task`):** source (Trợ lý / Ngân hàng / Hệ thống) · time · title + amount · evidence (original message,
  photo, bank line) · "Sau khi duyệt" consequence · actions (approve / edit / reject).
  - Only the first card carries the yellow action.
  - Approving writes an audit entry and runs the side effects through the outbox.
- **Tabs:** Chờ chị duyệt · Cảnh báo · Đã xử lý hôm nay.
- **Order:** money first, then orders, purchasing, tax, then alerts.
- **States not drawn:** empty ("Không có việc chờ duyệt"), a rejected item with its reason, and an expired draft.

# v7.5.0 · Sổ và kê khai (đợt 5) — context for the evaluator

Product: OPC, phone-first web app for Vietnamese household businesses (hộ kinh doanh) that buy goods to resell; 2026 rules: households self-declare revenue on eTax (no presumptive tax), quarterly filing; books per TT 152/2025; documents kept 10 years. Demo An Nhiên; accountant chị Lan; quarter III/2026 (deadline 31/10).
BA verdicts these screens must respect:
- In the pilot OPC NEVER shows a computed tax amount. It shows revenue by quarter (invoices + sales without invoice), the year-to-date total vs revenue thresholds (versioned rule data, conflicting values 200 triệu / 1 tỷ, waiting for the accountant), a filing guide with "không phải tư vấn thuế".
- OPC has no eTax connection: the owner files on eTax herself (VNeID level 2), then records the eTax notices: tiếp nhận (received) → chấp nhận (accepted). Tax payment is done by the owner; OPC only records it.
- Period: reconcile 3 sources (delivered revenue, issued invoices, tax portal invoices, money) → lock the period; changes after lock = amendment, logged append-only.
- Annual revenue notice and bank-account notice are mandatory items (form/deadline awaiting the accountant).
- Evidence pack: books, e-invoices, bank statement, purchase documents, lock record, eTax notices, change log.
Screens: tax (quarter overview) · tax--return (6-step eTax guide) · tax-file (sent, received notice) · tax-file--signed (accepted) · tax-evidence · period (reconcile, 2 open) · period--ready (all matched) · books (revenue book).
Score each screen 0–10 on: task clarity, business correctness, hierarchy, consistency with the rest of OPC, phone fit, copy (Vietnamese, plain). Target ≥ 8.0, no criterion < 7.

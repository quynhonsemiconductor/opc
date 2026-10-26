# ADR 0005 — River jobs with transactional outbox and webhook inbox

Status: Accepted · 2026-10-01

## Context
Provider calls (invoices, notifications), webhook processing, invoice-status polling, reminders and
PDF generation must be durable and exactly-once in effect. Casso webhooks are unsigned and retried up to
17 times; INVOICE/TVAN webhooks only 3 times.

## Decision
- **River** (Postgres-backed job queue): jobs are inserted in the same transaction as business data
  (`InsertTx`), so they exist iff the transaction commits.
- **Outbox** for all external effects; **inbox** for all inbound webhooks: persist raw payload with a
  dedup key, return 200, process asynchronously; unknown `grantId` → quarantine, never guess.
- Scheduled polling jobs replace unreliable webhooks (e.g. invoice tax-code status).

## Consequences
No extra broker to operate; Postgres is the single source of truth for business state and work.

## Revisit when
Event fan-out to many consumers or cross-service streaming is needed → add a broker behind the outbox.

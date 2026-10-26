# ADR 0004 — PostgreSQL 18, shared schema with RLS, tenant-keyed data, decimal money

Status: Accepted · 2026-10-01

## Context
Thousands of tenants now, possibly hundreds of thousands later. Tenant isolation failures leak financial
data. Schema-per-tenant breaks migrations and connection pooling at this tenant count.

## Decision
- PostgreSQL 18 (+ pgvector), single shared schema per module (Postgres schemas = modules).
- Every tenant table: `tenant_id` in the primary key and all unique indexes; `ENABLE` + `FORCE ROW LEVEL
  SECURITY`; policy on `current_setting('app.tenant_id', true)::uuid` (fails closed). Tenant context set
  with `SET LOCAL` inside the request transaction only.
- The app connects as a non-superuser, non-BYPASSRLS role; a deploy gate verifies it after migrations.
- Money in `numeric`; totals derived from lines; statuses that can be derived are not stored.
- Large append-mostly tables (orders, payments, invoices, journal) designed for monthly partitioning.
- Hand-written SQL migrations (goose); sqlc for queries.

## Consequences
Tenant-keyed design keeps sharding by tenant/province possible without key changes.
Cross-tenant aggregates (B2G) go through dedicated read models, never by bypassing RLS.

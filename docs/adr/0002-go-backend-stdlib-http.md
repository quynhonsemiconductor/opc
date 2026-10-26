# ADR 0002 — Backend in Go 1.27 with net/http + oapi-codegen, no web framework

Status: Accepted · 2026-10-01

## Context
OPC handles money, tax and invoices for a government programme, must run 24/7 for many years and may
grow from 5k to 100k+ households. The decisive criteria were long-term stability (avoid forced
migrations), efficiency at scale, explicit correctness for money/tax, and simple operations. NestJS
was the main alternative.

## Decision
- **Go 1.27**. HTTP via standard `net/http` (method/path routing) with **oapi-codegen** strict-server
  interfaces generated from `shared/contracts/openapi.yaml`.
- Middleware as plain `func(http.Handler) http.Handler`: recover, request id, slog, OpenTelemetry,
  auth, tenant context, rate limit (Valkey), idempotency, OpenAPI request validation.
- Constructor injection wired in `main.go`; no DI framework, no reflection magic.
- Libraries: pgx v5.9.2+ (CVE-2026-41889 fixed) + sqlc, goose, River, valkey-go, `cockroachdb/apd`
  (or shopspring/decimal), Anthropic Go SDK, MCP Go SDK, testcontainers-go. `chi` allowed if route
  grouping is wanted (100% net/http compatible).

## Consequences
- Go 1 compatibility promise and few dependencies minimise upgrade churn; small static binaries.
- More boilerplate than NestJS; no shared TS types with web — OpenAPI codegen covers it.
- Org TS packages (`@quynhonsemiconductor/*`) are not reused (deliberate; recorded here).

## Alternatives rejected
NestJS (ecosystem churn, higher resource use, decorator/DI pitfalls seen in SoloDesk); Echo/Gin (own
Context types → lock-in); Fiber (fasthttp, not net/http compatible); Rust (velocity, hiring).

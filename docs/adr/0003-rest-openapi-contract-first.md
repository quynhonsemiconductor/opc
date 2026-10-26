# ADR 0003 — REST + OpenAPI 3.1 contract-first; no gRPC now

Status: Accepted · 2026-10-01

## Context
Clients: browsers (web SPAs), native iOS/Android (via KMP), public pages, and inbound third-party
webhooks. There are no internal service-to-service calls (monolith).

## Decision
- `shared/contracts/openapi.yaml` is the source of truth; it generates the Go server interfaces, the
  TypeScript web client and the Kotlin client used by the KMP core.
- Versioned paths (`/v1`), RFC 9457 problem+json errors, `Idempotency-Key` on writes, cursor pagination.
- Realtime via SSE (web) and push (FCM/APNs). No WebSocket until a bidirectional need exists.
- CI: breaking-change check on the spec (OpenAPI diff) and contract tests against the server.

## Consequences
One contract for four consumers; JSON over HTTP is debuggable on poor rural networks and cacheable.

## Revisit when
Internal services appear with high-volume calls → ConnectRPC (gRPC + HTTP/JSON) for internal APIs only.

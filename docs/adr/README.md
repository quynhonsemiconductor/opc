# Architecture Decision Records

| ADR | Title | Status |
| --- | --- | --- |
| [0001](0001-modular-monolith-monorepo.md) | Modular monolith in one monorepo | Accepted |
| [0002](0002-go-backend-stdlib-http.md) | Backend in Go 1.27 with net/http + oapi-codegen, no web framework | Accepted |
| [0003](0003-rest-openapi-contract-first.md) | REST + OpenAPI 3.1 contract-first; no gRPC now | Accepted |
| [0004](0004-postgres-rls-multitenancy.md) | PostgreSQL 18, shared schema with RLS, tenant-keyed data, decimal money | Accepted |
| [0005](0005-river-jobs-outbox-inbox.md) | River jobs with transactional outbox and webhook inbox | Accepted |
| [0006](0006-native-mobile-kmp-core.md) | Native mobile (SwiftUI + Jetpack Compose) with a Kotlin Multiplatform shared core | Accepted |
| [0007](0007-web-surfaces-astro-spa.md) | Web surfaces: one Astro public site + React SPAs; no Next.js | Accepted |
| [0008](0008-offline-sync.md) | Offline sync: client outbox first, PowerSync-compatible schema | Accepted |
| [0009](0009-hosting-aws-first.md) | Hosting: AWS first, with a data-residency plan and on-prem portability | Accepted |
| [0010](0010-ai-provider-agnostic.md) | AI: provider-agnostic LLM port, Claude + GLM now, self-hosted later | Accepted |
| [0011](0011-identity-access.md) | Identity, access and owner identity verification (eKYC) | Accepted |
| [0012](0012-finance-integrations-casso.md) | Finance integrations through ports; Casso as the first provider | Accepted (provider under evaluation) |

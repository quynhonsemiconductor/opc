# OPC — Solution Architecture

> Status: **accepted direction, v0.1 (2026-10-01)**. Decisions are recorded as ADRs in `docs/adr/`.
> Open items are listed in §12 — none of them blocks starting the foundation work.

## 1. What OPC is

OPC ("Doanh nghiệp một người ứng dụng AI") is a multi-tenant platform that lets Vietnamese
**household businesses (hộ kinh doanh)** and one-person companies run sales, payments, invoicing,
stock, books and tax on a phone, with an AI assistant. First rollout: the Gia Lai *Kế nghiệp số*
programme (successors aged 25–40; food & specialties, tourism, agriculture; many owners elderly,
phone-only, weak network).

| Horizon | Households | Notes |
| --- | --- | --- |
| Pilot | 5–10 | Q4/2026 |
| Target v1 | **3,000–5,000** | design point for this document |
| Programme | ~32,500 (Gia Lai) | provincial rollout |
| Platform | 100k+ | other provinces — must be reachable **without a rewrite** |

Users: household owner (often elderly; the successor does the paperwork), staff/family members,
delegated accountant, programme officers (B2G), buyers (public QR trace page).

## 2. Principles

1. **Right-size, but never paint into a corner.** Modular monolith now; module boundaries,
   tenant-keyed data and contract-first APIs so any module can be extracted later.
2. **The household is always in control.** OPC drafts; the owner approves. OPC never signs,
   files, pays or moves money on the owner's behalf (programme rules N-06/N-07).
3. **Deterministic rules own money, tax, stock and status.** AI explains, drafts and
   classifies; it never decides a number.
4. **Tenant isolation is enforced in the database** (RLS, fail-closed), not only in code.
5. **Integrations are ports, providers are adapters.** No business logic depends on Casso, a
   bank, an e-invoice provider or an LLM vendor directly.
6. **Offline is a first-class state** for the counter sale.
7. **Every number is traceable** to a bank transaction id, invoice number or ledger entry.

## 3. Capacity design point (estimates, not measurements)

| | 5k households | 50k | 500k |
| --- | --- | --- | --- |
| Peak order writes/s | ~100 | ~1,000 | ~10,000 |
| Connected devices (sync/realtime) | ~15k | ~150k | ~1.5M |
| Data growth/yr (orders+invoices+journal) | ~0.5 TB | ~5 TB | ~50 TB |

At v1 one Postgres primary + replica is ample. The paths to 50k–500k are: read replicas →
monthly partitioning of large tables → tenant-keyed sharding (every key already carries
`tenant_id`) → extracting hot modules. None requires changing the language or API style.

## 4. System overview

```text
 iOS (SwiftUI) · Android (Compose)   Web SPAs: app (owner/accountant) · gov · console   site (Astro: landing + QR)
        └── KMP shared core ──┐                    │                                 │
                              └────── HTTPS REST (OpenAPI 3.1), SSE, push ─────────────┘
                                               │
                      AWS: CloudFront + WAF → ALB → ECS Fargate (Graviton)
                                               │
        ┌──────────────── opc-api (Go modular monolith) ──────────────────┐   opc-worker (same binary,
        │ identity·tenant │ catalog·stock │ sales·order │ payment·recon     │   River jobs: outbox relay,
        │ invoicing │ tax·books │ booking │ procurement │ traceability      │   webhook inbox, invoice
        │ connectors (ports + adapters: Casso, …) │ assistant │ program/B2G │   status polling, sync,
        │ notifications │ audit journal │ consent & data-protection         │   reminders, PDFs)
        └──────────────────────────────┬──────────────────────────────────┘
          RDS PostgreSQL 18 (RLS, pgvector) · ElastiCache Valkey · S3 + KMS · Secrets Manager
          External: Casso Cas API · e-invoice providers · Zalo OA/ZNS · FCM/APNs · LLM gateway → Claude / GLM
```

Two processes from **one Go binary** (`api`, `worker`). A separate deployable is added only with
evidence (security boundary, independent scaling, different runtime).

## 5. Technology choices (summary)

| Layer | Choice | ADR |
| --- | --- | --- |
| Architecture | Modular monolith, monorepo | 0001 |
| Backend | **Go 1.27**, `net/http` + **oapi-codegen** strict server, no framework, constructor DI | 0002 |
| API | **REST + OpenAPI 3.1, contract-first**; SSE for realtime; no gRPC now | 0003 |
| Data | **PostgreSQL 18**, shared schema + RLS, `tenant_id` in every key; pgx v5.9.2+ + sqlc; goose SQL migrations | 0004 |
| Jobs & events | **River** (Postgres job queue, transactional enqueue) + transactional outbox/inbox | 0005 |
| Mobile | **Native**: SwiftUI (Swift 6.3) + Jetpack Compose (Kotlin 2.4) + **KMP shared core** | 0006 |
| Web | 4 static deployables: `site` (Astro: landing, help, QR trace, SEO) · `app` (owner+accountant) · `gov` (officers) · `console` (internal, F2) — React 19 + Vite 8 SPAs; **no Next.js** | 0007 |
| Offline sync | v1 client outbox (KMP, SQLDelight) + Idempotency-Key; schema PowerSync-compatible | 0008 |
| Hosting | **AWS first** (ap-southeast-1), data-residency plan, portable to on-prem | 0009 |
| AI | Provider-agnostic LLM port; **Claude + GLM** via gateway; switchable to self-hosted | 0010 |
| Identity | Phone OTP (Zalo ZNS, SMS fallback), roles, MFA for officers; verification levels L0/L1/L2 gate features; **web phase**: assisted check (pilot), Casso eKYC via Cas ID (desktop), vendor Web eKYC SDK (phone browser); **native phase**: CCCD chip via NFC in-app + embedded face/liveness SDK | 0011 |
| Finance integrations | **Casso** (Cas API) behind provider ports; fallbacks kept possible | 0012 |
| Money | Decimal everywhere (`numeric` in DB, `apd`/decimal in Go, bignum in KMP); shared test vectors | 0004, 0006 |

## 6. Modules (bounded contexts)

| Module | Owns | Notes |
| --- | --- | --- |
| identity·tenant | households, members, roles, devices, sessions | tenant table is the only non-RLS core table |
| catalog·stock | SKUs, lots, stock ledger | race-safe guarded updates |
| sales·order | counter sale, channel orders, order state machine | Idempotency-Key on every write |
| payment·recon | QR payment intents, received transactions, matching, verification | see §8.1 |
| invoicing | sales invoices, provider orchestration, tax-authority code tracking | see §8.2 |
| tax·books | HKD books (TT 152/2025 S1a/S2a), tax computation & forecast, filing drafts, deadlines | deterministic, versioned rules |
| booking | resources, holds, bookings | tourism vertical |
| procurement | suppliers, purchase notes, inbound invoices | farmers often have no invoice |
| traceability | public lot pages (explicit publish only) | deliberate non-RLS projection |
| connectors | provider ports + adapters, grant/token vault, webhook inbox, freshness | Casso first |
| assistant | AI conversations, tools (read-only DB role), RAG (pgvector) | never decides numbers |
| program·B2G | activation milestones (installed, first invoice, active at 90 days), anonymized aggregates | province pays per milestone |
| notifications | in-app, push, Zalo OA/ZNS, email; outbox-backed | |
| audit | append-only journal of every mutation, actor attribution | grant-enforced append-only |
| consent | data-protection consents, 180-day bank-data consent (TT 64/2024), retention, erasure | PDPL 91/2025 |

Module rules: domain layer pure (no IO); modules talk through application services or outbox
events, never by reading each other's tables.

## 7. Cross-cutting rules (carried from SoloDesk lessons)

- **RLS**: `ENABLE` + `FORCE` on every tenant table; policy on `current_setting('app.tenant_id', true)`;
  `SET LOCAL` inside the request transaction only; app role is never superuser/BYPASSRLS — a deploy
  gate checks it; a concurrent cross-tenant test must never be weakened.
- **Idempotency**: client-generated UUIDs + `Idempotency-Key` on every write; cached replay inside the
  same transaction.
- **Money**: never float. Totals derived from lines; payment status derived on read, not stored.
- **Outbox/inbox**: external effects (notifications, provider calls) leave via a transactional outbox;
  inbound webhooks land in a durable inbox **before** responding.
- **Audit**: every mutating use case writes one journal entry in the same transaction; actor resolution
  fails closed.
- **Time**: store UTC, compute business periods in Asia/Ho_Chi_Minh, and re-filter provider data by
  local period (Casso GDT Hub filters dates in UTC — see §8.3).
- **Configuration**: one env schema per app; CI fails on drift.
- **Language**: code, DB values and docs in English; apps bilingual (vi default, en for staff).

## 8. Finance integrations with Casso (from the CEO's sandbox evaluation, 2026-09-29)

Casso is a **connection layer** (banks, e-invoice providers, tax portal, eKYC, lookups), not
accounting software. Books, tax computation, forecasts, reminders, AI, Zalo and consent are OPC's
own core. Of 21 integration needs: 2 proven, 8 conditional, 4 untested, 7 not offered by Casso.

Ports defined in `connectors` (each with a Casso adapter first):
`PaymentCollection`, `BankTransactions`, `InvoiceIssuing`, `TaxPortalSync`, `TaxFiling`,
`IdentityVerification`, `BusinessLookup`, `PaymentDeeplink`.

### 8.1 Payments and reconciliation
- Dynamic QR per order (`POST /qr-pay`, order code in `referenceNumber`, description ≤ 9 chars).
- **Webhooks are unsigned.** Design: secret webhook path + source-IP monitoring + durable inbox +
  dedup key `tx:{grantId}:{transaction.id}`; every received payment is **"pending verification"**
  until a second channel confirms (statement sync or owner confirmation); owner-set threshold above
  which goods are not released without confirmation. A forged webhook must never mark an order verified.
- One webhook per grant on the same account — merge duplicates; the duplicate may lack the order code.
- Unmatched money (no order code) goes to a review queue, never guessed.
- Account must be the **household's organisation account** (TT 17/2024), not the owner's personal
  account — untested with Casso yet (task B23).

### 8.2 Sales invoices
- Invoice Hub forwards to the household's provider (X Invoice, Hilo, S-Invoice, Bkav); the provider
  signs with the household's certificate. Cash-register (máy tính tiền) invoices: Hilo returns the
  `M…` tax code immediately; X Invoice did not.
- `POST /invoices` has **no confirmed idempotency** → on timeout mark **"outcome unknown"**, check the
  provider, never auto-retry (duplicates consume invoice numbers and cannot be cancelled via API).
- INVOICE webhooks were never received → **poll** status at 3, 5, 15, 60 min, then hourly to 24 h.
- Totals are recomputed from lines by the server → all discounts/rounding live on lines; OPC checks
  the invoice total against the order.
- Adjust/replace/cancel are **not supported via API** → guided flow on the provider portal, then
  record the result.

### 8.3 Tax portal, filing, signatures, eKYC
- GDT Hub (inbound/outbound invoices): filters by **UTC dates**, no pagination, returns buyers' personal
  data (mask it), per-account fee → enable per household, re-filter by `issuancePeriod`.
  Legal basis for Casso logging into the tax portal on the household's behalf must be cleared first.
- Tax return API is too thin to plan on → OPC generates the return as structured data/XML from its own
  books; default path is "owner files on eTax, OPC records the receipt code"; Casso filing only after testing.
- Tax payment is never automated (no third-party path exists).
- XML signing: no Casso API; e-invoice signing stays with providers.
- Casso eKYC goes through the separate **Cas ID app + NFC** and is **not a prerequisite** for any other
  Casso product. Web phase: offered to desktop users (scan the laptop's QR with Cas ID); phone-browser users
  use a vendor Web eKYC SDK; native phase: chip read in the OPC app. The verified identity is passed to
  Casso's grant `user` object, which blocks linking a bank account that is not the owner's (ADR 0011).
- Linking UX: Cas Link opens inside OPC (web popup/iframe; native in-app browser + universal-link return —
  to be confirmed); users never create a Casso account (ADR 0012).

### 8.4 Cost signal
Floor 500 USD/month. Per-household cost scales with per-account products (Transactions, GDT Hub
200,000đ/account/month). Pilot estimate at 100 households: ~132k–462k đ/household/month. At 5,000
households, QR + invoice alone is roughly 120k đ/household/month → **volume pricing must be
negotiated** before scale, and per-account products stay opt-in per household.

Product maturity (Casso demo 23/09): GDT Hub, TVAN, Balance Hook, Payment Initiation **Beta**;
E-Invoice **Alpha** — the programme brief asks for stable products → keep provider ports so a direct
adapter (e.g. an e-invoice provider's own API, payOS or a bank) can replace any Casso product.

## 9. Regulatory anchors (verify before coding the rule engine)

| Topic | Reference (as cited by the CEO evaluation) |
| --- | --- |
| HKD VAT/PIT exemption threshold 1 tỷ/yr (retroactive 01/01/2026) | NĐ 141/2026 amending NĐ 68/2026 |
| E-invoice obligation > 1 tỷ, register within 30 days | NĐ 68/2026 Art. 8 cl. 5 |
| E-invoices (replaces NĐ 123/2020 and NĐ 70/2025 from 01/07/2026); POS invoices need no digital signature | NĐ 254/2026 |
| Rates on revenue (VAT 1/5/3/2%; PIT 0.5/2/1.5/1%) | Law 48/2024/QH15; Law 109/2025/QH15 (PIT not yet cross-checked) |
| HKD books S1a/S2a | TT 152/2025/TT-BTC (not yet cross-checked) |
| 14 HKD tax forms | TT 18/2026/TT-BTC |
| Bank-data consent max 180 days | TT 64/2024/TT-NHNN |
| HKD account naming | TT 17/2024/TT-NHNN |
| Personal data | PDPL 91/2025/QH15 + Decree 356/2025; cybersecurity data storage Decree 53/2022 |

Rates and thresholds live in versioned reference tables with `effective_from/to`, never in code.

## 10. Repository layout

```text
apps/
  api/            Go: cmd/api, cmd/worker, internal/{platform,<module>}, db/migrations
  app/            React SPA — owner + staff + accountant (role-based)
  gov/            React SPA — programme officers (B2G)
  site/           Astro — landing, help, legal, QR trace pages (SEO)
  console/        React SPA — internal support/ops (F2)
  android/        Kotlin + Jetpack Compose
  ios/            Swift + SwiftUI
shared/
  contracts/      openapi.yaml (source of truth) + generated clients (TS, Kotlin/KMP)
  core-kmp/       Kotlin Multiplatform: money/tax rules, cart, offline outbox, SQLDelight, API client
  test-vectors/   JSON cases for money/tax/rounding — run by Go AND KMP test suites
  design-tokens/  generated from the design system (Tailwind theme, Kotlin, Swift)
design/           uiux-studio projects: system + apps/{site, app, gov, owner-ios, owner-android}
infra/            OpenTofu (AWS), environments, migration gate
docs/             ARCHITECTURE.md, adr/
```

Build orchestration: Taskfile at the root calling `go`, `pnpm`/Turborepo, Gradle and Xcode builds.

## 11. Delivery phases

| Phase | Scope |
| --- | --- |
| F0 Foundation | repo, CI, OpenTofu baseline, platform package (tx + RLS, idempotency, outbox/inbox, audit, auth skeleton), OpenAPI pipeline, design system |
| F1 Pilot slice — **web first** | `app` web SPA (desktop + phone browser): onboarding with L0/L1 verification, catalog/stock, counter sale, QR payment + verification, invoice via Casso/Hilo, notifications (Zalo), books v1, tax computation & deadlines; `site` landing + QR trace |
| F2 Pilot hardening | first filing period (Q4/2026 due 31/01/2027), B2G milestones, consent flows, monitoring of connector freshness |
| F3 Native mobile | iOS (SwiftUI) + Android (Compose) on the KMP core: offline counter sale, in-app CCCD chip eKYC (L2), push |
| F4 Scale to 3–5k | volume pricing, multi-device sync (PowerSync), partitioning, load tests, pentest |

## 12. Open items

1. Data residency on AWS: Singapore region vs Hanoi Local Zone for PII — legal opinion (ADR 0009).
2. Casso open questions (webhook signing & IPs, invoice idempotency, organisation accounts, tax-portal
   legal basis, filing API, signing certificates, 180-day consent signal, SLA, volume pricing).
3. Identity: Ory Kratos vs in-house (spike); eKYC vendor quotes (VNPT / FPT.AI / Viettel, web + native SDK); Vietnam CSCA certificates; L0/L1/L2 feature gates; VNeID conditions.
4. E-invoice for HKD > 1 tỷ: tax-code invoice vs cash-register invoice per household type (conflict #7
   in the CEO evaluation).
5. Information-system security level required by the programme (Decree 85/2016).
6. Leaked Casso sandbox key and console password (23/09) must be rotated before development (B18).

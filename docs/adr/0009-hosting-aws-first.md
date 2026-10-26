# ADR 0009 — Hosting: AWS first, with a data-residency plan and on-prem portability

Status: Accepted · 2026-10-01 (deviates from the org's on-prem plan — deliberate, owner decision)

## Decision
- Region **ap-southeast-1**: ECS on Fargate (Graviton/arm64) for `api` and `worker`; RDS for
  PostgreSQL 18 Multi-AZ + read replica; ElastiCache for Valkey; S3 + KMS; Secrets Manager; CloudFront +
  WAF; ALB; SES (email). IaC with OpenTofu; reuse org CI actions (OIDC to AWS, ECR, gated migrations,
  ECS deploy, Gitleaks, OpenAPI diff).
- Connector tokens (Casso access tokens, provider secrets) **envelope-encrypted with KMS**; only the
  connector code path can decrypt; every decryption audited.
- Observability: OpenTelemetry (ADOT) with PII scrubbing; CloudWatch/X-Ray initially.
- **Data residency**: PDPL 91/2025 and Decree 53/2022 may require personal data of Vietnamese users to be
  stored in Vietnam. Before production data: obtain a legal opinion; options are (a) Singapore region with
  a cross-border transfer dossier, or (b) PII stores in the **AWS Hanoi Local Zone** (EC2/EBS-based
  Postgres if RDS is unavailable there). Pilot data handled under option (a) only with that dossier.
- Portability: containers + Postgres + Valkey + S3 API only (no AWS-only data services) so an on-prem
  k3s/CNPG move stays a deployment change.

## Revisit when
Legal opinion arrives; or the org's on-prem platform is production-ready with an SLA.

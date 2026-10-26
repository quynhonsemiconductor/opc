# ADR 0001 — Modular monolith in one monorepo

Status: Accepted · 2026-10-01

## Context
Target v1 is 3,000–5,000 households (~100 peak writes/s), one small team, one release train across
backend, web and native apps. Microservices would add network failure modes, distributed transactions
and operational cost without a scaling need.

## Decision
- One Go binary with two entrypoints (`api`, `worker`), organised as hexagonal modules (domain / app /
  adapters). Modules communicate through application services or outbox events, never by reading each
  other's tables.
- One monorepo for backend, web, mobile, contracts, test vectors, design and infra.

## Consequences
- One deploy, in-process transactions across aggregates, simple local development.
- Boundaries must be enforced by convention + lint (no cross-module imports of `adapters/` or tables).

## Alternatives rejected
Microservices from day one; separate repos per app (contracts and test vectors would drift).

## Revisit when
A module needs a separate security boundary, independent scaling, or a different runtime — extract it
behind the existing port/outbox boundary.

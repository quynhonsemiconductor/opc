# ADR 0008 — Offline sync: client outbox first, PowerSync-compatible schema

Status: Accepted · 2026-10-01

## Context
Counter sales must work offline (rural networks, Casso incidents). Multiple devices per household are
likely later (owner, family, staff).

## Decision
- v1: KMP outbox in SQLite; every offline write carries a client-generated UUID used as the
  `Idempotency-Key`; replay is exactly-once server-side. Server remains the source of truth for stock;
  conflicts (e.g. oversell) are surfaced to the owner, not silently resolved.
- Schema rules now so a sync engine can be added later: client-generatable UUID keys, `updated_at`,
  soft deletes, tenant-scoped buckets.
- During provider incidents the app falls back to the household's static VietQR with manual matching
  confirmed by the owner, flagged "fallback mode".

## Revisit when
Multi-device editing per household becomes common → self-hosted PowerSync (Kotlin and Swift SDKs are GA).

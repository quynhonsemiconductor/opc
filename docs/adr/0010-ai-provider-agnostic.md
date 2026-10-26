# ADR 0010 — AI: provider-agnostic LLM port, Claude + GLM now, self-hosted later

Status: Accepted · 2026-10-01

## Decision
- A Go `LLM` port with adapters: **Anthropic Claude** (direct API or Amazon Bedrock) and **GLM**
  (Z.ai API); a routing policy per task (assistant reasoning, extraction/classification, Vietnamese
  explanations) with per-tenant budgets and full call logging.
- Tools run under a **read-only DB role** through a fixed tool registry; money/tax/stock answers come from
  deterministic queries; AI never writes business data without an owner-approved action.
- PII minimisation before any external call (mask IDs, phones, buyer data); prompts and outputs logged
  without raw PII. Sending data abroad (US/China providers) requires the PDPL transfer dossier; tasks that
  need raw personal data are routed to self-hosted models once available.
- An evaluation suite (Vietnamese cases, tool-use correctness) gates any model or provider switch.
- RAG over approved, versioned, cited content (pgvector); embeddings provider behind the same port.

## Revisit when
On-prem GPU capacity exists → add a self-hosted adapter (e.g. open-weight GLM via vLLM) and move PII tasks.

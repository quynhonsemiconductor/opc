# ADR 0007 — Web surfaces: one Astro public site + React SPAs; no Next.js

Status: Accepted · 2026-10-01 (supersedes the earlier "0007-web-spa-react-astro")

## Context
OPC's primary owner surface is the native app. The web serves the public (marketing, help, QR trace
pages), owners/staff/accountants on desktop or a counter tablet, programme officers (B2G), and QNSC staff.
These audiences differ in SEO needs, security posture and release approvals. The backend is Go behind an
OpenAPI contract; avoiding forced migrations is a primary criterion.

## Decision
| Deployable | Domain (example) | Users | Stack |
|---|---|---|---|
| `apps/site` | `opc.vn` | public, buyers scanning QR | **Astro** (static-first): landing, pricing, help centre, news, legal, `/truy-xuat/{lot}` trace pages (re-generated on publish) |
| `apps/app` | `app.opc.vn` | owner, staff, delegated accountant (tenant switcher) | **React 19 + Vite 8 SPA**, TanStack Router/Query, Tailwind v4, shadcn/ui |
| `apps/gov` | `gov.opc.vn` | programme / province officers | React SPA; mandatory MFA, stricter CSP, optional IP allow-list, separate audit and release approval |
| `apps/console` (F2) | `console.opc.vn` | QNSC support, field onboarding team, connector health | React SPA behind SSO, never public |

- Owner and accountant share one app (same data and flows; accountant = role with multi-tenant switch).
  Officers and internal staff get separate apps so their code and privileges never ship to households.
- Shared packages: `ui` (shadcn themed from design tokens), generated API client, `design-tokens`, `i18n`,
  auth helpers. Consistency through packages, independence through deployables.
- Hosting: all four are static assets on S3 + CloudFront (+ WAF). No Node server runtime.
- Auth without a BFF: `api.opc.vn` issues an `httpOnly; Secure; SameSite=Lax` session cookie on the shared
  registrable domain + double-submit CSRF token; tokens never reach JavaScript; strict CORS to known origins.
- `apps/app` may become an installable PWA for counter tablets (service worker + IndexedDB outbox) in F2.

## Why not Next.js
- No SEO need behind login; React Server Components add little for per-user dashboards.
- It would add a second backend (Node BFF) next to Go, duplicating logic, and a server runtime to operate.
- Its model has changed repeatedly (pages → app router, caching defaults reversed in 15, middleware → proxy
  and Cache Components in 16) — contrary to the avoid-migration criterion. Astro beats it for content pages
  on weak phones (zero JS by default).

## Revisit when
Personalised SEO pages at scale, or a hard BFF requirement, appear.

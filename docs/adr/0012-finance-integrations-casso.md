# ADR 0012 — Finance integrations through ports; Casso as the first provider

Status: Accepted (provider under evaluation) · 2026-10-01

## Context
The CEO's sandbox evaluation (2026-09-29) shows Casso as a connection layer to banks, e-invoice providers,
the tax portal and eKYC. Of 21 integration needs: 2 proven, 8 conditional, 4 untested, 7 not offered.
Several products are Beta/Alpha; webhooks are unsigned; invoice creation is not proven idempotent; minimum
fee 500 USD/month. Casso Link is a hosted page (web JS popup/iframe available); native SDKs are
"coming soon"; no white-label or headless linking.

## Decision
**Ports and ownership**
- `connectors` module ports: PaymentCollection, BankTransactions, InvoiceIssuing, TaxPortalSync, TaxFiling,
  IdentityVerification, BusinessLookup, PaymentDeeplink. Casso adapters first; every port keeps a second
  adapter possible (payOS or a bank for QR; an e-invoice provider's own API).
- Books, tax computation, forecasts, filing drafts, reminders, consent and AI are OPC core.

**Linking UX (one flow, inside OPC)** — users never create a Casso account
- Web: Cas Link via the official JS script in popup/iframe mode (`onSuccess(publicToken, state)`).
- Native: Cas Link in the system in-app browser (ASWebAuthenticationSession / Custom Tabs), returning via a
  universal/app link `redirectUri` — **to be confirmed by Casso** (not documented).
- Always pass `fiServiceId` (open the right bank/provider directly), `language: "vi"`, the verified `user`
  identity (ADR 0011) and a random `state` checked on return. One scope per grant until combined scopes
  are proven. Order: QR first (minimum to sell) → invoice provider when needed → tax portal opt-in.
- Detect duplicate links (same account number / tax code) and remove extras via `/grant/remove`.

**Casso eKYC** (Cas ID): used in the web phase for desktop users and assisted pilot onboarding; replaced by in-app chip reading when native apps ship (ADR 0011).

**Safety rules (mandatory)**: payments "pending verification" until a second channel confirms; webhook
inbox with dedup and quarantine of unknown `grantId`; invoice "outcome unknown" on timeout without
auto-retry; invoice status polling (3/5/15/60 min, then hourly to 24 h); UTC re-filtering of tax-portal data
by local period; per-household opt-in for per-account products; 180-day bank-data consent tracking
(TT 64/2024); KMS envelope encryption of access tokens.

## Open questions for Casso
1. Does any product require the end user to hold a Cas ID account in production?
2. Accounts already linked to another Casso-based app: can consent be given without the Cas ID app?
3. A parameter to open Cas Link directly in "connect first" mode (skip the "scan with Cas ID" screen)?
4. Official support for in-app browsers/WebView and universal-link `redirectUri`; native SDK timeline;
   branding options.
5. Webhook signing and production source IPs; `POST /invoices` idempotency; HKD organisation accounts;
   legal basis for tax-portal login on the household's behalf; Tax return API scope; signing certificates;
   consent-expiry signal; SLA; volume pricing at 5,000 households.

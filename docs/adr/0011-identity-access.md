# ADR 0011 — Identity, access and owner identity verification (eKYC)

Status: Accepted · 2026-10-01 (account-service implementation pending a 3-day spike; eKYC vendor pending quotes)

## Context
- **Delivery order: web first, native mobile later.** The first owner surface is the `app` web SPA, used on
  a laptop/counter PC and on phone browsers.
- The programme requires a verified electronic identity for owners (R-A1-03, OPC-23). Verification also
  protects money and the province's budget: QR payments must reach the real household, Casso's grant `user`
  check needs a verified name/ID to confirm bank-account ownership, invoices are issued in the household's
  name, and the province pays per activated household (milestones must be real households).
- Browsers **cannot read the CCCD chip** (Web NFC only supports NDEF tags, not ICAO 9303 ISO-DEP), so
  chip-based verification on web needs a second device or a native app.
- Casso eKYC: the user opens the separate **Cas ID** app and scans a QR shown on the partner's screen; Cas ID
  reads the chip via NFC; Casso returns name + CCCD number (5-minute token). It is **not a prerequisite** for
  any other Casso product OPC uses (QR Pay, Transactions, Balance Hook, Invoice Hub, GDT Hub, Deeplink). It
  suits desktop users (screen + phone) and fails single-phone users (cannot scan their own screen).

## Decision

### Accounts and sessions
- Owners/staff sign in with **phone number + OTP** (Zalo ZNS first, SMS fallback); optional passkey; no
  passwords required. Officers and accountants: email/phone + **mandatory MFA**.
- Roles per tenant: owner, staff, delegated accountant (time-boxed, scoped); programme officer reads only
  B2G read models. Web sessions: `httpOnly` cookie + CSRF (ADR 0007). Native later: short-lived JWT +
  rotating refresh tokens with reuse detection. Device registry; remote sign-out.
- Account service: **Ory Kratos** (self-hosted, Go) vs in-house module — 3-day spike (Zalo ZNS OTP,
  refresh rotation, audit hooks).

### Verification levels and feature gates
| Level | How | Unlocks |
|---|---|---|
| **L0** phone verified | OTP | explore, set up catalog/stock, record sales offline-style (no money received through OPC) |
| **L1** identity verified | document + face match + liveness, **or** Casso eKYC (chip via Cas ID), **or** assisted check by field staff | link bank account / QR payments, issue invoices, B2G "activated" milestone |
| **L2** chip-verified | CCCD chip read (Cas ID now; OPC native app later) + national population data check via vendor (C06/RAR) where available | tax filing drafts submission path, raising per-transaction limits, accountant delegation |

Exact gates are a product decision; the mechanism (level stored per owner, checked by the API) is fixed now.

### Phase 1 — web (now)
Pick per context, behind one `IdentityVerification` port:
1. **Pilot (5–10 households, field team on site): assisted verification.** Staff checks the physical CCCD
   against the person and records it (staff identity + timestamp + photo of nothing biometric), or uses
   Casso eKYC on the owner's phone with the staff laptop showing the QR. Reaches L1 (L2 if Casso eKYC).
2. **Desktop users: Casso eKYC** — QR on the laptop screen, owner scans with Cas ID on their phone →
   chip-based → L2. Requires installing Cas ID; offered, not forced.
3. **Phone-browser users: vendor Web eKYC SDK** (FPT.AI has a Web SDK; VNPT/Viettel to confirm) — photo of
   both CCCD sides (OCR) + selfie with liveness in the browser → L1. No chip, so not L2.
4. Pass the verified identity into Casso's `POST /grant/token` `user` object (`legalName`, `idNumber`, or
   `companyName` + `companyLegalId` for the household's organisation account) so Casso blocks linking a bank
   account that is not the owner's.

### Phase 2 — native apps (later): one flow inside OPC, no other app
1. Read the CCCD chip via NFC **in the OPC app** with open-source ICAO 9303 libraries (JMRTD on Android,
   NFCPassportReader on iOS; references: flutter_cccd_vn for the Vietnamese CAN/PACE flow, gmrtd for
   server-side checks). Passive Authentication requires Vietnam's CSCA certificates — source to be found.
2. Face match + liveness with an **embedded vendor SDK** (FPT.AI, Viettel — ISO 30107-3 level 2 — or VNPT)
   themed to OPC; backend calls the vendor for the national population data check. Prefer a vendor that
   accepts chip data read by OPC's own library so OPC keeps the UI.
3. Upgrades existing L1 owners to L2 without re-registering. Later: VNeID-based identification/sign-in
   (Decree 69/2024 — integration conditions to be confirmed).

### Data protection (all phases)
- Store only: level, method, timestamp, vendor/request reference, name and CCCD number (encrypted).
  **No face images or biometric templates are stored** (sensitive data under PDPL 91/2025); process on device
  or in the vendor session; separate consent screen for identity verification.
- Name matching against the bank-account holder: strip diacritics, uppercase, collapse spaces, drop the
  "HỘ KINH DOANH" prefix; mismatch → human review.

## Consequences
- Web-first ships without waiting for native NFC; verification strength rises when native apps arrive.
- Two paths to maintain in phase 1 (Casso eKYC + one web vendor); the port keeps them swappable.
- OPC bears vendor cost (one-time per owner) and the data-protection obligations (consent, DPIA, retention).

## To do
1. Quotes from FPT.AI, Viettel AI, VNPT eKYC (web + native SDK, per-verification price, UI customisation,
   whether they accept externally-read chip data, C06/RAR check availability).
2. Find the source of Vietnam's CSCA certificates for Passive Authentication.
3. Confirm with Casso that Cas ID is not required for other products in production (ADR 0012).
4. Product decision on the exact L0/L1/L2 feature gates.

# Connector catalog — the list of providers is DATA, not UI (v4.9.0, credentials v5.0.0)

Why: OPC will connect dozens of providers (delivery alone: GHTK, GHN, J&T, Ahamove, Grab Express, Viettel Post…). The screens
(`Thêm cách nối`, provider page, `Đã nối`, `Việc OPC làm`, category hubs) only **render** this catalog (rows live in `tools/v4/providers.py`). Adding a provider = adding an entry,
not redesigning a screen. QNSC maintains it in the console (F2); a household sees the entries that are published to it.

Three layers (see also `apps/app/IMPLEMENT.md` → Connections data model):

1. **Provider** (this catalog) → what exists.
2. **ProviderAccount** (per household) → what the owner connected, once, with a display name (several per provider allowed).
3. **JobGrant** (per account) → what OPC may do with it; scope is stored per (account, job).

## Provider entry (schema)

```json
{
  "id": "ghtk",
  "name": "Giao Hàng Tiết Kiệm",
  "short": "GHTK",
  "categories": ["giao-hang"],
  "jobs": [
    { "id": "create-shipment", "label": "Tạo vận đơn", "category": "giao-hang", "scopes": ["shipment.create"], "needs_human_click": true,
      "cost_note": "GHTK thu phí theo bảng phí của họ; OPC chỉ hiện", "prerequisites": ["Tài khoản GHTK của hộ", "Địa chỉ lấy hàng"] },
    { "id": "track", "label": "Theo dõi vận đơn", "category": "giao-hang", "scopes": ["shipment.read"] },
    { "id": "cod", "label": "Thu hộ, đối soát", "category": "giao-hang", "scopes": ["cod.read"], "settlement": "weekly-fri" }
  ],
  "auth": { "mode": "casso | oauth | key | link | assist", "owner_only": true, "consent_days": 180, "otp": "zalo|sms" },   // v5.0: see "who holds the credential" below
  "coverage": { "regions": ["national"], "cod": true, "same_day": false },
  "status": "available | simulated | coming_soon | needs_partner | sunset",
  "phase": "demo | pilot | ga",
  "fit_when": ["sells to other provinces", "needs COD"],
  "fit_rules": { "any_of": ["model.sells_online", "model.sells_b2b"], "unless": ["uses:own-staff-only"] },
  "manual_path": "giao bằng người của hộ, nhà xe hoặc nhập mã vận đơn",
  "never": ["resend a shipment whose result is unknown", "pay fees on the owner's behalf"],
  "trust": { "checked_by": "OPC", "checked_at": "2026-10-06", "legal_check": null },
  "links": { "signup": "…", "docs": "…" }
}
```

Rules the UI relies on
- `status: coming_soon` → tile shows **Báo tôi** only (never a connect button); a request is counted per household.
- `status: simulated` → **Mô phỏng** badge everywhere it appears (demo only).
- `fit_rules` feed the **Gợi ý cho hộ của chị** shelf together with Readiness gaps (categories still on the manual path).
- `jobs[].needs_human_click` → OPC prepares, a person presses (N-06/N-07). `never[]` is shown on the provider page as **Không làm**.
- `auth.owner_only` → only the owner can connect / reconnect / disconnect; others see the state (role rails).
- A provider may list jobs in several categories (Zalo OA: nhận đơn + ZNS; X Invoice: hoá đơn + tra cứu + chữ ký số). The household connects it once.
- Open questions: does one Casso login cover Cas / QR Pay / GDT Hub? does one Zalo authorisation cover messaging and ZNS? The schema holds both answers
  (`auth` per provider, `scopes` per job; split the provider into two entries if the vendor requires separate activation).

## Choosing between several providers in one category

| Category policy | Example | UI |
|---|---|---|
| `fan-in` | chat channels (Zalo OA, Messenger) | all feed one inbox; nothing to choose |
| `accumulate` | bank accounts, shops | all count; list them |
| `choose-per-action` | delivery, invoice issuer (counter vs B2B) | **default + assistant suggests + the person chooses**; quote preview |
| `rules` (later) | delivery by weight / zone / same-day | ordered rules with a default (ShipStation-style "if … else if … default"); max 3 for a household |

MVP = `choose-per-action` with a default. Automatic rules and rate-shopping strategies (cheapest / fastest / best value) come later; rules classify an
order, a strategy prices it — keep them separate when they arrive.

## Scale checklist (for the directory and "Đã nối")
- Directory: search; status chips; **Gợi ý cho hộ**; groups by purpose with `sắp có` folded; result counts on chips; provider page before connecting.
- Đã nối: **Cần chị xem** strip first (error, expiring, needs login); chips Lỗi / Sắp hết hạn / Theo nhóm; compact grouped rows, broken rows highlighted.
- Category hub (one per multi-provider category): the list, the default, how it is chosen, a quote preview.
- Request a provider: free text; the count per provider drives the backlog.

## v5.0.0 — who holds the credential (`mode`) — replaces `auth.type`

The authoritative rows are in `tools/v4/providers.py` (71 providers; `id, mono, name, group, mode, status, households, src`). The schema's `auth.type` becomes:

| mode | What the household does | What OPC stores | Revoke | Examples |
|---|---|---|---|---|
| `casso` | types the secret on Casso's Cas Link page | a grant token only; never the password or key | on Casso (webhook `GRANT`) or in OPC | banks via Casso, Hilo, X Invoice, S-Invoice, Bkav, GDT Hub |
| `oauth` | approves on the provider's page (owner OTP) | access + refresh token, encrypted, expires | provider page or OPC | Zalo OA, Messenger, Shopee, TikTok Shop |
| `key` | pastes keys into OPC | keys in a vault; UI shows last 4 only; never shown again | rotate (test first, old key keeps working until the new passes) or remove; also delete at the provider | payOS, SePay, GHN, GHTK, SMS brandname |
| `link` | nothing; OPC opens the provider's app pre-filled | nothing | — | eTax Mobile, accountant exports |
| `assist` | registers or signs a contract first; OPC staff help | nothing until registered | — | wallets (MoMo, ZaloPay), CAs, eKYC, other invoice providers |

Status adds `partner` (platform-side gate; the household sees "Sắp có"). `GATE` in providers.py lists the reason (legal N-15, BIDV contract, Câu 2…).
Jobs of another provider are not rows (ZNS = a job of Zalo OA; IDKit/tra MST = a job of Casso). Zalo personal accounts are not a provider (no API).
Platform side (QNSC console): a provider can be **hidden** (existing households keep working; new ones do not see it) or **removed** (households disconnected and told; platform keys deleted); a reason is required and goes to the audit log.
Casso is a hub: hiding or removing it stops 11 providers at once; the registry shows the consequence first.

## v5.1.0 — features first (capabilities sit above providers)

The household never starts from a provider. Source: `tools/v4/capabilities.py` — 12 features, each with a **tier** (from the business model), **when** it is due, the **recommended way**, the provider **choices**, the **manual path** and the connector categories it covers:

| Việc OPC làm | Tier (An Nhiên) | Categories (SCOPE §8) | Manual path |
|---|---|---|---|
| Xác minh chủ hộ | Cần, ngay | 9 | — (OPC staff on site) |
| Nhận tiền chuyển khoản | Cần, ngay | 1, 2 | — (OPC staff connect it) |
| Xuất hoá đơn bán ra | Cần, trước đơn sỉ đầu tiên | 4 | — |
| Chữ ký số | Cần, trước đơn sỉ đầu tiên (chờ quyết định) | 8 | — |
| Nhận yêu cầu từ khách | Nên có | 11 | dán tin, ảnh, gõ tay |
| Báo tin cho khách | Nên có | 14 | chị tự nhắn |
| Hoá đơn mua vào tự về sổ | Nên có | 5 | chị Lan tải bảng kê |
| Trả tiền nhà cung cấp | Nên có | 3 | chép số tài khoản và số tiền vào app ngân hàng |
| Giao hàng | Khi cần | 13 | người của hộ, nhà xe |
| Bán trên sàn | Khi cần | 12 | nhập file đối soát |
| Kê khai và nộp thuế | Khi cần | 6, 7 | xuất file, eTax |
| Sổ sách và xuất cho kế toán | Khi cần | 16, 17 | Excel/CSV có sẵn |

"Require" = the dependent flow is locked until one way is connected (no transfer payments, no wholesale orders, no coded invoices); the app itself is not blocked and cash at the counter works. Tiers are rules on the model (quầy / khách sỉ / sàn · mua về bán / tự chế biến), not fixed per household.

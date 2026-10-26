# Providers OPC can connect to in Vietnam — working list (2026-10-07)

> The build source is `tools/v4/providers.py` (71 rows with connection mode). This file is the research note behind it. Zalo personal accounts are not connectable: Zalo offers an API for Official Accounts only; pasted text in the Hộp yêu cầu is manual input, not a connection.

Source tags: **[BA]** named in the BA/CEO documents (`opc/docs/ba/`, mainly "Casso cho SoloMatrix" 29/09/2026, PRD/BRD/Feature catalog) ·
**[Web]** confirmed by a web search on 2026-10-07 (exists / is used in Vietnam — NOT that an OPC integration or partner API is available) ·
**[Tôi]** from my own knowledge, not verified in this session — check before committing.
Phase: **P1** pilot (tested or needed by the BA scope) · **P2** next · **P3** later/optional · **Tay** manual path only (no API, or not open to third parties).
"Demo" = shown as **Mô phỏng** in the design. Nothing here is a commitment that a partner API exists; each needs a partner/legal check.

## 1 · Chat and order intake (category 11)
| Provider | Use | Source | Phase |
|---|---|---|---|
| Zalo OA | receive customer requests, reply, confirm (required channel) | BA · Web | P1 |
| Telegram | fallback notification while the OA is awaiting approval (B20) | BA | P2 |
| Facebook Messenger (Page) | orders from a Page | Tôi (SCOPE lists as later) | P2 |
| Instagram DM, TikTok messages, email inbox | orders from other channels | Tôi | P3 |

## 2 · Notifications out (category 14)
| Provider | Use | Source | Phase |
|---|---|---|---|
| Zalo ZNS | tiền về, hoá đơn, nhắc nợ to a phone number; **templates must be approved by Zalo**, per-message cost | BA · Web (8x8/Infobip docs) | P1 |
| SMS brandname (eSMS, SpeedSMS, Viettel, VNPT, FPT…) | SMS fallback / OTP | Tôi | P2 |
| CPaaS resellers of ZNS/SMS (Infobip, 8x8) | alternative route to ZNS | Web | P3 |
| Web push / email | app alerts | Tôi | P2 |

## 3 · Banks and incoming money (categories 1–2)
| Provider | Use | Source | Phase |
|---|---|---|---|
| **Casso (Cas API)**: QR Pay, Transactions, Virtual Account, Balance hook | QR per order, "tiền về" webhook, transactions | BA (tested on sandbox) | P1 |
| MB (VietQR Official via Casso) | tested OK, 10/12 cases, real money | BA | P1 |
| BIDV (via Casso) | virtual account needs a contract (2–5 working days); org account link to test | BA | P2 |
| Techcombank, Vietcombank, Agribank (via Casso, internet-banking password) | transactions only by **date, no time** → weak matching | BA | P2 |
| Ví Bảo Kim | in Casso's organisation list | BA | P3 |
| SePay | bank-transfer notification; 19+ banks (MB, OCB, KienlongBank, MSB, VietinBank, BIDV, TPBank, VPBank, ACB…); **old spec used it** | BA · Web | P2 (alternative to Casso) |
| payOS | VietQR payment link | Web | P2 |
| VietQR (NAPAS) account-name lookup | check a supplier's account name | BA · Web | P2 |
| VNPAY, ViettelPay | QR / wallet | Web | P3 |
| MoMo, ZaloPay, ShopeePay | the three dominant wallets; **Casso's list has none of them** | BA (gap) · Web | P3 |
| Card POS / SmartPOS acquirers (VNPAY, Napas, banks) | card at the counter | Tôi | P3 |

## 4 · Invoices and tax (categories 4–8)
| Provider | Use | Source | Phase |
|---|---|---|---|
| **Hilo** | cash-register invoice at the counter (mẫu số 2), code "M" at once | BA (tested) | P1 |
| **X Invoice** (App for businesses · TVAN for individuals) | invoices with a tax code for B2B; MST lookup API | BA (tested 11/11) | P1 |
| **Viettel S-Invoice** | invoice provider via Invoice Hub | BA (partly tested) · Web | P2 |
| **Bkav eHoadon** | invoice provider via Invoice Hub | BA (untested) · Web | P2 |
| MISA meInvoice, VNPT Invoice, FPT eInvoice, EasyInvoice, Sinvoice, VNInvoice | the household may already use one | Web (used by SMEs) · Tôi | P3 |
| **Casso GDT Hub** (Tổng cục Thuế data) | purchase invoices, tax portal data; household enters eTax login on Cas Link → **legal check N-15 first** | BA | P2 (opt-in) |
| **Casso TVAN / Cas TVAN** | file returns, send self-built invoices; **not tested; not for the pilot** | BA | P3 |
| Other T-VAN (TS24, Thái Sơn, VNPT, Viettel) | same job | Tôi | P3 |
| eTax Mobile (deeplink) | the owner pays tax herself; OPC records the receipt code — **the State does not open payment to third parties** | BA | Tay (deeplink) |
| Remote digital signature: **Cas ID eSign (PDF only)**, VNPT SmartCA, Viettel MySign (Viettel-CA), FPT.eSign, MISA eSign, BkavCA | owner's certificate for invoices / returns; Casso has **no XML signing API** | BA · Web (VNPT, Viettel, FPT) · Tôi (MISA, Bkav) | decision open (Câu 2) |

## 5 · Identity and lookup (categories 9–10)
| Provider | Use | Source | Phase |
|---|---|---|---|
| **Cas ID** (eKYC via the Cas ID app: chip ID + face, 5-minute code) | owner identity; conflicts with "no app install" | BA | P1 (assisted alt.) |
| **Casso IDKit** | MST → name, industry, address | BA (tested) | P1 |
| VNPT eKYC, FPT.AI eKYC | alternative without an app | Tôi | P2 |
| OPC staff on site | assisted identity when no NFC / no Cas ID | BA | Tay |

## 6 · Delivery (category 13) — "own staff link, bus, tracking number" stay first-class
| Provider | Use | Source | Phase |
|---|---|---|---|
| Người của hộ (link for the deliverer), nhà xe (coach companies), tracking number | always available | BA (own staff, bus) | P1 (built-in, no API) |
| GHTK | create shipment, track, COD, weekly settlement | Tôi · Web (exists) | P1 demo / P2 real |
| GHN (Giao Hàng Nhanh) | same | Web (exists) | P2 |
| Viettel Post, VNPost | same; national coverage | Web | P2 |
| J&T Express | same | Tôi | P2 |
| Ninja Van, SPX Express (Shopee), BEST Express | same | Web (Ninja Van, SPX) · Tôi (BEST) | P3 |
| Ahamove, Grab Express, Lalamove | same-day / on-demand in cities | Web (Ahamove) · Tôi | P3 |
| Shipping aggregators (one connection, many carriers) | less setup for the household | Tôi — **business decision** | open |

## 7 · Online selling (category 12) — post-MVP, data model ready
| Provider | Use | Source | Phase |
|---|---|---|---|
| Shopee | orders, payouts, fees, tax withheld | Web (market leader) | P2 |
| TikTok Shop | same; fast growing (now ~44% share) | Web | P2 |
| Lazada, Tiki, Sendo | small / declining shares (Lazada ~3%, Tiki steep decline) | Web | P3 |
| ShopeeFood, GrabFood, BeFood | food delivery orders | Tôi | P3 |
| Website / store platforms: Haravan, Sapo, KiotViet, Nhanh.vn, WooCommerce, Shopify | the household's own web shop | Tôi | P3 |
| Facebook Shop / Live orders | manual add via Zalo/Messenger first | Tôi | Tay |

## 8 · Data in/out and AI (categories 15–17)
| Provider | Use | Source | Phase |
|---|---|---|---|
| Excel / CSV | import opening data, export for the accountant | BA (SCOPE) | P1 |
| Photo / PDF + OCR | invoices, price lists, tin nhắn | BA | P1 |
| Google Sheets | import/export | Tôi | P3 |
| Accounting software exports: MISA, Fast, Bravo | hand-off to the accountant | BA (MISA was in the old spec) · Tôi | P3 |
| AI providers | per ADR 0010 (provider-agnostic) | BA | — |

## What this tells us
1. **The pilot needs only ~9 real connections**: Zalo OA (+ZNS), Casso (MB QR Pay + Transactions), Hilo, X Invoice, Cas ID, IDKit, eTax deeplink — the rest are manual paths.
2. **Casso covers banks, invoices, tax portal, eKYC, lookup in one vendor** — but has **no wallets (MoMo/ZaloPay)**, **no XML signing**, **no shipping, no marketplaces, no chat**.
3. **Open decisions**: digital-signature provider (Câu 2), tax filing path (Câu 1), SePay vs Casso for banks, shipping aggregator vs direct carriers, which marketplaces first (Shopee + TikTok Shop carry ~98% of the big four).
4. **Legal/partner gates**: GDT Hub (N-15), ZNS templates (Zalo approval), BIDV VA contract, Shopee/TikTok Shop open-platform partner approval **[Tôi — verify]**, Meta app review for Messenger **[Tôi — verify]**.

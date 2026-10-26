# Handoff — Onboarding (onboard-*.html, 5 steps · v6.0.0)

<!-- v41:start -->
## v4.1 (current)
> Layout and parts follow DESIGN.md §3 (v4.1). Primary = sea `--act`, one per view; money states use the truth palette. If any older note below disagrees with this block, this block wins.

- **Purpose:** Open a household in ~10 minutes, 5 steps, autosaved; bank and the rest are gates in Sẵn sàng.
- **First read:** Per step: the title question; on ≥1180 the right panel (step map, or the sample proof card on welcome/done).
- **Primary action:** The sticky forward button (one per step); helpers are links.
- **Layout:** ≥1180 two columns (form ≤560 | panel ≤400). <1180 one column + compact strip (current step, why, minutes left). Household is one question "Đây có đúng hộ của chị?" with OPC-prefilled rows; welcome shows the sample proof ("Ví dụ"); bank shows MB → Casso → Quầy OPC read-only; products--review folds the 7 sure items; done folds the recap and leads with reviewing 2 AI-uncertain prices.
- **Also:** Generators: `tools/v4/onboard_aside.py` (panel) then `inert.py` (help dialog).
<!-- v41:end -->


- **Content:** BRIEF §11. **Rules:** DESIGN.md §5 Onboarding. **Flow:** prototype "Đăng ký lần đầu (điện thoại)".
- **Users:** Trần Thị Hai (58, Android phone, self-serve). Field staff Lan does the assisted path on a laptop
  (`onboard-assisted.html`).

## Flow and server state (every step saves; resume opens the next unfinished step)
| # | Screen | Saves | Leaves the app? |
|---|---|---|---|
| — | welcome | — | — |
| 1 | phone → otp | phone verified (L0) | Zalo ZNS (SMS fallback) |
| 2 | household | MST lookup (tax portal) + display name + ngành | — |
| 3 | verify → verify--camera | L1 via vendor web SDK; or staff appointment; or chip via Cas ID (assisted) | camera permission |
| 4 | bank → bank--done | Casso grant; bank holder name compared with verified name (ADR 0011) | Casso hosted page, then returns |
| 5 | products → products--review | items (AI suggestions confirmed by the owner) | camera/mic permission |
| 6 | invoice | invoice-required flag; Hilo link via Casso | — |
| — | firstsale (coach, 3 steps) → done | test order (not revenue) | — |

## Components
- **Shell:** `OnboardingStep` (r-onboard) on every screen except assisted.
- **Inputs and choices:**
  - StepProgress (c-steps)
  - CodeInput (c-otp, shadcn InputOTP)
  - OptionCard big (c-option--big)
  - Field with `data-check` (AI chưa chắc)
- **Guidance:**
  - AssistantAnswer (c-answer)
  - CoachMark (c-coach + anchor)
  - CaptureFrame (c-camera)
- **Feedback:** Banner ok.

The specs per screen are in `bridge/opc-shadcn/onboard-*.md`.

## Behaviour
- **Back:** always available. The step bar is not clickable (no skipping ahead).
- **"Hỏi" opens `onboard-help`** (dialog, full-screen on phone):
  - People come first: call Lan (`tel:`), Zalo deep link, "Nhờ người thân làm giúp" (shares a magic link valid for
    24 h; the relative fills in, the owner confirms with OTP).
  - Then suggested questions and the automatic answer (LLM via the AI port, ADR 0010; no PII in prompts).
- **AI products:**
  - Photo/voice → server extraction → review list. Uncertain fields get `data-check` and "Đúng rồi" / "Xem trong
    ảnh" (opens the photo at the region).
  - Saving keeps every value as shown, and unchecked items are flagged later in Hàng hoá.
- **OTP:** `autocomplete="one-time-code"`; paste fills all boxes; resend after 60 s; SMS fallback.
- **Camera:** the vendor SDK runs inside c-camera. OPC never stores face images (ADR 0011).
- **Casso page:** opens in the same tab and returns to `bank--done` or to an error state (not drawn).
- **Coach:** max 3 steps, "Bỏ qua hướng dẫn" always available, and the test order is excluded from revenue.

## States not drawn yet
- OTP wrong or expired
- MST not found / no MST
- Camera denied
- Verification failed (retry or staff)
- Bank link cancelled or name mismatch (human review)
- AI could not read the photo
- Products empty and "Để sau"
- Resume screen ("Chào chị Hai, còn 3 bước" = home--firstrun)

## Open questions
- Can "Nhờ người thân" complete identity verification for the owner? Proposal: no, only data entry.
- Which eKYC vendor provides the web SDK? Pending quotes (ADR 0011).
- Does the ngành choice prefill the product template, and from which source?

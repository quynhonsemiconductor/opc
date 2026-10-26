<!-- uiux-studio · paste into apps/app/AGENTS.md (or CLAUDE.md) of the OPC repo -->
## Implementing UI from the design

**Source of truth**: `design/apps/app` (extends `design/system`, design v1.0.0, direction F "Biển Chỉ Dẫn").
Read before any UI work, in this order:
1. `design/system/DESIGN.md` (rules, components, patterns, content)
2. `handoff/<screen>.md` (layout, data, states, behaviour)
3. `handoff/bridge/opc-shadcn/<screen>.md` (which component and props to use for every element)
4. `handoff/<screen>.inventory.json` (the component tree with boxes)

The HTML in `screens/` is a **visual reference, not code to copy**. `handoff/annotated/*.html` shows
component boundaries (`data-component`, `data-variant`, `data-part`, `data-state`).

**Stack** (ADR 0007): React 19 + Vite SPA, TanStack Router/Query, Tailwind v4, shadcn/ui.
- Component map: `design/system/maps/opc-shadcn.json`.
- Theme: import `design/system/handoff/tailwind.theme.css` after `tailwindcss` for the OPC utilities
  (`bg-canvas`, `text-ink-3`, `bg-act`, `text-pend`, `text-hero`…).
- Use `handoff/bridge/opc-shadcn/theme.css` for the shadcn variables (`--primary` = act yellow, `--ring` = ink).
- Never hand-copy colours or sizes.

**Rules**
1. Build with shadcn components as mapped in the bridge spec. Every component marked `custom` lives
   **once** in `src/components/opc/` (QuantityStepper, PaymentLadder, MoneyConfirm, Lane, StatusSign,
   MoneyLine, MoneySign, QrPayment, ProductButton, PhoneTabBar, PhoneCartBar…). Never build them inline in a page.
2. No raw values in feature code: colours, spacing, radius and font sizes come from tokens/utilities.
3. **Money states are an enum shared with the API**: `awaiting_customer` → `received_unverified` → `verified`;
   invoices `pending_tax_code` → `has_tax_code`. Map them to StatusSign / MoneyLine / PaymentLadder in exactly
   one place. A payment is never shown as done before `verified`.
4. Contexts are wrappers, not per-page CSS. The counter and phone sheets render inside
   `<div data-density="touch">`; accountant tables later use `data-density="compact"`.
5. Behaviour follows the WAI-ARIA APG pattern named in `design/system/components/registry.json`:
   - Drawer: focus trap, Esc, focus returns to the trigger.
   - Switch: role=switch.
   - Segmented: radio semantics.
   - Stepper: spinbutton.
   - Ladder: `aria-current="step"`.
   - QR status: `aria-live="polite"`.
6. Implement every state listed in the handoff, including the ones marked "not drawn". Ask design for those
   before inventing them.
7. Serve the demo content on fixture routes (`/__design/home`, `/__design/counter`, `/__design/counter-cart`,
   `/__design/counter-payment`) so the visual check compares design, not data. Fixture clock: Thứ Sáu 02/10/2026 10:45.

**Definition of done for a screen** (run from the repo with the dev server up):
```
node ~/.claude/skills/uiux-studio/scripts/verify.mjs design/apps/app <screen> http://localhost:5173/__design/<screen> --qa
```
- It must report PASS at 1440, 1280, 1024 and 390, with no component over its drift threshold and no
  serious or critical a11y violations.
- If a difference is intentional, record it in the handoff ("deviation: … because …") and get design sign-off.
- Otherwise fix the code, not the threshold.

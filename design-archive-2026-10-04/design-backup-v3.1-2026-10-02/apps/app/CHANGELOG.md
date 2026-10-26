# Design changelog

Every change to tokens, components or screens gets an entry. Version: MAJOR = direction/structure change,
MINOR = new component or screen, PATCH = adjustment to an existing one.

## 0.1.0 — 2026-10-01
- Project initialised.

## 1.0.0 — 2026-10-02
- Screens (layout only, on system 1.0.0): home.html, counter.html, counter--payment.html (phone sheet). Optional order-table columns hide ≤1180.
- Lock evaluator (7.8): Home on phone now leads with Tiền hôm nay (page actions move to the tab bar / Thêm; legend replaces the sign panel); new state counter--cart.html (phone cart sheet with steppers) reached from "Sửa giỏ" in the cart bar and from the payment sheet; lanes 2–3 use a 1px quiet outline.

## 1.2.0 — 2026-10-02
- New screens: money.html (+ money--assign dialog), orders.html, invoices.html.
- New states: counter--received / --verified / --cash / --offline / --empty, counter--payment--received / --verified (phone), home--offline, home--firstrun.

## 1.4.0 — 2026-10-02
- Onboarding (15 screens): welcome → phone → otp → household → verify (+camera) → bank (+done) → products (+AI review, help sheet) → invoice → first sale (coach) → done; staff-assisted desktop screen.
- List tools: orders r-listbar (search, date preset, filter, sort) + states filtered / filters / daterange / search / noresult; invoices--accountant (compact, 25 per page, pager).

## 1.5.0 — 2026-10-02
- Onboarding error states ×6; home--loading, orders--loading; order-detail (DH-1040), invoice-detail (00000418).

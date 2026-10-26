# Handoff — Hoá đơn (invoices)

- Visual reference: `../screens/invoices.html`. Content: BRIEF §10.4. Component spec: `bridge/opc-shadcn/invoices.md`.
- **Purpose:** check that every sale has its cash-register e-invoice and tax-authority code (mã CQT).
- **First read:** the pending banner.
- **Primary action:** "Gửi lại" on the invoice that is waiting for its code.

## Layout
- **1440:**
  1. r-page-head (Hilo connection; facts: ký hiệu 2C26MCH · tháng 10: 19 hoá đơn · 7.080.000 ₫)
  2. c-banner--pend + one note line
  3. c-tabs
  4. Table: Số HĐ · Đơn · Giờ · Người mua · Tổng · Loại · Mã CQT (sign + code) · Xem
- **390:** rows stack. The tax code is hidden (`c-table__desk`); order and time fold into the buyer line
  (`c-table__phone`).

## Data
- **Invoice Hub via Casso:** number, symbol, order, issue time, buyer (MST for company invoices), total, type,
  CQT state + code.
- **Status:** poll, because INVOICE webhooks were not observed (ADR 0012).
- **Mã CQT format:** e.g. `M1-26-QN7K2-00000000421`.

## States
- **Drawn:** one waiting for its tax code.
- **Not drawn:**
  - error (Hilo rejected: c-banner--err + reason + "Sửa và gửi lại")
  - invoice detail / PDF preview
  - empty month

## Interactions
- "Gửi lại" re-submits (idempotent per invoice number) and shows c-banner--ok.
- "Xem" opens the detail.
- A waiting invoice is still valid to hand to the customer (copy on the page).

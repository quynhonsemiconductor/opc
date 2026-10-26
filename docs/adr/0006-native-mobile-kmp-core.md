# ADR 0006 — Native mobile (SwiftUI + Jetpack Compose) with a Kotlin Multiplatform shared core

Status: Accepted · 2026-10-01 · delivered in phase F3, after the web-first pilot

## Context
The owner app is the primary surface (counter sale, invoices, tax on the phone; elderly users; cheap
Android devices; offline). Native UI was chosen for platform fidelity and accessibility. Offline sales must
compute money, tax and stock identically on Android, iOS and the server.

## Decision
- iOS: Swift 6.3 + SwiftUI (Xcode 26), deployment target iOS 17. Android: Kotlin 2.4 + Jetpack Compose
  (Material 3), minSdk 26.
- **`shared/core-kmp`**: business rules (cart, money, tax), offline outbox and sync, SQLDelight storage,
  generated API client, mappers — consumed natively by Android and via Swift export by iOS.
- **`shared/test-vectors`**: JSON cases (tax groups, rounding, discounts, thresholds) executed by both
  the Go and KMP test suites; a one-đồng difference fails CI.
- Platform features stay native: VisionKit/CameraX + ML Kit (barcodes), Speech/SpeechRecognizer + TTS
  (Vietnamese, on-device), CoreBluetooth/ESC-POS printers, BackgroundTasks/WorkManager.

## Consequences
Two UI codebases (needs Swift and Kotlin skills); one implementation of the rules that matter most.

## Alternatives rejected
Flutter/React Native (cross-platform UI); pure native without a shared core (rules duplicated 3×).

## Revisit when
The iOS team cannot work with KMP → pure native with mandatory test vectors.

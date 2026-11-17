---
type: Table
title: "AuditLogin — Prisijungimų sekimas"
description: "Kiekvieno prisijungimo metu sukuriamas įrašas, atsekti koks naudotojas prisijungė, su kokia priemone."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/viisp/AuditLogin"
tags: [gov, ivpk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/viisp.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/viisp.csv#L15"
    last_modified: "2026-11-11T14:39:20Z"
---

# AuditLogin — Prisijungimų sekimas

Kiekvieno prisijungimo metu sukuriamas įrašas, atsekti koks naudotojas prisijungė, su kokia priemone.

- **Model:** `datasets/gov/ivpk/viisp/AuditLogin`[^manifest]
- **Dataset:** [datasets/gov/ivpk/viisp](../viisp.md) (`datasets/gov/ivpk/viisp`)
- **Manifest CSV:** [datasets/gov/ivpk/viisp.csv#L15](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/viisp.csv#L15)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/viisp/AuditLogin`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Unikalus prisijungimo ID | — |
| `login_date` | `datetime` | `S` | `4` | `open` | — | Prisijungimo data | — |
| `auth_provider` | `string` | — | `4` | `open` | — | Prisijungimo būdas | Su kokiu prisijungimo būdu prisijungta |
| `country_code` | `string` | — | `4` | `open` | — | Šalies kodas | Valstybės iš kurios prisijungė kodas. Pvz. LT, IT, LV |
| `country_name` | `string` | — | `4` | `open` | — | Šalies pavadinimas | Valstybės pavadinimas iš kurios prisijungė |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/viisp.csv

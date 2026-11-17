---
type: Table
title: "Uzsakymas — Mokamos sumos už ortopedijos technines ir medicinos priemones"
description: "Informacija apie PSDF biudžeto išlaidas ortopedijos techninėms priemonėms"
resource: "https://get.data.gov.lt/datasets/gov/vlk/otp_sumos/Uzsakymas"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/otp_sumos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/otp_sumos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Uzsakymas — Mokamos sumos už ortopedijos technines ir medicinos priemones

Informacija apie PSDF biudžeto išlaidas ortopedijos techninėms priemonėms

- **Model:** `datasets/gov/vlk/otp_sumos/Uzsakymas`[^manifest]
- **Dataset:** [datasets/gov/vlk/otp_sumos](../otp_sumos.md) (`datasets/gov/vlk/otp_sumos`)
- **Manifest CSV:** [datasets/gov/vlk/otp_sumos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/otp_sumos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/otp_sumos/Uzsakymas`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `data` | `date` | — | `4` | `open` | — | Data | Ataskaitinio laikotarpio data mėnesio tikslumu |
| `istaiga` | `ref` | [Istaiga](Istaiga.md) | `4` | `open` | — | Įstaigos ID | — |
| `tipas` | `ref` | [Tipas](Tipas.md) | `4` | `open` | — | Nuoroda į Tipas | — |
| `suma` | `number` | — | `2` | `open` | — | Suma eurais | Kompensuojamoji suma eurais, sumokėta už OTP |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `suma` | `update(type: "money, ref: "EUR")"` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/otp_sumos.csv

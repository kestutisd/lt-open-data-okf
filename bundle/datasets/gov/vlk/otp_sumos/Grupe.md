---
type: Table
title: "Grupe — Ortopedijos techninių ir medicinos priemonių tipai"
description: "Informacija apie ortopedijos techninių ir medicinos priemonių tipus"
resource: "https://get.data.gov.lt/datasets/gov/vlk/otp_sumos/Grupe"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/otp_sumos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/otp_sumos.csv#L18"
    last_modified: "2026-11-11T14:39:20Z"
---

# Grupe — Ortopedijos techninių ir medicinos priemonių tipai

Informacija apie ortopedijos techninių ir medicinos priemonių tipus

- **Model:** `datasets/gov/vlk/otp_sumos/Grupe`[^manifest]
- **Dataset:** [datasets/gov/vlk/otp_sumos](../otp_sumos.md) (`datasets/gov/vlk/otp_sumos`)
- **Manifest CSV:** [datasets/gov/vlk/otp_sumos.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/otp_sumos.csv#L18)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/otp_sumos/Grupe`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `kodas` | `string` | — | `4` | `open` | — | OTP tipo kodas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | OTP tipo pavadinimas | — |
| `klase` | `ref` | [Klase](Klase.md) | `4` | `open` | — | Nuoroda į Klasė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/otp_sumos.csv

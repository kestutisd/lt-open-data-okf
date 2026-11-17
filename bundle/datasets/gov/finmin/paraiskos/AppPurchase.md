---
type: Table
title: "AppPurchase — Vykdomi ir iki paraiškos pateikimo įvykdyti pirkimai"
description: "Spinta table datasets/gov/finmin/paraiskos/AppPurchase (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/paraiskos/AppPurchase"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L59"
    last_modified: "2026-11-11T14:39:20Z"
---

# AppPurchase — Vykdomi ir iki paraiškos pateikimo įvykdyti pirkimai

- **Model:** `datasets/gov/finmin/paraiskos/AppPurchase`[^manifest]
- **Dataset:** [datasets/gov/finmin/paraiskos](../paraiskos.md) (`datasets/gov/finmin/paraiskos`)
- **Manifest CSV:** [datasets/gov/finmin/paraiskos.csv#L59](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L59)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/paraiskos/AppPurchase`
- **Primary Key (`ref`):** `app_purchase_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `app_purchase_id` | `string` | — | `4` | `open` | — | Pirkimo identifikatorius | — |
| `project` | `ref` | [Project](Project.md) | `4` | `open` | — | Projekto identifikatorius | — |
| `name` | `string` | — | `1` | `open` | — | Pirkimo pavadinimas ir Nr | — |
| `part` | `string` | — | `1` | `open` | — | Pirkimo dalis | — |
| `value` | `number` | — | `2` | `open` | — | Pirkimo dalies vertė | — |
| `info` | `string` | — | `1` | `open` | — | Informacija apie pirkimą | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `value` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv

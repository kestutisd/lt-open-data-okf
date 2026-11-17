---
type: Table
title: "IndicatorsKeyFamiliesI18N — IndicatorsKeyFamiliesI18N"
description: "Lentelė, kurioje yra saugomas dimensijų aprašymas"
resource: "https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsKeyFamiliesI18N"
tags: [gov, ird, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L47"
    last_modified: "2026-11-11T14:39:20Z"
---

# IndicatorsKeyFamiliesI18N — IndicatorsKeyFamiliesI18N

Lentelė, kurioje yra saugomas dimensijų aprašymas

- **Model:** `datasets/gov/ird/nusikalstamumas/IndicatorsKeyFamiliesI18N`[^manifest]
- **Dataset:** [datasets/gov/ird/nusikalstamumas](../nusikalstamumas.md) (`datasets/gov/ird/nusikalstamumas`)
- **Manifest CSV:** [datasets/gov/ird/nusikalstamumas.csv#L47](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L47)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsKeyFamiliesI18N`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Identifikacijos kodas | Identifikacijos kodas |
| `lang` | `string` | — | `3` | `open` | — | Kalba | Duomenų rinkinio kalba (LT/EN) |
| `target` | `ref` | [IndicatorsKeyFamilie](IndicatorsKeyFamilie.md) | `4` | `open` | — | Kodas | Nusikalstama veika ar asmuo |
| `title` | `string` | — | `3` | `open` | — | Rinkinio pavadinimas | Duomenų rinkinys apie nusikalstamas veikas Lietuvoje/ Duomenų rinkinys pagal įtariamus / kaltinamus ir nukentėjusius asmenis |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv

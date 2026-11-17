---
type: Table
title: "IndicatorsMapping — IndicatorsMapping"
description: "Lentelė, kurioje yra saugomi duomenys apie ataskaitas"
resource: "https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsMapping"
tags: [gov, ird, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L53"
    last_modified: "2026-11-11T14:39:20Z"
---

# IndicatorsMapping — IndicatorsMapping

Lentelė, kurioje yra saugomi duomenys apie ataskaitas

- **Model:** `datasets/gov/ird/nusikalstamumas/IndicatorsMapping`[^manifest]
- **Dataset:** [datasets/gov/ird/nusikalstamumas](../nusikalstamumas.md) (`datasets/gov/ird/nusikalstamumas`)
- **Manifest CSV:** [datasets/gov/ird/nusikalstamumas.csv#L53](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L53)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsMapping`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `date_from` | `date` | `M` | `4` | `open` | — | Data nuo | Ataskaitos galiojimo data nuo |
| `date_to` | `date` | `M` | `4` | `open` | — | Data iki | Ataskaitos galiojimo data iki |
| `form_code` | `string` | — | `4` | `open` | — | Ataskaitos kodas | Iš kokios ataskaitos pateikiami duomenys |
| `id` | `integer` | — | `4` | `open` | — | Identifikatorius | Ataskaitai priskirtas kodas |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv

---
type: Table
title: "IndicatorsOb — IndicatorsOb"
description: "Lentelė, kurioje yra saugomos rodiklių reikšmės"
resource: "https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsOb"
tags: [gov, ird, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L65"
    last_modified: "2026-11-11T14:39:20Z"
---

# IndicatorsOb — IndicatorsOb

Lentelė, kurioje yra saugomos rodiklių reikšmės

- **Model:** `datasets/gov/ird/nusikalstamumas/IndicatorsOb`[^manifest]
- **Dataset:** [datasets/gov/ird/nusikalstamumas](../nusikalstamumas.md) (`datasets/gov/ird/nusikalstamumas`)
- **Manifest CSV:** [datasets/gov/ird/nusikalstamumas.csv#L65](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L65)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsOb`
- **Primary Key (`ref`):** `item, dt`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `dt` | `string` | — | `2` | `open` | — | Data | Laikotarpis, kurį apima duomenų rinkinys, pvz.: 2020-07 - 2020 metų spalio mėn. |
| `item` | `ref` | [IndicatorsItem](IndicatorsItem.md) | `4` | `open` | — | Kodas | Dimensijos ID iš Indicatorsitem lentelės |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv

---
type: Table
title: "IndicatorsMetadata — IndicatorsMetadata"
description: "Lentelė, kurioje yra saugomos rodiklių metaduomenys"
resource: "https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsMetadata"
tags: [gov, ird, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L59"
    last_modified: "2026-11-11T14:39:20Z"
---

# IndicatorsMetadata — IndicatorsMetadata

Lentelė, kurioje yra saugomos rodiklių metaduomenys

- **Model:** `datasets/gov/ird/nusikalstamumas/IndicatorsMetadata`[^manifest]
- **Dataset:** [datasets/gov/ird/nusikalstamumas](../nusikalstamumas.md) (`datasets/gov/ird/nusikalstamumas`)
- **Manifest CSV:** [datasets/gov/ird/nusikalstamumas.csv#L59](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L59)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsMetadata`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | Identifikacijos kodas | Identifikacijos kodas |
| `item` | `ref` | [IndicatorsItem](IndicatorsItem.md) | `4` | `open` | — | Kodas | Dimensijos ID iš Indicatorsitem lentelės |
| `key` | `string` | — | `2` | `open` | — | Dimensijos raktas | Dimensijų kodiniai pavadinimai |
| `value` | `string` | — | `2` | `open` | — | Dimensijos reikšmė | Pasirinktos dimensijos reikšmė |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv

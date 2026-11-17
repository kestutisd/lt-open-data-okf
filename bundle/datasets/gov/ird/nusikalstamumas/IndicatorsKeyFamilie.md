---
type: Table
title: "IndicatorsKeyFamilie — IndicatorsKeyFamilie"
description: "Lentelė, kurioje saugomi rodikliai ir juos sudarančios dimensijos"
resource: "https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsKeyFamilie"
tags: [gov, ird, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L41"
    last_modified: "2026-11-11T14:39:20Z"
---

# IndicatorsKeyFamilie — IndicatorsKeyFamilie

Lentelė, kurioje saugomi rodikliai ir juos sudarančios dimensijos

- **Model:** `datasets/gov/ird/nusikalstamumas/IndicatorsKeyFamilie`[^manifest]
- **Dataset:** [datasets/gov/ird/nusikalstamumas](../nusikalstamumas.md) (`datasets/gov/ird/nusikalstamumas`)
- **Manifest CSV:** [datasets/gov/ird/nusikalstamumas.csv#L41](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L41)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsKeyFamilie`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | — | `2` | `open` | — | Kodas | Nusikalstamos veikos ar asmenys |
| `dimensions` | `string` | — | `2` | `open` | — | Dimensijos kodas | Kodų sąrašas priskirtas nusikalstamoms veikoms ar asmenims |
| `id` | `integer` | — | `4` | `open` | — | Identifikacijos kodas | Identifikacijos kodas |
| `main_dimension` | `ref` | [IndicatorsDimension](IndicatorsDimension.md) | `4` | `open` | — | Kodas | Nusikalstama veika ar asmuo |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv

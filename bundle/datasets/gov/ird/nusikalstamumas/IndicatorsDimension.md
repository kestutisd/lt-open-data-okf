---
type: Table
title: "IndicatorsDimension — IndicatorsDimension"
description: "Lentelė, kurioje saugomas sąrašas identifikuotų dimensijų ir jų pavadinimai, kodai ir aprašymai"
resource: "https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsDimension"
tags: [gov, ird, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# IndicatorsDimension — IndicatorsDimension

Lentelė, kurioje saugomas sąrašas identifikuotų dimensijų ir jų pavadinimai, kodai ir aprašymai

- **Model:** `datasets/gov/ird/nusikalstamumas/IndicatorsDimension`[^manifest]
- **Dataset:** [datasets/gov/ird/nusikalstamumas](../nusikalstamumas.md) (`datasets/gov/ird/nusikalstamumas`)
- **Manifest CSV:** [datasets/gov/ird/nusikalstamumas.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ird/nusikalstamumas.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ird/nusikalstamumas/IndicatorsDimension`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | — | `2` | `open` | — | Dimensijos kodas | Dimensijos kodas - NV tipas, savivaldybė, straipsnis... |
| `id` | `integer` | — | `4` | `open` | — | Dimensijos identifikatorius | Dimensijos identifikatorius - kodas |
| `options` | `string` | — | `2` | `open` | — | Galimybės | Aprašymo ilgis LEFT(`options`, 256) |
| `position` | `integer` | — | `4` | `open` | — | Pozicija ataskaitoje | Pozicija ataskaitoje |

[^manifest]: atviriduomenys/manifest — datasets/gov/ird/nusikalstamumas.csv

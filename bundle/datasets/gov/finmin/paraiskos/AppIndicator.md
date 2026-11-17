---
type: Table
title: "AppIndicator — Paraiškos produkto ir rezultato stebėsenos rodikliai"
description: "Spinta table datasets/gov/finmin/paraiskos/AppIndicator (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/paraiskos/AppIndicator"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L68"
    last_modified: "2026-11-11T14:39:20Z"
---

# AppIndicator — Paraiškos produkto ir rezultato stebėsenos rodikliai

- **Model:** `datasets/gov/finmin/paraiskos/AppIndicator`[^manifest]
- **Dataset:** [datasets/gov/finmin/paraiskos](../paraiskos.md) (`datasets/gov/finmin/paraiskos`)
- **Manifest CSV:** [datasets/gov/finmin/paraiskos.csv#L68](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L68)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/paraiskos/AppIndicator`
- **Primary Key (`ref`):** `app_indicator_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `app_indicator_id` | `string` | — | `4` | `open` | — | Paraiškos rodiklio identifikatorius | — |
| `project` | `ref` | [Project](Project.md) | `4` | `open` | — | Projekto identifikatorius | — |
| `measure_indicator` | `ref` | [/datasets/gov/finmin/kvietimai/MeasureIndicator](../kvietimai/MeasureIndicator.md) | `4` | `open` | — | Priemonės rodiklio identifikatorius | — |
| `value` | `number` | — | `4` | `open` | — | Rodiklio siektina reikšmė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv

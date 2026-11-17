---
type: Table
title: "AppTask — Paraiškos uždaviniai"
description: "Spinta table datasets/gov/finmin/paraiskos/AppTask (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/paraiskos/AppTask"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L82"
    last_modified: "2026-11-11T14:39:20Z"
---

# AppTask — Paraiškos uždaviniai

- **Model:** `datasets/gov/finmin/paraiskos/AppTask`[^manifest]
- **Dataset:** [datasets/gov/finmin/paraiskos](../paraiskos.md) (`datasets/gov/finmin/paraiskos`)
- **Manifest CSV:** [datasets/gov/finmin/paraiskos.csv#L82](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L82)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/paraiskos/AppTask`
- **Primary Key (`ref`):** `app_task_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `app_task_id` | `string` | — | `4` | `open` | — | Paraiškos uždavinio identifikatorius | — |
| `project` | `ref` | [Project](Project.md) | `4` | `open` | — | Projekto identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Projekto uždavinio numeris | — |
| `name` | `string` | — | `4` | `open` | — | Projekto uždavinio pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv

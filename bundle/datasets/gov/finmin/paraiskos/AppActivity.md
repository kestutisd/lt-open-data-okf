---
type: Table
title: "AppActivity — Paraiškos uždavinio veiklos"
description: "Spinta table datasets/gov/finmin/paraiskos/AppActivity (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/paraiskos/AppActivity"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L88"
    last_modified: "2026-11-11T14:39:20Z"
---

# AppActivity — Paraiškos uždavinio veiklos

- **Model:** `datasets/gov/finmin/paraiskos/AppActivity`[^manifest]
- **Dataset:** [datasets/gov/finmin/paraiskos](../paraiskos.md) (`datasets/gov/finmin/paraiskos`)
- **Manifest CSV:** [datasets/gov/finmin/paraiskos.csv#L88](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L88)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/paraiskos/AppActivity`
- **Primary Key (`ref`):** `app_activity_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `app_activity_id` | `string` | — | `4` | `open` | — | Paraiškos uždavinio veiklos identifikatorius | — |
| `app_task` | `ref` | [AppTask](AppTask.md) | `4` | `open` | — | Paraiškos uždavinio identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Projekto veiklos numeris | — |
| `name` | `string` | — | `4` | `open` | — | Projekto veiklos pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv

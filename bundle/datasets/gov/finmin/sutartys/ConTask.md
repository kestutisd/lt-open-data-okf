---
type: Table
title: "ConTask — Sutarties uždaviniai"
description: "Spinta table datasets/gov/finmin/sutartys/ConTask (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConTask"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L132"
    last_modified: "2026-11-11T14:39:20Z"
---

# ConTask — Sutarties uždaviniai

- **Model:** `datasets/gov/finmin/sutartys/ConTask`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L132](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L132)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConTask`
- **Primary Key (`ref`):** `con_task_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `con_task_id` | `string` | — | `4` | `open` | — | Sutarties uždavinio identifikatorius | — |
| `project` | `ref` | [Contract](Contract.md) | `4` | `open` | — | Projekto identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Projekto uždavinio numeris | — |
| `task` | `string` | — | `4` | `open` | — | Projekto uždavinio pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv

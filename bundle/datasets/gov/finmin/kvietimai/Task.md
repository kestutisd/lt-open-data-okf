---
type: Table
title: "Task — Investicinio prioriteto uždavinys"
description: "Spinta table datasets/gov/finmin/kvietimai/Task (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/kvietimai/Task"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L60"
    last_modified: "2026-11-11T14:39:20Z"
---

# Task — Investicinio prioriteto uždavinys

- **Model:** `datasets/gov/finmin/kvietimai/Task`[^manifest]
- **Dataset:** [datasets/gov/finmin/kvietimai](../kvietimai.md) (`datasets/gov/finmin/kvietimai`)
- **Manifest CSV:** [datasets/gov/finmin/kvietimai.csv#L60](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L60)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/kvietimai/Task`
- **Primary Key (`ref`):** `task_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `task_id` | `string` | — | `4` | `open` | — | Investicinio prioriteto uždavinio identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Uždavinio numeris | — |
| `name` | `string` | — | `4` | `open` | — | Uždavinio pavadinimas | — |
| `priority` | `ref` | [Priority](Priority.md) | `4` | `open` | — | Prioriteto identifikatorius | — |
| `invest_priority_number` | `string` | — | `4` | `open` | — | Investicinio prioriteto numeris | — |
| `invest_priority_name` | `string` | — | `4` | `open` | — | Investicinio prioriteto pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv

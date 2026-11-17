---
type: Table
title: "Measure — Investicinio prioriteto uždavinio priemonė"
description: "Spinta table datasets/gov/finmin/kvietimai/Measure (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/kvietimai/Measure"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Measure — Investicinio prioriteto uždavinio priemonė

- **Model:** `datasets/gov/finmin/kvietimai/Measure`[^manifest]
- **Dataset:** [datasets/gov/finmin/kvietimai](../kvietimai.md) (`datasets/gov/finmin/kvietimai`)
- **Manifest CSV:** [datasets/gov/finmin/kvietimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/kvietimai/Measure`
- **Primary Key (`ref`):** `measure_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `measure_id` | `string` | — | `4` | `open` | — | Priemonės identifikatorius | — |
| `task` | `ref` | [Task](Task.md) | `4` | `open` | — | Uždavinio identifikatorius | — |
| `fund_id` | `string` | — | `3` | `open` | — | Fondo identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Priemonės numeris | — |
| `name` | `string` | — | `4` | `open` | — | Priemonės pavadinimas | — |
| `impl_inst` | `string` | — | `2` | `open` | — | Įgyvendinančioji institucija | — |
| `intr_inst` | `string` | — | `2` | `open` | — | Tarpinė institucija | — |
| `selection_method` | `string` | — | `3` | `open` | — | Projektų atrankos būdas | — |
| `joint_measure_id` | `string` | — | `4` | `open` | — | Jungtinės priemonės identifikatorius | — |
| `joint_measure_number` | `string` | — | `4` | `open` | — | Jungtinės priemonės numeris | — |
| `joint_measure_name` | `string` | — | `4` | `open` | — | Jungtinės priemonės pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv

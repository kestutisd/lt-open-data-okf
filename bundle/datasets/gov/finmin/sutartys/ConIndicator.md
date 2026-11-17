---
type: Table
title: "ConIndicator — Sutarties produkto ir rezultato stebėsenos rodikliai"
description: "Spinta table datasets/gov/finmin/sutartys/ConIndicator (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConIndicator"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L66"
    last_modified: "2026-11-11T14:39:20Z"
---

# ConIndicator — Sutarties produkto ir rezultato stebėsenos rodikliai

- **Model:** `datasets/gov/finmin/sutartys/ConIndicator`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L66](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L66)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConIndicator`
- **Primary Key (`ref`):** `con_indicator_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `con_indicator_id` | `string` | — | `4` | `open` | — | Sutarties rodiklio identifikatorius | — |
| `project` | `ref` | [Contract](Contract.md) | `4` | `open` | — | Projekto identifikatorius | — |
| `measure_indicator` | `ref` | [/datasets/gov/finmin/kvietimai/MeasureIndicator](../kvietimai/MeasureIndicator.md) | `4` | `open` | — | Priemonės stebėsenos rodiklio identifikatorius | — |
| `value` | `number` | — | `4` | `open` | — | Rodiklio siektina reikšmė | Rodiklio aprašymo lentelėje nurodytais vienetais |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv

---
type: Table
title: "ConPhIndicator — Sutarties uždavinio veiklos fiziniai rodikliai"
description: "Spinta table datasets/gov/finmin/sutartys/ConPhIndicator (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConPhIndicator"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L138"
    last_modified: "2026-11-11T14:39:20Z"
---

# ConPhIndicator — Sutarties uždavinio veiklos fiziniai rodikliai

- **Model:** `datasets/gov/finmin/sutartys/ConPhIndicator`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L138](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L138)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConPhIndicator`
- **Primary Key (`ref`):** `con_ph_indicator_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `con_ph_indicator_id` | `string` | — | `4` | `open` | — | Sutarties uždavinio veiklos fizinio rodiklio identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Fizinio rodiklio numeris | — |
| `unit` | `string` | — | `4` | `open` | — | Fizinio rodiklio matavimo vienetas | — |
| `aim` | `number` | — | `4` | `open` | — | Fizinio rodiklio siekiama reikšmė | — |
| `task` | `ref` | [ConTask](ConTask.md) | `4` | `open` | — | Sutarties uždavinys | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv

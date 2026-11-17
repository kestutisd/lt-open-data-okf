---
type: Table
title: "PayIndicator — Projekto mokėjimo prašymo dalies Nr. 1 produkto ir rezultato stebėsenos rodikliai"
description: "Spinta table datasets/gov/finmin/sutartys/PayIndicator (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayIndicator"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L227"
    last_modified: "2026-11-11T14:39:20Z"
---

# PayIndicator — Projekto mokėjimo prašymo dalies Nr. 1 produkto ir rezultato stebėsenos rodikliai

- **Model:** `datasets/gov/finmin/sutartys/PayIndicator`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L227](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L227)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PayIndicator`
- **Primary Key (`ref`):** `pay_indicator_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pay_indicator_id` | `string` | — | `4` | `open` | — | Projekto mokėjimo prašymo dalies stebėsenos rodiklio identifikatorius | — |
| `payment` | `ref` | [Payment](Payment.md) | `4` | `open` | — | Mokėjimo prašymo identifikatorius | — |
| `measure_indicator` | `ref` | [/datasets/gov/finmin/kvietimai/MeasureIndicator](../kvietimai/MeasureIndicator.md) | `4` | `open` | — | Priemonės stebėsenos rodiklio identifikatorius | — |
| `name` | `string` | — | `4` | `open` | — | Rodiklio pavadinimas | — |
| `code` | `string` | — | `4` | `open` | — | Rodiklio kodas | — |
| `type` | `string` | — | `3` | `open` | — | Rodiklio tipas | — |
| `unit` | `string` | — | `4` | `open` | — | Siektinos reikšmės matavimo vienetas | — |
| `con_value` | `number` | — | `4` | `open` | — | Rodiklio siektina reikšmė | — |
| `pay_value` | `number` | — | `4` | `open` | — | Rodiklio pasiekta reikšmė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv

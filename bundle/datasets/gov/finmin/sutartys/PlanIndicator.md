---
type: Table
title: "PlanIndicator — Projekto mokėjimo prašymo teikimo grafiko planuojamo mokėjimo prašymo stebėsenos rodikliai, įtraukti į veiklos peržiūros planą"
description: "Spinta table datasets/gov/finmin/sutartys/PlanIndicator (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PlanIndicator"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L364"
    last_modified: "2026-11-11T14:39:20Z"
---

# PlanIndicator — Projekto mokėjimo prašymo teikimo grafiko planuojamo mokėjimo prašymo stebėsenos rodikliai, įtraukti į veiklos peržiūros planą

- **Model:** `datasets/gov/finmin/sutartys/PlanIndicator`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L364](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L364)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PlanIndicator`
- **Primary Key (`ref`):** `plan_indicator_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `plan_indicator_id` | `string` | — | `4` | `open` | — | Planuojamo mokėjimo prašymo stebėsenos rodiklio identifikatorius | — |
| `plan_payment` | `ref` | [PlanPayment](PlanPayment.md) | `4` | `open` | — | Planuojamo mokėjimo prašymo identifikatorius | — |
| `measure_indicator` | `ref` | [/datasets/gov/finmin/kvietimai/MeasureIndicator](../kvietimai/MeasureIndicator.md) | `4` | `open` | — | Priemonės stebėsenos rodiklio identifikatorius | — |
| `name` | `string` | — | `4` | `open` | — | Rodiklio pavadinimas | — |
| `code` | `string` | — | `4` | `open` | — | Rodiklio kodas | — |
| `type` | `string` | — | `3` | `open` | — | Rodiklio tipas | — |
| `unit` | `string` | — | `4` | `open` | — | Siektinos reikšmės matavimo vienetas | — |
| `plan_value` | `number` | — | `4` | `open` | — | Numatoma deklaruoti stebėsenos rodiklio pasiekimo reikšmė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv

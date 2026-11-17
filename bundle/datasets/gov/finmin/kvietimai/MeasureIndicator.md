---
type: Table
title: "MeasureIndicator — Priemonės stebėsenos rodiklis"
description: "Spinta table datasets/gov/finmin/kvietimai/MeasureIndicator (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/kvietimai/MeasureIndicator"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L41"
    last_modified: "2026-11-11T14:39:20Z"
---

# MeasureIndicator — Priemonės stebėsenos rodiklis

- **Model:** `datasets/gov/finmin/kvietimai/MeasureIndicator`[^manifest]
- **Dataset:** [datasets/gov/finmin/kvietimai](../kvietimai.md) (`datasets/gov/finmin/kvietimai`)
- **Manifest CSV:** [datasets/gov/finmin/kvietimai.csv#L41](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L41)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/kvietimai/MeasureIndicator`
- **Primary Key (`ref`):** `measure_indicator_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `measure_indicator_id` | `string` | — | `4` | `open` | — | Priemonės stebėsenos rodiklio identifikatorius | — |
| `measure` | `ref` | [Measure](Measure.md) | `4` | `open` | — | Priemonės identifikatorius | — |
| `name` | `string` | — | `4` | `open` | — | Rodiklio pavadinimas | — |
| `code` | `string` | — | `4` | `open` | — | Rodiklio kodas | — |
| `type` | `string` | — | `3` | `open` | — | Rodiklio tipas | — |
| `ach_moment` | `string` | — | `3` | `open` | — | Rodiklio pasiekimo momentas | — |
| `unit` | `string` | — | `4` | `open` | — | Siektinos ir tarpinės reikšmių matavimo vienetas | — |
| `pip_intr_value` | `number` | — | `4` | `open` | — | PIP tarpinė reikšmė | — |
| `pip_target_value` | `number` | — | `4` | `open` | — | PIP siektina reikšmė | — |
| `base_indicator_type` | `string` | — | `3` | `open` | — | Bazinio rodiklio tipas | — |
| `base_indicator_code` | `string` | — | `4` | `open` | — | Bazinio rodiklio kodas | — |
| `base_indicator_name` | `string` | — | `4` | `open` | — | Bazinio rodiklio pavadinimas | — |
| `base_indicator_unit` | `string` | — | `3` | `open` | — | Bazinio rodiklio matavimo vienetas | — |
| `change_indicator_type` | `string` | — | `3` | `open` | — | Pokyčio rodiklio tipas | — |
| `change_indicator_code` | `string` | — | `4` | `open` | — | Pokyčio rodiklio kodas | — |
| `change_indicator_name` | `string` | — | `4` | `open` | — | Pokyčio rodiklio pavadinimas | — |
| `change_indicator_unit` | `string` | — | `3` | `open` | — | Pokyčio rodiklio matavimo vienetas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv

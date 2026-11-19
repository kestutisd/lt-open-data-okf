---
type: Table
title: "MeasureIndicator — Priemonės stebėsenos rodiklis"
description: "Spinta table datasets/gov/finmin/kvietimai/MeasureIndicator (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/kvietimai/MeasureIndicator"
tags: [gov, finmin, measureindicator, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L41"
    title: "atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv#L41"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2159/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/kvietimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# MeasureIndicator — Priemonės stebėsenos rodiklis

- **Model:** `datasets/gov/finmin/kvietimai/MeasureIndicator`[^manifest]
- **Dataset:** [2014-2020 m. Europos Sąjungos fondų kvietimų teikti paraiškas ir priemonių duomenys](../kvietimai.md) (`datasets/gov/finmin/kvietimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/kvietimai.csv#L41](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L41)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/kvietimai/MeasureIndicator` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `measure_indicator_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `measure_indicator_id` | `string` | — | `4` | `open` | — | Priemonės stebėsenos rodiklio identifikatorius | — |
| `measure` | `ref` | [Measure](Measure.md) (`level=4 UUID`: `measure._id`) | `4` | `open` | — | Priemonės identifikatorius | — |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv#L41 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L41)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/kvietimai (https://data.gov.lt/datasets/2159/)

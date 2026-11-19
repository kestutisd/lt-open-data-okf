---
type: Table
title: "Call — Kvietimas / patvirtintas sąrašas"
description: "Spinta table datasets/gov/finmin/kvietimai/Call (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/kvietimai/Call"
tags: [gov, finmin, call, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L20"
    title: "atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv#L20"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2159/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/kvietimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Call — Kvietimas / patvirtintas sąrašas

- **Model:** `datasets/gov/finmin/kvietimai/Call`[^manifest]
- **Dataset:** [2014-2020 m. Europos Sąjungos fondų kvietimų teikti paraiškas ir priemonių duomenys](../kvietimai.md) (`datasets/gov/finmin/kvietimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/kvietimai.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L20)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/kvietimai/Call` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `call_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `call_id` | `string` | — | `4` | `open` | — | Kvietimo / patvirtinto sąrašo identifikatorius | — |
| `measure` | `ref` | [Measure](Measure.md) (`level=4 UUID`: `measure._id`) | `4` | `open` | — | Priemonės identifikatorius | — |
| `joint_measure` | `ref` | [Measure](Measure.md) (`level=4 UUID` via `Measure[joint_measure_id]`: `joint_measure._id`) | `4` | `open` | — | Jungtinės priemonės identifikatorius | — |
| `long_number` | `string` | — | `4` | `open` | — | Pilnas numeris | — |
| `short_number` | `string` | — | `4` | `open` | — | Trumpasis numeris | — |
| `name` | `string` | — | `4` | `open` | — | Pavadinimas | — |
| `type` | `string` | — | `4` | `open` | — | Tipas | — |
| `ann_date` | `date` | `D` | `4` | `open` | — | Kvietimo / patvirtinto sąrašo paskelbimo data | — |
| `impl_inst` | `string` | — | `2` | `open` | — | Įgyvendinančioji institucija | — |
| `period_from` | `date` | `D` | `4` | `open` | — | Paraiškų pateikimo laikotarpio pradžia | — |
| `period_till` | `date` | `D` | `4` | `open` | — | Paraiškų pateikimo laikotarpio pabaiga | — |
| `eu_amount` | `number` | — | `2` | `open` | — | ES fondų lėšų suma | — |
| `gf_amount` | `number` | — | `2` | `open` | — | LR valstybės biudžeto lėšų suma | — |
| `executor_amount` | `number` | — | `2` | `open` | — | Patvirtinto sąrašo projekto vykdytojo ir (ar) partnerio (-ių) lėšos | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `type` | `"1"` | — | — | Kvietimas | — |
| `type` | `"2"` | — | — | Patvirtintas sąrašas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eu_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `gf_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `executor_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv#L20 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L20)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/kvietimai (https://data.gov.lt/datasets/2159/)

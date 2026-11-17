---
type: Table
title: "Call — Kvietimas / patvirtintas sąrašas"
description: "Spinta table datasets/gov/finmin/kvietimai/Call (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/kvietimai/Call"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L20"
    last_modified: "2026-11-11T14:39:20Z"
---

# Call — Kvietimas / patvirtintas sąrašas

- **Model:** `datasets/gov/finmin/kvietimai/Call`[^manifest]
- **Dataset:** [datasets/gov/finmin/kvietimai](../kvietimai.md) (`datasets/gov/finmin/kvietimai`)
- **Manifest CSV:** [datasets/gov/finmin/kvietimai.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L20)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/kvietimai/Call`
- **Primary Key (`ref`):** `call_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `call_id` | `string` | — | `4` | `open` | — | Kvietimo / patvirtinto sąrašo identifikatorius | — |
| `measure` | `ref` | [Measure](Measure.md) | `4` | `open` | — | Priemonės identifikatorius | — |
| `joint_measure` | `ref` | [Measure[joint_measure_id]](Measure.md) | `4` | `open` | — | Jungtinės priemonės identifikatorius | — |
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

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `type` | `"1"` | — | — | Kvietimas | — |
| `type` | `"2"` | — | — | Patvirtintas sąrašas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `eu_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `gf_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |
| `executor_amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv

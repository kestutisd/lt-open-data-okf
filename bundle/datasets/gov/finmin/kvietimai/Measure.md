---
type: Table
title: "Measure — Investicinio prioriteto uždavinio priemonė"
description: "Spinta table datasets/gov/finmin/kvietimai/Measure (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/kvietimai/Measure"
tags: [gov, finmin, measure, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2159/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/kvietimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Measure — Investicinio prioriteto uždavinio priemonė

- **Model:** `datasets/gov/finmin/kvietimai/Measure`[^manifest]
- **Dataset:** [2014-2020 m. Europos Sąjungos fondų kvietimų teikti paraiškas ir priemonių duomenys](../kvietimai.md) (`datasets/gov/finmin/kvietimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/kvietimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/kvietimai/Measure` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `measure_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `measure_id` | `string` | — | `4` | `open` | — | Priemonės identifikatorius | — |
| `task` | `ref` | [Task](Task.md) (`level=4 UUID`: `task._id`) | `4` | `open` | — | Uždavinio identifikatorius | — |
| `fund_id` | `string` | — | `3` | `open` | — | Fondo identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Priemonės numeris | — |
| `name` | `string` | — | `4` | `open` | — | Priemonės pavadinimas | — |
| `impl_inst` | `string` | — | `2` | `open` | — | Įgyvendinančioji institucija | — |
| `intr_inst` | `string` | — | `2` | `open` | — | Tarpinė institucija | — |
| `selection_method` | `string` | — | `3` | `open` | — | Projektų atrankos būdas | — |
| `joint_measure_id` | `string` | — | `4` | `open` | — | Jungtinės priemonės identifikatorius | — |
| `joint_measure_number` | `string` | — | `4` | `open` | — | Jungtinės priemonės numeris | — |
| `joint_measure_name` | `string` | — | `4` | `open` | — | Jungtinės priemonės pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/kvietimai (https://data.gov.lt/datasets/2159/)

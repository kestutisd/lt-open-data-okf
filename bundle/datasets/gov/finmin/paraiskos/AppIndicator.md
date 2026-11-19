---
type: Table
title: "AppIndicator — Paraiškos produkto ir rezultato stebėsenos rodikliai"
description: "Spinta table datasets/gov/finmin/paraiskos/AppIndicator (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/paraiskos/AppIndicator"
tags: [gov, finmin, appindicator, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L68"
    title: "atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv#L68"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2160/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/paraiskos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# AppIndicator — Paraiškos produkto ir rezultato stebėsenos rodikliai

- **Model:** `datasets/gov/finmin/paraiskos/AppIndicator`[^manifest]
- **Dataset:** [2014-2020 m. Europos Sąjungos fondų projektų paraiškų ir jų vertinimų duomenys](../paraiskos.md) (`datasets/gov/finmin/paraiskos`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/paraiskos.csv#L68](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L68)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/paraiskos/AppIndicator` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `app_indicator_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `app_indicator_id` | `string` | — | `4` | `open` | — | Paraiškos rodiklio identifikatorius | — |
| `project` | `ref` | [Project](Project.md) (`level=4 UUID`: `project._id`) | `4` | `open` | — | Projekto identifikatorius | — |
| `measure_indicator` | `ref` | [MeasureIndicator](../kvietimai/MeasureIndicator.md) (`level=4 UUID`: `measure_indicator._id`) | `4` | `open` | — | Priemonės rodiklio identifikatorius | — |
| `value` | `number` | — | `4` | `open` | — | Rodiklio siektina reikšmė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv#L68 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L68)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/paraiskos (https://data.gov.lt/datasets/2160/)

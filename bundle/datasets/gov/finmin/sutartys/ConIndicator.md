---
type: Table
title: "ConIndicator — Sutarties produkto ir rezultato stebėsenos rodikliai"
description: "Spinta table datasets/gov/finmin/sutartys/ConIndicator (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConIndicator"
tags: [gov, finmin, conindicator, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L66"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L66"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ConIndicator — Sutarties produkto ir rezultato stebėsenos rodikliai

- **Model:** `datasets/gov/finmin/sutartys/ConIndicator`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L66](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L66)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConIndicator` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `con_indicator_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `con_indicator_id` | `string` | — | `4` | `open` | — | Sutarties rodiklio identifikatorius | — |
| `project` | `ref` | [Contract](Contract.md) (`level=4 UUID`: `project._id`) | `4` | `open` | — | Projekto identifikatorius | — |
| `measure_indicator` | `ref` | [MeasureIndicator](../kvietimai/MeasureIndicator.md) (`level=4 UUID`: `measure_indicator._id`) | `4` | `open` | — | Priemonės stebėsenos rodiklio identifikatorius | — |
| `value` | `number` | — | `4` | `open` | — | Rodiklio siektina reikšmė | Rodiklio aprašymo lentelėje nurodytais vienetais |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L66 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L66)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)

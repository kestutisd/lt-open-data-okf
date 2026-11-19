---
type: Table
title: "ConPhIndicator — Sutarties uždavinio veiklos fiziniai rodikliai"
description: "Spinta table datasets/gov/finmin/sutartys/ConPhIndicator (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConPhIndicator"
tags: [gov, finmin, conphindicator, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L138"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L138"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ConPhIndicator — Sutarties uždavinio veiklos fiziniai rodikliai

- **Model:** `datasets/gov/finmin/sutartys/ConPhIndicator`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L138](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L138)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConPhIndicator` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `con_ph_indicator_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `con_ph_indicator_id` | `string` | — | `4` | `open` | — | Sutarties uždavinio veiklos fizinio rodiklio identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Fizinio rodiklio numeris | — |
| `unit` | `string` | — | `4` | `open` | — | Fizinio rodiklio matavimo vienetas | — |
| `aim` | `number` | — | `4` | `open` | — | Fizinio rodiklio siekiama reikšmė | — |
| `task` | `ref` | [ConTask](ConTask.md) (`level=4 UUID`: `task._id`) | `4` | `open` | — | Sutarties uždavinys | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L138 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L138)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)

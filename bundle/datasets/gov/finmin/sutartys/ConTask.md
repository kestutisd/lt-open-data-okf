---
type: Table
title: "ConTask — Sutarties uždaviniai"
description: "Spinta table datasets/gov/finmin/sutartys/ConTask (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConTask"
tags: [gov, finmin, contask, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L132"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L132"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ConTask — Sutarties uždaviniai

- **Model:** `datasets/gov/finmin/sutartys/ConTask`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L132](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L132)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConTask` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `con_task_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `con_task_id` | `string` | — | `4` | `open` | — | Sutarties uždavinio identifikatorius | — |
| `project` | `ref` | [Contract](Contract.md) (`level=4 UUID`: `project._id`) | `4` | `open` | — | Projekto identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Projekto uždavinio numeris | — |
| `task` | `string` | — | `4` | `open` | — | Projekto uždavinio pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L132 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L132)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)

---
type: Table
title: "AppActivity — Paraiškos uždavinio veiklos"
description: "Spinta table datasets/gov/finmin/paraiskos/AppActivity (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/paraiskos/AppActivity"
tags: [gov, finmin, appactivity, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L88"
    title: "atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv#L88"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2160/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/paraiskos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# AppActivity — Paraiškos uždavinio veiklos

- **Model:** `datasets/gov/finmin/paraiskos/AppActivity`[^manifest]
- **Dataset:** [2014-2020 m. Europos Sąjungos fondų projektų paraiškų ir jų vertinimų duomenys](../paraiskos.md) (`datasets/gov/finmin/paraiskos`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/paraiskos.csv#L88](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L88)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/paraiskos/AppActivity` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `app_activity_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `app_activity_id` | `string` | — | `4` | `open` | — | Paraiškos uždavinio veiklos identifikatorius | — |
| `app_task` | `ref` | [AppTask](AppTask.md) (`level=4 UUID`: `app_task._id`) | `4` | `open` | — | Paraiškos uždavinio identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Projekto veiklos numeris | — |
| `name` | `string` | — | `4` | `open` | — | Projekto veiklos pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv#L88 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L88)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/paraiskos (https://data.gov.lt/datasets/2160/)

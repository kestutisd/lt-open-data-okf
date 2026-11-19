---
type: Table
title: "FinishReport — Ataskaitos po finansavimo pabaigos"
description: "Spinta table datasets/gov/finmin/sutartys/FinishReport (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/FinishReport"
tags: [gov, finmin, finishreport, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L514"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L514"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# FinishReport — Ataskaitos po finansavimo pabaigos

- **Model:** `datasets/gov/finmin/sutartys/FinishReport`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L514](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L514)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/FinishReport` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `report_id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `report_id` | `string` | — | `4` | `open` | — | Ataskaitos po finansavimo pabaigos identifikatorius | — |
| `created` | `date` | `D` | `4` | `open` | — | Ataskaitos po finansavimo pabaigos data | — |
| `received` | `date` | `D` | `4` | `open` | — | Gavimo data | — |
| `from` | `date` | `D` | `4` | `open` | — | Ataskaitinio laikotarpio pradžios data | — |
| `to` | `date` | `D` | `4` | `open` | — | Ataskaitinio laikotarpio pabaigos data | — |
| `corrected` | `date` | `D` | `4` | `open` | — | Ataskaitos po užbaigimo patikslinimo data | — |
| `state` | `string` | — | `3` | `open` | — | Ataskaitos po finansavimo pabaigos būsena | — |
| `state_updated` | `datetime` | `L` | `4` | `open` | — | Ataskaitos po finansavimo pabaigos būsenos data | — |
| `state_decided` | `date` | `D` | `4` | `open` | — | Ataskaitos po finansavimo pabaigos būsenos sprendimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L514 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L514)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)

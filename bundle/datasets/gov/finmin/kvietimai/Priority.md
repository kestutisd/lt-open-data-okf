---
type: Table
title: "Priority — Prioritetas"
description: "Spinta table datasets/gov/finmin/kvietimai/Priority (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/kvietimai/Priority"
tags: [gov, finmin, priority, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L68"
    title: "atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv#L68"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2159/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/kvietimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Priority — Prioritetas

- **Model:** `datasets/gov/finmin/kvietimai/Priority`[^manifest]
- **Dataset:** [2014-2020 m. Europos Sąjungos fondų kvietimų teikti paraiškas ir priemonių duomenys](../kvietimai.md) (`datasets/gov/finmin/kvietimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/kvietimai.csv#L68](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L68)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/kvietimai/Priority` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `priority_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `priority_id` | `string` | — | `4` | `open` | — | Prioriteto identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Prioriteto numeris | — |
| `name` | `string` | — | `4` | `open` | — | Prioriteto pavadinimas | — |
| `program_id` | `string` | — | `4` | `open` | — | Programos identifikatorius | — |
| `program` | `string` | — | `4` | `open` | — | Veiksmų programos pavadinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv#L68 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L68)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/kvietimai (https://data.gov.lt/datasets/2159/)

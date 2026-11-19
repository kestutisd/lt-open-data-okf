---
type: Table
title: "AppFinSource — Paraiškos projekto tinkamų finansuoti išlaidų finansavimo šaltiniai"
description: "Spinta table datasets/gov/finmin/paraiskos/AppFinSource (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/paraiskos/AppFinSource"
tags: [gov, finmin, appfinsource, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L74"
    title: "atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv#L74"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2160/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/paraiskos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# AppFinSource — Paraiškos projekto tinkamų finansuoti išlaidų finansavimo šaltiniai

- **Model:** `datasets/gov/finmin/paraiskos/AppFinSource`[^manifest]
- **Dataset:** [2014-2020 m. Europos Sąjungos fondų projektų paraiškų ir jų vertinimų duomenys](../paraiskos.md) (`datasets/gov/finmin/paraiskos`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/paraiskos.csv#L74](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L74)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/paraiskos/AppFinSource` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `app_fin_source_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `app_fin_source_id` | `string` | — | `4` | `open` | — | Finansavimo šaltinio identifikatorius | — |
| `project` | `ref` | [Project](Project.md) (`level=4 UUID`: `project._id`) | `4` | `open` | — | Projekto identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Finansavimo šaltinio numeris | — |
| `name` | `string` | — | `3` | `open` | — | Finansavimo šaltinio pavadinimas | — |
| `amount` | `number` | — | `2` | `open` | — | Finansavimo šaltinio suma | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv#L74 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L74)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/paraiskos (https://data.gov.lt/datasets/2160/)

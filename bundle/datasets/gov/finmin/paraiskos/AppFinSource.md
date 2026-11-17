---
type: Table
title: "AppFinSource — Paraiškos projekto tinkamų finansuoti išlaidų finansavimo šaltiniai"
description: "Spinta table datasets/gov/finmin/paraiskos/AppFinSource (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/paraiskos/AppFinSource"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L74"
    last_modified: "2026-11-11T14:39:20Z"
---

# AppFinSource — Paraiškos projekto tinkamų finansuoti išlaidų finansavimo šaltiniai

- **Model:** `datasets/gov/finmin/paraiskos/AppFinSource`[^manifest]
- **Dataset:** [datasets/gov/finmin/paraiskos](../paraiskos.md) (`datasets/gov/finmin/paraiskos`)
- **Manifest CSV:** [datasets/gov/finmin/paraiskos.csv#L74](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L74)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/paraiskos/AppFinSource`
- **Primary Key (`ref`):** `app_fin_source_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `app_fin_source_id` | `string` | — | `4` | `open` | — | Finansavimo šaltinio identifikatorius | — |
| `project` | `ref` | [Project](Project.md) | `4` | `open` | — | Projekto identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Finansavimo šaltinio numeris | — |
| `name` | `string` | — | `3` | `open` | — | Finansavimo šaltinio pavadinimas | — |
| `amount` | `number` | — | `2` | `open` | — | Finansavimo šaltinio suma | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv

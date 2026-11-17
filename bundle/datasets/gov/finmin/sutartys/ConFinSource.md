---
type: Table
title: "ConFinSource — Sutarties projekto tinkamų finansuoti išlaidų finansavimo šaltiniai"
description: "Spinta table datasets/gov/finmin/sutartys/ConFinSource (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConFinSource"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L72"
    last_modified: "2026-11-11T14:39:20Z"
---

# ConFinSource — Sutarties projekto tinkamų finansuoti išlaidų finansavimo šaltiniai

- **Model:** `datasets/gov/finmin/sutartys/ConFinSource`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L72](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L72)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/ConFinSource`
- **Primary Key (`ref`):** `con_fin_source_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `con_fin_source_id` | `string` | — | `4` | `open` | — | Finansavimo šaltinio identifikatorius | — |
| `project` | `ref` | [Contract](Contract.md) | `4` | `open` | — | Projekto identifikatorius | — |
| `number` | `string` | — | `4` | `open` | — | Finansavimo šaltinio numeris | — |
| `fin_source` | `string` | — | `3` | `open` | — | Finansavimo šaltinio pavadinimas | — |
| `amount` | `number` | — | `2` | `open` | — | Finansavimo šaltinio suma | — |
| `percent` | `number` | `%` | `4` | `open` | — | Finansavimo šaltinio intensyvumo procentas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv

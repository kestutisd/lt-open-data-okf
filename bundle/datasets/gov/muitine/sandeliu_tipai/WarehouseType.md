---
type: Table
title: "WarehouseType"
description: "Spinta table datasets/gov/muitine/sandeliu_tipai/WarehouseType (5 columns)."
tags: [gov, muitine, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/sandeliu_tipai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/sandeliu_tipai.csv#L15"
    last_modified: "2026-11-11T14:39:20Z"
---

# WarehouseType

- **Model:** `datasets/gov/muitine/sandeliu_tipai/WarehouseType`[^manifest]
- **Dataset:** [datasets/gov/muitine/sandeliu_tipai](../sandeliu_tipai.md) (`datasets/gov/muitine/sandeliu_tipai`)
- **Manifest CSV:** [datasets/gov/muitine/sandeliu_tipai.csv#L15](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/sandeliu_tipai.csv#L15)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Rinkinio identifikacinis numeris | — |
| `metadata` | `ref` | [Metadata](Metadata.md) | `4` | `open` | — | Nuoroda į tėvinį elementą | — |
| `code` | `string` | — | `3` | `open` | — | Tipo kodas | 1 simbolio kodas |
| `valid_from` | `date` | `10D` | `4` | `open` | — | Galiojimo pradžios data | — |
| `valid_to` | `date` | `10D` | `4` | `open` | — | Galiojimo pabaigos data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/sandeliu_tipai.csv

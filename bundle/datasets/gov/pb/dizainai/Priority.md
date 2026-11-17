---
type: Table
title: "Priority"
description: "Spinta table datasets/gov/pb/dizainai/Priority (3 columns)."
tags: [gov, pb, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pb/dizainai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L34"
    last_modified: "2026-11-11T14:39:20Z"
---

# Priority

- **Model:** `datasets/gov/pb/dizainai/Priority`[^manifest]
- **Dataset:** [Dizainai](../dizainai.md) (`datasets/gov/pb/dizainai`)
- **Manifest CSV:** [datasets/gov/pb/dizainai.csv#L34](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L34)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `priority_number`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `priority_country_code` | `string` | — | `3` | `open` | — | Prioriteto šalies kodas | — |
| `priority_number` | `integer` | — | `4` | `open` | — | Prioriteto numeris | — |
| `priority_date` | `date` | `D` | `4` | `open` | — | Prioriteto data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/dizainai.csv

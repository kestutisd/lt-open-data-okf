---
type: Table
title: "ObjectManagerRelation — Registrų valdytojai"
description: "Spinta table datasets/gov/ivpk/registrai/ObjectManagerRelation (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/registrai/ObjectManagerRelation"
tags: [gov, ivpk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L174"
    last_modified: "2026-11-11T14:39:20Z"
---

# ObjectManagerRelation — Registrų valdytojai

- **Model:** `datasets/gov/ivpk/registrai/ObjectManagerRelation`[^manifest]
- **Dataset:** [datasets/gov/ivpk/registrai](../registrai.md) (`datasets/gov/ivpk/registrai`)
- **Manifest CSV:** [datasets/gov/ivpk/registrai.csv#L174](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/registrai.csv#L174)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/registrai/ObjectManagerRelation`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `institution` | `integer` | — | `1` | `open` | — | Valdytojas | — |
| `object` | `integer` | — | `1` | `open` | — | Registras | — |
| `manager_type` | `integer` | — | `1` | `open` | — | Valdytojo tipas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/registrai.csv

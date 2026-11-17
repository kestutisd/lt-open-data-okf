---
type: Table
title: "AdjustmentAction — Projekto institucijos koregavimo veiksmų dalys"
description: "Spinta table datasets/gov/finmin/sutartys/AdjustmentAction (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/AdjustmentAction"
tags: [gov, finmin, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L498"
    last_modified: "2026-11-11T14:39:20Z"
---

# AdjustmentAction — Projekto institucijos koregavimo veiksmų dalys

- **Model:** `datasets/gov/finmin/sutartys/AdjustmentAction`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L498](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L498)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/AdjustmentAction`
- **Primary Key (`ref`):** `action_id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `action_id` | `string` | — | `4` | `open` | — | Institucijos koregavimo veiksmo dalies identifikatorius | — |
| `sfmis_number` | `string` | — | `4` | `open` | — | SFMIS IKV dalies numeris | — |
| `started` | `date` | `D` | `4` | `open` | — | Koregavimo veiksmų registravimo data | — |
| `state` | `string` | — | `3` | `open` | — | Koregavimo veiksmų būsena | — |
| `state_updated` | `date` | `D` | `4` | `open` | — | Koregavimo veiksmų būsenos data | — |
| `is_tvi` | `string` | — | `2` | `open` | — | Koregavimo veiksmo dalies tipas | — |
| `is_ms` | `boolean` | — | `4` | `open` | — | ID ar MS | — |
| `amount` | `number` | — | `2` | `open` | — | Koregavimo veiksmo dalies suma | — |
| `declare_by` | `date` | `D` | `4` | `open` | — | Deklaruotinumo data | — |
| `declared` | `date` | `D` | `4` | `open` | — | Deklaravimo data | — |
| `submitted` | `date` | `D` | `4` | `open` | — | Sąskaitų EK teikimo data | — |
| `base` | `string` | — | `3` | `open` | — | IKV dalies pagrindas | — |
| `repayment` | `ref` | [Repayment](Repayment.md) | `4` | `open` | — | Grąžintinų lėšų identifikatorius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv

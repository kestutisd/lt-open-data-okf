---
type: Table
title: "AdjustmentAction — Projekto institucijos koregavimo veiksmų dalys"
description: "Spinta table datasets/gov/finmin/sutartys/AdjustmentAction (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/AdjustmentAction"
tags: [gov, finmin, adjustmentaction, deployed, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L498"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L498"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# AdjustmentAction — Projekto institucijos koregavimo veiksmų dalys

- **Model:** `datasets/gov/finmin/sutartys/AdjustmentAction`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L498](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L498)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/AdjustmentAction` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `action_id`[^manifest]
- **Level:** `—`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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
| `repayment` | `ref` | [Repayment](Repayment.md) (`level=4 UUID`: `repayment._id`) | `4` | `open` | — | Grąžintinų lėšų identifikatorius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amount` | `update(type: "money", ref: "EUR")` | `type` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L498 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L498)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)

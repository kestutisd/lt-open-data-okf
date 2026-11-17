---
type: Table
title: "TransportoPriemone"
description: "Lentelėje pateikiamos, reiso metu naudotos, keleivių vežimo priemonės"
resource: "https://get.data.gov.lt/datasets/gov/sp/keleiviu_srautai/TransportoPriemone"
tags: [gov, sp, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/sp/keleiviu_srautai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sp/keleiviu_srautai.csv#L42"
    last_modified: "2026-11-11T14:39:20Z"
---

# TransportoPriemone

Lentelėje pateikiamos, reiso metu naudotos, keleivių vežimo priemonės

- **Model:** `datasets/gov/sp/keleiviu_srautai/TransportoPriemone`[^manifest]
- **Dataset:** [Vilniaus miesto viešojo transporto maršrutų keleivių srautų duomenys](../keleiviu_srautai.md) (`datasets/gov/sp/keleiviu_srautai`)
- **Manifest CSV:** [datasets/gov/sp/keleiviu_srautai.csv#L42](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sp/keleiviu_srautai.csv#L42)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sp/keleiviu_srautai/TransportoPriemone`
- **Primary Key (`ref`):** `tp_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tp_id` | `string` | — | `4` | `open` | — | Transporto priemonės identifikatorius | — |
| `tp_kodas` | `string` | — | `4` | `open` | — | Transporto priemonės kodas | — |
| `marke` | `string` | — | `4` | `open` | — | Transporto priemonės markė | — |
| `sedimu_vietu_sk` | `integer` | — | `4` | `open` | — | Sėdimų vietų skaičius transporto priemonėje | — |
| `vezejas` | `string` | — | `4` | `open` | — | Vežėjas | — |
| `tp_aktyvumas` | `boolean` | — | `4` | `open` | — | Aktyvios transporto priemonės požymis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sp/keleiviu_srautai.csv

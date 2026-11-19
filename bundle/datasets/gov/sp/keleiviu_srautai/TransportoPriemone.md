---
type: Table
title: "TransportoPriemone"
description: "Lentelėje pateikiamos, reiso metu naudotos, keleivių vežimo priemonės"
resource: "https://get.data.gov.lt/datasets/gov/sp/keleiviu_srautai/TransportoPriemone"
tags: [gov, sp, transportopriemone, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sp/keleiviu_srautai.csv#L42"
    title: "atviriduomenys/manifest — datasets/gov/sp/keleiviu_srautai.csv#L42"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3901/"
    title: "data.gov.lt DCAT-AP — datasets/gov/sp/keleiviu_srautai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# TransportoPriemone

Lentelėje pateikiamos, reiso metu naudotos, keleivių vežimo priemonės[^manifest]

- **Model:** `datasets/gov/sp/keleiviu_srautai/TransportoPriemone`[^manifest]
- **Dataset:** [Vilniaus miesto viešojo transporto maršrutų keleivių srautų duomenys](../keleiviu_srautai.md) (`datasets/gov/sp/keleiviu_srautai`)[^manifest]
- **Manifest CSV:** [datasets/gov/sp/keleiviu_srautai.csv#L42](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sp/keleiviu_srautai.csv#L42)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/sp/keleiviu_srautai/TransportoPriemone` (`deployed`)[^manifest]
- **Provider:** `sp` — Vilniaus miesto SĮ „Susisiekimo paslaugos“ *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `tp_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tp_id` | `string` | — | `4` | `open` | — | Transporto priemonės identifikatorius | — |
| `tp_kodas` | `string` | — | `4` | `open` | — | Transporto priemonės kodas | — |
| `marke` | `string` | — | `4` | `open` | — | Transporto priemonės markė | — |
| `sedimu_vietu_sk` | `integer` | — | `4` | `open` | — | Sėdimų vietų skaičius transporto priemonėje | — |
| `vezejas` | `string` | — | `4` | `open` | — | Vežėjas | — |
| `tp_aktyvumas` | `boolean` | — | `4` | `open` | — | Aktyvios transporto priemonės požymis | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/sp/keleiviu_srautai.csv#L42 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/sp/keleiviu_srautai.csv#L42)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/sp/keleiviu_srautai (https://data.gov.lt/datasets/3901/)

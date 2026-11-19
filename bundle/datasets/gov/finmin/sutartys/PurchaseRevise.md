---
type: Table
title: "PurchaseRevise — Projekto pirkimo plano pirkimo patikra"
description: "Spinta table datasets/gov/finmin/sutartys/PurchaseRevise (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PurchaseRevise"
tags: [gov, finmin, purchaserevise, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L434"
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L434"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2161/"
    title: "data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PurchaseRevise — Projekto pirkimo plano pirkimo patikra

- **Model:** `datasets/gov/finmin/sutartys/PurchaseRevise`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L434](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L434)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PurchaseRevise` (`deployed`)[^manifest]
- **Provider:** `finmin` — Lietuvos Respublikos finansų ministerija *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `purchase_revise_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `purchase_revise_id` | `string` | — | `4` | `open` | — | Pirkimo patikros identifikatorius | — |
| `purchase` | `ref` | [Purchase](Purchase.md) (`level=4 UUID`: `purchase._id`) | `4` | `open` | — | Pirkimo identifikatorius | — |
| `sfmis_no` | `string` | — | `4` | `open` | — | SFMIS patikros numeris | — |
| `method` | `string` | — | `3` | `open` | — | Patikros būdas | — |
| `result` | `string` | — | `3` | `open` | — | Patikros rezultatas | — |
| `doc_pay` | `boolean` | — | `4` | `open` | — | Dok. teikiami su MP. | — |
| `doc_cvp_is` | `boolean` | — | `4` | `open` | — | Dok. teikiami per CVP IS / raštu. | — |
| `doc_received` | `date` | `D` | `4` | `open` | — | Dok. gavimo data | — |
| `state` | `string` | — | `3` | `open` | — | Patikros būsena | — |
| `state_updated` | `datetime` | `L` | `4` | `open` | — | Patikros būsenos data | — |
| `state_decided` | `date` | `D` | `4` | `open` | — | Patikros būsenos sprendimo data | — |
| `receipt` | `string` | — | `3` | `open` | — | Pirkimo dokumento gavimo būdas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv#L434 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L434)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/finmin/sutartys (https://data.gov.lt/datasets/2161/)

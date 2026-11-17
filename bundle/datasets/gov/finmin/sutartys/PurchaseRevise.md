---
type: Table
title: "PurchaseRevise — Projekto pirkimo plano pirkimo patikra"
description: "Spinta table datasets/gov/finmin/sutartys/PurchaseRevise (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PurchaseRevise"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L434"
    last_modified: "2026-11-11T14:39:20Z"
---

# PurchaseRevise — Projekto pirkimo plano pirkimo patikra

- **Model:** `datasets/gov/finmin/sutartys/PurchaseRevise`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L434](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L434)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PurchaseRevise`
- **Primary Key (`ref`):** `purchase_revise_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `purchase_revise_id` | `string` | — | `4` | `open` | — | Pirkimo patikros identifikatorius | — |
| `purchase` | `ref` | [Purchase](Purchase.md) | `4` | `open` | — | Pirkimo identifikatorius | — |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv

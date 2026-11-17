---
type: Table
title: "PurchaseReviseContract — Projekto pirkimo plano pirkimo patikros sutartis"
description: "Spinta table datasets/gov/finmin/sutartys/PurchaseReviseContract (4 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sutartys/PurchaseReviseContract"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L448"
    last_modified: "2026-11-11T14:39:20Z"
---

# PurchaseReviseContract — Projekto pirkimo plano pirkimo patikros sutartis

- **Model:** `datasets/gov/finmin/sutartys/PurchaseReviseContract`[^manifest]
- **Dataset:** [2014-2020 m. ES fondų projektų įgyvendinimo duomenys](../sutartys.md) (`datasets/gov/finmin/sutartys`)
- **Manifest CSV:** [datasets/gov/finmin/sutartys.csv#L448](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sutartys.csv#L448)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sutartys/PurchaseReviseContract`
- **Primary Key (`ref`):** `purchase_revise_contract_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `purchase_revise_contract_id` | `string` | — | `4` | `open` | — | Pirkimo patikros sutarties identifikatorius | — |
| `purchase_revise` | `ref` | [PurchaseRevise](PurchaseRevise.md) | `4` | `open` | — | Pirkimo patikros identifikatorius | — |
| `purchase_contract` | `ref` | [PurchaseContract](PurchaseContract.md) | `4` | `open` | — | Pirkimo sutarties identifikatorius | — |
| `sfmis_no` | `string` | — | `4` | `open` | — | SFMIS sutarties numeris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sutartys.csv

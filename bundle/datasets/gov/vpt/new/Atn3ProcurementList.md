---
type: Table
title: "Atn3ProcurementList — Atn-3 VII Viešųjų pirkimų įstatymo 10 straipsnyje arba komunalinio sektoriaus pirkimų įstatymo 19 straipsnyje nurodyti vidaus sandoriai"
description: "Spinta table datasets/gov/vpt/new/Atn3ProcurementList (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/new/Atn3ProcurementList"
tags: [gov, vpt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpt/new.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L1167"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atn3ProcurementList — Atn-3 VII Viešųjų pirkimų įstatymo 10 straipsnyje arba komunalinio sektoriaus pirkimų įstatymo 19 straipsnyje nurodyti vidaus sandoriai

- **Model:** `datasets/gov/vpt/new/Atn3ProcurementList`[^manifest]
- **Dataset:** [Pirkimų, vykdytų po 2017-07-01 duomenys](../new.md) (`datasets/gov/vpt/new`)
- **Manifest CSV:** [datasets/gov/vpt/new.csv#L1167](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L1167)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/new/Atn3ProcurementList`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `atn3` | `ref` | [Atn3](Atn3.md) | `4` | `open` | — | — | — |
| `number` | `integer` | — | `3` | `open` | — | — | — |
| `contracting_authority_code` | `integer` | — | `3` | `open` | — | — | — |
| `contracting_authority_name` | `string` | — | `3` | `open` | — | — | — |
| `contracting_authority_name_adjustment` | `string` | — | `3` | `open` | — | — | — |
| `object_of_purchase_name` | `string` | — | `3` | `open` | — | — | — |
| `contract_conclusion_date` | `string` | — | `3` | `open` | — | — | — |
| `contract_performance_date` | `string` | — | `3` | `open` | — | — | — |
| `total_value_of_concluded_contract` | `number` | — | `3` | `open` | — | — | — |
| `group_` | `string` | — | `3` | `open` | — | — | — |
| `item` | `integer` | — | `3` | `open` | — | — | — |
| `insert_date` | `datetime` | — | `3` | `open` | — | — | — |
| `update_date` | `datetime` | — | `3` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/new.csv

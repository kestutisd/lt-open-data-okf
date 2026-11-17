---
type: Table
title: "Atn1EndOfProcurementProcedureList"
description: "Spinta table datasets/gov/vpt/new/Atn1EndOfProcurementProcedureList (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/new/Atn1EndOfProcurementProcedureList"
tags: [gov, vpt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpt/new.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L692"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atn1EndOfProcurementProcedureList

- **Model:** `datasets/gov/vpt/new/Atn1EndOfProcurementProcedureList`[^manifest]
- **Dataset:** [Pirkimų, vykdytų po 2017-07-01 duomenys](../new.md) (`datasets/gov/vpt/new`)
- **Manifest CSV:** [datasets/gov/vpt/new.csv#L692](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L692)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/new/Atn1EndOfProcurementProcedureList`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `atn1` | `ref` | [Atn1](Atn1.md) | `4` | `open` | — | — | — |
| `end_of_procedures` | `string` | — | `3` | `open` | — | — | — |
| `part_number_of_object` | `string` | — | `3` | `open` | — | — | — |
| `decision_date` | `string` | — | `3` | `open` | — | — | — |
| `reason_for_making_decision` | `string` | — | `3` | `open` | — | — | — |
| `item` | `integer` | — | `3` | `open` | — | — | — |
| `insert_date` | `datetime` | — | `3` | `open` | — | — | — |
| `update_date` | `datetime` | — | `3` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/new.csv

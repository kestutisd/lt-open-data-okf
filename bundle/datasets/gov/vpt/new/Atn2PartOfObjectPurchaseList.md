---
type: Table
title: "Atn2PartOfObjectPurchaseList"
description: "Spinta table datasets/gov/vpt/new/Atn2PartOfObjectPurchaseList (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/new/Atn2PartOfObjectPurchaseList"
tags: [gov, vpt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpt/new.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L1034"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atn2PartOfObjectPurchaseList

- **Model:** `datasets/gov/vpt/new/Atn2PartOfObjectPurchaseList`[^manifest]
- **Dataset:** [Pirkimų, vykdytų po 2017-07-01 duomenys](../new.md) (`datasets/gov/vpt/new`)
- **Manifest CSV:** [datasets/gov/vpt/new.csv#L1034](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L1034)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/new/Atn2PartOfObjectPurchaseList`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `atn2` | `ref` | [Atn2](Atn2.md) | `4` | `open` | — | — | — |
| `subject` | `string` | — | `3` | `open` | — | — | — |
| `part_number` | `integer` | — | `3` | `open` | — | — | — |
| `item` | `integer` | — | `3` | `open` | — | — | — |
| `cpv_main_1` | `string` | — | `3` | `open` | — | — | — |
| `cpv_codes_1` | `string` | — | `3` | `open` | — | — | — |
| `cpv_ids_1` | `string` | — | `3` | `open` | — | — | — |
| `cpv_main_2` | `string` | — | `3` | `open` | — | — | — |
| `cpv_codes_2` | `string` | — | `3` | `open` | — | — | — |
| `cpv_ids_2` | `string` | — | `3` | `open` | — | — | — |
| `insert_date` | `datetime` | — | `3` | `open` | — | — | — |
| `update_date` | `datetime` | — | `3` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/new.csv

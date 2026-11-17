---
type: Table
title: "Atn2ContractedCandidateList"
description: "Spinta table datasets/gov/vpt/new/Atn2ContractedCandidateList (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/new/Atn2ContractedCandidateList"
tags: [gov, vpt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpt/new.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L996"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atn2ContractedCandidateList

- **Model:** `datasets/gov/vpt/new/Atn2ContractedCandidateList`[^manifest]
- **Dataset:** [Pirkimų, vykdytų po 2017-07-01 duomenys](../new.md) (`datasets/gov/vpt/new`)
- **Manifest CSV:** [datasets/gov/vpt/new.csv#L996](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L996)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/new/Atn2ContractedCandidateList`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `atn2` | `ref` | [Atn2](Atn2.md) | `4` | `open` | — | — | — |
| `part_no` | `string` | — | `3` | `open` | — | — | — |
| `tenderer_code` | `string` | — | `3` | `open` | — | — | — |
| `tenderer_name` | `string` | — | `3` | `open` | — | — | — |
| `tenderer_name_other` | `string` | — | `3` | `open` | — | — | — |
| `tender_id` | `integer` | — | `3` | `open` | — | — | — |
| `price_quality_ratio` | `number` | — | `3` | `open` | — | — | — |
| `price_cost_tender` | `string` | — | `3` | `open` | — | — | — |
| `price_cost_tender_expression` | `string` | — | `3` | `open` | — | — | — |
| `is_price` | `string` | — | `3` | `open` | — | — | — |
| `item` | `integer` | — | `3` | `open` | — | — | — |
| `insert_date` | `datetime` | — | `3` | `open` | — | — | — |
| `update_date` | `datetime` | — | `3` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/new.csv

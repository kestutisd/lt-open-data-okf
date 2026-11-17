---
type: Table
title: "Atn1CandidateRejectedTenderList"
description: "Spinta table datasets/gov/vpt/new/Atn1CandidateRejectedTenderList (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/new/Atn1CandidateRejectedTenderList"
tags: [gov, vpt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpt/new.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L558"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atn1CandidateRejectedTenderList

- **Model:** `datasets/gov/vpt/new/Atn1CandidateRejectedTenderList`[^manifest]
- **Dataset:** [Pirkimų, vykdytų po 2017-07-01 duomenys](../new.md) (`datasets/gov/vpt/new`)
- **Manifest CSV:** [datasets/gov/vpt/new.csv#L558](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L558)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/new/Atn1CandidateRejectedTenderList`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `atn1` | `ref` | [Atn1](Atn1.md) | `4` | `open` | — | — | — |
| `part_no` | `string` | — | `3` | `open` | — | — | — |
| `tenderer_code` | `string` | — | `3` | `open` | — | — | — |
| `tenderer_name` | `string` | — | `3` | `open` | — | — | — |
| `tenderer_name_other` | `string` | — | `3` | `open` | — | — | — |
| `not_submitted_reason` | `string` | — | `3` | `open` | — | — | — |
| `not_submitted_specification` | `string` | — | `3` | `open` | — | — | — |
| `legal_grounds_rejecting_public_procurement` | `string` | — | `3` | `open` | — | — | — |
| `legal_grounds_rejecting_utilities_procurement` | `string` | — | `3` | `open` | — | — | — |
| `reasons_rejecting` | `string` | — | `3` | `open` | — | — | — |
| `price_cost_tender` | `string` | — | `3` | `open` | — | — | — |
| `price_cost_tender_expression` | `string` | — | `3` | `open` | — | — | — |
| `is_price` | `string` | — | `3` | `open` | — | — | — |
| `item` | `integer` | — | `3` | `open` | — | — | — |
| `insert_date` | `datetime` | — | `3` | `open` | — | — | — |
| `update_date` | `datetime` | — | `3` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/new.csv

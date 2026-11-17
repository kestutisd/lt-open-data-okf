---
type: Table
title: "Atgn1RejectedCandidateList — VI. 2 Pasiūlymų nepateikę kandidatai (dalyviai) ir atmesti pasiūlymai (galutiniai pasiūlymai)"
description: "Spinta table datasets/gov/vpt/new/Atgn1RejectedCandidateList (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/new/Atgn1RejectedCandidateList"
tags: [gov, vpt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpt/new.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L183"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atgn1RejectedCandidateList — VI. 2 Pasiūlymų nepateikę kandidatai (dalyviai) ir atmesti pasiūlymai (galutiniai pasiūlymai)

- **Model:** `datasets/gov/vpt/new/Atgn1RejectedCandidateList`[^manifest]
- **Dataset:** [Pirkimų, vykdytų po 2017-07-01 duomenys](../new.md) (`datasets/gov/vpt/new`)
- **Manifest CSV:** [datasets/gov/vpt/new.csv#L183](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L183)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/new/Atgn1RejectedCandidateList`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `atgn1` | `ref` | [Atgn1](Atgn1.md) | `4` | `open` | — | — | — |
| `part_no` | `string` | — | `3` | `open` | — | — | — |
| `tenderer_code` | `string` | — | — | `open` | — | — | — |
| `tenderer_name` | `string` | — | — | `open` | — | — | — |
| `not_submitted_reason` | `string` | — | `3` | `open` | — | — | — |
| `not_submitted_specification` | `string` | — | `3` | `open` | — | — | — |
| `atg_rejection_legal_ground` | `string` | — | `3` | `open` | — | — | — |
| `reasons_rejecting` | `string` | — | `3` | `open` | — | — | — |
| `price_of_tender` | `number` | — | `3` | `open` | — | — | — |
| `price_cost_tender_expression` | `string` | — | `3` | `open` | — | — | — |
| `item` | `integer` | — | `3` | `open` | — | — | — |
| `insert_date` | `datetime` | — | `3` | `open` | — | — | — |
| `update_date` | `datetime` | — | `3` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/new.csv

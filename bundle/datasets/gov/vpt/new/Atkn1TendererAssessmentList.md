---
type: Table
title: "Atkn1TendererAssessmentList"
description: "Spinta table datasets/gov/vpt/new/Atkn1TendererAssessmentList (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/new/Atkn1TendererAssessmentList"
tags: [gov, vpt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpt/new.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L398"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atkn1TendererAssessmentList

- **Model:** `datasets/gov/vpt/new/Atkn1TendererAssessmentList`[^manifest]
- **Dataset:** [Pirkimų, vykdytų po 2017-07-01 duomenys](../new.md) (`datasets/gov/vpt/new`)
- **Manifest CSV:** [datasets/gov/vpt/new.csv#L398](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L398)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/new/Atkn1TendererAssessmentList`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `atkn1` | `ref` | [Atkn1](Atkn1.md) | `4` | `open` | — | — | — |
| `lot_no` | `integer` | — | `3` | `open` | — | — | — |
| `sequence_no` | `integer` | — | `3` | `open` | — | — | — |
| `insert_date` | `datetime` | — | `3` | `open` | — | — | — |
| `update_date` | `datetime` | — | `3` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/new.csv

---
type: Table
title: "Atkn1InformationAboutConcessionContractList — AtK-1"
description: "Spinta table datasets/gov/vpt/new/Atkn1InformationAboutConcessionContractList (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vpt/new/Atkn1InformationAboutConcessionContractList"
tags: [gov, vpt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpt/new.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L373"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atkn1InformationAboutConcessionContractList — AtK-1

- **Model:** `datasets/gov/vpt/new/Atkn1InformationAboutConcessionContractList`[^manifest]
- **Dataset:** [Pirkimų, vykdytų po 2017-07-01 duomenys](../new.md) (`datasets/gov/vpt/new`)
- **Manifest CSV:** [datasets/gov/vpt/new.csv#L373](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpt/new.csv#L373)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpt/new/Atkn1InformationAboutConcessionContractList`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `atkn1` | `ref` | [Atkn1](Atkn1.md) | `4` | `open` | — | — | — |
| `part_no` | `string` | — | `3` | `open` | — | — | — |
| `conclusion_date` | `string` | — | `3` | `open` | — | — | — |
| `duration_of_contract_date` | `datetime` | — | `3` | `open` | — | — | — |
| `total_value` | `number` | — | `3` | `open` | — | — | — |
| `insert_date` | `datetime` | — | `3` | `open` | — | — | — |
| `update_date` | `datetime` | — | `3` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpt/new.csv

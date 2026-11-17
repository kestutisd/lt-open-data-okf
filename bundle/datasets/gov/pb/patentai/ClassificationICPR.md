---
type: Table
title: "ClassificationICPR"
description: "Spinta table datasets/gov/pb/patentai/ClassificationICPR (7 columns)."
tags: [gov, pb, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pb/patentai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L20"
    last_modified: "2026-11-11T14:39:20Z"
---

# ClassificationICPR

- **Model:** `datasets/gov/pb/patentai/ClassificationICPR`[^manifest]
- **Dataset:** [Patentai](../patentai.md) (`datasets/gov/pb/patentai`)
- **Manifest CSV:** [datasets/gov/pb/patentai.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L20)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `date`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `date` | `date` | `D` | `4` | `open` | — | Tarptautinės klasifikacijos data | — |
| `section` | `string` | — | `3` | `open` | — | Tarptautinės klasifikacijos skyrius | — |
| `class` | `integer` | — | `3` | `open` | — | Tarptautinės klasifikacijos klasė | — |
| `subclass` | `string` | — | `3` | `open` | — | Tarptautinės klasifikacijos poklasė | — |
| `main_group` | `integer` | — | `3` | `open` | — | Tarptautinės klasifikacijos pagrindinė grupė | — |
| `subgroup` | `integer` | — | `3` | `open` | — | Tarptautinės klasifikacijos pogrupis | — |
| `symbol_position` | `string` | — | `3` | `open` | — | Simbolių pozicija | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/patentai.csv

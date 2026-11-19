---
type: Table
title: "ClassificationICPR"
description: "Spinta table datasets/gov/pb/patentai/ClassificationICPR (7 columns)."
tags: [gov, pb, classificationicpr, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L20"
    title: "atviriduomenys/manifest — datasets/gov/pb/patentai.csv#L20"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# ClassificationICPR

- **Model:** `datasets/gov/pb/patentai/ClassificationICPR`[^manifest]
- **Dataset:** [Patentai](../patentai.md) (`datasets/gov/pb/patentai`)[^manifest]
- **Manifest CSV:** [datasets/gov/pb/patentai.csv#L20](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L20)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `pb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `date`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/patentai.csv#L20 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/patentai.csv#L20)

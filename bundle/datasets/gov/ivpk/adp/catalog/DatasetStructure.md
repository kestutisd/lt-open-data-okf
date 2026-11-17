---
type: Table
title: "DatasetStructure — Duomenų struktūros aprašas"
description: "Spinta table datasets/gov/ivpk/adp/catalog/DatasetStructure (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/DatasetStructure"
tags: [gov, ivpk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/ivpk/adk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L355"
    last_modified: "2026-11-11T14:39:20Z"
---

# DatasetStructure — Duomenų struktūros aprašas

- **Model:** `datasets/gov/ivpk/adp/catalog/DatasetStructure`[^manifest]
- **Dataset:** [datasets/gov/ivpk/adp/catalog](../catalog.md) (`datasets/gov/ivpk/adp/catalog`)
- **Manifest CSV:** [datasets/gov/ivpk/adk.csv#L355](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/ivpk/adk.csv#L355)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/ivpk/adp/catalog/DatasetStructure`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | `4` | `open` | — | — | — |
| `created` | `datetime` | — | `4` | `open` | — | — | — |
| `modified` | `datetime` | — | `4` | `open` | — | — | — |
| `version` | `integer` | — | `4` | `open` | — | — | — |
| `filename` | `string` | — | `4` | `open` | — | — | — |
| `identifier` | `string` | — | `4` | `open` | — | — | — |
| `mime_type` | `string` | — | `5` | `open` | `dct:format` | — | — |
| `size` | `integer` | `B` | `4` | `open` | — | — | — |
| `title` | `string` | — | `4` | `open` | — | — | — |
| `dataset` | `ref` | [Dataset](Dataset.md) | `4` | `open` | — | — | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `dct` | `http://purl.org/dc/terms/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/ivpk/adk.csv

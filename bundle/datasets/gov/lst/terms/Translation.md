---
type: Table
title: "Translation"
description: "Termino atitikmenys kitomis kalbomis"
resource: "https://get.data.gov.lt/datasets/gov/lst/terms/Translation"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/terms.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L39"
    last_modified: "2026-11-11T14:39:20Z"
---

# Translation

Termino atitikmenys kitomis kalbomis

- **Model:** `datasets/gov/lst/terms/Translation`[^manifest]
- **Dataset:** [datasets/gov/lst/terms](../terms.md) (`datasets/gov/lst/terms`)
- **Manifest CSV:** [datasets/gov/lst/terms.csv#L39](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L39)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/terms/Translation`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `translation` | `string` | — | — | `open` | — | — | — |
| `language` | `ref` | [Language](Language.md) | — | `open` | — | — | — |
| `term` | `ref` | [Term](Term.md) | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/terms.csv

---
type: Table
title: "Attachment"
description: "Grafiniai priedai (JPG formatu) – paveikslai, formulės"
resource: "https://get.data.gov.lt/datasets/gov/lst/terms/Attachment"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/terms.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L29"
    last_modified: "2026-11-11T14:39:20Z"
---

# Attachment

Grafiniai priedai (JPG formatu) – paveikslai, formulės

- **Model:** `datasets/gov/lst/terms/Attachment`[^manifest]
- **Dataset:** [datasets/gov/lst/terms](../terms.md) (`datasets/gov/lst/terms`)
- **Manifest CSV:** [datasets/gov/lst/terms.csv#L29](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/terms.csv#L29)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/terms/Attachment`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `name` | `string` | — | — | `open` | — | — | — |
| `file` | `file` | — | — | `open` | — | — | — |
| `term` | `ref` | [Term](Term.md) | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/terms.csv

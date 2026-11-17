---
type: Table
title: "Document"
description: "Duomenys apie išleistą standartą"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/Document"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L215"
    last_modified: "2026-11-11T14:39:20Z"
---

# Document

Duomenys apie išleistą standartą

- **Model:** `datasets/gov/lst/standards/Document`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L215](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L215)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/Document`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `stage` | `ref` | [Stage](Stage.md) | — | `open` | — | — | — |
| `original_language` | `ref` | [Language](Language.md) | — | `open` | — | — | — |
| `language` | `ref` | [Language](Language.md) | — | `open` | — | — | — |
| `name` | `string` | — | — | `open` | — | — | — |
| `isbn` | `string` | — | — | `open` | — | — | — |
| `version` | `string` | — | — | `open` | — | — | — |
| `finished_date` | `datetime` | — | — | `open` | — | — | — |
| `number_of_pages` | `integer` | — | — | `open` | — | — | — |
| `free_number_of_pages` | `integer` | — | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv

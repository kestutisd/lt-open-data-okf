---
type: Table
title: "DocumentFile"
description: "Duomenys apie standarto dokumentų tipus ir jų formatus"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/DocumentFile"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L288"
    last_modified: "2026-11-11T14:39:20Z"
---

# DocumentFile

Duomenys apie standarto dokumentų tipus ir jų formatus

- **Model:** `datasets/gov/lst/standards/DocumentFile`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L288](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L288)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/DocumentFile`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `integer` | — | — | `open` | — | — | — |
| `document` | `ref` | [Document](Document.md) | — | `open` | — | — | — |
| `name` | `string` | — | — | `open` | — | — | — |
| `size` | `string` | — | — | `open` | — | — | — |
| `type` | `string` | — | — | `open` | — | — | — |
| `paper_size` | `string` | — | — | `open` | — | — | — |
| `last_write_time` | `datetime` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv

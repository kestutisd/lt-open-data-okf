---
type: Table
title: "StandardDocument"
description: "Duomenys apie standarto dokumentus ir jų tipus"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/StandardDocument"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L314"
    last_modified: "2026-11-11T14:39:20Z"
---

# StandardDocument

Duomenys apie standarto dokumentus ir jų tipus

- **Model:** `datasets/gov/lst/standards/StandardDocument`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L314](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L314)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/StandardDocument`
- **Primary Key (`ref`):** `standard, document`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `standard` | `ref` | [Standard](Standard.md) | — | `open` | — | — | — |
| `document` | `ref` | [Document](Document.md) | — | `open` | — | — | — |
| `document_type` | `ref` | [StandardDocumentType](StandardDocumentType.md) | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv

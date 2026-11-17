---
type: Table
title: "Stage"
description: "Standarto rengimo etapų duomenys (etapo kodas, pavadinimas, atlikimo terminas)"
resource: "https://get.data.gov.lt/datasets/gov/lst/standards/Stage"
tags: [gov, lst, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lst/standards.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L180"
    last_modified: "2026-11-11T14:39:20Z"
---

# Stage

Standarto rengimo etapų duomenys (etapo kodas, pavadinimas, atlikimo terminas)

- **Model:** `datasets/gov/lst/standards/Stage`[^manifest]
- **Dataset:** [datasets/gov/lst/standards](../standards.md) (`datasets/gov/lst/standards`)
- **Manifest CSV:** [datasets/gov/lst/standards.csv#L180](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lst/standards.csv#L180)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lst/standards/Stage`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `code` | `string` | — | — | `open` | — | — | — |
| `description` | `string` | — | — | `open` | — | — | — |
| `duration` | `integer` | — | — | `open` | — | — | — |
| `action_type` | `ref` | [ActionType](ActionType.md) | — | `open` | — | — | — |
| `id` | `integer` | — | — | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lst/standards.csv

---
type: Table
title: "Publication"
description: "Spinta table datasets/gov/pb/dizainai/Publication (3 columns)."
tags: [gov, pb, undeployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pb/dizainai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L38"
    last_modified: "2026-11-11T14:39:20Z"
---

# Publication

- **Model:** `datasets/gov/pb/dizainai/Publication`[^manifest]
- **Dataset:** [Dizainai](../dizainai.md) (`datasets/gov/pb/dizainai`)
- **Manifest CSV:** [datasets/gov/pb/dizainai.csv#L38](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L38)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `publication_identifier`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `publication_identifier` | `string` | — | `4` | `open` | — | Publikacijos identifikatorius | — |
| `publication_section` | `string` | — | `3` | `open` | — | Publikacijos skyrius | — |
| `publication_date` | `date` | `D` | `4` | `open` | — | Publikacijos data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/dizainai.csv

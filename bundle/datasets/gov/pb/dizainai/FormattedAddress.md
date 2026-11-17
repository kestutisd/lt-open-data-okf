---
type: Table
title: "FormattedAddress"
description: "Spinta table datasets/gov/pb/dizainai/FormattedAddress (3 columns)."
tags: [gov, pb, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pb/dizainai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L49"
    last_modified: "2026-11-11T14:39:20Z"
---

# FormattedAddress

- **Model:** `datasets/gov/pb/dizainai/FormattedAddress`[^manifest]
- **Dataset:** [Dizainai](../dizainai.md) (`datasets/gov/pb/dizainai`)
- **Manifest CSV:** [datasets/gov/pb/dizainai.csv#L49](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L49)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `address_post_code`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `address_street` | `string` | — | `3` | `open` | — | Pareiškėjo gatvė | — |
| `address_city` | `string` | — | `3` | `open` | — | Pareiškėjo miestas | — |
| `address_post_code` | `string` | — | `3` | `open` | — | Pareiškėjo pašto kodas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/dizainai.csv

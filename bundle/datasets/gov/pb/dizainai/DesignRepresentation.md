---
type: Table
title: "DesignRepresentation"
description: "Spinta table datasets/gov/pb/dizainai/DesignRepresentation (2 columns)."
tags: [gov, pb, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pb/dizainai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L24"
    last_modified: "2026-11-11T14:39:20Z"
---

# DesignRepresentation

- **Model:** `datasets/gov/pb/dizainai/DesignRepresentation`[^manifest]
- **Dataset:** [Dizainai](../dizainai.md) (`datasets/gov/pb/dizainai`)
- **Manifest CSV:** [datasets/gov/pb/dizainai.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pb/dizainai.csv#L24)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `view_uri`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `design` | `ref` | [Design](Design.md) | `4` | `open` | — | — | — |
| `view_uri` | `uri` | — | `3` | `open` | — | Dizaino pagrindinis vaizdas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pb/dizainai.csv

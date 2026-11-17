---
type: Dataset
title: "datasets/gov/pd/itpr"
description: "Spinta dataset datasets/gov/pd/itpr (1 table)."
tags: [gov, pd, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pd/itpr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/itpr.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/pd/itpr

- **Namespace:** `datasets/gov/pd/itpr`[^manifest]
- **Manifest CSV:** [datasets/gov/pd/itpr.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/itpr.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [IeskomuTransportoPriemoniuRegistras](itpr/IeskomuTransportoPriemoniuRegistras.md) | — | `4` | `nationalid` | — | 21 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(dataset)` | `create(type: "param", ref: "dist", source: "/datasets/gov/ivpk/adp/catalog/DatasetDistribution")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pd/itpr.csv

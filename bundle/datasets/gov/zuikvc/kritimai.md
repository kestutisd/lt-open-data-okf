---
type: Dataset
title: "datasets/gov/zuikvc/kritimai"
description: "Spinta dataset datasets/gov/zuikvc/kritimai (1 table)."
tags: [gov, zuikvc, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/kritimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/kritimai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/zuikvc/kritimai

- **Namespace:** `datasets/gov/zuikvc/kritimai`[^manifest]
- **Manifest CSV:** [datasets/gov/zuikvc/kritimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/kritimai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [GyvuliuKritimas](kritimai/GyvuliuKritimas.md) | Gyvulių kritimai | `2` | `savivaldybe` | — | 5 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(dataset)` | `create(type: "param", ref: "dist", source: "/datasets/gov/ivpk/adp/catalog/DatasetDistribution")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/kritimai.csv

---
type: Dataset
title: "datasets/gov/pd/eiis"
description: "Spinta dataset datasets/gov/pd/eiis (3 tables)."
tags: [gov, pd, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/pd/eiis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/eiis.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/pd/eiis

- **Namespace:** `datasets/gov/pd/eiis`[^manifest]
- **Manifest CSV:** [datasets/gov/pd/eiis.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pd/eiis.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [EismoIvykis](eiis/EismoIvykis.md) | — | `4` | `registrokodas` | — | 51 | — |
| [Dalyvis](eiis/Dalyvis.md) | — | `4` | `dalyvis_id` | — | 29 | — |
| [TransportoPriemone](eiis/TransportoPriemone.md) | — | `4` | `tpid` | — | 18 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(dataset)` | `create(type: "param", ref: "dist", source: "/datasets/gov/ivpk/adp/catalog/DatasetDistribution")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pd/eiis.csv

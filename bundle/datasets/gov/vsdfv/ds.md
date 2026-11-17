---
type: Dataset
title: "datasets/gov/vsdfv/ds"
description: "Spinta dataset datasets/gov/vsdfv/ds (2 tables)."
tags: [gov, vsdfv, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/ds.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/ds.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/vsdfv/ds

- **Namespace:** `datasets/gov/vsdfv/ds`[^manifest]
- **Manifest CSV:** [datasets/gov/vsdfv/ds.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/ds.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Draudejai](ds/Draudejai.md) | — | `3` | `draudeju_grupe, draudeju_tipas` | — | 5 | — |
| [Skolininkai](ds/Skolininkai.md) | — | `4` | `draudeju_grupe, draudeju_tipas` | — | 6 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(dataset)` | `update(prepare: 'extract("zip")["draudejai.csv"].file(encoding: "cp1257").tabular(sep: ";")')` | `prepare` | — | — | — | — | — |
| `(dataset)` | `update(prepare: 'extract("zip")["skolininkai.csv"].file(encoding: "cp1257").tabular(sep: ";")')` | `prepare` | — | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/ds.csv

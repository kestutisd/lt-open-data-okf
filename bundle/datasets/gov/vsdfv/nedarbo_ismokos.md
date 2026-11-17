---
type: Dataset
title: "datasets/gov/vsdfv/nedarbo_ismokos"
description: "Spinta dataset datasets/gov/vsdfv/nedarbo_ismokos (1 table)."
tags: [gov, vsdfv, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/nedarbo_ismokos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/nedarbo_ismokos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/vsdfv/nedarbo_ismokos

- **Namespace:** `datasets/gov/vsdfv/nedarbo_ismokos`[^manifest]
- **Manifest CSV:** [datasets/gov/vsdfv/nedarbo_ismokos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/nedarbo_ismokos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NedarboIsmoka](nedarbo_ismokos/NedarboIsmoka.md) | — | `2` | `metu_menuo` | — | 9 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(dataset)` | `update(prepare: 'extract("zip")["nedarbo_ismokos.csv"].file(encoding: "cp1257").tabular(sep: ";")')` | `prepare` | — | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/nedarbo_ismokos.csv

---
type: Dataset
title: "datasets/gov/vsdfv/pkbendroves"
description: "Spinta dataset datasets/gov/vsdfv/pkbendroves (1 table)."
tags: [gov, vsdfv, undeployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vsdfv/pkbendroves.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pkbendroves.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/vsdfv/pkbendroves

- **Namespace:** `datasets/gov/vsdfv/pkbendroves`[^manifest]
- **Manifest CSV:** [datasets/gov/vsdfv/pkbendroves.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsdfv/pkbendroves.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [PkBendrove](pkbendroves/PkBendrove.md) | — | — | `bendr_pav` | — | 2 | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `(dataset)` | `update(prepare: 'extract("zip")["pk_bendroves.csv"].file(encoding: "cp1257").tabular(sep: ";")')` | `prepare` | — | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsdfv/pkbendroves.csv

---
type: Dataset
title: "datasets/gov/vlk/istaigos"
description: "Spinta dataset datasets/gov/vlk/istaigos (1 table)."
resource: "https://get.data.gov.lt/datasets/gov/vlk/istaigos"
tags: [gov, vlk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/vlk_istg.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/vlk_istg.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/vlk/istaigos

- **Namespace:** `datasets/gov/vlk/istaigos`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/vlk_istg.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/vlk_istg.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/istaigos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Istaiga](istaigos/Istaiga.md) | Gydymo įstaigų, vaistinių ir kitų įmonių sąrašas | `4` | `kodas` | — | 18 | Informacija apie gydymo įstaigas, vaistines ir kitas įmones. |

# Enumerations

| Enum (`ref`) | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `bool` | `"Ne"` | — | — | Ne | — |
| `bool` | `"Taip"` | — | — | Taip | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/vlk_istg.csv

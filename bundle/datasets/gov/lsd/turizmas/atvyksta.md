---
type: Dataset
title: "Atvykstamojo turizmo statistiniai tyrimai"
description: "Spinta dataset datasets/gov/lsd/turizmas/atvyksta (2 tables)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/turizmas/atvyksta"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/turizmas/atvyksta.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/turizmas/atvyksta.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Atvykstamojo turizmo statistiniai tyrimai

- **Namespace:** `datasets/gov/lsd/turizmas/atvyksta`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/turizmas/atvyksta.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/turizmas/atvyksta.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/turizmas/atvyksta`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [KelionesAtvykSuNakv2021](atvyksta/KelionesAtvykSuNakv2021.md) | Atvykusių turistų kelionės su nakvyne 2021 m. | — | `id` | — | 55 | — |
| [KelionesAtvykBeNakv2021](atvyksta/KelionesAtvykBeNakv2021.md) | Atvykusių turistų kelionės be nakvynės 2021 m. | — | `id` | — | 32 | — |

# Enumerations

| Enum (`ref`) | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `bool` | `1` | — | — | Taip | — |
| `bool` | `0` | — | — | Ne | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://atviriduomenys.readthedocs.io/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/turizmas/atvyksta.csv

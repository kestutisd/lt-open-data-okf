---
type: Dataset
title: "datasets/gov/vlk/achi"
description: "Spinta dataset datasets/gov/vlk/achi (2 tables)."
resource: "https://get.data.gov.lt/datasets/gov/vlk/achi"
tags: [gov, vlk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/achi.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/achi.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/vlk/achi

- **Namespace:** `datasets/gov/vlk/achi`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/achi.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/achi.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/achi`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Intervencija](achi/Intervencija.md) | Medicininių intervencijų sąrašas | `4` | `ad_id` | — | 16 | Informacija apie medicinines intervencijas. |
| [Paslauga](achi/Paslauga.md) | Dienos chirurgijos metu atiliekamų intervencijų sąrašas | `4` | `ad_id` | — | 7 | — |

# Enumerations

| Enum (`ref`) | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `int_r` | `"Ne"` | — | — | — | — |
| `int_r` | `"Taip"` | — | — | — | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/achi.csv

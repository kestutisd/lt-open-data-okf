---
type: Dataset
title: "datasets/gov/finmin/sis"
description: "Spinta dataset datasets/gov/finmin/sis (4 tables)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sis"
tags: [gov, finmin, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sis/finmin.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/finmin/sis

- **Namespace:** `datasets/gov/finmin/sis`[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/sis/finmin.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sis`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Dokumentas](sis/Dokumentas.md) | Lentelėje pateikti valstybės strategijų, programų dokumentų duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos informacinė sistema (SIS). | `4` | `doc_id` | — | 10 | — |
| [Elementas](sis/Elementas.md) | Lentelėje pateikti valstybės strategijų, programų elementų hierarchijos duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos informacinė sistema (SIS). | `4` | `vda_id` | — | 16 | — |
| [Rodiklis](sis/Rodiklis.md) | Lentelėje pateikti valstybės strategijų, programų rodiklių duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos informacinė sistema (SIS). | `4` | `id_planas` | — | 10 | — |
| [FinansinisDuomuo](sis/FinansinisDuomuo.md) | Lentelėje pateikti valstybės strategijų, programų finansiniai duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos informacinė sistema (SIS). | `4` | `fnv_id` | — | 11 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sis/finmin.csv

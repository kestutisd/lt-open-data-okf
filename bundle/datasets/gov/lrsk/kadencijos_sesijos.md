---
type: Dataset
title: "Lietuvos Respublikos Seimo kadencijų ir sesijų klasifikatorius"
description: "Spinta dataset datasets/gov/lrsk/kadencijos_sesijos (2 tables)."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/kadencijos_sesijos"
tags: [gov, lrsk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lrsk/kadencijos_sesijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/kadencijos_sesijos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lietuvos Respublikos Seimo kadencijų ir sesijų klasifikatorius

- **Namespace:** `datasets/gov/lrsk/kadencijos_sesijos`[^manifest]
- **Manifest CSV:** [datasets/gov/lrsk/kadencijos_sesijos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/kadencijos_sesijos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/kadencijos_sesijos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Sesija](kadencijos_sesijos/Sesija.md) | Lietuvos Respublikos Seimo sesijų tvarkaraštis | `4` | `id` | — | 7 | Lietuvos Respublikos Seimo sesijų tvarkaraštis. |
| [Kadencija](kadencijos_sesijos/Kadencija.md) | Lietuvos Respublikos Seimo kadencijų tvarkaraštis | `4` | `id` | — | 3 | Lietuvos Respublikos Seimo kadencijų tvarkaraštis su kadencijų pradžios ir pabaigos datomis. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/kadencijos_sesijos.csv

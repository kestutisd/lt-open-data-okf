---
type: Dataset
title: "Nuolatinių Lietuvos gyventojų, mirusių Lietuvoje ar užsienyje, mirties atvejų ir jų priežasčių duomenys"
description: "Spinta dataset datasets/gov/hi/mirtys (2 tables)."
resource: "https://get.data.gov.lt/datasets/gov/hi/mirtys"
tags: [gov, hi, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/mirties_priezastys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/mirties_priezastys.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Nuolatinių Lietuvos gyventojų, mirusių Lietuvoje ar užsienyje, mirties atvejų ir jų priežasčių duomenys

- **Namespace:** `datasets/gov/hi/mirtys`[^manifest]
- **Manifest CSV:** [datasets/gov/hi/mirties_priezastys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/mirties_priezastys.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/mirtys`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NuolatinisGyventojas](mirtys/NuolatinisGyventojas.md) | Nuolatinių Lietuvos Respublikos gyventojų mirties atvejai ir jų priežastys | `4` | `m_id` | — | 26 | — |
| [Negyvagimis](mirtys/Negyvagimis.md) | Nuolatinių Lietuvos Respublikos gyventojų negyvagimių mirties atvejai ir jų priežastys | `3` | `m_id` | — | 26 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/mirties_priezastys.csv

---
type: Dataset
title: "Lietuvos Respublikos profesinių ligų valstybės registro duomenys"
description: "Spinta dataset datasets/gov/hi/profesines (3 tables)."
resource: "https://get.data.gov.lt/datasets/gov/hi/profesines"
tags: [gov, hi, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/profesines.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Lietuvos Respublikos profesinių ligų valstybės registro duomenys

- **Namespace:** `datasets/gov/hi/profesines`[^manifest]
- **Manifest CSV:** [datasets/gov/hi/profesines.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/profesines.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/profesines`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Issilavinimas](profesines/Issilavinimas.md) | Profesinių ligų atvejai pagal išsilavinimą | `4` | `atvejis_id` | — | 8 | — |
| [DarboStazas](profesines/DarboStazas.md) | Profesinių ligų atvejai pagal darbo stažą | `4` | `atvejis_id` | — | 8 | — |
| [Asmuo](profesines/Asmuo.md) | Profesinių ligų įvykių pagrindiniai duomenys | `4` | `m_id` | — | 15 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/profesines.csv

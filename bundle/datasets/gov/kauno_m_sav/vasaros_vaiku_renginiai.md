---
type: Dataset
title: "datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai"
description: "Šiame rinkinyje pateikti Kauno miesto savivaldybės vaikų vasaros renginių duomenis."
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai"
tags: [gov, kauno_m_sav, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai

Šiame rinkinyje pateikti Kauno miesto savivaldybės vaikų vasaros renginių duomenis. Rinkinys talpina pačių renginių aprašymus, dalyvavusius vaikus bei asmenis kurie registravo vaikus į šiuos renginius.

- **Namespace:** `datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai`[^manifest]
- **Manifest CSV:** [datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Dalyvis](vasaros_vaiku_renginiai/Dalyvis.md) | Dalyvių sąrašas | `4` | `vda_primary_key` | — | 10 | Šiame rinkinyje pateiktas Kauno miesto savivaldybės vaikų vasaros renginių dalyvių sąrašas. |
| [Renginys](vasaros_vaiku_renginiai/Renginys.md) | Renginių sąrašas | `4` | `renginio_id` | — | 25 | Šiame rinkinyje pateiktas Kauno miesto savivaldybės vaikų vasaros renginių sąrašas. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/vasaros_vaiku_renginiai.csv

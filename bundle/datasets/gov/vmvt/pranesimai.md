---
type: Dataset
title: "Pranešimai"
description: "Spinta dataset datasets/gov/vmvt/pranesimai (3 tables)."
resource: "https://get.data.gov.lt/datasets/gov/vmvt/pranesimai"
tags: [gov, vmvt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmvt/rasff/pranesimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/rasff/pranesimai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pranešimai

- **Namespace:** `datasets/gov/vmvt/pranesimai`[^manifest]
- **Manifest CSV:** [datasets/gov/vmvt/rasff/pranesimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmvt/rasff/pranesimai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmvt/pranesimai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Pranesimas](pranesimai/Pranesimas.md) | Pranešimų duomenys | `4` | `pranesimo_id` | — | 11 | Pateikiami pranešimai apie nustatytus pažeidimus, pažeidimo rūšį, pavojų, pažeidimo tipą, aptikimo tipą, išplatinimo ribas, rizikos tipą ir rizikos taikymo... |
| [Siunta](pranesimai/Siunta.md) | Siuntų duomenys | `4` | `siuntos_id` | — | 8 | Pateikiami siuntų duomenys: kilmės šalis, produkto grupė, produkto pavadinimas, partijos numeris, tinkamumo terminas ir tinkamumo tipas. |
| [Subjektas](pranesimai/Subjektas.md) | Subjektų duomenys | `4` | `id` | — | 6 | Pateikiama informacija apie ukio subjektus: subjekto pavadinimas, tipas ir šalis. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmvt/rasff/pranesimai.csv

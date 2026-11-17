---
type: Dataset
title: "datasets/gov/palangos_gintaras/pacientai"
description: "Spinta dataset datasets/gov/palangos_gintaras/pacientai (2 tables)."
resource: "https://get.data.gov.lt/datasets/gov/palangos_gintaras/pacientai"
tags: [gov, palangos_gintaras, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/palangos_gintaras/pacientai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/palangos_gintaras/pacientai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/palangos_gintaras/pacientai

- **Namespace:** `datasets/gov/palangos_gintaras/pacientai`[^manifest]
- **Manifest CSV:** [datasets/gov/palangos_gintaras/pacientai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/palangos_gintaras/pacientai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/palangos_gintaras/pacientai`
- **Parent Namespace (`ns`):** Vaikų reabilitacijos sanatorija "Palangos gintaras" (`datasets/gov/palangos_gintaras`)

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Ligonis](pacientai/Ligonis.md) | Pacientų sąrašas | `4` | `vda_id` | — | 5 | Vaikų reabilitacijos sanatorijos „Palangos gintaras“ pacientų sąrašas. |
| [PacientoRegistracija](pacientai/PacientoRegistracija.md) | Pacientų registracijų sąrašas | `4` | `vda_id` | — | 21 | Vaikų reabilitacijos sanatorijos „Palangos gintaras“ pacientų registracijų sąrašas. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/palangos_gintaras/pacientai.csv

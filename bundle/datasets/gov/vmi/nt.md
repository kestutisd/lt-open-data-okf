---
type: Dataset
title: "Nekilnojamo turto mokesčio duomenų rinkinys"
description: "Nekilnojamo turto mokesčio (toliau - NTM) duomenų rinkinys"
resource: "https://get.data.gov.lt/datasets/gov/vmi/nt"
tags: [gov, vmi, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vmi/nt.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/nt.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Nekilnojamo turto mokesčio duomenų rinkinys

Nekilnojamo turto mokesčio (toliau - NTM) duomenų rinkinys

- **Namespace:** `datasets/gov/vmi/nt`[^manifest]
- **Manifest CSV:** [datasets/gov/vmi/nt.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vmi/nt.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vmi/nt`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [BendrasNtMokestis](nt/BendrasNtMokestis.md) | NT mokesčio mokėtojo ir NT bendri duomenys | `2` | — | — | 13 | Nekilnojamojo turto (toliau - NT) mokesčio mokėtojo ir NT bendri duomenys |
| [AvansinisNtMokestis](nt/AvansinisNtMokestis.md) | Avansinio NT mokesčio duomenys | `2` | — | — | 10 | — |
| [SavivaldybeNtMokestis](nt/SavivaldybeNtMokestis.md) | NT mokesčio duomenys pagal savivaldybes | `3` | — | — | 20 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vmi/nt.csv

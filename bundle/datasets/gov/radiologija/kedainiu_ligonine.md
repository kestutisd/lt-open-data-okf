---
type: Dataset
title: "Kėdainių ligoninės pacientams atliktų radiologinių tyrimų duomenys"
description: "Spinta dataset datasets/gov/radiologija/kedainiu_ligonine (2 tables)."
resource: "https://get.data.gov.lt/datasets/gov/radiologija/kedainiu_ligonine"
tags: [gov, radiologija, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L668"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kėdainių ligoninės pacientams atliktų radiologinių tyrimų duomenys

- **Namespace:** `datasets/gov/radiologija/kedainiu_ligonine`[^manifest]
- **Manifest CSV:** [datasets/gov/radiologija/radiologija.csv#L668](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/radiologija/radiologija.csv#L668)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/radiologija/kedainiu_ligonine`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Cedara](kedainiu_ligonine/Cedara.md) | Kėdainių ligoninės „CEDARA“ sistemoje pacientams atliktų radiologinių tyrimų duomenys | — | `vda_prime_key` | — | 18 | Informacinėje sistemoje „CEDARA“ kaupiami Kėdainių ligoninės pacientams atliktų radiologinių tyrimų duomenys. |
| [Meddream](kedainiu_ligonine/Meddream.md) | Kėdainių ligoninės „Meddream“ sistemoje pacientams atliktų radiologinių tyrimų duomenys | — | `vda_prime_key` | — | 17 | Informacinėje sistemoje „MedDream“ kaupiami Kėdainių ligoninės pacientams atliktų radiologinių tyrimų duomenys. |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/radiologija/radiologija.csv

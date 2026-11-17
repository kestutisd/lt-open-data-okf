---
type: Dataset
title: "datasets/gov/finmin/paraiskos"
description: "Spinta dataset datasets/gov/finmin/paraiskos (8 tables)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/paraiskos"
tags: [gov, finmin, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/finmin/paraiskos

- **Namespace:** `datasets/gov/finmin/paraiskos`[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/paraiskos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/paraiskos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/paraiskos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Project](paraiskos/Project.md) | Projektas ir jo vertinimai | `4` | `project_id` | — | 17 | — |
| [Application](paraiskos/Application.md) | Projekto paraiška | `4` | `project` | — | 17 | — |
| [AppPartner](paraiskos/AppPartner.md) | Paraiškos partneriai | `4` | `app_partner_id` | — | 7 | — |
| [AppPurchase](paraiskos/AppPurchase.md) | Vykdomi ir iki paraiškos pateikimo įvykdyti pirkimai | `4` | `app_purchase_id` | — | 6 | — |
| [AppIndicator](paraiskos/AppIndicator.md) | Paraiškos produkto ir rezultato stebėsenos rodikliai | `4` | `app_indicator_id` | — | 4 | — |
| [AppFinSource](paraiskos/AppFinSource.md) | Paraiškos projekto tinkamų finansuoti išlaidų finansavimo šaltiniai | `4` | `app_fin_source_id` | — | 5 | — |
| [AppTask](paraiskos/AppTask.md) | Paraiškos uždaviniai | `4` | `app_task_id` | — | 4 | — |
| [AppActivity](paraiskos/AppActivity.md) | Paraiškos uždavinio veiklos | `4` | `app_activity_id` | — | 4 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://atviriduomenys.readthedocs.io/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/paraiskos.csv

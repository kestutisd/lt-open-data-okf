---
type: Dataset
title: "2014-2020 m. ES fondų projektų kontrolės veiksmų duomenys"
description: "Spinta dataset datasets/gov/finmin/kontroles_veiksmai (3 tables)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/kontroles_veiksmai"
tags: [gov, finmin, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/kontroles_veiksmai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kontroles_veiksmai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# 2014-2020 m. ES fondų projektų kontrolės veiksmų duomenys

- **Namespace:** `datasets/gov/finmin/kontroles_veiksmai`[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/kontroles_veiksmai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kontroles_veiksmai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/kontroles_veiksmai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Revise](kontroles_veiksmai/Revise.md) | Projekto patikros vietoje | `4` | `revise_id` | — | 13 | — |
| [Suspicion](kontroles_veiksmai/Suspicion.md) | Įtarimas | `4` | `suspicion_id` | — | 19 | — |
| [Audit](kontroles_veiksmai/Audit.md) | Projekto audito pastebėjimai | `4` | `audit_id` | — | 18 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://atviriduomenys.readthedocs.io/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/kontroles_veiksmai.csv

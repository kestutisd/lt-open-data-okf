---
type: Dataset
title: "datasets/gov/finmin/kvietimai"
description: "Spinta dataset datasets/gov/finmin/kvietimai (6 tables)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/kvietimai"
tags: [gov, finmin, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/finmin/kvietimai

- **Namespace:** `datasets/gov/finmin/kvietimai`[^manifest]
- **Manifest CSV:** [datasets/gov/finmin/kvietimai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/kvietimai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/kvietimai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Measure](kvietimai/Measure.md) | Investicinio prioriteto uždavinio priemonė | `4` | `measure_id` | — | 11 | — |
| [Call](kvietimai/Call.md) | Kvietimas / patvirtintas sąrašas | `4` | `call_id` | — | 14 | — |
| [MeasureIndicator](kvietimai/MeasureIndicator.md) | Priemonės stebėsenos rodiklis | `4` | `measure_indicator_id` | — | 17 | — |
| [Task](kvietimai/Task.md) | Investicinio prioriteto uždavinys | `4` | `task_id` | — | 6 | — |
| [Priority](kvietimai/Priority.md) | Prioritetas | `4` | `priority_id` | — | 5 | — |
| [PriorityFund](kvietimai/PriorityFund.md) | Prioriteto fondas | `4` | `priority_fund_id` | — | 5 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://atviriduomenys.readthedocs.io/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/kvietimai.csv

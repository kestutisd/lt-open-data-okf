---
type: Dataset
title: "Švietimo įstaigų lankomumo rodikliai"
description: "Spinta dataset datasets/gov/nsa/silr (3 tables)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/silr"
tags: [gov, nsa, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nsa/silr/silr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/silr/silr.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Švietimo įstaigų lankomumo rodikliai

- **Namespace:** `datasets/gov/nsa/silr`[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/silr/silr.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/silr/silr.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/silr`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Lankomumas](silr/Lankomumas.md) | Mokinių lankomumas | `4` | `vda_id` | — | 12 | — |
| [Mokykla](silr/Mokykla.md) | Mokinių lankomumo duomenų mokyklos | `4` | `vda_id` | — | 7 | — |
| [MokDalykas](silr/MokDalykas.md) | Mokinių lankomumo duomenų mokomųjų dalykų klasifikatorius | `4` | `vda_id` | — | 4 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/silr/silr.csv

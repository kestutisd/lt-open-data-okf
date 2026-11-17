---
type: Dataset
title: "datasets/gov/vlk/paslaugos"
description: "Spinta dataset datasets/gov/vlk/paslaugos (2 tables)."
resource: "https://get.data.gov.lt/datasets/gov/vlk/paslaugos"
tags: [gov, vlk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/paslaugos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/paslaugos.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/vlk/paslaugos

- **Namespace:** `datasets/gov/vlk/paslaugos`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/paslaugos.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/paslaugos.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/paslaugos`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Paslauga](paslaugos/Paslauga.md) | Asmens sveikatos priežiūros paslaugų sąrašas | `4` | `ad_id` | — | 10 | Asmens sveikatos priežiūros paslaugų klasifikatorius, patvirtintas Valstybinės ligonių kasos prie Sveikatos apsaugos ministerijos direktoriaus 2005 m.... |
| [Balas](paslaugos/Balas.md) | Bazinių kainų balais sąrašas | `4` | `ad_id` | — | 8 | Asmens sveikatos priežiūros paslaugų bazinių balų sąrašas |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/paslaugos.csv

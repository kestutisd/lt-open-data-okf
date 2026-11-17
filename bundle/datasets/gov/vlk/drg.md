---
type: Dataset
title: "datasets/gov/vlk/drg"
description: "Spinta dataset datasets/gov/vlk/drg (4 tables)."
resource: "https://get.data.gov.lt/datasets/gov/vlk/drg"
tags: [gov, vlk, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/drg.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/vlk/drg

- **Namespace:** `datasets/gov/vlk/drg`[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/drg.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/drg.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/drg`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Grupe](drg/Grupe.md) | DRG grupių sąrašas | `4` | — | — | 9 | Informacija apie giminingų diagnozių grupes. |
| [Koeficientai](drg/Koeficientai.md) | DRG koeficientai | `4` | — | — | 8 | Giminingų diagnozių grupių paros/dienos gydymo kainų koeficientai |
| [Trukmes](drg/Trukmes.md) | DRG trukmės | `4` | — | — | 6 | Giminingų diagnozių grupių gydymo trukmės |
| [Versija](drg/Versija.md) | DRG versijos | `4` | — | — | 3 | AR-DRG klasifikacijos versija |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/drg.csv

---
type: Dataset
title: "datasets/gov/vat/saugomos_veisles"
description: "Spinta dataset datasets/gov/vat/saugomos_veisles (3 tables)."
resource: "https://get.data.gov.lt/datasets/gov/vat/saugomos_veisles"
tags: [gov, vat, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/saugomos_veisles.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/saugomos_veisles.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# datasets/gov/vat/saugomos_veisles

- **Namespace:** `datasets/gov/vat/saugomos_veisles`[^manifest]
- **Manifest CSV:** [datasets/gov/vat/saugomos_veisles.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/saugomos_veisles.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/saugomos_veisles`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [Veisle](saugomos_veisles/Veisle.md) | Pateikiama informacija apie į Nacionalinį sąrašą įrašytas veisles, išbrauktas veisles, veislių palaikytojų ir selekcininkų įgaliotųjų atstovų sąrašus. | `4` | `id` | `open` | 14 | — |
| [Verte](saugomos_veisles/Verte.md) | Pateikiama informacija apie atlikto ūkinio vertingumo tyrimo duomenis. | `4` | `id` | `open` | 10 | — |
| [SaugVeisle](saugomos_veisles/SaugVeisle.md) | Saugomų augalų veislių sąrašas. | `4` | `eil_nr` | `open` | 7 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/saugomos_veisles.csv

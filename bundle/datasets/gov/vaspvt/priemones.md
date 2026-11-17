---
type: Dataset
title: "Sveikatos priežiūros technologijų, susijusių su medicinos prietaisais, vertinimo ir valdymo duomenys"
description: "Spinta dataset datasets/gov/vaspvt/priemones (5 tables)."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/priemones"
tags: [gov, vaspvt, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_iranga.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_iranga.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sveikatos priežiūros technologijų, susijusių su medicinos prietaisais, vertinimo ir valdymo duomenys

- **Namespace:** `datasets/gov/vaspvt/priemones`[^manifest]
- **Manifest CSV:** [datasets/gov/vaspvt/medicinos_iranga.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/medicinos_iranga.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/priemones`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [MedicinosPriemone](priemones/MedicinosPriemone.md) | Brangių medicinos priemonių sąrašas | `4` | `id` | `open` | 32 | — |
| [IstaigosAtaskaituDuomenys](priemones/IstaigosAtaskaituDuomenys.md) | Istaigų Ataskaitų Duomenys | `4` | `vda_prime_key` | `open` | 72 | — |
| [IstaigosDuomenys](priemones/IstaigosDuomenys.md) | Istaigu_Duomenys | `4` | `vda_prime_key` | `open` | 57 | — |
| [MedicinosPriemoniuAtaskaita](priemones/MedicinosPriemoniuAtaskaita.md) | Ataskaitų Apie Brangias Priemones Sąrašas | `4` | `id` | `open` | 18 | — |
| [Ataskaita](priemones/Ataskaita.md) | Ataskaita | `4` | `id` | `open` | 16 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/medicinos_iranga.csv

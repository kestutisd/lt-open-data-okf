---
type: Dataset
title: "Asmenys, paskiepyti įvairių ligų skiepais"
description: "Spinta dataset datasets/gov/lsd/sveikata/skiepai (3 tables)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/sveikata/skiepai"
tags: [gov, lsd, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/sveikata/skiepai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# Asmenys, paskiepyti įvairių ligų skiepais

- **Namespace:** `datasets/gov/lsd/sveikata/skiepai`[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/sveikata/skiepai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/sveikata/skiepai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/sveikata/skiepai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [SkiepytiGripo](skiepai/SkiepytiGripo.md) | Asmenys, paskiepyti šaltojo sezono ligų (gripo) skiepais, pagal ligą (gripas), įstaigą lytį ir amžiaus grupę | — | `vda_prime_key` | — | 11 | Kol kas pateikti tik gripo duomenys |
| [SkiepytiPadieniui](skiepai/SkiepytiPadieniui.md) | Pasiskiepiję asmenys pagal dieną ir ligą | — | `vda_prime_key` | — | 4 | — |
| [SkiepytiVakcina](skiepai/SkiepytiVakcina.md) | Pasiskiepiję asmenys pagal laikotarpį, ligą, vakciną ir įstaigą | — | `vda_prime_key` | — | 10 | — |

# Prefixes

| Prefix | URI |
| --- | --- |
| `spinta` | `https://github.com/atviriduomenys/spinta/issues/` |
| `manifest` | `https://github.com/atviriduomenys/manifest/issues/` |
| `vadovas` | `https://atviriduomenys.readthedocs.io/` |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/sveikata/skiepai.csv

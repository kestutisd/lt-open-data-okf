---
type: Dataset
title: "NTR paskirčių klasifikatoriai"
description: "Spinta dataset datasets/gov/rc/ntr/ntr_paskirtys (3 tables)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_paskirtys"
tags: [gov, rc, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_paskirtys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_paskirtys.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# NTR paskirčių klasifikatoriai

- **Namespace:** `datasets/gov/rc/ntr/ntr_paskirtys`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_paskirtys.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_paskirtys.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_paskirtys`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NtrPaskirtiesGrupe](ntr_paskirtys/NtrPaskirtiesGrupe.md) | NTR paskirčių grupės | `4` | `pasg_grupe` | — | 4 | — |
| [NtrPaskirtiesTipas](ntr_paskirtys/NtrPaskirtiesTipas.md) | NTR paskirčių tipai | `4` | `pask_tipas` | — | 6 | — |
| [NtrLeistinaPaskirtis](ntr_paskirtys/NtrLeistinaPaskirtis.md) | NTR leistinos paskirtys pagal objekto tipus | `3` | `obje_tipas` | — | 3 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_paskirtys.csv

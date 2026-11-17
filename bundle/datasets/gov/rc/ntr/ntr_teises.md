---
type: Dataset
title: "NTR teisių tipų ir teisių potipių klasifikatoriai"
description: "Spinta dataset datasets/gov/rc/ntr/ntr_teises (2 tables)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_teises"
tags: [gov, rc, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_teises.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_teises.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# NTR teisių tipų ir teisių potipių klasifikatoriai

- **Namespace:** `datasets/gov/rc/ntr/ntr_teises`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_teises.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_teises.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_teises`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NtrTeisesTipas](ntr_teises/NtrTeisesTipas.md) | NTR teisių ir suvaržymų tipai | `4` | `teit_tipas` | — | 8 | — |
| [NtrTeisesPotipis](ntr_teises/NtrTeisesPotipis.md) | NTR teisių ir suvaržymų potipiai | `4` | `teit_tipas, teip_potipis` | — | 14 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_teises.csv

---
type: Dataset
title: "NTR atributų klasifikatoriai"
description: "Spinta dataset datasets/gov/rc/ntr/ntr_atributai (5 tables)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai"
tags: [gov, rc, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# NTR atributų klasifikatoriai

- **Namespace:** `datasets/gov/rc/ntr/ntr_atributai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_atributai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_atributai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_atributai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NtrAtributas](ntr_atributai/NtrAtributas.md) | NTR atributų klasifikatorius | `4` | `atri_kodas` | — | 12 | — |
| [NtrAtributoReiksme](ntr_atributai/NtrAtributoReiksme.md) | NTR atributų reikšmių klasifikatorius | `3` | `atri_kodas, reik_reiksme` | — | 8 | — |
| [NtrAtributoTipas](ntr_atributai/NtrAtributoTipas.md) | NTR atributų tipų (kiekybiniai, kokybiniai, vertinimo) klasifikatorius | `4` | `atrt_tipas` | — | 3 | — |
| [NtrLeistinasAtributas](ntr_atributai/NtrLeistinasAtributas.md) | NTR leistinų atributų klasifikatorius | `4` | `obje_tipas, atri_kodas` | — | 11 | — |
| [NtrAtributoPozymis](ntr_atributai/NtrAtributoPozymis.md) | NTR atributų požymių (būtinas, galimas) klasifikatorius | `4` | `atrp_poz` | — | 3 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_atributai.csv

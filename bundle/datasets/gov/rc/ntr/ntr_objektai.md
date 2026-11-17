---
type: Dataset
title: "NTR objektus apibūdinantys klasifikatoriai"
description: "Spinta dataset datasets/gov/rc/ntr/ntr_objektai (5 tables)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai"
tags: [gov, rc, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_objektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L2"
    last_modified: "2026-11-11T14:39:20Z"
---

# NTR objektus apibūdinantys klasifikatoriai

- **Namespace:** `datasets/gov/rc/ntr/ntr_objektai`[^manifest]
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_objektai.csv#L2](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L2)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai`

# Tables

| Table | Title | Level | Primary Key | Access | Columns | Description |
| --- | --- | --- | --- | --- | --- | --- |
| [NtrObjektoTipas](ntr_objektai/NtrObjektoTipas.md) | NT objektų tipų klasifikatorius | `4` | `obje_tipas` | — | 16 | — |
| [NtrLeisinasObjektoTipas](ntr_objektai/NtrLeisinasObjektoTipas.md) | Nurodytam registro tipui leistinų objektų tipų sąrašas - klasifikatorius | `3` | `regt_tipas, obje_tipas, loti_priklauso` | — | 6 | — |
| [NtrTurtoGrupe](ntr_objektai/NtrTurtoGrupe.md) | NTR turto objektų grupių klasifikatorius | `4` | `objg_grupe` | — | 4 | — |
| [NtrObjektoBukle](ntr_objektai/NtrObjektoBukle.md) | NTR objektų būklių klasifikatorius | `4` | `obuk_bukle` | — | 6 | — |
| [NtrObjektoStatusas](ntr_objektai/NtrObjektoStatusas.md) | NTR objektų statusų klasifikatorius | `4` | `osta_statusas` | — | 6 | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_objektai.csv

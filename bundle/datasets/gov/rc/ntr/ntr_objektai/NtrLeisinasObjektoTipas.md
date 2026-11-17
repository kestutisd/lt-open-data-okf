---
type: Table
title: "NtrLeisinasObjektoTipas — Nurodytam registro tipui leistinų objektų tipų sąrašas - klasifikatorius"
description: "Spinta table datasets/gov/rc/ntr/ntr_objektai/NtrLeisinasObjektoTipas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai/NtrLeisinasObjektoTipas"
tags: [gov, rc, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_objektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L23"
    last_modified: "2026-11-11T14:39:20Z"
---

# NtrLeisinasObjektoTipas — Nurodytam registro tipui leistinų objektų tipų sąrašas - klasifikatorius

- **Model:** `datasets/gov/rc/ntr/ntr_objektai/NtrLeisinasObjektoTipas`[^manifest]
- **Dataset:** [NTR objektus apibūdinantys klasifikatoriai](../ntr_objektai.md) (`datasets/gov/rc/ntr/ntr_objektai`)
- **Manifest CSV:** [datasets/gov/rc/ntr/ntr_objektai.csv#L23](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ntr/ntr_objektai.csv#L23)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ntr/ntr_objektai/NtrLeisinasObjektoTipas`
- **Primary Key (`ref`):** `regt_tipas, obje_tipas, loti_priklauso`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `regt_tipas` | `integer` | — | `3` | `open` | — | Registro tipas | — |
| `obje_tipas` | `ref` | [NtrObjektoTipas](NtrObjektoTipas.md) | `4` | `open` | — | Turto objekto tipas | — |
| `loti_priklauso` | `integer` | — | `3` | `open` | — | Priklauso objekto tipui | — |
| `loti_koregavimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo koregavimo data | — |
| `loti_data_nuo` | `datetime` | `S` | `4` | `open` | — | Įrašas galioja nuo | — |
| `loti_data_iki` | `datetime` | `S` | `4` | `open` | — | Įrašas galioja iki | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ntr/ntr_objektai.csv

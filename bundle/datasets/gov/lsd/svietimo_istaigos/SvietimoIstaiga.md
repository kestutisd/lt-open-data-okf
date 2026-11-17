---
type: Table
title: "SvietimoIstaiga — Švietimo ir mokslo institucijos"
description: "Spinta table datasets/gov/lsd/svietimo_istaigos/SvietimoIstaiga (16 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/svietimo_istaigos/SvietimoIstaiga"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/svietimo_istaigos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/svietimo_istaigos.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# SvietimoIstaiga — Švietimo ir mokslo institucijos

- **Model:** `datasets/gov/lsd/svietimo_istaigos/SvietimoIstaiga`[^manifest]
- **Dataset:** [Švietimo ir mokslo institucijos](../svietimo_istaigos.md) (`datasets/gov/lsd/svietimo_istaigos`)
- **Manifest CSV:** [datasets/gov/lsd/svietimo_istaigos.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/svietimo_istaigos.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/svietimo_istaigos/SvietimoIstaiga`
- **Primary Key (`ref`):** `ins_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ins_id` | `string` | — | `4` | `open` | — | Identifikacinis institucijos kodas Švietimo ir mokslo institucijų registre (ŠMIR) | — |
| `ins_kodas` | `integer` | — | `2` | `open` | — | institucijos kodas Juridinių asmenų registre | — |
| `ins_pavad_lt` | `string` | — | `2` | `open` | — | Institucijos pavadinimas | — |
| `ins_motin_id` | `integer` | — | `2` | `open` | — | Motininės institucijos kodas | — |
| `ins_ireg_smir_data` | `date` | `D` | `4` | `open` | — | Institucijos įregistravimo ŠMIR data | — |
| `ins_isreg_smir_data` | `date` | `D` | `4` | `open` | — | Institucijos išregistravimo iš ŠMIR data | — |
| `ins_pask_grupe` | `string` | — | `3` | `open` | — | Institucijos paskirties grupė | — |
| `ins_pagr_tipas` | `string` | — | `3` | `open` | — | Institucijos tipas | — |
| `savivaldybe` | `integer` | — | `2` | `open` | — | Savivaldybės"," kurioje yra institucija kodas | — |
| `sav_pav` | `string` | — | `2` | `open` | — | Savivaldybės"," kurioje yra institucija pavadinimas | — |
| `sen_kodas` | `integer` | — | `2` | `open` | — | Seniūnijos"," kurioje yra institucija kodas | — |
| `sen_pav` | `string` | — | `2` | `open` | — | Seniūnijos"," kurioje yra institucija pavadinimas | — |
| `gyv_kodas` | `integer` | — | `2` | `open` | — | Gyvenvietės"," kurioje yra institucija kodas | — |
| `gyv_pav` | `string` | — | `2` | `open` | — | Gyvenvietės"," kurioje yra institucija pavadinimas | — |
| `gyvenamoji_vietove` | `string` | — | `3` | `open` | — | Gyvenvietės"," kurioje yra institucija tipas | — |
| `koord` | `geometry(point,3346)` | `m` | `4` | `open` | — | Švietimo institucijos koordinatės | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ins_kodas` | `create(property: "ja_kodas", type: "ref", ref: "datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo")` | `type` | `4` | `open` | — | — | — |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.sav_kodas", type: "")` | `type` | `4` | — | — | — | — |
| `sen_kodas` | `create(property: "seniunija", type: "ref", ref: "datasets/gov/rc/ar/seniunija/Seniunija")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/svietimo_istaigos.csv

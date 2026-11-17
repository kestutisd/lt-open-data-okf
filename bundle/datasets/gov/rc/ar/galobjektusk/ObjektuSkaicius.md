---
type: Table
title: "ObjektuSkaicius — Adresų registro galiojančių objektų kiekiai mėnesio pradžiai"
description: "Spinta table datasets/gov/rc/ar/galobjektusk/ObjektuSkaicius (15 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/galobjektusk/ObjektuSkaicius"
tags: [gov, rc, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/galiojanciu_objektu_kiekiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/galiojanciu_objektu_kiekiai.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# ObjektuSkaicius — Adresų registro galiojančių objektų kiekiai mėnesio pradžiai

- **Model:** `datasets/gov/rc/ar/galobjektusk/ObjektuSkaicius`[^manifest]
- **Dataset:** [Adresų registro galiojančių objektų kiekiai mėnesio pradžiai](../galobjektusk.md) (`datasets/gov/rc/ar/galobjektusk`)
- **Manifest CSV:** [datasets/gov/rc/ar/galiojanciu_objektu_kiekiai.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/galiojanciu_objektu_kiekiai.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/galobjektusk/ObjektuSkaicius`
- **Primary Key (`ref`):** `savivaldybe, metai, menuo`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `apskritis` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis](../apskritis/Apskritis.md) | `4` | `open` | — | Apskrities kodas | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/savivaldybe/Savivaldybe](../savivaldybe/Savivaldybe.md) | `4` | `open` | — | Savivaldybės kodas | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `menuo` | `integer` | — | `2` | `open` | — | Mėnuo | — |
| `sen_kiekis` | `integer` | `U` | `4` | `open` | — | Seniūnijų sk. | — |
| `gyv_vietoves_viso` | `integer` | `U` | `4` | `open` | — | Gyvenamųjų vietovių sk. iš viso | — |
| `gyv_vietoves_m` | `integer` | `U` | `4` | `open` | — | Miesto tipo gyvenamųjų vietovių sk. | — |
| `gyv_vietoves_mstl` | `integer` | `U` | `4` | `open` | — | Miestelio tipo gyvenamųjų vietovių sk. | — |
| `gyv_vietoves_k` | `integer` | `U` | `4` | `open` | — | Kaimo tipo gyvenamųjų vietovių sk. | — |
| `gyv_vietoves_vs` | `integer` | `U` | `4` | `open` | — | Viensėdžio tipo gyvenamųjų vietovių sk. | — |
| `gyv_vietoves_su_gat` | `integer` | `U` | `4` | `open` | — | Gyvenamųjų vietovių su gatvėmis sk. | — |
| `gyv_vietoves_be_gat_su_adr` | `integer` | `U` | `4` | `open` | — | Gyvenamųjų vietovių su adresais, be gatvių, sk. | — |
| `gat_kiekis` | `integer` | `U` | `4` | `open` | — | Gatvių sk. | — |
| `adresu_kiekis` | `integer` | `U` | `4` | `open` | — | Adresų taškų sk. | — |
| `pat_kiekis` | `integer` | `U` | `4` | `open` | — | Patalpų adresų sk. | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/galiojanciu_objektu_kiekiai.csv

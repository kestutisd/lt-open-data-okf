---
type: Table
title: "AdresoTaskas — Adresų registro žemės sklypams ir pastatams suteiktų adresų erdviniai duomenysAdresų registro žemės sklypams ir pastatams suteiktų adresų erdviniai duomenys"
description: "Žemės sklypams ir pastatams suteiktų adresų erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (žemės sklypams ir pastatams suteiktus adresus apibūdinantys duomenys (duomenų rinkinių grupė, 60 vnt.))."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/adresotaskas/AdresoTaskas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/adresotaskas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/adresotaskas.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# AdresoTaskas — Adresų registro žemės sklypams ir pastatams suteiktų adresų erdviniai duomenysAdresų registro žemės sklypams ir pastatams suteiktų adresų erdviniai duomenys

Žemės sklypams ir pastatams suteiktų adresų erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (žemės sklypams ir pastatams suteiktus adresus apibūdinantys duomenys (duomenų rinkinių grupė, 60 vnt.)). Duomenų geografinė imtis — visa šalies teritorija.

- **Model:** `datasets/gov/rc/ar/adresotaskas/AdresoTaskas`[^manifest]
- **Dataset:** [Adresų registras](../adresotaskas.md) (`datasets/gov/rc/ar/adresotaskas`)
- **Manifest CSV:** [datasets/gov/rc/ar/adresotaskas.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/adresotaskas.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/adresotaskas/AdresoTaskas`
- **Primary Key (`ref`):** `aob_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aob_kodas` | `integer` | — | `4` | `open` | — | Adreso kodas, unikalus Respublikos mastu (nuolat palaikomas) | — |
| `gyvenamoji_vietove` | `ref` | [/datasets/gov/rc/ar/gragyvenamojivietove/GraGyvenamojiVietove](../gragyvenamojivietove/GraGyvenamojiVietove.md) | `4` | `open` | — | Gyvenamosios vietovės kodas Registre (nekeičiamas gyvenamosios vietovės egzistavimo laiką) | — |
| `gatve` | `ref` | [/datasets/gov/rc/ar/gragatve/GraGatve](../gragatve/GraGatve.md) | `4` | `open` | — | Gatvės kodas Registre | — |
| `x_koord` | `number` | `m` | `4` | `open` | — | Adreso taško Y koordinatė LKS-94 koordinačių sistemoje | — |
| `y_koord` | `number` | `m` | `4` | `open` | — | Adreso taško X koordinatė LKS-94 koordinačių sistemoje | — |
| `lks` | `geometry(point, 3346)` | — | — | — | — | — | — |
| `aob_r` | `date` | `D` | `4` | `open` | — | Adreso taško įvedimo į Adresų registrą data | — |
| `aob_rk` | `date` | `D` | `4` | `open` | — | Adreso taško pakeitimo registre data | — |
| `aob_atr_ko` | `date` | `D` | `4` | `open` | — | Adreso taško geometrinių charakteristikų pakeitimo data | — |
| `pasto_koda` | `string` | — | `4` | `open` | — | Pašto kodas | — |
| `n_koord` | `number` | `m` | `4` | `open` | — | Adreso taško platuma WGS-84 koordinačių sistemoje | — |
| `e_koord` | `number` | `m` | `4` | `open` | — | Adreso taško ilguma WGS-84 koordinačių sistemoje | — |
| `wgs` | `geometry(point, 4326)` | — | — | — | — | — | — |
| `formavimo_data` | `date` | `D` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/adresotaskas.csv

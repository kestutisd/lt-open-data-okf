---
type: Table
title: "GraGyvenamojiVietove — Adresų registro gyvenamųjų vietovių erdviniai duomenys"
description: "Gyvenamųjų vietovių erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus – gyvenamąsias vietoves apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/gragyvenamojivietove/GraGyvenamojiVietove"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/gragyvenamojivietove.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gragyvenamojivietove.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# GraGyvenamojiVietove — Adresų registro gyvenamųjų vietovių erdviniai duomenys

Gyvenamųjų vietovių erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus – gyvenamąsias vietoves apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.

- **Model:** `datasets/gov/rc/ar/gragyvenamojivietove/GraGyvenamojiVietove`[^manifest]
- **Dataset:** [Adresų registras](../gragyvenamojivietove.md) (`datasets/gov/rc/ar/gragyvenamojivietove`)
- **Manifest CSV:** [datasets/gov/rc/ar/gragyvenamojivietove.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gragyvenamojivietove.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/gragyvenamojivietove/GraGyvenamojiVietove`
- **Primary Key (`ref`):** `gyv_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gyv_kodas` | `integer` | — | `4` | `open` | — | Gyvenamosios vietovės kodas Registre (nekeičiamas gyvenamosios vietovės egzistavimo laiką) | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Gyvenamosios vietovės vardas su sutrumpintu tipu | — |
| `plotas` | `number` | `ha` | `4` | `open` | — | Gyvenamosios vietovės grafinis plotas (ha) | — |
| `gyv_r` | `date` | `D` | `4` | `open` | — | Gyvenamosios vietovės įrašymo į Adresų registrą data | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/grasavivaldybe/GraSavivaldybe](../grasavivaldybe/GraSavivaldybe.md) | `4` | `open` | — | Savivaldybės į kurią patenka gyvenamosios vietovės teritorija, išorinis kodas | — |
| `formavimo_data` | `date` | `D` | `4` | `open` | — | Duomenų formavimo data | — |
| `gyv_vietoves` | `geometry(3346)` | `m` | `4` | `open` | — | Gyvenamųjų vietovių ribos | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/gragyvenamojivietove.csv

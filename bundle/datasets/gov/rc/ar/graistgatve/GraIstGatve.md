---
type: Table
title: "GraIstGatve — Adresų registro gatvių ašinių linijų erdviniai duomenys"
description: "Gatvių ašinių linijų erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (gatvių ašinių linijas apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/graistgatve/GraIstGatve"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/graistgatve.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/graistgatve.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# GraIstGatve — Adresų registro gatvių ašinių linijų erdviniai duomenys

Gatvių ašinių linijų erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (gatvių ašinių linijas apibūdinantys duomenys).

Duomenų geografinė imtis — visa šalies teritorija.

- **Model:** `datasets/gov/rc/ar/graistgatve/GraIstGatve`[^manifest]
- **Dataset:** [Adresų registras](../graistgatve.md) (`datasets/gov/rc/ar/graistgatve`)
- **Manifest CSV:** [datasets/gov/rc/ar/graistgatve.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/graistgatve.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/graistgatve/GraIstGatve`
- **Primary Key (`ref`):** `gat_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gat_kodas` | `integer` | — | `4` | `open` | — | Istorinės (panaikintos) gatvės kodas Registre | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Sutrumpintas istorinės (panaikintos) gatvės vardas su tipu (nuolat palaikomas) | — |
| `nuo` | `date` | `D` | `4` | `open` | — | Istorinės (panaikintos) gatvės atributų rinkinio pradžios galiojimo data | — |
| `iki` | `date` | `D` | `4` | `open` | — | Istorinės (panaikintos) gatvės atributų rinkinio galiojimo pabaigos data | — |
| `gat_r` | `date` | `D` | `4` | `open` | — | Istorinės (panaikintos) gatvės ašinės linijos įvedimo į Adresų registrą data | — |
| `gat_iki` | `date` | `D` | `4` | `open` | — | Istorinės (panaikintos) gatvės ašinės linijos išregistravimo iš registro data | — |
| `gat_ilgis` | `number` | `m` | `4` | `open` | — | Istorinės (panaikintos) gatvės ilgis metrais | — |
| `gyvenamoji_vietove` | `ref` | [/datasets/gov/rc/ar/gragyvenamojivietove/GraGyvenamojiVietove](../gragyvenamojivietove/GraGyvenamojiVietove.md) | `4` | `open` | — | Gyvenamosios vietovės kodas Registre | — |
| `formavimo_data` | `date` | `D` | `4` | `open` | — | Duomenų formavimo data | — |
| `ist_gatves` | `geometry(3346)` | `m` | `4` | `open` | — | Istorinės (panaikintos) gatvės ašinė linija su pradžia, pabaiga ir posūkio taškais | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/graistgatve.csv

---
type: Table
title: "GraGatve — Adresų registro gatvių ašinių linijų erdviniai duomenys"
description: "Gatvių ašinių linijų erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (gatvių ašinių linijas apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/gragatve/GraGatve"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/gragatve.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gragatve.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# GraGatve — Adresų registro gatvių ašinių linijų erdviniai duomenys

Gatvių ašinių linijų erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (gatvių ašinių linijas apibūdinantys duomenys).

Duomenų geografinė imtis — visa šalies teritorija.

- **Model:** `datasets/gov/rc/ar/gragatve/GraGatve`[^manifest]
- **Dataset:** [Adresų registras](../gragatve.md) (`datasets/gov/rc/ar/gragatve`)
- **Manifest CSV:** [datasets/gov/rc/ar/gragatve.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gragatve.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/gragatve/GraGatve`
- **Primary Key (`ref`):** `gat_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gat_kodas` | `integer` | — | `4` | `open` | — | Gatvės kodas Registre | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Sutrumpintas gatvės vardas su tipu (nuolat palaikomas) | — |
| `gat_r` | `date` | `D` | `4` | `open` | — | Gatvės ašinės linijos įvedimo į Adresų registrą data | — |
| `gat_ilgis` | `number` | `m` | `4` | `open` | — | Gatvės ilgis metrais | — |
| `gyvenamoji_vietove` | `ref` | [/datasets/gov/rc/ar/gragyvenamojivietove/GraGyvenamojiVietove](../gragyvenamojivietove/GraGyvenamojiVietove.md) | `4` | `open` | — | Gyvenamosios vietovės, į kurią patenka gatvė, išorinis kodas | — |
| `formavimo_data` | `date` | `D` | `4` | `open` | — | Duomenų formavimo data | — |
| `gatves` | `geometry(3346)` | `m` | `4` | `open` | — | Gatvės ašinė linija su pradžia, pabaiga ir posūkio taškai | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/gragatve.csv

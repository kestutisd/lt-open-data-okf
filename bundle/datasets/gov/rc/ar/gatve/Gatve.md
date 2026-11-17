---
type: Table
title: "Gatve — Adresų registro gatvių tekstinių duomenų rinkinys"
description: "Gatvių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos gatves apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/gatve/Gatve"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/gatve.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gatve.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Gatve — Adresų registro gatvių tekstinių duomenų rinkinys

Gatvių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos gatves apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.

- **Model:** `datasets/gov/rc/ar/gatve/Gatve`[^manifest]
- **Dataset:** [Adresų registras](../gatve.md) (`datasets/gov/rc/ar/gatve`)
- **Manifest CSV:** [datasets/gov/rc/ar/gatve.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/gatve.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/gatve/Gatve`
- **Primary Key (`ref`):** `gat_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gat_kodas` | `integer` | — | `4` | `open` | — | Gatvės identifikavimo kodas | — |
| `tipas` | `string` | — | `3` | `open` | — | Gatvės tipas | — |
| `tipo_santrumpa` | `string` | — | `3` | `open` | — | Gatvės tipo trumpinys | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Gatvės pavadinimas (kilmininko linksnyje) | — |
| `gyvenamoji_vietove` | `ref` | [/datasets/gov/rc/ar/gyvenamojivietove/GyvenamojiVietove](../gyvenamojivietove/GyvenamojiVietove.md) | `4` | `open` | — | Gyvenamosios vietovės, kurioje yra gatvė, identifikavimo kodas | — |
| `nuo` | `date` | `D` | `4` | `open` | — | Atributų rinkinio pradžios galiojimo data | — |
| `gat_nuo` | `date` | `D` | `4` | `open` | — | Objekto įregistravimo data | — |
| `gat_iki` | `date` | `D` | `4` | `open` | — | Objekto išregistravimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/gatve.csv

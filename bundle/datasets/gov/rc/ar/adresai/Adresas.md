---
type: Table
title: "Adresas — Adresų registro žemės sklypams ir pastatams suteiktų adresų tekstiniai duomenys"
description: "Žemės sklypams ir pastatams suteiktų adresų tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (žemės sklypams ar pastatams suteiktus adresus apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/adresai/Adresas"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/adresai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/adresai.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Adresas — Adresų registro žemės sklypams ir pastatams suteiktų adresų tekstiniai duomenys

Žemės sklypams ir pastatams suteiktų adresų tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (žemės sklypams ar pastatams suteiktus adresus apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.

- **Model:** `datasets/gov/rc/ar/adresai/Adresas`[^manifest]
- **Dataset:** [Adresų registras](../adresai.md) (`datasets/gov/rc/ar/adresai`)
- **Manifest CSV:** [datasets/gov/rc/ar/adresai.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/adresai.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/adresai/Adresas`
- **Primary Key (`ref`):** `aob_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `tipas` | `integer` | — | `4` | `open` | — | Adreso tipas (1 -žemės sklypas, pastatas, 2 - patalpa) | — |
| `aob_kodas` | `integer` | — | `4` | `open` | — | Adreso (sklypo, statinio, patalpos) identifikavimo kodas | — |
| `aob_data_nuo` | `date` | `D` | `4` | `open` | — | Objekto įregistravimo data | — |
| `aob_data_iki` | `date` | `D` | `4` | `open` | — | Objekto išregistravimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/adresai.csv

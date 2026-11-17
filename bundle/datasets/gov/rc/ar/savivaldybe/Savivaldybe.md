---
type: Table
title: "Savivaldybe — Adresų registro savivaldybių tekstinių duomenų rinkinys"
description: "Savivaldybių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - savivaldybes apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/savivaldybe/Savivaldybe"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/savivaldybe.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/savivaldybe.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Savivaldybe — Adresų registro savivaldybių tekstinių duomenų rinkinys

Savivaldybių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - savivaldybes apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.

- **Model:** `datasets/gov/rc/ar/savivaldybe/Savivaldybe`[^manifest]
- **Dataset:** [Adresų registras](../savivaldybe.md) (`datasets/gov/rc/ar/savivaldybe`)
- **Manifest CSV:** [datasets/gov/rc/ar/savivaldybe.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/savivaldybe.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/savivaldybe/Savivaldybe`
- **Primary Key (`ref`):** `sav_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sav_kodas` | `integer` | — | `4` | `open` | — | Savivaldybės identifikavimo kodas | — |
| `tipas` | `string` | — | `3` | `open` | — | Administracinio vieneto tipas | — |
| `tipo_santrumpa` | `string` | — | `3` | `open` | — | Administracinio vieneto tipo trumpinys | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Savivaldybės pavadinimas | — |
| `apskritis` | `ref` | [/datasets/gov/rc/ar/apskritis/Apskritis](../apskritis/Apskritis.md) | `4` | `open` | — | Apskrities, kurioje yra savivaldybė, identifikavimo kodas | — |
| `sav_nuo` | `date` | `D` | `4` | `open` | — | Objekto įregistravimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/savivaldybe.csv

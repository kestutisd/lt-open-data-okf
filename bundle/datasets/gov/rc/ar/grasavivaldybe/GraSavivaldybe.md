---
type: Table
title: "GraSavivaldybe — Adresų registro savivaldybių erdviniai duomenys"
description: "Savivaldybių erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - savivaldybes apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/grasavivaldybe/GraSavivaldybe"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/grasavivaldybe.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/grasavivaldybe.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# GraSavivaldybe — Adresų registro savivaldybių erdviniai duomenys

Savivaldybių erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - savivaldybes apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.

- **Model:** `datasets/gov/rc/ar/grasavivaldybe/GraSavivaldybe`[^manifest]
- **Dataset:** [Adresų registras](../grasavivaldybe.md) (`datasets/gov/rc/ar/grasavivaldybe`)
- **Manifest CSV:** [datasets/gov/rc/ar/grasavivaldybe.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/grasavivaldybe.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/grasavivaldybe/GraSavivaldybe`
- **Primary Key (`ref`):** `sav_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pavadinimas` | `string` | — | `3` | `open` | — | Savivaldybės pavadinimas | — |
| `sav_kodas` | `integer` | — | `4` | `open` | — | Savivaldybės kodas Registre (nekeičiamas savivaldybės egzistavimo laiką) | — |
| `sav_plotas` | `number` | `ha` | `4` | `open` | — | Savivaldybės grafinis plotas (ha) | — |
| `sav_r` | `date` | `D` | `4` | `open` | — | Savivaldybės įrašymo į Adresų registrą data | — |
| `apskritis` | `ref` | [/datasets/gov/rc/ar/graapskritis/GraApskritis](../graapskritis/GraApskritis.md) | `4` | `open` | — | LR AR apskrities, į kurią patenka savivaldybės teritorija, išorinis kodas | — |
| `formavimo_data` | `date` | `D` | `4` | `open` | — | Duomenų formavimo data | — |
| `savivaldybes` | `geometry(3346)` | `m` | `4` | `open` | — | Savivaldybių ribos | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/grasavivaldybe.csv

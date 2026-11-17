---
type: Table
title: "GraApskritis — Adresų registro apskričių erdvinių duomenys"
description: "Apskričių erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - apskritis apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/graapskritis/GraApskritis"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/graapskritis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/graapskritis.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# GraApskritis — Adresų registro apskričių erdvinių duomenys

Apskričių erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - apskritis apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.

- **Model:** `datasets/gov/rc/ar/graapskritis/GraApskritis`[^manifest]
- **Dataset:** [Adresų registras](../graapskritis.md) (`datasets/gov/rc/ar/graapskritis`)
- **Manifest CSV:** [datasets/gov/rc/ar/graapskritis.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/graapskritis.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/graapskritis/GraApskritis`
- **Primary Key (`ref`):** `aps_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aps_kodas` | `integer` | — | `4` | `open` | — | Apskrities kodas Registre (nekeičiamas apskrities egzistavimo laiką) | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Apskrities pavadinimas | — |
| `aps_plotas` | `number` | `ha` | `4` | `open` | — | Apskrities grafinis plotas (ha) | — |
| `aps_r` | `date` | `D` | `4` | `open` | — | Apskrities įrašymo į Adresų registrą data | — |
| `formavimo_data` | `date` | `D` | `4` | `open` | — | Duomenų formavimo data | — |
| `apskritys` | `geometry(3346)` | — | `4` | `open` | — | Apskričių ribos | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/graapskritis.csv

---
type: Table
title: "Apskritis — Adresų registro apskričių tekstinių duomenų rinkinys"
description: "Apskričių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - apskritis apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/apskritis/Apskritis"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/apskritis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/apskritis.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# Apskritis — Adresų registro apskričių tekstinių duomenų rinkinys

Apskričių tekstinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - apskritis apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.

- **Model:** `datasets/gov/rc/ar/apskritis/Apskritis`[^manifest]
- **Dataset:** [Adresų registras](../apskritis.md) (`datasets/gov/rc/ar/apskritis`)
- **Manifest CSV:** [datasets/gov/rc/ar/apskritis.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/apskritis.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/apskritis/Apskritis`
- **Primary Key (`ref`):** `adm_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `adm_kodas` | `integer` | — | `4` | `open` | — | Apskrities identifikavimo kodas | — |
| `tipas` | `string` | — | `3` | `open` | — | Administracinio vieneto tipas | — |
| `santrumpa` | `string` | — | `3` | `open` | — | Administracinio vieneto tipo santrumpa | — |
| `pavadinimas` | `string` | — | `3` | `open` | — | Apskrities pavadinimas | — |
| `adm_nuo` | `date` | `D` | `4` | `open` | — | Objekto įregistravimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/apskritis.csv

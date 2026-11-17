---
type: Table
title: "GraSeniunija — Adresų registro seniūnijų erdviniai duomenys"
description: "Seniūnijų erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - seniūnijas apibūdinantys duomenys)."
resource: "https://get.data.gov.lt/datasets/gov/rc/ar/graseniunija/GraSeniunija"
tags: [gov, rc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rc/ar/graseniunija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/graseniunija.csv#L3"
    last_modified: "2026-11-11T14:39:20Z"
---

# GraSeniunija — Adresų registro seniūnijų erdviniai duomenys

Seniūnijų erdvinių duomenų rinkinys iš Lietuvos Respublikos adresų registro (Lietuvos Respublikos administracinius vienetus - seniūnijas apibūdinantys duomenys). Duomenų geografinė imtis — visa šalies teritorija.

- **Model:** `datasets/gov/rc/ar/graseniunija/GraSeniunija`[^manifest]
- **Dataset:** [Adresų registras](../graseniunija.md) (`datasets/gov/rc/ar/graseniunija`)
- **Manifest CSV:** [datasets/gov/rc/ar/graseniunija.csv#L3](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rc/ar/graseniunija.csv#L3)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rc/ar/graseniunija/GraSeniunija`
- **Primary Key (`ref`):** `sen_kodas`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pavadinimas` | `string` | — | `3` | `open` | — | Seniūnijos pavadinimas | — |
| `sen_kodas` | `integer` | — | `4` | `open` | — | Seniūnijos kodas Registre (nekeičiamas savivaldybės egzistavimo laiką) | — |
| `sen_plotas` | `number` | `ha` | `4` | `open` | — | Seniūnijos grafinis plotas (ha) | — |
| `sen_r` | `date` | `D` | `4` | `open` | — | Seniūnijos įrašymo į Adresų registrą data | — |
| `savivaldybe` | `ref` | [/datasets/gov/rc/ar/grasavivaldybe/GraSavivaldybe](../grasavivaldybe/GraSavivaldybe.md) | `4` | `open` | — | LR AR savivaldybės į kurią patenka seniūnijos teritorija, išorinis kodas | — |
| `formavimo_data` | `date` | `D` | `4` | `open` | — | Duomenų formavimo data | — |
| `seniunijos` | `geometry(3346)` | `m` | `4` | `open` | — | Seniūnijų ribos | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rc/ar/graseniunija.csv

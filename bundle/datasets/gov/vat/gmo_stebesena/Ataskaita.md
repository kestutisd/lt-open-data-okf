---
type: Table
title: "Ataskaita — Pateikiama informacija apie ūkio subjekto vardą, pavardę, augalo rūšį, veislę, mainams skirtos sėklos kiekį, g"
description: "Spinta table datasets/gov/vat/gmo_stebesena/Ataskaita (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vat/gmo_stebesena/Ataskaita"
tags: [gov, vat, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vat/gmo_stebesena.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/gmo_stebesena.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Ataskaita — Pateikiama informacija apie ūkio subjekto vardą, pavardę, augalo rūšį, veislę, mainams skirtos sėklos kiekį, g

- **Model:** `datasets/gov/vat/gmo_stebesena/Ataskaita`[^manifest]
- **Dataset:** [datasets/gov/vat/gmo_stebesena](../gmo_stebesena.md) (`datasets/gov/vat/gmo_stebesena`)
- **Manifest CSV:** [datasets/gov/vat/gmo_stebesena.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vat/gmo_stebesena.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vat/gmo_stebesena/Ataskaita`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Įrašo identifikatorius | — |
| `tipas` | `string` | — | `4` | `open` | — | Mėginio tyrimo rezultatas | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybė, kurioje paimtas mėginys | — |
| `rusis` | `string` | — | `3` | `open` | — | Pasėlių kultūra | — |
| `kilmes_salis` | `string` | — | `3` | `open` | — | Kilmės šalis | — |
| `padalinys` | `string` | — | `4` | `open` | — | Mėginį paėmęs teritorinis padalinys | — |
| `registracija` | `date` | `D` | `4` | `open` | — | Mėginio paėmimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `tipas` | `"PASELIS"` | — | — | Pasėlis | — |
| `tipas` | `"SIUNTA"` | — | — | Siunta | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vat/gmo_stebesena.csv

---
type: Table
title: "Sarasas — Institucijos, teikiančios informaciją Virtualiai elektroninio paveldo sistemai (VEPIS)"
description: "Spinta table datasets/gov/lnb/epaveldas_institucijos/Sarasas (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lnb/epaveldas_institucijos/Sarasas"
tags: [gov, lnb, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lnb/epaveldas_institucijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/epaveldas_institucijos.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sarasas — Institucijos, teikiančios informaciją Virtualiai elektroninio paveldo sistemai (VEPIS)

- **Model:** `datasets/gov/lnb/epaveldas_institucijos/Sarasas`[^manifest]
- **Dataset:** [Institucijos, teikiančios informaciją Virtualiai elektroninio paveldo sistemai (VEPIS)](../epaveldas_institucijos.md) (`datasets/gov/lnb/epaveldas_institucijos`)
- **Manifest CSV:** [datasets/gov/lnb/epaveldas_institucijos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/epaveldas_institucijos.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lnb/epaveldas_institucijos/Sarasas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `pavadinimas_lt` | `string` | — | `4` | `open` | — | Institucijos pavadinimas lietuvių kalba | — |
| `pavadinimas_en` | `string` | — | `4` | `open` | — | Institucijos pavadinimas anglų kalba | — |
| `trumpinys` | `string` | — | `4` | `open` | — | Institucijos pavadinimo trumpinys | — |
| `ist_tipas` | `string` | — | `4` | `open` | — | Įstaigos tipas | — |
| `tipas` | `string` | — | `4` | `open` | — | Tipas | — |
| `url` | `url` | — | `4` | `open` | — | Nuoroda į institucijos svetainę | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybė | — |
| `adresas` | `string` | — | `4` | `open` | — | Institucijos adresas | — |
| `koord` | `geometry(4326)` | — | `4` | `open` | — | Koordinate wgs 84 formatu | — |
| `sukurta` | `date` | `D` | `4` | `open` | — | Įrašo apie instituciją sūkurimo data | — |
| `atnaujinta` | `date` | `D` | `4` | `open` | — | Data, kada paskutinį kartą atnaujinta informacija | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ist_tipas` | `"Biudžetinė įstaiga"` | — | — | Biudžetinė įstaiga | — |
| `ist_tipas` | `"Viešoji įstaiga"` | — | — | Viešoji įstaiga | — |
| `ist_tipas` | `"Valstybės įmonė"` | — | — | Valstybės įmonė | — |
| `ist_tipas` | `"Asociacija"` | — | — | Asociacija | — |
| `ist_tipas` | `"Kita"` | — | — | Kita | — |
| `ist_tipas` | `"Visuomeninė organizacija"` | — | — | Visuomeninė organizacija | — |
| `tipas` | `"Muziejus"` | — | — | Muziejus | — |
| `tipas` | `"Biblioteka"` | — | — | Biblioteka | — |
| `tipas` | `"Archyvas"` | — | — | Archyvas | — |
| `tipas` | `"Valstybės institucija"` | — | — | Valstybės institucija | — |
| `tipas` | `"Institutas"` | — | — | Institutas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lnb/epaveldas_institucijos.csv

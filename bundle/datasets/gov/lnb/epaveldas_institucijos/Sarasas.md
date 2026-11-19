---
type: Table
title: "Sarasas — Institucijos, teikiančios informaciją Virtualiai elektroninio paveldo sistemai (VEPIS)"
description: "Spinta table datasets/gov/lnb/epaveldas_institucijos/Sarasas (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lnb/epaveldas_institucijos/Sarasas"
tags: [gov, lnb, sarasas, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/epaveldas_institucijos.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/lnb/epaveldas_institucijos.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2627/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lnb/epaveldas_institucijos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sarasas — Institucijos, teikiančios informaciją Virtualiai elektroninio paveldo sistemai (VEPIS)

- **Model:** `datasets/gov/lnb/epaveldas_institucijos/Sarasas`[^manifest]
- **Dataset:** [Institucijos, teikiančios informaciją Virtualiai elektroninio paveldo sistemai (VEPIS)](../epaveldas_institucijos.md) (`datasets/gov/lnb/epaveldas_institucijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lnb/epaveldas_institucijos.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/epaveldas_institucijos.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lnb/epaveldas_institucijos/Sarasas` (`deployed`)[^manifest]
- **Provider:** `lnb` — Lietuvos nacionalinė Martyno Mažvydo biblioteka *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by-nc/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/lnb/epaveldas_institucijos.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lnb/epaveldas_institucijos.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lnb/epaveldas_institucijos (https://data.gov.lt/datasets/2627/)

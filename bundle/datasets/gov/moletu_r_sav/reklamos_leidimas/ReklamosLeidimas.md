---
type: Table
title: "ReklamosLeidimas — Rinkinyje pateikiami Molėtų savivaldybės geografinėje informacinėje sistemoje (GIS) nuo 2017 metų galiojantys reklamų leidimai. Duomenų rinkinį sudaro: įmonės ar fizinio asmens..."
description: "Spinta table datasets/gov/moletu_r_sav/reklamos_leidimas/ReklamosLeidimas (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/moletu_r_sav/reklamos_leidimas/ReklamosLeidimas"
tags: [gov, moletu_r_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/moletu_r_sav/reklamos_leidimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/moletu_r_sav/reklamos_leidimas.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# ReklamosLeidimas — Rinkinyje pateikiami Molėtų savivaldybės geografinėje informacinėje sistemoje (GIS) nuo 2017 metų galiojantys reklamų leidimai. Duomenų rinkinį sudaro: įmonės ar fizinio asmens...

- **Model:** `datasets/gov/moletu_r_sav/reklamos_leidimas/ReklamosLeidimas`[^manifest]
- **Dataset:** [Reklamos leidimų duomenų rinkinys](../reklamos_leidimas.md) (`datasets/gov/moletu_r_sav/reklamos_leidimas`)
- **Manifest CSV:** [datasets/gov/moletu_r_sav/reklamos_leidimas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/moletu_r_sav/reklamos_leidimas.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/moletu_r_sav/reklamos_leidimas/ReklamosLeidimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus įrašo identifikatorius | — |
| `leidimo_nr` | `string` | — | `4` | `open` | — | Leidimo numeris | — |
| `isdavimo_data` | `date` | — | `4` | `open` | — | Išdavimo data | — |
| `galioja_nuo` | `date` | — | `4` | `open` | — | Galiojimo pradžia | — |
| `galioja_iki` | `date` | — | `4` | `open` | — | Galiojimo pabaiga | — |
| `imone` | `string` | — | `4` | `open` | — | Įmonės pavadinimas | — |
| `imones_k` | `string` | — | `4` | `open` | — | Įmonės kodas | — |
| `irenginio_id` | `string` | — | `4` | `open` | — | Įrenginio ID | — |
| `reklamos_plotas` | `number` | — | `4` | `open` | — | Reklamos ploto dydis | — |
| `reklamos_tipas` | `string` | — | `4` | `open` | — | Reklamos tipas | — |
| `reklamos_adresas` | `string` | — | `4` | `open` | — | Reklamos adresas | — |
| `geometrija` | `geometry(point,3346)` | — | `4` | `open` | — | Geografinė vieta (LKS-94) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/moletu_r_sav/reklamos_leidimas.csv

---
type: Table
title: "ReklamosLeidimas — Rinkinyje pateikiami Molėtų savivaldybės geografinėje informacinėje sistemoje (GIS) nuo 2017 metų galiojantys reklamų leidimai. Duomenų rinkinį sudaro: įmonės ar fizinio asmens identifikatorius, įrenginio informacija..."
description: "Spinta table datasets/gov/moletu_r_sav/reklamos_leidimas/ReklamosLeidimas (12 columns)."
resource: "https://get.data.gov.lt/datasets/gov/moletu_r_sav/reklamos_leidimas/ReklamosLeidimas"
tags: [gov, moletu_r_sav, reklamosleidimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/moletu_r_sav/reklamos_leidimas.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/moletu_r_sav/reklamos_leidimas.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3811/"
    title: "data.gov.lt DCAT-AP — datasets/gov/moletu_r_sav/reklamos_leidimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# ReklamosLeidimas — Rinkinyje pateikiami Molėtų savivaldybės geografinėje informacinėje sistemoje (GIS) nuo 2017 metų galiojantys reklamų...

- **Model:** `datasets/gov/moletu_r_sav/reklamos_leidimas/ReklamosLeidimas`[^manifest]
- **Dataset:** [Reklamos leidimų duomenų rinkinys](../reklamos_leidimas.md) (`datasets/gov/moletu_r_sav/reklamos_leidimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/moletu_r_sav/reklamos_leidimas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/moletu_r_sav/reklamos_leidimas.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/moletu_r_sav/reklamos_leidimas/ReklamosLeidimas` (`deployed`)[^manifest]
- **Provider:** `moletu_r_sav` — Molėtų rajono savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/moletu_r_sav/reklamos_leidimas.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/moletu_r_sav/reklamos_leidimas.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/moletu_r_sav/reklamos_leidimas (https://data.gov.lt/datasets/3811/)

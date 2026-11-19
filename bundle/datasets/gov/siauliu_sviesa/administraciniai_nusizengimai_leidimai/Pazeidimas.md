---
type: Table
title: "Pazeidimas — Užfiksuoti pažeidimai už automobilių stovėjimą neleistinose vietose Šiaulių mieste"
description: "Informacija apie užfiksuotus pažeidimai už automobilių stovėjimą neleistinose vietose Šiaulių mieste"
resource: "https://get.data.gov.lt/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai/Pazeidimas"
tags: [gov, siauliu_sviesa, pazeidimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4037/"
    title: "data.gov.lt DCAT-AP — datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Pazeidimas — Užfiksuoti pažeidimai už automobilių stovėjimą neleistinose vietose Šiaulių mieste

Informacija apie užfiksuotus pažeidimai už automobilių stovėjimą neleistinose vietose Šiaulių mieste[^manifest]

- **Model:** `datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai/Pazeidimas`[^manifest]
- **Dataset:** [Išduoti automobilių stovėjimo leidimai ir užfiksuoti pažeidimai Šiaulių mieste](../administraciniai_nusizengimai_leidimai.md) (`datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai/Pazeidimas` (`deployed`)[^manifest]
- **Provider:** `siauliu_sviesa` — UAB Šiaulių šviesa *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `pazeidimo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pazeidimo_id` | `string` | — | `4` | `open` | — | Pažeidimo identifikatorius | — |
| `pazeidimo_data` | `date` | `D` | `4` | `open` | — | Pažeidimo nustatymo data | — |
| `vda_pazeidimo_vietos_koordinates` | `geometry(point, 4326)` | — | `4` | `open` | — | VDA nustatytos pažeidimo vietos koordinatės | — |
| `vda_koordinates_balai` | `number` | — | `4` | `open` | — | VDA nustatytų koordinačių tikslumas balais | — |
| `valstybinis_numeris` | `string` | — | `4` | `open` | — | Šifruotas automobilio valstybinis numeris | — |
| `vda_valstybinio_numerio_struktura` | `string` | — | `4` | `open` | — | Automobilio valstybinio numerio struktūra | — |
| `uzfiksuotas_pazeidimas` | `string` | — | `4` | `open` | — | Užfiksuotas pažeidimas | — |
| `parkavimo_zona` | `string` | — | `4` | `open` | — | Parkavimo zona kurioje nustatytas pažeidimas | — |
| `ar_sumoketa_rinkliava` | `boolean` | — | `4` | `open` | — | Požymis ar sumokėta rinkliava už pažeidimą | — |
| `ar_perduota_ank_teisenai` | `boolean` | — | `4` | `open` | — | Požymis ar informacija apie pažeidimą perduota ANK teisenai | — |
| `ar_pazeidimas_negalioja` | `boolean` | — | `4` | `open` | — | Požymis ar pažeidimo galiojimas panaikintas | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai (https://data.gov.lt/datasets/4037/)

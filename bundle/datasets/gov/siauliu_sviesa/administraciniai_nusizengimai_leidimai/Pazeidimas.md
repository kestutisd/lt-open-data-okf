---
type: Table
title: "Pazeidimas — Užfiksuoti pažeidimai už automobilių stovėjimą neleistinose vietose Šiaulių mieste"
description: "Informacija apie užfiksuotus pažeidimai už automobilių stovėjimą neleistinose vietose Šiaulių mieste"
resource: "https://get.data.gov.lt/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai/Pazeidimas"
tags: [gov, siauliu_sviesa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pazeidimas — Užfiksuoti pažeidimai už automobilių stovėjimą neleistinose vietose Šiaulių mieste

Informacija apie užfiksuotus pažeidimai už automobilių stovėjimą neleistinose vietose Šiaulių mieste

- **Model:** `datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai/Pazeidimas`[^manifest]
- **Dataset:** [Išduoti automobilių stovėjimo leidimai ir užfiksuoti pažeidimai Šiaulių mieste](../administraciniai_nusizengimai_leidimai.md) (`datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai`)
- **Manifest CSV:** [datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai/Pazeidimas`
- **Primary Key (`ref`):** `pazeidimo_id`
- **Level:** `4`

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

[^manifest]: atviriduomenys/manifest — datasets/gov/siauliu_sviesa/administraciniai_nusizengimai_leidimai.csv

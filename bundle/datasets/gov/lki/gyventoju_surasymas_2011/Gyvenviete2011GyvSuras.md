---
type: Table
title: "Gyvenviete2011GyvSuras — Gyvenviečių 2011 m. gyventojų surašymo rodikliai"
description: "Lentelėje pateikiami gyvenviečių erdviniai objektai ir su jais susieti 2011 m. gyventojų surašymo sociodemografiniai rodikliai."
resource: "https://get.data.gov.lt/datasets/gov/lki/gyventoju_surasymas_2011/Gyvenviete2011GyvSuras"
tags: [gov, lki, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lki/gyventoju_surasymas_2011.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/gyventoju_surasymas_2011.csv#L92"
    last_modified: "2026-11-11T14:39:20Z"
---

# Gyvenviete2011GyvSuras — Gyvenviečių 2011 m. gyventojų surašymo rodikliai

Lentelėje pateikiami gyvenviečių erdviniai objektai ir su jais susieti 2011 m. gyventojų surašymo sociodemografiniai rodikliai.

- **Model:** `datasets/gov/lki/gyventoju_surasymas_2011/Gyvenviete2011GyvSuras`[^manifest]
- **Dataset:** [datasets/gov/lki/gyventoju_surasymas_2011](../gyventoju_surasymas_2011.md) (`datasets/gov/lki/gyventoju_surasymas_2011`)
- **Manifest CSV:** [datasets/gov/lki/gyventoju_surasymas_2011.csv#L92](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lki/gyventoju_surasymas_2011.csv#L92)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lki/gyventoju_surasymas_2011/Gyvenviete2011GyvSuras`
- **Primary Key (`ref`):** `feature_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `feature_id` | `integer` | — | `4` | `open` | — | Erdvinio objekto identifikatorius | — |
| `feature_type` | `string` | — | `4` | `open` | — | Erdvinio objekto tipas | — |
| `geometry_type` | `string` | — | `4` | `open` | — | Geometrijos tipas | — |
| `geometry_wkt` | `string` | — | `4` | `open` | — | Geometrija WKT formatu | — |
| `geometry_geojson` | `string` | — | `4` | `open` | — | Geometrija GeoJSON formatu | — |
| `fid` | `integer` | — | `4` | `open` | — | Pirminio sluoksnio įrašo identifikatorius | — |
| `gyv_kodas` | `integer` | — | `4` | `open` | — | Gyvenvietės kodas | — |
| `gyv_pav` | `string` | — | `4` | `open` | — | Gyvenvietės pavadinimas | — |
| `gyv_r` | `string` | — | `4` | `open` | — | Gyvenvietės rūšis arba tipas | — |
| `objectid` | `integer` | — | `4` | `open` | — | Pirminio šaltinio objekto identifikatorius | — |
| `plotas` | `number` | — | `4` | `open` | — | Gyvenvietės plotas | — |
| `sav_kodas` | `string` | — | `4` | `open` | — | Savivaldybės kodas | — |
| `shape_area` | `number` | — | `4` | `open` | — | Objekto plotas | — |
| `shape_length` | `number` | — | `4` | `open` | — | Objekto perimetras arba geometrijos ilgis | — |
| `aktyvumo_stat_bedarbis` | `integer` | — | `4` | `open` | — | Bedarbių gyventojų skaičius | — |
| `aktyvumo_stat_neaktyvus` | `integer` | — | `4` | `open` | — | Ekonomiškai neaktyvių gyventojų skaičius | — |
| `amzius_0_14` | `integer` | — | `4` | `open` | — | 0–14 metų amžiaus gyventojų skaičius | — |
| `amzius_0_29_ir_60_plius_santykis` | `string` | — | `4` | `open` | — | 0–29 metų ir 60 metų bei vyresnių gyventojų santykis | — |
| `amzius_0_29_proc` | `number` | — | `4` | `open` | — | 0–29 metų amžiaus gyventojų dalis procentais | — |
| `amzius_15_29` | `integer` | — | `4` | `open` | — | 15–29 metų amžiaus gyventojų skaičius | — |
| `amzius_30_44` | `integer` | — | `4` | `open` | — | 30–44 metų amžiaus gyventojų skaičius | — |
| `amzius_45_59` | `integer` | — | `4` | `open` | — | 45–59 metų amžiaus gyventojų skaičius | — |
| `amzius_60_74` | `integer` | — | `4` | `open` | — | 60–74 metų amžiaus gyventojų skaičius | — |
| `amzius_60_plius_proc` | `number` | — | `4` | `open` | — | 60 metų ir vyresnių gyventojų dalis procentais | — |
| `amzius_75_plius` | `integer` | — | `4` | `open` | — | 75 metų ir vyresnių gyventojų skaičius | — |
| `aktyvumo_stat_uzimtas` | `integer` | — | `4` | `open` | — | Užimtų gyventojų skaičius | — |
| `bedarbyste_proc` | `number` | — | `4` | `open` | — | Bedarbystės lygis procentais | — |
| `gimimo_valstybe_kt` | `integer` | — | `4` | `open` | — | Už Lietuvos ribų gimusių gyventojų skaičius | — |
| `gimimo_valstybe_lt` | `integer` | — | `4` | `open` | — | Lietuvoje gimusių gyventojų skaičius | — |
| `gimtoji_kalba_kt` | `integer` | — | `4` | `open` | — | Gyventojų, kurių gimtoji kalba yra ne lietuvių, skaičius | — |
| `gimtoji_kalba_lt` | `integer` | — | `4` | `open` | — | Gyventojų, kurių gimtoji kalba yra lietuvių, skaičius | — |
| `gimtoji_kalba_lt_proc` | `number` | — | `4` | `open` | — | Gyventojų, kurių gimtoji kalba yra lietuvių, dalis procentais | — |
| `gimtoji_kalba_sl` | `integer` | — | `4` | `open` | — | Šaltinio kategorijos „sl“ gimtosios kalbos grupės gyventojų skaičius | — |
| `gimtoji_kalba_tautybe_lt_santykis` | `number` | — | `4` | `open` | — | Lietuvių gimtosios kalbos ir lietuvių tautybės rodiklių santykis | — |
| `gyv_sk` | `integer` | — | `4` | `open` | — | Gyventojų skaičius | — |
| `issilavinimas_aukstasis` | `integer` | — | `4` | `open` | — | Aukštąjį išsilavinimą turinčių gyventojų skaičius | — |
| `issilavinimas_aukstasis_proc` | `number` | — | `4` | `open` | — | Aukštąjį išsilavinimą turinčių gyventojų dalis procentais | — |
| `lytis_mot` | `integer` | — | `4` | `open` | — | Moterų skaičius | — |
| `lytis_vyr` | `integer` | — | `4` | `open` | — | Vyrų skaičius | — |
| `pilietybe_kt` | `integer` | — | `4` | `open` | — | Kitos nei Lietuvos pilietybės gyventojų skaičius | — |
| `pilietybe_lt` | `integer` | — | `4` | `open` | — | Lietuvos pilietybę turinčių gyventojų skaičius | — |
| `pilietybe_sl` | `integer` | — | `4` | `open` | — | Šaltinio kategorijos „sl“ pilietybės grupės gyventojų skaičius | — |
| `tautybe_kt` | `integer` | — | `4` | `open` | — | Kitos nei lietuvių tautybės gyventojų skaičius | — |
| `tautybe_lt` | `integer` | — | `4` | `open` | — | Lietuvių tautybės gyventojų skaičius | — |
| `tautybe_lt_proc` | `number` | — | `4` | `open` | — | Lietuvių tautybės gyventojų dalis procentais | — |
| `tautybe_sl` | `integer` | — | `4` | `open` | — | Šaltinio kategorijos „sl“ tautybės grupės gyventojų skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lki/gyventoju_surasymas_2011.csv

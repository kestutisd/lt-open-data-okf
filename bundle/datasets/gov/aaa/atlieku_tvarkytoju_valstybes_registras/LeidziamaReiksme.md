---
type: Table
title: "LeidziamaReiksme — Leidžiamų tvarkyti atliekų kiekiai"
description: "Atliekų tvarkymo vietai TIPK/taršos leidime nustatyti leidžiamų tvarkyti atliekų kiekiai"
resource: "https://get.data.gov.lt/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/LeidziamaReiksme"
tags: [gov, aaa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# LeidziamaReiksme — Leidžiamų tvarkyti atliekų kiekiai

Atliekų tvarkymo vietai TIPK/taršos leidime nustatyti leidžiamų tvarkyti atliekų kiekiai

- **Model:** `datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/LeidziamaReiksme`[^manifest]
- **Dataset:** [Atliekų tvarkytojų valstybės registro duomenys](../atlieku_tvarkytoju_valstybes_registras.md) (`datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras`)
- **Manifest CSV:** [datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras/LeidziamaReiksme`
- **Primary Key (`ref`):** `reiksmes_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `reiksmes_id` | `string` | — | `4` | `open` | — | Atliekų tvarkymo vietai leidžiamo tvarkyti kiekio identifikatorius | — |
| `kiekis_tonomis` | `number` | — | `4` | `open` | — | Atliekų tvarkymo vietai leidžiamų tvarkyti kiekis tonomis | — |
| `leidziamo_dydzio_tipas` | `string` | — | `4` | `open` | — | TIPK / Taršos leidžiamų dydžių tipai | — |
| `ar_pavojingos_atliekos` | `boolean` | — | `4` | `open` | — | Požymis nurodantis, ar atliekos pavojingos | — |
| `technologinio_srauto_identifikatorius` | `string` | — | `4` | `open` | — | Pavojingųjų atliekų technologinio srauto identifikatorius | — |
| `technologinio_srauto_pavadinimas` | `string` | — | `4` | `open` | — | Pavojingųjų atliekų technologinio srauto pavadinimas | — |
| `leidimo_tipas` | `string` | — | `4` | `open` | — | Leidimo tipas | — |
| `leidimo_potipis` | `string` | — | `4` | `open` | — | Leidimo potipis | — |
| `atlieku_skaidymas_pagal_srautus` | `boolean` | — | `4` | `open` | — | Leidžiamų tvarkyti pavojingųjų atliekų dydžių skaidymas pagal srautus | — |
| `leidziamo_atlieku_kiekio_leidimo_numeris` | `string` | — | `4` | `open` | — | Leidžiamą atliekų kiekį nustatančio leidimo numeris | — |
| `leidziamas_kiekis_nuo` | `date` | `D` | `4` | `open` | — | Leidime nurodytas kiekis galioja nuo | — |
| `leidziamas_kiekis_iki` | `date` | `D` | `4` | `open` | — | Leidime nurodytas kiekis galioja iki | — |
| `tvarkytojo_kodas_atvr_sistemoje` | `string` | — | `4` | `open` | — | Tvarkytojo kodas ATVR sistemoje | — |
| `tvarkytojo_juridinio_asmens_kodas` | `string` | — | `4` | `open` | — | Atliekų tvarkytojo juridinio asmens kodas | — |
| `tvarkytojo_pavadinimas` | `string` | — | `4` | `open` | — | Tvarkytojo pavadinimas | — |
| `tvarkytojo_isregistravimo_data` | `date` | `D` | `4` | `open` | — | Tvarkytojo išregistravimo data | — |
| `tvarkytojo_adresas` | `string` | — | `4` | `open` | — | Tvarkytojo adresas | — |
| `tvarkymo_vietos_numeris_atvr_sistemoje` | `string` | — | `4` | `open` | — | Tvarkymo vietos numeris ATVR | — |
| `tvarkymo_vietos_pavadinimas` | `string` | — | `4` | `open` | — | Tvarkymo vietos pavadinimas | — |
| `tvarkymo_vietos_isregistravimo_data` | `date` | `D` | `4` | `open` | — | Tvarkymo vietos išregistravimo data | — |
| `tvarkymo_vietos_busena` | `string` | — | `4` | `open` | — | Tvarkymo vietos būsena | — |
| `tvarkymo_vietos_adresas` | `string` | — | `4` | `open` | — | Tvarkymo vietos adresas, sugeneruotas VDA pagal GPAIS duomenis | — |
| `tvarkymo_vietos_koordinates_lks` | `string` | — | `4` | `open` | — | Tvarkymo vietos koordinatės lks sistemoje | — |
| `tvarkymo_vietos_tikslumas_balais` | `number` | — | `4` | `open` | — | Tvarkymo vietos tikslumas balais | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `leidimo_tipas` | `"Leidimas"` | — | — | — | — |
| `leidimo_tipas` | `"Licencija"` | — | — | — | — |
| `leidimo_potipis` | `"TIPK"` | — | — | — | — |
| `leidimo_potipis` | `"Taršos leidimas"` | — | — | — | — |
| `leidimo_potipis` | `"Surinkimas"` | — | — | — | — |
| `leidimo_potipis` | `"Vežimas"` | — | — | — | — |
| `leidimo_potipis` | `"Surinkimas ir vežimas"` | — | — | — | — |
| `tvarkymo_vietos_busena` | `"Patvirtinta"` | — | — | — | — |
| `tvarkymo_vietos_busena` | `"Išregistruota"` | — | — | — | — |
| `tvarkymo_vietos_busena` | `"Tikslinama"` | — | — | — | — |
| `tvarkymo_vietos_busena` | `"Išregistruojama"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/atlieku_tvarkytoju_valstybes_registras.csv

---
type: Table
title: "VietovardisTaskas — Sluoksnyje saugoma informacija apie pagrindinius ir pakartotinius vietovių ir kraštovaizdžio objektų pavadinimus ir jų vietas, kai nėra nustatoma konkreti objekto vieta"
description: "Spinta table datasets/gov/giscentras/grpk/VietovardisTaskas (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/giscentras/grpk/VietovardisTaskas"
tags: [gov, giscentras, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L261"
    last_modified: "2026-11-11T14:39:20Z"
---

# VietovardisTaskas — Sluoksnyje saugoma informacija apie pagrindinius ir pakartotinius vietovių ir kraštovaizdžio objektų pavadinimus ir jų vietas, kai nėra nustatoma konkreti objekto vieta

- **Model:** `datasets/gov/giscentras/grpk/VietovardisTaskas`[^manifest]
- **Dataset:** [Georeferencinio pagrindo kadastro erdviniai duomenys](../grpk.md) (`datasets/gov/giscentras/grpk`)
- **Manifest CSV:** [datasets/gov/giscentras/grpk.csv#L261](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L261)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/giscentras/grpk/VietovardisTaskas`
- **Primary Key (`ref`):** `top_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `top_id` | `string` | — | `4` | `open` | — | Objekto identifikavimo kodas (reikšmė yra privaloma) | — |
| `gkodas` | `string` | — | `4` | `open` | — | Erdvinio objekto kodas (reikšmė yra privaloma) | — |
| `meta` | `string` | — | `4` | `open` | — | Raktas į GRPK rinkinio sluoksnio metaduomenų lenteles | — |
| `red_priezastis` | `string` | — | `4` | `open` | — | Objekto duomenų ir informacijos sukūrimo ar paskutinio pakeitimo priežastis (reikšmė yra privaloma įvedus naują ar patikslinus esamo objekto duomenis ir informaciją) | — |
| `red_saltinis` | `string` | — | `4` | `open` | — | Objekto duomenims sukurti, nustatyti ar pakeisti naudotas duomenų šaltinis. Galimos reikšmės | — |
| `suk_data` | `datetime` | `L` | `4` | `open` | — | Objekto įregistravimo (sukūrimo) data (reikšmė yra privaloma) | — |
| `red_data` | `datetime` | `L` | `4` | `open` | — | Objekto duomenų ir informacijos keitimo data (reikšmė yra privaloma patikslinus esamo objekto duomenis ir informaciją) | — |
| `vardas` | `string` | — | `4` | `open` | — | Vietovardis | — |
| `gyvsk` | `integer` | — | `4` | `open` | — | Gyventojų skaičius gyvenvietėje | — |
| `adm_tip` | `string` | — | `4` | `open` | — | Administracinio vieneto centro tipas | — |
| `obj_tip` | `string` | — | `4` | `open` | — | Vietovardžio tipas | — |
| `antr` | `string` | — | `4` | `open` | — | Pakartotinis užrašas | — |
| `shape` | `geometry(point, 3346)` | — | `4` | `open` | — | Objekto geometrijos tipas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gkodas` | `"uas1"` | — | — | Valstybės pavadinimas | — |
| `gkodas` | `"uas2"` | — | — | Apskrities pavadinimas | — |
| `gkodas` | `"uas3"` | — | — | Savivaldybės pavadinimas | — |
| `gkodas` | `"uas511"` | — | — | Miesto pavadinimas | — |
| `gkodas` | `"uas512"` | — | — | Miestelio pavadinimas | — |
| `gkodas` | `"uas52"` | — | — | Kaimo pavadinimas | — |
| `gkodas` | `"uas53"` | — | — | Miesto dalies pavadinimas | — |
| `gkodas` | `"uas54"` | — | — | Viensėdžio pavadinimas | — |
| `gkodas` | `"uas55"` | — | — | Kitos gyvenamosios vietovės pavadinimas | — |
| `gkodas` | `"unk0"` | — | — | Kraštovaizdžio objekto pavadinimas | — |
| `gkodas` | `"uur14"` | — | — | Miesto parko, miško parko pavadinimas | — |
| `gkodas` | `"uvp1"` | — | — | Kapinių pavadinimas | — |
| `adm_tip` | `"SOST"` | — | — | sostinė | — |
| `adm_tip` | `"APSK"` | — | — | apskrities centras | — |
| `adm_tip` | `"SAV"` | — | — | savivaldybės centras | — |
| `adm_tip` | `"SEN"` | — | — | seniūnijos centras | — |
| `obj_tip` | `"RELJ"` | — | — | reljefo elementai | — |
| `obj_tip` | `"GEOLOG"` | — | — | geologiniai objektai | — |
| `obj_tip` | `"HIDRO"` | — | — | vandens telkinių elementai | — |
| `obj_tip` | `"INFRA"` | — | — | infrastruktūros objektai | — |
| `obj_tip` | `"KRAŠT"` | — | — | kraštovaizdžio objektai | — |
| `obj_tip` | `"SPORT"` | — | — | sporto ir (ar) laisvalaikio objektai | — |
| `obj_tip` | `"ISTOR"` | — | — | istorinis vietovardis | — |
| `obj_tip` | `"KT"` | — | — | kiti objektai | — |
| `antr` | `"A"` | — | — | pakartotinis užrašas | — |
| `antr` | `"T"` | — | — | pakartotiniai užrašai, skirti žemėlapiui M 1:10 000 nomenklatūrinio skaitymo lapais LKS-94 parengti | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vardas` | `update(property: "vardas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv

---
type: Table
title: "Pazeidimas — Pažeidimų informacija įtariant pažeidimą"
description: "Ši lentelė pateikia informaciją apie nustatytus pažeidimus, susijusius su 2014–2021 m. Europos ekonominės erdvės ir Norvegijos finansinių mechanizmų projektų įgyvendinimu."
resource: "https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys_noris/Pazeidimas"
tags: [gov, cpva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys_noris.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_noris.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pazeidimas — Pažeidimų informacija įtariant pažeidimą

Ši lentelė pateikia informaciją apie nustatytus pažeidimus, susijusius su 2014–2021 m. Europos ekonominės erdvės ir Norvegijos finansinių mechanizmų projektų įgyvendinimu. Joje fiksuojami pažeidimų identifikaciniai numeriai, projektų kodai, pažeidimų laikotarpiai, būsenos ir komentarai, taip pat nurodoma, ar pažeidimai susiję su nusikalstama veikla, viešaisiais pirkimais ar sutarties nuostatų pažeidimu. Lentelės duomenys leidžia analizuoti pažeidimų pobūdį ir dažnumą projektų administravimo procese.

- **Model:** `datasets/gov/cpva/paramu_duomenys_noris/Pazeidimas`[^manifest]
- **Dataset:** [VšĮ Centrinės projektų valdymo agentūros 2014–2021 m. Europos ekonominės erdvės ir Norvegijos finansinių mechanizmų administravimo ir procesų automatizavimo informacinės sistemos duomenys](../paramu_duomenys_noris.md) (`datasets/gov/cpva/paramu_duomenys_noris`)
- **Manifest CSV:** [datasets/gov/cpva/paramu_duomenys_noris.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/cpva/paramu_duomenys_noris.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/cpva/paramu_duomenys_noris/Pazeidimas`
- **Primary Key (`ref`):** `pazeidimo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pazeidimo_id` | `string` | — | `4` | `open` | — | Pažeidimo identifikacinis numeris | — |
| `projekto_kodas` | `string` | — | `4` | `open` | — | Projekto numeris | — |
| `pirmines_informacijos_gavimo_data` | `date` | `D` | `4` | `open` | — | Pirminės informacijos gavimo data | — |
| `nusikalstama_veikla` | `boolean` | — | `4` | `open` | — | Nusikalstama veikla (sukčiavimas, korupcija ir t.t.) | — |
| `pazeista_programos_sutartis` | `boolean` | — | `4` | `open` | — | Pažeistos programos sutarties nuostatos | — |
| `pazeista_projekto_sutartis` | `boolean` | — | `4` | `open` | — | Pažeistos projekto įgyvendinimo sutarties nuostatos: 0-ne, 1-taip | — |
| `paziesta_viesuju_pirkimu_proc` | `boolean` | — | `4` | `open` | — | Pažeistos viešųjų pirkimų procedūros: 0-ne, 1-taip | — |
| `pazeidimas_nuo` | `date` | `D` | `4` | `open` | — | Pažeidimo laikotarpio data nuo | — |
| `pazeidimas_iki` | `date` | `D` | `4` | `open` | — | Pažeidimo laikotarpio data iki | — |
| `statusas` | `string` | — | `4` | `open` | — | Pažeidimo būsenos pavadinimas | — |
| `komentaras_lt` | `string` | — | `2` | `open` | — | Įtariamo pažeidimo nustatymo metodo komentaras | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `statusas` | `"Baigtas"` | — | — | Baigtas | — |
| `statusas` | `"Patvirtintas"` | — | — | Patvirtintas | — |
| `statusas` | `"Anuliuotas"` | — | — | Anuliuotas | — |
| `statusas` | `"Tiriamas"` | — | — | Tiriamas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `komentaras_lt` | `update(property: "komentaras_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/cpva/paramu_duomenys_noris.csv

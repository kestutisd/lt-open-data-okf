---
type: Table
title: "Pasiulymas — Inicijuoti teisės aktų projektai"
description: "Rinkinyje pateikiami duomenys apie teiktus pasiūlymus teisės aktų projektams: teisės aktus ir jų atributus."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/pasiulyti_ta/Pasiulymas"
tags: [gov, lrsk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lrsk/pasiulyti_ta.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/pasiulyti_ta.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pasiulymas — Inicijuoti teisės aktų projektai

Rinkinyje pateikiami duomenys apie teiktus pasiūlymus teisės aktų projektams: teisės aktus ir jų atributus. Jeigu pasiūlymas buvo inicijuotas Seime, nurodyti ir jį teikusių Seimo narių vardai ir pavardės.

- **Model:** `datasets/gov/lrsk/pasiulyti_ta/Pasiulymas`[^manifest]
- **Dataset:** [Inicijuoti teisės aktų projektai](../pasiulyti_ta.md) (`datasets/gov/lrsk/pasiulyti_ta`)
- **Manifest CSV:** [datasets/gov/lrsk/pasiulyti_ta.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/pasiulyti_ta.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/pasiulyti_ta/Pasiulymas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `reg_data` | `date` | `D` | `4` | `open` | — | Dokumento registracijos data | — |
| `reg_nr` | `string` | — | `4` | `open` | — | Dokumento registracijos numeris | — |
| `busena` | `string` | — | `4` | `open` | — | Dokumento būsena | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Dokumento pavadinimas (antraštė) | — |
| `nuoroda` | `string` | — | `4` | `open` | — | Nuoroda į pasiūlymą e-seimas portale | — |
| `parengusi_inst` | `string` | — | `4` | `open` | — | Dokumentą parengusių institucijų pavadinimai (rūšiavimui) | — |
| `seimo_narys` | `string` | — | `2` | `open` | — | Pasiūlymą teikusio Seimo nario(-ių) vardas(-ai) ir pavardė(-s). Žymimas, jei pasiūlymas buvo teiktas Lietuvos Respublikos Seime. | — |
| `pozymis` | `string` | — | `4` | `open` | — | Požymis, nurodantis, ar pasiūlymas Seime teiktas individualiai Seimo nario ar grupėje kelių Seimo narių. Žymimas tik, jei pasiūlymas buvo teiktas Lietuvos Respublikos Seime. | — |
| `ar_projektinis` | `boolean` | — | `4` | `open` | — | Dokumento projekto požymis ("True" – taip, "False" – ne) | — |
| `ar_teises_aktas` | `boolean` | — | `4` | `open` | — | Teisės akto požymis ("True" – taip, "False" – ne) | — |
| `ar_elektroninis` | `boolean` | — | `4` | `open` | — | Elektroninio dokumento požymis ("True" – taip, "False" – ne) | — |
| `ar_nacionalinis` | `boolean` | — | `4` | `open` | — | Požymis, ar dokumentas nacionalinis ("True" –nacionalinis, "False" – savivaldybių) | — |
| `ar_verslo_reg` | `boolean` | — | `4` | `open` | — | Verslo sąlygų reguliavimo požymis ("True" – taip, "False" – ne) | — |
| `ar_pagr_isv` | `boolean` | — | `4` | `open` | — | Pagrindinės išvados požymis ("True" – istorinis, "False" – ne) | — |
| `atv_dok_nr` | `string` | — | `4` | `open` | — | Numeris atvaizdavimui sąrašuose (registracijos numeris) | — |
| `atvaizdavimas` | `date` | `D` | `4` | `open` | — | Atvaizduojama dokumento data | — |
| `paviesinimas` | `date` | `D` | `4` | `open` | — | Teisės akto, kito dokumento paviešinimo data | — |
| `es_teises_aktas` | `integer` | — | `4` | `open` | — | Nuorodų į ES teisės aktus skaičius | — |
| `duomenu_sviezumas` | `date` | `D` | `4` | `open` | — | Valstybės duomenų agentūros paskutinė duomenų atnaujinimo data | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `busena` | `"Parengtas"` | — | — | — | — |
| `busena` | `"Paruoštas archyvuoti"` | — | — | — | — |
| `busena` | `"Įsegtas"` | — | — | — | — |
| `busena` | `"Sunaikintas (loginis trynimas)"` | — | — | — | — |
| `pozymis` | `"Grupėje"` | — | — | — | — |
| `pozymis` | `"Individualiai"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `seimo_narys` | `"update(property: ""seimo_narys[]"", type: ""array"", source: ""Seimo_narys"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/pasiulyti_ta.csv

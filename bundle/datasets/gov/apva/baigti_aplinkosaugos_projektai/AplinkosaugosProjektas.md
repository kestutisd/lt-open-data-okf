---
type: Table
title: "AplinkosaugosProjektas — Pabaigtų aplinkosaugos projektų duomenys"
description: "Lentelėje pateikti pabaigtų aplinkosaugos projektų duomenys iš Lietuvos Respublikos aplinkos ministerijos Aplinkos projektų valdymo agentūros (APVA) Statybos sutarčių įvykdymo priežiūros informacinės sistemos (SSĮP)."
resource: "https://get.data.gov.lt/datasets/gov/apva/baigti_aplinkosaugos_projektai/AplinkosaugosProjektas"
tags: [gov, apva, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/apva/baigti_aplinkosaugos_projektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/baigti_aplinkosaugos_projektai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# AplinkosaugosProjektas — Pabaigtų aplinkosaugos projektų duomenys

Lentelėje pateikti pabaigtų aplinkosaugos projektų duomenys iš Lietuvos Respublikos aplinkos ministerijos Aplinkos projektų valdymo agentūros (APVA) Statybos sutarčių įvykdymo priežiūros informacinės sistemos (SSĮP). Duomenų laiko aprėptis - nuo 2008 metų. Informacija lentelėje atnaujinama kas pusę metų.

- **Model:** `datasets/gov/apva/baigti_aplinkosaugos_projektai/AplinkosaugosProjektas`[^manifest]
- **Dataset:** [Pabaigtų aplinkosaugos projektų duomenys](../baigti_aplinkosaugos_projektai.md) (`datasets/gov/apva/baigti_aplinkosaugos_projektai`)
- **Manifest CSV:** [datasets/gov/apva/baigti_aplinkosaugos_projektai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/baigti_aplinkosaugos_projektai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/apva/baigti_aplinkosaugos_projektai/AplinkosaugosProjektas`
- **Primary Key (`ref`):** `prj_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `prj_id` | `string` | — | `4` | `open` | — | Projekto identifikacinis numeris | — |
| `prg_pavadinimas` | `string` | — | `4` | `open` | — | Programos pavadinimas | — |
| `prj_kodas` | `string` | — | `4` | `open` | — | Projekto kodas | — |
| `prj_pavadinimas` | `string` | — | `4` | `open` | — | Projekto pavadinimas | — |
| `kat_pavadinimas` | `string` | — | `4` | `open` | — | Projekto kategorijos pavadinimas | — |
| `bus_pavadinimas` | `string` | — | `4` | `open` | — | Projekto būsenos pavadinimas | — |
| `bus_eiles_nr` | `integer` | — | `4` | `open` | — | Projekto būsenos eilės numeris | — |
| `pro_busenos_data` | `date` | `D` | `4` | `open` | — | Projekto būsenos data | — |
| `prj_sukurtas` | `date` | `D` | `4` | `open` | — | Projekto sukūrimo data | — |
| `prj_pradzia` | `date` | `D` | `4` | `open` | — | Projekto pradžios data | — |
| `prj_pabaiga_monitoringo` | `date` | `D` | `4` | `open` | — | Projekto monitoringo pabaigos data | — |
| `prj_komentaras_lt` | `string` | — | `4` | `open` | — | Papildoma informacija apie projektą | — |
| `sav_kodas` | `string` | — | `4` | `open` | — | Savivaldybės, kurioje įgyvendinamas projektas, kodas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `prj_komentaras_lt` | `update(property: "prj_komentaras_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `sav_kodas` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `4` | `open` | — | — | — |
| `sav_kodas` | `update(property: "savivaldybe.sav_kodas", type: "")` | `property` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/apva/baigti_aplinkosaugos_projektai.csv

---
type: Table
title: "Byla — Lietuvoje registruoti patentai"
description: "Lentelė „Lietuvoje registruoti patentai“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/lrpr/Byla"
tags: [gov, vpb, byla, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/lr_pr.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vpb/lr_pr.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3808/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpb/lrpr"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# Byla — Lietuvoje registruoti patentai

Lentelė „Lietuvoje registruoti patentai“. Lentelę sudaro: patento ir paraiškos numeriai, išradimo pavadinimas ir referatas lietuvių ir anglų kalbomis, paraiškos gavimo, paskelbimo, patento išdavimo bei galiojimo pabaigos datos ir licencijos galiojimo pradžios bei pabaigos datos. Vienas įrašas atitinka vieną patento bylą (unikalią patento numerio reikšmę).[^manifest]

- **Model:** `datasets/gov/vpb/lrpr/Byla`[^manifest]
- **Dataset:** [Lietuvos Respublikoje registruoti patentai](../lrpr.md) (`datasets/gov/vpb/lrpr`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/lr_pr.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/lr_pr.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/lrpr/Byla` (`deployed`)[^manifest]
- **Provider:** `vpb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `patento_nr`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `patento_nr` | `string` | — | `4` | `open` | — | Patento numeris | — |
| `paraiskos_nr` | `string` | — | `4` | `open` | — | Patento paraiškos numeris | — |
| `isradimo_pav` | `string` | — | `4` | `open` | — | Patentuoto išradimo lietuviškas pavadinimas | — |
| `isradimo_pav_en` | `string` | — | `4` | `open` | — | Patentuoto išradimo angliškas pavadinimas | — |
| `isradimo_referatas_lt` | `string` | — | `4` | `open` | — | Patentuoto išradimo lietuviškas referatas | — |
| `isradimo_referatas_en` | `string` | — | `4` | `open` | — | Patentuoto išradimo angliškas referatas | — |
| `paraiskos_gavimo_data` | `date` | `D` | `4` | `open` | — | Patento paraiškos gavimo data | — |
| `paraiskos_paskelbimo_data` | `date` | `D` | `4` | `open` | — | Patento paraiškos paskelbimo data | — |
| `patento_isdavimo_data` | `date` | `D` | `4` | `open` | — | Patento išdavimo data | — |
| `patento_galiojimo_pabaigos_data` | `date` | `D` | `4` | `open` | — | Patento galiojimo pabaigos data | — |
| `licencijos_galiojimo_pradzios_data` | `date` | `D` | `4` | `open` | — | Patento licencijos galiojimo pradžios data | — |
| `licencijos_galiojimo_pabaiga` | `date` | `D` | `4` | `open` | — | Patento licencijos galiojimo pabaigos data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/lr_pr.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/lr_pr.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpb/lrpr (https://data.gov.lt/datasets/3808/)

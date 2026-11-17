---
type: Table
title: "Byla — Lietuvoje įsigaliojusių Europos patentų bylos"
description: "Lentelė „Lietuvoje įsigaliojusių Europos patentų bylos“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/espr/Byla"
tags: [gov, vpb, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vpb/es_pr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Byla — Lietuvoje įsigaliojusių Europos patentų bylos

Lentelė „Lietuvoje įsigaliojusių Europos patentų bylos“. Lentelę sudaro: patento ir paraiškos numeriai, išradimo pavadinimas lietuvių ir anglų kalbomis, paraiškos padavimo, paskelbimo, patento išdavimo paskelbimo ir patento galiojimo pabaigos data. Vienas įrašas atitinka vieną patento bylą (unikalią patento numerio reikšmę).

- **Model:** `datasets/gov/vpb/espr/Byla`[^manifest]
- **Dataset:** [Lietuvoje įsigalioję Europos patentai](../espr.md) (`datasets/gov/vpb/espr`)
- **Manifest CSV:** [datasets/gov/vpb/es_pr.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/espr/Byla`
- **Primary Key (`ref`):** `patento_numeris`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `patento_numeris` | `string` | — | `4` | `open` | — | Patento numeris | — |
| `paraiskos_numeris` | `string` | — | `4` | `open` | — | Patento paraiškos numeris | — |
| `isradimo_pav` | `string` | — | `4` | `open` | — | Išradimo lietuviškas pavadinimas | — |
| `isradimo_pav_en` | `string` | — | `4` | `open` | — | Išradimo angliškas pavadinimas | — |
| `paraiskos_padavimo_data` | `date` | `D` | `4` | `open` | — | Patento paraiškos padavimo data | — |
| `paraiskos_paskelbimo_data` | `date` | `D` | `4` | `open` | — | Patento paraiškos paskelbimo data | — |
| `patento_isdavimo_paskelbimo_data` | `date` | `D` | `4` | `open` | — | Paskelbimo apie patento išdavimą data | — |
| `patento_galiojimo_pabaigos_data` | `date` | `D` | `4` | `open` | — | Iki kada galioja patentas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/es_pr.csv

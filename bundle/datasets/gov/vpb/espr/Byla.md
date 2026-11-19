---
type: Table
title: "Byla — Lietuvoje įsigaliojusių Europos patentų bylos"
description: "Lentelė „Lietuvoje įsigaliojusių Europos patentų bylos“."
resource: "https://get.data.gov.lt/datasets/gov/vpb/espr/Byla"
tags: [gov, vpb, byla, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vpb/es_pr.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2905/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vpb/espr"
    author: "team:vda"
    last_modified: "2026-10-27T00:00:00Z"
---

# Byla — Lietuvoje įsigaliojusių Europos patentų bylos

Lentelė „Lietuvoje įsigaliojusių Europos patentų bylos“. Lentelę sudaro: patento ir paraiškos numeriai, išradimo pavadinimas lietuvių ir anglų kalbomis, paraiškos padavimo, paskelbimo, patento išdavimo paskelbimo ir patento galiojimo pabaigos data. Vienas įrašas atitinka vieną patento bylą (unikalią patento numerio reikšmę).[^manifest]

- **Model:** `datasets/gov/vpb/espr/Byla`[^manifest]
- **Dataset:** [Lietuvoje įsigalioję Europos patentai](../espr.md) (`datasets/gov/vpb/espr`)[^manifest]
- **Manifest CSV:** [datasets/gov/vpb/es_pr.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vpb/espr/Byla` (`deployed`)[^manifest]
- **Provider:** `vpb` — Valstybinis patentų biuras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `patento_numeris`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-10-27`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vpb/es_pr.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vpb/es_pr.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vpb/espr (https://data.gov.lt/datasets/2905/)

---
type: Table
title: "AplinkosaugosProjektas — Pabaigtų aplinkosaugos projektų duomenys"
description: "Lentelėje pateikti pabaigtų aplinkosaugos projektų duomenys iš Lietuvos Respublikos aplinkos ministerijos Aplinkos projektų valdymo agentūros (APVA) Statybos sutarčių įvykdymo priežiūros informacinės sistemos (SSĮP)."
resource: "https://get.data.gov.lt/datasets/gov/apva/baigti_aplinkosaugos_projektai/AplinkosaugosProjektas"
tags: [gov, apva, aplinkosaugosprojektas, deployed, level-4, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/baigti_aplinkosaugos_projektai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/apva/baigti_aplinkosaugos_projektai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2888/"
    title: "data.gov.lt DCAT-AP — datasets/gov/apva/baigti_aplinkosaugos_projektai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# AplinkosaugosProjektas — Pabaigtų aplinkosaugos projektų duomenys

Lentelėje pateikti pabaigtų aplinkosaugos projektų duomenys iš Lietuvos Respublikos aplinkos ministerijos Aplinkos projektų valdymo agentūros (APVA) Statybos sutarčių įvykdymo priežiūros informacinės sistemos (SSĮP). Duomenų laiko aprėptis - nuo 2008 metų. Informacija lentelėje atnaujinama kas pusę metų. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/apva/baigti_aplinkosaugos_projektai/AplinkosaugosProjektas`[^manifest]
- **Dataset:** [Pabaigtų aplinkosaugos projektų duomenys](../baigti_aplinkosaugos_projektai.md) (`datasets/gov/apva/baigti_aplinkosaugos_projektai`)[^manifest]
- **Manifest CSV:** [datasets/gov/apva/baigti_aplinkosaugos_projektai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/baigti_aplinkosaugos_projektai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/apva/baigti_aplinkosaugos_projektai/AplinkosaugosProjektas` (`deployed`)[^manifest]
- **Provider:** `apva` — Aplinkos projektų valdymo agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `prj_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_2`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/apva/baigti_aplinkosaugos_projektai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/baigti_aplinkosaugos_projektai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/apva/baigti_aplinkosaugos_projektai (https://data.gov.lt/datasets/2888/)

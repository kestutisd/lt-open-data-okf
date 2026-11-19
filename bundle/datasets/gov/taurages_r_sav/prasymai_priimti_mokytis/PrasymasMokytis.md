---
type: Table
title: "PrasymasMokytis — Prašymų priimti vaikus į ugdymo įstaigas Tauragėje duomenys"
description: "Lentelėje pateikti prašymų priimti vaikus į ugdymo įstaigas duomenys nuo 2022 metų iš Tauragės savivaldybės centralizuoto vaikų priėmimo sistemos (CVPS)."
resource: "https://get.data.gov.lt/datasets/gov/taurages_r_sav/prasymai_priimti_mokytis/PrasymasMokytis"
tags: [gov, taurages_r_sav, prasymasmokytis, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/taurages_r_sav/prasymai_priimti_mokytis.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/taurages_r_sav/prasymai_priimti_mokytis.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2932/"
    title: "data.gov.lt DCAT-AP — datasets/gov/taurages_r_sav/prasymai_priimti_mokytis"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# PrasymasMokytis — Prašymų priimti vaikus į ugdymo įstaigas Tauragėje duomenys

Lentelėje pateikti prašymų priimti vaikus į ugdymo įstaigas duomenys nuo 2022 metų iš Tauragės savivaldybės centralizuoto vaikų priėmimo sistemos (CVPS). Informacija lentelėje atnaujinama kas mėnesį. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/taurages_r_sav/prasymai_priimti_mokytis/PrasymasMokytis`[^manifest]
- **Dataset:** [Prašymų priimti vaikus į ugdymo įstaigas Tauragėje duomenys](../prasymai_priimti_mokytis.md) (`datasets/gov/taurages_r_sav/prasymai_priimti_mokytis`)[^manifest]
- **Manifest CSV:** [datasets/gov/taurages_r_sav/prasymai_priimti_mokytis.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/taurages_r_sav/prasymai_priimti_mokytis.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/taurages_r_sav/prasymai_priimti_mokytis/PrasymasMokytis` (`deployed`)[^manifest]
- **Provider:** `taurages_r_sav` — Tauragės rajono savivaldybė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `prasymo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `prasymo_id` | `string` | — | `4` | `open` | — | Prašymo priimti vaiką į ugdymo įstaigą identifikatorius | — |
| `prasymo_pateikimo_data` | `date` | `D` | `4` | `open` | — | Prašymo priimti vaiką į ugdymo įstaigą pateikimo data | — |
| `mokslo_metai` | `string` | — | `4` | `open` | — | Kuriems mokslo metams prašoma priimti vaiką į ugdymo įstaigą | — |
| `grupes_id` | `string` | — | `4` | `open` | — | Ugdymo grupės identifikatorius | — |
| `amzius_nuo` | `number` | — | `4` | `open` | — | Vaiko amžius (nuo kada priimama į ugdymo grupę) | — |
| `amzius_iki` | `number` | — | `4` | `open` | — | Vaiko amžius (iki kada priimama į ugdymo grupę) | — |
| `grupes_tipas` | `string` | — | `4` | `open` | — | Ugdymo grupės tipas | — |
| `inst_pavadinimas` | `string` | — | `4` | `open` | — | Prašyme nurodytos institucijos pavadinimas | — |
| `inst_adresas` | `string` | — | `4` | `open` | — | Prašyme nurodytos institucijos adresas | — |
| `pirminis_priemimas_iki` | `string` | — | `4` | `open` | — | Iki kada vykdomas pirminis priėmimas | — |
| `papildomas_priemimas_iki` | `string` | — | `4` | `open` | — | Iki kada vykdomas pakartotinis priėmimas | — |
| `prasymo_busena` | `string` | — | `4` | `open` | — | Prašymo būsena | — |
| `prasymo_busenos_data` | `date` | `D` | `4` | `open` | — | Prašymo būsenos data | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `prasymo_busena` | `"contract_signed"` | — | — | Pasirašyta sutartis | — |
| `prasymo_busena` | `"submitted"` | — | — | Prašymas pateiktas | — |
| `prasymo_busena` | `"canceled"` | — | — | Prašymas atšauktas | — |
| `prasymo_busena` | `"registered"` | — | — | Prašymas užregistruotas | — |
| `prasymo_busena` | `"contract_canceled"` | — | — | Sutartis nutraukta | — |
| `prasymo_busena` | `"approved"` | — | — | Prašymas priimtas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/taurages_r_sav/prasymai_priimti_mokytis.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/taurages_r_sav/prasymai_priimti_mokytis.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/taurages_r_sav/prasymai_priimti_mokytis (https://data.gov.lt/datasets/2932/)

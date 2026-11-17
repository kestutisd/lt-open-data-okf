---
type: Table
title: "SandelioOperacija — Muitinės sandėliuose prekėms atliekamų operacijų sąrašai"
description: "Lentelėje pateikiami Lietuvos Respublikos teritorijoje veikiančių muitinės sandėlių ir laikinojo saugojimo sandėlių ir muitinės sandėliams leistų įprastinių prekių tvarkymo operacijų sąrašai iš LR Muitinės sandėlių ir terminalų veiklos..."
resource: "https://get.data.gov.lt/datasets/gov/muitine/muitines_sandeliu_statistika/SandelioOperacija"
tags: [gov, muitine, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_sandeliu_statistika.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_sandeliu_statistika.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# SandelioOperacija — Muitinės sandėliuose prekėms atliekamų operacijų sąrašai

Lentelėje pateikiami Lietuvos Respublikos teritorijoje veikiančių muitinės sandėlių ir laikinojo saugojimo sandėlių ir muitinės sandėliams leistų įprastinių prekių tvarkymo operacijų sąrašai iš LR Muitinės sandėlių ir terminalų veiklos apskaitos ir kontrolės informacinės sistemos (MSAS). Duomenų laiko aprėptis - nuo 2006 metų. Lentelė atnaujinama kas mėnesį.

- **Model:** `datasets/gov/muitine/muitines_sandeliu_statistika/SandelioOperacija`[^manifest]
- **Dataset:** [Muitinės sandėlių, laikinojo saugojimo sandėlių bei garantų, pateikusių muitinei garantijas už šiuose sandėliuose saugomas prekes, statistika](../muitines_sandeliu_statistika.md) (`datasets/gov/muitine/muitines_sandeliu_statistika`)
- **Manifest CSV:** [datasets/gov/muitine/muitines_sandeliu_statistika.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_sandeliu_statistika.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/muitines_sandeliu_statistika/SandelioOperacija`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Duomenų eilutės identifikatorius (sugeneruotas VDA) | — |
| `opr_kodas` | `string` | — | `4` | `open` | — | Operacijos su prekėmis, kuri atliekama muitinės sandėlyje, kodas | — |
| `pavad` | `string` | — | `4` | `open` | — | Operacijos pavadinimas | — |
| `mdata` | `datetime` | `S` | `4` | `open` | — | Informacijos apie operaciją paskutinio redagavimo data ir laikas | — |
| `sand_kodas` | `string` | — | `4` | `open` | — | Muitinės sandėlio kodas | — |
| `s_mdata` | `datetime` | `S` | `4` | `open` | — | Informacijos apie muitinės sandėlį paskutinio redagavimo data ir laikas | — |
| `ar_yra_nemuit_sarase` | `boolean` | — | `4` | `open` | — | Požymis, ar operacija su prekėmis galima ir ne muitinės sandėlyje | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_sandeliu_statistika.csv

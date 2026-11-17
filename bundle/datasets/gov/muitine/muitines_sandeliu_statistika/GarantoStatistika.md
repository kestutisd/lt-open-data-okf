---
type: Table
title: "GarantoStatistika — Muitinės sandėliams suteiktų garantijų statistika"
description: "Lentelėje pateikiama informacija apima garantų, pateikusių muitinei garantijas už prekes, saugomas muitinės sandėliuose ir laikinojo saugojimo sandėliuose, ir jų pateiktų garantijų apibendrintą statistiką, įskaitant sandėlių ir..."
resource: "https://get.data.gov.lt/datasets/gov/muitine/muitines_sandeliu_statistika/GarantoStatistika"
tags: [gov, muitine, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_sandeliu_statistika.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_sandeliu_statistika.csv#L18"
    last_modified: "2026-11-11T14:39:20Z"
---

# GarantoStatistika — Muitinės sandėliams suteiktų garantijų statistika

Lentelėje pateikiama informacija apima garantų, pateikusių muitinei garantijas už prekes, saugomas muitinės sandėliuose ir laikinojo saugojimo sandėliuose, ir jų pateiktų garantijų apibendrintą statistiką, įskaitant sandėlių ir garantijų skaičių bei vidutinę garantijos vertę iš LR Muitinės sandėlių ir terminalų veiklos apskaitos ir kontrolės informacinės sistemos (MSAS). Duomenų laiko aprėptis - nuo 2005 metų. Lentelė atnaujinama kas metus.

- **Model:** `datasets/gov/muitine/muitines_sandeliu_statistika/GarantoStatistika`[^manifest]
- **Dataset:** [Muitinės sandėlių, laikinojo saugojimo sandėlių bei garantų, pateikusių muitinei garantijas už šiuose sandėliuose saugomas prekes, statistika](../muitines_sandeliu_statistika.md) (`datasets/gov/muitine/muitines_sandeliu_statistika`)
- **Manifest CSV:** [datasets/gov/muitine/muitines_sandeliu_statistika.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_sandeliu_statistika.csv#L18)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/muitines_sandeliu_statistika/GarantoStatistika`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Duomenų eilutės identifikatorius (sugeneruotas VDA) | — |
| `garantija_nuo` | `string` | — | `4` | `open` | — | Garantijų suteikimų laikotarpis | — |
| `garant_imone` | `string` | — | `4` | `open` | — | Įmonės garanto kodas | — |
| `pavad` | `string` | — | `4` | `open` | — | Įmonės garanto pavadinimas | — |
| `garant_sk` | `integer` | — | `4` | `open` | — | Unikalių garantijų skaičius | — |
| `sand_sk` | `integer` | — | `4` | `open` | — | Unikalių muitinės sandėlių skaičius | — |
| `avg_garant_verte` | `number` | — | `4` | `open` | — | Vidutinė garantijos vertė (EUR) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_sandeliu_statistika.csv

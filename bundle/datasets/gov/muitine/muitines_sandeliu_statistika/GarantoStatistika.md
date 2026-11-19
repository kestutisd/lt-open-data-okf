---
type: Table
title: "GarantoStatistika — Muitinės sandėliams suteiktų garantijų statistika"
description: "Lentelėje pateikiama informacija apima garantų, pateikusių muitinei garantijas už prekes, saugomas muitinės sandėliuose ir laikinojo saugojimo sandėliuose, ir jų pateiktų garantijų apibendrintą statistiką, įskaitant sandėlių ir garantijų skaičių bei vidutinę garantijos vertę..."
resource: "https://get.data.gov.lt/datasets/gov/muitine/muitines_sandeliu_statistika/GarantoStatistika"
tags: [gov, muitine, garantostatistika, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_sandeliu_statistika.csv#L18"
    title: "atviriduomenys/manifest — datasets/gov/muitine/muitines_sandeliu_statistika.csv#L18"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/4117/"
    title: "data.gov.lt DCAT-AP — datasets/gov/muitine/muitines_sandeliu_statistika"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# GarantoStatistika — Muitinės sandėliams suteiktų garantijų statistika

Lentelėje pateikiama informacija apima garantų, pateikusių muitinei garantijas už prekes, saugomas muitinės sandėliuose ir laikinojo saugojimo sandėliuose, ir jų pateiktų garantijų apibendrintą statistiką, įskaitant sandėlių ir garantijų skaičių bei vidutinę garantijos vertę iš LR Muitinės sandėlių ir terminalų veiklos apskaitos ir kontrolės informacinės sistemos (MSAS). Duomenų laiko aprėptis - nuo 2005 metų. Lentelė atnaujinama kas metus. Su duomenimis susijusiais klausimais prašome kreiptis el. paštu atverimas@stat.gov.lt. Dėl techninių portalo veiklos sutrikimų prašome kreiptis el. paštu atviriduomenys@vssa.lt.[^manifest]

- **Model:** `datasets/gov/muitine/muitines_sandeliu_statistika/GarantoStatistika`[^manifest]
- **Dataset:** [Muitinės sandėlių, laikinojo saugojimo sandėlių bei garantų, pateikusių muitinei garantijas už...](../muitines_sandeliu_statistika.md) (`datasets/gov/muitine/muitines_sandeliu_statistika`)[^manifest]
- **Manifest CSV:** [datasets/gov/muitine/muitines_sandeliu_statistika.csv#L18](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_sandeliu_statistika.csv#L18)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/muitine/muitines_sandeliu_statistika/GarantoStatistika` (`deployed`)[^manifest]
- **Provider:** `muitine` — Muitinės departamentas prie LR FM *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/muitine/muitines_sandeliu_statistika.csv#L18 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/muitine/muitines_sandeliu_statistika.csv#L18)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/muitine/muitines_sandeliu_statistika (https://data.gov.lt/datasets/4117/)

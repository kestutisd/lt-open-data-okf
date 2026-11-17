---
type: Table
title: "Pazymejimas — Nuo okupacijų nukentėjusių asmenų pažymėjimai"
description: "Lietuvos gyventojų genocido ir rezistencijos tyrimo centro išduoti pažymėjimai asmenims, nukentėjusiems nuo 1939-1990 okupacijų."
resource: "https://get.data.gov.lt/datasets/gov/lggrtc/Pazymejimas"
tags: [gov, lggrtc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lggrtc/nukentejusiu_pazymejimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lggrtc/nukentejusiu_pazymejimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pazymejimas — Nuo okupacijų nukentėjusių asmenų pažymėjimai

Lietuvos gyventojų genocido ir rezistencijos tyrimo centro išduoti pažymėjimai asmenims, nukentėjusiems nuo 1939-1990 okupacijų. Rinkinyje pateikiama nukentėjusiojo statusas, pažymėjimo numeris, išdavimo įsakymo data ir numeris. Teisiniai straipsniai, jo dalys, punktai ir papunkčiai. Duomenys nuo 1998m iki dabar.

- **Model:** `datasets/gov/lggrtc/Pazymejimas`[^manifest]
- **Dataset:** [Lietuvos gyventojų genocido ir rezistencijos tyrimo centras](../lggrtc.md) (`datasets/gov/lggrtc`)
- **Manifest CSV:** [datasets/gov/lggrtc/nukentejusiu_pazymejimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lggrtc/nukentejusiu_pazymejimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lggrtc/Pazymejimas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `sertifikato_id` | `string` | — | `4` | `open` | — | Pažymėjimo identifikatorius | — |
| `statuso_id` | `string` | — | `4` | `open` | — | Statuso identifikatorius | — |
| `pazymejimo_nr` | `string` | — | `4` | `open` | — | Sertifikato numeris | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Subjekto kodas | — |
| `asm_kodas_tinkamas` | `string` | — | `4` | `open` | — | Ar asmens kodas validus | — |
| `lytis_ak` | `string` | — | `4` | `open` | — | Asmens lytis iš asmens kodo | — |
| `gimimo_metai_ak` | `date` | `Y` | `4` | `open` | — | Asmens gimimo metai iš asmens kodo | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Asmens gimimo metai | — |
| `vietove` | `string` | — | `4` | `open` | — | Asmens gyvenamoji vietovė dokumentų pateikimo datai | — |
| `statusas` | `string` | — | `4` | `open` | — | Nukentėjusiojo statusas | — |
| `straipsnis` | `string` | — | `4` | `open` | — | Straipsnio aprašymas | — |
| `straipsnio_dalis` | `string` | — | `4` | `open` | — | Straipsnio dalies aprašymas | — |
| `punktas` | `string` | — | `4` | `open` | — | Straipsnio punkto aprašymas | — |
| `papunktis` | `string` | — | `4` | `open` | — | Straipsnio papunkčio aprašymas | — |
| `isakymo_data` | `date` | `M` | `4` | `open` | — | Pažymėjimo įsakymo data | — |
| `isdavimo_isakymas` | `string` | — | `4` | `open` | — | Pažymėjimo įsakymo numeris | — |
| `pazymejimo_pametimo_data` | `date` | `M` | `4` | `open` | — | Pažymėjimo pametimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lggrtc/nukentejusiu_pazymejimai.csv

---
type: Table
title: "BaigiamasisDarbas — Studijų baigiamieji darbai"
description: "Lentelėje pateikti studijų apgintų baigiamųjų darbų duomenys nuo 2001 metų iš Nacionalinės švietimo agentūros (NŠA) diplomų, atestatų ir kvalifikacijos pažymėjimų registro (DAKPR)."
resource: "https://get.data.gov.lt/datasets/gov/nsa/dakpr/baigiamieji_darbai/BaigiamasisDarbas"
tags: [gov, nsa, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/nsa/dakpr/baigiamieji_darbai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/dakpr/baigiamieji_darbai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# BaigiamasisDarbas — Studijų baigiamieji darbai

Lentelėje pateikti studijų apgintų baigiamųjų darbų duomenys nuo 2001 metų iš Nacionalinės švietimo agentūros (NŠA) diplomų, atestatų ir kvalifikacijos pažymėjimų registro (DAKPR). Duomenų atnaujinimas - mėnesinis.

- **Model:** `datasets/gov/nsa/dakpr/baigiamieji_darbai/BaigiamasisDarbas`[^manifest]
- **Dataset:** [Studijų baigiamieji darbai](../baigiamieji_darbai.md) (`datasets/gov/nsa/dakpr/baigiamieji_darbai`)
- **Manifest CSV:** [datasets/gov/nsa/dakpr/baigiamieji_darbai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/dakpr/baigiamieji_darbai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/dakpr/baigiamieji_darbai/BaigiamasisDarbas`
- **Primary Key (`ref`):** `iraso_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `iraso_id` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikatorius | — |
| `bdarbo_id` | `string` | — | `4` | `open` | — | Baigiamojo darbo identifikatorius | — |
| `bdarbo_tema` | `string` | — | `4` | `open` | — | Baigiamojo darbo tema arba pavadinimas | — |
| `prg_valst_kodas` | `string` | — | `4` | `open` | — | Mokymo programos valstybinis kodas | — |
| `prg_pavad` | `string` | — | `4` | `open` | — | Mokymo programos pavadinimas | — |
| `igyt_issilav_pav` | `string` | — | `4` | `open` | — | Įgyto išsilavinimo pavadinimas | — |
| `igyt_kvl_pav` | `string` | — | `4` | `open` | — | Įgytos kvalifikacijos pavadinimas | — |
| `bdokumento_pav` | `string` | — | `4` | `open` | — | Išsilavinimo įgijimą patvirtinančio dokumento pavadinimas | — |
| `bdokumento_isdavimo_data` | `date` | `D` | `4` | `open` | — | Išsilavinimo įgijimą patvirtinančio dokumento išdavimo data | — |
| `ins_pavad` | `string` | — | `4` | `open` | — | Išsilavinimo įgijimą patvirtinantį dokumentą išdavusios institucijos pavadinimas | — |
| `asm_id` | `string` | — | `4` | `open` | — | Baigiamojo darbo autoriaus identifikatorius | — |
| `asm_gim_metai` | `date` | `Y` | `4` | `open` | — | Baigiamojo darbo autoriaus gimimo metai | — |
| `asm_lytis` | `string` | — | `4` | `open` | — | Baigiamojo darbo autoriaus lytis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `asm_lytis` | `"V"` | — | — | Vyras | — |
| `asm_lytis` | `"M"` | — | — | Moteris | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/dakpr/baigiamieji_darbai.csv

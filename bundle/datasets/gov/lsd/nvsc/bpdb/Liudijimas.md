---
type: Table
title: "Liudijimas — Produktų liudijimai"
description: "Lentelė „Produktų liudijimai“."
resource: "https://get.data.gov.lt/datasets/gov/lsd/nvsc/bpdb/Liudijimas"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/nvsc/bpdb.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L22"
    last_modified: "2026-11-11T14:39:20Z"
---

# Liudijimas — Produktų liudijimai

Lentelė „Produktų liudijimai“. Lentelę sudaro: negrįžtamai šifruotas produkto identifikatorius, liudijimo numeris, liudijimą gavęs asmuo (liudijimo turėtojas) ir liudijimo išdavimo bei galiojimo pabaigos data. Vienas įrašas atitinka vieną produkto ir liudijimo kombinaciją.

- **Model:** `datasets/gov/lsd/nvsc/bpdb/Liudijimas`[^manifest]
- **Dataset:** [Biocidinių produktų duomenys](../bpdb.md) (`datasets/gov/lsd/nvsc/bpdb`)
- **Manifest CSV:** [datasets/gov/lsd/nvsc/bpdb.csv#L22](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L22)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/nvsc/bpdb/Liudijimas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `produkto_id` | `string` | — | `4` | `open` | — | Išorinis raktas į produktą | — |
| `liudijimo_nr` | `string` | — | `4` | `open` | — | Liudijimo numeris | — |
| `liudijima_gaves_asm` | `string` | — | `2` | `open` | — | Liudijimo turėtojas | — |
| `liudijimo_isdavimo_data` | `date` | `D` | `4` | `open` | — | Išdavimo data | — |
| `liudijimas_galioja_iki` | `date` | `D` | `4` | `open` | — | Galiojimo pabaigos data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/nvsc/bpdb.csv

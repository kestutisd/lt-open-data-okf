---
type: Table
title: "Liudijimas — Produktų liudijimai"
description: "Lentelė „Produktų liudijimai“."
resource: "https://get.data.gov.lt/datasets/gov/lsd/nvsc/bpdb/Liudijimas"
tags: [gov, lsd, liudijimas, deployed, level-4, cadence-daily]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L22"
    title: "atviriduomenys/manifest — datasets/gov/lsd/nvsc/bpdb.csv#L22"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2917/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lsd/nvsc/bpdb"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Liudijimas — Produktų liudijimai

Lentelė „Produktų liudijimai“. Lentelę sudaro: negrįžtamai šifruotas produkto identifikatorius, liudijimo numeris, liudijimą gavęs asmuo (liudijimo turėtojas) ir liudijimo išdavimo bei galiojimo pabaigos data. Vienas įrašas atitinka vieną produkto ir liudijimo kombinaciją.[^manifest]

- **Model:** `datasets/gov/lsd/nvsc/bpdb/Liudijimas`[^manifest]
- **Dataset:** [Biocidinių produktų duomenys](../bpdb.md) (`datasets/gov/lsd/nvsc/bpdb`)[^manifest]
- **Manifest CSV:** [datasets/gov/lsd/nvsc/bpdb.csv#L22](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L22)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/nvsc/bpdb/Liudijimas` (`deployed`)[^manifest]
- **Provider:** `lsd` — Valstybės duomenų agentūra (VDA, buv. Lietuvos statistikos departamentas) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `DAILY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `produkto_id` | `string` | — | `4` | `open` | — | Išorinis raktas į produktą | — |
| `liudijimo_nr` | `string` | — | `4` | `open` | — | Liudijimo numeris | — |
| `liudijima_gaves_asm` | `string` | — | `2` | `open` | — | Liudijimo turėtojas | — |
| `liudijimo_isdavimo_data` | `date` | `D` | `4` | `open` | — | Išdavimo data | — |
| `liudijimas_galioja_iki` | `date` | `D` | `4` | `open` | — | Galiojimo pabaigos data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/nvsc/bpdb.csv#L22 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/nvsc/bpdb.csv#L22)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lsd/nvsc/bpdb (https://data.gov.lt/datasets/2917/)

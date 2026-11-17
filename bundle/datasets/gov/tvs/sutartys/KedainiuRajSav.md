---
type: Table
title: "KedainiuRajSav"
description: "Spinta table datasets/gov/tvs/sutartys/KedainiuRajSav (14 columns)."
resource: "https://get.data.gov.lt/datasets/gov/tvs/sutartys/KedainiuRajSav"
tags: [gov, tvs, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/tvs/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tvs/sutartys.csv#L24"
    last_modified: "2026-11-11T14:39:20Z"
---

# KedainiuRajSav

- **Model:** `datasets/gov/tvs/sutartys/KedainiuRajSav`[^manifest]
- **Dataset:** [Duomenys apie savyvaldybės sudarytas sutartis](../sutartys.md) (`datasets/gov/tvs/sutartys`)
- **Manifest CSV:** [datasets/gov/tvs/sutartys.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/tvs/sutartys.csv#L24)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/tvs/sutartys/KedainiuRajSav`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `sutarties_salis_tipas` | `string` | — | `4` | `open` | — | Sutarties šalies tipas | — |
| `sutarties_tipas` | `string` | — | `4` | `open` | — | Sutarties tipas | — |
| `vardas_pavarde` | `string` | — | `4` | `open` | — | Vardas pavardė | — |
| `asm_kodas` | `string` | — | `4` | `open` | — | Asmens kodas | — |
| `gim_metai_asmk` | `date` | `Y` | `4` | `open` | — | Gimimo metai iš asmens kodo | — |
| `lytis_asmk` | `string` | — | `4` | `open` | — | Lytis iš asmens kodo | — |
| `istaiga` | `string` | — | `4` | `open` | — | Įstaigos pavadinimas | — |
| `jar_kodas` | `string` | — | `4` | `open` | — | JAR kodas | — |
| `bankroto_data` | `date` | `D` | `4` | `open` | — | Įstaigos bankroto data | — |
| `menesio_imokos_suma` | `number` | — | `4` | `open` | — | Mėnesio nuomos suma | — |
| `sutart_isigal_data` | `date` | `D` | `4` | `open` | — | Sutarties įsigaliojimo data | — |
| `sutart_nutrauk_data` | `date` | `D` | `4` | `open` | — | Sutarties nutraukimo data | — |
| `teisinis_pagrindas` | `string` | — | `4` | `open` | — | Teisinis sutarties pagrindas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/tvs/sutartys.csv

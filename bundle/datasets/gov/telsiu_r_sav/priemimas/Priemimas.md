---
type: Table
title: "Priemimas — Priėmimai į bendrojo ugdymo įstaigas Telšių r. savivaldybėje"
description: "Spinta table datasets/gov/telsiu_r_sav/priemimas/Priemimas (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/telsiu_r_sav/priemimas/Priemimas"
tags: [gov, telsiu_r_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/telsiu_r_sav/priemimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/telsiu_r_sav/priemimai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Priemimas — Priėmimai į bendrojo ugdymo įstaigas Telšių r. savivaldybėje

- **Model:** `datasets/gov/telsiu_r_sav/priemimas/Priemimas`[^manifest]
- **Dataset:** [Priėmimai į bendrojo ugdymo įstaigas Telšių r. savivaldybėje](../priemimas.md) (`datasets/gov/telsiu_r_sav/priemimas`)
- **Manifest CSV:** [datasets/gov/telsiu_r_sav/priemimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/telsiu_r_sav/priemimai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/telsiu_r_sav/priemimas/Priemimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `prasymo_data` | `date` | `D` | `4` | `open` | — | Prašymo data | — |
| `mokslo_metu_pradzia` | `date` | `D` | `4` | `open` | — | Mokslų metų pradžia | — |
| `vaiko_ak` | `string` | — | `4` | `open` | — | Asmens kodas | — |
| `asm_kodas_tinkamas` | `string` | — | `4` | `open` | — | Ar asmens kodas tinkamas | — |
| `lytis_ak` | `string` | — | `4` | `open` | — | Lytis iš asmens kodo | — |
| `gimimo_metai_ak` | `date` | `Y` | `4` | `open` | — | Gimimo metai iš asmens kodo | — |
| `institucijos_kodas` | `string` | — | `4` | `open` | — | Institucijos kodas | — |
| `institucijos_pavadinimas` | `string` | — | `4` | `open` | — | Institucijos pavadinimas | — |
| `grupe` | `string` | — | `4` | `open` | — | Grupės pavadinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis_ak` | `"Moteris"` | — | — | Moteris | — |
| `lytis_ak` | `"Vyras"` | — | — | Vyras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/telsiu_r_sav/priemimai.csv

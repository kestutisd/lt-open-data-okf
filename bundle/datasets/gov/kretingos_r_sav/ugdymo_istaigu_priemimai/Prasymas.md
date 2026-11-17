---
type: Table
title: "Prasymas — Centralizuoto vaikų priėmimo į ikimokyklinio ir priešmokyklinio ugdymo grupes prašymai"
description: "Kretingos rajono savivaldybės centralizuoto vaikų priėmimo į ikimokyklinio ir priešmokyklinio ugdymo grupes prašymai."
resource: "https://get.data.gov.lt/datasets/gov/kretingos_r_sav/ugdymo_istaigu_priemimai/Prasymas"
tags: [gov, kretingos_r_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kretingos_r_sav/ugdymo_istaigu_priemimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kretingos_r_sav/ugdymo_istaigu_priemimai.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Prasymas — Centralizuoto vaikų priėmimo į ikimokyklinio ir priešmokyklinio ugdymo grupes prašymai

Kretingos rajono savivaldybės centralizuoto vaikų priėmimo į ikimokyklinio ir priešmokyklinio ugdymo grupes prašymai. Duomenys sistemoje nuo 2013 m.

- **Model:** `datasets/gov/kretingos_r_sav/ugdymo_istaigu_priemimai/Prasymas`[^manifest]
- **Dataset:** [Centralizuoto vaikų priėmimo į ikimokyklinio ir priešmokyklinio ugdymo grupes prašymai](../ugdymo_istaigu_priemimai.md) (`datasets/gov/kretingos_r_sav/ugdymo_istaigu_priemimai`)
- **Manifest CSV:** [datasets/gov/kretingos_r_sav/ugdymo_istaigu_priemimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kretingos_r_sav/ugdymo_istaigu_priemimai.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kretingos_r_sav/ugdymo_istaigu_priemimai/Prasymas`
- **Primary Key (`ref`):** `prasymo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `prasymo_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `prasymo_data` | `date` | `D` | `4` | `open` | — | Prašymo data | — |
| `norima_lankyti_nuo` | `integer` | — | `4` | `open` | — | Pageidaujama ugdymo įstaigos lankymo pradžios data | — |
| `asmuo` | `string` | — | `4` | `open` | — | Asmens kodas | — |
| `asm_kodas_tinkamas` | `string` | — | `4` | `open` | — | Ar asmens kodas validus | — |
| `gimimo_metai_ak` | `date` | `Y` | `4` | `open` | — | Asmens gimimo metai iš asmens kodo | — |
| `lytis_ak` | `string` | — | `4` | `open` | — | Asmens lytis iš asmens kodo | — |
| `tevas` | `string` | — | `4` | `open` | — | Globėjo, registruojančio asmenį, vardas, pavardė | — |
| `darzelis` | `string` | — | `4` | `open` | — | Įstaigos pavadinimas | — |
| `grupes_pavadinimas` | `string` | — | `4` | `open` | — | Ugdymo įstaigos grupės pavadinimas | — |
| `busena` | `string` | — | `4` | `open` | — | Būsena | — |
| `busena_1` | `string` | — | `4` | `open` | — | Antra prašymo būsena | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `busena` | `"0"` | — | — | Laukia patvirtinimo | — |
| `busena` | `"1"` | — | — | Atmesta | — |
| `busena` | `"2"` | — | — | Patvirtina | — |
| `busena_1` | `"0"` | — | — | Laukia patvirtinimo | — |
| `busena_1` | `"1"` | — | — | Atmesta | — |
| `busena_1` | `"2"` | — | — | Patvirtina | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kretingos_r_sav/ugdymo_istaigu_priemimai.csv

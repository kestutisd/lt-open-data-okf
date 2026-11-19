---
type: Table
title: "Priemimas — Priėmimai į bendrojo ugdymo įstaigas Telšių r. savivaldybėje"
description: "\"Duomenų rinkinyje pateikiami moksleivių priėmimo į bendrojo ugdymo įstaigų klases Telšių savivaldybėje duomenys.\""
resource: "https://get.data.gov.lt/datasets/gov/telsiu_r_sav/priemimas/Priemimas"
tags: [gov, telsiu_r_sav, priemimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/telsiu_r_sav/priemimai.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/telsiu_r_sav/priemimai.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2927/"
    title: "data.gov.lt DCAT-AP — datasets/gov/telsiu_r_sav/priemimas"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Priemimas — Priėmimai į bendrojo ugdymo įstaigas Telšių r. savivaldybėje

**Dataset Context:** "Duomenų rinkinyje pateikiami moksleivių priėmimo į bendrojo ugdymo įstaigų klases Telšių savivaldybėje duomenys."[^manifest]

- **Model:** `datasets/gov/telsiu_r_sav/priemimas/Priemimas`[^manifest]
- **Dataset:** [Priėmimai į bendrojo ugdymo įstaigas Telšių r. savivaldybėje](../priemimas.md) (`datasets/gov/telsiu_r_sav/priemimas`)[^manifest]
- **Manifest CSV:** [datasets/gov/telsiu_r_sav/priemimai.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/telsiu_r_sav/priemimai.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/telsiu_r_sav/priemimas/Priemimas` (`deployed`)[^manifest]
- **Provider:** `telsiu_r_sav` — Telšių rajono savivaldybė *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis_ak` | `"Moteris"` | — | — | Moteris | — |
| `lytis_ak` | `"Vyras"` | — | — | Vyras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/telsiu_r_sav/priemimai.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/telsiu_r_sav/priemimai.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/telsiu_r_sav/priemimas (https://data.gov.lt/datasets/2927/)

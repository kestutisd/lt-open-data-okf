---
type: Table
title: "Prasymas — Pateikti prašymai priimti mokinius į Kretingos rajono bendrojo ugdymo mokyklas"
description: "Informacija apie vaikų priėmimo į Kretingos rajono savivaldybės mokyklinio ugdymo įstaigas pateiktus prašymus"
resource: "https://get.data.gov.lt/datasets/gov/kretingos_r_sav/mokyklinio_ugdymo_istaigu_priemimai/Prasymas"
tags: [gov, kretingos_r_sav, prasymas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kretingos_r_sav/mokyklinio_ugdymo_istaigu_priemimai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/kretingos_r_sav/mokyklinio_ugdymo_istaigu_priemimai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2767/"
    title: "data.gov.lt DCAT-AP — datasets/gov/kretingos_r_sav/mokyklinio_ugdymo_istaigu_priemimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Prasymas — Pateikti prašymai priimti mokinius į Kretingos rajono bendrojo ugdymo mokyklas

Informacija apie vaikų priėmimo į Kretingos rajono savivaldybės mokyklinio ugdymo įstaigas pateiktus prašymus[^manifest]

- **Model:** `datasets/gov/kretingos_r_sav/mokyklinio_ugdymo_istaigu_priemimai/Prasymas`[^manifest]
- **Dataset:** [Pateikti prašymai priimti mokinius į Kretingos rajono bendrojo ugdymo mokyklas](../mokyklinio_ugdymo_istaigu_priemimai.md) (`datasets/gov/kretingos_r_sav/mokyklinio_ugdymo_istaigu_priemimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/kretingos_r_sav/mokyklinio_ugdymo_istaigu_priemimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kretingos_r_sav/mokyklinio_ugdymo_istaigu_priemimai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kretingos_r_sav/mokyklinio_ugdymo_istaigu_priemimai/Prasymas` (`deployed`)[^manifest]
- **Provider:** `kretingos_r_sav` — Kretingos rajono savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `prasymo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `prasymo_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `prasymo_data` | `date` | `D` | `4` | `open` | — | Prašymo data | — |
| `vaiko_asm_k` | `string` | — | `4` | `open` | — | Šifruotas vaiko asmens kodas | — |
| `lytis_ak` | `string` | — | `4` | `open` | — | Asmens lytis iš asmens kodo | — |
| `gimimo_metai_ak` | `date` | `Y` | `4` | `open` | — | Asmens gimimo metai iš asmens kodo | — |
| `asm_kodas_tinkamas` | `boolean` | — | `4` | `open` | — | Ar asmens kodas tinkamas | — |
| `mokslo_metai` | `integer` | — | `4` | `open` | — | Pageidaujama ugdymo įstaigos lankymo metai | — |
| `prasoma_priimti_nuo` | `date` | `D` | `4` | `open` | — | Pageidaujama ugdymo įstaigos lankymo pradžios data | — |
| `mokyklos_pavadinimas` | `string` | — | `4` | `open` | — | Mokyklos pavadinimas | — |
| `klases_pavadinimas` | `string` | — | `4` | `open` | — | Klases pavadinimas | — |
| `klases_numeris` | `integer` | — | `4` | `open` | — | Klases numeris | — |
| `spec_poreikiu_klase` | `boolean` | — | `4` | `open` | — | Ar klasė specialiųjų poreikių | — |
| `ar_islyginamoji` | `boolean` | — | `4` | `open` | — | Ar klasė išlyginamoji | — |
| `laisvu_vietu_skaicius` | `integer` | — | `4` | `open` | — | Laisvų vietų skaičius | — |
| `ar_prioritetinis` | `boolean` | — | `4` | `open` | — | Ar prašymas prioritetinis | — |
| `busena` | `string` | — | `4` | `open` | — | Būsena | — |
| `busena_1` | `string` | — | `4` | `open` | — | Antra prašymo būsena | — |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis_ak` | `"Vyras"` | — | — | — | — |
| `lytis_ak` | `"Moteris"` | — | — | — | — |
| `lytis_ak` | `"Nenurodyta"` | — | — | — | — |
| `busena` | `"0"` | — | — | Laukia patvirtinimo | — |
| `busena` | `"1"` | — | — | Atmesta | — |
| `busena` | `"2"` | — | — | Patvirtinta | — |
| `busena_1` | `"0"` | — | — | Laukia patvirtinimo | — |
| `busena_1` | `"1"` | — | — | Atmesta | — |
| `busena_1` | `"2"` | — | — | Patvirtinta | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kretingos_r_sav/mokyklinio_ugdymo_istaigu_priemimai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kretingos_r_sav/mokyklinio_ugdymo_istaigu_priemimai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/kretingos_r_sav/mokyklinio_ugdymo_istaigu_priemimai (https://data.gov.lt/datasets/2767/)

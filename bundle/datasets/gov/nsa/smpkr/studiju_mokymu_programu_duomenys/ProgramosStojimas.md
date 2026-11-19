---
type: Table
title: "ProgramosStojimas — Stojimų į aukštojo mokslo programas duomenys"
description: "Lentelėje pateikiami apibendrinti kasmetinių stojimų į aukštojo mokslo programas duomenys iš LAMA BPO sistemos."
resource: "https://get.data.gov.lt/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys/ProgramosStojimas"
tags: [gov, nsa, programosstojimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L51"
    title: "atviriduomenys/manifest — datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L51"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3918/"
    title: "data.gov.lt DCAT-AP — datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# ProgramosStojimas — Stojimų į aukštojo mokslo programas duomenys

Lentelėje pateikiami apibendrinti kasmetinių stojimų į aukštojo mokslo programas duomenys iš LAMA BPO sistemos. Duomenų laiko aprėptis - nuo 2024 metų. Lentelė atnaujinama kasmet, rudens antroje pusėje. Dėl techninių klausimų ar galimų klaidų kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys/ProgramosStojimas`[^manifest]
- **Dataset:** [Studijų ir mokymų programų duomenys](../studiju_mokymu_programu_duomenys.md) (`datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys`)[^manifest]
- **Manifest CSV:** [datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L51](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L51)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys/ProgramosStojimas` (`deployed`)[^manifest]
- **Provider:** `nsa` — Nacionalinė švietimo agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_prime_key`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros sukurtas duomenų eilutės identifikatorius | — |
| `pasirinkimo_metai` | `date` | `D` | `4` | `open` | — | Metai, kuriais stojantysis pateikė prašymą studijuoti per LAMA BPO sistemą | — |
| `prg_valst_kodas` | `string` | — | `4` | `open` | — | Studijų programos valstybinis kodas | — |
| `inst_kodas` | `string` | — | `4` | `open` | — | Švietimo institucijos identifikacinis (JAR) kodas | — |
| `lamabpo_pagr_stojim` | `integer` | — | `4` | `open` | — | Stojančiųjų skaičius pagrindinio priėmimo metu | — |
| `lamabpo_pirmu_nr` | `integer` | — | `4` | `open` | — | Stojančiųjų skaičius, kurie pasirinko programą pirmu numeriu pagrindiniame priėmime | — |
| `lamabpo_antru_treciu_nr` | `integer` | — | `4` | `open` | — | Stojančiųjų skaičius, kurie pasirinko programą antru ar trečiu numeriu pagrindiniame priėmime | — |
| `lamabpo_papild_stojim` | `integer` | — | `4` | `open` | — | Stojančiųjų skaičius papildomo priėmimo metu | — |
| `lamabpo_papild_stojim_pirmu_nr` | `integer` | — | `4` | `open` | — | Stojančiųjų skaičius, kurie pasirinko programą pirmu numeriu papildomame priėmime | — |
| `lamabpo_papild_stojim_antru_treciu_nr` | `integer` | — | `4` | `open` | — | Stojančiųjų skaičius, kurie pasirinko programą antru ar trečiu numeriu papildomame priėmime | — |
| `lamabpo_pakv_pagr_stojim` | `integer` | — | `4` | `open` | — | Pakviestųjų studijuoti skaičius pagrindinio priėmimo metu | — |
| `lamabpo_pakv_papild_stojim` | `integer` | — | `4` | `open` | — | Pakviestųjų studijuoti skaičius papildomo priėmimo metu | — |
| `lamabpo_pasir_pagr_stojim` | `integer` | — | `4` | `open` | — | Pasirašiusiųjų studijų sutartį skaičius pagrindinio priėmimo metu | — |
| `lamabpo_pasir_papild_stojim` | `integer` | — | `4` | `open` | — | Pasirašiusiųjų studijų sutartį skaičius papildomo priėmimo metu | — |
| `lamabpo_nutrauk_pagr_stojim` | `integer` | — | `4` | `open` | — | Nutraukusiųjų studijų sutartį iki prasidedant mokslo metams skaičius pagrindinio priėmimo metu | — |
| `lamabpo_nutrauk_papild_stojim` | `integer` | — | `4` | `open` | — | Nutraukusiųjų studijų sutartį iki prasidedant mokslo metams skaičius papildomo priėmimo metu | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L51 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys.csv#L51)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/nsa/smpkr/studiju_mokymu_programu_duomenys (https://data.gov.lt/datasets/3918/)

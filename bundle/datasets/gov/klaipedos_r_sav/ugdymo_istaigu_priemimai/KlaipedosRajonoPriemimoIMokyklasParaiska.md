---
type: Table
title: "KlaipedosRajonoPriemimoIMokyklasParaiska — Priėmimai į Klaipėdos rajono mokyklinio ugdymo įstaigas"
description: "Informacija apie vaikų priėmimo į Klaipėdos rajono savivaldybės mokyklinio ugdymo įstaigas pateiktus prašymus"
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai/KlaipedosRajonoPriemimoIMokyklasParaiska"
tags: [gov, klaipedos_r_sav, klaipedosrajonopriemimoimokyklasparaiska, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L24"
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L24"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2739/"
    title: "data.gov.lt DCAT-AP — datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# KlaipedosRajonoPriemimoIMokyklasParaiska — Priėmimai į Klaipėdos rajono mokyklinio ugdymo įstaigas

Informacija apie vaikų priėmimo į Klaipėdos rajono savivaldybės mokyklinio ugdymo įstaigas pateiktus prašymus[^manifest]

- **Model:** `datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai/KlaipedosRajonoPriemimoIMokyklasParaiska`[^manifest]
- **Dataset:** [Priėmimai į Klaipėdos rajono ikimokyklinio ir mokyklinio ugdymo įstaigas](../ugdymo_istaigu_priemimai.md) (`datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L24](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L24)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai/KlaipedosRajonoPriemimoIMokyklasParaiska` (`deployed`)[^manifest]
- **Provider:** `klaipedos_r_sav` — Klaipėdos rajono savivaldybė *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `paraiskos_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `paraiskos_id` | `string` | — | `4` | `open` | — | Paraiškos identifikatorius | — |
| `vaiko_asmens_kodas` | `string` | — | `4` | `open` | — | Šifruotas vaiko asmens kodas | — |
| `mokyklos_pavadinimas` | `string` | — | `4` | `open` | — | Mokyklos pavadinimas | — |
| `mokyklos_adresas` | `string` | — | `4` | `open` | — | Mokyklos adresas | — |
| `pageidaujama_klase_lt` | `string` | — | `4` | `open` | — | Paraiškoje nurodyta pageidaujama klasė | — |
| `klases_grupe` | `string` | — | `4` | `open` | — | Paraiškoje nurodoma klasė | — |
| `prasoma_priimti_nuo` | `date` | `D` | `4` | `open` | — | Paraiškoje nurodyta priėmimo data | — |
| `klases_pabaiga` | `date` | `D` | `4` | `open` | — | Klasės veikimo pabaigos data | — |
| `laisvu_vietu_skaicius` | `integer` | — | `4` | `open` | — | Laisvų vietų skaičius | — |
| `buvusi_istaiga` | `string` | — | `4` | `open` | — | Vaiko buvusios ugdymo įstaigos pavadinimas | — |
| `buvusios_istaigos_grupe_lt` | `string` | — | `4` | `open` | — | Vaiko buvusios ugdymo įstaigos grupė ar klasė | — |
| `paraiskos_pateikimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos pateikimo data | — |
| `ar_prioritetinis` | `boolean` | — | `4` | `open` | — | Požymis, ar paraiška yra prioritetinė | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pageidaujama_klase_lt` | `update(property: "pageidaujama_klase@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `buvusios_istaigos_grupe_lt` | `update(property: "buvusios_istaigos_grupe@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L24 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L24)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai (https://data.gov.lt/datasets/2739/)

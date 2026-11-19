---
type: Table
title: "KlaipedosRajonoPriemimoIDarzeliusParaiska — Priėmimai į Klaipėdos rajono ikimokyklinio ugdymo įstaigas"
description: "Informacija apie vaikų priėmimo į Klaipėdos rajono savivaldybės ikimokyklinio ugdymo įstaigas pateiktus prašymus"
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai/KlaipedosRajonoPriemimoIDarzeliusParaiska"
tags: [gov, klaipedos_r_sav, klaipedosrajonopriemimoidarzeliusparaiska, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2739/"
    title: "data.gov.lt DCAT-AP — datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# KlaipedosRajonoPriemimoIDarzeliusParaiska — Priėmimai į Klaipėdos rajono ikimokyklinio ugdymo įstaigas

Informacija apie vaikų priėmimo į Klaipėdos rajono savivaldybės ikimokyklinio ugdymo įstaigas pateiktus prašymus[^manifest]

- **Model:** `datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai/KlaipedosRajonoPriemimoIDarzeliusParaiska`[^manifest]
- **Dataset:** [Priėmimai į Klaipėdos rajono ikimokyklinio ir mokyklinio ugdymo įstaigas](../ugdymo_istaigu_priemimai.md) (`datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai/KlaipedosRajonoPriemimoIDarzeliusParaiska` (`deployed`)[^manifest]
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
| `darzelio_pavadinimas` | `string` | — | `4` | `open` | — | Darželio pavadinimas | — |
| `darzelio_adresas` | `string` | — | `4` | `open` | — | Darželio adresas | — |
| `pageidaujama_grupe_lt` | `string` | — | `4` | `open` | — | Paraiškoje nurodyta pageidaujama grupė | — |
| `grupes_amziaus_intervalas` | `string` | — | `4` | `open` | — | Paraiškoje nurodomas grupės amžiaus intervalas | — |
| `amziaus_pradzia_menesiais` | `string` | — | `4` | `open` | — | Grupės lankymo pradžios amžius mėnesiais | — |
| `prasoma_priimti_nuo` | `date` | `D` | `4` | `open` | — | Paraiškoje nurodyta priėmimo data | — |
| `grupes_pradzia` | `date` | `D` | `4` | `open` | — | Grupės veikimo pradžios data | — |
| `grupes_pabaiga` | `date` | `D` | `4` | `open` | — | Grupės veikimo pabaigos data | — |
| `laisvu_vietu_sk` | `integer` | — | `4` | `open` | — | Laisvų vietų skaičius | — |
| `paraiskos_pateikimo_data` | `date` | `D` | `4` | `open` | — | Paraiškos pateikimo data | — |
| `papildoma_informacija_lt` | `string` | — | `4` | `open` | — | Papildoma informacija apie paraišką | — |
| `budinti_grupe_darzelyje` | `boolean` | — | `4` | `open` | — | Požymis, ar darželyje yra budinti grupė | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pageidaujama_grupe_lt` | `update(property: "pageidaujama_grupe@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `papildoma_informacija_lt` | `update(property: "papildoma_informacija@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/klaipedos_r_sav/ugdymo_istaigu_priemimai (https://data.gov.lt/datasets/2739/)

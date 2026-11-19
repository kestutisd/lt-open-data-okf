---
type: Table
title: "Sutartis — VšĮ Kauno regiono atliekų tvarkymo centro sutarčių duomenys"
description: "\"Rinkinys apima VšĮ Kauno regiono atliekų tvarkymo centro įvairių sutarčių registrus (duomenys nuo 2021- 2023 metų – vienkartiniai duomenys, nebus naujinami): Atliekų priėmimo į Kauno MBA ir Zabieliškio MAR sutarčių registre kaupiami duomenys apie sudarytas sutartis, Atliekų..."
resource: "https://get.data.gov.lt/datasets/gov/karatc/krec/Sutartis"
tags: [gov, karatc, sutartis, deployed, level-4, cadence-never]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/karatc/krec/sutartys.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/karatc/krec/sutartys.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2923/"
    title: "data.gov.lt DCAT-AP — datasets/gov/karatc/krec"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Sutartis — VšĮ Kauno regiono atliekų tvarkymo centro sutarčių duomenys

"Rinkinys apima VšĮ Kauno regiono atliekų tvarkymo centro įvairių sutarčių registrus (duomenys nuo 2021- 2023 metų – vienkartiniai duomenys, nebus naujinami): Atliekų priėmimo į Kauno MBA ir Zabieliškio MAR sutarčių registre kaupiami duomenys apie sudarytas sutartis, Atliekų priėmimo į Lapių ir Zabieliškio regioninius sąvartynus trišalių sutarčių registre kaupiami duomenys apie sudarytas trišales sutartis, Atliekų priėmimo į Zabieliškio ir Lapių regioninį sąvartyną sutarčių registre saugomi duomenys apie sudarytas sutartis, Asbesto turinčių statybinių atliekų priėmimo į Zabieliškio ir Lapių regioninį sąvartyną sutarčių registre kaupiami duomenys apie sudarytas sutartis, Atliekų priėmimo į žaliųjų atliekų kompostavimo aikšteles sutarčių su juridiniais asmenimis registre kaupiami duomenys apie sudarytas sutartis. VšĮ Kauno regiono atliekų tvarkymo centro sutarčių su kitomis šalimis registro duomenys - Ūkinės sutartys Rinkinyje pateikiama sutarties metai, sutarčių kiekis ir duomenų šaltinis - registro pavadinimas"[^manifest]

- **Model:** `datasets/gov/karatc/krec/Sutartis`[^manifest]
- **Dataset:** [VšĮ Kauno regiono atliekų tvarkymo centro sutartys](../krec.md) (`datasets/gov/karatc/krec`)[^manifest]
- **Manifest CSV:** [datasets/gov/karatc/krec/sutartys.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/karatc/krec/sutartys.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/karatc/krec/Sutartis` (`deployed`)[^manifest]
- **Provider:** `karatc` — VšĮ Kauno regiono atliekų tvarkymo centras *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `NEVER`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `metai` | `date` | `Y` | `4` | `open` | — | Sutarčių metai | — |
| `duomenu_saltinis` | `string` | — | `4` | `open` | — | Duomenų šaltinis - sutarčių registras | — |
| `sutarciu_sk` | `number` | — | `4` | `open` | — | Sutarčių skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/karatc/krec/sutartys.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/karatc/krec/sutartys.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/karatc/krec (https://data.gov.lt/datasets/2923/)

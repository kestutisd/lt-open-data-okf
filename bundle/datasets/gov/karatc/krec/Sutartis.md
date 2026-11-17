---
type: Table
title: "Sutartis — VšĮ Kauno regiono atliekų tvarkymo centro sutarčių duomenys"
description: "Rinkinys apima VšĮ Kauno regiono atliekų tvarkymo centro įvairių sutarčių registrus (duomenys nuo 2021- 2023 metų – vienkartiniai duomenys, nebus naujinami): Atliekų priėmimo į Kauno MBA ir Zabieliškio MAR sutarčių registre kaupiami..."
resource: "https://get.data.gov.lt/datasets/gov/karatc/krec/Sutartis"
tags: [gov, karatc, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/karatc/krec/sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/karatc/krec/sutartys.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sutartis — VšĮ Kauno regiono atliekų tvarkymo centro sutarčių duomenys

Rinkinys apima VšĮ Kauno regiono atliekų tvarkymo centro įvairių sutarčių registrus (duomenys nuo 2021- 2023 metų – vienkartiniai duomenys, nebus naujinami): Atliekų priėmimo į Kauno MBA ir Zabieliškio MAR sutarčių registre kaupiami duomenys apie sudarytas sutartis, Atliekų priėmimo į Lapių ir Zabieliškio regioninius sąvartynus trišalių sutarčių registre kaupiami duomenys apie sudarytas trišales sutartis, Atliekų priėmimo į Zabieliškio ir Lapių regioninį sąvartyną sutarčių registre saugomi duomenys apie sudarytas sutartis, Asbesto turinčių statybinių atliekų priėmimo į Zabieliškio ir Lapių regioninį sąvartyną sutarčių registre kaupiami duomenys apie sudarytas sutartis, Atliekų priėmimo į žaliųjų atliekų kompostavimo aikšteles sutarčių su juridiniais asmenimis registre kaupiami duomenys apie sudarytas sutartis. VšĮ Kauno regiono atliekų tvarkymo centro sutarčių su kitomis šalimis registro duomenys - Ūkinės sutartys Rinkinyje pateikiama sutarties metai, sutarčių kiekis ir duomenų šaltinis - registro pavadinimas

- **Model:** `datasets/gov/karatc/krec/Sutartis`[^manifest]
- **Dataset:** [VšĮ Kauno regiono atliekų tvarkymo centro sutartys](../krec.md) (`datasets/gov/karatc/krec`)
- **Manifest CSV:** [datasets/gov/karatc/krec/sutartys.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/karatc/krec/sutartys.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/karatc/krec/Sutartis`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `metai` | `date` | `Y` | `4` | `open` | — | Sutarčių metai | — |
| `duomenu_saltinis` | `string` | — | `4` | `open` | — | Duomenų šaltinis - sutarčių registras | — |
| `sutarciu_sk` | `number` | — | `4` | `open` | — | Sutarčių skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/karatc/krec/sutartys.csv

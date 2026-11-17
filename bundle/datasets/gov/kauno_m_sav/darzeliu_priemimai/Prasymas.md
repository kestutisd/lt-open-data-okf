---
type: Table
title: "Prasymas — Priėmimai į Kauno miesto ikimokyklinio ugdymo įstaigas"
description: "Informacija apie vaikų priėmimo į Kauno miesto savivaldybės ikimokyklinio ugdymo įstaigas pateiktus prašymus"
resource: "https://get.data.gov.lt/datasets/gov/kauno_m_sav/darzeliu_priemimai/Prasymas"
tags: [gov, kauno_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/kauno_m_sav/darzeliu_priemimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/darzeliu_priemimai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Prasymas — Priėmimai į Kauno miesto ikimokyklinio ugdymo įstaigas

Informacija apie vaikų priėmimo į Kauno miesto savivaldybės ikimokyklinio ugdymo įstaigas pateiktus prašymus

- **Model:** `datasets/gov/kauno_m_sav/darzeliu_priemimai/Prasymas`[^manifest]
- **Dataset:** [Priėmimai į Kauno miesto ikimokyklinio ugdymo įstaigas](../darzeliu_priemimai.md) (`datasets/gov/kauno_m_sav/darzeliu_priemimai`)
- **Manifest CSV:** [datasets/gov/kauno_m_sav/darzeliu_priemimai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/kauno_m_sav/darzeliu_priemimai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/kauno_m_sav/darzeliu_priemimai/Prasymas`
- **Primary Key (`ref`):** `busenos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `busenos_id` | `string` | — | `4` | `open` | — | Būsenos identifikatorius | — |
| `vaiko_id` | `string` | — | `4` | `open` | — | Vaiko identifikatorius | — |
| `asmens_kodas` | `string` | — | `4` | `open` | — | Šifruotas asmens kodas | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Vaiko gimimo metai gauti iš asmens kodo | — |
| `lytis` | `string` | — | `4` | `open` | — | Vaiko lytis gauta iš asmens kodo | — |
| `prasymo_id` | `string` | — | `4` | `open` | — | Prašymo identifikatorius | — |
| `pirma_priemimo_data` | `date` | `D` | `4` | `open` | — | Numatoma pirma priėmimo data pagal prašymą | — |
| `busenos_laikas` | `datetime` | — | `4` | `open` | — | Būsenos laikas | — |
| `busena` | `string` | — | `4` | `open` | — | Būsena | — |
| `istaigos_pavadinimas` | `string` | — | `4` | `open` | — | Įstaigos pavadinimas | — |
| `istaigos_adresas` | `string` | — | `4` | `open` | — | Įstaigos adresas | — |
| `grupes_pavadinimas_lt` | `string` | — | `4` | `open` | — | Grupės pavadinimas | — |
| `grupes_amzius_nuo` | `string` | — | `4` | `open` | — | Grupės amžius nuo | — |
| `grupes_amzius_iki` | `string` | — | `4` | `open` | — | Grupės amžius iki | — |
| `mokslo_metai` | `date` | `Y` | `4` | `open` | — | Mokslo metai | — |
| `grupes_vietu_skaicius` | `integer` | — | `4` | `open` | — | Vietų skaičius grupėje | — |
| `prasymas_negalioja_nuo` | `date` | `D` | `4` | `open` | — | Prašymas pažymėtas negaliojančiu nuo | — |
| `nelankoma_nuo` | `date` | `D` | `4` | `open` | — | Grupės lankymo nutraukimas nuo | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Moteris"` | — | — | — | — |
| `lytis` | `"Vyras"` | — | — | — | — |
| `busena` | `"pateko"` | — | — | — | — |
| `busena` | `"pasirašė sutartį su kita įstaiga"` | — | — | — | — |
| `busena` | `"nepateko, nes neliko vietų"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `grupes_pavadinimas_lt` | `update(property: "grupes_pavadinimas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/kauno_m_sav/darzeliu_priemimai.csv

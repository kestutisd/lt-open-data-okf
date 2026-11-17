---
type: Table
title: "Prasymas — Priėmimo prašymų į profesines mokyklas duomenys"
description: "Lentelėje pateikiami priėmimo į profesinio mokymo įstaigas duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lamabpo/profesines_mokyklos/Prasymas"
tags: [gov, lamabpo, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lamabpo/profesiniu_prasymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/profesiniu_prasymai.csv#L46"
    last_modified: "2026-11-11T14:39:20Z"
---

# Prasymas — Priėmimo prašymų į profesines mokyklas duomenys

Lentelėje pateikiami priėmimo į profesinio mokymo įstaigas duomenys. Lentelės eilutės objektas – asmens priėmimo prašymas (prasymo_id). Nurodomas asmens identifikacinis numeris, programos pasirinkimo laiko žyma, priėmimo etapas ir etapo prašymų pateikimo termino data, asmens prašymo prioriteto numeris, programos identifikacinis numeris, mokymo programos finansavimo pobūdis, požymis, ar asmuo gavo pakvietimą į pasirinktą mokymo programą ir mokymo sutarties pasirašymo bei nutraukimo data, jei nutraukimas įvyko iki mokslų pradžios.

- **Model:** `datasets/gov/lamabpo/profesines_mokyklos/Prasymas`[^manifest]
- **Dataset:** [Priėmimo į profesinio mokymo įstaigas prašymų duomenys](../profesines_mokyklos.md) (`datasets/gov/lamabpo/profesines_mokyklos`)
- **Manifest CSV:** [datasets/gov/lamabpo/profesiniu_prasymai.csv#L46](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/profesiniu_prasymai.csv#L46)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lamabpo/profesines_mokyklos/Prasymas`
- **Primary Key (`ref`):** `prasymo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `prasymo_id` | `string` | — | `4` | `open` | — | Prašymo identifikacinis numeris | — |
| `asmens_id` | `string` | — | `4` | `open` | — | Asmens identifikacinis numeris | — |
| `pasirinkimo_data` | `datetime` | `S` | `4` | `open` | — | Mokymo programos pasirinkimo data | — |
| `etapas` | `string` | — | `4` | `open` | — | Prašymo teikimo etapas | — |
| `teikimo_terminas` | `date` | `D` | `4` | `open` | — | Prašymo teikimo termino data | — |
| `prioriteto_nr` | `integer` | — | `4` | `open` | — | Studijų ar mokymo programos prioriteto numeris prašyme | — |
| `programos_id` | `string` | — | `4` | `open` | — | Programos identifikacinis numeris | — |
| `finansavimas` | `string` | — | `4` | `open` | — | Mokymo programos finansavimo pobūdis | — |
| `ar_pakviete` | `boolean` | — | `4` | `open` | — | Požymis, ar asmuo buvo pakviestas į mokymo programą | — |
| `pasirasymo_data` | `datetime` | `S` | `4` | `open` | — | Sutarties pasirašymo data | — |
| `nutraukimo_data` | `date` | `D` | `4` | `open` | — | Mokymo sutarties nutraukimo data (jei tai įvyko iki mokslų pradžios) | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `finansavimas` | `"VF"` | — | — | Valstybinis finansuojama vieta | — |
| `finansavimas` | `"VNF"` | — | — | Valstybės nefinansuojama vieta | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lamabpo/profesiniu_prasymai.csv

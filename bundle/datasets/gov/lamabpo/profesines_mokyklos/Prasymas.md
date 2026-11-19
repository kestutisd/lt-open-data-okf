---
type: Table
title: "Prasymas — Priėmimo prašymų į profesines mokyklas duomenys"
description: "Lentelėje pateikiami priėmimo į profesinio mokymo įstaigas duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lamabpo/profesines_mokyklos/Prasymas"
tags: [gov, lamabpo, prasymas, deployed, level-4, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/profesiniu_prasymai.csv#L46"
    title: "atviriduomenys/manifest — datasets/gov/lamabpo/profesiniu_prasymai.csv#L46"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2913/"
    title: "data.gov.lt DCAT-AP — datasets/gov/lamabpo/profesines_mokyklos"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Prasymas — Priėmimo prašymų į profesines mokyklas duomenys

Lentelėje pateikiami priėmimo į profesinio mokymo įstaigas duomenys. Lentelės eilutės objektas – asmens priėmimo prašymas (prasymo_id). Nurodomas asmens identifikacinis numeris, programos pasirinkimo laiko žyma, priėmimo etapas ir etapo prašymų pateikimo termino data, asmens prašymo prioriteto numeris, programos identifikacinis numeris, mokymo programos finansavimo pobūdis, požymis, ar asmuo gavo pakvietimą į pasirinktą mokymo programą ir mokymo sutarties pasirašymo bei nutraukimo data, jei nutraukimas įvyko iki mokslų pradžios.[^manifest]

- **Model:** `datasets/gov/lamabpo/profesines_mokyklos/Prasymas`[^manifest]
- **Dataset:** [Priėmimo į profesinio mokymo įstaigas prašymų duomenys](../profesines_mokyklos.md) (`datasets/gov/lamabpo/profesines_mokyklos`)[^manifest]
- **Manifest CSV:** [datasets/gov/lamabpo/profesiniu_prasymai.csv#L46](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/profesiniu_prasymai.csv#L46)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lamabpo/profesines_mokyklos/Prasymas` (`deployed`)[^manifest]
- **Provider:** `lamabpo` — Lietuvos aukštųjų mokyklų asociacija bendrajam priėmimui organizuoti (LAMA BPO) *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `prasymo_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `finansavimas` | `"VF"` | — | — | Valstybinis finansuojama vieta | — |
| `finansavimas` | `"VNF"` | — | — | Valstybės nefinansuojama vieta | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lamabpo/profesiniu_prasymai.csv#L46 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lamabpo/profesiniu_prasymai.csv#L46)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/lamabpo/profesines_mokyklos (https://data.gov.lt/datasets/2913/)

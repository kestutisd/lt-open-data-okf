---
type: Table
title: "Dalyvis — Pinigų plovimo prevencijos apmokymų dalyvių duomenys"
description: "Pinigų plovimo prevencijos kompetencijų centro (PPPKC) administruojamoje Organizuojamų mokymų dalyvių registracijos formoje (OMDRF) kaupiami į įstaigos vykdomus mokymus užsiregistravusiųjų dalyvių duomenys."
resource: "https://get.data.gov.lt/datasets/gov/pppkc/omdrf/Dalyvis"
tags: [gov, pppkc, dalyvis, deployed, level-4, cadence-quarterly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pppkc/omdrf.csv#L6"
    title: "atviriduomenys/manifest — datasets/gov/pppkc/omdrf.csv#L6"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/2743/"
    title: "data.gov.lt DCAT-AP — datasets/gov/pppkc/omdrf"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# Dalyvis — Pinigų plovimo prevencijos apmokymų dalyvių duomenys

Pinigų plovimo prevencijos kompetencijų centro (PPPKC) administruojamoje Organizuojamų mokymų dalyvių registracijos formoje (OMDRF) kaupiami į įstaigos vykdomus mokymus užsiregistravusiųjų dalyvių duomenys. Duomenys kaupiami nuo 2022 m. ir yra atnaujinami kas 3 mėnesius. Duomenų rinkinį sudaro dalyvio pseudonimizuotas, tiek maišos algoritmu, tiek raides pavertus žvaigždutėmis, vardas ir pavardė, pseudonimizuotas el. pašto adresas, atviras el. pašto teikėjas, organizacijos pavadinimas, rūšis ir mokymų tema.[^manifest]

- **Model:** `datasets/gov/pppkc/omdrf/Dalyvis`[^manifest]
- **Dataset:** [Pinigų plovimo prevencijos apmokymų dalyvių duomenys](../omdrf.md) (`datasets/gov/pppkc/omdrf`)[^manifest]
- **Manifest CSV:** [datasets/gov/pppkc/omdrf.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pppkc/omdrf.csv#L6)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/pppkc/omdrf/Dalyvis` (`deployed`)[^manifest]
- **Provider:** `pppkc` — VšĮ Pinigų plovimo prevencijos kompetencijų centras *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `vda_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `QUARTERLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `vardas_pavarde` | `string` | — | `4` | `open` | — | Dalyvio vardas ir pavardė, pseudonimizuoti maišos algoritmu | — |
| `vardo_pavardes_simboliai` | `string` | — | `4` | `open` | — | Dalyvio vardas ir pavardė, pseudonimizuoti pavertus raides spec. simboliu | — |
| `el_pastas` | `string` | — | `4` | `open` | — | Dalyvio el. pašto adresas, pseudonimizuotas maišos algoritmu | — |
| `el_pasto_domenas` | `string` | — | `4` | `open` | — | Dalyvio nurodyto el. pašto adreso teikėjas | — |
| `organizacija` | `string` | — | `3` | `open` | — | Organizacija, kuriai priklauso dalyvis | — |
| `organizacijos_rusis` | `string` | — | `4` | `open` | — | Dalyvio organizacijos sritis | — |
| `mokymu_tema` | `string` | — | `4` | `open` | — | Tema mokymų, kuriems užsiregistruota | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/pppkc/omdrf.csv#L6 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/pppkc/omdrf.csv#L6)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/pppkc/omdrf (https://data.gov.lt/datasets/2743/)

---
type: Table
title: "ProfesijPatirtPrilyginimas — Užsienio piliečių profesinės patirties prilyginimo aukštojo mokslo kvalifikacijai statistiniai duomenys"
description: "Statistinis duomenų rinkinys apie profesinės patirties prilyginimui aukštojo mokslo kvalifikacijai išduodamus dokumentus trečiosios valstybės piliečiams, siekiantiems dirbti aukštos profesinės kvalifikacijos reikalaujantį darbą pagal..."
resource: "https://get.data.gov.lt/datasets/gov/eimin/prof_patirt_prilyginimas/ProfesijPatirtPrilyginimas"
tags: [gov, eimin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/eimin/prof_patirt_prilyginimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eimin/prof_patirt_prilyginimas.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# ProfesijPatirtPrilyginimas — Užsienio piliečių profesinės patirties prilyginimo aukštojo mokslo kvalifikacijai statistiniai duomenys

Statistinis duomenų rinkinys apie profesinės patirties prilyginimui aukštojo mokslo kvalifikacijai išduodamus dokumentus trečiosios valstybės piliečiams, siekiantiems dirbti aukštos profesinės kvalifikacijos reikalaujantį darbą pagal nereglamentuojamą profesiją Lietuvoje. Viena eilutė rinkinyje atitinka vieną prašymą. Rinkinyje nurodoma valstybė, iš kurios atvyksta užsienietis, profesija, pagal kurią ketinama įdarbinti užsienietį, sprendimas (teigiamas / neigiamas) bei prašymo gavimo ir sprendimo priėmimo data. Rinkinį sudaro nuo 2017 metų birželio 19 dienos sukaupti duomenys (pagal prašymo gavimo datą).

- **Model:** `datasets/gov/eimin/prof_patirt_prilyginimas/ProfesijPatirtPrilyginimas`[^manifest]
- **Dataset:** [Užsienio piliečių profesinės patirties prilyginimo aukštojo mokslo kvalifikacijai statistiniai duomenys](../prof_patirt_prilyginimas.md) (`datasets/gov/eimin/prof_patirt_prilyginimas`)
- **Manifest CSV:** [datasets/gov/eimin/prof_patirt_prilyginimas.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/eimin/prof_patirt_prilyginimas.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/eimin/prof_patirt_prilyginimas/ProfesijPatirtPrilyginimas`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Duomenų eilutės įrašo identifikacinis kodas | — |
| `id` | `string` | — | `4` | `open` | — | prašymo identifikatorius | — |
| `profesija` | `string` | — | `4` | `open` | — | Profesija | — |
| `pilietybes_salis` | `string` | — | `4` | `open` | — | Pilietybės šalis | — |
| `prasymo_gavimo_data` | `date` | `D` | `4` | `open` | — | Prašymo gavimo data | — |
| `sprendimo_priemimo_data` | `date` | `D` | `4` | `open` | — | Sprendimo priėmimo data | — |
| `sprendimas` | `string` | — | `4` | `open` | — | Sprendimas | — |
| `kodas_pagal_lpk` | `string` | — | `4` | `open` | — | Profesijos kodas pagal Lietuvos profesijų klasifikatorių | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `sprendimas` | `"Atmesta"` | — | — | Profesija neprilyginta aukštojo mokslo kvalifikacijai | — |
| `sprendimas` | `"Prilyginta"` | — | — | Profesija prilyginta aukštojo mokslo kvalifikacijai | — |
| `sprendimas` | `"Nagrinėjimas nutrauktas"` | — | — | Profesijos prilyginimo aukštojo mokslo kvalifikacijai nagrinėjimas buvo nutrauktas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/eimin/prof_patirt_prilyginimas.csv

---
type: Table
title: "LesuPaskirstymas — Lėšų paskirstymas studijų programų kainos kompensavimui"
description: "Duomenų rinkinyje pateikiama informacija apie lėšų paskirstymą, skirtą studijų programų kainų kompensavimui."
resource: "https://get.data.gov.lt/datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui/LesuPaskirstymas"
tags: [gov, vsf, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# LesuPaskirstymas — Lėšų paskirstymas studijų programų kainos kompensavimui

Duomenų rinkinyje pateikiama informacija apie lėšų paskirstymą, skirtą studijų programų kainų kompensavimui. Rinkinyje nurodyti lėšų paskirstymai nuo 2011 metų iki naujausių prieinamų metų. Rinkinio lentelės viena eilutė atitinka vieną studijų programą ir jai paskirtą lėšų sumą kainos kompensavimui. Rinkinį sudaro kompensavimo periodo pavadinimai, mokymosi įstaigos, studijų krypties ir programos pavadinimai, į programą įstojusių ir baigusių asmenų skaičius, asmenų, kuriems kompensuojama už studijas sumokėta suma, studijų kaina ir kompensuojama studijų kaina.

Duomenų teikėjas – Valstybinis studijų fondas.

- **Model:** `datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui/LesuPaskirstymas`[^manifest]
- **Dataset:** [Lėšų paskirstymas studijų programų kainos kompensavimui](../lesu_paskirstymas_studiju_programu_kainos_kompensavimui.md) (`datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui`)
- **Manifest CSV:** [datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui/LesuPaskirstymas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus lėšų paskirstymo eilutės identifikatorius | — |
| `laikotarpis_pavadinimas` | `string` | — | `4` | `open` | — | Lėšų paskirstymo laikotarpio pavadinimas | — |
| `paskirstymas_pav_trump` | `string` | — | `4` | `open` | — | Lėšų paskirstymo laikotarpio pavadinimo trumpinys | — |
| `inst_pavadinimas` | `string` | — | `4` | `open` | — | Mokymosi įstaigos pavadinimas | — |
| `stud_kryptis` | `string` | — | `4` | `open` | — | Studiju kryptis | — |
| `programa_pavadinimas` | `string` | — | `4` | `open` | — | Studijų programos pavadinimas | — |
| `baige` | `integer` | — | `4` | `open` | — | Programą baigusių asmenų skaičius valstybės finansuojamoje vietoje | — |
| `baige_vnf` | `integer` | — | `4` | `open` | — | Programą baigusių asmenų skaičius valstybės nefinansuojamoje vietoje | — |
| `istojo` | `integer` | — | `4` | `open` | — | Į studijų programą įstojusių asmenų skaičius | — |
| `istojimo_metai` | `integer` | — | `4` | `open` | — | Įstojimo į studijų programą metai | — |
| `kompensuojamas_asmenu_skaicius` | `number` | — | `4` | `open` | — | Studijų programoje kompensuojamas asmenų skaičius | — |
| `studiju_kaina` | `number` | — | `4` | `open` | — | Studijų programos kaina | — |
| `kompensuojama_kaina` | `number` | — | `4` | `open` | — | Kompensuojama studijų programos kaina | — |
| `valiuta` | `string` | — | `4` | `open` | — | Studijų programos ir kompensuojamos kainos valiuta | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui.csv

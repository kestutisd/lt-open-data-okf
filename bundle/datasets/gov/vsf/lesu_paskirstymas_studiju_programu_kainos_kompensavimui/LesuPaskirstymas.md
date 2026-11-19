---
type: Table
title: "LesuPaskirstymas — Lėšų paskirstymas studijų programų kainos kompensavimui"
description: "Duomenų rinkinyje pateikiama informacija apie lėšų paskirstymą, skirtą studijų programų kainų kompensavimui."
resource: "https://get.data.gov.lt/datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui/LesuPaskirstymas"
tags: [gov, vsf, lesupaskirstymas, deployed, level-4, cadence-annual_2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui.csv#L7"
    title: "atviriduomenys/manifest — datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui.csv#L7"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/3891/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# LesuPaskirstymas — Lėšų paskirstymas studijų programų kainos kompensavimui

Duomenų rinkinyje pateikiama informacija apie lėšų paskirstymą, skirtą studijų programų kainų kompensavimui. Rinkinyje nurodyti lėšų paskirstymai nuo 2011 metų iki naujausių prieinamų metų. Rinkinio lentelės viena eilutė atitinka vieną studijų programą ir jai paskirtą lėšų sumą kainos kompensavimui. Rinkinį sudaro kompensavimo periodo pavadinimai, mokymosi įstaigos, studijų krypties ir programos pavadinimai, į programą įstojusių ir baigusių asmenų skaičius, asmenų, kuriems kompensuojama už studijas sumokėta suma, studijų kaina ir kompensuojama studijų kaina. Duomenų teikėjas – Valstybinis studijų fondas. Dėl techninių klausimų ar galimų klaidų galima kreiptis į atverimas@stat.gov.lt.[^manifest]

- **Model:** `datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui/LesuPaskirstymas`[^manifest]
- **Dataset:** [Lėšų paskirstymas studijų programų kainos kompensavimui](../lesu_paskirstymas_studiju_programu_kainos_kompensavimui.md) (`datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui`)[^manifest]
- **Manifest CSV:** [datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui.csv#L7)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui/LesuPaskirstymas` (`deployed`)[^manifest]
- **Provider:** `vsf` — Valstybinis studijų fondas *(declared `ns`)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL_2`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui.csv#L7 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui.csv#L7)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vsf/lesu_paskirstymas_studiju_programu_kainos_kompensavimui (https://data.gov.lt/datasets/3891/)

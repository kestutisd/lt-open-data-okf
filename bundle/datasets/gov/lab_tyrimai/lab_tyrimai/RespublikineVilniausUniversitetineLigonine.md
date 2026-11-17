---
type: Table
title: "RespublikineVilniausUniversitetineLigonine — Respublikinės Vilniaus universitetinės ligoninės pacientams atliktų laboratorinių tyrimų rezultatai"
description: "Respublikinės VU ligoninės sistemoje „LIS“ kaupiami pacientams atliktų laboratorinių tyrimų duomenys."
resource: "https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/RespublikineVilniausUniversitetineLigonine"
tags: [gov, lab_tyrimai, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L965"
    last_modified: "2026-11-11T14:39:20Z"
---

# RespublikineVilniausUniversitetineLigonine — Respublikinės Vilniaus universitetinės ligoninės pacientams atliktų laboratorinių tyrimų rezultatai

Respublikinės VU ligoninės sistemoje „LIS“ kaupiami pacientams atliktų laboratorinių tyrimų duomenys. Duomenų rinkinyje pateikiami nuo 2021 metų kaupiami ir iki šiol atnaujinami duomenys. Vienas įrašas atitinka vieną analitės identifikatoriaus reikšmę (visi analičių identifikatoriai yra unikalūs). Rinkinio duomenis sudaro: paciento identifikatorius, gimimo metai, lytis, tyrimo identifikatorius, pavadinimas bei validacijos data, tyrimo analitės identifikatorius, pavadinimas, originalus rezultatų stulpelis su dviem papildomais stulpeliais, į kuriuos atitinkamai išskirstyti tyrimų semantiniai vertinimai ir skaitiniai rezultatai, rezultatų normų rėžiai ir matavimo vienetai. Tyrimo analitė – vienas iš matuojamų sudedamųjų atliekamo laboratorinio tyrimo veiksnių. Kadangi į vieną stulpelį suvedami tiek analičių skaitiniai rezultatai, tiek semantiniai vertinimai, stulpelių su atskirais semantiniais vertinimais arba skaitiniais rezultatais reikšmės kartais gali neatitikti realybės. Duomenų teikėjas – VšĮ Respublikinė Vilniaus universitetinė ligoninė.

- **Model:** `datasets/gov/lab_tyrimai/lab_tyrimai/RespublikineVilniausUniversitetineLigonine`[^manifest]
- **Dataset:** [Pacientams atliktų laboratorinių tyrimų rezultatai](../lab_tyrimai.md) (`datasets/gov/lab_tyrimai/lab_tyrimai`)
- **Manifest CSV:** [datasets/gov/lab_tyrimai/lab_tyrimai.csv#L965](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lab_tyrimai/lab_tyrimai.csv#L965)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lab_tyrimai/lab_tyrimai/RespublikineVilniausUniversitetineLigonine`
- **Primary Key (`ref`):** `vda_prime_key`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `gimimo_metai` | `date` | `Y` | `4` | `open` | — | Gimimo data metų tikslumu | — |
| `lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `tyrimo_id` | `string` | — | `4` | `open` | — | Tyrimo identifikatorius | — |
| `tyrimo_pav` | `string` | — | `4` | `open` | — | Tyrimo pavadinimas | — |
| `tyrimo_val_data` | `date` | `W` | `4` | `open` | — | Tyrimo validacijos data savaitės tikslumu | — |
| `tyrimo_analites_id` | `string` | — | `4` | `open` | — | Tyrimo analitės identifikatorius | — |
| `tyrimo_analites_pav` | `string` | — | `4` | `open` | — | Tyrimo analitės pavadinimas | — |
| `tyrimo_analites_rez_orig` | `string` | — | `1` | `open` | — | Tyrimo analitės rezultatų originalus stulpelis | — |
| `tyrimo_analites_tekst_rez_parsed` | `string` | — | `3` | `open` | — | Tyrimo analitės išskirti semantiniai vertinimai | — |
| `tyrimo_analites_skait_rez_parsed` | `number` | — | `4` | `open` | — | Tyrimo analitės išskirti skaitiniai rezultatai | — |
| `tyrimo_analites_norma_nuo` | `number` | — | `4` | `open` | — | Tyrimo analitės rezultato mažiausia normali reikšmė | — |
| `tyrimo_analites_norma_iki` | `number` | — | `4` | `open` | — | Tyrimo analitės rezultato didžiausia normali reikšmė | — |
| `tyrimo_analites_vnt` | `string` | — | `4` | `open` | — | Tyrimo analitės rezultato matavimo vienetas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Vyras"` | `V` | — | Vyras | — |
| `lytis` | `"Moteris"` | `M` | — | Moteris | — |
| `lytis` | `"Nežinoma"` | `N` | — | Nežinoma | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lab_tyrimai/lab_tyrimai.csv

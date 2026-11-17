---
type: Table
title: "Diplomas — Sveikatos priežiūros specialistų diplomai"
description: "Sveikatos priežiūros specialistų diplomų duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos priežiūros specialistų kompetencijų platformos."
resource: "https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos/Diplomas"
tags: [gov, vaspvt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vaspvt/specialistu_kompetencijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L39"
    last_modified: "2026-11-11T14:39:20Z"
---

# Diplomas — Sveikatos priežiūros specialistų diplomai

Sveikatos priežiūros specialistų diplomų duomenys iš Valstybinės akreditavimo sveikatos priežiūros veiklai tarnybos sveikatos priežiūros specialistų kompetencijų platformos. Viena lentelės eilutė atitinka vieną sveikatos priežiūros specialisto įgytą mokslinio išsilavinimo pažymėjimą (diplomą). Eilutėje nurodomas sveikatos priežiūros specialisto identifikacinis numeris, diplomo tipas, švietimo programos pavadinimas ir valstybinis mokymosi programos kodas, kvalifikacijos pavadinimas ir kodas pagal Nacionalinę švietimo agentūrą, diplomą išdavusios institucijos pavadinimas, JAR kodas, kodo validacijos įvertis ir diplomo išdavimo metai. Paskutiniai du stulpeliai nurodo įrašo sukūrimo ir atnaujinimo datą ir laiką duomenų bazėje.

- **Model:** `datasets/gov/vaspvt/specialistu_kompetencijos/Diplomas`[^manifest]
- **Dataset:** [Sveikatos priežiūros specialistų kompetencijų duomenys](../specialistu_kompetencijos.md) (`datasets/gov/vaspvt/specialistu_kompetencijos`)
- **Manifest CSV:** [datasets/gov/vaspvt/specialistu_kompetencijos.csv#L39](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vaspvt/specialistu_kompetencijos.csv#L39)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vaspvt/specialistu_kompetencijos/Diplomas`
- **Primary Key (`ref`):** `diplomo_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `diplomo_id` | `string` | — | `4` | `open` | — | Diplomo ID | Unikalios eilutės identifikatorius nurodantis unikalų diplomą |
| `specialisto_id` | `string` | — | `4` | `open` | — | Specialisto ID | Specialisto, kuriam priklauso išsilavinimo dokumentas, identifikacinis numeris |
| `diplomo_tipas` | `string` | — | `4` | `open` | — | Išsilavinimo dokumento tipas | — |
| `svietimo_prog` | `string` | — | `4` | `open` | — | Švietimo programos pavadinimas | — |
| `svietimo_prog_kodas` | `string` | — | `4` | `open` | — | Valstybinis mokymosi programos kodas | — |
| `kval` | `string` | — | `4` | `open` | — | Kvalifikacija | Įgytos kvalifikacijos pavadinimas pagal Nacionalinę švietimo agentūrą |
| `kval_kodas` | `string` | — | `4` | `open` | — | Kvalifikacijos kodas | Valstybinis įgytos kvalifikacijos kodas pagal Nacionalinę švietimo agentūrą |
| `institucija` | `string` | — | `4` | `open` | — | Institucija | Išsilavinimo dokumentą išdavusios institucijos pavadinimas |
| `institucijos_kodas` | `string` | — | `4` | `open` | — | Institucijos kodas | Išsilavinimo dokumentą išdavusios institucijos JAR kodas |
| `jar_validacija` | `string` | — | `4` | `open` | — | JAR kodo validacija | Valstybės duomenų agentūros sugeneruotas stulpelis validuojantis institucijos JAR kodus |
| `isdavimo_metai` | `date` | `Y` | `4` | `open` | — | Išsilavinimo dokumento išdavimo metai | — |
| `irasas_sukurtas` | `datetime` | `S` | `4` | `open` | — | Įrašas sukurtas | Įrašo, duomenų bazėje, sukūrimo data ir laikas |
| `irasas_atnaujintas` | `datetime` | `S` | `4` | `open` | — | Įrašas atnaujintas | Įrašo, duomenų bazėje, atnaujinimo data ir laikas |

[^manifest]: atviriduomenys/manifest — datasets/gov/vaspvt/specialistu_kompetencijos.csv

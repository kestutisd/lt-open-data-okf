---
type: Table
title: "PriemimuStatistika — Prašymų, priimti į Klaipėdos miesto savivaldybės mokyklas, statistika"
description: "Lentelėje yra pateikta prašymų, priimti į Klaipėdos miesto savivaldybės mokyklas, statistika nuo 2019 metų iš informacinės registravimosi į Klaipėdos miesto savivaldybės mokyklas sistemos (PM IS)."
resource: "https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/pmis/PriemimuStatistika"
tags: [gov, klaipedos_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/pmis.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/pmis.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# PriemimuStatistika — Prašymų, priimti į Klaipėdos miesto savivaldybės mokyklas, statistika

Lentelėje yra pateikta prašymų, priimti į Klaipėdos miesto savivaldybės mokyklas, statistika nuo 2019 metų iš informacinės registravimosi į Klaipėdos miesto savivaldybės mokyklas sistemos (PM IS). Duomenys atnaujinami kas 6 mėnesius. Duomenų rinkinys apima priėmimo identifikatorių, mokyklos identifikatorių, pavadinimą, tipą ir adresą. Į prototipą taip pat patenka klasės numeris, identifikatorius, paskirtis bei statistikos etapas ir įrašo sukūrimo data su laiku. Statistiniai duomenys pagal laikotarpį yra suskaičiuoti iš šių reiškinių: laisvos vietos, pateikti prašymai, tikrinami prašymai, priimti prašymai, atmesti prašymai bei nepriimti prašymai.

- **Model:** `datasets/gov/klaipedos_m_sav/pmis/PriemimuStatistika`[^manifest]
- **Dataset:** [Prašymų, priimti į Klaipėdos miesto savivaldybės mokyklas, statistika](../pmis.md) (`datasets/gov/klaipedos_m_sav/pmis`)
- **Manifest CSV:** [datasets/gov/klaipedos_m_sav/pmis.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/klaipedos_m_sav/pmis.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/klaipedos_m_sav/pmis/PriemimuStatistika`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `priemimo_id` | `string` | — | `4` | `open` | — | Priėmimo identifikatorius | — |
| `mokyklos_id` | `string` | — | `4` | `open` | — | Mokyklos identifikatorius | — |
| `mokyklos_pavadinimas` | `string` | — | `4` | `open` | — | Mokyklos pavadinimas | — |
| `mokyklos_tipas` | `string` | — | `4` | `open` | — | Mokyklos tipas | — |
| `mokyklos_adresas` | `string` | — | `4` | `open` | — | Mokyklos adresas | — |
| `klases_id` | `string` | — | `4` | `open` | — | Mokyklinės klasės identifikatorius | — |
| `klases_nr` | `integer` | — | `4` | `open` | — | Mokyklinės klasės numeris | — |
| `klases_paskirtis` | `string` | — | `4` | `open` | — | Mokyklinės klasės paskirtis | — |
| `etapas` | `string` | — | `4` | `open` | — | Statistikos etapas | — |
| `laisvos_vietos` | `integer` | — | `4` | `open` | — | Laisvų vietų skaičius | — |
| `pateikti_prasymai` | `integer` | — | `4` | `open` | — | Pateiktų prašymų skaičius | — |
| `tikrinami_prasymai` | `integer` | — | `4` | `open` | — | Tikrinamų prašymų skaičius | — |
| `priimti_prasymai` | `integer` | — | `4` | `open` | — | Priimtų prašymų skaičius | — |
| `atmesti_prasymai` | `integer` | — | `4` | `open` | — | Atmestų prašymų skaičius | — |
| `nepriimti_prasymai` | `integer` | — | `4` | `open` | — | Nepriimtų prašymų skaičius | — |
| `skaiciai_laikotarpiui` | `string` | — | `4` | `open` | — | Laikotarpis, kuriam pateikti skaičiai | — |
| `iraso_sukurimo_data` | `datetime` | `S` | `4` | `open` | — | Įrašo sukūrimo data ir laikas sekundžių tikslumu | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `mokyklos_tipas` | `"progimnazija"` | — | — | Progimnazija | — |
| `mokyklos_tipas` | `"gimnazija"` | — | — | Gimnazija | — |
| `mokyklos_tipas` | `"pagrindinė mokykla"` | — | — | Pagrindinė mokykla | — |
| `mokyklos_tipas` | `"mokykla-darželis"` | — | — | Mokykla-darželis | — |
| `mokyklos_tipas` | `"pradinė mokykla"` | — | — | Pradinė mokykla | — |
| `etapas` | `"pirmas"` | — | — | Pirmas statistikos etapas | — |
| `etapas` | `"antras"` | — | — | Antras statistikos etapas | — |
| `skaiciai_laikotarpiui` | `"po_priemimo"` | — | — | Skaičiai po priėmimo | — |
| `skaiciai_laikotarpiui` | `"prieš_priemimą"` | — | — | Skaičiai prieš priėmimą | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/klaipedos_m_sav/pmis.csv

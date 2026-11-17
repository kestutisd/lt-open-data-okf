---
type: Table
title: "Registracija — Pacientų registracijos paslaugoms Žalgirio klinikoje"
description: "Vilniaus universiteto ligoninės Žalgirio klinikos sveikatos priežiūros sistema kaupia pacientų asmeninius duomenis, kaip registracija vizitams pas gydytoją."
resource: "https://get.data.gov.lt/datasets/gov/vulzk/registracija/Registracija"
tags: [gov, vulzk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vulzk/registracija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/registracija.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# Registracija — Pacientų registracijos paslaugoms Žalgirio klinikoje

Vilniaus universiteto ligoninės Žalgirio klinikos sveikatos priežiūros sistema kaupia pacientų asmeninius duomenis, kaip registracija vizitams pas gydytoją. Duomenys kaupiami nuo 2010 m. iki 2020 m. Duomenų rinkinys sudarytas iš registracijos identifikatoriaus, datos, kuriai registruotasi, įrašo sukūrimo bei keitimo datų, paciento duomenų: šifruoto identifikatoriaus, lyties, gimimo metų bei gydytojo duomenų: identifikatoriaus ir specialybės.

- **Model:** `datasets/gov/vulzk/registracija/Registracija`[^manifest]
- **Dataset:** [Pacientų registracijos paslaugoms Žalgirio klinikoje](../registracija.md) (`datasets/gov/vulzk/registracija`)
- **Manifest CSV:** [datasets/gov/vulzk/registracija.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vulzk/registracija.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vulzk/registracija/Registracija`
- **Primary Key (`ref`):** `registracijos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `registracijos_id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `gydymo_registracijos_data` | `datetime` | `T` | `4` | `open` | — | Data ir laikas minutės tikslumu, kuriam registruotasi pas gydytoją | — |
| `registracijos_iraso_sukurimo_data` | `datetime` | `T` | `4` | `open` | — | Registracijos pas gydytoją įrašo sukūrimo data ir laikas minutės tikslumu | — |
| `registracijos_iraso_keitimo_data` | `datetime` | `T` | `4` | `open` | — | Registracijos pas gydytoją įrašo keitimo data ir laikas minutės tikslumu | — |
| `paciento_id` | `string` | — | `4` | `open` | — | Paciento identifikatorius | — |
| `paciento_lytis` | `string` | — | `4` | `open` | — | Paciento lytis | — |
| `paciento_gimimo_metai` | `datetime` | `Y` | `4` | `open` | — | Paciento gimimo metai | — |
| `gydytojo_id` | `string` | — | `4` | `open` | — | Gydytojo, pas kurį registruotasi, identifikatorius | — |
| `gydytojo_specialybe` | `string` | — | `4` | `open` | — | Gydytojo, pas kurį registruotasi, specialybė | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `paciento_lytis` | `"vyras"` | `V` | — | Vyras | — |
| `paciento_lytis` | `"moteris"` | `M` | — | Moteris | — |
| `paciento_lytis` | `"kita"` | `X` | — | Kita | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vulzk/registracija.csv

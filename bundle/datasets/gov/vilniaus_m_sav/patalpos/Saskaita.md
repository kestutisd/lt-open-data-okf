---
type: Table
title: "Saskaita — Vilniaus miesto savivaldybės sąskaitos patalpų nuomininkams už suteiktas paslaugas"
description: "Spinta table datasets/gov/vilniaus_m_sav/patalpos/Saskaita (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/patalpos/Saskaita"
tags: [gov, vilniaus_m_sav, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/patalpos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L54"
    last_modified: "2026-11-11T14:39:20Z"
---

# Saskaita — Vilniaus miesto savivaldybės sąskaitos patalpų nuomininkams už suteiktas paslaugas

- **Model:** `datasets/gov/vilniaus_m_sav/patalpos/Saskaita`[^manifest]
- **Dataset:** [Vilniaus miesto savivaldybės nuomojamų patalpų sutarčių duomenys](../patalpos.md) (`datasets/gov/vilniaus_m_sav/patalpos`)
- **Manifest CSV:** [datasets/gov/vilniaus_m_sav/patalpos.csv#L54](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vilniaus_m_sav/patalpos.csv#L54)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vilniaus_m_sav/patalpos/Saskaita`
- **Primary Key (`ref`):** `saskaitos_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `saskaitos_id` | `string` | — | `4` | `open` | — | Sąskaitos identifikacinis numeris | — |
| `sutarties_id` | `string` | — | `4` | `open` | — | Sutarties identifikacinis numeris | — |
| `saskaitos_nr` | `string` | — | `4` | `open` | — | Sąskaitos numeris | — |
| `periodo_pradzia` | `date` | `D` | `4` | `open` | — | Periodo, už kurį išrašyta sąskaita faktūra, pradžia | — |
| `periodo_pabaiga` | `date` | `D` | `4` | `open` | — | Periodo, už kurį išrašyta sąskaita faktūra, pabaiga | — |
| `israsymo_data` | `date` | `D` | `4` | `open` | — | Sąskaitos apmokėjimo data | — |
| `apmokejimas` | `date` | `D` | `4` | `open` | — | Sąskaitos faktūros išrašymo data | — |
| `nuomos_val` | `number` | `h` | `4` | `open` | — | Nuomos valandų skaičius | — |
| `suma_reitingas` | `integer` | — | `4` | `open` | — | Sąskaitoje faktūroje nurodyta bendra suma apmokėjimui, kurios dydis išreitinguotas pagal visas kitas sąskaitas, išrašytas per tą patį laikotarpį | — |
| `duomenu_atnaujinimas` | `date` | `D` | `4` | `open` | — | Sąskaitos duomenų atnaujinimo data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vilniaus_m_sav/patalpos.csv

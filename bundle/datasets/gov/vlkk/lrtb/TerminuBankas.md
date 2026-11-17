---
type: Table
title: "TerminuBankas — VLKK terminų banko terminų duomenys"
description: "Valstybinės lietuvių kalbos komisijos Lietuvos Respublikos terminų banke kaupiami įvairių sričių terminai lietuvių bei kitomis Europos kalbomis, kaip vokiečių, prancūzų, lenkų."
resource: "https://get.data.gov.lt/datasets/gov/vlkk/lrtb/TerminuBankas"
tags: [gov, vlkk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlkk/lrtb.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/lrtb.csv#L7"
    last_modified: "2026-11-11T14:39:20Z"
---

# TerminuBankas — VLKK terminų banko terminų duomenys

Valstybinės lietuvių kalbos komisijos Lietuvos Respublikos terminų banke kaupiami įvairių sričių terminai lietuvių bei kitomis Europos kalbomis, kaip vokiečių, prancūzų, lenkų. Duomenys kaupiami nuo 2005 m. ir atnaujinami kas mėnesį. Apimami duomenys yra patys terminai, jų sritys, kalba, statusas: teiktinas, neteiktinas arba aprobuotas, įvedimo data bei organizacija, pateikusi patį terminą. Tarp tokių organizacijų patenka VLKK, Užsienio reikalų ministerija, Policijos departamentas.

- **Model:** `datasets/gov/vlkk/lrtb/TerminuBankas`[^manifest]
- **Dataset:** [VLKK terminų banko terminų duomenys](../lrtb.md) (`datasets/gov/vlkk/lrtb`)
- **Manifest CSV:** [datasets/gov/vlkk/lrtb.csv#L7](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlkk/lrtb.csv#L7)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlkk/lrtb/TerminuBankas`
- **Primary Key (`ref`):** `termino_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `termino_id` | `string` | — | `4` | `open` | — | Identifikatorius | — |
| `terminas` | `string` | — | `4` | `open` | — | Terminas | — |
| `sritis` | `string` | — | `4` | `open` | — | Termino sritis | — |
| `kalba` | `string` | — | `4` | `open` | — | Termino kalba | — |
| `statusas` | `string` | — | `4` | `open` | — | Termino statusas, anot VLKK | — |
| `pateikusi_org` | `string` | — | `4` | `open` | — | Terminą pateikusi organizacija | — |
| `ivedimo_data` | `datetime` | `S` | `4` | `open` | — | Termino įvedimo data ir laikas sekundžių tikslumu | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `statusas` | — | `Teiktinas` | — | Teiktinas terminas | — |
| `statusas` | — | `Neteiktinas` | — | Neteiktinas terminas | — |
| `statusas` | — | `Aprobuotas` | — | Aprobuotas terminas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlkk/lrtb.csv

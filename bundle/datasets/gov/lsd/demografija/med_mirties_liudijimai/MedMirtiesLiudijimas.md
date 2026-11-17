---
type: Table
title: "MedMirtiesLiudijimas — Mirčių skaičiai pagal elektroninius medicininius mirties liudijimus"
description: "Spinta table datasets/gov/lsd/demografija/med_mirties_liudijimai/MedMirtiesLiudijimas (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/lsd/demografija/med_mirties_liudijimai/MedMirtiesLiudijimas"
tags: [gov, lsd, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lsd/demografija/demografija.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/demografija/demografija.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# MedMirtiesLiudijimas — Mirčių skaičiai pagal elektroninius medicininius mirties liudijimus

- **Model:** `datasets/gov/lsd/demografija/med_mirties_liudijimai/MedMirtiesLiudijimas`[^manifest]
- **Dataset:** [datasets/gov/lsd/demografija/med_mirties_liudijimai](../med_mirties_liudijimai.md) (`datasets/gov/lsd/demografija/med_mirties_liudijimai`)
- **Manifest CSV:** [datasets/gov/lsd/demografija/demografija.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lsd/demografija/demografija.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lsd/demografija/med_mirties_liudijimai/MedMirtiesLiudijimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus įdentifikatorius | — |
| `data` | `date` | `D` | `4` | `open` | — | Faktinė asmens mirties data | — |
| `amzius` | `integer` | — | `3` | `open` | — | Asmens amžius mirties datą | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis | — |
| `mirtys` | `integer` | — | `4` | `open` | — | Mirčių skaičius pagal mirties datą, asmens amžių ir lytį | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"mot"` | — | — | Moteris | — |
| `lytis` | `"vyr"` | — | — | Vyras | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `amzius` | `update(ref: "Y")` | `ref` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lsd/demografija/demografija.csv

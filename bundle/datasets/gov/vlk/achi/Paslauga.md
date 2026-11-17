---
type: Table
title: "Paslauga — Dienos chirurgijos metu atiliekamų intervencijų sąrašas"
description: "Spinta table datasets/gov/vlk/achi/Paslauga (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vlk/achi/Paslauga"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/achi.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/achi.csv#L42"
    last_modified: "2026-11-11T14:39:20Z"
---

# Paslauga — Dienos chirurgijos metu atiliekamų intervencijų sąrašas

- **Model:** `datasets/gov/vlk/achi/Paslauga`[^manifest]
- **Dataset:** [datasets/gov/vlk/achi](../achi.md) (`datasets/gov/vlk/achi`)
- **Manifest CSV:** [datasets/gov/vlk/achi.csv#L42](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/achi.csv#L42)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/achi/Paslauga`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `intervencija` | `ref` | [Intervencija](Intervencija.md) | `4` | `open` | — | ACHI ID | Nuoroda į Intervencijas |
| `is_gnr_anestesia` | `string` | `int_r` | `4` | `open` | — | Bendroji nejautra | — |
| `is_rgn_anestesia` | `string` | `int_r` | `4` | `open` | — | Regioninė nejautra | — |
| `dchir_grupe` | `string` | — | `4` | `open` | — | Paslaugų grupė | Dienos chirurgijos paslaugų grupė |
| `nuo` | `date` | `D` | `4` | `open` | — | Galioja nuo | Dienos chirurgijos procedūros galiojimo pradžios data |
| `iki` | `date` | `D` | `4` | `open` | — | Galioja iki | Dienos chirurgijos procedūros galiojimo pabaigos data |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `is_gnr_anestesia` | `"Ne"` | — | — | — | — |
| `is_gnr_anestesia` | `"Taip"` | — | — | — | — |
| `is_rgn_anestesia` | `"Ne"` | — | — | — | — |
| `is_rgn_anestesia` | `"Taip"` | — | — | — | — |
| `dchir_grupe` | `"I"` | — | — | I - grupė | — |
| `dchir_grupe` | `"II"` | — | — | II - grupė | — |
| `dchir_grupe` | `"III"` | — | — | III - grupė | — |
| `dchir_grupe` | `"IV"` | — | — | IV - grupė | — |
| `dchir_grupe` | `"V"` | — | — | V - grupė | — |
| `dchir_grupe` | `"VI"` | — | — | VI - grupė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/achi.csv

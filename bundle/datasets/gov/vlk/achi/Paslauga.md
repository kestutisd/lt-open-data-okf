---
type: Table
title: "Paslauga — Dienos chirurgijos metu atiliekamų intervencijų sąrašas"
description: "Spinta table datasets/gov/vlk/achi/Paslauga (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/vlk/achi/Paslauga"
tags: [gov, vlk, paslauga, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/achi.csv#L42"
    title: "atviriduomenys/manifest — datasets/gov/vlk/achi.csv#L42"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1383/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/achi"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Paslauga — Dienos chirurgijos metu atiliekamų intervencijų sąrašas

- **Model:** `datasets/gov/vlk/achi/Paslauga`[^manifest]
- **Dataset:** [Medicininių intervencijų sąrašas (ACHI)](../achi.md) (`datasets/gov/vlk/achi`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/achi.csv#L42](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/achi.csv#L42)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/achi/Paslauga` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `ad_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `intervencija` | `ref` | [Intervencija](Intervencija.md) (`level=4 UUID`: `intervencija._id`) | `4` | `open` | — | ACHI ID | Nuoroda į Intervencijas |
| `is_gnr_anestesia` | `string` | `enum: int_r` | `4` | `open` | — | Bendroji nejautra | — |
| `is_rgn_anestesia` | `string` | `enum: int_r` | `4` | `open` | — | Regioninė nejautra | — |
| `dchir_grupe` | `string` | — | `4` | `open` | — | Paslaugų grupė | Dienos chirurgijos paslaugų grupė |
| `nuo` | `date` | `D` | `4` | `open` | — | Galioja nuo | Dienos chirurgijos procedūros galiojimo pradžios data |
| `iki` | `date` | `D` | `4` | `open` | — | Galioja iki | Dienos chirurgijos procedūros galiojimo pabaigos data |

# Enumerations

| Property | Value (prepare) | Source | Access | Title | Description |
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

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/achi.csv#L42 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/achi.csv#L42)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/achi (https://data.gov.lt/datasets/1383/)

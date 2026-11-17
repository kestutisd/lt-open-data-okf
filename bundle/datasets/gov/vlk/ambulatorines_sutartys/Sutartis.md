---
type: Table
title: "Sutartis — Ambulatorinių asmens sveikatos priežiūros paslaugų sutarčių sąrašas"
description: "Informacija apie asmens sveikatos priežiūros įstaigų Privalomojo sveikatos draudimo fondo lėšomis sudarytas ambulatorines paslaugų sutartis"
resource: "https://get.data.gov.lt/datasets/gov/vlk/ambulatorines_sutartys/Sutartis"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/ambulatorines_sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/ambulatorines_sutartys.csv#L11"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sutartis — Ambulatorinių asmens sveikatos priežiūros paslaugų sutarčių sąrašas

Informacija apie asmens sveikatos priežiūros įstaigų Privalomojo sveikatos draudimo fondo lėšomis sudarytas ambulatorines paslaugų sutartis

- **Model:** `datasets/gov/vlk/ambulatorines_sutartys/Sutartis`[^manifest]
- **Dataset:** [datasets/gov/vlk/ambulatorines_sutartys](../ambulatorines_sutartys.md) (`datasets/gov/vlk/ambulatorines_sutartys`)
- **Manifest CSV:** [datasets/gov/vlk/ambulatorines_sutartys.csv#L11](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/ambulatorines_sutartys.csv#L11)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/ambulatorines_sutartys/Sutartis`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `kodas` | `ref` | [/datasets/gov/vlk/istaigos/Istaiga[kodas]](../istaigos/Istaiga.md) | `4` | `open` | — | Įstaigos ID | Įstaigos, kuri sudarė sutartį, ID |
| `nuo` | `date` | `D` | `4` | `open` | — | Sutarties galiojimo pradžia | Sutarties galiojimo pradžios data |
| `iki` | `date` | `D` | `4` | `open` | — | Sutarties galiojimo pabaiga | Sutarties galiojimo pabaigos data |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/ambulatorines_sutartys.csv

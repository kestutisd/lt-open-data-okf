---
type: Table
title: "Paslauga — Ambulatorinių asmens sveikatos priežiūros paslaugų sutartyse sąrašas"
description: "Informacija apie asmens sveikatos priežiūros įstaigų Privalomojo sveikatos draudimo fondo lėšomis teikiamas ambulatorines paslaugas"
resource: "https://get.data.gov.lt/datasets/gov/vlk/ambulatorines_sutartys/Paslauga"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/ambulatorines_sutartys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/ambulatorines_sutartys.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Paslauga — Ambulatorinių asmens sveikatos priežiūros paslaugų sutartyse sąrašas

Informacija apie asmens sveikatos priežiūros įstaigų Privalomojo sveikatos draudimo fondo lėšomis teikiamas ambulatorines paslaugas

- **Model:** `datasets/gov/vlk/ambulatorines_sutartys/Paslauga`[^manifest]
- **Dataset:** [datasets/gov/vlk/ambulatorines_sutartys](../ambulatorines_sutartys.md) (`datasets/gov/vlk/ambulatorines_sutartys`)
- **Manifest CSV:** [datasets/gov/vlk/ambulatorines_sutartys.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/ambulatorines_sutartys.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/ambulatorines_sutartys/Paslauga`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sutartis` | `ref` | [Sutartis](Sutartis.md) | `4` | `open` | — | Nuoroda į Sutartis | — |
| `paslauga` | `ref` | [/datasets/gov/vlk/paslaugos/Paslauga](../paslaugos/Paslauga.md) | `4` | `open` | — | Nuoroda į paslaugą, dėl kurios sudaryta sutartis | Paslaugos, dėl kurios sudaryta sutartis, kodas |
| `nuo` | `date` | `D` | `4` | `open` | — | Paslaugos galiojimo sutartyje pradžia | Paslaugos galiojimo sutartyje pradžios data |
| `iki` | `date` | `D` | `4` | `open` | — | Paslaugos galiojimo sutartyje pabaiga | Paslaugos galiojimo sutartyje pabaigos data |
| `anuliavimo_data` | `date` | `D` | `4` | `open` | — | Paslaugos galiojimo sutartyje anuliavimo data | Paslaugos galiojimo sutartyje anuliavimo data |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/ambulatorines_sutartys.csv

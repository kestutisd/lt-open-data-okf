---
type: Table
title: "Paslauga — Ambulatorinių asmens sveikatos priežiūros paslaugų sutartyse sąrašas"
description: "Informacija apie asmens sveikatos priežiūros įstaigų Privalomojo sveikatos draudimo fondo lėšomis teikiamas ambulatorines paslaugas"
resource: "https://get.data.gov.lt/datasets/gov/vlk/ambulatorines_sutartys/Paslauga"
tags: [gov, vlk, paslauga, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/ambulatorines_sutartys.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/vlk/ambulatorines_sutartys.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1536/"
    title: "data.gov.lt DCAT-AP — datasets/gov/vlk/ambulatorines_sutartys"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# Paslauga — Ambulatorinių asmens sveikatos priežiūros paslaugų sutartyse sąrašas

Informacija apie asmens sveikatos priežiūros įstaigų Privalomojo sveikatos draudimo fondo lėšomis teikiamas ambulatorines paslaugas[^manifest]

- **Model:** `datasets/gov/vlk/ambulatorines_sutartys/Paslauga`[^manifest]
- **Dataset:** [Numatomų teikti ambulatorinių asmens sveikatos priežiūros paslaugų sąrašas, pateikiamas gydymo...](../ambulatorines_sutartys.md) (`datasets/gov/vlk/ambulatorines_sutartys`)[^manifest]
- **Manifest CSV:** [datasets/gov/vlk/ambulatorines_sutartys.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/ambulatorines_sutartys.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/ambulatorines_sutartys/Paslauga` (`deployed`)[^manifest]
- **Provider:** `vlk` — Valstybinė ligonių kasa *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `sutartis` | `ref` | [Sutartis](Sutartis.md) (`level=4 UUID`: `sutartis._id`) | `4` | `open` | — | Nuoroda į Sutartis | — |
| `paslauga` | `ref` | [Paslauga](../paslaugos/Paslauga.md) (`level=4 UUID`: `paslauga._id`) | `4` | `open` | — | Nuoroda į paslaugą, dėl kurios sudaryta sutartis | Paslaugos, dėl kurios sudaryta sutartis, kodas |
| `nuo` | `date` | `D` | `4` | `open` | — | Paslaugos galiojimo sutartyje pradžia | Paslaugos galiojimo sutartyje pradžios data |
| `iki` | `date` | `D` | `4` | `open` | — | Paslaugos galiojimo sutartyje pabaiga | Paslaugos galiojimo sutartyje pabaigos data |
| `anuliavimo_data` | `date` | `D` | `4` | `open` | — | Paslaugos galiojimo sutartyje anuliavimo data | Paslaugos galiojimo sutartyje anuliavimo data |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/ambulatorines_sutartys.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/ambulatorines_sutartys.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/vlk/ambulatorines_sutartys (https://data.gov.lt/datasets/1536/)

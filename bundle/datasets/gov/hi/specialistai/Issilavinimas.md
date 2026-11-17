---
type: Table
title: "Issilavinimas — Visuomenės sveikatos specialistų duomenys pagal išsilavinimą"
description: "Spinta table datasets/gov/hi/specialistai/Issilavinimas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/hi/specialistai/Issilavinimas"
tags: [gov, hi, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/specialistai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Issilavinimas — Visuomenės sveikatos specialistų duomenys pagal išsilavinimą

- **Model:** `datasets/gov/hi/specialistai/Issilavinimas`[^manifest]
- **Dataset:** [Visuomenės sveikatos priežiūros specialistų duomenys](../specialistai.md) (`datasets/gov/hi/specialistai`)
- **Manifest CSV:** [datasets/gov/hi/specialistai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/specialistai/Issilavinimas`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `jar` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_kodas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Įstaiga | Įstaigos, kurioje dirba visuomenės sveikatos priežiūros specialistas, kodas |
| `lytis` | `string` | — | `4` | `open` | — | Specialisto lytis | — |
| `amzius` | `string` | — | `4` | `open` | — | Specialisto amžiaus grupė | — |
| `studiju_sritis` | `string` | — | `4` | `open` | — | Specialistui priskirta studijų krypčių grupė | — |
| `kvalifikacija` | `string` | — | `4` | `open` | — | Specialisto kvalifikacinis laipsnis | — |
| `mokslo_laipsnis` | `string` | — | `4` | `open` | — | Specialisto mokslo laipsnis | — |
| `issilavinimas` | `string` | — | `4` | `open` | — | Specialisto išsilavinimas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/specialistai.csv

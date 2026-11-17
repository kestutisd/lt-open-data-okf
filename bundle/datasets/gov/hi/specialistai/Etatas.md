---
type: Table
title: "Etatas — Visuomenės sveikatos specialistų duomenys pagal darbo etatus"
description: "Spinta table datasets/gov/hi/specialistai/Etatas (6 columns)."
resource: "https://get.data.gov.lt/datasets/gov/hi/specialistai/Etatas"
tags: [gov, hi, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/hi/specialistai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L13"
    last_modified: "2026-11-11T14:39:20Z"
---

# Etatas — Visuomenės sveikatos specialistų duomenys pagal darbo etatus

- **Model:** `datasets/gov/hi/specialistai/Etatas`[^manifest]
- **Dataset:** [Visuomenės sveikatos priežiūros specialistų duomenys](../specialistai.md) (`datasets/gov/hi/specialistai`)
- **Manifest CSV:** [datasets/gov/hi/specialistai.csv#L13](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/hi/specialistai.csv#L13)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/hi/specialistai/Etatas`
- **Primary Key (`ref`):** `m_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `m_id` | `string` | — | `4` | `open` | — | Specialisto ID | — |
| `jar` | `ref` | [/datasets/gov/rc/jar/iregistruoti/JuridinisAsmuo[ja_kodas]](../../rc/jar/iregistruoti/JuridinisAsmuo.md) | `4` | `open` | — | Įstaiga | Įstaigos, kurioje dirba visuomenės sveikatos priežiūros specialistas, kodas |
| `etatas` | `number` | `U` | `4` | `open` | — | Etatas | — |
| `priimtas` | `integer` | `yr` | `2` | `open` | — | Metai | Kuomet priimtas dirbti visuomenės sveikatos priežiūros specialistas |
| `lytis` | `string` | — | `4` | `open` | — | Specialisto lytis | — |
| `valstybes_tarnautojas` | `string` | — | `2` | `open` | — | Valstybės tarnautojas | Nurodo, ar specialsitas yra valstybės tarnautojas |

[^manifest]: atviriduomenys/manifest — datasets/gov/hi/specialistai.csv

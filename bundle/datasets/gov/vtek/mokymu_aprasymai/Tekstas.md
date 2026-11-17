---
type: Table
title: "Tekstas — Nuotolinių mokymų aprašymai"
description: "Siekdama padėti deklaruojantiesiems geriau suprasti, kaip taikyti Viešųjų ir privačių interesų derinimo įstatymo nuostatas bei tinkamai deklaruoti interesus, Vyriausioji tarnybinės etikos komisija organizuoja nuotolinius mokymų kursus."
resource: "https://get.data.gov.lt/datasets/gov/vtek/mokymu_aprasymai/Tekstas"
tags: [gov, vtek, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vtek/mokymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/mokymai.csv#L10"
    last_modified: "2026-11-11T14:39:20Z"
---

# Tekstas — Nuotolinių mokymų aprašymai

Siekdama padėti deklaruojantiesiems geriau suprasti, kaip taikyti Viešųjų ir privačių interesų derinimo įstatymo nuostatas bei tinkamai deklaruoti interesus, Vyriausioji tarnybinės etikos komisija organizuoja nuotolinius mokymų kursus. Kursai skirti viešojo sektoriaus darbuotojams bei deklaracijas teikiantiems asmenims. Rinkinyje pateikiami nuotolinių mokymų duomenys.

- **Model:** `datasets/gov/vtek/mokymu_aprasymai/Tekstas`[^manifest]
- **Dataset:** [Nuotolinių mokymų aprašymai](../mokymu_aprasymai.md) (`datasets/gov/vtek/mokymu_aprasymai`)
- **Manifest CSV:** [datasets/gov/vtek/mokymai.csv#L10](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vtek/mokymai.csv#L10)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vtek/mokymu_aprasymai/Tekstas`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės duomenų agentūros įrašo identifikatorius | — |
| `mokymas` | `string` | — | `4` | `open` | — | Mokymų kurso pavadinimas | — |
| `atnaujinimo_data` | `date` | `D` | `4` | `open` | — | Paskutinė teksto atnaujinimo data | — |
| `aprasymas_lt` | `string` | — | `2` | `open` | — | Mokymų aprašymas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `mokymas` | `"Privačių interesų deklaravimas"` | — | — | — | — |
| `mokymas` | `"Lobistinė veikla"` | — | — | — | — |
| `mokymas` | `"Interesų konflikto identifikavimas ir valdymas"` | — | — | — | — |
| `mokymas` | `"Apribojimai pasibaigus tarnybai"` | — | — | — | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `aprasymas_lt` | `update(property: "aprasymas_lt@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vtek/mokymai.csv

---
type: Table
title: "Prasytojas — Duomenys apie prieglobsčio prašytojus"
description: "Spinta table datasets/gov/migracija/prieglobscio_suteikimas/Prasytojas (5 columns)."
resource: "https://get.data.gov.lt/datasets/gov/migracija/prieglobscio_suteikimas/Prasytojas"
tags: [gov, migracija, deployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/migracija/prieglobscio_suteikimas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/prieglobscio_suteikimas.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Prasytojas — Duomenys apie prieglobsčio prašytojus

- **Model:** `datasets/gov/migracija/prieglobscio_suteikimas/Prasytojas`[^manifest]
- **Dataset:** [datasets/gov/migracija/prieglobscio_suteikimas](../prieglobscio_suteikimas.md) (`datasets/gov/migracija/prieglobscio_suteikimas`)
- **Manifest CSV:** [datasets/gov/migracija/prieglobscio_suteikimas.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/prieglobscio_suteikimas.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/prieglobscio_suteikimas/Prasytojas`
- **Primary Key (`ref`):** `id`
- **Level:** `3`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `registracija` | `date` | `D` | `4` | `open` | — | Prašymo prieglobsčiui gauti registracijos data | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis byloje | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Asmens amžiaus grupė pagal gimimo datą, nurodytą byloje | — |
| `pilietybe` | `string` | — | `3` | `open` | — | Asmens pilietybė | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"M"` | — | — | Moteris | — |
| `lytis` | `"V"` | — | — | Vyras | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/prieglobscio_suteikimas.csv

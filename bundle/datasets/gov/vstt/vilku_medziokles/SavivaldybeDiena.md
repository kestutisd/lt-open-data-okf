---
type: Table
title: "SavivaldybeDiena — Statistika apie sumedžiotus vilkus Lietuvos savivaldybėse"
description: "Pateikiama sumedžiotų vilkų statistika savivaldybės ir datos tikslumu."
resource: "https://get.data.gov.lt/datasets/gov/vstt/vilku_medziokles/SavivaldybeDiena"
tags: [gov, vstt, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vstt/medziokles.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/medziokles.csv#L9"
    last_modified: "2026-11-11T14:39:20Z"
---

# SavivaldybeDiena — Statistika apie sumedžiotus vilkus Lietuvos savivaldybėse

Pateikiama sumedžiotų vilkų statistika savivaldybės ir datos tikslumu. Duomenų teikėjas: Valstybinė saugomų teritorijų tarnyba prie Aplinkos ministerijos.

- **Model:** `datasets/gov/vstt/vilku_medziokles/SavivaldybeDiena`[^manifest]
- **Dataset:** [Sumedžioti vilkai Lietuvoje](../vilku_medziokles.md) (`datasets/gov/vstt/vilku_medziokles`)
- **Manifest CSV:** [datasets/gov/vstt/medziokles.csv#L9](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vstt/medziokles.csv#L9)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vstt/vilku_medziokles/SavivaldybeDiena`
- **Primary Key (`ref`):** `vda_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_id` | `string` | — | `4` | `open` | — | Valstybės Duomenų Agentūros įrašo identifikatorius | — |
| `savivaldybe` | `string` | — | `4` | `open` | — | Savivaldybės pavadinimas | — |
| `data` | `date` | `D` | `4` | `open` | — | Medžioklės data | — |
| `sumedziota_vnt` | `integer` | `U` | `4` | `open` | — | Bendras sumedžiotų vilkų skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vstt/medziokles.csv

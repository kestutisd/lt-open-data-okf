---
type: Table
title: "GrazinimasIssiuntimasIpareigojimas"
description: "Spinta table datasets/gov/migracija/deportacijos/GrazinimasIssiuntimasIpareigojimas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/migracija/deportacijos/GrazinimasIssiuntimasIpareigojimas"
tags: [gov, migracija, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/migracija/deportacijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/deportacijos.csv#L5"
    last_modified: "2026-11-11T14:39:20Z"
---

# GrazinimasIssiuntimasIpareigojimas

- **Model:** `datasets/gov/migracija/deportacijos/GrazinimasIssiuntimasIpareigojimas`[^manifest]
- **Dataset:** [datasets/gov/migracija/deportacijos](../deportacijos.md) (`datasets/gov/migracija/deportacijos`)
- **Manifest CSV:** [datasets/gov/migracija/deportacijos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/deportacijos.csv#L5)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/deportacijos/GrazinimasIssiuntimasIpareigojimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `pilietybe` | `string` | — | `2` | `open` | — | Sprendimą gavusio asmens pilietybė | — |
| `sprendimo_registracija` | `date` | `D` | `4` | `open` | — | Sprendimo registracijos data | — |
| `sprendimas` | `string` | — | `3` | `open` | — | Migracijos departamento sprendimas | — |
| `sprendimo_pagrindas` | `string` | — | `2` | `open` | — | Migracijos departamento pagrindas grąžinti, išsiųsti ar įpareigoti | — |
| `poreiksme` | `string` | — | `2` | `open` | — | Sprendimo poreikšmė | — |
| `lytis` | `string` | — | `4` | `open` | — | Lytis byloje | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Sprendimą gavusio asmens amžiaus grupė | — |
| `nurodytas_isvykimas` | `string` | — | `4` | `open` | — | Nurodyta išvykimo šalis | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"M"` | — | — | Moteris | — |
| `lytis` | `"V"` | — | — | Vyras | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pilietybe` | `"update(property: ""pilietybe[]"", type: ""array"", source: ""Pilietybe"")"` | `property` | `4` | — | — | — | — |
| `sprendimo_pagrindas` | `"update(property: ""sprendimo_pagrindas[]"", type: ""array"", source: ""Sprendimo_pagrindas"")"` | `property` | `4` | — | — | — | — |
| `poreiksme` | `"update(property: ""poreiksme[]"", type: ""array"", source: ""Poreiksme"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/deportacijos.csv

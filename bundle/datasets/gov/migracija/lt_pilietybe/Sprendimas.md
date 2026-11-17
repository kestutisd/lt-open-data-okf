---
type: Table
title: "Sprendimas — Sprendimai dėl Lietuvos Respublikos pilietybės suteikimo"
description: "Spinta table datasets/gov/migracija/lt_pilietybe/Sprendimas (7 columns)."
resource: "https://get.data.gov.lt/datasets/gov/migracija/lt_pilietybe/Sprendimas"
tags: [gov, migracija, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/migracija/lt_pilietybe.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/lt_pilietybe.csv#L15"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sprendimas — Sprendimai dėl Lietuvos Respublikos pilietybės suteikimo

- **Model:** `datasets/gov/migracija/lt_pilietybe/Sprendimas`[^manifest]
- **Dataset:** [datasets/gov/migracija/lt_pilietybe](../lt_pilietybe.md) (`datasets/gov/migracija/lt_pilietybe`)
- **Manifest CSV:** [datasets/gov/migracija/lt_pilietybe.csv#L15](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/lt_pilietybe.csv#L15)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/lt_pilietybe/Sprendimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `sprendimo_registracija` | `date` | `D` | `4` | `open` | — | Sprendimo registracijos data | — |
| `sprendimas` | `string` | — | `3` | `open` | — | Migracijos departamento sprendimas dėl Lietuvos Respublikos pilietybės | — |
| `sprendimo_pagrindas` | `string` | — | `3` | `open` | — | Sprendimo pagrindas | — |
| `poreiksme` | `string` | — | `2` | `open` | — | Sprendimo poreikšmė | — |
| `pilietybe` | `string` | — | `2` | `open` | — | Sprendimą gavusio asmens pilietybė | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Sprendimą gavusio asmens amžiaus grupė | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `poreiksme` | `"update(property: ""poreiksme[]"", type: ""array"", source: ""Poreiksme"")"` | `property` | `4` | — | — | — | — |
| `pilietybe` | `"update(property: ""pilietybe[]"", type: ""array"", source: ""Pilietybe"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/lt_pilietybe.csv

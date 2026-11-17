---
type: Table
title: "Sprendimas — Duomenys apie Migracijos departamento sprendimus trečiųjų šalių piliečiams išduoti arba pakeisti leidimą ar pažymėjimą laikinai gyventi Lietuvos Respublikoje"
description: "Spinta table datasets/gov/migracija/teise_gyventi_lr/Sprendimas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/migracija/teise_gyventi_lr/Sprendimas"
tags: [gov, migracija, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/migracija/teise_gyventi_lr.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/teise_gyventi_lr.csv#L19"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sprendimas — Duomenys apie Migracijos departamento sprendimus trečiųjų šalių piliečiams išduoti arba pakeisti leidimą ar pažymėjimą laikinai gyventi Lietuvos Respublikoje

- **Model:** `datasets/gov/migracija/teise_gyventi_lr/Sprendimas`[^manifest]
- **Dataset:** [datasets/gov/migracija/teise_gyventi_lr](../teise_gyventi_lr.md) (`datasets/gov/migracija/teise_gyventi_lr`)
- **Manifest CSV:** [datasets/gov/migracija/teise_gyventi_lr.csv#L19](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/teise_gyventi_lr.csv#L19)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/teise_gyventi_lr/Sprendimas`
- **Primary Key (`ref`):** `id`
- **Level:** `4`
- **Access:** `open`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `sprendimo_registracija` | `date` | `D` | `4` | `open` | — | Sprendimo registracijos data | — |
| `sprendimas` | `string` | — | `3` | `open` | — | Migracijos departamento sprendimas prašytojui | — |
| `pilietybe` | `string` | — | `2` | `open` | — | Sprendimą gavusio asmens pilietybė | — |
| `amziaus_grupe` | `string` | — | `3` | `open` | — | Sprendimą gavusio asmens amžiaus grupė | — |
| `lytis` | `string` | — | `4` | `open` (inherited) | — | Sprendimą gavusio asmens lytis | — |
| `pagrindas` | `string` | — | `3` | `open` | — | Sprendimo pagrindas | — |
| `poreiksme` | `string` | — | `3` | `open` | — | Sprendimo poreikšmė | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"M"` | — | `open` | Moteris | — |
| `lytis` | `"V"` | — | — | Vyras | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pilietybe` | `"update(property: ""pilietybe[]"", type: ""array"", source: ""Pilietybe"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/teise_gyventi_lr.csv

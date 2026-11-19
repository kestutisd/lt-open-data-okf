---
type: Table
title: "GrazinimasIssiuntimasIpareigojimas"
description: "Duomenys apie trečiųjų šalių piliečius, pagal Lietuvos Respublikos įstatymus neteisėtai esančius Lietuvos Respublikoje, taip pat apie neteisėtai Lietuvos Respublikoje esančius trečiųjų šalių piliečius, dėl kurių grąžinimo, išsiuntimo ar įpareigojimo yra priimtas sprendimas ir..."
resource: "https://get.data.gov.lt/datasets/gov/migracija/deportacijos/GrazinimasIssiuntimasIpareigojimas"
tags: [gov, migracija, grazinimasissiuntimasipareigojimas, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/deportacijos.csv#L5"
    title: "atviriduomenys/manifest — datasets/gov/migracija/deportacijos.csv#L5"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1944/"
    title: "data.gov.lt DCAT-AP — datasets/gov/migracija/deportacijos"
    author: "team:vda"
    last_modified: "2025-12-18T00:00:00Z"
---

# GrazinimasIssiuntimasIpareigojimas

**Dataset Context:** Duomenys apie trečiųjų šalių piliečius, pagal Lietuvos Respublikos įstatymus neteisėtai esančius Lietuvos Respublikoje, taip pat apie neteisėtai Lietuvos Respublikoje esančius trečiųjų šalių piliečius, dėl kurių grąžinimo, išsiuntimo ar įpareigojimo yra priimtas sprendimas ir apie trečiųjų šalių piliečius, kurie jau išvyko iš Lietuvos Respublikos pagal sprendimą dėl grąžinimo, išsiuntimo ar įpareigojimo išvykti.[^manifest]

- **Model:** `datasets/gov/migracija/deportacijos/GrazinimasIssiuntimasIpareigojimas`[^manifest]
- **Dataset:** [Duomenys apie sprendimus grąžinti/išsiųsti/įpareigoti](../deportacijos.md) (`datasets/gov/migracija/deportacijos`)[^manifest]
- **Manifest CSV:** [datasets/gov/migracija/deportacijos.csv#L5](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/deportacijos.csv#L5)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/migracija/deportacijos/GrazinimasIssiuntimasIpareigojimas` (`deployed`)[^manifest]
- **Provider:** `migracija` — Migracijos departamentas *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `open`[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2025-12-18`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"M"` | — | — | Moteris | — |
| `lytis` | `"V"` | — | — | Vyras | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pilietybe` | `"update(property: ""pilietybe[]"", type: ""array"", source: ""Pilietybe"")"` | `property` | `4` | — | — | — | — |
| `sprendimo_pagrindas` | `"update(property: ""sprendimo_pagrindas[]"", type: ""array"", source: ""Sprendimo_pagrindas"")"` | `property` | `4` | — | — | — | — |
| `poreiksme` | `"update(property: ""poreiksme[]"", type: ""array"", source: ""Poreiksme"")"` | `property` | `4` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/migracija/deportacijos.csv#L5 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/migracija/deportacijos.csv#L5)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/migracija/deportacijos (https://data.gov.lt/datasets/1944/)

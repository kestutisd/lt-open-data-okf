---
type: Table
title: "AtliekuObjektas"
description: "Spinta table datasets/gov/apva/atlieku_objektai/AtliekuObjektas (16 columns)."
resource: "https://get.data.gov.lt/datasets/gov/apva/atlieku_objektai/AtliekuObjektas"
tags: [gov, apva, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# AtliekuObjektas

- **Model:** `datasets/gov/apva/atlieku_objektai/AtliekuObjektas`[^manifest]
- **Dataset:** [Pabaigtų Atliekų tvarkymo projektų objektų duomenys](../atlieku_objektai.md) (`datasets/gov/apva/atlieku_objektai`)
- **Manifest CSV:** [datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/apva/atlieku_objektai/AtliekuObjektas`
- **Primary Key (`ref`):** `vda_prime_key`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vda_prime_key` | `string` | — | `4` | `open` | — | Unikalus eilutės identifikatorius | — |
| `prj_id` | `string` | — | `4` | `open` | — | Projekto identifikatorius | — |
| `prj_kodas` | `string` | — | `4` | `open` | — | Unikalus projekto kodas | — |
| `programa` | `string` | — | `4` | `open` | — | Programos pavadinimas kurios metu buvo pradėtas vykdyti projektas | — |
| `pavadinimas` | `string` | — | `4` | `open` | — | Objekto pavadinimas | — |
| `tipas` | `string` | — | `4` | `open` | — | Objekto tipas | — |
| `nt_nr` | `string` | — | `4` | `open` | — | Nekilnojamo turto numeris | — |
| `busena` | `string` | — | `4` | `open` | — | Objekto būsena | — |
| `plotas` | `number` | — | `4` | `open` | — | Objekto plotas išreikštas hektarais (ha) | — |
| `pajegumas` | `number` | — | `4` | `open` | — | Objekto pajegumas išreikštas tonomis per metus (t/m) | — |
| `pajegumas_projektinis` | `number` | — | `4` | `open` | — | Objekto numatomas pajegumas išreikštas tonomis per metus (t/m) | — |
| `komentaras` | `string` | — | `4` | `open` | — | Komentaras | — |
| `sav_pav` | `string` | — | `4` | `open` | — | Objekto savivaldybė | — |
| `vda_sav_pav` | `string` | — | `4` | `open` | — | Savivaldybės reikšmė į kurią patenka objekto koordinatės | — |
| `shape_wkt_wgs` | `geometry(4326)` | — | `4` | `open` | — | Objekto wgs-84 koordinatės (wkt reprezentacija) | — |
| `irenginiai` | `string` | — | `4` | `open` | — | Objekte esantys įrenginiai | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `busena` | `"Įrengtas"` | — | — | — | — |
| `busena` | `"Esamas"` | — | — | — | — |
| `busena` | `"Planuojamas"` | — | — | — | — |
| `busena` | `"Įrengiamas"` | — | — | — | — |
| `busena` | `"Neįrengtas"` | — | — | — | — |
| `busena` | `"Nepajungtas"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/apva/baigtu_atlieku_projektu_objektai.csv

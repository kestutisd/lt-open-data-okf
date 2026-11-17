---
type: Table
title: "Dokumentas — Lentelėje pateikti valstybės strategijų, programų dokumentų duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos informacinė sistema (SIS)."
description: "Spinta table datasets/gov/finmin/sis/Dokumentas (10 columns)."
resource: "https://get.data.gov.lt/datasets/gov/finmin/sis/Dokumentas"
tags: [gov, finmin, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/finmin/sis/finmin.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Dokumentas — Lentelėje pateikti valstybės strategijų, programų dokumentų duomenys iš Lietuvos Respublikos finansų ministerijos Stebėsenos informacinė sistema (SIS).

- **Model:** `datasets/gov/finmin/sis/Dokumentas`[^manifest]
- **Dataset:** [datasets/gov/finmin/sis](../sis.md) (`datasets/gov/finmin/sis`)
- **Manifest CSV:** [datasets/gov/finmin/sis/finmin.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/finmin/sis/finmin.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/finmin/sis/Dokumentas`
- **Primary Key (`ref`):** `doc_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `doc_id` | `string` | — | `4` | `open` | — | Įrašo identifikacinis numeris. Generuojamas seka DOC_SEQ. | — |
| `dokumento_kodas` | `string` | — | `4` | `open` | — | Dokumento struktūros identifikacinis numeris. Nuoroda į DOC_STRUCTURES. DCS_ID. | — |
| `dokumento_pavadinimas` | `string` | — | `4` | `open` | — | Dokumento pavadinimas. | — |
| `dokumento_tipas` | `string` | — | `4` | `open` | — | Dokumentų tipo pavadinimas. | — |
| `versija` | `number` | — | `4` | `open` | — | Paskutinės uždarytos dokumento versijos numeris. | — |
| `proceso_etapas` | `string` | — | `4` | `open` | — | Proceso etapas | — |
| `periodas_nuo` | `date` | `D` | `4` | `open` | — | Dokumento galiojimo laikotarpio pradžia | — |
| `periodas_iki` | `date` | `D` | `4` | `open` | — | Dokumento galiojimo laikotarpio pabaiga | — |
| `institucijos_kodas` | `string` | — | `4` | `open` | — | Unikalus institucijos kodas (pirminio šaltinio kodas). | — |
| `institucija` | `string` | — | `4` | `open` | — | Institucijos pavadinimas. | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/finmin/sis/finmin.csv

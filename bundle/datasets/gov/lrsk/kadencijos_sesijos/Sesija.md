---
type: Table
title: "Sesija — Lietuvos Respublikos Seimo sesijų tvarkaraštis"
description: "Lietuvos Respublikos Seimo sesijų tvarkaraštis."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/kadencijos_sesijos/Sesija"
tags: [gov, lrsk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lrsk/kadencijos_sesijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/kadencijos_sesijos.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Sesija — Lietuvos Respublikos Seimo sesijų tvarkaraštis

Lietuvos Respublikos Seimo sesijų tvarkaraštis. Pateikiama eilinių ir neeilinių sesijų pradžia ir pabaiga bei kadencijos, kuriai priklauso sesija, id.

- **Model:** `datasets/gov/lrsk/kadencijos_sesijos/Sesija`[^manifest]
- **Dataset:** [Lietuvos Respublikos Seimo kadencijų ir sesijų klasifikatorius](../kadencijos_sesijos.md) (`datasets/gov/lrsk/kadencijos_sesijos`)
- **Manifest CSV:** [datasets/gov/lrsk/kadencijos_sesijos.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/kadencijos_sesijos.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/kadencijos_sesijos/Sesija`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Sesijos identifikacinis numeris | — |
| `sesija` | `string` | — | `4` | `open` | — | Sesijos pavadinimas | — |
| `sutrump_pav` | `string` | — | `4` | `open` | — | Sutrumpintas sesijos pavadinimas | — |
| `nuo` | `date` | `D` | `4` | `open` | — | Sesijos pradžios data | — |
| `iki` | `date` | `D` | `4` | `open` | — | Sesijos pabaigos data | — |
| `ses_pozm` | `string` | — | `4` | `open` | — | Sesijos požymis: eilinė arba neeilinė | — |
| `kadencija` | `string` | — | `4` | `open` | — | Kadencijos numeris | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `ses_pozm` | `"eilinė"` | — | — | — | — |
| `ses_pozm` | `"neeilinė"` | — | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/kadencijos_sesijos.csv

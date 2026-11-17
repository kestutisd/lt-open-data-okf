---
type: Table
title: "Kadencija — Lietuvos Respublikos Seimo kadencijų tvarkaraštis"
description: "Lietuvos Respublikos Seimo kadencijų tvarkaraštis su kadencijų pradžios ir pabaigos datomis."
resource: "https://get.data.gov.lt/datasets/gov/lrsk/kadencijos_sesijos/Kadencija"
tags: [gov, lrsk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/lrsk/kadencijos_sesijos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/kadencijos_sesijos.csv#L17"
    last_modified: "2026-11-11T14:39:20Z"
---

# Kadencija — Lietuvos Respublikos Seimo kadencijų tvarkaraštis

Lietuvos Respublikos Seimo kadencijų tvarkaraštis su kadencijų pradžios ir pabaigos datomis.

- **Model:** `datasets/gov/lrsk/kadencijos_sesijos/Kadencija`[^manifest]
- **Dataset:** [Lietuvos Respublikos Seimo kadencijų ir sesijų klasifikatorius](../kadencijos_sesijos.md) (`datasets/gov/lrsk/kadencijos_sesijos`)
- **Manifest CSV:** [datasets/gov/lrsk/kadencijos_sesijos.csv#L17](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/lrsk/kadencijos_sesijos.csv#L17)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/lrsk/kadencijos_sesijos/Kadencija`
- **Primary Key (`ref`):** `id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Kadencijos id numeris | — |
| `nuo` | `date` | `D` | `4` | `open` | — | kadencijos pradžios data | — |
| `iki` | `date` | `D` | `4` | `open` | — | kadencijos pabaigos data | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/lrsk/kadencijos_sesijos.csv

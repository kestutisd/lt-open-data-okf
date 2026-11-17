---
type: Table
title: "Archyvas — Utenos rajono savivaldybės administracijos georeferencinių duomenų archyvas"
description: "Spinta table datasets/gov/utenos_r_sav/infoera/Archyvas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/utenos_r_sav/infoera/Archyvas"
tags: [gov, utenos_r_sav, deployed]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/utenos_r_sav/infoera.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/utenos_r_sav/infoera.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Archyvas — Utenos rajono savivaldybės administracijos georeferencinių duomenų archyvas

- **Model:** `datasets/gov/utenos_r_sav/infoera/Archyvas`[^manifest]
- **Dataset:** [Utenos rajono savivaldybės administracijos georeferencinių duomenų sistema](../infoera.md) (`datasets/gov/utenos_r_sav/infoera`)
- **Manifest CSV:** [datasets/gov/utenos_r_sav/infoera.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/utenos_r_sav/infoera.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/utenos_r_sav/infoera/Archyvas`
- **Primary Key (`ref`):** `id`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | — | `open` | — | Archyvuoto darbo ID | — |
| `darbo_tipas` | `string` | — | — | `open` | — | Archyvuoto darbo tipas | — |
| `darbo_tipas_klasifikatorius` | `string` | — | `4` | `open` | — | Darbo tipo klasifikatorius iš Infoera dokumentacijos | — |
| `atlikto_darbo_data` | `date` | `D` | `4` | `open` | — | Archyvuoto darbo data | — |
| `atlikto_darbo_failo_data` | `date` | `D` | `4` | `open` | — | Archyvuoto darbo failo data | — |
| `reg_nr` | `string` | — | `4` | `open` | — | Archyvinio darbo registracijos numeris | — |
| `darbo_vykdytojas` | `string` | — | `4` | `open` | — | Geodezinio darbo vykdytojas | — |
| `geometry` | `string` | — | `4` | `open` | — | Archyvuoto darbo geometrija LKS koordinatėse | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `darbo_tipas` | `"1"` | — | — | Topografinė nuotrauka | — |
| `darbo_tipas` | `"2"` | — | — | Kontrolinė geodezinė nuotrauka | — |
| `darbo_tipas` | `"3"` | — | — | Sklypo planas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/utenos_r_sav/infoera.csv

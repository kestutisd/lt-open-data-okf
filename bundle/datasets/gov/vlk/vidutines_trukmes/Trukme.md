---
type: Table
title: "Trukme — Vidutinė hospitalizuotų pacientų terapijos, chirurgijos ir psichiatrijos paslaugų grupių gydymo trukmė įstaigoje"
description: "Informacija apie vidutinę hospitalizuotų pacientų terapijos, chirurgijos ir psichiatrijos paslaugų grupių gydymo trukmę įstaigoje"
resource: "https://get.data.gov.lt/datasets/gov/vlk/vidutines_trukmes/Trukme"
tags: [gov, vlk, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/vlk/vidutines_trukmes.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/vidutines_trukmes.csv#L6"
    last_modified: "2026-11-11T14:39:20Z"
---

# Trukme — Vidutinė hospitalizuotų pacientų terapijos, chirurgijos ir psichiatrijos paslaugų grupių gydymo trukmė įstaigoje

Informacija apie vidutinę hospitalizuotų pacientų terapijos, chirurgijos ir psichiatrijos paslaugų grupių gydymo trukmę įstaigoje

- **Model:** `datasets/gov/vlk/vidutines_trukmes/Trukme`[^manifest]
- **Dataset:** [datasets/gov/vlk/vidutines_trukmes](../vidutines_trukmes.md) (`datasets/gov/vlk/vidutines_trukmes`)
- **Manifest CSV:** [datasets/gov/vlk/vidutines_trukmes.csv#L6](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/vlk/vidutines_trukmes.csv#L6)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/vlk/vidutines_trukmes/Trukme`
- **Primary Key (`ref`):** `ad_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `ad_id` | `integer` | — | `4` | `open` | — | Unikalus identifikatorius | — |
| `metai` | `integer` | — | `2` | `open` | — | Metai | — |
| `istg_id` | `ref` | [/datasets/gov/vlk/istaigos/Istaiga](../istaigos/Istaiga.md) | `4` | `open` | — | Įstaigos ID | Įstaigos, kuri suteikė paslaugas, ID |
| `grupe` | `string` | — | `3` | `open` | — | Paslaugos grupė | — |
| `vid_trukme` | `number` | `U` | `4` | `open` | — | Vidutinė trukmė dienomis | — |
| `lovadieniai` | `number` | `U` | `4` | `open` | — | Lovadienių skaičius | — |
| `atvejai` | `number` | `U` | `4` | `open` | — | Atvejų (etapų) skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `metai` | `update(type: "date", ref: "Y")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/vlk/vidutines_trukmes.csv

---
type: Table
title: "Bokstas — Sluoksnyje saugoma informacija apie atskirai stovinčius bokštus ir kaminus, kurie negali būti išreikšti plotu"
description: "Spinta table datasets/gov/giscentras/grpk/Bokstas (8 columns)."
resource: "https://get.data.gov.lt/datasets/gov/giscentras/grpk/Bokstas"
tags: [gov, giscentras, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L201"
    last_modified: "2026-11-11T14:39:20Z"
---

# Bokstas — Sluoksnyje saugoma informacija apie atskirai stovinčius bokštus ir kaminus, kurie negali būti išreikšti plotu

- **Model:** `datasets/gov/giscentras/grpk/Bokstas`[^manifest]
- **Dataset:** [Georeferencinio pagrindo kadastro erdviniai duomenys](../grpk.md) (`datasets/gov/giscentras/grpk`)
- **Manifest CSV:** [datasets/gov/giscentras/grpk.csv#L201](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L201)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/giscentras/grpk/Bokstas`
- **Primary Key (`ref`):** `top_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `top_id` | `string` | — | `4` | `open` | — | Objekto identifikavimo kodas (reikšmė yra privaloma) | — |
| `gkodas` | `string` | — | `4` | `open` | — | Erdvinio objekto kodas (reikšmė yra privaloma) | — |
| `meta` | `string` | — | `4` | `open` | — | Raktas į GRPK rinkinio sluoksnio metaduomenų lenteles | — |
| `red_priezastis` | `string` | — | `4` | `open` | — | Objekto duomenų ir informacijos sukūrimo ar paskutinio pakeitimo priežastis (reikšmė yra privaloma įvedus naują ar patikslinus esamo objekto duomenis ir informaciją) | — |
| `red_saltinis` | `string` | — | `4` | `open` | — | Objekto duomenims sukurti, nustatyti ar pakeisti naudotas duomenų šaltinis. Galimos reikšmės | — |
| `suk_data` | `datetime` | `L` | `4` | `open` | — | Objekto įregistravimo (sukūrimo) data (reikšmė yra privaloma) | — |
| `red_data` | `datetime` | `L` | `4` | `open` | — | Objekto duomenų ir informacijos keitimo data (reikšmė yra privaloma patikslinus esamo objekto duomenis ir informaciją) | — |
| `shape` | `geometry(point, 3346)` | — | `4` | `open` | — | Objekto geometrijos tipas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gkodas` | `"pa6"` | — | — | Atskirai stovintys bokštai, kaminai | — |
| `gkodas` | `"pa651"` | — | — | Vėjo malūnai | — |
| `gkodas` | `"pa652"` | — | — | Kitos vėjo jėgainės | — |
| `gkodas` | `"pa67"` | — | — | Apžvalgos bokštai (išskyrus miško stebėjimo bokštus) | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv

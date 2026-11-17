---
type: Table
title: "MiskasRiba — Sluoksnyje saugoma informacija apie miškų kvartalinių linijų ir proskynų ašines linijas, taip pat medžių juostas"
description: "Spinta table datasets/gov/giscentras/grpk/MiskasRiba (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/giscentras/grpk/MiskasRiba"
tags: [gov, giscentras, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L323"
    last_modified: "2026-11-11T14:39:20Z"
---

# MiskasRiba — Sluoksnyje saugoma informacija apie miškų kvartalinių linijų ir proskynų ašines linijas, taip pat medžių juostas

- **Model:** `datasets/gov/giscentras/grpk/MiskasRiba`[^manifest]
- **Dataset:** [Georeferencinio pagrindo kadastro erdviniai duomenys](../grpk.md) (`datasets/gov/giscentras/grpk`)
- **Manifest CSV:** [datasets/gov/giscentras/grpk.csv#L323](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L323)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/giscentras/grpk/MiskasRiba`
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
| `shape_length` | `number` | `m` | `4` | `open` | — | Objekto perimetro ilgis | — |
| `shape` | `geometry(multilinestring, 3346)` | — | `4` | `open` | — | Objekto geometrijos tipas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gkodas` | `"lp3"` | — | — | 1–10 m pločio miško kvartalinių linijų ir proskynų ašinės linijos | — |
| `gkodas` | `"mj0"` | — | — | Medžių juosta – ne trumpesnė kaip 100 m išilgai kelio, geležinkelio ar kanalo einanti medžių juosta (ne miestų ir miestelių teritorijose), kurios paprastai apima vieną eilę medžių | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv

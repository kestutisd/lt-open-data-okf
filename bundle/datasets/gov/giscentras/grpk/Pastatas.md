---
type: Table
title: "Pastatas — Sluoksnyje saugoma informacija apie aiškiai atpažįstamų pastatų ir statinių dengiamą teritoriją"
description: "Spinta table datasets/gov/giscentras/grpk/Pastatas (11 columns)."
resource: "https://get.data.gov.lt/datasets/gov/giscentras/grpk/Pastatas"
tags: [gov, giscentras, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L182"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pastatas — Sluoksnyje saugoma informacija apie aiškiai atpažįstamų pastatų ir statinių dengiamą teritoriją

- **Model:** `datasets/gov/giscentras/grpk/Pastatas`[^manifest]
- **Dataset:** [Georeferencinio pagrindo kadastro erdviniai duomenys](../grpk.md) (`datasets/gov/giscentras/grpk`)
- **Manifest CSV:** [datasets/gov/giscentras/grpk.csv#L182](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L182)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/giscentras/grpk/Pastatas`
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
| `pask` | `string` | — | `4` | `open` | — | Pastato pagrindinė naudojimo paskirtis, kuri nustatoma vadovaujantis Nekilnojamojo turto kadastro duomenimis | — |
| `shape_length` | `number` | `m` | `4` | `open` | — | Objekto perimetro ilgis | — |
| `shape_area` | `number` | `m²` | `4` | `open` | — | Objekto plotas | — |
| `shape` | `geometry(multipolygon, 3346)` | — | `4` | `open` | — | Objekto geometrijos tipas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gkodas` | `"pa0"` | — | — | Pastatai – apdengti stogu statiniai, kurių didžiausią dalį sudaro patalpos | — |
| `gkodas` | `"pa23"` | — | — | Garažai – pastatai, skirti transporto priemonėms laikyti ir remontuoti | — |
| `gkodas` | `"pa58"` | — | — | Šiltnamiai – pramoniniams augalams auginti skirti dengti daržai | — |
| `gkodas` | `"pa6"` | — | — | Bokštinio tipo statiniai (vandentiekio ir siloso bokštai, aušinimo bokštai, ugniagesių bokštai, cisternos, naftos ir dujų rezervuarai, kt.) | — |
| `gkodas` | `"pa651"` | — | — | Vėjo malūnai | — |
| `gkodas` | `"pa652"` | — | — | Kitos vėjo jėgainės | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv

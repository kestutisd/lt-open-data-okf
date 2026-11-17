---
type: Table
title: "Plotas — Sluoksnyje saugoma informacija apie vandens telkinių dengiamas teritorijas"
description: "Spinta table datasets/gov/giscentras/grpk/Plotas (13 columns)."
resource: "https://get.data.gov.lt/datasets/gov/giscentras/grpk/Plotas"
tags: [gov, giscentras, deployed, level-4]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L141"
    last_modified: "2026-11-11T14:39:20Z"
---

# Plotas — Sluoksnyje saugoma informacija apie vandens telkinių dengiamas teritorijas

- **Model:** `datasets/gov/giscentras/grpk/Plotas`[^manifest]
- **Dataset:** [Georeferencinio pagrindo kadastro erdviniai duomenys](../grpk.md) (`datasets/gov/giscentras/grpk`)
- **Manifest CSV:** [datasets/gov/giscentras/grpk.csv#L141](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L141)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/giscentras/grpk/Plotas`
- **Primary Key (`ref`):** `top_id`
- **Level:** `4`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `top_id` | `string` | — | `4` | `open` | — | Objekto identifikavimo kodas (reikšmė yra privaloma) | — |
| `gkodas` | `string` | — | `4` | `open` | — | Erdvinio objekto kodas (reikšmė yra privaloma) | GKODAS - 13 lentelė, https://e-tar.lt/portal/lt/legalAct/c53d28609d7811eea5a28c81c82193a8 |
| `meta` | `string` | — | `4` | `open` | — | Raktas į GRPK rinkinio sluoksnio metaduomenų lenteles | — |
| `red_priezastis` | `string` | — | `4` | `open` | — | Objekto duomenų ir informacijos sukūrimo ar paskutinio pakeitimo priežastis (reikšmė yra privaloma įvedus naują ar patikslinus esamo objekto duomenis ir informaciją) | — |
| `red_saltinis` | `string` | — | `4` | `open` | — | Objekto duomenims sukurti, nustatyti ar pakeisti naudotas duomenų šaltinis. Galimos reikšmės | — |
| `suk_data` | `datetime` | `L` | `4` | `open` | — | Objekto įregistravimo (sukūrimo) data (reikšmė yra privaloma) | — |
| `red_data` | `datetime` | `L` | `4` | `open` | — | Objekto duomenų ir informacijos keitimo data (reikšmė yra privaloma patikslinus esamo objekto duomenis ir informaciją) | — |
| `graktas` | `string` | — | `4` | `open` | — | Tvenkinio kodas pagal Lietuvos Respublikos tvenkinių klasifikatorių arba ežero kodas pagal Lietuvos Respublikos ežerų klasifikatorių | — |
| `vardas` | `string` | — | `4` | `open` | — | Objekto pavadinimas | — |
| `info` | `string` | — | `4` | `open` | — | Papildoma informacija apie objektą | — |
| `shape_length` | `number` | `m` | `4` | `open` | — | Objekto perimetro ilgis | — |
| `shape_area` | `number` | `m²` | `4` | `open` | — | Objekto plotas | — |
| `shape` | `string` | — | `4` | `open` | — | Objekto geometrijos tipas | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `vardas` | `update(property: "vardas@lt", type: "text")` | `type` | `4` | `open` | — | — | — |
| `info` | `update(property: "info@lt", type: "text")` | `type` | `4` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv

---
type: Table
title: "EzerasTvenkinys — Ežerai ir tvenkiniai"
description: "Spinta table datasets/gov/aaa/ezerai_tvenkiniai/EzerasTvenkinys (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/ezerai_tvenkiniai/EzerasTvenkinys"
tags: [gov, aaa, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/aaa/ezerai_tvenkiniai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/ezerai_tvenkiniai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# EzerasTvenkinys — Ežerai ir tvenkiniai

- **Model:** `datasets/gov/aaa/ezerai_tvenkiniai/EzerasTvenkinys`[^manifest]
- **Dataset:** [datasets/gov/aaa/ezerai_tvenkiniai](../ezerai_tvenkiniai.md) (`datasets/gov/aaa/ezerai_tvenkiniai`)
- **Manifest CSV:** [datasets/gov/aaa/ezerai_tvenkiniai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/ezerai_tvenkiniai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/ezerai_tvenkiniai/EzerasTvenkinys`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `pavadinimas` | `string` | — | `4` | `open` | — | Ežero/tvenkinio pavadinimas | — |
| `registruota` | `date` | `D` | `4` | `open` | — | Kadastro objekto registravimo data | Metai, mėnuo, diena, laikas |
| `redaguota` | `date` | `D` | `4` | `open` | — | Kadastro objekto redagavimo data | Metai, mėnuo, diena, laikas |
| `koord` | `geometry(point, 3346)` | `m` | `4` | `open` | — | Objekto centro koordinatė | LKS-94 koordinačių sistemoje, metrais |
| `pav_plotas` | `number` | `ha` | `4` | `open` | — | Vandens paviršiaus plotas Lietuvos teritorijoje geografinis | — |
| `kadastroid` | `string` | — | `4` | `open` | — | Kadastro identifikavimo kodas | — |
| `kategorija` | `integer` | — | `4` | `open` | — | Objekto kategorijos pavadinimo kodas | — |
| `kvadrato_nr` | `integer` | — | `4` | `open` | — | Ežero kvadrato numeris | Kvadratas – Lietuvos ežerų schemoje, sudarytoje Respublikinio žemėtvarkos projektavimo instituto 1964 metais, išskirtas plotas ežero numeriui suteikti. |
| `nr_kvadrate` | `integer` | — | `4` | `open` | — | Ežero numeris kvadrate | — |
| `rusis` | `integer` | — | `4` | `open` | — | Ežero rūšis | — |
| `ilgis` | `number` | `km` | `4` | `open` | — | Ežero, tvenkinio ilgis | — |
| `plotis` | `number` | `km` | `4` | `open` | — | Ežero, tvenkinio vidutinis plotis | — |
| `linijos_ilgis` | `number` | `km` | `4` | `open` | — | Kranto linijos ilgis geografinis | — |
| `ubr_kodas` | `string` | — | `4` | `open` | — | Upės pabaseinio arba baseino, kuriame yra vandens objektas, kodas | — |
| `vyrupes_uid` | `string` | — | `4` | `open` | — | Tiesioginės upės unikalus identifikatorius | — |
| `kiti_duomenys` | `string` | — | `2` | `open` | — | Kiti duomenys | — |
| `shape` | `geometry(3346)` | — | `4` | `open` | — | Geometrinis primityvas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `kategorija` | `1` | — | — | Upė | — |
| `kategorija` | `2` | — | — | Kanalas | — |
| `kategorija` | `3` | — | — | Natūralus ežeras | — |
| `kategorija` | `4` | — | — | Užtvenktas ežeras | — |
| `kategorija` | `5` | — | — | Tvenkinys | — |
| `kategorija` | `6` | — | — | Dirbtinis nepratekamas paviršinio vandens telkinys | — |
| `kategorija` | `7` | — | — | Tarpinis vandens telkinys | — |
| `kategorija` | `8` | — | — | Pakrantės vandens telkinys | — |
| `kategorija` | `9` | — | — | Teritorinis vandens telkinys | — |
| `rusis` | `1` | — | — | Lašišinis | — |
| `rusis` | `2` | — | — | Potencialiai lašišinis | — |
| `rusis` | `3` | — | — | Karpinis | — |
| `rusis` | `4` | — | — | Ešerinis | — |
| `rusis` | `5` | — | — | Karosinis | — |
| `rusis` | `6` | — | — | Karšinis | — |
| `rusis` | `7` | — | — | Kuojinis | — |
| `rusis` | `8` | — | — | Lydekinis | — |
| `rusis` | `9` | — | — | Lyninis | — |
| `rusis` | `10` | — | — | Seliavinis | — |
| `rusis` | `11` | — | — | Sterkinis | — |
| `rusis` | `12` | — | — | Stintinis | — |
| `rusis` | `13` | — | — | Kitas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/ezerai_tvenkiniai.csv

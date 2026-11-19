---
type: Table
title: "EzerasTvenkinys — Ežerai ir tvenkiniai"
description: "Spinta table datasets/gov/aaa/ezerai_tvenkiniai/EzerasTvenkinys (17 columns)."
resource: "https://get.data.gov.lt/datasets/gov/aaa/ezerai_tvenkiniai/EzerasTvenkinys"
tags: [gov, aaa, ezerastvenkinys, deployed, level-2, cadence-annual]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/ezerai_tvenkiniai.csv#L4"
    title: "atviriduomenys/manifest — datasets/gov/aaa/ezerai_tvenkiniai.csv#L4"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1049/"
    title: "data.gov.lt DCAT-AP — datasets/gov/aaa/ezerai_tvenkiniai"
    author: "team:vda"
    last_modified: "2026-01-05T00:00:00Z"
---

# EzerasTvenkinys — Ežerai ir tvenkiniai

- **Model:** `datasets/gov/aaa/ezerai_tvenkiniai/EzerasTvenkinys`[^manifest]
- **Dataset:** [Ežerų, tvenkinių ir dirbtinių nepratekamų paviršinio vandens telkinių duomenys](../ezerai_tvenkiniai.md) (`datasets/gov/aaa/ezerai_tvenkiniai`)[^manifest]
- **Manifest CSV:** [datasets/gov/aaa/ezerai_tvenkiniai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/ezerai_tvenkiniai.csv#L4)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/aaa/ezerai_tvenkiniai/EzerasTvenkinys` (`deployed`)[^manifest]
- **Provider:** `aaa` — Aplinkos apsaugos agentūra *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `— (_id UUID)`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `ANNUAL`, Modified `2026-01-05`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
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

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/aaa/ezerai_tvenkiniai.csv#L4 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/aaa/ezerai_tvenkiniai.csv#L4)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/aaa/ezerai_tvenkiniai (https://data.gov.lt/datasets/1049/)

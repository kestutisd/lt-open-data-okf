---
type: Table
title: "MiskasRiba — Sluoksnyje saugoma informacija apie miškų kvartalinių linijų ir proskynų ašines linijas, taip pat medžių juostas"
description: "Specifikacija - https://e-tar.lt/portal/lt/legalAct/c53d28609d7811eea5a28c81c82193a8"
resource: "https://get.data.gov.lt/datasets/gov/giscentras/grpk/MiskasRiba"
tags: [gov, giscentras, miskasriba, deployed, level-4, cadence-monthly]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L323"
    title: "atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv#L323"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
  - id: dcat
    resource: "https://data.gov.lt/datasets/1302/"
    title: "data.gov.lt DCAT-AP — datasets/gov/giscentras/grpk"
    author: "team:vda"
    last_modified: "2026-04-07T00:00:00Z"
---

# MiskasRiba — Sluoksnyje saugoma informacija apie miškų kvartalinių linijų ir proskynų ašines linijas, taip pat medžių juostas

**Dataset Context:** Specifikacija - https://e-tar.lt/portal/lt/legalAct/c53d28609d7811eea5a28c81c82193a8[^manifest]

- **Model:** `datasets/gov/giscentras/grpk/MiskasRiba`[^manifest]
- **Dataset:** [Georeferencinio pagrindo kadastro erdviniai duomenys](../grpk.md) (`datasets/gov/giscentras/grpk`)[^manifest]
- **Manifest CSV:** [datasets/gov/giscentras/grpk.csv#L323](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L323)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/giscentras/grpk/MiskasRiba` (`deployed`)[^manifest]
- **Provider:** `giscentras` — VĮ Žemės ūkio duomenų centras (buv. VĮ „GIS-Centras“) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `top_id`[^manifest]
- **Level:** `4`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]
- **Portal Cadence & License (DCAT-AP):** Periodicity `MONTHLY`, Modified `2026-04-07`, License `https://creativecommons.org/licenses/by/4.0/deed.lt`[^dcat]

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

| Property | Value (prepare) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `gkodas` | `"lp3"` | — | — | 1–10 m pločio miško kvartalinių linijų ir proskynų ašinės linijos | — |
| `gkodas` | `"mj0"` | — | — | Medžių juosta – ne trumpesnė kaip 100 m išilgai kelio, geležinkelio ar kanalo einanti medžių juosta (ne miestų ir miestelių teritorijose), kurios paprastai apima vieną eilę medžių | — |

# Related References

- [AR Address Hierarchy & LKS-94 Reference](../../../../references/joins/ar-address-hierarchy.md) — Administrative hierarchy (`Apskritis` -> `Patalpa`) and `EPSG:3346` vs `EPSG:4326` coordinates.

[^manifest]: atviriduomenys/manifest — datasets/gov/giscentras/grpk.csv#L323 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/giscentras/grpk.csv#L323)
[^dcat]: data.gov.lt DCAT-AP — datasets/gov/giscentras/grpk (https://data.gov.lt/datasets/1302/)

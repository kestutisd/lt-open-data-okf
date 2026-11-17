---
type: Table
title: "GalvijuLikvidavimas — Galvijų likvidavimai"
description: "Spinta table datasets/gov/zuikvc/galviju_likvidavimai/GalvijuLikvidavimas (12 columns)."
tags: [gov, zuikvc, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/galviju_likvidavimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galviju_likvidavimai.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# GalvijuLikvidavimas — Galvijų likvidavimai

- **Model:** `datasets/gov/zuikvc/galviju_likvidavimai/GalvijuLikvidavimas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/galviju_likvidavimai](../galviju_likvidavimai.md) (`datasets/gov/zuikvc/galviju_likvidavimai`)
- **Manifest CSV:** [datasets/gov/zuikvc/galviju_likvidavimai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galviju_likvidavimai.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `savivaldybe`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Gyvūno bandos savivaldybės pavadinimas | — |
| `bul_iki_8` | `integer` | `U` | `4` | `open` | — | Likviduotų bulių iki 8 mėnesių amžiaus skaičius | — |
| `bul_virs_8` | `integer` | `U` | `4` | `open` | — | Likviduotų bulių virš 8 mėnesių amžiaus skaičius | — |
| `tel_iki_8` | `integer` | `U` | `4` | `open` | — | Likviduotų telyčių iki 8 mėnesių amžiaus skaičius | — |
| `tel_virs_8` | `integer` | `U` | `4` | `open` | — | Likviduotų telyčių virš 8 mėnesių amžiaus skaičius | — |
| `karv` | `integer` | `U` | `4` | `open` | — | Likviduotų karvių skaičius | — |
| `bul_iki_8_im` | `integer` | `U` | `4` | `open` | — | Skerdimo įmonėse paskerstų bulių iki 8 mėnesių amžiaus skaičius | — |
| `bul_virs_8_im` | `integer` | `U` | `4` | `open` | — | Skerdimo įmonėse paskerstų bulių virš 8 mėnesių amžiaus skaičius | — |
| `tel_iki_8_im` | `integer` | `U` | `4` | `open` | — | Skerdimo įmonėse paskerstų telyčių iki 8 mėnesių amžiaus skaičius | — |
| `tel_virs_8_im` | `integer` | `U` | `4` | `open` | — | Skerdimo įmonėse paskerstų telyčių virš 8 mėnesių amžiaus skaičius | — |
| `karv_im` | `integer` | `U` | `4` | `open` | — | Skerdimo įmonėse paskerstų karvių skaičius | — |
| `galv_uzs_im` | `integer` | `U` | `4` | `open` | — | Skerdimo įmonėse paskerstų galvijų iš užsienio skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/galviju_likvidavimai.csv

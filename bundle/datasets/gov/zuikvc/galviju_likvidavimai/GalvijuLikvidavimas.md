---
type: Table
title: "GalvijuLikvidavimas — Galvijų likvidavimai"
description: "Spinta table datasets/gov/zuikvc/galviju_likvidavimai/GalvijuLikvidavimas (12 columns)."
tags: [gov, zuikvc, galvijulikvidavimas, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galviju_likvidavimai.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/galviju_likvidavimai.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# GalvijuLikvidavimas — Galvijų likvidavimai

- **Model:** `datasets/gov/zuikvc/galviju_likvidavimai/GalvijuLikvidavimas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/galviju_likvidavimai](../galviju_likvidavimai.md) (`datasets/gov/zuikvc/galviju_likvidavimai`)[^manifest]
- **Manifest CSV:** [datasets/gov/zuikvc/galviju_likvidavimai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galviju_likvidavimai.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `zuikvc` — VĮ Žemės ūkio duomenų centras (buv. VĮ Žemės ūkio informacijos ir kaimo verslo centras) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `savivaldybe`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/galviju_likvidavimai.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galviju_likvidavimai.csv#L8)

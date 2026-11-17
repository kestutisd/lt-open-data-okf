---
type: Table
title: "GalvijuLyciuAmziausPasiskirstymas — Galvijų pasiskirstymas pagal lytis ir amžiaus grupes"
description: "Spinta table datasets/gov/zuikvc/galvijai_lytys_amzius/GalvijuLyciuAmziausPasiskirstymas (9 columns)."
tags: [gov, zuikvc, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/galvijai_lytys_amzius.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galvijai_lytys_amzius.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# GalvijuLyciuAmziausPasiskirstymas — Galvijų pasiskirstymas pagal lytis ir amžiaus grupes

- **Model:** `datasets/gov/zuikvc/galvijai_lytys_amzius/GalvijuLyciuAmziausPasiskirstymas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/galvijai_lytys_amzius](../galvijai_lytys_amzius.md) (`datasets/gov/zuikvc/galvijai_lytys_amzius`)
- **Manifest CSV:** [datasets/gov/zuikvc/galvijai_lytys_amzius.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galvijai_lytys_amzius.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `savivaldybe`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Gyvūno bandos savivaldybės pavadinimas | — |
| `bul_0_8` | `integer` | `U` | `4` | `open` | — | Bulių iki 8 mėnesių amžiaus skaičius | — |
| `tel_0_8` | `integer` | `U` | `4` | `open` | — | Telyčių iki 8 mėnesių amžiaus skaičius | — |
| `bul_8_12` | `integer` | `U` | `4` | `open` | — | Bulių nuo 8 iki 12 mėnesių amžiaus skaičius | — |
| `tel_8_12` | `integer` | `U` | `4` | `open` | — | Telyčių nuo 8 iki 12 mėnesių amžiaus skaičius | — |
| `bul_12_24` | `integer` | `U` | `4` | `open` | — | Bulių nuo 12 iki 24 mėnesių amžiaus skaičius | — |
| `tel_12_24` | `integer` | `U` | `4` | `open` | — | Telyčių nuo 12 iki 24 mėnesių amžiaus skaičius | — |
| `bul_24` | `integer` | `U` | `4` | `open` | — | Bulių virš 24 mėnesių amžiaus skaičius | — |
| `tel_24` | `integer` | `U` | `4` | `open` | — | Telyčių virš 24 mėnesių amžiaus skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/galvijai_lytys_amzius.csv

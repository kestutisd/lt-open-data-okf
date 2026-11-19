---
type: Table
title: "GalvijuLyciuAmziausPasiskirstymas — Galvijų pasiskirstymas pagal lytis ir amžiaus grupes"
description: "Spinta table datasets/gov/zuikvc/galvijai_lytys_amzius/GalvijuLyciuAmziausPasiskirstymas (9 columns)."
tags: [gov, zuikvc, galvijulyciuamziauspasiskirstymas, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galvijai_lytys_amzius.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/galvijai_lytys_amzius.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# GalvijuLyciuAmziausPasiskirstymas — Galvijų pasiskirstymas pagal lytis ir amžiaus grupes

- **Model:** `datasets/gov/zuikvc/galvijai_lytys_amzius/GalvijuLyciuAmziausPasiskirstymas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/galvijai_lytys_amzius](../galvijai_lytys_amzius.md) (`datasets/gov/zuikvc/galvijai_lytys_amzius`)[^manifest]
- **Manifest CSV:** [datasets/gov/zuikvc/galvijai_lytys_amzius.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galvijai_lytys_amzius.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `zuikvc` — VĮ Žemės ūkio duomenų centras (buv. VĮ Žemės ūkio informacijos ir kaimo verslo centras) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `savivaldybe`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | ﻿Gyvūno bandos savivaldybės pavadinimas | — |
| `bul_0_8` | `integer` | `U` | `4` | `open` | — | Bulių iki 8 mėnesių amžiaus skaičius | — |
| `tel_0_8` | `integer` | `U` | `4` | `open` | — | Telyčių iki 8 mėnesių amžiaus skaičius | — |
| `bul_8_12` | `integer` | `U` | `4` | `open` | — | Bulių nuo 8 iki 12 mėnesių amžiaus skaičius | — |
| `tel_8_12` | `integer` | `U` | `4` | `open` | — | Telyčių nuo 8 iki 12 mėnesių amžiaus skaičius | — |
| `bul_12_24` | `integer` | `U` | `4` | `open` | — | Bulių nuo 12 iki 24 mėnesių amžiaus skaičius | — |
| `tel_12_24` | `integer` | `U` | `4` | `open` | — | Telyčių nuo 12 iki 24 mėnesių amžiaus skaičius | — |
| `bul_24` | `integer` | `U` | `4` | `open` | — | Bulių virš 24 mėnesių amžiaus skaičius | — |
| `tel_24` | `integer` | `U` | `4` | `open` | — | Telyčių virš 24 mėnesių amžiaus skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/galvijai_lytys_amzius.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galvijai_lytys_amzius.csv#L8)

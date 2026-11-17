---
type: Table
title: "GyvuliuEksportas — Gyvulių eksportas"
description: "Spinta table datasets/gov/zuikvc/gyvuliu_eksportas/GyvuliuEksportas (8 columns)."
tags: [gov, zuikvc, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/gyvuliu_eksportas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/gyvuliu_eksportas.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# GyvuliuEksportas — Gyvulių eksportas

- **Model:** `datasets/gov/zuikvc/gyvuliu_eksportas/GyvuliuEksportas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/gyvuliu_eksportas](../gyvuliu_eksportas.md) (`datasets/gov/zuikvc/gyvuliu_eksportas`)
- **Manifest CSV:** [datasets/gov/zuikvc/gyvuliu_eksportas.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/gyvuliu_eksportas.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `valstybe`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `valstybe` | `string` | — | `2` | `open` | — | Valstybės pavadinimas | — |
| `buliai_iki_8_men` | `integer` | `U` | `4` | `open` | — | Eksportuotų bulių iki 8 mėnesių amžiaus skaičius | — |
| `telycios_iki_8_men` | `integer` | `U` | `4` | `open` | — | Eksportuotų telyčių iki 8 mėnesių amžiaus skaičius | — |
| `buliai_virs_8_men` | `integer` | `U` | `4` | `open` | — | Eksportuotų bulių virš 8 mėnesių amžiaus skaičius | — |
| `telycios_virs_8_men` | `integer` | `U` | `4` | `open` | — | Eksportuotų telyčių virš 8 mėnesių amžiaus skaičius | — |
| `karves` | `integer` | `U` | `4` | `open` | — | Eksportuotų karvių skaičius | — |
| `avys` | `integer` | `U` | `4` | `open` | — | Eksportuotų avių skaičius | — |
| `arkliai` | `integer` | `U` | `4` | `open` | — | Eksportuotų arklių skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/gyvuliu_eksportas.csv

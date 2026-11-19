---
type: Table
title: "GyvuliuEksportas — Gyvulių eksportas"
description: "Spinta table datasets/gov/zuikvc/gyvuliu_eksportas/GyvuliuEksportas (8 columns)."
tags: [gov, zuikvc, gyvuliueksportas, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.3.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/gyvuliu_eksportas.csv#L8"
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/gyvuliu_eksportas.csv#L8"
    author: "team:vssa"
    last_modified: "2026-11-11T14:39:20Z"
---

# GyvuliuEksportas — Gyvulių eksportas

- **Model:** `datasets/gov/zuikvc/gyvuliu_eksportas/GyvuliuEksportas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/gyvuliu_eksportas](../gyvuliu_eksportas.md) (`datasets/gov/zuikvc/gyvuliu_eksportas`)[^manifest]
- **Manifest CSV:** [datasets/gov/zuikvc/gyvuliu_eksportas.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/gyvuliu_eksportas.csv#L8)[^manifest]
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in` (undeployed — HTTP 404 on `get.data.gov.lt`)[^manifest]
- **Provider:** `zuikvc` — VĮ Žemės ūkio duomenų centras (buv. VĮ Žemės ūkio informacijos ir kaimo verslo centras) *(resolved from institutional code)*[^manifest]
- **Primary Key (`ref`):** `valstybe`[^manifest]
- **Level:** `2`[^manifest]
- **Access:** `—` *(determined by column access in `# Schema`)*[^manifest]

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

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/gyvuliu_eksportas.csv#L8 (https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/gyvuliu_eksportas.csv#L8)

---
type: Table
title: "Banda — Užregistruotų gyvulių bandų ataskaita"
description: "Spinta table datasets/gov/zuikvc/bandos/Banda (6 columns)."
tags: [gov, zuikvc, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/bandos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/bandos.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# Banda — Užregistruotų gyvulių bandų ataskaita

- **Model:** `datasets/gov/zuikvc/bandos/Banda`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/bandos](../bandos.md) (`datasets/gov/zuikvc/bandos`)
- **Manifest CSV:** [datasets/gov/zuikvc/bandos.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/bandos.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `savivaldybe`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `galviju_bandu_sk` | `integer` | `U` | `4` | `open` | — | Galvijų bandų skaičius | — |
| `aviu_bandu_sk` | `integer` | `U` | `4` | `open` | — | Avių bandų skaičius | — |
| `ozku_bandu_sk` | `integer` | `U` | `4` | `open` | — | Ožkų bandų skaičius | — |
| `arkliu_bandu_sk` | `integer` | `U` | `4` | `open` | — | Arklių bandų skaičius | — |
| `kiauliu_bandu_sk` | `integer` | `U` | `4` | `open` | — | Kiaulių bandų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/bandos.csv

---
type: Table
title: "BanduGyvuliuSkaicius — Registruotų bandų ir gyvūlių skaičius savivaldybėse"
description: "Spinta table datasets/gov/zuikvc/bandos_gyvuliai/BanduGyvuliuSkaicius (9 columns)."
tags: [gov, zuikvc, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/bandos_gyvuliai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/bandos_gyvuliai.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# BanduGyvuliuSkaicius — Registruotų bandų ir gyvūlių skaičius savivaldybėse

- **Model:** `datasets/gov/zuikvc/bandos_gyvuliai/BanduGyvuliuSkaicius`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/bandos_gyvuliai](../bandos_gyvuliai.md) (`datasets/gov/zuikvc/bandos_gyvuliai`)
- **Manifest CSV:** [datasets/gov/zuikvc/bandos_gyvuliai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/bandos_gyvuliai.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `savivaldybe`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `galviju_bandu_sk` | `integer` | `U` | `4` | `open` | — | Galvijų bandų skaičius | — |
| `galviju_sk` | `integer` | `U` | `4` | `open` | — | Galvijų skaičius | — |
| `aviu_bandu_sk` | `integer` | `U` | `4` | `open` | — | Avių bandų skaičius | — |
| `aviu_sk` | `integer` | `U` | `4` | `open` | — | Avių skaičius | — |
| `ozku_bandu_sk` | `integer` | `U` | `4` | `open` | — | Ožkų bandų skaičius | — |
| `ozku_sk` | `integer` | `U` | `4` | `open` | — | Ožkų skaičius | — |
| `arkliu_bandu_sk` | `integer` | `U` | `4` | `open` | — | Arklių bandų skaičius | — |
| `arkliu_sk` | `integer` | `U` | `4` | `open` | — | Arklių skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/bandos_gyvuliai.csv

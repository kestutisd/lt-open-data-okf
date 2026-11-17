---
type: Table
title: "GyvuliuKritimas — Gyvulių kritimai"
description: "Spinta table datasets/gov/zuikvc/kritimai/GyvuliuKritimas (5 columns)."
tags: [gov, zuikvc, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/kritimai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/kritimai.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# GyvuliuKritimas — Gyvulių kritimai

- **Model:** `datasets/gov/zuikvc/kritimai/GyvuliuKritimas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/kritimai](../kritimai.md) (`datasets/gov/zuikvc/kritimai`)
- **Manifest CSV:** [datasets/gov/zuikvc/kritimai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/kritimai.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `savivaldybe`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `galviju_skaicius` | `integer` | `U` | `4` | `open` | — | Kritusių galvijų skaičius | — |
| `aviu_skaicius` | `integer` | `U` | `4` | `open` | — | Kritusių avių skaičius | — |
| `ozku_skaicius` | `integer` | `U` | `4` | `open` | — | Kritusių ožkų skaičius | — |
| `arkliu_skaicius` | `integer` | `U` | `4` | `open` | — | Kritusių arklių skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/kritimai.csv

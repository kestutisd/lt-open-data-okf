---
type: Table
title: "KiauliuLaikytojas — Kiaulių laikytojų ir kiaulių skaičius pagal ūkių dydį"
description: "Spinta table datasets/gov/zuikvc/kiauliu_laikytojai/KiauliuLaikytojas (13 columns)."
tags: [gov, zuikvc, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/kiauliu_laikytojai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/kiauliu_laikytojai.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# KiauliuLaikytojas — Kiaulių laikytojų ir kiaulių skaičius pagal ūkių dydį

- **Model:** `datasets/gov/zuikvc/kiauliu_laikytojai/KiauliuLaikytojas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/kiauliu_laikytojai](../kiauliu_laikytojai.md) (`datasets/gov/zuikvc/kiauliu_laikytojai`)
- **Manifest CSV:** [datasets/gov/zuikvc/kiauliu_laikytojai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/kiauliu_laikytojai.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `savivaldybe`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `laikytoju_1_10_kiauliu_sk` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 1 iki 10 kiaulių skaičius | — |
| `kiauliu_1_10_sk` | `integer` | `U` | `4` | `open` | — | Kiaulių, kurios laikomos pas asmenis, kurie laiko nuo 1 iki 10 kiaulių, skaičius | — |
| `laikytoju_11_100_kiauliu_sk` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 11 iki 100 kiaulių skaičius | — |
| `kiauliu_11_100_sk` | `integer` | `U` | `4` | `open` | — | Kiaulių, kurios laikomos pas asmenis, kurie laiko nuo 11 iki 100 kiaulių, skaičius | — |
| `laikytoju_101_500_kiauliu_sk` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 100 iki 500 kiaulių skaičius | — |
| `kiauliu_101_500_sk` | `integer` | `U` | `4` | `open` | — | Kiaulių, kurios laikomos pas asmenis, kurie laiko nuo 100 iki 500 kiaulių, skaičius | — |
| `laikytoju_501_1000_kiauliu_sk` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 501 iki 1000 kiaulių skaičius | — |
| `kiauliu_501_1000_sk` | `integer` | `U` | `4` | `open` | — | Kiaulių, kurios laikomos pas asmenis, kurie laiko nuo 501 iki 1000 kiaulių, skaičius | — |
| `laikytoju_virs_1000_kiauliu_sk` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 1001 kiaulių skaičius | — |
| `kiauliu_virs_1000_sk` | `integer` | `U` | `4` | `open` | — | Kiaulių, kurios laikomos pas asmenis, kurie laiko nuo 1001 kiaulių, skaičius | — |
| `kiauliu_laikytoju_sk` | `integer` | `U` | `4` | `open` | — | Kiaulių laikytojų skaičius | — |
| `kiauliu_sk` | `integer` | `U` | `4` | `open` | — | Kiaulių skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/kiauliu_laikytojai.csv

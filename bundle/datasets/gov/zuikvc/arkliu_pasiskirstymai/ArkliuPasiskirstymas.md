---
type: Table
title: "ArkliuPasiskirstymas — Arklių pasiskirstymas pagal savivaldybes"
description: "Spinta table datasets/gov/zuikvc/arkliu_pasiskirstymai/ArkliuPasiskirstymas (5 columns)."
tags: [gov, zuikvc, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/arkliu_pasiskirstymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/arkliu_pasiskirstymai.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# ArkliuPasiskirstymas — Arklių pasiskirstymas pagal savivaldybes

- **Model:** `datasets/gov/zuikvc/arkliu_pasiskirstymai/ArkliuPasiskirstymas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/arkliu_pasiskirstymai](../arkliu_pasiskirstymai.md) (`datasets/gov/zuikvc/arkliu_pasiskirstymai`)
- **Manifest CSV:** [datasets/gov/zuikvc/arkliu_pasiskirstymai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/arkliu_pasiskirstymai.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `savivaldybe`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `arkliu_sk` | `integer` | `U` | `4` | `open` | — | Arklių skaičius | — |
| `arkliu_laik_sk` | `integer` | `U` | `4` | `open` | — | Arklių laikytojų skaičius | — |
| `veisliniu_arkliu_sk` | `integer` | `U` | `4` | `open` | — | Veislinių arklių skaičius | — |
| `neveisliniu_arkliu_sk` | `integer` | `U` | `4` | `open` | — | Neveislinių arklių skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/arkliu_pasiskirstymai.csv

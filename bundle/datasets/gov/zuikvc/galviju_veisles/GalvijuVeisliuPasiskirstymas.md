---
type: Table
title: "GalvijuVeisliuPasiskirstymas — Gavlijų pasiskirstymas pagal veisles"
description: "Spinta table datasets/gov/zuikvc/galviju_veisles/GalvijuVeisliuPasiskirstymas (8 columns)."
tags: [gov, zuikvc, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/galviju_veisles.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galviju_veisles.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# GalvijuVeisliuPasiskirstymas — Gavlijų pasiskirstymas pagal veisles

- **Model:** `datasets/gov/zuikvc/galviju_veisles/GalvijuVeisliuPasiskirstymas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/galviju_veisles](../galviju_veisles.md) (`datasets/gov/zuikvc/galviju_veisles`)
- **Manifest CSV:** [datasets/gov/zuikvc/galviju_veisles.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galviju_veisles.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `savivaldybe`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Gyvūno bandos savivaldybės pavadinimas | — |
| `galv_zal` | `integer` | `U` | `4` | `open` | — | Žalųjų veislių galvijų skaičius | — |
| `galv_juod` | `integer` | `U` | `4` | `open` | — | Juodmargių veislių galvijų skaičius | — |
| `galv_kit` | `integer` | `U` | `4` | `open` | — | Kitų pieninių veislių galvijų skaičius | — |
| `galv_mes` | `integer` | `U` | `4` | `open` | — | Mėsinių veislių galvijų skaičius | — |
| `galv_misr` | `integer` | `U` | `4` | `open` | — | Mišrūnų veislių galvijų skaičius | — |
| `galv_viet` | `integer` | `U` | `4` | `open` | — | Vietinių veislių galvijų skaičius | — |
| `galv_vis` | `integer` | `U` | `4` | `open` | — | Visų veislių galvijų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/galviju_veisles.csv

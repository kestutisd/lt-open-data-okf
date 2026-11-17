---
type: Table
title: "GalvijuPasiskirstymasZub — Galvijų pasiskirstymas pagal savivaldybes įmonėse"
description: "Spinta table datasets/gov/zuikvc/galviju_pasiskirstymai_zub/GalvijuPasiskirstymasZub (5 columns)."
tags: [gov, zuikvc, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/galviju_pasiskirstymai_zub.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galviju_pasiskirstymai_zub.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# GalvijuPasiskirstymasZub — Galvijų pasiskirstymas pagal savivaldybes įmonėse

- **Model:** `datasets/gov/zuikvc/galviju_pasiskirstymai_zub/GalvijuPasiskirstymasZub`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/galviju_pasiskirstymai_zub](../galviju_pasiskirstymai_zub.md) (`datasets/gov/zuikvc/galviju_pasiskirstymai_zub`)
- **Manifest CSV:** [datasets/gov/zuikvc/galviju_pasiskirstymai_zub.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galviju_pasiskirstymai_zub.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `savivaldybe`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Gyvūno bandos savivaldybės pavadinimas | — |
| `asmenys_laikantys_galvijus` | `integer` | `U` | `4` | `open` | — | Juridinių asmenų, kurie laiko galvijus savivaldybėje, skaičius | — |
| `galviju_sk` | `integer` | `U` | `4` | `open` | — | Galvijų skaičius | — |
| `asmenys_laikantys_pienines_karves` | `integer` | `U` | `4` | `open` | — | Juridinių asmenų, kurie laiko pieninių veislių karves savivaldybėje, skaičius | — |
| `pieniniu_karviu_sk` | `integer` | `U` | `4` | `open` | — | Pieninių veislių karvių skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/galviju_pasiskirstymai_zub.csv

---
type: Table
title: "LaikytojaiBandaVieta — Laikytojų, bandų ir laikymo vietų skaičius"
description: "Spinta table datasets/gov/zuikvc/laikytojai_bandos_vietos/LaikytojaiBandaVieta (4 columns)."
tags: [gov, zuikvc, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/laikytojai_bandos_vietos.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/laikytojai_bandos_vietos.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# LaikytojaiBandaVieta — Laikytojų, bandų ir laikymo vietų skaičius

- **Model:** `datasets/gov/zuikvc/laikytojai_bandos_vietos/LaikytojaiBandaVieta`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/laikytojai_bandos_vietos](../laikytojai_bandos_vietos.md) (`datasets/gov/zuikvc/laikytojai_bandos_vietos`)
- **Manifest CSV:** [datasets/gov/zuikvc/laikytojai_bandos_vietos.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/laikytojai_bandos_vietos.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `savivaldybe`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |
| `laikytoju_skaicius` | `integer` | `U` | `4` | `open` | — | Laikytojų skaičius | — |
| `bandu_skaicius` | `integer` | `U` | `4` | `open` | — | Bandų skaičius | — |
| `laikymo_vietu_skaicius` | `integer` | `U` | `4` | `open` | — | Laikymo vietų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/laikytojai_bandos_vietos.csv

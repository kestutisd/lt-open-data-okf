---
type: Table
title: "AviuOzkuLyciuPasiskirstymas — Aviu ir ožkų pasiskirstymas pagal lytis"
description: "Spinta table datasets/gov/zuikvc/aviu_ozku_lytys/AviuOzkuLyciuPasiskirstymas (7 columns)."
tags: [gov, zuikvc, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/aviu_ozku_lytys.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/aviu_ozku_lytys.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# AviuOzkuLyciuPasiskirstymas — Aviu ir ožkų pasiskirstymas pagal lytis

- **Model:** `datasets/gov/zuikvc/aviu_ozku_lytys/AviuOzkuLyciuPasiskirstymas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/aviu_ozku_lytys](../aviu_ozku_lytys.md) (`datasets/gov/zuikvc/aviu_ozku_lytys`)
- **Manifest CSV:** [datasets/gov/zuikvc/aviu_ozku_lytys.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/aviu_ozku_lytys.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `savivaldybe`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Gyvūno bandos savivaldybės pavadinimas | — |
| `avys_vyr` | `integer` | `U` | `4` | `open` | — | Vyriškosios lyties avių skaičius | — |
| `avys_mot` | `integer` | `U` | `4` | `open` | — | Moteriškosios lyties avių skaičius | — |
| `avys_eriavedes` | `integer` | `U` | `4` | `open` | — | Ėriavedžių skaičius | — |
| `ozkos_vyr` | `integer` | `U` | `4` | `open` | — | Vyriškosios lyties ožkų skaičius | — |
| `ozkos_mot` | `integer` | `U` | `4` | `open` | — | Moteriškosios lyties ožkų skaičius | — |
| `ozkos_ozkavedes` | `integer` | `U` | `4` | `open` | — | Ožkavedžių skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/aviu_ozku_lytys.csv

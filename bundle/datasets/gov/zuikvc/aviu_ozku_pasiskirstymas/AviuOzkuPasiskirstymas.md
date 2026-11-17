---
type: Table
title: "AviuOzkuPasiskirstymas — Aviu ir ožkų laikytojų pasiskirstymas"
description: "Spinta table datasets/gov/zuikvc/aviu_ozku_pasiskirstymas/AviuOzkuPasiskirstymas (7 columns)."
tags: [gov, zuikvc, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/aviu_ozku_pasiskirstymas.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/aviu_ozku_pasiskirstymas.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# AviuOzkuPasiskirstymas — Aviu ir ožkų laikytojų pasiskirstymas

- **Model:** `datasets/gov/zuikvc/aviu_ozku_pasiskirstymas/AviuOzkuPasiskirstymas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/aviu_ozku_pasiskirstymas](../aviu_ozku_pasiskirstymas.md) (`datasets/gov/zuikvc/aviu_ozku_pasiskirstymas`)
- **Manifest CSV:** [datasets/gov/zuikvc/aviu_ozku_pasiskirstymas.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/aviu_ozku_pasiskirstymas.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `savivaldybe`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Gyvūno bandos savivaldybės pavadinimas | — |
| `avys_laik` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko avis, skaičius | — |
| `avys` | `integer` | `U` | `4` | `open` | — | Avių skaičius | — |
| `ozkos_laik` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko ožkas, skaičius | — |
| `ozkos` | `integer` | `U` | `4` | `open` | — | Ožkų skaičius | — |
| `avys_ozkos_laik` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko avis arba ožkos, skaičius | — |
| `avys_ozkos` | `integer` | `U` | `4` | `open` | — | Avių ir ožkų skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/aviu_ozku_pasiskirstymas.csv

---
type: Table
title: "AviuUkiuPasiskirstymas — Ūkių pasiskirstymas pagal avių skaičių"
description: "Spinta table datasets/gov/zuikvc/aviu_ukiai/AviuUkiuPasiskirstymas (19 columns)."
tags: [gov, zuikvc, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/aviu_ukiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/aviu_ukiai.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# AviuUkiuPasiskirstymas — Ūkių pasiskirstymas pagal avių skaičių

- **Model:** `datasets/gov/zuikvc/aviu_ukiai/AviuUkiuPasiskirstymas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/aviu_ukiai](../aviu_ukiai.md) (`datasets/gov/zuikvc/aviu_ukiai`)
- **Manifest CSV:** [datasets/gov/zuikvc/aviu_ukiai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/aviu_ukiai.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `savivaldybe`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Gyvūno bandos savivaldybės pavadinimas | — |
| `laik_avys_1_2` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko 1 arba 2 avis, skaičius | — |
| `avys_1_2` | `integer` | `U` | `4` | `open` | — | Avių, kurios laikomos pas asmenis, kurie laiko 1 arba 2 avis, skaičius | — |
| `laik_avys_3_5` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 3 iki 5 avių, skaičius | — |
| `avys_3_5` | `integer` | `U` | `4` | `open` | — | Avių, kurios laikomos pas asmenis, kurie laiko nuo 3 iki 5 avių, skaičius | — |
| `laik_avys_6_10` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 6 iki 10 avių, skaičius | — |
| `avys_6_10` | `integer` | `U` | `4` | `open` | — | Avių, kurios laikomos pas asmenis, kurie laiko nuo 6 iki 10 avių, skaičius | — |
| `laik_avys_11_20` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 11 iki 20 avių, skaičius | — |
| `avys_11_20` | `integer` | `U` | `4` | `open` | — | Avių, kurios laikomos pas asmenis, kurie laiko nuo 11 iki 20 avių, skaičius | — |
| `laik_avys_21_30` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 21 iki 30 avių, skaičius | — |
| `avys_21_30` | `integer` | `U` | `4` | `open` | — | Avių, kurios laikomos pas asmenis, kurie laiko nuo 21 iki 30 avių, skaičius | — |
| `laik_avys_31_50` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 31 iki 50 avių, skaičius | — |
| `avys_31_50` | `integer` | `U` | `4` | `open` | — | Avių, kurios laikomos pas asmenis, kurie laiko nuo 31 iki 50 avių, skaičius | — |
| `laik_avys_51_100` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 51 iki 100 avių, skaičius | — |
| `avys_51_100` | `integer` | `U` | `4` | `open` | — | Avių, kurios laikomos pas asmenis, kurie laiko nuo 51 iki 100 avių, skaičius | — |
| `laik_avys_101_150` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 101 iki 150 avių, skaičius | — |
| `avys_101_150` | `integer` | `U` | `4` | `open` | — | Avių, kurios laikomos pas asmenis, kurie laiko nuo 101 iki 150 avių, skaičius | — |
| `laik_avys_151` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 151 avių, skaičius | — |
| `avys_151` | `integer` | `U` | `4` | `open` | — | Avių, kurios laikomos pas asmenis, kurie laiko nuo 151 avių, skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/aviu_ukiai.csv

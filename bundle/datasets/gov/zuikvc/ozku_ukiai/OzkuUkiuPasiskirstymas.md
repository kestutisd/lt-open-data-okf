---
type: Table
title: "OzkuUkiuPasiskirstymas — Ūkių pasiskirstymas pagal ožkų skaičių"
description: "Spinta table datasets/gov/zuikvc/ozku_ukiai/OzkuUkiuPasiskirstymas (19 columns)."
tags: [gov, zuikvc, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/ozku_ukiai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/ozku_ukiai.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# OzkuUkiuPasiskirstymas — Ūkių pasiskirstymas pagal ožkų skaičių

- **Model:** `datasets/gov/zuikvc/ozku_ukiai/OzkuUkiuPasiskirstymas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/ozku_ukiai](../ozku_ukiai.md) (`datasets/gov/zuikvc/ozku_ukiai`)
- **Manifest CSV:** [datasets/gov/zuikvc/ozku_ukiai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/ozku_ukiai.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `savivaldybe`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Gyvūno bandos savivaldybės pavadinimas | — |
| `laik_ozkos_1_2` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko 1 arba 2 ožkas, skaičius | — |
| `ozkos_1_2` | `integer` | `U` | `4` | `open` | — | Ožkų, kurios laikomos pas asmenis, kurie laiko 1 arba 2 ožkas, skaičius | — |
| `laik_ozkos_3_5` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 3 iki 5 ožkų, skaičius | — |
| `ozkos_3_5` | `integer` | `U` | `4` | `open` | — | Ožkų, kurios laikomos pas asmenis, kurie laiko nuo 3 iki 5 ožkų, skaičius | — |
| `laik_ozkos_6_10` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 6 iki 10 ožkų, skaičius | — |
| `ozkos_6_10` | `integer` | `U` | `4` | `open` | — | Ožkų, kurios laikomos pas asmenis, kurie laiko nuo 6 iki 10 ožkų, skaičius | — |
| `laik_ozkos_11_20` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 11 iki 20 ožkų, skaičius | — |
| `ozkos_11_20` | `integer` | `U` | `4` | `open` | — | Ožkų, kurios laikomos pas asmenis, kurie laiko nuo 11 iki 20 ožkų, skaičius | — |
| `laik_ozkos_21_30` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 21 iki 30 ožkų, skaičius | — |
| `ozkos_21_30` | `integer` | `U` | `4` | `open` | — | Ožkų, kurios laikomos pas asmenis, kurie laiko nuo 21 iki 30 ožkų, skaičius | — |
| `laik_ozkos_31_50` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 31 iki 50 ožkų, skaičius | — |
| `ozkos_31_50` | `integer` | `U` | `4` | `open` | — | Ožkų, kurios laikomos pas asmenis, kurie laiko nuo 31 iki 50 ožkų, skaičius | — |
| `laik_ozkos_51_100` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 51 iki 100 ožkų, skaičius | — |
| `ozkos_51_100` | `integer` | `U` | `4` | `open` | — | Ožkų, kurios laikomos pas asmenis, kurie laiko nuo 51 iki 100 ožkų, skaičius | — |
| `laik_ozkos_101_150` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 101 iki 150 ožkų, skaičius | — |
| `ozkos_101_150` | `integer` | `U` | `4` | `open` | — | Ožkų, kurios laikomos pas asmenis, kurie laiko nuo 101 iki 150 ožkų, skaičius | — |
| `laik_ozkos_151` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko nuo 151 ožkų, skaičius | — |
| `ozkos_151` | `integer` | `U` | `4` | `open` | — | Ožkų, kurios laikomos pas asmenis, kurie laiko nuo 151 ožkų, skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/ozku_ukiai.csv

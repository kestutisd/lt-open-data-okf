---
type: Table
title: "TelyciosKarvesAmzius — Mėsinių ir mišrūnų veislių telyčių ir karvių pasiskirstymas pagal amžiaus grupes"
description: "Spinta table datasets/gov/zuikvc/telyciu_karviu_amzius/TelyciosKarvesAmzius (12 columns)."
tags: [gov, zuikvc, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/telyciu_karviu_amzius.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/telyciu_karviu_amzius.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# TelyciosKarvesAmzius — Mėsinių ir mišrūnų veislių telyčių ir karvių pasiskirstymas pagal amžiaus grupes

- **Model:** `datasets/gov/zuikvc/telyciu_karviu_amzius/TelyciosKarvesAmzius`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/telyciu_karviu_amzius](../telyciu_karviu_amzius.md) (`datasets/gov/zuikvc/telyciu_karviu_amzius`)
- **Manifest CSV:** [datasets/gov/zuikvc/telyciu_karviu_amzius.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/telyciu_karviu_amzius.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `savivaldybe`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Gyvūno bandos savivaldybės pavadinimas | — |
| `laik` | `integer` | `U` | `4` | `open` | — | Asmenų, kurie laiko mėsinių arba mišrūnų veislių telyčias arba karves | — |
| `tel_0_8_mes` | `integer` | `U` | `4` | `open` | — | Mėsinių veislių telyčių iki 8 mėnesių amžiaus skaičius | — |
| `tel_0_8_mis` | `integer` | `U` | `4` | `open` | — | Mišrūnų veislių telyčių iki 8 mėnesių amžiaus skaičius | — |
| `tel_8_12_mes` | `integer` | `U` | `4` | `open` | — | Mėsinių veislių telyčių nuo 8 iki 12 mėnesių amžiaus skaičius | — |
| `tel_8_12_mis` | `integer` | `U` | `4` | `open` | — | Mišrūnų veislių telyčių nuo 8 iki 12 mėnesių amžiaus skaičius | — |
| `tel_12_24_mes` | `integer` | `U` | `4` | `open` | — | Mėsinių veislių telyčių nuo 12 iki 24 mėnesių amžiaus skaičius | — |
| `tel_12_24_mis` | `integer` | `U` | `4` | `open` | — | Mišrūnų veislių telyčių nuo 12 iki 24 mėnesių amžiaus skaičius | — |
| `tel_24_mes` | `integer` | `U` | `4` | `open` | — | Mėsinių veislių telyčių nuo 24 mėnesių amžiaus skaičius | — |
| `tel_24_mis` | `integer` | `U` | `4` | `open` | — | Mišrūnų veislių telyčių nuo 24 mėnesių amžiaus skaičius | — |
| `karv_mes` | `integer` | `U` | `4` | `open` | — | Mėsinių veislių karvių skaičius | — |
| `karv_mis` | `integer` | `U` | `4` | `open` | — | Mišrūnų veislių karvių skaičius | — |

# Comments

| Target | Prepare | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `create(property: "savivaldybe", type: "ref", ref: "/datasets/gov/rc/ar/savivaldybe/Savivaldybe")` | `type` | `2` | `open` | — | — | — |
| `savivaldybe` | `update(property: "savivaldybe.pavadinimas", type: "")` | `type` | `2` | `open` | — | — | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/telyciu_karviu_amzius.csv

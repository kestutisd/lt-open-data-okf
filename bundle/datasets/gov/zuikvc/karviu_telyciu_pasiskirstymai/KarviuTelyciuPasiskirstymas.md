---
type: Table
title: "KarviuTelyciuPasiskirstymas — Karvių ir telyčių pasiskirstymas"
description: "Spinta table datasets/gov/zuikvc/karviu_telyciu_pasiskirstymai/KarviuTelyciuPasiskirstymas (10 columns)."
tags: [gov, zuikvc, undeployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/karviu_telyciu_pasiskirstymai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/karviu_telyciu_pasiskirstymai.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# KarviuTelyciuPasiskirstymas — Karvių ir telyčių pasiskirstymas

- **Model:** `datasets/gov/zuikvc/karviu_telyciu_pasiskirstymai/KarviuTelyciuPasiskirstymas`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/karviu_telyciu_pasiskirstymai](../karviu_telyciu_pasiskirstymai.md) (`datasets/gov/zuikvc/karviu_telyciu_pasiskirstymai`)
- **Manifest CSV:** [datasets/gov/zuikvc/karviu_telyciu_pasiskirstymai.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/karviu_telyciu_pasiskirstymai.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `savivaldybe`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `savivaldybe` | `string` | — | `2` | `open` | — | Gyvūno bandos savivaldybės pavadinimas | — |
| `karv_visos` | `integer` | `U` | `4` | `open` | — | Visų veislių karvių skaičius | — |
| `karv_zal` | `integer` | `U` | `4` | `open` | — | Žalųjų veislių karvių skaičius | — |
| `karv_juod` | `integer` | `U` | `4` | `open` | — | Juodmargių veislių karvių skaičius | — |
| `karv_kit` | `integer` | `U` | `4` | `open` | — | Kitų pieninių veislių karvių skaičius | — |
| `karv_mes` | `integer` | `U` | `4` | `open` | — | Mėsinių veislių karvių skaičius | — |
| `karv_misr` | `integer` | `U` | `4` | `open` | — | Mišrūnų veislių karvių skaičius | — |
| `karv_viet` | `integer` | `U` | `4` | `open` | — | Vietinių veislių karvių skaičius | — |
| `tel_mes` | `integer` | `U` | `4` | `open` | — | Mėsinių veislių telyčių skaičius | — |
| `tel_misr` | `integer` | `U` | `4` | `open` | — | Mišrūnų veislių telyčių skaičius | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/karviu_telyciu_pasiskirstymai.csv

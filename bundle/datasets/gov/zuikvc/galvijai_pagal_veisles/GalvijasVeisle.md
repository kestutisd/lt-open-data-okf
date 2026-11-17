---
type: Table
title: "GalvijasVeisle — Mėsinių ir mėsinių mišrūnų galvijų pasiskirstymas pagal veisles"
description: "Spinta table datasets/gov/zuikvc/galvijai_pagal_veisles/GalvijasVeisle (4 columns)."
tags: [gov, zuikvc, undeployed, level-3]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/zuikvc/galvijai_pagal_veisles.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galvijai_pagal_veisles.csv#L8"
    last_modified: "2026-11-11T14:39:20Z"
---

# GalvijasVeisle — Mėsinių ir mėsinių mišrūnų galvijų pasiskirstymas pagal veisles

- **Model:** `datasets/gov/zuikvc/galvijai_pagal_veisles/GalvijasVeisle`[^manifest]
- **Dataset:** [datasets/gov/zuikvc/galvijai_pagal_veisles](../galvijai_pagal_veisles.md) (`datasets/gov/zuikvc/galvijai_pagal_veisles`)
- **Manifest CSV:** [datasets/gov/zuikvc/galvijai_pagal_veisles.csv#L8](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/zuikvc/galvijai_pagal_veisles.csv#L8)
- **Saugykla (`get_data_gov_lt.in`):** Not listed in `get_data_gov_lt.in`
- **Primary Key (`ref`):** `veisle`
- **Level:** `3`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `veisle` | `string` | — | `3` | `open` | — | Veislė | — |
| `veisles_kodas` | `string` | — | `4` | `open` | — | Veislės kodas pagal Ūkinių gyvūnų registrą | — |
| `lytis` | `string` | — | `4` | `open` | — | Galvijo lytis | — |
| `gyvunus_skaicius` | `integer` | `U` | `4` | `open` | — | Gyvulių skaičius | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `lytis` | `"Buliukas"` | — | — | Buliukas | — |
| `lytis` | `"Karvė"` | — | — | Karvė | — |
| `lytis` | `"Telyčaitė"` | — | — | Telyčaitė | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/zuikvc/galvijai_pagal_veisles.csv

---
type: Table
title: "Pasiskirstymas — Jonizuojančiosios spinduliuotės generatorių pasiskirstymas"
description: "Spinta table datasets/gov/rsc/generatoriai/Pasiskirstymas (9 columns)."
resource: "https://get.data.gov.lt/datasets/gov/rsc/generatoriai/Pasiskirstymas"
tags: [gov, rsc, deployed, level-2]
generated: { by: "lt-open-data-okf/0.2.0", at: "2026-11-11T14:39:20Z" }
sources:
  - id: manifest
    title: "atviriduomenys/manifest — datasets/gov/rsc/generatoriai.csv"
    resource: "https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/generatoriai.csv#L4"
    last_modified: "2026-11-11T14:39:20Z"
---

# Pasiskirstymas — Jonizuojančiosios spinduliuotės generatorių pasiskirstymas

- **Model:** `datasets/gov/rsc/generatoriai/Pasiskirstymas`[^manifest]
- **Dataset:** [datasets/gov/rsc/generatoriai](../generatoriai.md) (`datasets/gov/rsc/generatoriai`)
- **Manifest CSV:** [datasets/gov/rsc/generatoriai.csv#L4](https://github.com/atviriduomenys/manifest/blob/ec54998dcea52a0d26dc1c172eacec438d47e727/datasets/gov/rsc/generatoriai.csv#L4)
- **Saugykla (`get_data_gov_lt.in`):** `https://get.data.gov.lt/datasets/gov/rsc/generatoriai/Pasiskirstymas`
- **Level:** `2`

# Schema

| Property | Type | Ref | Level | Access | URI | Title | Description |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `id` | `string` | — | `4` | `open` | — | Generatoriaus identifikatorius | — |
| `pagaminta` | `date` | `D` | `4` | `open` | — | Generatoriaus pagaminimo data | — |
| `statusas` | `string` | — | `4` | `open` | — | Generatoriaus statusas | — |
| `model_pav` | `string` | — | `4` | `open` | — | Generatoriaus modelio pavadinimas | — |
| `montav_busena` | `string` | — | `4` | `open` | — | Generatoriaus sumontavimo būsena | — |
| `panaud_busena` | `string` | — | `4` | `open` | — | Panaudojimo būsenos pavadinimas | — |
| `veiklos_pav` | `string` | — | `4` | `open` | — | Veiklos pavadinimas | Pateikiami tik medicinoje naudojami generatoriai |
| `tipas` | `string` | — | `3` | `open` | — | Generatoriaus tipo pavadinimas | — |
| `savivaldybe` | `string` | — | `2` | `open` | — | Savivaldybės pavadinimas | — |

# Enumerations

| Property | Value (`prepare`) | Source | Access | Title | Description |
| --- | --- | --- | --- | --- | --- |
| `statusas` | `"eksploatuojamas"` | — | — | Generatorius eksploatuojamas | — |
| `statusas` | `"utilizuotas"` | — | — | Generatorius utilizuotas | — |
| `montav_busena` | `"Sumontuotas"` | — | — | Sumontuotas | — |
| `montav_busena` | `"Išmontuotas"` | — | — | Išmontuotas | — |
| `montav_busena` | `"Mobilus"` | — | — | Mobilus | — |
| `panaud_busena` | `"Nežinoma"` | — | — | Nežinoma | — |
| `panaud_busena` | `"Sandėliuojamas"` | — | — | Sandėliuojamas | — |
| `panaud_busena` | `"Saugomas"` | — | — | Saugomas | — |
| `panaud_busena` | `"Naudojamas"` | — | — | Naudojamas | — |

[^manifest]: atviriduomenys/manifest — datasets/gov/rsc/generatoriai.csv
